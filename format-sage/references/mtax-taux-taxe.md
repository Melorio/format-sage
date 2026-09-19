# `#MTAX` — Taux de taxe

**Encodage : CP850. Fins de ligne : CRLF. 15 champs fixes + N comptes HT, pas de ligne vide de séparation.**

## Structure du fichier

```
#FLG 000
#VER 31
#DEV EUR
#MTAX
<champ 1>
...
<champ 15>
<compte HT 1>      ← facultatif, répétable
<compte HT 2>
#MTAX
...
#FIN
```

## Ordre des champs

| # | Champ | Format / valeurs |
|---|---|---|
| 1 | Intitulé | 35 caractères max (ex. `TVA collectée 20%`) |
| 2 | Type taux | 0=Taux, 1=Montant, 2=Quantité |
| 3 | Taux | 14 caractères numériques, selon le type taux (ex. `20,00`) |
| 4 | Type | 0=TVA/débit, 1=TVA/encaissement, 2=TP/HT, 3=TP/TTC, 4=TP/Poids, 5=TVA/CEE, 6=Surtaxe, 7=IRPF (Espagne), 8=IRPF Agraire (Espagne), 9=IGIC (Espagne) |
| 5 | Numéro compte général TVA | 13 caractères max (ex. `44571000`) |
| 6 | **Code taxe** | 5 caractères max (ex. `A20`, `D20`) — c'est la clé référencée par le champ 20 du `#MPLG` et le champ 25 du `#MECG` |
| 7 | Taxe non perçue | 0=Non, 1=Oui |
| 8 | **Sens** | 0=Déductible sur les achats, 1=Collectée sur les ventes |
| 9 | Provenance | 0=Nationale, 1=Intracommunautaire, 2=Export, 3..7=Divers 1 à 5 |
| 10 | Code regroupement | 5 caractères majuscules |
| 11 | Assujettissement | 14 caractères numériques |
| 12 | Grille base | 3 caractères majuscules |
| 13 | Grille taxe | 3 caractères majuscules |
| 14 | Code EDI | 3 caractères |
| 15 | Mention exonération TVA | 100 caractères max |
| 16+ | Numéro compte général HT | 3 à 13 caractères, **répétable N fois** — un champ par ligne |

Le nombre de comptes HT est variable d'un taux à l'autre. Le validateur accepte donc tout bloc
`#MTAX` d'au moins 15 champs.

## Points d'attention

- **Le code taxe (champ 6) est une clé partagée.** Avant de générer un `#MPLG` avec un code
  taxe en champ 20, ou un `#MECG` avec un code taxe en champ 25, vérifier que ce code existe
  dans la table des taxes du dossier — un code inconnu fait échouer ou dériver l'import.
- **Le sens (champ 8) est la source d'erreur la plus fréquente** : un taux d'achat déclaré en
  collecté fausse silencieusement la déclaration de TVA. Le faire confirmer.
- **Format décimal** : virgule décimale, comme partout dans le format Sage (`20,00`, pas `20.00`).
- **Modification d'un taux existant** : même règle que pour le plan comptable — repartir de
  l'export du dossier et ne changer que les champs ciblés, en conservant les comptes HT
  rattachés, sous peine de les perdre.

## Exemple — un taux de TVA collectée à 20 %

```
#FLG 000
#VER 31
#DEV EUR
#MTAX
TVA collectée 20%
0
20,00
0
44571000
A20
0
1
0




0

70600000
#FIN
```

Ici : champ 10 à 14 vides, champ 15 (mention d'exonération) vide, puis un compte HT rattaché
(`70600000`). Fichier réel encodé en CP850, fins de ligne CRLF.
