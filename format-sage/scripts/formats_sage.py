#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
formats_sage.py — Connaissance du format Sage 100, partagee par les scripts.

Trois modules, trois tables :
  DRAPEAUX_CPTA  Comptabilite,        #VER 31, en-tete de 3 lignes (64 drapeaux)
  DRAPEAUX_GC    Gestion commerciale, #VER 33, en-tete de 2 lignes (116 drapeaux)
  DRAPEAUX_IMMO  Immobilisations,     #VER 23, en-tete de 2 lignes (43 drapeaux)

Origine : documentation editeur (v12.25 pour la Comptabilite et la Gestion commerciale, v11.00
pour les Immobilisations) croisee avec un export complet de chaque module, pris sur le meme
dossier de demonstration.

DES DRAPEAUX PARTAGES, MAIS PAS TOUJOURS IDENTIQUES. Les exports de Gestion commerciale et
d'Immobilisations embarquent une partie du parametrage comptable sous les memes drapeaux #M...
La plupart ont la meme structure partout, mais deux exceptions sont averees :
  #MECE  10 champs en Comptabilite, 9 en Gestion commerciale
  #MPCT  133 champs fixes en Comptabilite, 129 en Immobilisations (+ n comptes rattaches)
Ne jamais presumer qu'un drapeau partage se comporte pareil dans un autre module : interroger
la table du module cible, jamais celle d'un autre.

CHAMP "type" (table Immobilisations uniquement) :
  enregistrement  le drapeau se repete, un par enregistrement ;
  table GxR       le drapeau apparait UNE SEULE FOIS, suivi de R repetitions d'un groupe de G
                  champs. La table doit etre ecrite entiere, emplacements vides compris :
                  la tronquer decale tout le reste du fichier ;
  variable        longueur dependante du parametrage du dossier, a deduire de l'export client.

nb_lignes  nombre de CHAMPS du bloc. Il egale le nombre de lignes entre deux drapeaux, sauf
           pour #MECG ou s'ajoute une ligne vide de separation (38 champs, 39 lignes).
           None = format a champs repetables : seul min_lignes est controle.
fiabilite  eprouve  importe avec succes en production ;
           observe  structure constatee sur plusieurs occurrences reelles, jamais importee ;
           unique   une seule occurrence dans l'export modele : le caractere fixe du nombre
                    de champs n'est pas prouve, verifier sur l'export du dossier client.

Ne jamais elargir cette table par extrapolation : ajouter un drapeau seulement apres l'avoir
constate dans un export reel ou dans references/doc-champs-comptabilite.md.
"""

ENCODAGE = "cp850"          # Comptabilite ET Gestion commerciale. Jamais CP1252, jamais UTF-8.
CRLF = "\r\n"
FIN = "#FIN"
# La ligne #DEV EUR est propre a la Comptabilite. Sa presence dans un fichier de Gestion
# commerciale provoque le rejet "Fichier inconnu ligne : 3".
NOMS_MODULE = {"CPTA": "Comptabilite", "GC": "Gestion commerciale", "IMMO": "Immobilisations"}

# Module lu sur la ligne #VER d'un fichier existant. C'est la source la plus fiable : les
# drapeaux #M... partages ne permettent pas a eux seuls de trancher.
VERSIONS = {"#VER 31": "CPTA", "#VER 33": "GC", "#VER 23": "IMMO"}

ENTETES = {
    "CPTA": ["#FLG 000", "#VER 31", "#DEV EUR"],
    "GC":   ["#FLG 000", "#VER 33"],
    "IMMO": ["#FLG 000", "#VER 23"],
}
ENTETE = ENTETES["CPTA"]   # compatibilite avec le code appelant existant

DRAPEAUX_CPTA = {
    "MANA": {"nb_lignes": 253, "min_lignes": 253, "separateur": False, "occ_modele": 1, "fiabilite": "unique", "libelle": "Plan analytique"},
    "MBAP": {"nb_lignes": 5, "min_lignes": 5, "separateur": False, "occ_modele": 1, "fiabilite": "unique", "libelle": "Bon a payer"},
    "MBQE": {"nb_lignes": None, "min_lignes": 192, "separateur": False, "occ_modele": 5, "fiabilite": "observe", "libelle": "Banque"},
    "MBQT": {"nb_lignes": 21, "min_lignes": 21, "separateur": False, "occ_modele": 47, "fiabilite": "observe", "libelle": "Banques tiers"},
    "MBUD": {"nb_lignes": None, "min_lignes": 440, "separateur": False, "occ_modele": 7, "fiabilite": "observe", "libelle": "Poste budgetaire"},
    "MCAC": {"nb_lignes": 2, "min_lignes": 2, "separateur": False, "occ_modele": 1, "fiabilite": "unique", "libelle": "Codes action facture"},
    "MCAL": {"nb_lignes": 53, "min_lignes": 53, "separateur": False, "occ_modele": 2, "fiabilite": "observe", "libelle": "Calendrier"},
    "MCDL": {"nb_lignes": 17, "min_lignes": 17, "separateur": False, "occ_modele": 25, "fiabilite": "observe", "libelle": "Lieux de livraisons clients"},
    "MCIB": {"nb_lignes": None, "min_lignes": 58, "separateur": False, "occ_modele": 125, "fiabilite": "observe", "libelle": "Codes interbancaires"},
    "MCJA": {"nb_lignes": 4, "min_lignes": 4, "separateur": False, "occ_modele": 1, "fiabilite": "unique", "libelle": "Codes journaux analytiques"},
    "MCJR": {"nb_lignes": 16, "min_lignes": 16, "separateur": False, "occ_modele": 18, "fiabilite": "eprouve", "libelle": "Codes journaux"},
    "MCLN": {"nb_lignes": 1890, "min_lignes": 1890, "separateur": False, "occ_modele": 1, "fiabilite": "unique", "libelle": "Organisation"},
    "MCOL": {"nb_lignes": 31, "min_lignes": 31, "separateur": False, "occ_modele": 11, "fiabilite": "observe", "libelle": "Collaborateur"},
    "MCTB": {"nb_lignes": 13, "min_lignes": 13, "separateur": False, "occ_modele": 2, "fiabilite": "observe", "libelle": "Contacts banques"},
    "MCTD": {"nb_lignes": 19, "min_lignes": 19, "separateur": False, "occ_modele": 1, "fiabilite": "unique", "libelle": "Contacts dossiers"},
    "MCTT": {"nb_lignes": 13, "min_lignes": 13, "separateur": False, "occ_modele": 22, "fiabilite": "observe", "libelle": "Contacts tiers"},
    "MDEV": {"nb_lignes": 640, "min_lignes": 640, "separateur": False, "occ_modele": 1, "fiabilite": "unique", "libelle": "Devises"},
    "MDOS": {"nb_lignes": 133, "min_lignes": 133, "separateur": False, "occ_modele": 1, "fiabilite": "unique", "libelle": "Dossier entreprise"},
    "MECA": {"nb_lignes": 4, "min_lignes": 4, "separateur": False, "occ_modele": 2, "fiabilite": "eprouve", "libelle": "Ecriture analytique"},
    "MECE": {"nb_lignes": 10, "min_lignes": 10, "separateur": False, "occ_modele": 1, "fiabilite": "unique", "libelle": "Services connectes"},
    "MECG": {"nb_lignes": 38, "min_lignes": 38, "separateur": True, "occ_modele": 279, "fiabilite": "eprouve", "libelle": "Ecriture generale"},
    "MENA": {"nb_lignes": 4, "min_lignes": 4, "separateur": False, "occ_modele": 6, "fiabilite": "observe", "libelle": "Enumere analytique"},
    "MEXT": {"nb_lignes": None, "min_lignes": 98, "separateur": False, "occ_modele": 12, "fiabilite": "observe", "libelle": "Extrait bancaire"},
    "MFIS": {"nb_lignes": 76, "min_lignes": 76, "separateur": False, "occ_modele": 1, "fiabilite": "unique", "libelle": "Informations fiscales"},
    "MINF": {"nb_lignes": None, "min_lignes": 6, "separateur": False, "occ_modele": 4, "fiabilite": "observe", "libelle": "Information libre"},
    "MIVA": {"nb_lignes": 8, "min_lignes": 8, "separateur": False, "occ_modele": 10, "fiabilite": "observe", "libelle": "Informations libres"},
    "MLET": {"nb_lignes": 65, "min_lignes": 65, "separateur": False, "occ_modele": 1, "fiabilite": "unique", "libelle": "Ajustement lettrage"},
    "MLIB": {"nb_lignes": 2, "min_lignes": 2, "separateur": False, "occ_modele": 4, "fiabilite": "observe", "libelle": "Libelle"},
    "MMDA": {"nb_lignes": None, "min_lignes": 44, "separateur": False, "occ_modele": 3, "fiabilite": "observe", "libelle": "Modele d'abonnement"},
    "MMDG": {"nb_lignes": None, "min_lignes": 11, "separateur": False, "occ_modele": 4, "fiabilite": "observe", "libelle": "Modele de grille"},
    "MMDR": {"nb_lignes": None, "min_lignes": 12, "separateur": False, "occ_modele": 4, "fiabilite": "observe", "libelle": "Modele de reglement"},
    "MMEX": {"nb_lignes": 3, "min_lignes": 3, "separateur": False, "occ_modele": 8, "fiabilite": "observe", "libelle": "Mentions d'exoneration de TVA"},
    "MMOL": {"nb_lignes": 30, "min_lignes": 30, "separateur": False, "occ_modele": 1, "fiabilite": "unique", "libelle": "Motifs de litiges"},
    "MMRE": {"nb_lignes": 6, "min_lignes": 6, "separateur": False, "occ_modele": 26, "fiabilite": "observe", "libelle": "Motifs refus facture"},
    "MNAT": {"nb_lignes": 1820, "min_lignes": 1820, "separateur": False, "occ_modele": 1, "fiabilite": "unique", "libelle": "Nature de compte"},
    "MNIC": {"nb_lignes": 30, "min_lignes": 30, "separateur": False, "occ_modele": 1, "fiabilite": "unique", "libelle": "Niveau d'analyse"},
    "MPAB": {"nb_lignes": 433, "min_lignes": 433, "separateur": False, "occ_modele": 26, "fiabilite": "observe", "libelle": "Budget plan analytique"},
    "MPAY": {"nb_lignes": 8, "min_lignes": 8, "separateur": False, "occ_modele": 15, "fiabilite": "observe", "libelle": "Pays"},
    "MPCA": {"nb_lignes": 22, "min_lignes": 22, "separateur": False, "occ_modele": 62, "fiabilite": "observe", "libelle": "Plan analytique/ Section"},
    "MPCT": {"nb_lignes": None, "min_lignes": 134, "separateur": False, "occ_modele": 64, "fiabilite": "eprouve", "libelle": "Plan tiers"},
    "MPIA": {"nb_lignes": 4, "min_lignes": 4, "separateur": False, "occ_modele": 9, "fiabilite": "observe", "libelle": "Modele de saisie/ Ecriture analytique"},
    "MPIC": {"nb_lignes": 83, "min_lignes": 83, "separateur": False, "occ_modele": 106, "fiabilite": "observe", "libelle": "Modele de saisie/ Ecriture comptable"},
    "MPIE": {"nb_lignes": 4, "min_lignes": 4, "separateur": False, "occ_modele": 37, "fiabilite": "observe", "libelle": "Modele de saisie"},
    "MPLB": {"nb_lignes": 3, "min_lignes": 3, "separateur": False, "occ_modele": 1, "fiabilite": "unique", "libelle": "Parametrage des libelles"},
    "MPLG": {"nb_lignes": 23, "min_lignes": 23, "separateur": False, "occ_modele": 0, "fiabilite": "eprouve", "libelle": "Plan comptable"},
    "MPLJ": {"nb_lignes": 5, "min_lignes": 5, "separateur": False, "occ_modele": 1, "fiabilite": "unique", "libelle": "Personnalisation des libelles (dans les codes"},
    "MRAP": {"nb_lignes": 40, "min_lignes": 40, "separateur": False, "occ_modele": 1, "fiabilite": "unique", "libelle": "Periode de rappel"},
    "MRCO": {"nb_lignes": 5, "min_lignes": 5, "separateur": False, "occ_modele": 1, "fiabilite": "unique", "libelle": "Recouvrement"},
    "MREG": {"nb_lignes": 300, "min_lignes": 300, "separateur": False, "occ_modele": 1, "fiabilite": "unique", "libelle": "Mode de reglement"},
    "MREJ": {"nb_lignes": 2, "min_lignes": 2, "separateur": False, "occ_modele": 51, "fiabilite": "observe", "libelle": "Motif de rejet"},
    "MRES": {"nb_lignes": 200, "min_lignes": 200, "separateur": False, "occ_modele": 1, "fiabilite": "unique", "libelle": "Parametrage des resultats"},
    "MRGI": {"nb_lignes": 2, "min_lignes": 2, "separateur": False, "occ_modele": 1, "fiabilite": "unique", "libelle": "Registres"},
    "MRGL": {"nb_lignes": 6, "min_lignes": 6, "separateur": False, "occ_modele": 1, "fiabilite": "unique", "libelle": "Regularisations comptables"},
    "MRGT": {"nb_lignes": 91, "min_lignes": 91, "separateur": False, "occ_modele": 138, "fiabilite": "eprouve", "libelle": "Registre taxe"},
    "MRIS": {"nb_lignes": 40, "min_lignes": 40, "separateur": False, "occ_modele": 1, "fiabilite": "unique", "libelle": "Code risque"},
    "MRJS": {"nb_lignes": 2, "min_lignes": 2, "separateur": False, "occ_modele": 49, "fiabilite": "observe", "libelle": "Motifs de rejet SEPA"},
    "MRLT": {"nb_lignes": 11, "min_lignes": 11, "separateur": False, "occ_modele": 40, "fiabilite": "observe", "libelle": "Reglements tiers"},
    "MRSO": {"nb_lignes": 30, "min_lignes": 30, "separateur": False, "occ_modele": 1, "fiabilite": "unique", "libelle": "Resolutions"},
    "MSBQ": {"nb_lignes": 40, "min_lignes": 40, "separateur": False, "occ_modele": 1, "fiabilite": "unique", "libelle": "Structure banque"},
    "MSCT": {"nb_lignes": 60, "min_lignes": 60, "separateur": False, "occ_modele": 1, "fiabilite": "unique", "libelle": "Service des contacts"},
    "MSTT": {"nb_lignes": 10, "min_lignes": 10, "separateur": False, "occ_modele": 1, "fiabilite": "unique", "libelle": "Champ Statistique Tiers"},
    "MSTV": {"nb_lignes": 2, "min_lignes": 2, "separateur": False, "occ_modele": 8, "fiabilite": "observe", "libelle": "Enumere statistique"},
    "MTAX": {"nb_lignes": None, "min_lignes": 15, "separateur": False, "occ_modele": 21, "fiabilite": "eprouve", "libelle": "Taux de taxe"},
    "MTCO": {"nb_lignes": 30, "min_lignes": 30, "separateur": False, "occ_modele": 1, "fiabilite": "unique", "libelle": "Type contact"},
    "MTTI": {"nb_lignes": 136, "min_lignes": 136, "separateur": False, "occ_modele": 1, "fiabilite": "unique", "libelle": "Types tiers"},}


DRAPEAUX_GC = {
    "CABO": {"nb_lignes": 44, "min_lignes": 44, "separateur": False, "occ_modele": 12, "fiabilite": "observe", "libelle": "Abonnements"},
    "CACL": {"nb_lignes": 16, "min_lignes": 16, "separateur": False, "occ_modele": 100, "fiabilite": "observe", "libelle": "Tarifs de vente - Articles"},
    "CACO": {"nb_lignes": 6, "min_lignes": 6, "separateur": False, "occ_modele": 6, "fiabilite": "observe", "libelle": "Conditionnements - Articles"},
    "CACP": {"nb_lignes": None, "min_lignes": 28, "separateur": False, "occ_modele": 61, "fiabilite": "observe", "libelle": "Comptabilite - Articles"},
    "CAEN": {"nb_lignes": 35, "min_lignes": 35, "separateur": False, "occ_modele": 12, "fiabilite": "observe", "libelle": "En-tete des abonnements"},
    "CAFR": {"nb_lignes": 19, "min_lignes": 19, "separateur": False, "occ_modele": 54, "fiabilite": "observe", "libelle": "References fournisseurs - Articles"},
    "CAGE": {"nb_lignes": 14, "min_lignes": 14, "separateur": False, "occ_modele": 3, "fiabilite": "observe", "libelle": "Fichier Agenda"},
    "CAGL": {"nb_lignes": 1, "min_lignes": 1, "separateur": False, "occ_modele": 10, "fiabilite": "observe", "libelle": "Glossaires - Articles"},
    "CALI": {"nb_lignes": 52, "min_lignes": 52, "separateur": False, "occ_modele": 40, "fiabilite": "observe", "libelle": "Lignes d'abonnement"},
    "CANA": {"nb_lignes": 253, "min_lignes": 253, "separateur": False, "occ_modele": 1, "fiabilite": "unique", "libelle": "Plans analytiques - Parametres societe"},
    "CANO": {"nb_lignes": 12, "min_lignes": 12, "separateur": False, "occ_modele": 27, "fiabilite": "observe", "libelle": "Liste nomenclatures - Articles"},
    "CAOP": {"nb_lignes": 12, "min_lignes": 12, "separateur": False, "occ_modele": 67, "fiabilite": "observe", "libelle": "Gamme operatoire – Articles"},
    "CAPE": {"nb_lignes": 5, "min_lignes": 5, "separateur": False, "occ_modele": 46, "fiabilite": "observe", "libelle": "Historique et periodicite de l'abonnement"},
    "CAPR": {"nb_lignes": 5, "min_lignes": 5, "separateur": False, "occ_modele": 826, "fiabilite": "observe", "libelle": "Previsions – Articles"},
    "CARG": {"nb_lignes": 11, "min_lignes": 11, "separateur": False, "occ_modele": 5, "fiabilite": "observe", "libelle": "Conditions de reglement de l'abonnement"},
    "CARR": {"nb_lignes": 20, "min_lignes": 20, "separateur": False, "occ_modele": 1, "fiabilite": "unique", "libelle": "Modes arrondi - Parametres societe"},
    "CART": {"nb_lignes": None, "min_lignes": 76, "separateur": False, "occ_modele": 71, "fiabilite": "observe", "libelle": "Fiches Articles"},
    "CARTRES": {"nb_lignes": None, "min_lignes": 1, "separateur": False, "occ_modele": 7, "fiabilite": "observe", "libelle": "Article / ressource"},
    "CAST": {"nb_lignes": 6, "min_lignes": 6, "separateur": False, "occ_modele": 83, "fiabilite": "observe", "libelle": "Depots de stockage - Articles"},
    "CASTGAM": {"nb_lignes": 7, "min_lignes": 7, "separateur": False, "occ_modele": 18, "fiabilite": "observe", "libelle": "Stock par enumere de gamme"},
    "CATG": {"nb_lignes": None, "min_lignes": 12, "separateur": False, "occ_modele": 4, "fiabilite": "observe", "libelle": "Articles/nomenclatures"},
    "CATQ": {"nb_lignes": None, "min_lignes": 16, "separateur": False, "occ_modele": 8, "fiabilite": "observe", "libelle": "Gammes de remise du tarif - Articles/ nomenclatures"},
    "CBQT": {"nb_lignes": 21, "min_lignes": 21, "separateur": False, "occ_modele": 44, "fiabilite": "observe", "libelle": "Banques – Tiers (clients ou fournisseurs)"},
    "CBTNACT": {"nb_lignes": 20, "min_lignes": 20, "separateur": False, "occ_modele": 1, "fiabilite": "unique", "libelle": "Bouton Actions"},
    "CCAF": {"nb_lignes": 4, "min_lignes": 4, "separateur": False, "occ_modele": 20, "fiabilite": "observe", "libelle": "Cadre de facturation"},
    "CCATAL": {"nb_lignes": 5, "min_lignes": 5, "separateur": False, "occ_modele": 39, "fiabilite": "observe", "libelle": "Catalogue article"},
    "CCCL": {"nb_lignes": 64, "min_lignes": 64, "separateur": False, "occ_modele": 1, "fiabilite": "unique", "libelle": "Categories tarifaires - Parametres societe"},
    "CCCO": {"nb_lignes": 250, "min_lignes": 250, "separateur": False, "occ_modele": 1, "fiabilite": "unique", "libelle": "Categories comptables - Parametres societe"},
    "CCDL": {"nb_lignes": 17, "min_lignes": 17, "separateur": False, "occ_modele": 26, "fiabilite": "observe", "libelle": "Depots de livraison clients"},
    "CCLA": {"nb_lignes": 10, "min_lignes": 10, "separateur": False, "occ_modele": 1, "fiabilite": "unique", "libelle": "Classement clients (compatibilite <= 9.00)"},
    "CCLI": {"nb_lignes": None, "min_lignes": 120, "separateur": False, "occ_modele": 25, "fiabilite": "observe", "libelle": "Fiche client"},
    "CCOL": {"nb_lignes": 60, "min_lignes": 60, "separateur": False, "occ_modele": 1, "fiabilite": "unique", "libelle": "Conditions de livraison - Parametres societe"},
    "CCOM": {"nb_lignes": 19, "min_lignes": 19, "separateur": False, "occ_modele": 1, "fiabilite": "unique", "libelle": "Communication"},
    "CCON": {"nb_lignes": 20, "min_lignes": 20, "separateur": False, "occ_modele": 1, "fiabilite": "unique", "libelle": "Intitules Conditionnement - Parametres societe"},
    "CCPT": {"nb_lignes": 790, "min_lignes": 790, "separateur": False, "occ_modele": 1, "fiabilite": "unique", "libelle": "Comptabilite (compatibilite <= 9.00)"},
    "CDEC": {"nb_lignes": 13, "min_lignes": 13, "separateur": False, "occ_modele": 2, "fiabilite": "observe", "libelle": "Contacts depot"},
    "CDEE": {"nb_lignes": 5, "min_lignes": 5, "separateur": False, "occ_modele": 111, "fiabilite": "observe", "libelle": "Emplacement depot"},
    "CDEP": {"nb_lignes": 18, "min_lignes": 18, "separateur": False, "occ_modele": 2, "fiabilite": "observe", "libelle": "Depots de stockage"},
    "CDEV": {"nb_lignes": 640, "min_lignes": 640, "separateur": False, "occ_modele": 1, "fiabilite": "unique", "libelle": "Devises - Parametres societe"},
    "CDGA": {"nb_lignes": None, "min_lignes": 3, "separateur": False, "occ_modele": 7, "fiabilite": "observe", "libelle": "Enumeres gamme - Parametres societe"},
    "CDOS": {"nb_lignes": 187, "min_lignes": 187, "separateur": False, "occ_modele": 1, "fiabilite": "unique", "libelle": "Dossier entreprise"},
    "CEAG": {"nb_lignes": None, "min_lignes": 2, "separateur": False, "occ_modele": 8, "fiabilite": "observe", "libelle": "Evenements agenda - Parametres societe"},
    "CECH": {"nb_lignes": 12, "min_lignes": 12, "separateur": False, "occ_modele": 1, "fiabilite": "unique", "libelle": "Echanges electroniques"},
    "CEIN": {"nb_lignes": 3, "min_lignes": 3, "separateur": False, "occ_modele": 3, "fiabilite": "observe", "libelle": "Enumeres d'information libre"},
    "CENA": {"nb_lignes": 4, "min_lignes": 4, "separateur": False, "occ_modele": 6, "fiabilite": "observe", "libelle": "Enumeres analytiques - Parametres societe"},
    "CEXP": {"nb_lignes": 500, "min_lignes": 500, "separateur": False, "occ_modele": 1, "fiabilite": "unique", "libelle": "Modes expedition - Parametres societe"},
    "CFAC": {"nb_lignes": None, "min_lignes": 0, "separateur": False, "occ_modele": 13, "fiabilite": "observe", "libelle": "Comptabilite - Familles d'articles"},
    "CFAM": {"nb_lignes": 42, "min_lignes": 42, "separateur": False, "occ_modele": 19, "fiabilite": "observe", "libelle": "Fiche - Familles d'articles"},
    "CFCL": {"nb_lignes": 9, "min_lignes": 9, "separateur": False, "occ_modele": 7, "fiabilite": "observe", "libelle": "Categories tarifaires - Familles d'articles"},
    "CFFR": {"nb_lignes": 13, "min_lignes": 13, "separateur": False, "occ_modele": 8, "fiabilite": "observe", "libelle": "References fournisseurs - Familles d'articles"},
    "CFOU": {"nb_lignes": None, "min_lignes": 114, "separateur": False, "occ_modele": 28, "fiabilite": "observe", "libelle": "Fiche Fournisseur"},
    "CFRC": {"nb_lignes": 2, "min_lignes": 2, "separateur": False, "occ_modele": 7, "fiabilite": "observe", "libelle": "Remises par client - Familles d'articles"},
    "CGAG": {"nb_lignes": 200, "min_lignes": 200, "separateur": False, "occ_modele": 1, "fiabilite": "unique", "libelle": "Groupes d'evenements agenda - Parametres societe"},
    "CGAM": {"nb_lignes": 100, "min_lignes": 100, "separateur": False, "occ_modele": 1, "fiabilite": "unique", "libelle": "Gammes articles - Parametres societe"},
    "CGEN": {"nb_lignes": 44, "min_lignes": 44, "separateur": False, "occ_modele": 1, "fiabilite": "unique", "libelle": "Codification automatique"},
    "CGLO": {"nb_lignes": 8, "min_lignes": 8, "separateur": False, "occ_modele": 8, "fiabilite": "observe", "libelle": "Fichier Glossaire"},
    "CHEN": {"nb_lignes": 86, "min_lignes": 86, "separateur": False, "occ_modele": 74, "fiabilite": "observe", "libelle": "En-tetes de documents"},
    "CHLI": {"nb_lignes": None, "min_lignes": 62, "separateur": False, "occ_modele": 281, "fiabilite": "observe", "libelle": "Lignes de documents"},
    "CHRE": {"nb_lignes": 10, "min_lignes": 10, "separateur": False, "occ_modele": 73, "fiabilite": "observe", "libelle": "Acomptes / echeances"},
    "CINF": {"nb_lignes": None, "min_lignes": 6, "separateur": False, "occ_modele": 7, "fiabilite": "observe", "libelle": "Informations libres - Parametres societe"},
    "CIVA": {"nb_lignes": None, "min_lignes": 2, "separateur": False, "occ_modele": 63, "fiabilite": "observe", "libelle": "Informations libres elementsArticles/nomenclatures"},
    "CNIC": {"nb_lignes": 30, "min_lignes": 30, "separateur": False, "occ_modele": 1, "fiabilite": "unique", "libelle": "Niveaux d'analyse - Parametres societe"},
    "COLO": {"nb_lignes": 46, "min_lignes": 46, "separateur": False, "occ_modele": 1, "fiabilite": "unique", "libelle": "Organisation Autres fonctions - Parametres societe"},
    "COLR": {"nb_lignes": 5, "min_lignes": 5, "separateur": False, "occ_modele": 1, "fiabilite": "unique", "libelle": "Reglements – Parametres societe"},
    "CORG": {"nb_lignes": 2101, "min_lignes": 2101, "separateur": False, "occ_modele": 1, "fiabilite": "unique", "libelle": "Organisation Documents - Parametres societe"},
    "CORGINT": {"nb_lignes": 527, "min_lignes": 527, "separateur": False, "occ_modele": 1, "fiabilite": "unique", "libelle": "Organisation interne"},
    "CPAI": {"nb_lignes": 8, "min_lignes": 8, "separateur": False, "occ_modele": 15, "fiabilite": "eprouve", "libelle": "Pays - Parametres societe"},
    "CPER": {"nb_lignes": 10, "min_lignes": 10, "separateur": False, "occ_modele": 1, "fiabilite": "unique", "libelle": "Periodicites - Parametres societe"},
    "CPROJFAB": {"nb_lignes": 10, "min_lignes": 10, "separateur": False, "occ_modele": 5, "fiabilite": "observe", "libelle": "Projet de fabrication"},
    "CPROJHISTO": {"nb_lignes": 18, "min_lignes": 18, "separateur": False, "occ_modele": 23, "fiabilite": "observe", "libelle": "Projet — historique"},
    "CPROJLIG": {"nb_lignes": 5, "min_lignes": 5, "separateur": False, "occ_modele": 1, "fiabilite": "unique", "libelle": "Projet — lignes"},
    "CPROJPLAN": {"nb_lignes": 27, "min_lignes": 27, "separateur": False, "occ_modele": 92, "fiabilite": "observe", "libelle": "Projet — planning"},
    "CRAB": {"nb_lignes": 7, "min_lignes": 7, "separateur": False, "occ_modele": 1, "fiabilite": "unique", "libelle": "Rabais, remises et ristournes clients"},
    "CRABF": {"nb_lignes": 8, "min_lignes": 8, "separateur": False, "occ_modele": 1, "fiabilite": "unique", "libelle": "Rabais, remises, ristournes fournisseurs"},
    "CRAC": {"nb_lignes": 9, "min_lignes": 9, "separateur": False, "occ_modele": 7, "fiabilite": "observe", "libelle": "Clavier"},
    "CREF": {"nb_lignes": 10, "min_lignes": 10, "separateur": False, "occ_modele": 9, "fiabilite": "observe", "libelle": "Enumeres de gamme - Articles"},
    "CREG": {"nb_lignes": 420, "min_lignes": 420, "separateur": False, "occ_modele": 1, "fiabilite": "unique", "libelle": "Modes reglement - Parametres societe"},
    "CREP": {"nb_lignes": None, "min_lignes": 29, "separateur": False, "occ_modele": 11, "fiabilite": "observe", "libelle": "Fichier Collaborateurs"},
    "CRES": {"nb_lignes": 30, "min_lignes": 30, "separateur": False, "occ_modele": 1, "fiabilite": "unique", "libelle": "Resiliations abonnements - Parametres societe"},
    "CRESART": {"nb_lignes": None, "min_lignes": 1, "separateur": False, "occ_modele": 16, "fiabilite": "observe", "libelle": "Ressources / articles"},
    "CRESPROD": {"nb_lignes": None, "min_lignes": 58, "separateur": False, "occ_modele": 18, "fiabilite": "observe", "libelle": "Ressources / production"},
    "CRIS": {"nb_lignes": 40, "min_lignes": 40, "separateur": False, "occ_modele": 1, "fiabilite": "unique", "libelle": "Codes risques- Parametres societe"},
    "CRLT": {"nb_lignes": 11, "min_lignes": 11, "separateur": False, "occ_modele": 40, "fiabilite": "observe", "libelle": "fournisseurs)"},
    "CSAV": {"nb_lignes": None, "min_lignes": 3, "separateur": False, "occ_modele": 2, "fiabilite": "observe", "libelle": "Enumeres statistiques articles - Parametres societe"},
    "CSBQ": {"nb_lignes": 40, "min_lignes": 40, "separateur": False, "occ_modele": 1, "fiabilite": "unique", "libelle": "Structure banque - Parametres societe"},
    "CSOL": {"nb_lignes": 5, "min_lignes": 5, "separateur": False, "occ_modele": 1, "fiabilite": "unique", "libelle": "Soldes et promotions clients"},
    "CSOLF": {"nb_lignes": 6, "min_lignes": 6, "separateur": False, "occ_modele": 1, "fiabilite": "unique", "libelle": "Soldes et promotions fournisseurs"},
    "CSTA": {"nb_lignes": 5, "min_lignes": 5, "separateur": False, "occ_modele": 1, "fiabilite": "unique", "libelle": "Champs statistiques articles - Parametres societe"},
    "CSTT": {"nb_lignes": 10, "min_lignes": 10, "separateur": False, "occ_modele": 1, "fiabilite": "unique", "libelle": "Champs statistiques tiers - Parametres societe"},
    "CSTV": {"nb_lignes": 2, "min_lignes": 2, "separateur": False, "occ_modele": 8, "fiabilite": "observe", "libelle": "Enumeres statistiques tiers - Parametres societe"},
    "CTAA": {"nb_lignes": None, "min_lignes": 2, "separateur": False, "occ_modele": 6, "fiabilite": "observe", "libelle": "Selection articles/familles, clients/categories du bareme"},
    "CTAR": {"nb_lignes": 9, "min_lignes": 9, "separateur": False, "occ_modele": 2, "fiabilite": "observe", "libelle": "Commissions"},
    "CTRE": {"nb_lignes": None, "min_lignes": 8, "separateur": False, "occ_modele": 4, "fiabilite": "observe", "libelle": "Gamme de commission du bareme"},
    "CTTI": {"nb_lignes": 136, "min_lignes": 136, "separateur": False, "occ_modele": 1, "fiabilite": "unique", "libelle": "Types de tiers - Parametres societe"},
    "CUA1": {"nb_lignes": 10, "min_lignes": 10, "separateur": False, "occ_modele": 1, "fiabilite": "unique", "libelle": "Enumeres conditionnement - Parametres societe"},
    "CUAV": {"nb_lignes": 150, "min_lignes": 150, "separateur": False, "occ_modele": 1, "fiabilite": "unique", "libelle": "Unites achat / vente - Parametres societe"},
    "MBAP": {"nb_lignes": 5, "min_lignes": 5, "separateur": False, "occ_modele": 1, "fiabilite": "unique", "libelle": "Bon a payer"},
    "MBQE": {"nb_lignes": None, "min_lignes": 192, "separateur": False, "occ_modele": 5, "fiabilite": "observe", "libelle": "Banques"},
    "MCAC": {"nb_lignes": 2, "min_lignes": 2, "separateur": False, "occ_modele": 1, "fiabilite": "unique", "libelle": ""},
    "MCAL": {"nb_lignes": 53, "min_lignes": 53, "separateur": False, "occ_modele": 2, "fiabilite": "observe", "libelle": "Calendrier"},
    "MCJR": {"nb_lignes": 16, "min_lignes": 16, "separateur": False, "occ_modele": 18, "fiabilite": "observe", "libelle": "Codes journaux"},
    "MCTB": {"nb_lignes": 13, "min_lignes": 13, "separateur": False, "occ_modele": 2, "fiabilite": "observe", "libelle": "Contacts banque"},
    "MCTD": {"nb_lignes": 19, "min_lignes": 19, "separateur": False, "occ_modele": 1, "fiabilite": "unique", "libelle": "Contacts dossier"},
    "MCTT": {"nb_lignes": 13, "min_lignes": 13, "separateur": False, "occ_modele": 23, "fiabilite": "observe", "libelle": "Contacts clients"},
    "MECE": {"nb_lignes": 9, "min_lignes": 9, "separateur": False, "occ_modele": 1, "fiabilite": "unique", "libelle": "Echanges electroniques comptables"},
    "MMDG": {"nb_lignes": None, "min_lignes": 11, "separateur": False, "occ_modele": 4, "fiabilite": "observe", "libelle": "Modeles de grille"},
    "MMDR": {"nb_lignes": None, "min_lignes": 12, "separateur": False, "occ_modele": 4, "fiabilite": "observe", "libelle": "Modeles de reglement"},
    "MMEX": {"nb_lignes": 3, "min_lignes": 3, "separateur": False, "occ_modele": 8, "fiabilite": "observe", "libelle": "Mentions d'exoneration de taxes"},
    "MMRE": {"nb_lignes": 6, "min_lignes": 6, "separateur": False, "occ_modele": 26, "fiabilite": "observe", "libelle": "Motifs de refus facture"},
    "MPCA": {"nb_lignes": 22, "min_lignes": 22, "separateur": False, "occ_modele": 62, "fiabilite": "observe", "libelle": "Fichier Plan analytique (Codes affaires)"},
    "MPGA": {"nb_lignes": 4, "min_lignes": 4, "separateur": False, "occ_modele": 43, "fiabilite": "observe", "libelle": "Repartition analytique - Comptes generaux"},
    "MPLB": {"nb_lignes": 3, "min_lignes": 3, "separateur": False, "occ_modele": 1, "fiabilite": "unique", "libelle": "Export de la personnalisation de la langue"},
    "MPLG": {"nb_lignes": 23, "min_lignes": 23, "separateur": False, "occ_modele": 314, "fiabilite": "observe", "libelle": "Plan comptable"},
    "MSCT": {"nb_lignes": 60, "min_lignes": 60, "separateur": False, "occ_modele": 1, "fiabilite": "unique", "libelle": "Service contact - Parametres societe"},
    "MTAX": {"nb_lignes": None, "min_lignes": 15, "separateur": False, "occ_modele": 21, "fiabilite": "observe", "libelle": "Taux de taxes"},
    "MTCO": {"nb_lignes": 30, "min_lignes": 30, "separateur": False, "occ_modele": 1, "fiabilite": "unique", "libelle": "Type contact"},
}

DRAPEAUX_IMMO = {
    "IACQ": {"nb_lignes": 10, "min_lignes": 10, "separateur": False, "occ_modele": 1, "fiabilite": "unique", "type": "table 1x10", "libelle": "Natures d'acquisition"},
    "IANA": {"nb_lignes": 253, "min_lignes": 253, "separateur": False, "occ_modele": 1, "fiabilite": "unique", "type": "table 23x11", "libelle": "Plans analytiques"},
    "IBIE": {"nb_lignes": 40, "min_lignes": 40, "separateur": False, "occ_modele": 1, "fiabilite": "unique", "type": "table 4x10", "libelle": "Natures de bien"},
    "ICESPLAN": {"nb_lignes": 18, "min_lignes": 18, "separateur": False, "occ_modele": 1, "fiabilite": "unique", "type": "enregistrement", "libelle": "Plan de cession"},
    "ICOEF": {"nb_lignes": None, "min_lignes": 9, "separateur": False, "occ_modele": 3, "fiabilite": "observe", "type": "variable", "libelle": "Coefficients d'amortissement"},
    "IDEV": {"nb_lignes": 640, "min_lignes": 640, "separateur": False, "occ_modele": 1, "fiabilite": "unique", "type": "table 20x32", "libelle": "Devises"},
    "IDOS": {"nb_lignes": 127, "min_lignes": 127, "separateur": False, "occ_modele": 1, "fiabilite": "unique", "type": "enregistrement", "libelle": "Dossier entreprise"},
    "IEIN": {"nb_lignes": 3, "min_lignes": 3, "separateur": False, "occ_modele": 32, "fiabilite": "observe", "type": "enregistrement", "libelle": "Enumeres d'information libre"},
    "IENA": {"nb_lignes": 4, "min_lignes": 4, "separateur": False, "occ_modele": 6, "fiabilite": "observe", "type": "enregistrement", "libelle": "Enumeres analytiques"},
    "IFAM": {"nb_lignes": 58, "min_lignes": 58, "separateur": False, "occ_modele": 9, "fiabilite": "observe", "type": "enregistrement", "libelle": "Familles d'immobilisations"},
    "IFIS": {"nb_lignes": 20, "min_lignes": 20, "separateur": False, "occ_modele": 1, "fiabilite": "unique", "type": "table 2x10", "libelle": "Natures fiscales"},
    "IIMO": {"nb_lignes": 110, "min_lignes": 110, "separateur": False, "occ_modele": 39, "fiabilite": "observe", "type": "enregistrement", "libelle": "Immobilisations"},
    "IINF": {"nb_lignes": None, "min_lignes": 6, "separateur": False, "occ_modele": 4, "fiabilite": "observe", "type": "variable", "libelle": "Informations libres"},
    "IIVA": {"nb_lignes": None, "min_lignes": 4, "separateur": False, "occ_modele": 42, "fiabilite": "observe", "type": "variable", "libelle": "Valeurs des informations libres"},
    "ILIE": {"nb_lignes": 12, "min_lignes": 12, "separateur": False, "occ_modele": 2, "fiabilite": "observe", "type": "enregistrement", "libelle": "Lieux"},
    "ILOY": {"nb_lignes": 2, "min_lignes": 2, "separateur": False, "occ_modele": 253, "fiabilite": "observe", "type": "enregistrement", "libelle": "Loyers (credit-bail, location)"},
    "INAT": {"nb_lignes": 30, "min_lignes": 30, "separateur": False, "occ_modele": 1, "fiabilite": "unique", "type": "table 3x10", "libelle": "Natures de sortie"},
    "INCP": {"nb_lignes": 1820, "min_lignes": 1820, "separateur": False, "occ_modele": 1, "fiabilite": "unique", "type": "table 14x130", "libelle": "Natures de compte"},
    "INIC": {"nb_lignes": 30, "min_lignes": 30, "separateur": False, "occ_modele": 1, "fiabilite": "unique", "type": "table 1x30", "libelle": "Niveaux d'analyse"},
    "IPAI": {"nb_lignes": 8, "min_lignes": 8, "separateur": False, "occ_modele": 15, "fiabilite": "observe", "type": "enregistrement", "libelle": "Pays"},
    "IPLAN": {"nb_lignes": 10, "min_lignes": 10, "separateur": False, "occ_modele": 593, "fiabilite": "observe", "type": "enregistrement", "libelle": "Plans d'amortissement"},
    "IREG": {"nb_lignes": 300, "min_lignes": 300, "separateur": False, "occ_modele": 1, "fiabilite": "unique", "type": "table 10x30", "libelle": "Modes de reglement"},
    "IRIS": {"nb_lignes": 40, "min_lignes": 40, "separateur": False, "occ_modele": 1, "fiabilite": "unique", "type": "table 4x10", "libelle": "Codes risque"},
    "ISAV": {"nb_lignes": 6, "min_lignes": 6, "separateur": False, "occ_modele": 2, "fiabilite": "observe", "type": "enregistrement", "libelle": "Enumeres statistiques"},
    "ISBQ": {"nb_lignes": 40, "min_lignes": 40, "separateur": False, "occ_modele": 1, "fiabilite": "unique", "type": "table 10x4", "libelle": "Structures banque"},
    "ISERIE": {"nb_lignes": 1, "min_lignes": 1, "separateur": False, "occ_modele": 12, "fiabilite": "observe", "type": "enregistrement", "libelle": "Numeros de serie"},
    "ISTA": {"nb_lignes": 10, "min_lignes": 10, "separateur": False, "occ_modele": 1, "fiabilite": "unique", "type": "table 1x10", "libelle": "Champs statistiques"},
    "ISTT": {"nb_lignes": 10, "min_lignes": 10, "separateur": False, "occ_modele": 1, "fiabilite": "unique", "type": "table 1x10", "libelle": "Statistiques tiers"},
    "ISTV": {"nb_lignes": 2, "min_lignes": 2, "separateur": False, "occ_modele": 8, "fiabilite": "observe", "type": "enregistrement", "libelle": "Enumeres statistiques tiers"},
    "ITTI": {"nb_lignes": 136, "min_lignes": 136, "separateur": False, "occ_modele": 1, "fiabilite": "unique", "type": "table 34x4", "libelle": "Types de tiers"},
    "MBQT": {"nb_lignes": 21, "min_lignes": 21, "separateur": False, "occ_modele": 47, "fiabilite": "observe", "type": "enregistrement", "libelle": "Banques tiers"},
    "MCDL": {"nb_lignes": 17, "min_lignes": 17, "separateur": False, "occ_modele": 25, "fiabilite": "observe", "type": "enregistrement", "libelle": "Lieux de livraison clients"},
    "MCJR": {"nb_lignes": 16, "min_lignes": 16, "separateur": False, "occ_modele": 18, "fiabilite": "observe", "type": "enregistrement", "libelle": "Codes journaux"},
    "MCTD": {"nb_lignes": 19, "min_lignes": 19, "separateur": False, "occ_modele": 1, "fiabilite": "unique", "type": "enregistrement", "libelle": "Contacts dossier"},
    "MCTT": {"nb_lignes": 13, "min_lignes": 13, "separateur": False, "occ_modele": 22, "fiabilite": "observe", "type": "enregistrement", "libelle": "Contacts tiers"},
    "MMDG": {"nb_lignes": None, "min_lignes": 11, "separateur": False, "occ_modele": 2, "fiabilite": "observe", "type": "variable", "libelle": "Modeles de grille"},
    "MPCT": {"nb_lignes": None, "min_lignes": 130, "separateur": False, "occ_modele": 64, "fiabilite": "observe", "type": "variable", "libelle": "Plan tiers"},
    "MPGA": {"nb_lignes": 4, "min_lignes": 4, "separateur": False, "occ_modele": 43, "fiabilite": "observe", "type": "enregistrement", "libelle": "Repartition analytique des comptes"},
    "MPLB": {"nb_lignes": 3, "min_lignes": 3, "separateur": False, "occ_modele": 1, "fiabilite": "unique", "type": "enregistrement", "libelle": "Parametrage des libelles"},
    "MPLG": {"nb_lignes": 23, "min_lignes": 23, "separateur": False, "occ_modele": 314, "fiabilite": "observe", "type": "enregistrement", "libelle": "Plan comptable"},
    "MRLT": {"nb_lignes": 11, "min_lignes": 11, "separateur": False, "occ_modele": 40, "fiabilite": "observe", "type": "enregistrement", "libelle": "Niveaux de relance"},
    "MSCT": {"nb_lignes": 60, "min_lignes": 60, "separateur": False, "occ_modele": 1, "fiabilite": "unique", "type": "table 2x30", "libelle": "Services contacts"},
    "MTCO": {"nb_lignes": 30, "min_lignes": 30, "separateur": False, "occ_modele": 1, "fiabilite": "unique", "type": "table 1x30", "libelle": "Types de contact"},
}

TABLES = {"CPTA": DRAPEAUX_CPTA, "GC": DRAPEAUX_GC, "IMMO": DRAPEAUX_IMMO}

# Compatibilite : DRAPEAUX designait la table de Comptabilite.
DRAPEAUX = DRAPEAUX_CPTA


# Filiation : un bloc enfant doit suivre son parent. Sage refuse ou rattache au mauvais
# enregistrement un enfant orphelin. Liste volontairement limitee aux filiations constatees
# dans les exports reels ; un enfant absent d'ici n'est pas controle.
PARENTS = {
    # Comptabilite
    "MRGT": ("MECG",), "MECA": ("MECG",), "MPIC": ("MPIE",), "MPIA": ("MPIE",),
    "MCDL": ("MPCT",), "MRLT": ("MPCT",), "MBQT": ("MPCT",), "MCTT": ("MPCT",),
    "MPAB": ("MPCA",), "MCTB": ("MBQE",), "MPGA": ("MPLG",), "MCJA": ("MCJR",),
    "MIVA": ("MPLG", "MPCT"),
    # Gestion commerciale
    "CACP": ("CART",), "CACL": ("CART",), "CAFR": ("CART",), "CAST": ("CART",),
    "CANO": ("CART",), "CAGL": ("CART",),
    "CFAC": ("CFAM",), "CFFR": ("CFAM",), "CFCL": ("CFAM",), "CFRC": ("CFAM",),
    "CHLI": ("CHEN",), "CHRE": ("CHEN",),
    "CBQT": ("CCLI", "CFOU"), "CRLT": ("CCLI", "CFOU"), "CCDL": ("CCLI", "CFOU"),
    "CAEN": ("CABO",), "CALI": ("CABO",), "CAPE": ("CABO",), "CARG": ("CABO",),
    # Immobilisations
    "IPLAN": ("IIMO",), "ILOY": ("IIMO",), "ICESPLAN": ("IIMO",),
    "ISERIE": ("IIMO", "ICESPLAN"), "IIVA": ("IIMO", "MPCT"),
}


# Champs dont Sage refuse les caracteres non alphanumeriques, etabli par test d'import reel.
# "alnum" : lettres et chiffres uniquement, ni tiret, ni espace, ni ponctuation. Un champ vide
# reste accepte. La documentation editeur annonce "n caracteres alphanumeriques" sans preciser
# que la contrainte est stricte : un tiret suffit a faire rejeter l'enregistrement entier.
CHAMPS_ALNUM = {
    "IMMO": {"IIMO": {11: "N de piece"}},
}


def controler_caracteres(module, drapeau, champs):
    """Renvoie la liste des (position, libelle, valeur) violant une contrainte alphanumerique."""
    regles = CHAMPS_ALNUM.get(module, {}).get(drapeau.lstrip("#").upper(), {})
    anomalies = []
    for position, libelle in regles.items():
        if position <= len(champs):
            valeur = champs[position - 1]
            if valeur and not valeur.isalnum():
                anomalies.append((position, libelle, valeur))
    return anomalies


def module_du_fichier(drapeaux):
    """Deduit le module d'une liste de drapeaux.

    Un drapeau present dans plusieurs tables (#MPLG, #MCJR, #MPCT...) n'arbitre rien : seule la
    presence d'un drapeau exclusif tranche. Sans aucun drapeau exclusif, la Comptabilite est
    retenue par defaut — c'est le cas d'un fichier ne contenant que des drapeaux partages, qui
    s'importe alors dans le module choisi par l'utilisateur.
    """
    modules = set()
    for d in drapeaux:
        nom = d.lstrip("#").upper()
        presents = [m for m, table in TABLES.items() if nom in table]
        if len(presents) == 1:
            modules.add(presents[0])
    if len(modules) > 1:
        raise ValueError(
            "Le fichier melange des drapeaux exclusifs a plusieurs modules (%s). Les en-tetes "
            "different : produire un fichier par module." % ", ".join(sorted(modules)))
    return modules.pop() if modules else "CPTA"


def decrire(drapeau, module="CPTA"):
    """Fiche d'un drapeau dans le module indique, ou None s'il y est absent."""
    return TABLES[module].get(drapeau.lstrip("#").upper())


def nb_lignes_bloc(drapeau, module="CPTA"):
    """Nombre de lignes qu'occupe un bloc, ligne de separation comprise, drapeau exclu."""
    spec = decrire(drapeau, module)
    if spec is None or spec["nb_lignes"] is None:
        return None
    return spec["nb_lignes"] + (1 if spec["separateur"] else 0)
