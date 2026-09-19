# Catalogue des drapeaux — Sage 100 Comptabilité

Inventaire construit en croisant la documentation éditeur v12.25 et un export complet d'un
dossier de démonstration. Ce dossier ne sert qu'à l'analyse structurelle : **son nom ne doit
jamais apparaître dans un fichier livré à un client.**

## Lire la colonne « lignes »

C'est le **nombre de lignes entre le drapeau et le drapeau suivant**, tel qu'observé. C'est la
valeur à reproduire. Elle inclut les champs vides (une ligne vide chacun), les champs répétés
développés sur des lignes consécutives, et la ligne vide de séparation propre à `#MECG`.

Un intervalle (`134…135`) signale un format à champs répétables : ne pas figer le nombre de
lignes dans un contrôle. Le « pas » donne la taille du groupe répété quand il est identifiable.

`fixe` n'est établi que sur ce jeu de données : un drapeau vu une seule fois est fixe par
accident, pas par nature. Vérifier sur l'export du dossier client avant de produire un fichier.

| Drapeau | Objet | Occ. | Lignes | Statut | Source |
|---|---|---|---|---|---|
| `#MANA` | Plan analytique | 1 | 253 | fixe | doc + export |
| `#MBAP` | Bon à payer | 1 | 5 | fixe | doc + export |
| `#MBQE` | Banque | 5 | 192…237 | variable (pas 45) | doc + export |
| `#MBQT` | Banques tiers | 47 | 21 | fixe | doc + export |
| `#MBUD` | Poste budgétaire | 7 | 440…453 | variable | doc + export |
| `#MCAC` | Codes action facture | 1 | 2 | fixe | doc + export |
| `#MCAL` | Calendrier | 2 | 53 | fixe | doc + export |
| `#MCDL` | Lieux de livraisons clients | 25 | 17 | fixe | doc + export |
| `#MCIB` | Codes interbancaires | 125 | 58…73 | variable (pas 3) | doc + export |
| `#MCJA` | Codes journaux analytiques | 1 | 4 | fixe | doc + export |
| `#MCJR` | Codes journaux | 18 | 16 | fixe | doc + export |
| `#MCLN` | Organisation | 1 | 1890 | fixe | doc + export |
| `#MCOL` | Collaborateur | 11 | 31 | fixe | doc + export |
| `#MCTB` | Contacts banques | 2 | 13 | fixe | doc + export |
| `#MCTD` | Contacts dossiers | 1 | 19 | fixe | doc + export |
| `#MCTT` | Contacts tiers | 22 | 13 | fixe | doc + export |
| `#MDEV` | devise | 1 | 640 | fixe | doc + export |
| `#MDOS` | Dossier entreprise | 1 | 133 | fixe | doc + export |
| `#MECA` | Ecriture analytique | 2 | 4 | fixe | doc + export |
| `#MECE` | Services connectés | 1 | 10 | fixe | doc + export |
| `#MECG` | Ecriture générale | 279 | 39 | fixe | doc + export |
| `#MENA` | Enuméré analytique | 6 | 4 | fixe | doc + export |
| `#MEXT` | Extrait bancaire | 12 | 98…649 | variable | doc + export |
| `#MFIS` | Informations fiscales | 1 | 76 | fixe | doc + export |
| `#MINF` | Information libre | 4 | 6…41 | variable (pas 5) | doc + export |
| `#MIVA` | Informations libres | 10 | 8 | fixe | doc + export |
| `#MLET` | Ajustement lettrage | 1 | 65 | fixe | doc + export |
| `#MLIB` | Libellé | 4 | 2 | fixe | doc + export |
| `#MMDA` | Modèle d'abonnement | 3 | 44…89 | variable (pas 45) | doc + export |
| `#MMDG` | Modèle de grille | 4 | 11…15 | variable (pas 4) | doc + export |
| `#MMDR` | Modèle de règlement | 4 | 12…34 | variable (pas 11) | doc + export |
| `#MMEX` | Mentions d’exonération de TVA | 8 | 3 | fixe | doc + export |
| `#MMOL` | Motifs de litiges | 1 | 30 | fixe | doc + export |
| `#MMRE` | Motifs refus facture | 26 | 6 | fixe | doc + export |
| `#MNAT` | Nature de compte | 1 | 1820 | fixe | doc + export |
| `#MNIC` | Niveau d'analyse | 1 | 30 | fixe | doc + export |
| `#MPAB` | Budget plan analytique | 26 | 433 | fixe | doc + export |
| `#MPAY` | Pays | 15 | 8 | fixe | doc + export |
| `#MPCA` | Plan analytique/ Section | 62 | 22 | fixe | doc + export |
| `#MPCT` | Plan tiers | 64 | 134…135 | variable | doc + export |
| `#MPIA` | Modèle de saisie/ Ecriture analytique | 9 | 4 | fixe | doc + export |
| `#MPIC` | Modèle de saisie/ Ecriture comptable | 106 | 83 | fixe | doc + export |
| `#MPIE` | Modèle de saisie | 37 | 4 | fixe | doc + export |
| `#MPLB` | Paramétrage des libellés | 1 | 3 | fixe | doc + export |
| `#MPLJ` | Personnalisation des libellés (dans les codes | 1 | 5 | fixe | doc + export |
| `#MRAP` | Période de rappel | 1 | 40 | fixe | doc + export |
| `#MRCO` | Recouvrement | 1 | 5 | fixe | doc + export |
| `#MREG` | Mode de règlement | 1 | 300 | fixe | doc + export |
| `#MREJ` | Motif de rejet | 51 | 2 | fixe | doc + export |
| `#MRES` | Paramétrage des résultats | 1 | 200 | fixe | doc + export |
| `#MRGI` | Registres | 1 | 2 | fixe | doc + export |
| `#MRGL` | Régularisations comptables | 1 | 6 | fixe | doc + export |
| `#MRGT` | Registre taxe | 138 | 91 | fixe | doc + export |
| `#MRIS` | Code risque | 1 | 40 | fixe | doc + export |
| `#MRJS` | Motifs de rejet SEPA | 49 | 2 | fixe | doc + export |
| `#MRLT` | Règlements tiers | 40 | 11 | fixe | doc + export |
| `#MRSO` | Résolutions | 1 | 30 | fixe | doc + export |
| `#MSBQ` | Structure banque | 1 | 40 | fixe | doc + export |
| `#MSCT` | Service des contacts | 1 | 60 | fixe | doc + export |
| `#MSTT` | Champ Statistique Tiers | 1 | 10 | fixe | doc + export |
| `#MSTV` | Enuméré statistique | 8 | 2 | fixe | doc + export |
| `#MTAX` | Taux de taxe | 21 | 15…42 | variable | doc + export |
| `#MTCO` | Type contact | 1 | 30 | fixe | doc + export |
| `#MTTI` | Types tiers | 1 | 136 | fixe | doc + export |

## Documentés mais absents de l'export modèle

Structure connue par la seule documentation, jamais confrontée à un fichier réel :

`#CMOTIF`, `#MCNB`, `#MCTA`, `#MCVB`, `#MEDN`, `#MEIN`, `#MFAR`, `#MFRT`, `#MHIT`, `#MPCR`, `#MPGA`, `#MPGB`, `#MPLG`, `#MRAN`, `#MRFC`, `#MRGR`

## Ordre et imbrication des enregistrements

Un export suit l'ordre logique du dossier, et certains drapeaux sont des **sous-blocs** du
drapeau qui les précède. Séquence observée :

```
#MPCT  tiers
  #MCDL  lieux de livraison du tiers
  #MRLT  niveaux de relance du tiers
  #MBQT  banques du tiers
  #MCTT  contacts du tiers
  #MIVA  informations libres du tiers
#MPCA  section analytique
  #MPAB  budgets de la section
#MPIE  modèle de saisie
  #MPIC  lignes du modèle
  #MPIA  ventilation analytique du modèle
#MECG  écriture générale
  #MRGT  registre de taxe de l'écriture
  #MECA  ventilation analytique de l'écriture
#MCJR  code journal
  #MCJA  journal analytique
#MBQE  banque
  #MCTB  contacts de la banque
```

Conséquence : un `#MBQT` rencontré après un `#MPCT` appartient à **ce** tiers. Un parseur qui
traite les drapeaux à plat, sans mémoriser le parent courant, rattache les sous-blocs au
mauvais enregistrement.
