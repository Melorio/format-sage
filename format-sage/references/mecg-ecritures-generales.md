# `#MECG` — Écritures générales

**Encodage : CP850. Fins de ligne : CRLF. 38 champs + 1 ligne vide de séparation par bloc.**

> **Correction.** Une version antérieure de cette fiche annonçait CP1252 pour `#MECG`. C'est
> faux. L'export complet du dossier de démonstration contient l'octet `\x82` dans
> `Cr\x82dit-bail mobilier` : `\x82` vaut `é` en CP850 et `‚` en CP1252. **Tous les formats
> Sage 100 sont en CP850**, écritures comprises. Contrôle :
> `open(f,'rb').read().decode('cp850')` doit afficher les accents correctement.

C'est le format le plus piégeux des trois. Trois règles ont été établies empiriquement et
coûtent un import raté chacune si on les oublie.

## Règle 1 — Chaque bloc fait 40 lignes

```
#MECG          ← 1 ligne de drapeau
<champ 1>
...
<champ 38>     ← 38 lignes de champs
               ← 1 LIGNE VIDE de séparation
#MECG          ← bloc suivant
```

Symptôme si on l'oublie : Sage signale une « incohérence » toujours à la même position — la
première ligne du 2ᵉ bloc. Règle vérifiée sur les 279 blocs `#MECG` du dossier de démonstration.

**Attention — cette ligne vide est propre à `#MECG`.** Les blocs annexes du même fichier n'en
ont pas : sur le dossier de démonstration, `#MRGT` compte 91 champs et `#MECA` 4 champs (numéro analytique,
section, montant, quantité), sans ligne vide finale. Ne pas généraliser le séparateur par
symétrie. Lecture équivalente, si elle vous parle davantage : `#MECG` a 39 champs dont le 39ᵉ
est toujours vide — les octets produits sont identiques.

## Règle 2 — Une ligne du CSV = un bloc `#MECG`

Chaque paire débit/crédit produit **deux blocs distincts**, avec le même numéro de pièce et le
même numéro de facture : l'un avec Sens=0 et le montant au débit, l'autre avec Sens=1 et le
montant au crédit.

L'hypothèse « un seul bloc avec le compte de contrepartie en champ 8 » a été **testée et
invalidée** : Sage refuse l'import avec « Les écritures générales ne sont pas équilibrées pour
le journal … ». Le champ 8 ne sert pas à l'équilibrage automatique. Le laisser vide.

## Règle 3 — L'équilibre débit/crédit se contrôle avant livraison

Somme des montants Sens=0 = somme des montants Sens=1, sur l'ensemble du fichier **et journal
par journal** si le fichier en couvre plusieurs. `scripts/valider_sage.py` fait ce contrôle.

## Ordre des 38 champs

| # | Champ | Source / valeur par défaut |
|---|---|---|
| 1 | Code journal | 6 caractères (ex. `ACH`, `VTE`, `OD`). Reporter vers le bas si vide dans le CSV |
| 2 | Date de pièce | JJMMAA (conversion depuis JJ/MM/AAAA). Reporter vers le bas si vide |
| 3 | Date de saisie | JJMMAA — généralement identique au champ 2 |
| 4 | Pièce | Séquence 1, 2, 3… par groupe de « Numéro facture ». **Identique pour les 2 blocs d'une même pièce** |
| 5 | Numéro facture | 17 caractères |
| 6 | Pièce trésorerie | vide |
| 7 | N° compte général | de la ligne CSV correspondante |
| 8 | N° compte général contrepartie | **vide** (cf. règle 2) |
| 9 | N° compte tiers | de la ligne CSV, ou vide |
| 10 | N° compte tiers contrepartie | vide |
| 11 | Intitulé (libellé écriture) | 69 caractères max |
| 12 | Numéro règlement | `0` (0..30) |
| 13 | Échéance | vide, ou JJMMAA |
| 14 | Parité | `0,000000` |
| 15 | Quantité | `0,00` |
| 16 | Numéro devise | `0` |
| 17 | **Sens** | `0`=Débit, `1`=Crédit |
| 18 | **Montant** | valeur non vide de la ligne CSV, séparateurs de milliers supprimés, virgule décimale conservée (`1200,00`) |
| 19 | Numéro lettrage | vide |
| 20 | Numéro pointage | vide |
| 21 | Numéro lettrage quantité | vide |
| 22 | Nombre de rappels | `0` |
| 23 | Type à-nouveau | `0`=Normale, 1=reprise en Détail, 2=reprise en Solde, 3=AN Manuel, 4=AN Résultat |
| 24 | Type révision | `0`=Non, 1=Oui |
| 25 | Montant devise | vide |
| 26 | **Code taxe** | vide, ou 5 caractères majuscules (ex. `D20`) — doit exister dans la table `#MTAX` |
| 27 | Norme | `0`=Les deux, 1=Nationale, 2=IFRS |
| 28 | Provenance | `0`=Aucune, 1=Nationale, 2=Intracommunautaire, 3=Export, 4..8=Divers |
| 29 | Type pénalités | `0`=Aucun, 1=Intérêts de retard, 2=Frais d'impayés |
| 30 | Date pénalités | vide |
| 31 | Date relance | vide |
| 32 | Date rapprochement | vide |
| 33 | Référence | vide (17 caractères max) |
| 34 | Statut règlement | `0`=Non réglé, 1=À traiter GC, 2=Traité GC |
| 35 | Montant réglé | `0,00` |
| 36 | Date opération | vide |
| 37 | Date clôture | vide |
| 38 | Export rapprochement | `0`=Non exporté, 1=Exporté |

**Valeurs par défaut des champs 19 à 38** (bloc simple, sans TVA ni analytique), telles
qu'observées dans le dossier de démonstration :

```
"", "", "", "0", "0", "0", "", "", "0", "0", "0", "", "", "", "", "0", "0,00", "", "", "0"
```

Les champs 19 à 38 ne sont pas détaillés dans la documentation Sage officielle : la
correspondance ci-dessus est une déduction empirique validée pour le cas simple. Pour un cas
qui en sort, repartir du dossier de démonstration plutôt que d'extrapoler.

## Mapping depuis un CSV « import paramétrable »

Colonnes usuelles : `* Code journal ; * Date de pièce ; Numéro facture ; * N° compte général ;
N° compte tiers ; Libellé écriture ; Montant débit ; Montant crédit`.

Traitement :
1. Regrouper les lignes par « Numéro facture » pour attribuer le numéro de pièce (champ 4).
2. Reporter vers le bas le code journal et la date quand la cellule est vide (fréquent sur la
   ligne de banque).
3. Convertir les dates JJ/MM/AAAA → JJMMAA, et les montants en supprimant les espaces de
   milliers tout en conservant la virgule décimale.
4. Émettre un bloc par ligne du CSV : Sens=0 si « Montant débit » est rempli, Sens=1 si
   « Montant crédit » l'est.
5. Contrôler l'équilibre, puis générer.

## Cas non couverts par le mapping simple

- **TVA** : nécessite un bloc `#MRGT` (registre taxe, 91 champs, sans ligne vide) après le
  `#MECG` concerné, avec le code taxe en champ 26 du `#MECG`.
- **Analytique** : nécessite un bloc `#MECA` (4 champs, sans ligne vide) après le `#MECG`.

Dans ces deux cas, prévenir l'utilisateur que le mapping simple ne suffit pas et s'appuyer sur
un modèle de fichier réel du dossier (par exemple les blocs « ENGIE TEST ACH REG TAXE » du
dossier de démonstration) plutôt que de reconstruire les champs de mémoire.

## Extrait du modèle de référence (premier bloc BIJOU)

```
#MECG
ACH
300123
180924
5
FAC

4010000

DUBOI

REGLEMENT DUBOI
1
310323
0,000000
0,00
0
1
1200,00
```
(…suite des champs 19 à 38, puis la ligne vide de séparation.)
