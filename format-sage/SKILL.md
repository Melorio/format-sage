---
name: format-sage
description: Générer et valider des fichiers d'import Sage 100 au format à plat, pour la Comptabilité (#FLG 000 / #VER 31 / #DEV EUR ... #FIN), la Gestion commerciale (#FLG 000 / #VER 33 ... #FIN) et les Immobilisations (#FLG 000 / #VER 23 ... #FIN). Couvre les 64 drapeaux de la Comptabilité — écritures (#MECG), plan comptable (#MPLG), taux de taxe (#MTAX), plan tiers (#MPCT), codes journaux (#MCJR) — et les 116 de la Gestion commerciale — articles (#CART), familles (#CFAM), clients (#CCLI), fournisseurs (#CFOU), documents (#CHEN/#CHLI), pays (#CPAI) — et les 43 des Immobilisations — immobilisations (#IIMO), plans d'amortissement (#IPLAN), familles (#IFAM), loyers de crédit-bail (#ILOY) — via un catalogue par module et la documentation éditeur v12.25 embarquée. Déclencher cette skill dès qu'il est question de produire, corriger ou contrôler un fichier à importer dans Sage 100, même si le drapeau n'est pas nommé : "fichier d'import Sage", "importer des écritures", "générer des OD", "mettre à jour le code taxe des comptes", "créer des comptes ou des tiers en masse", "créer des articles ou des clients en masse", "reprendre le fichier articles", "reprendre le fichier des immobilisations", "importer des amortissements", "paramétrer les taux de TVA", "convertir ce CSV pour Sage", "reprendre le plan comptable du dossier X", "créer les journaux". Déclencher aussi pour toute analyse d'un export Sage existant (inventaire des drapeaux, équilibre débit/crédit, encodage, nombre de champs) ou pour convertir un export en fichier d'import modifié.
---

# Génération de fichiers d'import Sage 100

## Trois modules, trois en-têtes

| Module | En-tête | Drapeaux |
|---|---|---|
| Comptabilité | `#FLG 000` / `#VER 31` / `#DEV EUR` | 64, préfixe `#M` |
| Gestion commerciale | `#FLG 000` / `#VER 33` | 116, préfixes `#C` et `#M` |
| Immobilisations | `#FLG 000` / `#VER 23` | 43, préfixes `#I` et `#M` |

**`#DEV EUR` est propre à la Comptabilité.** Ailleurs, cette troisième ligne provoque le rejet
« Fichier inconnu ligne : 3 ». Les scripts déduisent le module des drapeaux employés et
écrivent le bon en-tête : ne pas le composer à la main.

Les exports de Gestion commerciale et d'Immobilisations embarquent une partie du paramétrage
comptable sous les mêmes drapeaux `#M...` — c'est d'ailleurs là que se trouve le plan comptable
`#MPLG` du dossier, absent de l'export de Comptabilité. **Un drapeau partagé n'a pas toujours la
même structure d'un module à l'autre.** Deux écarts sont avérés :

| Drapeau | Comptabilité | Gestion commerciale | Immobilisations |
|---|---|---|---|
| `#MECE` | 10 champs | 9 champs | — |
| `#MPCT` | 133 fixes + n | — | 129 fixes + n |

Toujours interroger la table du module cible, jamais celle d'un autre.

## Formats de dates — à ne pas transposer

La Comptabilité et la Gestion commerciale utilisent `JJMMAA` sur 6 chiffres. **Les
Immobilisations utilisent `JJMMAAAA` sur 8 chiffres** (`01022017`), sauf le champ « dernière
période archivée » de `#IDOS`, resté à 6. Une date de 6 chiffres dans un fichier
d'immobilisations décale le champ.

## Ce dont on dispose

| Ressource | Contenu | Quand la lire |
|---|---|---|
| `references/mecg-ecritures-generales.md` | Écritures, OD, journaux | Fiche détaillée, format éprouvé |
| `references/mplg-plan-comptable.md` | Comptes généraux | idem |
| `references/mtax-taux-taxe.md` | Taux et codes taxe | idem |
| `references/mpct-plan-tiers.md` | Clients, fournisseurs, salariés | idem |
| `references/mcjr-codes-journaux.md` | Codes journaux | idem |
| `references/cpai-pays-gc.md` | Table des pays (Gestion commerciale) | idem |
| `references/immobilisations.md` | Module Immobilisations en entier : en-tête, familles de drapeaux, `#IIMO` (110 champs), `#IPLAN`, ordre des blocs | Toute demande sur les immobilisations |
| `references/catalogue-drapeaux.md` | Les 64 drapeaux de Comptabilité : lignes, statut, imbrication | Drapeau sans fiche dédiée |
| `references/catalogue-drapeaux-gc.md` | Les 116 drapeaux de Gestion commerciale | idem |
| `references/doc-champs-comptabilite.md` | Documentation éditeur v12.25, Comptabilité | Noms et énumérations des champs |
| `references/doc-champs-gestion-commerciale.md` | Documentation éditeur v12.25, Gestion commerciale | idem |
| `references/index-champs-empirique.md` | Position par position, 27 drapeaux de Comptabilité | Vérifier un mapping |
| `references/index-champs-empirique-gc.md` | Position par position, 28 drapeaux de Gestion commerciale | idem |

Les quatre derniers fichiers sont volumineux : **ne jamais les charger entiers**, extraire la
section utile (`grep -A 60 '^## #MCJR' references/doc-champs-comptabilite.md`).

Ordre de consultation pour un drapeau donné : fiche dédiée si elle existe, sinon catalogue
(structure), puis documentation (sémantique), puis index empirique (vérification). Si le
drapeau n'apparaît nulle part, il n'existe probablement pas dans ce module — ne pas l'inventer.

## Étape 1 — Qualifier la demande AVANT de produire quoi que ce soit

Un fichier d'import Sage est destructif : **les champs non renseignés écrasent silencieusement
les valeurs existantes**. Produire un fichier plausible mais incomplet est pire que ne rien
produire. Poser les questions manquantes et s'arrêter tant qu'un élément bloquant n'est pas
fourni — jamais de valeur par défaut silencieuse.

1. Quel dossier client ? Il sert au nommage du fichier livré. Le nom du dossier de
   démonstration ayant servi à l'analyse ne doit jamais apparaître dans un livrable.
2. **Création** de nouveaux enregistrements ou **modification** d'existants ?

**Si modification :** exiger l'export du dossier contenant les enregistrements concernés. Ne
jamais reconstruire un enregistrement existant à partir de la seule table fournie par
l'utilisateur : lire le bloc complet dans l'export, ne modifier que les champs ciblés,
reporter tous les autres à l'identique. Sans export, le dire et proposer soit de le demander,
soit de se limiter aux enregistrements réellement nouveaux.

**Compléments par type :**
- `#MECG` : code journal, date de pièce, numérotation, et — si la source est un CSV — le
  mapping des colonnes. Vérifier si des blocs annexes sont nécessaires (`#MRGT` pour la TVA,
  `#MECA` pour l'analytique) et le signaler avant de générer.
- `#MPLG` : si le dossier utilise des informations libres (`#MIVA`), demander lesquelles.
- `#MPCT` : nombre de comptes collectifs rattachés par tiers.
- `#MTAX` : sens, type de taux, comptes de TVA rattachés.
- `#CART` : familles de rattachement, unités de vente, dépôts, et si des tarifs (`#CACL`) ou
  des références fournisseurs (`#CAFR`) doivent accompagner chaque article.
- `#CCLI` / `#CFOU` : catégorie tarifaire, catégorie comptable, mode de règlement, et les
  sous-blocs attendus (banques `#CBQT`, relances `#CRLT`, dépôts de livraison `#CCDL`).
- `#IIMO` : famille de rattachement (doit exister en `#IFAM`), lieu (`#ILIE`), modes et durées
  d'amortissement pour chacun des cinq plans, et si les plans `#IPLAN` doivent accompagner les
  immobilisations — sans eux, les biens sont importés sans amortissement.

## Étape 2 — Générer avec le script, jamais à la main

Construire un fichier ligne à ligne dans une réponse est la première source d'erreurs :
encodage perdu, LF au lieu de CRLF, champ oublié.

```bash
python scripts/ecrire_sage.py --spec spec.json --sortie DOSSIER_MPLG_20260911.txt
```

```json
{"blocs": [
  {"drapeau": "MPLG", "champs": ["49500000", "0", "Prov. Comptes groupe", "Prov. Comptes gro",
    "6", "2", "", "", "1", "0", "0", "0", "0", "0", "0", "050123", "", "0", "0", "A20", "0", "0", "0"]}
]}
```

Le script applique l'en-tête, CP850 et les CRLF, refuse d'écrire si le nombre de champs ne
correspond pas, et **avertit quand le drapeau employé n'a jamais été importé en production**.

Écrire un script Python ad hoc pour préparer la `spec.json` (parcours du CSV, croisement avec
l'export client, conversion des dates et montants) est normal et souhaitable. C'est la
génération du fichier final qui passe par `ecrire_sage.py`.

## Étape 3 — Valider avant livraison, toujours

```bash
python scripts/valider_sage.py DOSSIER_MPLG_20260911.txt
```

Contrôle l'en-tête, le `#FIN`, l'encodage réel des octets, les LF isolés, le nombre de champs
de chaque bloc, la ligne de séparation, et pour `#MECG` l'équilibre débit/crédit global **et
par journal**. Ne jamais livrer un fichier qui n'a pas passé le validateur. En cas d'anomalie,
corriger la source, pas le fichier de sortie.

Le validateur sert aussi à **inspecter un export client** : il en restitue l'inventaire des
drapeaux et les totaux.

## Étape 4 — Livrer

- Nommer `<DOSSIER>_<DRAPEAU>_<AAAAMMJJ>.txt`.
- Écrire dans `/mnt/user-data/outputs/` et présenter le fichier.
- Restituer la sortie du validateur.
- **Lister les hypothèses retenues** : code journal, numérotation, champs laissés vides,
  comptes de contrepartie. L'utilisateur doit pouvoir les infirmer.
- Recommander un import en environnement de test, impérativement pour toute modification
  d'existants ou tout drapeau marqué `observe` ou `unique` dans le catalogue.

## Règles communes du format

- **En-tête selon le module** : `#FLG 000` puis `#VER 31` et `#DEV EUR` en Comptabilité,
  `#VER 33` seul en Gestion commerciale, `#VER 23` seul aux Immobilisations. **Fin** : `#FIN`.
  Les scripts écrivent le bon en-tête à partir des drapeaux employés ou de `--module`.
- **Un champ par ligne.** Aucun séparateur `;` ou tabulation. Le drapeau est seul sur sa ligne
  et précède les champs de son enregistrement.
- **Un champ vide est une ligne vide, jamais un champ omis.** Un seul champ manquant décale
  tout le reste de l'enregistrement.
- **Aucun drapeau de Gestion commerciale n'a de ligne vide de séparation** : `#MECG` reste le
  seul cas connu, tous modules confondus.
- **Trois familles de drapeaux en Immobilisations.** Outre les drapeaux d'enregistrement
  classiques, le module comporte des drapeaux « table » — écrits **une seule fois**, suivis d'un
  groupe répété un nombre de fois imposé par Sage (`#INCP` = 14 × 130, `#IREG` = 10 × 30,
  `#ITTI` = 34 × 4) — et des drapeaux à cardinalité variable (`#IDOS` = 71 + 2 × nombre
  d'exercices). Tronquer une table décale tout le reste du fichier. Le validateur refuse un
  drapeau « table » écrit plusieurs fois ; `references/immobilisations.md` donne la liste.
- **Des drapeaux dépassent quatre caractères en Gestion commerciale** : `#CPROJHISTO`,
  `#CPROJPLAN`, `#CCATAL`, `#CRESPROD`, `#CASTGAM`… treize au total. Un parseur qui filtre sur
  quatre caractères les ignore **silencieusement** et absorbe leurs champs dans le bloc
  précédent, qui paraît seulement plus long que prévu. Filtrer sur `^#[A-Z0-9]{3,12}$`.
- **CRLF (`\r\n`) impérativement.** Seule exception rencontrée : un LF isolé à l'intérieur du
  champ *Formule* d'une information libre `#MINF`, que Sage exporte lui-même. Dans un fichier
  que nous générons, un LF isolé est toujours une anomalie.
- **Encodage CP850 pour tous les drapeaux.** Pas CP1252, pas UTF-8. Vérification :
  `open(f,'rb').read().decode('cp850')` doit afficher les accents correctement. Octets utiles :
  `é`=`\x82`, `â`=`\x83`, `à`=`\x85`, `ç`=`\x87`, `ê`=`\x88`, `è`=`\x8a`.
- Une erreur d'encodage à l'écriture vient presque toujours d'un caractère typographique absent
  de CP850, copié depuis une source moderne : tiret cadratin, apostrophe courbe, points de
  suspension.
- **Ligne vide de séparation : propre à `#MECG`.** 38 champs puis une ligne vide, soit 39
  lignes. Aucun autre drapeau n'en a — ni `#MRGT` (91 champs) ni `#MECA` (4 champs). Ne pas
  généraliser par symétrie.
- **Un export partiel est valide** : un fichier ne contenant que les enregistrements modifiés
  suffit pour une mise à jour.

## Attention aux exports versés dans un projet ou une pièce jointe

Un export Sage déposé comme fichier de projet est souvent **ré-encodé en UTF-8 au dépôt**. Le
fichier reste structurellement intact — mêmes drapeaux, mêmes occurrences, même nombre de
lignes — mais ses octets ne sont plus ceux de Sage : `é` (`\x82` en CP850) devient la séquence
`\xc3\xa9` ou `\xe2\x80\x9a` selon la chaîne subie, et le fichier grossit de quelques milliers
d'octets.

Conséquences : un tel fichier ne prouve rien sur l'encodage, et **ne doit jamais être réimporté
tel quel dans Sage**. Vérifier avant toute analyse d'encodage :

```python
raw = open(chemin, 'rb').read()
raw.decode('cp850')          # doit afficher les accents correctement
```

Si l'aperçu donne `Orf┼ávres` ou `accordÔÇÜ` au lieu de `Orfèvres` et `accordé`, le fichier a
subi `decode('cp1252').encode('utf-8')`. Récupération exacte, octet pour octet :

```python
original = raw.decode('utf-8').encode('cp1252')     # puis relire en cp850
```

La structure restant intacte, un fichier corrompu de la sorte demeure exploitable pour compter
des champs ou inventorier des drapeaux. Il est inutilisable pour tout le reste.

## Lire un export client

- Décoder en CP850, découper sur `\r\n`. **Jamais `.splitlines()`** : il coupe aussi sur les LF
  isolés et laisse des `\r` résiduels qui font échouer les comparaisons de noms de drapeaux.
- Ne jamais supposer un pas fixe entre enregistrements : des sous-blocs de longueur variable
  s'intercalent. Repérer les positions des drapeaux et découper entre deux marqueurs.
- Mémoriser le drapeau parent courant : `#MBQT`, `#MCTT`, `#MRLT`, `#MCDL`, `#MIVA` appartiennent
  au `#MPCT` qui les précède ; `#MRGT` et `#MECA` au `#MECG` ; `#MPIC` et `#MPIA` au `#MPIE`.
  En Gestion commerciale : `#CACP`, `#CACL`, `#CAFR`, `#CAST` appartiennent au `#CART` courant ;
  `#CHLI` et `#CHRE` au `#CHEN`. En Immobilisations : `#IPLAN`, `#ILOY`, `#ISERIE`, `#ICESPLAN`
  et `#IIVA` appartiennent au `#IIMO` courant. Chaque catalogue donne l'arbre de son module, et
  le validateur signale un bloc enfant qui ne suit pas un parent valide.

## Quand un import échoue

Sage indique un numéro de **ligne physique du fichier**, en-tête compris ; la position du champ
vaut ligne moins ligne du drapeau. Quand l'erreur porte sur l'enregistrement entier, c'est la
ligne du drapeau qui est citée.

Ne pas corriger au jugé : isoler par bissection. Réémettre d'abord un enregistrement réel de
l'export sans aucune modification, puis le même avec le seul code changé, puis réintroduire les
valeurs métier une par une. Trois essais valent mieux que trois hypothèses.

Certaines contraintes ne figurent dans aucune documentation et ne se découvrent qu'ainsi : le
champ 11 de `#IIMO` refuse tout caractère non alphanumérique, un simple tiret dans un numéro de
facture faisant rejeter l'enregistrement. Consigner chaque contrainte trouvée dans la fiche du
drapeau et, quand c'est automatisable, dans `valider_sage.py`.

## Ce qui fait autorité

L'export réel, pas la documentation. La documentation éditeur regroupe les champs répétés
(« ce champ est répété 10 fois ») là où le fichier les développe sur des lignes consécutives,
et elle est parfois incomplète : `#MCJR` y compte 13 champs contre 16 dans les fichiers réels,
`#MRGT` 19 champs groupés contre 91 lignes. Elle nomme aussi certains drapeaux de façon
tronquée : `#CPRO` dans la documentation, `#CPROJHISTO` dans le fichier. Toujours confronter la documentation à un export
avant de produire un fichier sur un drapeau non éprouvé.

## Après validation en production

Quand un nouveau format passe l'import réel chez un client, mettre à jour la skill dans la
foulée : passer sa `fiabilite` à `eprouve` dans `scripts/formats_sage.py`, créer sa fiche dans
`references/`, et la référencer dans le tableau en tête de ce document.
