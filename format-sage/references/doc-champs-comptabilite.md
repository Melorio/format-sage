# Documentation éditeur Sage 100 Comptabilité v12.25 — champs par drapeau

Extraction fidèle de la documentation officielle (`#VER 31`), découpée par drapeau.

**Ne pas charger ce fichier en entier.** Extraire la seule section utile :
`grep -A 60 '^## #MCJR' references/doc-champs-comptabilite.md`

La documentation **regroupe** les champs répétés (« ce champ est répété 10 fois ») là où
le fichier réel les **développe** sur des lignes consécutives. Le nombre de champs annoncé
ici est donc presque toujours inférieur au nombre de lignes réelles : croiser avec
`catalogue-drapeaux.md` et `index-champs-empirique.md` avant d'écrire quoi que ce soit.

## #MDOS — Dossier entreprise
*Export modèle : 1 occurrence(s), 133 lignes.*

Champ Code Correspondance/Commentaire
Raison sociale 35 caractères alphanumériques
Activité 35 caractères alphanumériques
Adresse 35 caractères alphanumériques
Complément 35 caractères alphanumériques
Code postal 9 caractères alphanumériques
Ville 35 caractères alphanumériques
Code région 25 caractères alphanumériques
Pays 35 caractères alphanumériques
Commentaire 69 caractères alphanumériques
Siret 14 caractères alphanumériques
Ape 6 caractères alphanumériques
Identifiant 25 caractères alphanumériques
Début exercice 10 * (Date au format JJMMAA ou vide à 
partir du deuxième)
Fin exercice 10 * (Date au format JJMMAA ou vide à 
partir du deuxième)
Longueur comptes 
généraux 0, 3..13 0, 3..13
Longueur sections 
analytiques 0, 3..13 0, 3..13
Format quantités 31 caractères alphanumériques
Calcul code traitement 0..1
Proche
Par nature
Confirmation 
suppressions 0..2
Aucune
Eléments
Liste
Analyse grand-livre 3 * (0..99) 3 * Nombre de mois par période
Délai client maxi 0..999
Non
Oui
Ouverture compte en 
saisie
1
Non
Oui
Champ Code Correspondance/Commentaire
Gestion budgets/Axe 
général
1
Non
Oui
Suppression après 
validation
1
Non
Oui
Mise à jour registre taxe
1
Non
Après confirmation
Mise à jour automatique
Ventilation analytique 
qtés/devises 
1
Non
Quantité
Devises
Suppression extraits 
apres .incorpo.
Non
Oui
Mise à jour import
1
Non
Oui
Complément à zéro
1
Sans modification
Modification
Choix manuel
Type validation en saisie
1
Non
Oui
Impression des zéros
1
Tabulation
Entrée
Monnaie de tenue de 
compte
1
Non
Oui
Devise d''équivalence 1..32 Position dans la table des devises
Type écritures en saisie 
A.N. 1..32 Position dans la table des devises
Code journal à-nouveaux
1
Normal
A-nouveau
Compte ouverture ànouveaux
6 caractères alphanumériques ou vide
Compte bénéfice ànouveaux
3..13 caractères alphanumériques ou vide
Compte perte ànouveaux
3..13 caractères alphanumériques ou vide
TVA/encaissement : 
registres 3..13 caractères alphanumériques ou vide
TVA/encaissement : 
affectation
1
Non
Oui
Equilibre en devise
1
Prorata HT
Priorité aux taux sur les débits
Mode affectation 
analytique
1
Non
Afficher un message
Champ Code Correspondance/Commentaire
3
Modifier le montant en devises
Modifier le cours
N° pièce des règlements 
tiers
1
Manuelle
Automatique,
Après confirmation
Extourne/annulation en 
négatif
1
N° pièce
Référence pièce
Libellé
Devise de 
rapprochement
1
Non
Oui
Equilibre journal en 
import
1
Monnaie de tenue
Devise du RIB
Equilibre analytique en 
import
1
Non
Par journal/période
Compte écart 
débit/import
1
Compte écart 
crédit/import 3..13 caractères alphanumériques ou vide
Plan analytique par 
défaut 3..13 caractères alphanumériques ou vide
Numéro dossier 1..11 Position dans la table des plans analytiques
Adresse messagerie 
client 8 caractères alphanumériques majuscules
Adresse expert 69 caractères alphanumériques
Intitulé expert 69 caractères alphanumériques
Téléphone 35 caractères alphanumériques
Télécopie 21 caractères alphanumériques
Adresse eMail 21 caractères alphanumériques
Site 69 caractères alphanumériques
Appel des tiers 69 caractères alphanumériques
Appel des sections
1
Sur le numéro
Sur l'intitulé
Protection zone pièce
1
Sur le numéro
Sur l'intitulé
Numérotation continue
1
Non 
Oui
Champ Code Correspondance/Commentaire
Date dernière clôture
1
Non 
Oui
Test sur comptes de type 
Total Date au format JJMMAA ou vide
Recherche systématique 
écr.
1
Non 
Oui
Ecart
1
Non 
Oui
Compte d''attente 14 caractères numériques
Ecr.contrepartie unique 3..13 caractères alphanumériques ou vide
Synchro compta/Sens du 
transfert 
1
Non 
Oui
Synchro compta/Type
1
Client -> Expert comptable 
Expert comptable -> Client
Synchro compta/Moyen
1
Communication 
Synchronisation
Synchro compta/Logiciel
1
Messagerie 
Fichier magnétique
Synchro compta/Code 
expert
1
Sage 30 & 100 
Sage Expert 
Ciel
Synchro compta/Date 
synchro 8 caractères alphanumériques majuscules
Rappro/Type écart Date au format JJMMAA ou vide
Rappro/Report extrait
1
Ecart de montant 
Ecart de pourcentage
Rappro/Code journal 
Clients
1
Pièce de trésorerie 
Référence pièce 
N° pièce
Rappro/Modèle Clients 6 caractères alphanumériques
Rappro/Code journal 
Fournisseurs 35 caractères alphanumériques
Rappro/Modèle 
Fournisseurs 6 caractères alphanumériques
Gestion normes 
comptables IFRS 35 caractères alphanumériques
Saisie IFRS
1
Non 
Oui
Plan analytique IFRS
1
Journaux IFRS 
Tous types de journaux
Champ Code Correspondance/Commentaire
Code journal AN 
analytique 0..11 Position du plan IFRS
Code journal AN IFRS 6 caractères alphanumériques
Code journal AN 
analytique IFRS 6 caractères alphanumériques
Rappel/Solde minimum 6 caractères alphanumériques
Appliquer pré-ventilation 
comptes 14 caractères numériques
Pénalités retard/Taux
1
Non 
Oui
Pénalités 
retard/Imputation 14 caractères numériques
Pénalités retard/Code 
journal
1
Ordre des échéances 
Proportionnelle
Pénalités retard/Modèle 
saisie 6 caractères alphanumériques
Frais impayés/Frais 
forfaitaires 35 caractères alphanumériques
Frais impayés/Code 
journal 14 caractères numériques
Frais impayés/Modèle 
saisie 6 caractères alphanumériques
Impression 
N°facture/Référence 35 caractères alphanumériques
Seuil équilibre TVA
1
Non 
Oui
Interdire éléments en 
sommeil 14 caractères numériques
Dernière période clôturée
1
Non 
Oui
Matérialisation pièces 
dans journaux Date au format JJMMAA
Gestion budgets/Axe 
analytique
1
Non 
Oui
Capital
1
Non 
Oui
Forme juridique Format double
Compte Facebook 35 caractères alphanumériques
Compte LinkedIn 35 caractères alphanumériques
Mise à jour Devises 35 caractères alphanumériques
Mise à jour Devises en 
saisie
1
Non 
Oui
Champ Code Correspondance/Commentaire
Gestion de la LAF
1
Non 
Oui
Pas de la recherche 
d''écriture
1
Non 
Oui
Prospect en création 
client
1
Non
Oui
Report Numéro écriture 0
Numéro pièce
Numéro facture
Régime d’imposition FEC 0
2
Général
BA
BNC
Registre Taxe/Date 
acompte
Date (6) ou vide
Fichiers liés

## #MSTT — Champ Statistique Tiers
*Export modèle : 1 occurrence(s), 10 lignes.*

Champ Code Correspondance/Commentaire
Intitulé 35 caractères alphanumériques
Ce champ est répété 10 fois.

## #MSTV — Enuméré statistique
*Export modèle : 8 occurrence(s), 2 lignes.*

Champ Code Correspondance/Commentaire
Numéro statistique 1..10 Position du champ statistique
Intitulé 21 caractères alphanumériques

## #MRIS — Code risque
*Export modèle : 1 occurrence(s), 40 lignes.*

10 fois :
Champ Code Correspondance/Commentaire
Intitulé 35 caractères alphanumériques
Action 0
2
A livrer
A surveiller
A bloquer
Dépassement d'encours 
minimum
14 caractères numériques
Dépassement d'encours 
maximum
14 caractères numériques
Tous ces champs sont répétés 10 fois

## #MDEV — devise
*Export modèle : 1 occurrence(s), 640 lignes.*

Champ Code Correspondance/Commentaire
Intitulé 35 caractères 
alphanumériques
Format 31 caractères 
alphanumériques
Champ Code Correspondance/Commentaire
Cours 14 caractères numériques
Cours période 14 caractères numériques
Unité monnétaire 21 caractères 
alphanumériques
Sous-unité monnétaire 21 caractères 
alphanumériques
Code ISO 3 caractères 
alphanumériques
Sigle 5 caractères 
alphanumériques
Mode de cotation
1
Certain
Incertain
Devise de cotation 1..32 Position dans la table des 
devises
Cours clôture 14 caractères numériques
Date limite Date au format JJMMAA
Cours ancienne cotation 14 caractères numériques
Mode ancienne cotation
1
Certain
Incertain
Anc.devise de cotation 1..32 Position dans la table des 
devises
Code remise
1
3
Aucun
Blanc
Franc
Euro. 
Réservé à Moyens de 
paiement
Monnaie zone Euro
1
Non
Oui
Code ISO numérique 4 caractères 
alphanumériques
Date de mise à jour Date au format JJMMAA ou 
vide
Heure de mise à jour Temps[8] ou vide
Tous ces champs sont répétés 32 fois.

## #MINF — Information libre
*Export modèle : 4 occurrence(s), lignes 6, 11, 36, 41.*

Il y a autant de drapeaux #MINF que de type de fichier distincts.
Indice fichier (0 pour comptes généraux, 1 pour sections analytiques, 2 pour comptes tiers, 3 
pour écritures comptables)
N fois :
Champ Code Correspondance/Commentaire
Nom champ 31 caractères alphanumériques
Type champ 0
2
4
Texte
Valeur
Date
Date longue
Montant
Table
Longueur champ 1..69 Longueur de l'information libre 
de type Texte, blanc pour les 
autres types
Créateur 4 caractères alphanumériques
Formule 1024 caractères 
alphanumériques

## #MEIN — Enuméré Information libre
*Absent de l'export modèle — structure non vérifiée sur fichier réel.*

Fichier lié au fichier Information libre. Ce drapeau est répété autant de fois que nécessaire.
Champ Code Correspondance/Commentaire
Numéro fichier 1,6,10,38 Comptes généraux, Sections
analytiques, Comptes 
tiers, Ecritures 
comptables
Numéro information libre 1..64
Intitulé 35 caractères alphanumériques

## #MREG — Mode de règlement
*Export modèle : 1 occurrence(s), 300 lignes.*

30 fois :
Champ Code Correspondance/Commentaire
Intitulé 35 caractères alphanumériques
Code 3 caractères alphanumériques
Mode de paiement débit 0..11
Mode de paiement crédit 0..8
Code AFB décaissement principal 2 caractères alphanumériques
Code AFB encaissement principal 2 caractères alphanumériques
Champ Code Correspondance/Commentaire
Abrégé RIB décaissement 5 caractères alphanumériques 
majuscules
Abrégé RIB encaissement 5 caractères alphanumériques 
majuscules
Code Edi 3 caractères alphanumériques
Paiement en ligne 0
Non 
Oui

## #MREJ — Motif de rejet
*Export modèle : 51 occurrence(s), 2 lignes.*

Champ Code Correspondance/Commentaire
Code 2 caractères alphanumériques
Intitulé 35 caractères alphanumériques
Tous ces champs sont répétés 50 fois.

## #MNAT — Nature de compte
*Export modèle : 1 occurrence(s), 1820 lignes.*

14 fois 10 fois (=140 fois) :
Champ Code Correspondance/Commentaire
Fourchette radical début 3..13 caractères alphanumériques
Fourchette radical fin 3..13 caractères alphanumériques
Option regroupement 0
Non
Oui
Option analytique 0
Non
Oui
Option échéance 0
Non
Oui
Option quantité 0
Non
Oui
Option devise 0
Non
Oui
Numéro devise 0..32 Position dans la table des devises
Option lettrage 0
Non
Oui
Option tiers 0
Non
Oui
Type report 0
2
Aucun
Solde
Détail
Champ Code Correspondance/Commentaire
Report analytique 0
Non
Oui
Lettrage en saisie 0
Non
Oui
Tous ces champs sont répétés 10 fois pour chaque nature de compte (14 natures 
différentes), dans l'ordre : Client, Fournisseur, Salarié, Banque, Caisse, 
Amortissement/Provision, Résultat - Bilan, Charge, Produit, Résultat – Gestion, 
Immobilisations, Capitaux, Stock, Titre.

## #MNIC — Niveau d'analyse
*Export modèle : 1 occurrence(s), 30 lignes.*

30 fois
Champ Code Correspondance/Commentaire
Intitulé 35 caractères alphanumériques

## #MCLN — Organisation
*Export modèle : 1 occurrence(s), 1890 lignes.*

Ce champ est répété 126 fois, pour chaque zone disponible pour chacune des 15 listes, 
dans l’ordre : Saisie par pièce, Journal achat, Journal vente, Journal trésorerie, Journal 
général, Journal de situation, Saisie des opérations bancaires, Interrogation générale, 
Interrogation tiers, Interrogation analytique, Rapprochement bancaire, Règlement tiers, 
Rappel/relevé clients, Recherche générale, Recherche analytique.
La liste des champs disponibles pour chaque liste est décrite dans la fonction Fichier/ 
Paramètres société.
Champ Code Correspondance/Commentaire
Statut de la colonne 0
2
4
Disponible pour le fichier
Obligatoire pour l'application
Impossible pour cette fonction
Obligatoire pour le fichier
Masquée pour le fichier

## #MPLB — Paramétrage des libellés
*Export modèle : 1 occurrence(s), 3 lignes.*

Champ Code Correspondance/Commentaire
Tiers/Langue Aucune 21 caractères alphanumériques
Tiers/Langue 1 21 caractères alphanumériques
Tiers/Langue 2 21 caractères alphanumériques

## #MANA — Plan analytique
*Export modèle : 1 occurrence(s), 253 lignes.*

11 fois :
Champ Code Correspondance/Commentaire
Intitulé 35 caractères alphanumériques
Section analytique 
d'attente
13 caractères alphanumériques majuscules ou vide
Gestion en colonne 0
Non 
oui
Type d'imputation 0
2
Aucune
Charge Produit
Tous
Plan obligatoire 0
Non
oui
6fois 
Nom 21 caractères alphanumériques
Longueur 0..13 (Somme des 6 <= 13)
Type 0..2

## #MENA — Enuméré analytique
*Export modèle : 6 occurrence(s), 4 lignes.*

Champ Code Correspondance/Commentaire
Numéro analytique 1..11
Numéro de rupture 1..6
Numéro 13 caractères alphanumériques
Intitulé 21 caractères alphanumériques

## #MRAP — Période de rappel
*Export modèle : 1 occurrence(s), 40 lignes.*

Champ Code Correspondance/Commentaire
Intitulé 35 caractères alphanumériques
Nombre jours début -999..999
Nombre jours fin -999..999
Nbre jours entre deux 
rappels 3 caractères numériques
Tous ces champs sont répétés 10 fois.

## #MSBQ — Structure banque
*Export modèle : 1 occurrence(s), 40 lignes.*

4 fois : Ces champs sont répétés 4 fois pour les structures, dans l’ordre : Locale, Autre, 
BBAN, IBAN.
Champ Code Correspondance/Commentaire
Structure Edi 0
Non
Oui
Longueur code banque 0..14 0 à 14 caractères
Type code banque 0
Numérique
Alphanumérique
Longueur code guichet 0..17 0 à 17 caractères
Type code guichet 0
Numérique
Alphanumérique
Longueur compte 0..34 0 à 34 caractères
Type compte 0
Numérique
Alphanumérique
Longueur clé 0..2 0 à 2 caractères
Type clé 0
Numérique
Alphanumérique
Contrôle clé 0
2
4
Aucun
France
Espagne
Portugal
Belgique

## #MTTI — Types tiers
*Export modèle : 1 occurrence(s), 136 lignes.*

4 fois :
Champ Code Correspondance/Commentaire
Tiers principal 1..10 Position dans la table des types tiers
Type numérotation 0
2
Manuelle
Automatique
Manuelle avec racine
Longueur 0..17
Racine 17 caractères alphanumériques majuscules
10 fois
Intitulé
17 caractères alphanumériques
Type compte 0
Radical
Compte
Champ Code Correspondance/Commentaire
Compte 3..13 caractères alphanumériques

## #MRGI — Registres
*Export modèle : 1 occurrence(s), 2 lignes.*

Champ Code Correspondance/Commentaire
Gestion registres révision 0
Non
Oui
Gérer les registres de taxes 0
Non
Oui

## #MLET — Ajustement lettrage
*Export modèle : 1 occurrence(s), 65 lignes.*

Champ Code Correspondance/Commentaire
Code journal écart 
règlement
6 caractères alphanumériques
Intitulé modèle de saisie 
débit écart règlement
35 caractères alphanumériques
Intitulé modèle de saisie 
crédit écart règlement
35 caractères alphanumériques
Maximum débit 14 caractères numériques
Maximum crédit 14 caractères numériques
Gestion écarts conversion 0
Non
Oui
Code journal écart 
conversion
6 caractères alphanumériques
Intitulé modèle de saisie 
débit écart conversion
35 caractères alphanumériques
Intitulé modèle de saisie 
crédit écart conversion
35 caractères alphanumériques
Seuil écart conversion 14 caractères numériques
Code journal écart change 6 caractères alphanumériques
Intitulé modèle de saisie 
débit écart change
35 caractères alphanumériques
Intitulé modèle de saisie 
crédit écart change
35 caractères alphanumériques
Ces champs sont répétés 5 fois pour chaque type d'ajustement lettrage, dans l'ordre: Client, 
Fournisseur, Salarié, Autre, Général.

## #MCIB — Codes interbancaires
*Export modèle : 125 occurrence(s), lignes 58, 61, 64, 67, 73.*

Champ Code Correspondance/Commentaire
Code AFB 2 caractères alphanumériques
Code nature 5 caractères alphanumériques Majuscules
Intitulé 35 caractères alphanumériques
Sens 0
Décaissement ou Crédit comptable
Encaissement ou Débit comptable
Numéros règlements associés 30 * (0..30) Position dans la table des modes de 
règlement.
Nombre jours de 
valeur999...999
(dans l’application Trésorerie)
Type de jour 0
2
Aucun
Calendaire
Ouvré
(dans l’application Trésorerie)
Echéance reportée 0
Non 
Oui
(dans l’application Trésorerie)
Exonération commission de 
mouvement
1
Non 
Oui
(dans l’application Trésorerie)
Nombre jours décalage 
échéance
-9999..9999
Type de jour décalage échéance 0
2
Délai entre date des ecritures comptables
Délai entre dates des lignes d’extraits
Délai entre date écriture des écritures 
comptables et lignes d’extraits
Numéro règlement principal 
Finance
0..30
Rappro/Mode de 
rapprochement
1
Montant
Montant brut bancaire
Montant net bancaire
Rappro/Code interbancaire 
associé/Code AFB
2 caractères alphanumériques
Rappro/Puissance écritures 0
2
4
1 écriture
5 écritures
10 écritures
30 écritures
50 écritures
100 écritures
Rappro/Puissance extraits 0
1 ligne mouvement
5 lignes mouvement
Champ Code Correspondance/Commentaire
3
5
10 lignes mouvement
30 lignes mouvement
50 lignes mouvement
100 lignes mouvement
Rappro/Délai écritures 0
Non 
Oui
Rappro/Nb jours délai écritures 0..999
Rappro/Délai extraits 0
Non 
Oui
Rappro/Nb jours délai extraits 0..999 0..999
Rappro/Délai écritures et 
extraits
1
Non 
Oui
Rappro/Nb jours délai écritures 
et extraits
0..999
Rappro/Comparaison écritures 
et extraits_
1
Non
Oui
Rappro/Comparaison/Nb 
caractères
0..99
Rappro/Comparaison/Zone 
écriture
1
3
Aucun
Numéro de pièce
Référence
N° facture
Libellé
Rappro/Comparaison/Position 
zone écriture
0..99
Rappro/Comparaison/Zone 
extrait
1
3
Aucun
Numéro de pièce
Référence
N° facture
Libellé
Rappro/Comparaison/Position 
zone extrait
0..99
Rappro/Modèle de saisie type 
trésorerie
35 caractères alphanumériques
N fois
Domaine 4 caractères alphanumériques
Code famille 4 caractères alphanumériques
Code ISO 4 caractères alphanumériques

## #MCTD — Contacts dossiers
*Export modèle : 1 occurrence(s), 19 lignes.*

Champ Code Correspondance/Commentaire
Nom 35 caractères alphanumériques
Prénom 35 caractères alphanumériques
Service 1..30 Position dans la table des services contacts
Fonction 35 caractères alphanumériques
Téléphone 21 caractères alphanumériques
Téléphone portable 21 caractères alphanumériques
Télécopie 21 caractères alphanumériques
Adresse eMail 69 caractères alphanumériques
Civilité 0
2
M.
Mme
Mlle
Numéro contact 1..30 Position dans la table des types contacts
Adresse 35 caractères alphanumériques
Complément adresse 35 caractères alphanumériques
Code postal 9 caractères alphanumériques
Ville 35 caractères alphanumériques
Code région 25 caractères alphanumériques
Pays 35 caractères alphanumériques
Compte Facebook 35 caractères alphanumériques
Compte LinkedIn 35 caractères alphanumériques
Compte Skype 35 caractères alphanumériques

## #MPAY — Pays
*Export modèle : 15 occurrence(s), 8 lignes.*

Champ Code Correspondance/Commentaire
Intitulé 35 caractères alphanumériques
Code 3 caractères alphanumériques
Code DEI 3 caractères alphanumériques
Assurance Montant (14 caractères). Réservé à la Gestion 
commerciale
Transport Montant (14 caractères). Réservé à la Gestion 
commerciale
Code ISO2 2 caractères alphanumériques
Espace Sepa 0
Non 
Oui
Localisation 0
2
Union européenne
France
Hors Union européenne
Champ Code Correspondance/Commentaire
4
DROM
COM

## #MSCT — Service des contacts
*Export modèle : 1 occurrence(s), 60 lignes.*

30 fois :
Champ Code Correspondance/Commentaire
Intitulé 35 caractères alphanumériques
Abrégé 3 caractères alphanumériques Majuscules

## #MRES — Paramétrage des résultats
*Export modèle : 1 occurrence(s), 200 lignes.*

50 fois :
Champ Code Correspondance/Commentaire
Génération écr.résultat 0
Non
Oui
Compte résultat 3..13 caractères alphanumériques ou vide
Compte imposition 3..13 caractères alphanumériques ou vide
Compte contrepartie 3..13 caractères alphanumériques ou vide

## #MFIS — Informations fiscales
*Export modèle : 1 occurrence(s), 76 lignes.*

Champ Code Correspondance/Commentaire
Régime 0
2
0 = Réel Normal – CA3
1 = Mini-Réel – CA3
2 = Réel simplifié – CA12
3 = Réel simplifié agriculture – CA3
Recette 13 caractères alphanumériques majuscules
Numéro dossier 13 caractères alphanumériques majuscules
Clé 5 caractères alphanumériques majuscules
CDI 5 caractères alphanumériques majuscules
Code service 5 caractères alphanumériques majuscules
% déduction pour CA12 Montant (3 caractères)
Centre impôts/Adresse 35 caractères alphanumériques
Centre 
impôts/Complément
35 caractères alphanumériques
Centre impôts/Code 
postal
14 caractères alphanumériques
Centre impôts/Ville 35 caractères alphanumériques
Centre 
impôts/Téléphone
21 caractères alphanumériques
Centre 
impôts/Horaires
35 caractères alphanumériques
Code journal 6 caractères alphanumériques ou vide
Champ Code Correspondance/Commentaire
TVA à décaisser 3..13 caractères alphanumériques ou vide
Crédit de TVA 3..13 caractères alphanumériques ou vide
Ecart arrondi débit 3..13 caractères alphanumériques ou vide
Ecart arrondi crédit 3..13 caractères alphanumériques ou vide
6 fois
*Compte de TVA 3..13 caractères alphanumériques ou vide
* Rubr.montant Chaîne[8]
Apurement de TVA 3..13 caractères alphanumériques ou vide
Arrondissement fiscal 30 caractères alphanumériques
Code arrondissement 
fiscal
4 caractères alphanumériques
Numéro 
arrondissement fiscal
5 caractères alphanumériques
NIF expert comptable 25 caractères alphanumériques
Montant limite 14 caractères numériques
Affiliation chambre des 
métiers
1
Non 
Oui
Jour de la date limite 1..31
Mois de la date limite 0..13 0 = Mois suivant
1 = Deuxième mois suivant
2 = Janvier
3 = Février
……
13 = Décembre
EDI/Numéro FRP 15 caractères alphanumériques majuscules
EDI/Représentant 35 caractères alphanumériques
EDI/Emetteur 0
2
Société
Autre tiers déclarant
Expert comptable
Emetteur/Raison 
sociale
35 caractères alphanumériques
Emetteur/Adresse 35 caractères alphanumériques
Emetteur/Complément 35 caractères alphanumériques
Emetteur/Code postal 9 caractères alphanumériques
Emetteur/Ville 35 caractères alphanumériques
Emetteur/Siret 14 caractères alphanumériques
Emetteur/Téléphone 21 caractères alphanumériques
Emetteur/Adresse 
eMail
69 caractères alphanumériques
Champ Code Correspondance/Commentaire
Déclarant/Nom et 
prénom
69 caractères alphanumériques
Déclarant/Qualité 35 caractères alphanumériques
Déclarant/Téléphone 21 caractères alphanumériques
EDI/Numéro ROF 8 caractères alphanumériques
EDI/Date redressement 
judiciaire
Date au format JJMMAA ou vide
Emetteur/Code région 25 caractères alphanumériques
Emetteur/Pays 35 caractères alphanumériques
Centre impôts/Code 
région
25 caractères alphanumériques
Centre impôts/Pays 35 caractères alphanumériques
OGA/Raison sociale ou 
Désignation xml
35 caractères alphanumériques
OGA/Complément 
Raison sociale
35 caractères alphanumériques
OGA/Qualité 35 caractères alphanumériques
OGA/Siret ou 
Identifiant xml
14 caractères alphanumériques
OGA/Adhérent ou 
Reference2 xml
35 caractères alphanumériques
OGA/Agrément ou 
NumeroReference xml 6 caractères alphanumériques
OGA/Adresse 35 caractères alphanumériques
OGA/Complément 35 caractères alphanumériques
OGA/Code postal 9 caractères alphanumériques
OGA/Ville 35 caractères alphanumériques
OGA/Pays 35 caractères alphanumériques
OGA/Téléphone 21 caractères alphanumériques
OGA/Adresse eMail 69 caractères alphanumériques
EDI/Date cession ou 
cessation 
Date au format JJMMAA ou vide
Option paiement 
TVA/Débit
0 Non 
1 oui 
Date application Date au format JJMMAA ou vide 
Date résiliation Date au format JJMMAA ou vide

## #MMOL — Motifs de litiges
*Export modèle : 1 occurrence(s), 30 lignes.*

30 fois
Champ Code Correspondance/Commentaire
Intitulé 35 caractères alphanumériques
Tous ces champs sont répétés 30 fois.

## #MRSO — Résolutions
*Export modèle : 1 occurrence(s), 30 lignes.*

Champ Code Correspondance/Commentaire
Intitulé 35 caractères alphanumériques
Tous ces champs sont répétés 30 fois.

## #MRCO — Recouvrement
*Export modèle : 1 occurrence(s), 5 lignes.*

Champ Code Correspondance/Commentaire
Provision/ Code 
journal
6 caractères alphanumériques ou vide
Provision/ Modèle 
saisie Dotations 
35 caractères alphanumériques
Provision/ Modèle 
saisie Reprise
35 caractères alphanumériques
Compte de perte 3..13 caractères alphanumériques ou vide
Compte clients 
douteux
3..13 caractères alphanumériques ou vide

## #MECE — Services connectés
*Export modèle : 1 occurrence(s), 10 lignes.*

Champ Code Correspondance/Commentaire
Type code Edi 0
2
0 = GLN
1= DUNS
2 = Autre
Code Edi
23 caractères alphanumériques
Code Edi Sage 8 caractères numériques
Nom contact émetteur 35 caractères alphanumériques
Prénom contact émetteur 35 caractères alphanumériques
Code journal échange 6 caractères alphanumériques
Modèle saisie échange 35 caractères alphanumériques
Type Autre identifiant 0
2
4
Aucun
Union européenne Hors France
Hors Union Européenne
RIDET
TAHITI
Particulier
Champ Code Correspondance/Commentaire
6 Autre
Valeur Autre identifiant 80 caractères alphanumériques
Option traitement 
factures
5
2
4
Non géré ok
Tester l’émission et la réception des factures 
(phase pilote)
Tester l’émission et la réception des factures
Emettre des factures vers les entités publiques 
uniquement
Recevoir des factures électroniques
Emettre et recevoir ds factures électroniques

## #MBAP — Bon à payer
*Export modèle : 1 occurrence(s), 5 lignes.*

Champ Code Correspondance/Commentaire
Niveau de validation 0
2
0 = Aucun 
1= Responsable financier uniquement
2 = Acheteur et Responsable financier
Nom responsable financier 35 caractères alphanumériques
Prénom responsable 
financier
35 caractères alphanumériques
Factures à valider 0
Toutes les factures
Selon montant
Seuil de validation 14 caractères numériques

## #MRGL — Régularisations comptables
*Export modèle : 1 occurrence(s), 6 lignes.*

Champ Code Correspondance/Commentaire
Code journal 6 caractères alphanumériques
Modèle saisie Charges 35 caractères alphanumériques
Modèle saisie Fournisseurs 35 caractères alphanumériques
Modèle saisie Produits 35 caractères alphanumériques
Modèle saisie Clients 35 caractères alphanumériques
Base prorata 0
360 jours
Jours réels

## #MTCO — Type contact
*Export modèle : 1 occurrence(s), 30 lignes.*

Champ Code Correspondance/Commentaire
Intitulé 35 caractères alphanumériques
Tous ces champs sont répétés 30 fois.

## #MCAL — Calendrier
*Export modèle : 2 occurrence(s), 53 lignes.*

Champ Code Correspondance/Commentaire
Intitulé 35 caractères alphanumériques
Numéro Banque 1
Standard 2
Autre 0
Première semaine de 
l'année
1
Commence le 1er janvier
Première semaine de 4 jours
Première semaine entière
Jours ouvrés 0
Non
Oui
7 fois : une fois / jour
Tranches horaires 7 * (2 * (2 * 
Temps[8]))
Jours de commande
1
Non
Oui
Répété 7 fois : une fois / jour
Jours de livraison
1
Non
Oui
Répété 7 fois : une fois / jour
N fois : 
Date jour d'exception Date au format JJMMAA
Motif jour d'exception 35 caractères alphanumériques

## #MPLG — Plan comptable
*Absent de l'export modèle — structure non vérifiée sur fichier réel.*

Champ Code Correspondance/Commentaire
Numéro compte général 3..13 caractères alphanumériques
Type 0
Détail
Total
Intitulé 35 caractères alphanumériques
Abrégé 17 caractères alphanumériques
Numéro nature 0
2
4
Aucune
Client
Fournisseur
Salaire
Banque
Caisse
Champ Code Correspondance/Commentaire
7
9
11
13
Amortissement
Résultat bilan
Charges
Produits
Résultat gestion 
Immobilisations
Capitaux 
Stock
Titre
Type report 0
2
Aucun
Solde
Détail
Numéro compte 
reporting
13 caractères 
alphanumériques 
majuscules ou vide
Raccourci 6 caractères alphanumériques majuscules
Saut lignes 0
1…99
Saut de page
Sauts de lignes
Option regroupement 0
Non
Oui
Option analytique 0
Non
Ou
Option échéance 0
Non
Oui
Option quantité 0
Non
Oui
Option lettrage 0
Non
Oui
Option tiers 0
Non
Oui
Date de création Date sous la forme JJMMAANon importé
Bloc-note 255 caractères alphanumériques
Option devise 0
Non
Oui
Numéro devise 0..32 Position dans la table des devises
Code taxe 5 caractères 
alphanumériques 
majuscules ou vide
Mise en sommeil 0
Non
Oui
Report analytique 0 Non
Champ Code Correspondance/Commentaire
1 Oui
Lettrage en saisie 0
Non
Oui

## #MPGB — Budget plan comptable
*Absent de l'export modèle — structure non vérifiée sur fichier réel.*

Champ Code Correspondance/Commentaire
Sens 0
Charge
Produit
Valeurs dotations montants 6 * 36 montants (nombre 
maximum de période par exercice) 
de 14 caractères numériques dans 
l'ordre Dotation faible N, Dotation 
forte N, Dota-tion faible N-1, 
Dotation forte N-1, Dotation faible 
N-2, Dotation forte N-2,
Valeurs dotations quantités 6 * 36 14 caractères numériques
N fois
Numéro analytique 1..11
Numéro section analytique 13 caractères alphanumériques 
majuscules
Type répartition 6 * (0..2)
Valeur répartition montant 6 * (14 caractères numériques ou 14 
caractères numériques suivant Type 
répartition)
Valeur répartition quantité 6 * Quantité[14]

## #MPGA — Répartition analytique plan comptable
*Absent de l'export modèle — structure non vérifiée sur fichier réel.*

Champ Code Correspondance/Commentaire
Numéro analytique 1..11 Position dans la table des plans 
analytiques
Numéro section analytique 13 caractères alphanumériques 
majuscules
Type répartition 0
2
Pourcentage
Equilibre
Montant
Valeur répartition montant 14 caractères 
numériques ou 14 
caractères numériques
suivant Type 
répartition

## #MIVA — Informations libres
*Export modèle : 10 occurrence(s), 8 lignes.*

Pour un compte général, doit suivre : #MPLG ou #MPGB
Pour une section analytique, doit suivre : #MPCA ou #MPAB
Pour un compte tiers, doit suivre : #MPCT, #MBQT, #MRLT ou #MCDL
ou #MCTT ou #MHIT ou # MFRT
Pour une écriture comptable, doit suivre : #MECG, #MECA, #MRGR ou #MRGT
Champ Code Correspondance/Commentaire
Valeur 
N fois
Selon le type d'information 
libre:
Texte sur 69 caractères 
alphanumériques,
Montant sur 14 caractères 
numériques,
Date sur 6 caractères,
Date longue sur 8 
caractères,
Valeur sur 14 caractères 
numériques,
Enuméré sur 21 caractères 
alphanumériques
Ce champ est répété jusqu'à 64 fois, c'est-à-dire autant de fois que d'informations libres 
paramétrées

Champ Code Correspondance/Commentaire
Valeur 
N fois
Date[6], Date[8], 14 caractères 
numériques ou 69 caractères 
alphanumériques

Champ Code Correspondance/Commentaire
Valeur 
N fois
Date[6], Date[8], 14 caractères 
numériques ou 69 caractères 
alphanumériques

Pour un compte général, doit suivre : #MPLG ou #MPGB
Pour une section analytique, doit suivre : #MPCA ou #MPAB
Pour un compte tiers, doit suivre : #MPCT, #MBQT, #MRLT ou #MCDL
Pour une écriture comptable, doit suivre : #MECG, #MECA, #MRGR ou #MRGT
Champ Code Correspondance/Commentaire
Valeur 
N fois
Date[6], Date[8], 14 caractères 
numériques ou 69 caractères 
alphanumériques

## #MPCA — Plan analytique/ Section
*Export modèle : 62 occurrence(s), 22 lignes.*

Champ Code Correspondance/Commentaire
Numéro analytique 1..11 Position dans la table des plans 
analytiques
Numéro section analytique 13 caractères alphanumériques 
majuscules
Intitulé 35 caractères alphanumériques
Type 0
Détail
Total
Abrégé 17 caractères alphanumériques
Raccourci 6 caractères alphanumériques majuscules
Report 0
Non
Oui
Numéro analyse 1..30 1..30
Saut lignes 0
1…99
Saut de page
Sauts de lignes
Mise en sommeil 0
Non
Oui
Date de création Date sous la forme JJMMAA Non importé
Domaine 0
2
Les deux
Vente
Achat
Objectif chiffre affaire achat 14 caractères 
numériques
Objectif chiffre affaire vente 14 caractères 
numériques
Nom collaborateur 35 caractères alphanumériques
Prénom collaborateur 35 caractères alphanumériques
Statut 0..5
Date création affaire Date au format JJMMAA ou vide
Date acceptation affaire Date au format JJMMAA ou vide
Date début affaire Date au format JJMMAA ou vide
Date fin affaire Date au format JJMMAA ou vide
Mode facturation 0
0 = Forfait
1 = Avancement

## #MPAB — Budget plan analytique
*Export modèle : 26 occurrence(s), 433 lignes.*

Champ Code Correspondance/Commentaire
Sens 0
Charge
Produit
Valeurs dotations montants 6 * 36 montants (nombre maximum de 
périodes pour un exercice) de 14 
caractères numériques dans l'ordre 
Dotation faible N, Dotation forte N, 
Dotation faible N-1, Dotation forte N1, Dotation faible N-2, Dotation forte 
N-2,
Valeurs dotations quantités 6 * 36 14 caractères numériques
N fois
Numéro compte général 3..13 caractères alphanumériques
Type répartition 6 * (0..2)
Valeur répartition montants 6 * (14 caractères 
numériques ou 14 
caractères numériques
suivant Type 
répartition)
Valeur répartition quantités 6 * Quanté[14]

## #MCTA — Contact analytique
*Absent de l'export modèle — structure non vérifiée sur fichier réel.*

Champ Code Correspondance/Commentaire
Nom 35 caractères alphanumériques
Prénom 35 caractères alphanumériques
Service 1..30 Position dans la table des services 
contacts
Fonction 35 caractères alphanumériques
Téléphone 21 caractères alphanumériques
Téléphone portable 21 caractères alphanumériques
Télécopie 21 caractères alphanumériques
Adresse eMail 69 caractères alphanumériques
Civilité 0
2
M.
Mme
Mlle
Champ Code Correspondance/Commentaire
Numéro contact 1..30
Compte Facebook 35 caractères alphanumériques
Compte LinkedIn 35 caractères alphanumériques
CompteSkype 35 caractères alphanumériques

## #MPCR — Plan reporting
*Absent de l'export modèle — structure non vérifiée sur fichier réel.*

Champ Code Correspondance/Commentaire
Numéro compte 
reporting
13 caractères alphanumériques 
majuscules
Type 0
Détail
Total
Intitulé 35 caractères alphanumériques
Abrégé
17 caractères alphanumériques
Saut lignes 0
1..99
Saut de page
Sauts de lignes (nombre de lignes)

## #MPCT — Plan tiers
*Export modèle : 64 occurrence(s), lignes 134, 135.*

Champ Code Correspondance/Commentaire
Numéro compte tiers 17 caractères alphanumériques 
majuscules
Intitulé 69 caractères alphanumériques
Type 0
2
Client
Fournisseur 
Salarié
Autre
Numéro compte 
général principal
3..13 caractères alphanumériques
Qualité 17 caractères alphanumériques
Abrégé 17 caractères alphanumériques
Contact 35 caractères alphanumériques
Adresse 35 caractères alphanumériques
Complement adresse 35 caractères alphanumériques
Code postal 9 caractères alphanumériques
Ville 35 caractères alphanumériques
Code région 25 caractères alphanumériques
Pays 35 caractères alphanumériques
Champ Code Correspondance/Commentaire
Raccourci 6 caractères alphanumériques 
majuscules
Numéro devise 0
1..32
Aucun
Position dans la table des devises
Ape 6 caractères alphanumériques
Identifiant 25 caractères alphanumériques
Siret 14 caractères alphanumériques
Valeurs Statistiques 10 * 21 caractères alphanumériques
Commentaire 35 caractères alphanumériques
Encours 14 caractères numériques
Plafond assurance 
crédit
14 caractères numériques
Numéro compte tiers 
payeur
17 caractères alphanumériques 
majuscules
Code risque 1..10 Position dans la table des codes 
risques. Réservé à la Gestion 
commerciale
Catégorie tarifaire 1..32 Position dans la table des catégories. 
Réservé à la Gestion commerciale
Montant taux 4 * 14 caractères numériques. 
Réservé à la Gestion commerciale
Catégorie comptable 1..32 Position dans la table des catégories. 
Réservé à la Gestion commerciale
Périodicité 1..10 Réservé à la Gestion commerciale
Nombre de factures 0..99 Réservé à la Gestion commerciale
Un BL par facture 0
Non
Oui. Réservé à la Gestion 
commerciale
Langue 0
2
Aucune
Langue 1
Langue 2
Réservé à la Gestion commerciale
Code Edi 23 caractères alphanumériques. 
Réservé à la Ges-tion commerciale
Expédition 1..50 Réservé à la Gestion commerciale
Condition 1..30 Réservé à la Gestion commerciale
Saut lignes 0
1..99
Saut de page 
Sauts de lignes (nombre de lignes)
Option lettrage 0
Non
Oui
Validation des dates 
d'échéance
1
Non
Oui
Mise en sommeil 0 Non
Champ Code Correspondance/Commentaire
1 Oui
Contrôle de l'encours 0
2
Contrôle automatique
Selon code risque
Compte bloqué
Réservé à la Gestion commerciale
Date de création Date au format JJMMAA// Non 
importé
Hors rappel/relevé 0
Non
Oui
Numéro analytique 1..11 Position dans la table de plans 
analytiques
Numéro section 
analytique
13 caractères alphanumériques 
majuscules
Téléphone 21 caractères alphanumériques
Télécopie 21 caractères alphanumériques
Adresse eMail 69 caractères alphanumériques
Site 69 caractères alphanumériques
Numéro EASY 25 caractères alphanumériques
Placé sous 
surveillance
1
Non
Oui
Date création société Date au format JJMMAA
Forme juridique 32 caractères alphanumériques
Effectif 10 caractères alphanumériques
Chiffre d'affaires 14 caractères numériques
Résultat net 14 caractères numériques
Incidents de paiement 0
Non
Oui
Date du dernier 
incident
Date au format JJMMAA
Privilèges 0.
2
Aucun privilège
Présence privilège
Privilège inconnu
Régularité des 
paiements
0 à 99 2 caractères numériques
Cotation de la 
solvabilité
4 caractères alphanumériques 
majuscules
Date dernière mise à 
jour
Date au format JJMMAA
Objet dernière mise à 
jour
60 caractères alphanumériques
Date arrêté de bilan Date au format JJMMAA ou vide
Champ Code Correspondance/Commentaire
Nombre de mois du 
bilan
0..99
Numéro analytique 
IFRS
0..11
Position plan IFRS
Numéro section 
analytique IFRS
13 caractères alphanumériques 
majuscules
Priorité livraison 0..999 (dans l’application Gestion 
commerciale)
Livraison partielle 0
Non
Oui
(dans l’application Gestion 
commerciale)
Intitulé modèle de 
règlement
35 caractères 
alphanumériques
35 caractères alphanumériques
Non soumis à 
pénalités de retard
1
Non
Oui
Code banque élément 
banque
14 caractères 
alphanumériques
14 caractères alphanumériques
Guichet élément 
banque
17 caractères numériques 
(dans l’application Trésorerie)
Compte élément 
banque
34 caractères numériques
(dans l’application Trésorerie)
Numéro devise 
élément banque
0..32 Position dans la table des devises
(dans l’application Trésorerie)
Numéro tiers centrale 
d'achat
17 caractères alphanumériques 
majuscules
Nom collaborateur 35 caractères alphanumériques
Prénom collaborateur 35 caractères alphanumériques
Date fermeture début Date au format JJMMAA ou vide
Date fermeture fin Date au format JJMMAA ou vide
Format facture 0
2
4
0 = Aucun
1 = Défaut
2 = Pdf
3 = UBL
4 = Facture
5 = Xades
Type NIF 0
2
4
0 = NIF
1 = NIF IntraComm
2 = Passeport
3 = DocOfficiel
4 = Certificat
5 = Autre
Champ Code Correspondance/Commentaire
Intitulé représentant 
légal
35 caractères 
alphanumériques
35 caractères alphanumériques
NIF représentant légal 25 caractères alphanumériques
Type code Edi 0..2 0 = GLN
1 = DUNS
2 = Autre
Code Edi
23 caractères alphanumériques
Identifiant Edi Sage 8 caractères numériques
Profil du tiers 0
2
0 = Non défini
1 = Non inscrit
2 = Accepte la dématérialisation
3 = Refuse la dématérialisation
Statut d'échange 0
2
4
0 = Aucun
1 = Invitation en cours
2 = Accepte l’échange
3= Refuse l’échange
4 = Echange révoqué
Date actualisation
échange
Date au format JJMMAA ou vide
Rapprochement 
facture
1
Non
Oui
Compte rendu 
rapprochement
0.
Non
Oui
Modèle de saisie 35 caractères alphanumériques
Autorisation de bon à 
payer
1
Non
Oui
Délai de transport 0..999 0..999
Délai 
d'approvisionnement
0..999
Code langue ISO2 Edi 2 caractères
Compte rendu 
d'annulation
1
Non
Oui
Compte Facebook 35 caractères alphanumériques
Compte LinkedIn 35 caractères alphanumériques
Exclure des 
traitements
1
Non
Oui
Jours de commande 
(ligne répétée 7 fois)
1
Non
Oui
Jours de livraison 
(ligne répétée 7 fois)
1
Non
Oui
Champ Code Correspondance/Commentaire
Calendrier
2
Calendrier bancaire
Calendrier standard B
Assujettissement
1
Assujettissement
Particulier ou Non assujetti à TVA
Type Autre identifiant
1
3
5
Aucun
Union Européenne Hors france
Hors Union Européenne
RIDET
TAHITI
Particulier
Autre
Valeur Autre 
identifiant 80 caractères alphanumériques
Type entité
1
Non referencée annuaire
Privée assujettie TVA France
Publique
Contrôles émission
1
3
Aucun
Code service obligatoire
Référence engagement obligatoire
Code service et Référence 
engagement obligatoires
Code service ou Référence 
engagement obligatoire
Application préférée
Réservé Facture 
électronique et 
disponible Sage100 
v10.X
1
3
Aucune
Gestion commerciale
Comptabilité
Application externe
Selon code routage
Bloc note 2000 alphanumérique
Compte bancaire 
société
Banque
14 caractères alphanumériques
Compte bancaire 
société
Guichet
17 caractères alphanumériques
Compte bancaire 
société
Devise
1 à 32 N° de devise
N fois : Numéro 
compte général 
rattaché
3..13 caractères alphanumériques

## #MBQT — Banques tiers
*Export modèle : 47 occurrence(s), 21 lignes.*

Champ Code Correspondance/Commentaire
Banque principale 0
Non
Oui
Intitulé 35 caractères alphanumériques
Code banque 14 caractères alphanumériques
Guichet 17 caractères numériques
Compte 34 caractères alphanumériques 
majuscules
Clé 2 caractères numériques
Commentaire 69 caractères alphanumériques
Structure banque 0.
2
Locale
Etranger
BIN
IBAN
Numéro devise 1..32
Adresse agence 35 caractères alphanumériques
Complément agence 35 caractères alphanumériques
Code postal agence 9 caractères alphanumériques
Ville agence 35 caractères alphanumériques
Pays 35 caractères alphanumériques
BIC 11 caractères alphanumériques
Code routage 35 caractères alphanumériques
Code IBAN 34 caractères alphanumériques
Calcul IBAN 0
Non
Oui
Nom agence 35 caractères alphanumériques
Code région agence 25 caractères alphanumériques
Pays agence 35 caractères alphanumériques

## #MRLT — Règlements tiers
*Export modèle : 40 occurrence(s), 11 lignes.*

Doit suivre #MPCT ou #MBQT ou #MRLT ou #MCDL ou #MCTT ou #MHIT ou # MFRT
Champ Code Correspondance/Commentaire
Numéro règlement 1..30 Position dans la table des modes de 
règlement
Condition 0
2
Jour net
Fin de mois civil
Fin du mois
Nombre jours 0..999
Jours tombée 6 * (0..31)
Jusqu'à 6 jours de tombée
Type répartition 0
2
Pourcentage
Equilibre
Montant
Valeur répartition 14 caractères numériques ou 14 
caractères numériques suivant Type 
répartition

## #MCDL — Lieux de livraisons clients
*Export modèle : 25 occurrence(s), 17 lignes.*

Doit suivre #MPCT ou #MBQT ou #MRLT ou #MCDL ou #MCTT ou #MHIT ou # MFRT
Champ Code Correspondance/Commentaire
Intitulé 69 caractères alphanumériques
Adresse 35 caractères alphanumériques
Complément 35 caractères alphanumériques
Code postal 9 caractères alphanumériques
Ville 35 caractères alphanumériques
Code région 25 caractères alphanumériques
Pays 35 caractères alphanumériques
Contact 35 caractères alphanumériques
Mode d’expédition 1..50
Condition 1..30
Lieu principal 0
Non
Oui
Téléphone 21 caractères alphanumériques
Télécopie 21 caractères alphanumériques
Adresse eMail 69 caractères alphanumériques
Commentaire 69 caractères alphanumériques
Délai de transport 0..999
Adresse facturation 0
Non
Oui

## #MFRT — Réception facture des comptes tiers
*Absent de l'export modèle — structure non vérifiée sur fichier réel.*

Doit suivre #MPCT ou #MBQT ou #MRLT ou #MCDL ou #MCTT ou #MHIT ou # MFRT
Champ Code Correspondance/Commentaire
Type code routage 0
2
4
Code service
GLN
ODETTE
SWIFT
AUTRE
Code routage 100 caractères alphanumériques
Intitulé code routage 100 caractères alphanumériques
Actif 0
Non
Oui

Doit suivre #MPCT ou #MBQT ou #MRLT ou #MCDL ou #MCTT ou #MHIT ou # MFRT
Champ Code Correspondance/Commentaire
Type code routage 0
2
Code service
GLN
ODETTE
3
SWIFT
AUTRE
Code routage 100 caractères alphanumériques
Intitulé code routage 100 caractères alphanumériques
Actif 0
Non
Oui

## #MCTT — Contacts tiers
*Export modèle : 22 occurrence(s), 13 lignes.*

Fichier lié au Plan Tiers.
Le drapeau #MCTT doit suivre directement le compte tiers #MPCT auquel il se rapporte
ou #MBQT ou #MRLT ou #MCDL ou #MCTT ou #MHIT ou # MFRT
Champ Code Correspondance/Commentaire
Nom 35 caractères alphanumériques
Prénom 35 caractères alphanumériques
Service 1..30 Position dans la table des services 
contacts
Fonction 35 caractères alphanumériques
Téléphone 21 caractères alphanumériques
Téléphone portable 21 caractères alphanumériques
Télécopie 21 caractères alphanumériques
Adresse eMail 69 caractères alphanumériques
Civilité 0
2
M.
Mme
Mlle
Numéro contact 1..30
Champ Code Correspondance/Commentaire
Compte Facebook 35 caractères alphanumériques
Compte LinkedIn 35 caractères alphanumériques
Compte Skype 35 caractères alphanumériques

## #MHIT — Historique des rappels/ recouvrements
*Absent de l'export modèle — structure non vérifiée sur fichier réel.*

Doit suivre #MPCT ou #MBQT ou #MRLT ou #MCDL ou #MCTT ou #MHIT ou # MFRT
Champ Code Correspondance/Commentaire
Date traitement Date au format JJMMAA
Traitement 0..11 0..11
Frais impayés 14 caractères numériques
Pénalités retard 14 caractères numériques
Date échéance Date au format JJMMAA ou vide
Numéro règlement 0..30
Comptabilisation 0.
Non
Oui
Solde relance 14 caractères numériques

## #MCOL — Collaborateur
*Export modèle : 11 occurrence(s), 31 lignes.*

Champ Code Correspondance/Commentaire
Nom 35 caractères alphanumériques
Prénom 35 caractères alphanumériques
Fonction 35 caractères alphanumériques
Adresse 35 caractères alphanumériques
Complément 35 caractères alphanumériques
Code postal 9 caractères alphanumériques
Ville 35 caractères alphanumériques
Code région 25 caractères alphanumériques
Pays 35 caractères alphanumériques
Service 35 caractères alphanumériques
Vendeur/représentant 0
Non
Oui
Chef des ventes 0
Non
Oui
Caissier 0
non
Oui
Champ Code Correspondance/Commentaire
Date création Date au format JJMMAA ou videNon 
importé
Acheteur 0
non
Oui
Téléphone 21 caractères alphanumériques
Télécopie 21 caractères alphanumériques
Adresse eMail 69 caractères alphanumériques
Contrôleur 0
Non
Oui
Nom utilisateur 35 caractères alphanumériques
Téléphone portable 21 caractères 
alphanumériques
21 caractères alphanumériques
Chargé recouvrement 0
Non
Oui
Matricule 10 caractères alphanumériques 
majuscules
Responsable financier 0
Non
Oui
Mode de transmission 0
2
0 = Aucun
1 = Mail
2 = BusinessMobile
Compte Facebook 35 caractères alphanumériques
Compte LinkedIn 35 caractères alphanumériques
Compte Skype 35 caractères alphanumériques
Mise en sommeil 0
Non
Oui
Nom Chef des ventes associé 35 caractères alphanumériques
Prénom Chef des ventes associé 35 caractères alphanumériques

## #MTAX — Taux de taxe
*Export modèle : 21 occurrence(s), lignes 15, 16, 17, 18, 21, 23, 42.*

Champ Code Correspondance/Commentaire
Intitulé 35 caractères alphanumériques
Type taux 0
2
Taux
Montant
Quantité
Taux 14 caractères numériques ou 14 caractères 
numériques suivant Type taux
Type 0
TVA/débit
TVA/encaissement
Champ Code Correspondance/Commentaire
3
5
7
9
TP/HT
TP/TTC
TP/Poids 
TVA/CEE
Surtaxe 
IRPF (réservé version Espagnole)
IRPF Agraire (réservé version Espagnole)
IGIC (réservé version Espagnole)
Numéro compte général TVA 13 caractères alphanumériques
Code taxe 5 caractères alphanumériques
Taxe non perçue 0
Non
Oui
Sens 0
Déductible sur les achats
Collectée sur les ventes
Provenance 0
2
4
6
Nationale
Intracommunautaire
Export
Divers 1
Divers 2
Divers 3
Divers 4
Divers 5
Code regroupement 5 caractères alphanumériques majuscules
Assujettissement 14 caractères numériques
Grille base 3 caractères alphanumériques Majuscules
Grille taxe 3 caractères alphanumériques Majuscules
Code Edi 3 caractères alphanumériques
Mention exonération TVA 100 caractères alphanumériques
N fois 
Numéro compte général HT
3..13 caractères alphanumériques

## #MCJR — Codes journaux
*Export modèle : 18 occurrence(s), 16 lignes.*

Champ Code Correspondance/Commentaire
Code journal 6 caractères alphanumériques
Intitulé 35 caractères alphanumériques
Numéro compte général 
trésorerie
3..13 caractères alphanumériques
Type 0
Achat
Vente
Champ Code Correspondance/Commentaire
3
Trésorerie
Général
Situation
Type numérotation pièce 0
2
Manuelle
Continue par journal
Continue pour le fichier
Mensuelle
Option contrepartie/ligne 0
Non
Oui
Option saisie analytique 0
Non
Oui
Type rapprochement 0
2
Aucun
Contrepartie
Trésorerie
Mise en sommeil 0
Non
Oui
Option calcul totaux 0
Non
Oui
Réservé IFRS 0
Non
Oui
Règlement définitif 0
Non
Oui
Suivi trésorerie 0
Non
Oui
(dans l’application Trésorerie)
Lettrage en saisie 0
Non
OUi
Protéger le journal 0
Non
Oui
Personnalisation libellé 69 caractères alphanumériques

## #MCJA — Codes journaux analytiques
*Export modèle : 1 occurrence(s), 4 lignes.*

Champ Code Correspondance/Commentaire
Code journal 6 caractères alphanumériques
Intitulé 35 caractères alphanumériques
Mise en sommeil 0
Non
Oui
Réservé IFRS 0 Non
1 Oui

## #MBQE — Banque
*Export modèle : 5 occurrence(s), lignes 192, 237.*

Champ Code Correspondance/Commentaire
Intitulé
35 caractères alphanumériques
Adresse 35 caractères alphanumériques
Complement 35 caractères alphanumériques
Code postal 9 caractères alphanumériques
Ville 35 caractères alphanumériques
Code région 25 caractères alphanumériques
Pays 35 caractères alphanumériques
Contact 35 caractères alphanumériques
Abrégé 17 caractères alphanumériques
Mode remise 0
2
Fichier magnétique
Télétransmission
Papier
Réservé à Moyens de paiement
Bordereau en devise 0
Non
Oui
Réservé à Moyens de paiement
Date convention Dailly Date au format JJMMAA. Réservé à Moyens de 
paiement
Nature juridique Dailly 35 caractères alphanumériques
Adresse Dailly 35 caractères alphanumériques
Complément Dailly 35 caractères alphanumériques
Code postal Dailly 9 caractères alphanumériques
Ville Dailly 35 caractères alphanumériques
Registre Commerce Société 
Dailly
35 caractères alphanumériques
Code BIC 11 caractères alphanumériques. Réservé à 
Moyens de paiement
Code identification 16 caractères alphanumériques. Réservé à 
Moyens de paiement
Achat en devise 0
Non
Oui
Réservé à Moyens de paiement
Remise 0
2
Mono devise / Mono date d'exécution
Mono devise / Multi date d'exécution
Multi devise / Mono date d'exécution
Champ Code Correspondance/Commentaire
3 Multi devise / Multi date d'exécution
Donneur ordre adresse 0
Non
Oui
Zone obligatoire pour les Virements 
internationaux dans Moyens de paiement
Donneur ordre ville 0
Idem
Donneur ordre code postal 0
Idem
Donneur ordre numéro de Siret 0
Idem
Donneur ordre code 
identification
1
Idem
Donneur ordre ville agence 0
Idem
Donneur ordre code postal 
agence
1
Idem
Donneur ordre type identifiant 0
Idem
Donneur ordre clé RIB 0
Idem
Virement adresse 0
Idem
Virement ville 0
Idem
Virement code postal 0
Idem
Virement numéro de Siret 0
Idem
Virement pays 0
Idem
Virement référence du contrat 
de change
1
Idem
Virement date achat 0
Idem
Virement taux de change 0
Idem
Virement instruction 
particulière
1
Idem
Banque bénéficiaire intitulé 0 Idem
Champ Code Correspondance/Commentaire
Banque bénéficiaire BIC 0
Idem
Banque bénéficiaire adresse 0
Idem
Banque bénéficiaire ville 0
Idem
Banque bénéficiaire code 
postal
1
Idem
Banque bénéficiaire compte 
bancaire
1
Idem
Banque intermédiaire intitulé 0
Idem
Banque intermédiaire BIC 0
Idem
Banque intermédiaire adresse 0
Idem
Banque intermédiaire ville 0
Idem
Banque intermédiaire code 
postal
1
Idem
Banque intermédiaire pays 0
Idem
Téléphone 0
21 caractères alphanumériques
Télécopie 0
21 caractères alphanumériques
Adresse eMail 0
69 caractères alphanumériques
Site 0
69 caractères alphanumériques
Conditions découvert Type 
plafond
1
Intervalle
Seuil
Conditions découvert Base 
calcul intérêts débiteurs
1
Non
Oui
Conditions découvert Taux 
effectif
1
14 caractères numériques
2 fois :
Conditions découvert Valeur 
plafond
14 caractères numériques
Champ Code Correspondance/Commentaire
Conditions découvert Marge 14 caractères numériques
Type application intérêt 0
Fictive
Réelle
Taux effectif intérêt 14 caractères numériques
Assiette intérêt 0
Total créditeur
Solde créditeur : débiteur
Limite intérêt 0
2
Commission mouvement
Intérêt trimestriel
Solde débiteur moyen
Base calcul intérêts créditeurs 0
Total créditeur
Solde créditeur / débiteur
Type calcul commission 0
2
Plafond mensuel
Plafond trimestriel
Solde débiteur moyen
Limite commission 0..999999
Taux CPFD 14 caractères numériques
Commission mouvement frais 14 caractères numériques
Montant frais tenue compte 
frais
14 caractères numériques
Périodicité comptabilisation 
frais
1
Mensuelle
Trimestrielle
Annuelle
Seuil exonération frais 14 caractères numériques
Type exonération frais 0
2
Aucune
Commission mouvement
Solde créditeur moyen
Seuil exonération solde 
créditeur frais
caractères 
numériques
14 caractères numériques
• Mode de perception 0
Aucun
Ligne
• Montant variable HT 14 caractères numériques
• Minimum perçu 14 caractères numériques
• Maximum perçu 14 caractères numériques
• Assujettir la commission/TVA 0
Non
Oui
• Assujettir les frais/TVA 0
Non
Oui
Transfert/Adresse eMail envoi 69 caractères alphanumériques
Champ Code Correspondance/Commentaire
Transfert/Site 69 caractères alphanumériques
Format Virements 0
AFB
SEPA
Format Virements 
internationaux
1
AFB
SEPA
12 fois : 
*Délai Télétransmission 0..99
*Délai Fichier 0..99
*Heure limite Télétransmission Temps[8] ou vide
*Heure limite Fichier Temps[8] ou vide
Virement code service Chaîne AlphaNum Maj[4]
Format Prélèvements 0
AFB
SEPA
Version Format Prélèvements 0
0 = PAIN00800101
1 = PAIN00800102
Version Format Virements 0
0 = PAIN00800101
1 = PAIN00800102
Format Virements 
internationaux
1
0 : AFB
1 :Pain.001.001.03
Compte général Frais OPCVM 3..13 caractères alphanumériques ou vide
Compte général TVA OPCVM 3..13 caractères alphanumériques ou vide
Compte général Moins Value 
OPCVM
3..13 caractères alphanumériques ou vide
Compte général Plus Value 
OPCVM
3..13 caractères alphanumériques ou vide
Virement imputation 0
2
0 = Bénéficiaire / Emetteur
1 = Bénéficiaire
2 = Emetteur
Format Extraits 0
AFB
XML
Version Format Extraits 0..0
N fois : autant de fois qu’il y a 
de comptes à la banque
Code banque 14 caractères alphanumériques
Guichet 17 caractères alphanumériques
Compte 34 caractères alphanumériques
Clé 2 caractères numériques
Commentaire 69 caractères alphanumériques
Code journal 6 caractères alphanumériques
Champ Code Correspondance/Commentaire
Structure banque 0
2
Locale
Etranger
BIN
IBAN
Numéro devise 1..32
Abrégé 5 caractères alphanumériques majuscules
Numéro émetteur 3 * 7 caractères numériques
Adresse agence 35 caractères alphanumériques
Complément agence 35 caractères alphanumériques
Code postal agence 9 caractères alphanumériques
Ville agence 35 caractères alphanumériques
Pays 35 caractères alphanumériques
BIC 11 caractères alphanumériques
Code IBAN 34 caractères alphanumériques
Calcul IBAN 0
Non
oui
Nom agence 35 caractères alphanumériques
Code journal escompte 6 caractères alphanumériques
Code journal encaissement 6 caractères alphanumériques
Compte intra-groupe 0
Non
oui
Raison sociale bénéficiaire 35 caractères alphanumériques
Adresse bénéficiaire 35 caractères alphanumériques
Complément bénéficiaire 35 caractères alphanumériques
Code postal bénéficiaire 9 caractères alphanumériques
Ville bénéficiaire 35 caractères alphanumériques
Pays bénéficiaire 35 caractères alphanumériques
Siret bénéficiaire 14 caractères alphanumériques
Code région bénéficiaire 25 caractères alphanumériques
Code région agence 25 caractères alphanumériques
Pays agence 35 caractères alphanumériques
Compte dépôts Trésor Public 0
Non
Oui
Compte Banque de France 0
Non
Oui
Trésor Public Service dépôts 70 caractères alphanumériques
Trésor Public Type service 0
2
0 = Trésorerie générale
1 = Direction Régionale des Finances Publiques 
Champ Code Correspondance/Commentaire
2 = Direction Départementale des Finances 
Publiques
Trésor Public Codique service 7 caractères alphanumériques
Trésor Public IBAN 35 caractères alphanumériques
Trésor Public BIC 11 caractères alphanumériques
Trésor Public Remise ESI 51 0
Non
Oui
Trésor Public Identifiant 51 9 caractères alphanumériques
BDF Code remettant 5caractères alphanumériques
Mise en sommeil 0
Non
Oui

## #MCTB — Contacts banques
*Export modèle : 2 occurrence(s), 13 lignes.*

Champ Code Correspondance/Commentaire
Nom 35 caractères alphanumériques
Prénom 35 caractères alphanumériques
Service 1..30 Position dans la table des services contacts
Fonction 35 caractères alphanumériques
Téléphone 21 caractères alphanumériques
Téléphone portable 21 caractères alphanumériques
Télécopie 21 caractères alphanumériques
Adresse eMail 69 caractères alphanumériques
Civilité 0
2
M.
Mme
Mlle
Numéro contact 1..30 Position dans la table des types contacts
Compte Facebook 35 caractères alphanumériques
Compte LinkedIn 35 caractères alphanumériques
Compte Skype 35 caractères alphanumériques

## #MCVB — Conditions de valeurs banques
*Absent de l'export modèle — structure non vérifiée sur fichier réel.*

Doit suivre #MBQE ou #MCTB ou #MCVB
Champ Code Correspondance/Commentaire
Code AFB 2 caractères alphanumériques
Sens 0
Décaissement ou Crédit comptable
Encaissement ou Débit comptable
Nombre jours de valeur 0..999
Champ Code Correspondance/Commentaire
Type de jour 0
2
Aucun
Calendaire
Ouvré
Echéance reportée 0
Non
Oui
Exonération commission de 
mouvement
1
Non
Oui

## #MCNB — Conditions éléments banques
*Absent de l'export modèle — structure non vérifiée sur fichier réel.*

Champ Code Correspondance/Commentaire
Code banque élément banque 5 caractères alphanumériques majuscules
Guichet élément banque 5 caractères numériques
Compte élément banque 11 caractères alphanumériques majuscules
Numéro devise élément banque 1..32
Position dans la table des devises
Type plafond 0
Intervalle de montant
Seuil de montant
Base calcul intérêts débiteurs 0
0 = 360 jours
1 = 365 jours
3 fois :
*Valeur plafond 14 caractères numériques
*Taux effectif plafond 14 caractères numériques
Type application intérêt 0
Application fictive
Application réelle
Taux effectif intérêt 14 caractères numériques
Assiette intérêt 0
Total des nombres créditeur 
Nombres créditeur - moins nombres débiteur
Limite intérêt 0
2
Commission de mouvement
Intérêts débiteurs
Pas de limite
Base calcul intérêts créditeurs 0
Total créditeur
Solde créditeur / débiteur
Type calcul commission 0
2
PFD mensuel
PFD trimestriel
Solde débiteur moyen
Limite commission 0..999999
Type plafond commission 0
Intervalle de montant
Seuil de montant
Champ Code Correspondance/Commentaire
3 fois
Valeur plafond commission 14 caractères numériques
Commission 0..999999
Commission mouvement frais 0..999999
Montant frais tenue compte frais 14 caractères numériques
Périodicité comptabilisation frais 0
2
Mois
Trimestre
Année
Méthode calcul frais 0
Balance des intérêts
Total intérêts créditeurs
Seuil exonération frais 14 caractères numériques
Type exonération frais 0
2
Pas d’exonération
Commission de mouvement
Solde créditeur moyen
Seuil exonération solde créditeur 
frais
caractères 
numériques
14 caractères numériques

## #MPIE — Modèle de saisie
*Export modèle : 37 occurrence(s), 4 lignes.*

Champ Code Correspondance/Commentaire
Intitulé 35 caractères alphanumériques
Raccourci 6 caractères alphanumériques majuscules
Type journal 0
2
4
Achat
Vente
Trésorerie
Général
Situation
Code journal 6 caractères alphanumériques

## #MPIC — Modèle de saisie/ Ecriture comptable
*Export modèle : 106 occurrence(s), 83 lignes.*

Fichier lié au Modèle de saisie.
Ce drapeau doit suivre directement le modèle de saisie (#MPIE) auquel il se rapporte, ou un 
autre fichier de Modèle de saisie / Ecritures comptables (#MPIC).
Chaque zone peut comporter :
• Une macro:
• \#M pour Main ou Saisie,
• \#E pour Equilibre,
• \#D pour Double,
• \#I pour Incrémentation,
• \#C pour Calcul,
• ## pour le caractère #.
• Une formule, précédée du signe '=',
• Une chaîne de caractères ou une valeur selon le type de zone,
• Une valeur fixe pour certaines zones (exemple : Numéro devise). Voir ci-dessous.
Champ Code Correspondance/Commentaire
Jour 2 caractères numériques
Pièce 3 ou 13 caractères alphanumériques 
majuscules M
Numéro facture 17 caractères alphanumériques
Numéro compte général 13 caractères
Numéro compte général 
contrepartie
13 caractères
Numéro compte tiers 17 caractères alphanumériques 
majuscules
Numéro compte tiers contrepartie 17 caractères alphanumériques 
majuscules
Intitulé 69 caractères alphanumériques
Numéro règlement -1
30
Aucun (je ne suis pas sûr qu’il affiche -1)
Calcul
Position dans la table des modes de 
règlement
Echéance Date de 6 caractères
Parité 14 caractères numériques
Quantité 14 caractères numériques
Numéro devise -1
1…32
Aucun (je ne suis pas sûr qu’il affiche -1)
Calcul
Position dans la table des devises
Sens 0
Débit
Crédit
Montant 14 caractères
Montant devise 14 caractères
Code taxe 5 caractères alphanumériques
Provenance -1..8
Référence 17 caractères alphanumériques 
majuscules
Information libre1 35 caractères alphanumériques
Information libre2 35 caractères alphanumériques
Information libre3 35 caractères alphanumériques
Information libre4 35 caractères alphanumériques
Information libre5 35 caractères alphanumériques
Champ Code Correspondance/Commentaire
Information libre6 35 caractères alphanumériques
Information libre7 35 caractères alphanumériques
Information libre8 35 caractères alphanumériques
Information libre9 35 caractères alphanumériques
Information libre10 35 caractères alphanumériques
Information libre11 35 caractères alphanumériques
Information libre12 35 caractères alphanumériques
Information libre13 35 caractères alphanumériques
Information libre14 35 caractères alphanumériques
Information libre15 35 caractères alphanumériques
Information libre16 35 caractères alphanumériques
Information libre64 35 caractères alphanumériques

## #MPIA — Modèle de saisie/ Ecriture analytique
*Export modèle : 9 occurrence(s), 4 lignes.*

Fichier lié au Modèle de saisie/ Ecritures comptables.
Ce drapeau doit suivre directement le modèle de saisie/ Ecritures comptables (#MPIC) 
auquel il se rapporte, ou un autre fichier de Modèle de saisie/ Ecritures analytiques (#MPIA).
Chaque zone peut comporter une macro qui peut être :
• \#M pour Main ou Saisie,
• \#E pour Equilibre,
• ## pour le caractère #,
• Caractère %.
• Une formule, précédée du signe '=',
• Une chaîne de caractères ou une valeur selon le type de zone.
Champ Code Correspondance/Commentaire
Numéro analytique 1..11 Position dans la table des plans
Numéro section analytique 13 caractères alphanumériques 
majuscules M
Montant 14 caractères numériques
Quantité 14 caractères numériques

## #MMDG — Modèle de grille
*Export modèle : 4 occurrence(s), lignes 11, 15.*

Champ Code Correspondance/Commentaire
Type 0..1 Analytique
Général
Intitulé 35 caractères alphanumériques
Raccourci Chaîne AlphaNum Maj[6]
N fois :
Numéro analytique 0
1..11
Aucun si répartition générale
Position dans la table des plans
Numéro compte général ou 
analytique
13 caractères alphanumériques majuscules
Type répartition 0
2
Pourcentage
Equilibre
Montant
Valeur répartition 14 caractères numériques ou 14 caractères 
numériques suivant Type répartition

## #MMDR — Modèle de règlement
*Export modèle : 4 occurrence(s), lignes 12, 23, 34.*

Champ Code Correspondance/Commentaire
Intitulé 35 caractères 
alphanumériques
35 caractères alphanumériques
Champ Code Correspondance/Commentaire
N fois :
Numéro règlement 1..30
Condition 0
2
Jours nets
Fin de mois civil
Fin de mois
Nbre jours 0..999
Jours tombée 6 *(0..31)
Type répartition 0
2
Pourcentage
Equilibre
Montant
Valeur répartition 14 caractères numériques ou 14 caractères 
numériques suivant Type répartition

## #MMDA — Modèle d'abonnement
*Export modèle : 3 occurrence(s), lignes 44, 89.*

Champ Code Correspondance/Commentaire
Intitulé 35 caractères alphanumériques
Code journal 6 caractères alphanumériques
Date début 6 caractères au format JJMMAA
Date fin 6 caractères au format JJMMAA
Type périodicité 0
2
Jour
Semaine
Mois
Année
Valeur périodicité 1..99
Intitulé modèle de saisie 35 caractères alphanumériques
Pièce 17 caractères alphanumériques 
majuscules
N fois :
*Date 6 caractères au format JJMMAA
*Montant 14 caractères numériques
*Génération 0
Non
Oui

## #MLIB — Libellé
*Export modèle : 4 occurrence(s), 2 lignes.*

Champ Code Correspondance/Commentaire
Intitulé 35 caractères alphanumériques
Raccourci 6 caractères alphanumériques 
majuscules

## #MBUD — Poste budgétaire
*Export modèle : 7 occurrence(s), lignes 440, 441, 443, 447, 453.*

Champ Code Correspondance/Commentaire
Numéro budget 13 caractères alphanumériques 
majuscules
Intitulé 35 caractères alphanumériques
Type 0
2
Détail
Total
Centralisateur
Sens 0
Charge
Produit
Numéro budget centralisateur 13 caractères alphanumériques 
majuscules
Type répartition 0
1..11
11..20
Général
11 analytiques
10 statistiques
Valeur répartition 21 caractères alphanumériques
Valeurs dotations montants 6 * 36 14 caractères numériques
Valeurs dotations quantités 6 * 36 14 caractères numériques
N fois
Numéro compte général (1) 13 caractères
(1)Ce champ est répété autant de fois que de comptes généraux rattachés.

## #MECG — Ecriture générale
*Export modèle : 279 occurrence(s), 39 lignes.*

Champ Code Correspondance/Commentaire
Code journal 6 caractères alphanumériques
Date 6 caractères au format JJMMAA
Date saisie 6 caractères ou à blanc
Pièce 13 caractères alphanumériques 
majuscules
Numéro facture 17 caractères alphanumériques
Pièce trésorerie 17 caractères alphanumériques
Numéro compte général 3..13 caractères alphanumériques
Numéro compte général contrepartie 3..13 caractères alphanumériques
Numéro compte tiers 17 caractères alphanumériques
Numéro compte tiers contrepartie 17 caractères alphanumériques
Intitulé 69 caractères alphanumériques
Numéro règlement 0..30
Echéance blanc ou date sur 6 caractères au 
format JJMMAA
Parité 14 caractères numériques
Champ Code Correspondance/Commentaire
Quantité 14 caractères numériques
Numéro devise 0
1…32
Aucun
Position dans la table des devises
Sens 0
Débit
Crédit
Montant 14 caractères numériques
Numéro lettre montant 5 caractères alphanumériques 
majuscules
Numéro lettre quantité 5 caractères alphanumériques 
majuscules
Numéro pointage 5 caractères alphanumériques 
majuscules
Nombre de rappels 0..10
Type à-nouveau 0
2
4
Normale
Ecriture reprise en Détail
Ecriture reprise en Solde
Ecriture d'AN Manuel
Ecriture d'AN Résultat
Type révision 0
Non
Oui
Montant devise 14 caractères numériques
Code taxe 5 caractères alphanumériques 
majuscules ou vide
Norme 0
2
Les deux
Nationale
IFRS
Provenance 0
2
4
6
8
Aucune
Nationale
Intra-commu.
Export
Divers 1
Divers 2
Divers 3
Divers 4
Divers 5
Type pénalités 0
2
Aucun
Intérêts de retard
Frais d’impayés
Date pénalités Date au format JJMMAA ou vide
Date relance Date au format JJMMAA ou vide
Champ Code Correspondance/Commentaire
Date de rapprochement Date au format JJMMAA ou vide
Référence 17 caractères alphanumériques
Statut règlement 0
2
Non réglé
A traiter GC
Traité GC
Montant réglé 14 caractères numériques
Date dernier règlement Date au format JJMMAA ou vide
Date opération Date au format JJMMAA ou vide
Export Rapprochement 0
Non exporté
Exporté
Date clôture Date au format JJMMAA ou vide

## #MECA — Ecriture analytique
*Export modèle : 2 occurrence(s), 4 lignes.*

Champ Code Correspondance/Commentaire
Numéro analytique 1..11 Position dans la table des plans 
analytiques
Numéro section analytique 13 caractères alphanumériques 
majuscules
Montant 14 caractères numériques
Quantité 14 caractères numériques

## #MRGR — Registre révision
*Absent de l'export modèle — structure non vérifiée sur fichier réel.*

Doit suivre #MECG ou #MECA
Champ Code Correspondance/Commentaire
Date début 6 caractères au format JJMMAA
Date fin 6 caractères au format JJMMAA
Réviseur 35 caractères alphanumériques
Contrôleur 35 caractères alphanumériques
Commentaire 69 caractères alphanumériques
Date révision 6 caractères au format JJMMAA
Date contrôle 6 caractères au format JJMMAA

## #MRGT — Registre taxe
*Export modèle : 138 occurrence(s), 91 lignes.*

Fichier lié aux Ecritures comptables.
Ce drapeau doit suivre directement l'écriture comptable (#MECG) à laquelle il se rapporte, 
une écriture analytique (#MECA), ou un registre révision (#MRGR).
Champ Code Correspondance/Commentaire
Numéro chrono Long
Type registre 0
2
4
Achat
Vente
Général achat
Général vente
Règlement achat
Règlement vente
Date registre 6 caractères au format JJMMAA
Date pièce 6 caractères au format JJMMAA
Numéro compte tiers 17 caractères alphanumériques 
majuscules
Provenance 0
2
4
6
Aucune Nationale
Intra-communautaire
Export
Divers 1
Divers 2
Divers 3
Divers 4
Divers 5
Compte de taxe 10 * 3..13 
caractères 
alphanumériques
Type taux 10 * (0..2) Taux % Montant F Quantité U
Taux 10 * 14 caractères numériques ou 
Montant[14
Base taxable 10 * 14 caractères numériques
Montant taxe 10 * 14 caractères numériques
Code taxe 10 * 5 caractères alphanumériques 
majuscules
Nombre de factures/tickets 14 caractères numériques
Type de transaction 0..24 0..24
Numéro facture/ticket De 9 caractères numériques
Numéro facture/ticket A 9 caractères numériques
Numéro facture rectifiée 69 caractères alphanumériques
Motif 0..24 69 caractères alphanumériques
Type ligne 0 Aucun
Champ Code Correspondance/Commentaire
1 10*(0..1) Acompte

## #MRAN — OD et reports analytiques / Report analytique
*Absent de l'export modèle — structure non vérifiée sur fichier réel.*

Champ Code Correspondance/Commentaire
Date 6 caractères au format JJMMAA
Numéro compte général 3..13 caractères 
alphanumériques
Numéro analytique 1..11 Position dans la table des plans 
analytiques
Numéro section analytique 13 caractères alphanumériques 
majuscules
Sens 0
Débit
Crédit
Montant analytique 14 caractères numériques
Quantité analytique 14 caractères numériques
Type 0
OD analytique
Report à nouveau analytique
Code journal analytique 6 caractères alphanumériques
Pièce 13 caractères alphanumériques 
majuscules
Numéro facture 17 caractères alphanumériques 
majuscules
Intitulé 69 caractères alphanumériques
Norme 0
2
Les deux 
Nationale
IFRS

Champ Code Correspondance/Commentaire
Date 6 caractères au format JJMMAA
Numéro compte général 3..13 caractères 
alphanumériques
Numéro analytique 1..11 Position dans la table des plans 
analytiques
Numéro section analytique 13 caractères alphanumériques 
majuscules
Sens 0
Débit
Crédit
Montant analytique 14 caractères numériques
Quantité analytique 14 caractères numériques
Type 0
OD analytique
Report à nouveau analytique
Code journal analytique 6 caractères alphanumériques
Pièce 13 caractères alphanumériques 
majuscules
Numéro facture 17 caractères alphanumériques 
majuscules
Intitulé 69 caractères alphanumériques
Norme 0
2
Les deux 
Nationale
IFRS

## #MEXT — Extrait bancaire
*Export modèle : 12 occurrence(s), lignes 98, 127, 156, 272, 417, 625, 649.*

Champ Code Correspondance/Commentaire
Code banque élément banque 14 caractères alphanumériques
Guichet élément banque 17 caractères alphanumériques
Compte élément banque 34 caractères alphanumériques
Numéro devise élément banque 1..32 Position dans la table des devises
Type 0
Saisie manuelle
Téléchargé
Numéro de relevé 35 caractères alphanumériques
Etat 0
2
Non rapproché
Partiellement rapproché
Totalement rapproché
Date ancien solde 6 caractères au format JJMMAA
Ancien solde 14 caractères numériques
Date nouveau solde 6 caractères au format JJMMAA
Etat opérations bancaires 0
0 = Non incorporé dans les op. 
bancaires
1 = Incorporé dans les op. 
bancaires
N fois :
• Date opération 6 caractères au format 
JJMMAA
• Date valeur 6 caractères au format 
JJMMAA
• Intitulé 141caractères alphanumériques
• Pièce 35 caractères alphanumériques
• Etat 0
Non
Oui
• Indisponible 0
Non
Oui
• Exonéré 0
Non
Oui
• Montant en devise RIB 14 caractères numériques
• Référence 35 caractères alphanumériques
• Code opération interne 4 caractères alphanumériques
• Code AFB 2 caractères alphanumériques
• Code motif rejet 2 caractères alphanumériques
• Lettre de rapprochement 8 caractères alphanumériques
• Montant en devise compte 14 caractères numériques
Champ Code Correspondance/Commentaire
• Type pointage 0
2
0 = Non pointé
1 = Pointage unitaire
2 = Pointage manuel
3 = Pointage auto
• Numéro pointage 3 caractères alphanumériques
• Date pointage Date au format JJMMAA ou vide
• Date initiale règlement Date au format JJMMAA ou vide
• Référence transaction 35 caractères alphanumériques
• Référence initiale 35 caractères alphanumériques
• Numéro de chèque 35 caractères alphanumériques
• Référence Unique Mandat 35 caractères alphanumériques
• Code ISO 4 caractères alphanumériques
• Donneur ordre 35 caractères alphanumériques
• Identification 35 caractères alphanumériques
• Bénéficiaire 35 caractères alphanumériques
• Code motif rejet SEPA 4 caractères alphanumériques
• Domaine 4 caractères alphanumériques
• Code famille 4 caractères alphanumériques
• N fois : // Libellés complémentaires des 
éléments extraits
• Type 0
2
4
6
8
10
12
14
16
18
0 = (vide)
1 = LIB
2 = MMO
3 = NPY
4 = IPY
5 = NBE
6 = IBE
7 = NPO
8 = IPO
9 = NBU
10 = IBU
11 = LCC
12 = LC2
13 = LCS
14 = CBE
15 = RUM
16 = CPY
17 = RCN
18 = REF
• Libellé 83 caractères alphanumériques

## #CMOTIF — Motifs de rectification
*Absent de l'export modèle — structure non vérifiée sur fichier réel.*

Champ Code Correspondance/Commentaire
Intitulé 69 caractères alphanumériques
Code 2 caractères numériques

## #MRFC — Résultat/Fourchettes de comptes
*Absent de l'export modèle — structure non vérifiée sur fichier réel.*

Champ Code Correspondance/Commentaire
N_Resultat 1..50 1..50
Fourchette début Radical 3..13 caractères 
alphanumériques
Fourchette fin Radical 3..13 caractères 
alphanumériques

## #MRJS — Motifs de rejet SEPA
*Export modèle : 49 occurrence(s), 2 lignes.*

49 fois
Champ Code Correspondance/Commentaire
Code rejet 4 caractères alphanumériques
Intitulé 35 caractères alphanumériques

## #MPLJ — Personnalisation des libellés (dans les codes
*Export modèle : 1 occurrence(s), 5 lignes.*

journaux)
5 fois (Achat, Ventes, Trésorerie Général, Situation)
Champ Code Correspondance/Commentaire
Intitulé 69 caractères alphanumériques

## #MMEX — Mentions d’exonération de TVA
*Export modèle : 8 occurrence(s), 3 lignes.*

Champ Code Correspondance/Commentaire
Intitulé 100 caractères alphanumériques
Code motif 20 caractères alphanumériques
Code catégorie 2 caractères alphanumériques

## #MFAR — Facture électronique-Réception facture
*Absent de l'export modèle — structure non vérifiée sur fichier réel.*

(réservé facture électronique et disponible sage100v10.x)
Champ Code Correspondance/Commentaire
Type code routage 0
2
4
Code service
GLN
ODETTE
SWIFT
AUTRE
Code routage 100 caractères alphanumériques
Application préféré 0
2
Gestion commeriale
Comptabilité
Application externe

## #MMRE — Motifs refus facture
*Export modèle : 26 occurrence(s), 6 lignes.*

Champ Code Correspondance/Commentaire
Code motif 20 caractères alphanumériques
Refusée
1
Non
Oui
En litige 0
Non
Oui
Approuvée partiellement 0
Non
Oui
Suspendue
1
Non
Oui

## #MCAC — Codes action facture
*Export modèle : 1 occurrence(s), 2 lignes.*

Champ Code Correspondance/Commentaire
Intitulé 0 250 caractères alphanumériques
Code action 25 caractères alphanumériques

## #MEDN — Liens Ecritures / Entêtes documents Factures
*Absent de l'export modèle — structure non vérifiée sur fichier réel.*

(réservé facture électronique et disponible sage100v11x)
Champ Code Correspondance/Commentaire
Date facture DGI 0 Date courte 6 caracteres
Flux fiscal 0 a 6 0..5 (vente), 0.1.2.6 (achat), 0 
(autres)
Exclure Flux encaissement 0
Non
Oui
