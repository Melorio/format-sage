# Exemples

## `plan-comptable.json` — format d'une spécification

Une spécification est un simple JSON : une liste de blocs, chacun composé d'un drapeau et de
ses champs, **dans l'ordre et au complet**. Un champ vide se déclare `""` — jamais omis.

```json
{
  "module": "CPTA",
  "blocs": [
    {"drapeau": "MPLG", "champs": ["49500000", "0", "Prov. Comptes groupe", "..."]}
  ]
}
```

La clé `module` (`CPTA`, `GC` ou `IMMO`) n'est nécessaire que lorsque le fichier ne contient
que des drapeaux partagés entre modules, dont la déduction automatique est impossible.
Les cardinalités diffèrent alors : `#MPCT` compte 134 champs en Comptabilité et 130 aux
Immobilisations.

## Produire et contrôler

```bash
cd format-sage/scripts
python ecrire_sage.py --spec ../../exemples/plan-comptable.json --sortie DEMO_MPLG_20260919.txt
python valider_sage.py DEMO_MPLG_20260919.txt
```

`DEMO_MPLG_20260919.txt` est le résultat de cette commande, versionné ici comme référence :
52 lignes, 280 octets, CP850, CRLF.

## En pratique

Écrire un script Python ad hoc pour préparer la spécification — parcours d'un CSV, croisement
avec l'export client, conversion des dates et des montants — est la démarche normale. C'est la
**génération du fichier final** qui doit passer par `ecrire_sage.py`, afin que l'en-tête,
l'encodage, les fins de ligne et le nombre de champs ne dépendent pas d'une écriture manuelle.
