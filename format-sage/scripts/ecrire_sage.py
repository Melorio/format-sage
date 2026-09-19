#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ecrire_sage.py — Génération de fichiers d'import Sage 100.

Couvre les trois modules : Comptabilité (#VER 31), Gestion commerciale (#VER 33) et
Immobilisations (#VER 23). Le module est déduit des drapeaux employés, et avec lui l'en-tête à
écrire et les cardinalités à contrôler.

Quand un fichier ne contient que des drapeaux partagés (#MPLG, #MPCT, #MCJR...), la déduction
est impossible : préciser alors --module, ou la clé "module" dans la spec. C'est important, les
cardinalités diffèrent — #MPCT compte 134 champs en Comptabilité et 130 en Immobilisations.

Applique automatiquement l'en-tête, l'encodage CP850, les fins de ligne CRLF, le nombre de
champs attendu et la ligne vide de séparation. Les tables de drapeaux, avec leur niveau de
fiabilité, vivent dans formats_sage.py.

Utilisation en ligne de commande :
    python ecrire_sage.py --spec spec.json --sortie QUANTUM_MPLG_20260822.txt

Format de spec.json :
    {
      "blocs": [
        {"drapeau": "MPLG", "champs": ["49500000", "0", "...", ...]},
        {"drapeau": "MPLG", "champs": [...]}
      ]
    }

Utilisation comme bibliothèque :
    from ecrire_sage import ecrire_fichier
    ecrire_fichier([{"drapeau": "MECG", "champs": [...]}], "sortie.txt")
"""

import argparse
import json
import sys

try:
    from formats_sage import TABLES, ENTETES, ENCODAGE, FIN, CRLF, NOMS_MODULE, module_du_fichier
except ImportError:  # execution depuis un autre repertoire
    import os
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from formats_sage import (TABLES, ENTETES, ENCODAGE, FIN, CRLF, NOMS_MODULE,
                              module_du_fichier)

# Table du module courant, fixee par ecrire_fichier a partir des drapeaux de la spec.
FORMATS = TABLES["CPTA"]


AVERTISSEMENTS = []
_MODULE = ["CPTA"]


class ErreurFormat(Exception):
    """Anomalie bloquante : le fichier n'est pas ecrit."""


def _normaliser(blocs):
    """Valide la structure de la spec et renvoie une liste de tuples (drapeau, champs)."""
    if not blocs:
        raise ErreurFormat("Aucun bloc a ecrire : la spec est vide.")

    normalises = []
    for i, bloc in enumerate(blocs, start=1):
        if not isinstance(bloc, dict):
            raise ErreurFormat("Bloc %d : un objet {drapeau, champs} est attendu." % i)

        drapeau = str(bloc.get("drapeau", "")).lstrip("#").upper()
        if drapeau not in FORMATS:
            raise ErreurFormat(
                "Bloc %d : drapeau '%s' non supporte. Drapeaux disponibles : %s. "
                "Ne pas extrapoler un format non eprouve." % (i, drapeau, ", ".join(sorted(FORMATS)))
            )

        champs = bloc.get("champs")
        if champs is None:
            raise ErreurFormat("Bloc %d (%s) : cle 'champs' absente." % (i, drapeau))
        if not isinstance(champs, (list, tuple)):
            raise ErreurFormat("Bloc %d (%s) : 'champs' doit etre une liste." % (i, drapeau))

        # None -> chaine vide (un champ vide est une ligne vide, jamais un champ omis)
        champs = ["" if c is None else str(c) for c in champs]

        spec = FORMATS[drapeau]
        if spec["nb_lignes"] is not None and len(champs) != spec["nb_lignes"]:
            raise ErreurFormat(
                "Bloc %d (#%s) : %d champs fournis, %d attendus. Un champ vide doit etre "
                "present sous forme de chaine vide, pas omis." % (i, drapeau, len(champs), spec["nb_lignes"])
            )
        if len(champs) < spec["min_lignes"]:
            raise ErreurFormat(
                "Bloc %d (#%s) : %d champs fournis, minimum %d. Ce format comporte des champs "
                "repetables : seul le minimum est controle." % (i, drapeau, len(champs), spec["min_lignes"])
            )
        if spec["fiabilite"] != "eprouve":
            message = ("#%s (%s) : format %s, jamais importe en production. Verifier la "
                       "structure sur l'export du dossier client et tester l'import sur un "
                       "dossier d'essai." % (drapeau, spec["libelle"], spec["fiabilite"]))
            if message not in AVERTISSEMENTS:
                AVERTISSEMENTS.append(message)

        for j, valeur in enumerate(champs, start=1):
            if "\n" in valeur or "\r" in valeur:
                raise ErreurFormat(
                    "Bloc %d (#%s), champ %d : contient un saut de ligne. "
                    "Un champ occupe exactement une ligne." % (i, drapeau, j)
                )

        normalises.append((drapeau, champs))

    return normalises


def _encodage_du_fichier(normalises):
    """Tous les formats Sage 100 s'ecrivent en CP850, sans exception connue."""
    return ENCODAGE


def construire_lignes(normalises):
    """Construit la liste des lignes du fichier, en-tete et #FIN compris."""
    lignes = list(ENTETES[_MODULE[0]])
    for drapeau, champs in normalises:
        lignes.append("#" + drapeau)
        lignes.extend(champs)
        if FORMATS[drapeau]["separateur"]:
            lignes.append("")  # ligne vide de separation
    lignes.append(FIN)
    return lignes


def ecrire_fichier(blocs, chemin_sortie, verbeux=True, module=None):
    """Ecrit le fichier d'import. Renvoie un dictionnaire de synthese."""
    global FORMATS
    del AVERTISSEMENTS[:]
    if module:
        module = str(module).upper()
        module = {"IMMOS": "IMMO", "COMPTA": "CPTA", "CPTA": "CPTA",
                  "GC": "GC", "GESCOM": "GC", "IMMO": "IMMO"}.get(module)
        if module is None:
            raise ErreurFormat("Module inconnu. Valeurs acceptees : cpta, gc, immo.")
    else:
        try:
            module = module_du_fichier([str(b.get("drapeau", "")) for b in blocs
                                        if isinstance(b, dict)])
        except ValueError as err:
            raise ErreurFormat(str(err))
    FORMATS = TABLES[module]
    _MODULE[0] = module
    normalises = _normaliser(blocs)
    encodage = _encodage_du_fichier(normalises)
    lignes = construire_lignes(normalises)

    contenu = CRLF.join(lignes) + CRLF
    try:
        octets = contenu.encode(encodage)
    except UnicodeEncodeError as err:
        caractere = contenu[err.start:err.end]
        raise ErreurFormat(
            "Caractere %r non representable en %s (position %d). Remplacer ce caractere : "
            "Sage n'accepte pas l'UTF-8 sur ce format." % (caractere, encodage.upper(), err.start)
        )

    with open(chemin_sortie, "wb") as flux:
        flux.write(octets)

    compte = {}
    for drapeau, _ in normalises:
        compte[drapeau] = compte.get(drapeau, 0) + 1

    synthese = {
        "fichier": chemin_sortie,
        "encodage": encodage,
        "module": _MODULE[0],
        "avertissements": list(AVERTISSEMENTS),
        "nb_lignes": len(lignes),
        "nb_octets": len(octets),
        "blocs": compte,
    }

    if verbeux:
        print("Fichier ecrit : %s" % chemin_sortie)
        print("  Module     : %s, en-tete %s"
              % (NOMS_MODULE[_MODULE[0]], " / ".join(ENTETES[_MODULE[0]])))
        print("  Encodage   : %s, fins de ligne CRLF" % encodage.upper())
        print("  Blocs      : %s" % ", ".join("#%s x%d" % (d, n) for d, n in sorted(compte.items())))
        print("  Lignes     : %d  (%d octets)" % (len(lignes), len(octets)))
        for avert in AVERTISSEMENTS:
            print("  ATTENTION  : %s" % avert)
        print("A valider avec : python valider_sage.py %s" % chemin_sortie)

    return synthese


def main():
    parseur = argparse.ArgumentParser(
        description="Genere un fichier d'import Sage 100 Comptabilite a partir d'une spec JSON."
    )
    parseur.add_argument("--spec", required=True, help="Chemin du fichier JSON decrivant les blocs.")
    parseur.add_argument("--module", default=None,
                         help="cpta, gc ou immo. Facultatif : deduit des drapeaux si omis. "
                              "Obligatoire pour un fichier ne contenant que des drapeaux partages.")
    parseur.add_argument("--sortie", required=True, help="Chemin du fichier d'import a produire.")
    args = parseur.parse_args()

    with open(args.spec, "r", encoding="utf-8") as flux:
        donnees = json.load(flux)

    blocs = donnees.get("blocs", donnees if isinstance(donnees, list) else None)
    if blocs is None:
        print("ERREUR : la spec doit contenir une cle 'blocs' (ou etre une liste de blocs).",
              file=sys.stderr)
        return 2

    try:
        ecrire_fichier(blocs, args.sortie, module=args.module or donnees.get("module"))
    except ErreurFormat as err:
        print("ERREUR DE FORMAT — aucun fichier ecrit.\n  %s" % err, file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
