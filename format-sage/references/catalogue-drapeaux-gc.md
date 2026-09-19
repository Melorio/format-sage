# Catalogue des drapeaux — Sage 100 Gestion commerciale

Inventaire croisant la documentation éditeur v12.25 (`#VER 33`) et un export complet d'un
dossier de démonstration (116 drapeaux, 2 953 enregistrements). Ce dossier ne sert qu'à
l'analyse : **son nom ne doit jamais apparaître dans un fichier livré à un client.**

## En-tête — la différence qui fait échouer l'import

L'en-tête de Gestion commerciale ne compte que **deux lignes** : `#FLG 000` puis `#VER 33`.
Ajouter `#DEV EUR`, qui appartient à la Comptabilité, provoque le rejet
« Fichier inconnu ligne : 3 ».

## Des drapeaux de plus de quatre caractères

Contrairement à la Comptabilité, la Gestion commerciale comporte treize drapeaux plus longs :
`#CPROJHISTO`, `#CPROJPLAN`, `#CPROJFAB`, `#CPROJLIG`, `#CCATAL`, `#CRESPROD`, `#CRESART`,
`#CASTGAM`, `#CARTRES`, `#CORGINT`, `#CBTNACT`, `#CRABF`, `#CSOLF`. Un parseur filtrant sur
quatre caractères les ignore **silencieusement** : leurs champs sont alors absorbés dans le
bloc précédent, qui paraît simplement plus long que prévu.

## Lire la colonne « lignes »

Nombre de lignes entre le drapeau et le drapeau suivant, champs vides compris. C'est la valeur
à reproduire. Un intervalle signale un format à champs répétables : ne pas le figer dans un
contrôle. `fixe` n'est établi que sur ce jeu de données.

| Drapeau | Objet | Occ. | Lignes | Statut | Source |
|---|---|---|---|---|---|
| `#CABO` | Abonnements | 12 | 44 | fixe | doc + export |
| `#CACL` | Tarifs de vente - Articles | 100 | 16 | fixe | doc + export |
| `#CACO` | Conditionnements - Articles | 6 | 6 | fixe | doc + export |
| `#CACP` | Comptabilité - Articles | 61 | 28…98 | variable (pas 14) | doc + export |
| `#CAEN` | En-tête des abonnements | 12 | 35 | fixe | doc + export |
| `#CAFR` | Références fournisseurs - Articles | 54 | 19 | fixe | doc + export |
| `#CAGE` | Fichier Agenda | 3 | 14 | fixe | doc + export |
| `#CAGL` | Glossaires - Articles | 10 | 1 | fixe | doc + export |
| `#CALI` | Lignes d’abonnement | 40 | 52 | fixe | doc + export |
| `#CANA` | Plans analytiques - Paramètres société | 1 | 253 | fixe | doc + export |
| `#CANO` | Liste nomenclatures - Articles | 27 | 12 | fixe | doc + export |
| `#CAOP` | Gamme opératoire – Articles | 67 | 12 | fixe | doc + export |
| `#CAPE` | Historique et périodicité de l’abonnement | 46 | 5 | fixe | doc + export |
| `#CAPR` | Prévisions – Articles | 826 | 5 | fixe | doc + export |
| `#CARG` | Conditions de règlement de l’abonnement | 5 | 11 | fixe | doc + export |
| `#CARR` | Modes arrondi - Paramètres société | 1 | 20 | fixe | doc + export |
| `#CART` | Fiches Articles | 71 | 76…86 | variable (pas 2) | doc + export |
| `#CARTRES` | Article / ressource | 7 | 1…6 | variable | doc + export |
| `#CAST` | Dépôts de stockage - Articles | 83 | 6 | fixe | doc + export |
| `#CASTGAM` | Stock par énuméré de gamme | 18 | 7 | fixe | doc + export |
| `#CATG` | Articles/nomenclatures | 4 | 12…36 | variable (pas 6) | doc + export |
| `#CATQ` | Gammes de remise du tarif - Articles/ nomenclatures | 8 | 16…28 | variable (pas 4) | doc + export |
| `#CBQT` | Banques – Tiers (clients ou fournisseurs) | 44 | 21 | fixe | doc + export |
| `#CBTNACT` | Bouton Actions | 1 | 20 | fixe | doc + export |
| `#CCAF` | Cadre de facturation | 20 | 4 | fixe | doc + export |
| `#CCATAL` | Catalogue article | 39 | 5 | fixe | doc + export |
| `#CCCL` | Catégories tarifaires - Paramètres société | 1 | 64 | fixe | doc + export |
| `#CCCO` | Catégories comptables - Paramètres société | 1 | 250 | fixe | doc + export |
| `#CCDL` | Dépôts de livraison clients | 26 | 17 | fixe | doc + export |
| `#CCLA` | Classement clients (compatibilité <= 9.00) | 1 | 10 | fixe | doc + export |
| `#CCLI` | Fiche client | 25 | 120…121 | variable | doc + export |
| `#CCOL` | Conditions de livraison - Paramètres société | 1 | 60 | fixe | doc + export |
| `#CCOM` | Communication | 1 | 19 | fixe | doc + export |
| `#CCON` | Intitulés Conditionnement - Paramètres société | 1 | 20 | fixe | doc + export |
| `#CCPT` | Comptabilité (compatibilité <= 9.00) | 1 | 790 | fixe | doc + export |
| `#CDEC` | Contacts dépôt | 2 | 13 | fixe | doc + export |
| `#CDEE` | Emplacement dépôt | 111 | 5 | fixe | doc + export |
| `#CDEP` | Dépôts de stockage | 2 | 18 | fixe | doc + export |
| `#CDEV` | Devises - Paramètres société | 1 | 640 | fixe | doc + export |
| `#CDGA` | Enumérés gamme - Paramètres société | 7 | 3…9 | variable | doc + export |
| `#CDOS` | Dossier entreprise | 1 | 187 | fixe | doc + export |
| `#CEAG` | Evénements agenda - Paramètres société | 8 | 2…5 | variable | doc + export |
| `#CECH` | Echanges électroniques | 1 | 12 | fixe | doc + export |
| `#CEIN` | Enumérés d'information libre | 3 | 3 | fixe | doc + export |
| `#CENA` | Enumérés analytiques - Paramètres société | 6 | 4 | fixe | doc + export |
| `#CEXP` | Modes expédition - Paramètres société | 1 | 500 | fixe | doc + export |
| `#CFAC` | Comptabilité - Familles d’articles | 13 | 0…98 | variable (pas 14) | doc + export |
| `#CFAM` | Fiche - Familles d’articles | 19 | 42 | fixe | doc + export |
| `#CFCL` | Catégories tarifaires - Familles d’articles | 7 | 9 | fixe | doc + export |
| `#CFFR` | Références fournisseurs - Familles d’articles | 8 | 13 | fixe | doc + export |
| `#CFOU` | Fiche Fournisseur | 28 | 114…115 | variable | doc + export |
| `#CFRC` | Remises par client - Familles d’articles | 7 | 2 | fixe | doc + export |
| `#CGAG` | Groupes d’événements agenda - Paramètres société | 1 | 200 | fixe | doc + export |
| `#CGAM` | Gammes articles - Paramètres société | 1 | 100 | fixe | doc + export |
| `#CGEN` | Codification automatique | 1 | 44 | fixe | doc + export |
| `#CGLO` | Fichier Glossaire | 8 | 8 | fixe | doc + export |
| `#CHEN` | En-têtes de documents | 74 | 86 | fixe | doc + export |
| `#CHLI` | Lignes de documents | 281 | 62…64 | variable (pas 2) | doc + export |
| `#CHRE` | Acomptes / échéances | 73 | 10 | fixe | doc + export |
| `#CINF` | Informations libres - Paramètres société | 7 | 6…41 | variable (pas 5) | doc + export |
| `#CIVA` | Informations libres élémentsArticles/nomenclatures | 63 | 2…8 | variable | doc + export |
| `#CNIC` | Niveaux d'analyse - Paramètres société | 1 | 30 | fixe | doc + export |
| `#COLO` | Organisation Autres fonctions - Paramètres société | 1 | 46 | fixe | doc + export |
| `#COLR` | Règlements – Paramètres société | 1 | 5 | fixe | doc + export |
| `#CORG` | Organisation Documents - Paramètres société | 1 | 2101 | fixe | doc + export |
| `#CORGINT` | Organisation interne | 1 | 527 | fixe | doc + export |
| `#CPAI` | Pays - Paramètres société | 15 | 8 | fixe | doc + export |
| `#CPER` | Périodicités - Paramètres société | 1 | 10 | fixe | doc + export |
| `#CPROJFAB` | Projet de fabrication | 5 | 10 | fixe | doc + export |
| `#CPROJHISTO` | Projet — historique | 23 | 18 | fixe | doc + export |
| `#CPROJLIG` | Projet — lignes | 1 | 5 | fixe | doc + export |
| `#CPROJPLAN` | Projet — planning | 92 | 27 | fixe | doc + export |
| `#CRAB` | Rabais, remises et ristournes clients | 1 | 7 | fixe | doc + export |
| `#CRABF` | Rabais, remises, ristournes fournisseurs | 1 | 8 | fixe | doc + export |
| `#CRAC` | Clavier | 7 | 9 | fixe | doc + export |
| `#CREF` | Enumérés de gamme - Articles | 9 | 10 | fixe | doc + export |
| `#CREG` | Modes règlement - Paramètres société | 1 | 420 | fixe | doc + export |
| `#CREP` | Fichier Collaborateurs | 11 | 29…30 | variable | doc + export |
| `#CRES` | Résiliations abonnements - Paramètres société | 1 | 30 | fixe | doc + export |
| `#CRESART` | Ressources / articles | 16 | 1…2 | variable | doc + export |
| `#CRESPROD` | Ressources / production | 18 | 58…60 | variable | doc + export |
| `#CRIS` | Codes risques- Paramètres société | 1 | 40 | fixe | doc + export |
| `#CRLT` | fournisseurs) | 40 | 11 | fixe | doc + export |
| `#CSAV` | Enumérés statistiques articles - Paramètres société | 2 | 3…4 | variable | doc + export |
| `#CSBQ` | Structure banque - Paramètres société | 1 | 40 | fixe | doc + export |
| `#CSOL` | Soldes et promotions clients | 1 | 5 | fixe | doc + export |
| `#CSOLF` | Soldes et promotions fournisseurs | 1 | 6 | fixe | doc + export |
| `#CSTA` | Champs statistiques articles - Paramètres société | 1 | 5 | fixe | doc + export |
| `#CSTT` | Champs statistiques tiers - Paramètres société | 1 | 10 | fixe | doc + export |
| `#CSTV` | Enumérés statistiques tiers - Paramètres société | 8 | 2 | fixe | doc + export |
| `#CTAA` | Sélection articles/familles, clients/catégories du barème | 6 | 2…6 | variable (pas 2) | doc + export |
| `#CTAR` | Commissions | 2 | 9 | fixe | doc + export |
| `#CTRE` | Gamme de commission du barème | 4 | 8…12 | variable (pas 2) | doc + export |
| `#CTTI` | Types de tiers - Paramètres société | 1 | 136 | fixe | doc + export |
| `#CUA1` | Enumérés conditionnement - Paramètres société | 1 | 10 | fixe | doc + export |
| `#CUAV` | Unités achat / vente - Paramètres société | 1 | 150 | fixe | doc + export |
| `#MBAP` | Bon à payer | 1 | 5 | fixe | doc + export |
| `#MBQE` | Banques | 5 | 192…237 | variable (pas 45) | doc + export |
| `#MCAC` |  | 1 | 2 | fixe | export seul |
| `#MCAL` | Calendrier | 2 | 53 | fixe | doc + export |
| `#MCJR` | Codes journaux | 18 | 16 | fixe | doc + export |
| `#MCTB` | Contacts banque | 2 | 13 | fixe | doc + export |
| `#MCTD` | Contacts dossier | 1 | 19 | fixe | doc + export |
| `#MCTT` | Contacts clients | 23 | 13 | fixe | doc + export |
| `#MECE` | Echanges électroniques comptables | 1 | 9 | fixe | doc + export |
| `#MMDG` | Modèles de grille | 4 | 11…15 | variable (pas 4) | doc + export |
| `#MMDR` | Modèles de règlement | 4 | 12…34 | variable (pas 11) | doc + export |
| `#MMEX` | Mentions d’exonération de taxes | 8 | 3 | fixe | doc + export |
| `#MMRE` | Motifs de refus facture | 26 | 6 | fixe | doc + export |
| `#MPCA` | Fichier Plan analytique (Codes affaires) | 62 | 22 | fixe | doc + export |
| `#MPGA` | Répartition analytique - Comptes généraux | 43 | 4 | fixe | doc + export |
| `#MPLB` | Export de la personnalisation de la langue | 1 | 3 | fixe | doc + export |
| `#MPLG` | Plan comptable | 314 | 23 | fixe | doc + export |
| `#MSCT` | Service contact - Paramètres société | 1 | 60 | fixe | doc + export |
| `#MTAX` | Taux de taxes | 21 | 15…42 | variable | doc + export |
| `#MTCO` | Type contact | 1 | 30 | fixe | doc + export |

## Documentés mais absents de l'export modèle

Structure connue par la seule documentation :

`#CAFC`, `#CAFF`, `#CAMO`, `#CATC`, `#CBIL`, `#CCAI`, `#CDUS`, `#CEXPGRI`, `#CFMO`, `#CFTQ`, `#CHGRI`, `#CINC`, `#CIVL`, `#CLIA`, `#CMOD`, `#CREC`, `#CRGA`, `#CRGT`, `#CTIA`, `#MCIC`, `#MCTA`, `#MCVB`, `#MFAR`, `#MFRT`

## Drapeaux de Comptabilité présents dans un export de Gestion commerciale

Un export de Gestion commerciale embarque une partie du paramétrage comptable du dossier, avec
les mêmes drapeaux `#M...` et la même structure que côté Comptabilité :

`#MBAP`, `#MBQE`, `#MCAC`, `#MCAL`, `#MCJR`, `#MCTB`, `#MCTD`, `#MCTT`, `#MECE`, `#MMDG`, `#MMDR`, `#MMEX`, `#MMRE`, `#MPCA`, `#MPGA`, `#MPLB`, `#MPLG`, `#MSCT`, `#MTAX`, `#MTCO`

Notamment `#MPLG` : le plan comptable (314 comptes de 23 champs) figure dans l'export de
Gestion commerciale, alors qu'il est absent de l'export de Comptabilité du même dossier.
Ces drapeaux s'écrivent à l'identique dans les deux modules — seul l'en-tête du fichier change.

## Ordre et imbrication des enregistrements

```
#CFAM  famille d'articles
  #CFAC  comptabilité de la famille
  #CFFR  références fournisseurs de la famille
  #CFCL  catégories tarifaires de la famille
  #CFRC  remises par client
#CART  article
  #CACP  comptabilité de l'article
  #CACL  tarifs de vente
  #CAFR  références fournisseurs
  #CAST  dépôts de stockage
  #CANO  nomenclature
  #CAGL  glossaire
  #CIVA  informations libres
#CCLI  client        /  #CFOU  fournisseur
  #CBQT  banques du tiers
  #CRLT  relances du tiers
  #CCDL  dépôts de livraison
  #MCTT  contacts du tiers
#CHEN  en-tête de document
  #CHLI  lignes du document
  #CHRE  acomptes et échéances
#CABO  abonnement
  #CAEN  en-tête d'abonnement
  #CALI  lignes d'abonnement
  #CAPE  historique et périodicité
  #CARG  conditions de règlement
```

Un `#CACL` rencontré après un `#CART` porte les tarifs de **cet** article. Un parseur qui
traite les drapeaux à plat rattache les sous-blocs au mauvais enregistrement.
