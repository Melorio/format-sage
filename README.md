# format-sage

Une compétence (*skill*) Claude pour **générer, contrôler et relire les fichiers d'import à plat de Sage 100**, sur les trois modules : Comptabilité, Gestion commerciale, Immobilisations.

Publié par [Melorio](https://www.melorio.fr), cabinet de conseil en gestion, partenaire Sage et Microsoft.

---

## Le problème

Le format d'import de Sage 100 est un format à plat propriétaire : un drapeau (`#MECG`, `#CART`, `#IIMO`…) seul sur sa ligne, puis un champ par ligne, en CP850, avec des fins de ligne CRLF. Il n'y a ni séparateur, ni nom de colonne, ni schéma.

Trois conséquences pratiques, connues de tous ceux qui ont déjà produit ces fichiers :

- **Un champ vide est une ligne vide, jamais un champ omis.** Une ligne manquante décale tout le reste de l'enregistrement, et Sage signale l'erreur ailleurs — voire pas du tout.
- **Les champs non renseignés écrasent les valeurs existantes.** Un fichier de mise à jour incomplet détruit silencieusement du paramétrage.
- **La documentation éditeur ne suffit pas.** Elle regroupe les champs répétés là où le fichier les développe ligne à ligne, et elle diverge parfois du réel : `#MCJR` y compte 13 champs contre 16 dans les exports, `#MRGT` 19 champs groupés contre 91 lignes.

Un LLM à qui l'on demande ce fichier sans cadrage produit un résultat plausible et faux : bon nombre de lignes apparentes, mauvais encodage, drapeau inventé.

## Ce que fait cette compétence

Elle donne à l'assistant la structure réelle du format, vérifiée, et l'oblige à passer par des scripts plutôt que d'écrire le fichier à la main dans sa réponse.

- **Un catalogue de 223 drapeaux** — 64 en Comptabilité (`#VER 31`), 116 en Gestion commerciale (`#VER 33`), 43 en Immobilisations (`#VER 23`) — avec pour chacun le nombre de champs, la cardinalité et l'arbre d'imbrication.
- **Un niveau de fiabilité par drapeau**, explicite et non promotionnel :

  | Niveau | Signification |
  |---|---|
  | `eprouve` | importé avec succès dans un Sage de production |
  | `observe` | structure constatée sur plusieurs occurrences réelles, jamais importée |
  | `unique` | une seule occurrence observée : le caractère fixe du nombre de champs n'est pas prouvé |

  À ce jour : 8 drapeaux `eprouve`, 123 `observe`, 93 `unique`. Cet écart est le point le plus important du projet — il dit exactement jusqu'où va la garantie.

- **Un générateur** (`ecrire_sage.py`) qui déduit le module des drapeaux employés, écrit l'en-tête correspondant, applique CP850 et les CRLF, refuse d'écrire si le nombre de champs ne correspond pas, et avertit quand le drapeau visé n'a jamais été importé en production.
- **Un validateur** (`valider_sage.py`) qui contrôle l'en-tête, le `#FIN`, l'encodage réel des octets, les LF isolés, le nombre de champs de chaque bloc, l'imbrication parent/enfant, et — pour `#MECG` — l'équilibre débit/crédit global et par journal. Il sert aussi à **inspecter un export client** : inventaire des drapeaux et totaux.

## Quelques points établis empiriquement

Ils ne figurent pas, ou pas exactement, dans la documentation éditeur. Ils sont documentés fichier par fichier dans `format-sage/references/`.

- **L'encodage est CP850**, pas CP1252 ni UTF-8, sur les trois modules. Un export sans caractère accentué ne permet pas de trancher — c'est le piège le plus courant.
- **`#DEV EUR` est propre à la Comptabilité.** Cette troisième ligne d'en-tête dans un fichier de Gestion commerciale provoque le rejet « Fichier inconnu ligne : 3 ».
- **Les Immobilisations datent en `JJMMAAAA`** (8 chiffres), là où les deux autres modules utilisent `JJMMAA`. Une date de 6 chiffres décale le champ.
- **Treize drapeaux de Gestion commerciale dépassent quatre caractères** (`#CPROJHISTO`, `#CASTGAM`…). Un parseur qui filtre sur `^#[A-Z]{3,4}$` les ignore *silencieusement* et absorbe leurs champs dans le bloc précédent. Filtrer sur `^#[A-Z0-9]{3,12}$`.
- **La ligne vide de séparation est propre à `#MECG`** : 38 champs puis une ligne vide, soit 39 lignes. Ni `#MRGT` ni `#MECA` n'en ont. Ne pas généraliser par symétrie.
- **Un drapeau partagé n'a pas toujours la même structure d'un module à l'autre** : `#MECE` compte 10 champs en Comptabilité et 9 en Gestion commerciale ; `#MPCT` 133 champs fixes en Comptabilité et 129 aux Immobilisations.
- **Les Immobilisations comportent des drapeaux « table »**, écrits une seule fois puis suivis d'un groupe répété un nombre de fois imposé par Sage (`#INCP` = 14 × 130). Tronquer la table décale tout le fichier.
- **Le champ 11 de `#IIMO` refuse tout caractère non alphanumérique** : un tiret dans un numéro de pièce fait rejeter l'enregistrement. Aucune documentation ne le mentionne ; établi par bissection.

## Installation

### Comme compétence Claude

```bash
git clone https://github.com/Melorio/format-sage.git
cd format-sage
zip -r format-sage.zip format-sage
```

Puis, dans Claude : *Paramètres → Capacités → Compétences → Téléverser une compétence*, et déposer `format-sage.zip`.

La compétence se déclenche seule dès qu'il est question de produire ou de contrôler un fichier d'import Sage, même sans nommer de drapeau.

### En ligne de commande, sans Claude

Les deux scripts fonctionnent de façon autonome, sans dépendance hors bibliothèque standard (Python 3.9+).

```bash
cd format-sage/scripts
python ecrire_sage.py --spec spec.json --sortie DOSSIER_MPLG_20260919.txt
python valider_sage.py DOSSIER_MPLG_20260919.txt
```

Le format de `spec.json` est décrit dans [`exemples/`](exemples/).

## Structure du dépôt

```
format-sage/
├── SKILL.md                 Méthode de travail : qualification, génération, validation, livraison
├── references/
│   ├── catalogue-drapeaux.md            64 drapeaux Comptabilité
│   ├── catalogue-drapeaux-gc.md         116 drapeaux Gestion commerciale
│   ├── immobilisations.md               Module Immobilisations en entier
│   ├── doc-champs-*.md                  Documentation éditeur v12.25, par drapeau
│   ├── index-champs-empirique*.md       Position par position, 55 drapeaux
│   └── m*.md, cpai-*.md                 Fiches détaillées par drapeau éprouvé
└── scripts/
    ├── formats_sage.py      Tables de drapeaux et fiabilités, partagées
    ├── ecrire_sage.py       Génération
    └── valider_sage.py      Validation et inspection d'export
```

## Méthode

Le travail repose sur une règle unique : **l'export réel fait autorité, pas la documentation.** Chaque drapeau est confronté à un export complet du dossier de démonstration Sage *BIJOU* avant d'entrer au catalogue, et son statut reflète le niveau de preuve atteint, pas le niveau de confiance souhaité.

Quand un import échoue, le protocole est la bissection, jamais la correction au jugé : réémettre d'abord un enregistrement réel sans aucune modification, puis le même avec le seul code changé, puis réintroduire les valeurs métier une par une. Les contraintes non documentées se découvrent ainsi, et seulement ainsi.

## Données

Ce dépôt ne contient **aucune donnée client**. Les valeurs d'exemple proviennent du dossier de démonstration *BIJOU* fourni par Sage, qui est fictif.

Les fichiers `references/doc-champs-comptabilite.md` et `references/doc-champs-gestion-commerciale.md` sont des extractions, découpées par drapeau, de la documentation de format publiée par Sage (v12.25). Elles donnent le nom métier de chaque champ et l'énumération des valeurs admises — ce que la seule observation d'un export ne fournit pas. Le reste du dépôt est le fruit du travail de rapprochement mené par Melorio, et documente notamment les écarts constatés entre cette documentation et les fichiers réels.

## Avertissement

Un fichier d'import Sage est destructif. Aucun fichier produit avec cet outil ne doit être importé en production sans passage préalable en environnement de test, et impérativement pour toute modification d'enregistrements existants ou tout drapeau marqué `observe` ou `unique`.

« Sage » et « Sage 100 » sont des marques de leurs propriétaires respectifs.

## Contribuer

Les retours de terrain sont la matière première de ce catalogue. Sont particulièrement utiles :

- un drapeau **importé avec succès en production** — il passe à `eprouve`, précisez le module et la version ;
- un **écart constaté** entre le catalogue et un export réel ;
- une **contrainte non documentée** découverte à l'occasion d'un rejet, avec le message d'erreur de Sage et la démarche de bissection qui l'a isolée.

Ouvrez une *issue* ou une *pull request*. Merci de ne joindre aucun extrait d'export client : une description de structure, des champs anonymisés ou un enregistrement du dossier BIJOU suffisent toujours.

## Portages

Le catalogue et les deux scripts ne dépendent d'aucun assistant : ils s'utilisent en ligne de commande, et servent de socle aux différentes enveloppes. Le paquet publié ici est celui de Claude, seul testé à ce jour. **Un paquet équivalent pour Mistral est en préparation** ; les formats de compétence n'étant pas interchangeables, il fera l'objet d'une publication distincte dans ce dépôt.

## Support

Ce dépôt est libre d'usage. Melorio, cabinet de conseil en gestion et partenaire Sage, accompagne les reprises de données, les interfaçages et les migrations Sage 100 — c'est dans ce cadre que ce catalogue a été constitué. Pour un fichier à produire sous contrainte, un import qui échoue sans message exploitable ou un chantier de reprise à cadrer : [melorio.fr](https://www.melorio.fr).

## Licence

[MIT](LICENSE) — © Melorio.
