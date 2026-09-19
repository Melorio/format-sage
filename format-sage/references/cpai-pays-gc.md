# `#CPAI` — Table des pays (Gestion commerciale)

**Encodage : CP850. Fins de ligne : CRLF. 8 champs par bloc, pas de ligne vide de séparation.**

En-tête du fichier : `#FLG 000` puis `#VER 33`, **sans `#DEV EUR`**. Cette ligne appartient à
la Comptabilité ; dans un fichier de Gestion commerciale elle provoque le rejet
« Fichier inconnu ligne : 3 ».

Le nom du dossier n'apparaît nulle part dans le contenu d'un fichier `#CPAI` : il ne sert qu'au
nommage du fichier livré. Inutile donc d'en exiger la confirmation avant de générer.

## Structure

| # | Champ | Format | Exemples |
|---|---|---|---|
| 1 | Intitulé | 35 caractères | `Allemagne`, `Côte d'Ivoire` |
| 2 | Code pays | 3 caractères | `DEU`, `BEL`, `USA` |
| 3 | Code DEI | 3 caractères | `004`, `019`, `400` |
| 4 | Coefficient assurance | décimal à 4 chiffres | `1,0000` |
| 5 | Coefficient transport | décimal à 4 chiffres | `1,0000` |
| 6 | Code ISO2 | 2 caractères | `DE`, `BE`, `US` |
| 7 | SEPA | `0` / `1` | Non / Oui |
| 8 | Localisation | `0`..`4` | 0 Union européenne · 1 France · 2 Hors UE · 3 DROM · 4 COM |

Documentation et fichier réel concordent exactement : 8 champs, aucun champ répété. Les
15 pays du dossier de démonstration font tous 8 lignes.

## Pièges

- **Séparateur décimal** : virgule, jamais point. `1,0000` et non `1.0000`.
- **Localisation `1` = France**, valeur distincte de `0` = Union européenne. Elle est réservée
  au pays du dossier.
- **Cohérence SEPA / localisation** : un pays hors UE porte normalement SEPA à `0`. Sage ne
  contrôle pas cette cohérence à l'import — l'incohérence se paiera sur les règlements.
- Le drapeau `#CPAI` doit être répété avant chaque pays. Le nombre de pays est illimité.

## Exemple réel

```
#CPAI
Allemagne
DEU
004
1,0000
1,0000
DE
1
0
#CPAI
Etats unis
USA
400
1,0000
1,0000
US
0
2
```
