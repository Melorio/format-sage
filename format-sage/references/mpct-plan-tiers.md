# `#MPCT` — Plan tiers

**Encodage : CP850. Fins de ligne : CRLF. 133 champs fixes + 1 à n comptes rattachés.**

Le bloc fait donc **au minimum 134 lignes**. Dans l'export du dossier de démonstration,
63 tiers sur 64 font 134 lignes (un compte rattaché) et un tiers en fait 135 (deux comptes).

## Le champ répété — position 134 et suivantes

Le dernier champ est *« répété autant de fois que de comptes généraux rattachés »* :

```
... champs 1 à 133 ...
4010000        ← compte rattaché 1   (ligne 134)
4040000        ← compte rattaché 2   (ligne 135, facultatif)
#MPCT          ← tiers suivant
```

Deux conséquences pour le code :

- à l'écriture, `nb_lignes` vaut `None` et seul le minimum de 134 est contrôlé — une valeur
  fixe rejetterait à tort les tiers multi-comptes ;
- à la lecture d'un export, ne jamais supposer un pas de 134 lignes : repérer les positions
  des marqueurs `#MPCT` et découper entre deux marqueurs.

## Sous-blocs enfants

Un `#MPCT` est suivi des sous-blocs propres à ce tiers, qui font partie du même enregistrement
logique. Ordre observé :

| Drapeau | Objet | Lignes |
|---|---|---|
| `#MCDL` | Lieux de livraison | 17 |
| `#MRLT` | Niveaux de relance | 11 |
| `#MBQT` | Banques du tiers | 21 |
| `#MCTT` | Contacts | 13 |
| `#MIVA` | Informations libres | 8 |

Tous sont facultatifs. Un `#MBQT` rencontré après un `#MPCT` appartient à **ce** tiers : un
parseur à plat le rattacherait au mauvais enregistrement.

## Pièges de champs

- **Dates** : format `JJMMAA` ou chaîne vide. Jamais `0`.
- **Montants et taux** : virgule décimale, avec la précision du champ — les positions 30-31
  sont à deux décimales (`0,00`), les positions 35-38 à quatre (`0,0000`). Recopier la
  précision de l'export plutôt que de la deviner.
- Position 3 : type de tiers. Position 4 : compte collectif — il doit rester cohérent avec le
  compte rattaché de la position 134.
- Position 32 : code du tiers centralisateur, souvent le code du tiers lui-même.

## En modification

Un import `#MPCT` réécrit tout l'enregistrement. Pour changer un seul champ, partir du bloc
complet de l'export client, modifier la position visée, réémettre les 133 autres à
l'identique, comptes rattachés compris. Un bloc reconstruit « au mieux » vide silencieusement
les champs non renseignés.
