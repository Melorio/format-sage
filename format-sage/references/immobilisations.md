# Sage 100 Immobilisations — format d'import (`#VER 23`, doc v11.00)

Fiche autoportante. Toutes les valeurs ci-dessous ont été **réconciliées ligne à ligne** entre
la documentation officielle v11.00 et un export réel complet (modèle BIJOU, 35 291 lignes,
39 immobilisations, 593 plans d'amortissement). Les écarts doc/réel sont signalés explicitement.

> **BIJOU est un dossier de démonstration** servant uniquement à l'analyse structurelle.
> Il ne doit jamais apparaître comme nom de dossier dans un fichier livré.

---

## 1. En-tête — différent de la Comptabilité

```
#FLG 000
#VER 23
```

**Deux lignes seulement.** C'est la principale cause de rejet quand on recopie l'en-tête
Comptabilité :

| Module | Ligne 1 | Ligne 2 | Ligne 3 |
|---|---|---|---|
| Comptabilité | `#FLG 000` | `#VER 31` | `#DEV EUR` |
| Gestion commerciale | `#FLG 000` | `#VER 33` | *(aucune)* |
| **Immobilisations** | `#FLG 000` | **`#VER 23`** | *(aucune)* |

- `#VER 23` et non `#VER 31` : le module Immobilisations a son propre numéro de version de format.
- **Pas de `#DEV EUR`** : provoque un rejet « Fichier inconnu ligne : 3 ».
- Fin de fichier : `#FIN`.

## 2. Encodage et fins de ligne

- **CP850**, confirmé au niveau octet sur l'export réel :
  `é`=`\x82`, `â`=`\x83`, `à`=`\x85`, `ç`=`\x87`, `ê`=`\x88`, `è`=`\x8a`, `ô`=`\x93`, `û`=`\x96`,
  `£`=`\x9c`, `ß`=`\xe1`, `°`=`\xf8`, espace insécable=`\xff`.
- **CRLF (`\r\n`) sur toutes les lignes**, y compris la dernière après `#FIN`.
- Écriture : `open(p,'wb').write((CRLF.join(lignes)+CRLF).encode('cp850'))`.
- Lecture d'un export : `open(f,'rb').read().decode('cp850').split('\r\n')`.
  Ne jamais utiliser `.splitlines()` (laisse des `\r` qui font échouer les comparaisons de drapeaux).

## 3. Formats de données

| Type | Format | Exemple |
|---|---|---|
| Date (majorité des drapeaux `#I…`) | **`JJMMAAAA`** — 8 chiffres | `01022017` |
| Date (`#IDOS` « dernière période archivée ») | `JJMMAA` — 6 chiffres | `311223` |
| Montant | virgule décimale, pas de séparateur de milliers | `300000,00` |
| Taux / coefficient | virgule décimale, 4 décimales | `2,5000` |
| Booléen | `0` / `1` | |
| Champ vide | ligne vide — **jamais un champ omis** | |

Attention : la Comptabilité utilise `JJMMAA` (6 chiffres) pour ses dates d'écriture, les
Immobilisations `JJMMAAAA` (8 chiffres). Ne pas transposer.

---

## 4. Trois familles de drapeaux — distinction structurelle essentielle

C'est la particularité du format Immobilisations, et la source d'erreur n° 1.

### a) Drapeaux « enregistrement » — le drapeau se répète

Un drapeau par enregistrement, nombre de champs fixe. Comportement classique.

`#IIMO`, `#IPLAN`, `#IFAM`, `#ILOY`, `#ILIE`, `#ICESPLAN`, `#ISERIE`, `#IPAI`, `#IENA`, `#IEIN`,
`#MPLG`, `#MPCT`, `#MCJR`, `#MBQT`, `#MCTT`, `#MCDL`, `#MRLT`, `#MPGA`.

### b) Drapeaux « table » — le drapeau apparaît **une seule fois**, le groupe de champs se répète

Le drapeau est écrit une fois, suivi de N répétitions du groupe de champs, à plat.
Le nombre de répétitions est **fixe et imposé par Sage** (taille de la table).

| Drapeau | Groupe | × | Total | Table |
|---|---:|---:|---:|---|
| `#INIC` | 1 | 30 | 30 | Niveaux d'analyse |
| `#IANA` | 23 | 11 | 253 | Plans analytiques |
| `#IBIE` | 4 | 10 | 40 | Natures de bien |
| `#IFIS` | 2 | 10 | 20 | Natures fiscales |
| `#IACQ` | 1 | 10 | 10 | Natures d'acquisition |
| `#INAT` | 3 | 10 | 30 | Natures de sortie |
| `#ISTA` | 1 | 10 | 10 | Champs statistiques |
| `#ISTT` | 1 | 10 | 10 | Statistiques tiers |
| `#IRIS` | 4 | 10 | 40 | Codes risque |
| `#IDEV` | 20 | 32 | 640 | Devises |
| `#IREG` | 10 | 30 | 300 | Modes de règlement |
| `#INCP` | 14 | 130 | 1820 | Natures de compte |
| `#ITTI` | 34 | 4 | 136 | Types de tiers |
| `#ISBQ` | 10 | 4 | 40 | Structures banque |
| `#MSCT` | 2 | 30 | 60 | Services contacts |
| `#MTCO` | 1 | 30 | 30 | Types contacts |

> Une table doit être écrite **entière** : les 10 natures fiscales, même si 5 sont vides.
> Les emplacements inutilisés sont remplis par un intitulé vide + les valeurs par défaut
> (voir l'export du dossier). Tronquer la table décale tout le reste du fichier.

**`#ITTI` (34 = 4 + 3×10)** : dans chacun des 4 blocs, les 4 premiers champs sont uniques,
les 3 derniers (Type compte, Compte, …) sont répétés 10 fois.

**`#IANA` (23 par plan)** : 5 champs de plan, puis 6 ruptures analytiques × 3 champs.
La doc ne décrit qu'un champ « Nom rupture analytique » : le fichier réel en porte 3 par rupture.

### c) Drapeaux « à cardinalité variable » — longueur dépendante du paramétrage

Le nombre de champs dépend du dossier. **Toujours le déduire de l'export client**, jamais d'une
constante.

| Drapeau | Structure | Observé (BIJOU) |
|---|---|---|
| `#IDOS` | **71 champs fixes + 2 × nombre d'exercices** (début/fin) | 127 = 71 + 2×28 |
| `#ICOEF` | 1 (type) + 4 × nombre de dates d'application | 9 et 13 |
| `#IINF` | 1 (type de fichier) + 5 × nombre d'informations libres | 6, 11, 21, 41 |
| `#IIVA` | 1 × nombre d'informations libres du fichier parent | 4 (immo), 8 (tiers) |
| `#ISAV` | 1 (n° champ stat.) + 1 × nombre d'énumérés | 6 |
| `#ISTV` | 1 (n° champ stat.) + 1 × nombre d'énumérés | 2 |
| `#MMDG` | 3 + 4 × nombre de lignes de grille | 11, 15 |
| `#MPCT` | 129 fixes + 1 × nombre de comptes généraux rattachés | 130, 131 |

---

## 5. Ordre des blocs

L'export complet suit un ordre strict. Un import partiel n'a pas besoin de tout contenir,
mais **l'ordre relatif des blocs présents doit être respecté** : un enfant suit toujours son parent.

```
#FLG 000 / #VER 23
  Paramètres dossier : #IDOS #IDEV #INIC #IANA #IENA #IBIE #IFIS #IACQ #INAT #ICOEF
                       #ISTA #ISAV #ISTT #ISTV #IRIS #IREG #IPAI #ITTI #INCP #ISBQ
                       #MSCT #MTCO #MPLB #IINF #MCTD #IEIN
  Structure comptable : #MPLG (+#MPGA) #MPCT (+#MCDL #MRLT #MBQT #MCTT #IIVA) #MCJR #MMDG
  Immobilisations     : #IFAM #ILIE #IIMO (+#IIVA +#ISERIE +#IPLAN… +#ICESPLAN +#ILOY…)
#FIN
```

**Blocs enfants de `#IIMO`**, dans cet ordre :
1. `#IIVA` — valeurs des informations libres (autant de champs que d'informations définies)
2. `#ISERIE` — 1 champ par numéro de série (si champ 19 de `#IIMO` = `1`)
3. `#IPLAN` — un bloc de 10 champs **par exercice et par type d'amortissement**
4. `#ICESPLAN` puis `#ISERIE` — en cas de cession
5. `#ILOY` — un bloc de 2 champs par échéance (crédit-bail / location)

Sur BIJOU : 39 `#IIMO` pour 593 `#IPLAN` et 253 `#ILOY`.

---

## 6. `#IIMO` — Immobilisations · **110 champs**

| # | Champ | Codes |
|---:|---|---|
| 1 | Type immobilisation | 0 : Bien · 1 : Crédit-bail · 2 : Location |
| 2 | Code | 10 car. alphanum. — **clé de l'immobilisation** |
| 3 | Code rattaché | 10 car. (composant) |
| 4 | Désignation | 69 car. |
| 5 | Complément | 35 car. |
| 6 | Code famille | 13 car. — doit exister en `#IFAM` |
| 7 | Lieu | 69 car. — doit exister en `#ILIE` |
| 8 | Fournisseur | 17 car. |
| 9 | Compte | 14 car. |
| 10 | Tiers | 69 car. |
| 11 | N° de pièce | 13 car. **strictement alphanumériques** — voir ci-dessous |
| 12 | Valeur acquisition | 14 car. num. |
| 13 | Valeur résiduelle | 14 car. num. |
| 14 | Date acquisition | JJMMAAAA |
| 15 | Date mise en service | JJMMAAAA |
| 16 | Quantité | 9 car. num. |
| 17 | Taux TVA | 14 car. num. |
| 18 | TVA déductible | 14 car. num. |
| 19 | Gestion des numéros de série | 0 : Non · 1 : Oui → conditionne `#ISERIE` |
| 20 | Code barres | 18 car. majuscules |
| 21 | Type | 0 : Neuf · 1 : Occasion |
| 22 | Nature fiscale | 1..10 — indice dans la table `#IFIS` |
| 23 | Nature acquisition | 1..10 — indice dans la table `#IACQ` |
| 24–33 | Énumérés statistiques 1 à 10 | 21 car. — indices dans `#ISTA`/`#ISAV` |
| 34 | Compte immobilisation | |
| 35 | Compte amortissement économique | |
| 36 | Compte dotation économique | |
| 37 | Compte amortissement dérogatoire | |
| 38 | Compte dotation dérogatoire | |
| 39 | Compte reprise dérogatoire | |
| 40 | Compte valeur comptable | |
| 41 | Compte créance | |
| 42 | Compte produit de cession | |
| 43 | Compte TVA collectée | |
| 44 | Compte dotation exceptionnelle | |
| 45 | Compte reprise exceptionnelle | |
| 46 | Compte provision pour dépréciation | |
| 47 | Compte dotations aux provisions | |
| 48 | Compte reprise sur provisions | |
| 49 | Mode amortissement **économique** | 0 : Linéaire · 1 : Dégressif normal · 2 : Dégressif minoré · 3 : Dégressif majoré · 4 : Exceptionnel · 5 : Manuel |
| 50 | Durée (année) économique | 0..999 |
| 51 | Durée (mois) économique | 0..11 |
| 52 | Départ économique | 0 : Date acquisition · 1 : Date mise en service |
| 53 | Coefficient économique | 14 car. num. |
| 54 | Prorata économique | 0 : Jours · 1 : Mois · 2 : Aucun |
| 55–60 | Idem pour l'amortissement **fiscal** | même ordre : mode, durée an, durée mois, départ, coefficient, prorata |
| 61–66 | Idem **natif** | |
| 67–72 | Idem **économique IFRS** | |
| 73–78 | Idem **natif IFRS** | |
| 79 | Base d'amortissement économique | |
| 80 | Base d'amortissement fiscale | |
| 81 | Base d'amortissement native | |
| 82 | Base d'amortissement économique IFRS | |
| 83 | Base d'amortissement native IFRS | |
| 84 | Bloc-notes | 255 car. |
| 85 | Début location | JJMMAAAA |
| 86 | Fin location | JJMMAAAA |
| 87 | Montant loyer | |
| 88 | Valeur locative | |
| 89 | Prix d'achat résiduel | |
| 90 | Type périodicité | 0 : Jour · 1 : Semaine · 2 : Mois · 3 : Année |
| 91 | Durée périodicité | 0..999 |
| 92 | Loyer à réintégrer | |
| 93 | Soumis à taxe véhicule | 0/1 |
| 94 | Prix de revient bien | |
| 95 | Type d'origine | 0 : Aucun · 1 : Rachat crédit-bail · 2 : Rachat location |
| 96 | Date de rachat | JJMMAAAA |
| 97 | Code analytique | |
| 98 | N° immatriculation | 9 car. |
| 99 | Date immatriculation | JJMMAAAA |
| 100 | Date première circulation | JJMMAAAA |
| 101 | Genre | 4 car. |
| 102 | Marque | 10 car. |
| 103 | Type carrosserie | 8 car. |
| 104 | Puissance administrative | 0..99 |
| 105 | Code carte grise | 2 car. |
| 106 | Réception communautaire | 0/1 |
| 107 | CO2 grammes/km | |
| 108 | Composé | 0/1 |
| 109 | Non immobilisée IFRS | 0/1 |
| 110 | Contrat de location financement | 0/1 |

Les 5 jeux d'amortissement (49→78) sont toujours écrits, même si le dossier n'utilise
que l'économique : mettre `0` partout plutôt que des champs vides.

## 7. `#IPLAN` — Plan d'amortissement · **10 champs**

Un bloc **par exercice et par type d'amortissement**. Suit l'`#IIMO` concerné.

| # | Champ | Codes |
|---:|---|---|
| 1 | Type amortissement | 0 : Économique · 1 : Fiscal · 2 : Natif · 3 : Économique IFRS · 4 : Natif IFRS |
| 2 | Début exercice | JJMMAAAA |
| 3 | Fin exercice | JJMMAAAA |
| 4 | État | 1..13 |
| 5 | Mise à jour en comptabilité | 0/1 |
| 6 | Valeur début | montant |
| 7 | Dotation | montant |
| 8 | Début période | JJMMAAAA |
| 9 | Fin période | JJMMAAAA |
| 10 | État origine | 1..13 |

Exemple réel : `0 | 01012017 | 31122017 | 6 | 0 | 250000,00 | 11458,33 | 01012017 | 31122017 | 6`

## 8. `#IFAM` — Familles · **58 champs**

| # | Champ | Codes |
|---:|---|---|
| 1 | Code famille | 13 car. |
| 2 | Type | 1 : Détail · 2 : Total |
| 3 | Intitulé | 35 car. |
| 4 | Nature de bien | 0..10 (indice `#IBIE`) |
| 5 | Nature fiscale | 0..10 (indice `#IFIS`) |
| 6–15 | Énumérés statistiques 1 à 10 | |
| 16–30 | Comptes | même ordre que `#IIMO` champs 34→48 |
| 31–35 | Amortissement économique | mode, durée an, durée mois, départ, prorata (**pas de coefficient**) |
| 36–40 | Amortissement fiscal | idem |
| 41–45 | Amortissement natif | idem |
| 46–50 | Amortissement économique IFRS | idem |
| 51–55 | Amortissement natif IFRS | idem |
| 56 | Base amortissement | |
| 57 | Plancher | |
| 58 | Code analytique | |

> Différence avec `#IIMO` : les groupes d'amortissement de `#IFAM` comptent **5 champs**
> (sans coefficient), contre 6 dans `#IIMO`. Ne pas copier le mapping de l'un vers l'autre.

## 9. Autres drapeaux Immobilisations courants

| Drapeau | Champs | Contenu |
|---|---:|---|
| `#ILOY` | 2 | Date loyer (JJMMAAAA), Montant loyer — un bloc par échéance |
| `#ISERIE` | 1 | Un numéro de série — un bloc par numéro |
| `#ILIE` | 12 | Intitulé, Adresse, Complément, CP, Ville, Région, Pays, Interlocuteur, Principal, Tél, Fax, Email |
| `#ICESPLAN` | 18 | Date, Qté cédée, Nature sortie, Valeur cession, Règle TVA, Taux TVA, Montant TVA, Commentaire, +/- value CT, +/- value LT, TVA reversée, 5 dotations, Régime +/- value, Dotation amorts exceptionnels |
| `#IEIN` | 3 | N° de fichier (0 immo · 1 tiers · 2 sections · 3 comptes généraux), N° information libre, Intitulé |
| `#IPAI` | 8 | Table des pays (drapeau répété) |
| `#IDOS` | 71 + 2×N | Identité dossier, comptes par défaut, exercices |

## 10. Drapeaux partagés avec la Comptabilité

Présents dans un export Immobilisations complet, avec des cardinalités **propres à la v11** :

| Drapeau | Champs (réel) | Doc v11 | Remarque |
|---|---:|---:|---|
| `#MPLG` | 23 | 23 | identique à la fiche `mplg-plan-comptable.md` |
| `#MPGA` | 4 | 4 | répartition analytique, suit `#MPLG` |
| `#MCJR` | 16 | 16 | codes journaux |
| `#MCTT` | 13 | 13 | contacts tiers |
| `#MBQT` | 21 | 21 | banques tiers |
| `#MCDL` | **17** | 16 | ⚠ un champ de plus dans le fichier réel |
| `#MRLT` | 11 | 6 lignes | la ligne « Jours tombée » vaut 6 champs → 3 + 6 + 2 = 11 |
| `#MPCT` | **130 / 131** | 107 lignes | 129 fixes + n comptes généraux |
| `#MCTD` | 19 | 19 | contacts dossier |
| `#MPLB` | 3 | — | **non documenté** : 3 champs vides observés |

> ⚠ Ces cardinalités sont celles du **format Immobilisations v11**. Elles diffèrent de la
> Comptabilité v12.25 (`#MPCT` y compte 134 champs). Ne pas réutiliser un mapping `#MPCT`
> Comptabilité dans un fichier Immobilisations sans le revalider sur un export du dossier.

---

## 10 bis. Contrainte de caractères sur le n° de pièce — établie par test d'import réel

Le champ 11 de `#IIMO` n'accepte **que des lettres et des chiffres**. Un tiret suffit à faire
rejeter l'enregistrement entier. Vérifié par bissection sur un dossier réel :

| Valeur testée | Longueur | Résultat |
|---|---|---|
| *(vide)* | 0 | accepté |
| `FA2026014` | 9 | accepté |
| `FA-01` | 5 | **rejeté** |
| `FA2026-014` | 10 | **rejeté** |

La longueur n'est pas en cause : neuf caractères passent, cinq échouent dès qu'ils contiennent
un séparateur. Les valeurs présentes dans un dossier réel sont du type `A456`, `IO854`, `JB001`,
`PO56` — courtes et sans ponctuation.

La documentation éditeur annonce « 13 caractères alphanumériques » sans signaler que la
contrainte est stricte. À l'import, un numéro de facture de la forme `FA2026-014`, pourtant
banal dans les fichiers sources clients, fait échouer l'enregistrement. **Retirer les
séparateurs à la génération** plutôt que de les découvrir à l'import.

`valider_sage.py` contrôle désormais ce champ et reproduit le message de Sage avant l'import.

## Comment lire les numéros de ligne de Sage Immobilisations

Sage numérote les **lignes physiques du fichier**, en-tête compris. Deux cas :

- *« Une incohérence à la ligne 14 a été détectée »* → la ligne 14 du fichier, donc pour un
  premier bloc commençant ligne 3, le champ 11 de l'enregistrement.
- *« L'immobilisation 00008 existe déjà à la ligne 3 »* → la ligne du **drapeau**, quand
  l'erreur porte sur l'enregistrement entier et non sur un champ.

Pour retrouver un champ à partir d'un numéro de ligne : position = ligne − ligne du drapeau.

## Méthode de diagnostic quand un import échoue

Raisonner sur le fichier fautif fait perdre du temps. Isoler par bissection :

1. **Copie conforme** — réémettre un enregistrement réel de l'export, sans aucune modification.
   S'il est refusé, le problème est structurel ; s'il passe (ou signale « existe déjà »), la
   structure est bonne et la cause est dans les valeurs.
2. **Création** — même bloc, seul le code changé. Sépare la structure du cas de la création.
3. **Une modification à la fois** — réintroduire les valeurs métier champ par champ.

Trois allers-retours suffisent généralement. C'est ainsi qu'a été établie la contrainte
ci-dessus, après trois hypothèses erronées formulées sans mesure.

## 11. Pièges à contrôler avant livraison

1. **En-tête à 2 lignes** (`#VER 23`, pas de `#DEV`) — erreur la plus fréquente.
2. **Dates sur 8 chiffres** (`JJMMAAAA`), pas 6 comme en Comptabilité.
3. **Tables complètes** : écrire les 10 natures fiscales, les 30 modes de règlement, etc.
   Une table tronquée décale tout le fichier.
4. **`#IDOS` porte l'identité du dossier** (raison sociale, SIRET, TVA intracom., adresse).
   Contrairement aux formats Comptabilité, elle est **dans le contenu** : vérifier qu'aucune
   donnée du dossier de démonstration ne subsiste.
5. **Cohérence référentielle** : le code famille (`#IIMO` champ 6) doit exister en `#IFAM`,
   le lieu (champ 7) en `#ILIE`, les comptes (34→48) au plan comptable du dossier.
6. **`#IPLAN` doit couvrir tous les exercices** déclarés en `#IDOS`, sans trou.
7. **Ordre parent → enfants** : un `#IPLAN` orphelin (sans `#IIMO` avant lui) est rejeté.
8. **`#ISERIE` conditionné** par le champ 19 de `#IIMO` à `1`.
9. **Import destructif** : comme en Comptabilité, les champs non renseignés écrasent
   l'existant. Pour une modification, partir de l'export du dossier et ne changer que la cible.
10. **N° de pièce sans séparateur** : champ 11 de `#IIMO`, lettres et chiffres uniquement.
11. **Caractères hors CP850** : tiret cadratin `—`, apostrophe courbe `’`, points de suspension `…`
    copiés depuis Word font échouer l'encodage. Les remplacer par `-`, `'`, `...`.

## 12. Génération et contrôle

```bash
python scripts/ecrire_sage.py --spec spec.json --module immos --sortie CLIENT_IIMO_20260911.txt
python scripts/valider_sage.py CLIENT_IIMO_20260911.txt
```

`ecrire_sage.py` écrit l'en-tête `#FLG 000` / `#VER 23`, encode en CP850, applique les CRLF et
refuse d'écrire si un bloc n'a pas le bon nombre de champs. `valider_sage.py` détecte le module
à partir de la ligne `#VER` et contrôle en plus l'ordre parent/enfant des blocs Immobilisations.

**Statut : format analysé et réconcilié doc/export réel, mais pas encore éprouvé par un import
en production.** Test obligatoire en environnement Sage de recette avant tout import réel.
