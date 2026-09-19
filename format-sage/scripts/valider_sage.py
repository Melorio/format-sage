#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
valider_sage.py — Controle d'un fichier d'import Sage 100 avant livraison.

Couvre la Comptabilite (#VER 31), la Gestion commerciale (#VER 33) et les Immobilisations
(#VER 23). Le module est lu sur la ligne #VER du fichier, et recoupe avec les drapeaux presents.

Verifie : en-tete, #FIN, encodage reel des octets, absence de LF isole, nombre de champs
par bloc, ligne vide de separation la ou elle est requise, et — pour #MECG — l'equilibre
debit/credit global et par journal.

    python valider_sage.py QUANTUM_MECG_20260822.txt

Code retour 0 si le fichier est livrable, 1 sinon.
"""

import argparse
import sys
from decimal import Decimal, InvalidOperation

try:
    from formats_sage import (TABLES, ENTETES, VERSIONS, ENCODAGE, FIN, PARENTS,
                              NOMS_MODULE, controler_caracteres,
                              module_du_fichier)
except ImportError:  # execution depuis un autre repertoire
    import os
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from formats_sage import (TABLES, ENTETES, VERSIONS, ENCODAGE, FIN, PARENTS,
                              NOMS_MODULE, controler_caracteres,
                              module_du_fichier)

# Position (1-based) des champs utiles au controle d'equilibre dans un bloc #MECG
MECG_CHAMP_JOURNAL = 1
MECG_CHAMP_SENS = 17
MECG_CHAMP_MONTANT = 18


def _montant(texte):
    """Convertit un montant Sage ('1 200,50') en Decimal. Renvoie None si non convertible."""
    nettoye = texte.replace(" ", "").replace("\u00a0", "").replace(",", ".")
    if not nettoye:
        return Decimal("0")
    try:
        return Decimal(nettoye)
    except InvalidOperation:
        return None


def valider(chemin):
    anomalies = []
    avertissements = []
    infos = []

    with open(chemin, "rb") as flux:
        octets = flux.read()

    if not octets:
        return ["Fichier vide."], [], []

    # --- Fins de ligne -------------------------------------------------------
    nb_lf = octets.count(b"\n")
    nb_crlf = octets.count(b"\r\n")
    isoles = nb_lf - nb_crlf
    if isoles > 0:
        # Un LF isole est presque toujours une erreur de generation. Il existe pourtant un cas
        # legitime : le champ Formule d'une information libre #MINF, ou Sage exporte lui-meme du
        # code multiligne. On signale sans interrompre l'analyse, qui reste valide puisque le
        # decoupage se fait sur CRLF et que le LF isole demeure a l'interieur d'un champ.
        message = ("Fins de ligne : %d LF dont %d en CRLF, soit %d LF isole(s). Legitime "
                   "uniquement a l'interieur d'un champ multiligne (formule #MINF exportee par "
                   "Sage). Dans un fichier genere, c'est une anomalie : regenerer avec "
                   "ecrire_sage.py plutot que corriger a la main." % (nb_lf, nb_crlf, isoles))
        avertissements.append(message)
    else:
        infos.append("Fins de ligne : CRLF sur les %d lignes." % nb_crlf)

    # --- Encodage ------------------------------------------------------------
    encodages_valides = []
    for encodage in ("cp850", "cp1252", "utf-8"):
        try:
            octets.decode(encodage)
            encodages_valides.append(encodage)
        except UnicodeDecodeError:
            pass
    if not encodages_valides:
        return anomalies + ["Encodage illisible en CP850, CP1252 et UTF-8."], [], infos

    # Decodage de travail en CP850, encodage reel du format.
    texte = octets.decode(ENCODAGE, errors="replace")
    lignes = texte.split("\r\n")
    if lignes and lignes[-1] == "":
        lignes.pop()

    # --- Fin de fichier ------------------------------------------------------
    if lignes[-1] != FIN:
        anomalies.append("Derniere ligne : '%s' au lieu de '%s'." % (lignes[-1], FIN))

    # --- Decoupage en blocs --------------------------------------------------
    positions = [i for i, ligne in enumerate(lignes)
                 if ligne.startswith("#") and ligne.strip() != ""]
    blocs = []
    for debut, suivant in zip(positions, positions[1:]):
        drapeau = lignes[debut].split()[0].lstrip("#")
        if drapeau in ("FLG", "VER", "DEV", "FIN"):
            continue
        blocs.append((debut + 1, drapeau, lignes[debut + 1:suivant]))

    if not blocs:
        anomalies.append("Aucun bloc de donnees trouve entre l'en-tete et #FIN.")
        return anomalies, avertissements, infos

    # --- Module et en-tete ---------------------------------------------------
    version = lignes[1] if len(lignes) > 1 else ""
    module_entete = VERSIONS.get(version)
    try:
        module_drapeaux = module_du_fichier({d for _, d, _ in blocs})
    except ValueError as err:
        anomalies.append(str(err))
        module_drapeaux = None
    if module_entete and module_drapeaux and module_entete != module_drapeaux:
        anomalies.append(
            "Incoherence : l'en-tete annonce %s (%s) mais les drapeaux presents relevent de %s. "
            "Les cardinalites des drapeaux partages different d'un module a l'autre : l'import "
            "decalera les champs." % (module_entete, version, module_drapeaux))
    module = module_entete or module_drapeaux or "CPTA"
    FORMATS = TABLES[module]
    attendu = ENTETES[module]
    if lignes[:len(attendu)] != attendu:
        anomalies.append(
            "En-tete incorrect : attendu %s (module deduit des drapeaux presents), trouve %s."
            % (attendu, lignes[:3]))
    else:
        infos.append("Module : %s, en-tete %s."
                     % (NOMS_MODULE[module], " / ".join(attendu)))
    if module != "CPTA" and "#DEV EUR" in lignes[:4]:
        anomalies.append(
            "Ligne #DEV EUR hors Comptabilite : rejet \"Fichier inconnu ligne : 3\" a "
            "l'import. La supprimer.")

    # --- Encodage ------------------------------------------------------------
    if ENCODAGE not in encodages_valides:
        anomalies.append("Fichier non decodable en CP850, seul encodage accepte par Sage 100.")
    elif not any(o > 127 for o in octets):
        infos.append("Encodage : CP850 (aucun caractere accentue, donc non discriminant).")
    else:
        extraits = [l for l in texte.split("\r\n") if any(ord(c) > 127 for c in l)][:2]
        infos.append("Encodage : CP850 — controle visuel des accents : %s" % " | ".join(extraits))
        avertissements.append(
            "Le fichier contient des accents : relire l'extrait ci-dessus. Des caracteres du "
            "type 'Cr,dit' au lieu de 'Credit' trahissent une source CP1252 mal convertie."
        )

    # --- Controle bloc par bloc ---------------------------------------------
    compte = {}
    for numero_ligne, drapeau, corps in blocs:
        compte[drapeau] = compte.get(drapeau, 0) + 1
        if drapeau not in FORMATS:
            avertissements.append(
                "Ligne %d : drapeau #%s non couvert par cette skill, structure non verifiee."
                % (numero_ligne, drapeau)
            )
            continue

        spec = FORMATS[drapeau]
        champs = list(corps)

        if spec["separateur"]:
            if not champs or champs[-1] != "":
                anomalies.append(
                    "Ligne %d (#%s) : ligne vide de separation absente apres le dernier champ."
                    % (numero_ligne, drapeau)
                )
            else:
                champs = champs[:-1]

        if spec["nb_lignes"] is not None and len(champs) != spec["nb_lignes"]:
            anomalies.append(
                "Ligne %d (#%s) : %d champs, %d attendus."
                % (numero_ligne, drapeau, len(champs), spec["nb_lignes"])
            )
        elif len(champs) < spec["min_lignes"]:
            anomalies.append(
                "Ligne %d (#%s) : %d champs, minimum %d."
                % (numero_ligne, drapeau, len(champs), spec["min_lignes"])
            )

    # --- Caracteres refuses par Sage ----------------------------------------
    for numero_ligne, drapeau, corps in blocs:
        for position, libelle, valeur in controler_caracteres(module, drapeau, corps):
            anomalies.append(
                "Ligne %d (#%s champ %d, %s) : '%s' contient un caractere non alphanumerique. "
                "Sage refuse l'enregistrement avec le message \"Une incoherence a la ligne %d a "
                "ete detectee\" — le numero designe la ligne physique du fichier."
                % (numero_ligne + position, drapeau, position, libelle, valeur,
                   numero_ligne + position))

    infos.append("Blocs : %s." % ", ".join("#%s x%d" % (d, n) for d, n in sorted(compte.items())))

    if module == "IMMO" and "IIMO" in compte:
        infos.append("Immobilisations : %d #IIMO, %d #IPLAN, %d #ILOY."
                     % (compte.get("IIMO", 0), compte.get("IPLAN", 0), compte.get("ILOY", 0)))
        if not compte.get("IPLAN"):
            avertissements.append(
                "Aucun bloc #IPLAN : les immobilisations seront importees sans plan "
                "d'amortissement. Verifier que c'est bien l'intention.")

    # --- Drapeaux "table" : une seule occurrence autorisee -------------------
    for drapeau, nombre in sorted(compte.items()):
        spec = FORMATS.get(drapeau)
        if spec and spec.get("type", "").startswith("table") and nombre > 1:
            anomalies.append(
                "#%s est une %s : le drapeau doit apparaitre une seule fois, suivi du groupe "
                "repete a plat. Il apparait %d fois." % (drapeau, spec["type"], nombre))

    # --- Filiation parent / enfant ------------------------------------------
    precedent = None
    parent_courant = None
    for numero_ligne, drapeau, _ in blocs:
        attendus = PARENTS.get(drapeau)
        if attendus:
            if parent_courant not in attendus:
                avertissements.append(
                    "Ligne %d : #%s doit suivre %s ; le dernier enregistrement ouvert est %s."
                    % (numero_ligne, drapeau, " ou ".join("#" + p for p in attendus),
                       "#" + parent_courant if parent_courant else "l'en-tete"))
        elif drapeau in {p for parents in PARENTS.values() for p in parents}:
            parent_courant = drapeau
        precedent = drapeau

    non_eprouves = sorted(d for d in compte if d in FORMATS and FORMATS[d]["fiabilite"] != "eprouve")
    if non_eprouves:
        avertissements.append(
            "Formats non eprouves en production : %s. Import a tester sur un dossier d'essai."
            % ", ".join("#" + d for d in non_eprouves))

    # --- Equilibre debit / credit (MECG) ------------------------------------
    ecritures = [(n, c) for n, d, c in blocs if d == "MECG"]
    if ecritures:
        total_debit = Decimal("0")
        total_credit = Decimal("0")
        par_journal = {}

        for numero_ligne, corps in ecritures:
            champs = corps[:-1] if corps and corps[-1] == "" else corps
            if len(champs) < MECG_CHAMP_MONTANT:
                continue
            journal = champs[MECG_CHAMP_JOURNAL - 1].strip()
            sens = champs[MECG_CHAMP_SENS - 1].strip()
            montant = _montant(champs[MECG_CHAMP_MONTANT - 1].strip())

            if montant is None:
                anomalies.append("Ligne %d (#MECG) : montant illisible '%s'."
                                 % (numero_ligne, champs[MECG_CHAMP_MONTANT - 1]))
                continue
            if sens not in ("0", "1"):
                anomalies.append("Ligne %d (#MECG) : sens '%s' invalide (attendu 0 ou 1)."
                                 % (numero_ligne, sens))
                continue

            debit, credit = par_journal.get(journal, (Decimal("0"), Decimal("0")))
            if sens == "0":
                total_debit += montant
                par_journal[journal] = (debit + montant, credit)
            else:
                total_credit += montant
                par_journal[journal] = (debit, credit + montant)

        infos.append("Total debit  : %s" % total_debit)
        infos.append("Total credit : %s" % total_credit)
        if total_debit != total_credit:
            anomalies.append("Fichier desequilibre : debit %s / credit %s (ecart %s)."
                             % (total_debit, total_credit, total_debit - total_credit))

        for journal, (debit, credit) in sorted(par_journal.items()):
            if debit != credit:
                anomalies.append("Journal '%s' desequilibre : debit %s / credit %s."
                                 % (journal, debit, credit))
            else:
                infos.append("Journal '%s' : equilibre a %s." % (journal, debit))

    return anomalies, avertissements, infos


def main():
    parseur = argparse.ArgumentParser(
        description="Valide un fichier d'import Sage 100 avant livraison."
    )
    parseur.add_argument("fichier", help="Chemin du fichier d'import a controler.")
    args = parseur.parse_args()

    anomalies, avertissements, infos = valider(args.fichier)

    print("Controle de : %s" % args.fichier)
    for info in infos:
        print("  . %s" % info)
    for avertissement in avertissements:
        print("  ! AVERTISSEMENT : %s" % avertissement)
    for anomalie in anomalies:
        print("  X ANOMALIE : %s" % anomalie)

    if anomalies:
        print("\nFichier NON LIVRABLE : corriger la source, pas le fichier de sortie.")
        return 1
    print("\nFichier conforme. Rappel : importer d'abord en environnement Sage de test.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
