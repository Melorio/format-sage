# `#MPLG` — Plan comptable général

**Encodage : CP850. Fins de ligne : CRLF. 23 champs par bloc, pas de ligne vide de séparation.**

## Structure du fichier

```
#FLG 000
#VER 31
#DEV EUR
#MPLG
<champ 1>
...
<champ 23>
#MPLG
<champ 1>
...
<champ 23>
#FIN
```

## Ordre des 23 champs

| # | Champ | Format / valeurs |
|---|---|---|
| 1 | Numéro compte général | 3 à 13 caractères alphanumériques |
| 2 | Type | 0=Détail, 1=Total |
| 3 | Intitulé | 35 caractères max |
| 4 | Abrégé | 17 caractères max |
| 5 | Numéro nature | 0=Aucune, 1=Client, 2=Fournisseur, 3=Salaire, 4=Banque, 5=Caisse, 6=Amortissement, 7=Résultat bilan, 8=Charges, 9=Produits, 10=Résultat gestion, 11=Immobilisations, 12=Capitaux, 13=Stock, 14=Titre |
| 6 | Type report | 0=Aucun, 1=Solde, 2=Détail |
| 7 | Numéro compte reporting | 13 caractères majuscules, ou vide |
| 8 | Raccourci | 6 caractères majuscules |
| 9 | Saut lignes | 0=Saut de page, 1..99=sauts de lignes |
| 10 | Option regroupement | 0=Non, 1=Oui |
| 11 | Option analytique | 0=Non, 1=Oui |
| 12 | Option échéance | 0=Non, 1=Oui |
| 13 | Option quantité | 0=Non, 1=Oui |
| 14 | Option lettrage | 0=Non, 1=Oui |
| 15 | Option tiers | 0=Non, 1=Oui |
| 16 | Date de création | JJMMAA, ou vide (non importé) |
| 17 | Bloc-note | 255 caractères max |
| 18 | Option devise | 0=Non, 1=Oui |
| 19 | Numéro devise | 0..32, position dans la table des devises |
| 20 | **Code taxe** | 5 caractères majuscules, ou vide (ex. `A20`) |
| 21 | Mise en sommeil | 0=Non, 1=Oui |
| 22 | Report analytique | 0=Non, 1=Oui |
| 23 | Lettrage en saisie | 0=Non, 1=Oui |

## Cas 1 — Création de comptes

Générable directement à partir de cette fiche, sans export client. Renseigner les champs
pertinents (numéro, type, intitulé, abrégé, nature, code taxe) et laisser les autres à `0` ou
vides selon leur nature. Vérifier auprès de l'utilisateur les options qui engagent la saisie :
option tiers (15), option lettrage (14), option analytique (11), option échéance (12).

## Cas 2 — Modification de comptes existants

**Exiger l'export du dossier.** Procédure :

1. Parser l'export en scannant les drapeaux ligne à ligne (des sous-blocs `#MPGA`, `#MPGB`,
   `#MIVA` peuvent s'intercaler entre deux `#MPLG` — un pas fixe de 24 lignes est faux).
2. Pour chaque compte à modifier, extraire ses 23 champs tels quels.
3. Ne remplacer que les champs ciblés (typiquement le champ 20, code taxe).
4. Réémettre les 23 champs, les autres inchangés.
5. Le fichier ne contient que les comptes modifiés — c'est valide pour une mise à jour.

Un compte réémis avec des champs vides voit ses valeurs **écrasées silencieusement** dans Sage :
c'est le risque principal de ce drapeau.

## Informations libres (`#MIVA`)

Si le dossier utilise des informations libres sur les comptes généraux, elles se présentent
sous forme de blocs `#MIVA` **positionnels** placés après le `#MPLG` du compte concerné —
autant de valeurs que d'informations libres définies dans le dossier, dans l'ordre de leur
définition (`#MINF`).

Avant de réémettre des comptes d'un dossier qui utilise des champs libres, vérifier avec
l'utilisateur combien sont configurés et lesquels. Réémettre un `#MPLG` sans ses `#MIVA` peut
vider les valeurs existantes. Cette question reste ouverte sur certains dossiers : la poser
plutôt que la supposer.

## Exemple — modification du code taxe d'un compte existant

```
#FLG 000
#VER 31
#DEV EUR
#MPLG
49500000
0
Prov. Comptes groupe et associés
Prov. Comptes gro
6
2


1
0
0
0
0
0
0
050123

0
0
A20
0
0
0
#FIN
```

Le fichier réel est encodé en CP850 (le `é` de « associés » vaut l'octet `\x82`) avec des fins
de ligne CRLF.
