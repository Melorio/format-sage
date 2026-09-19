# `#MCJR` — Codes journaux

**Encodage : CP850. Fins de ligne : CRLF. 16 champs par bloc, pas de ligne vide de séparation.**

## L'écart doc / fichier réel

La documentation éditeur v12.25 décrit **13 champs**. Les fichiers réels en contiennent
**16** : trois champs de fin ne sont pas documentés. Un bloc de 13 lignes produit en se fiant
à la seule documentation décale tout ce qui suit.

C'est le cas d'école qui justifie la règle générale de cette skill : la documentation donne
les noms et les énumérations, l'export donne la structure.

## Structure constatée

| # | Champ | Valeurs | Commentaire |
|---|---|---|---|
| 1 | Code journal | `ACH`, `VTE`, `BEU`, `CAIS` | 6 caractères |
| 2 | Intitulé | `Achats`, `Caisse` | 35 caractères |
| 3 | Compte général de trésorerie | `5125`, `5310`, vide | Vide hors journaux de trésorerie |
| 4 | Type | `0`..`4` | 0 Achat · 1 Vente · 2 Trésorerie · 3 Général · 4 Situation |
| 5 | Type numérotation pièce | `0`..`3` | 0 Manuelle · 1 Continue par journal · 2 Continue pour le fichier · 3 Mensuelle |
| 6 | Option contrepartie / ligne | `0` / `1` | Non / Oui |
| 7 | Option saisie analytique | `0` / `1` | Non / Oui |
| 8 | Type rapprochement | `0`..`2` | Aucun · Contrepartie · Trésorerie |
| 9 | Mise en sommeil | `0` / `1` | Non / Oui |
| 10 | Option calcul totaux | `0` / `1` | Non / Oui |
| 11 | Réservé IFRS | `0` / `1` | Non / Oui |
| 12 | Règlement définitif | `0` / `1` | Non / Oui |
| 13 | Suivi trésorerie | `0` / `1` | Non / Oui |
| 14 | *non documenté* | `0` / `1` | Reprendre la valeur d'un journal existant de même type |
| 15 | *non documenté* | `0` | idem |
| 16 | *non documenté* | vide | idem |

Les positions 1 à 13 suivent l'ordre de la documentation et concordent avec les données
réelles : les journaux de type `0` (Achat) ont un compte de trésorerie vide, ceux de type `2`
portent un compte `512x` ou `531x`. Les positions 14 à 16 sont structurellement certaines,
leur signification ne l'est pas — ne pas les inventer, les recopier.

## Exemple réel — journal d'achat

```
#MCJR
ACH
Achats

0
2
0
1
0
0
0
0
0
1
0
0

```

La dernière ligne est le 16ᵉ champ, vide. Le bloc occupe 17 lignes, drapeau compris.

## En modification

Sage réécrit l'enregistrement entier. Pour changer le seul type de numérotation d'un journal,
lire son bloc complet dans l'export du dossier client, modifier la position 5, et réémettre
les 15 autres champs à l'identique.
