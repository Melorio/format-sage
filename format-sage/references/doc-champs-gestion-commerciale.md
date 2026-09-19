# Documentation éditeur Sage 100 Gestion commerciale v12.25 — champs par drapeau

Extraction fidèle de la documentation officielle (`#VER 33`), découpée par drapeau.

**Ne pas charger ce fichier en entier.** Extraire la seule section utile :
`grep -A 60 '^## #CART' references/doc-champs-gestion-commerciale.md`

La documentation regroupe les champs répétés là où le fichier réel les développe sur des
lignes consécutives, et elle nomme parfois un drapeau de façon tronquée : le fichier contient
`#CPROJHISTO` là où la documentation écrit `#CPRO`. Croiser avec `catalogue-drapeaux-gc.md`
avant d'écrire quoi que ce soit.

## #CDOS — Dossier entreprise
*Export modèle : 1 occurrence(s), 187 lignes.*

Champ Code Correspondance/Commentaire
Raison sociale 35 caractères alphanumériques
Activité 35 caractères alphanumériques
Adresse 35 caractères alphanumériques
Complément 35 caractères alphanumériques
Code postal 9 caractères alphanumériques
Ville 35 caractères alphanumériques
Région 25 caractères alphanumériques
Pays 35 caractères alphanumériques
Commentaire 69 caractères alphanumériques
N° de SIRET 14 caractères alphanumériques
NAF (APE) 5 caractères alphanumériques
N° identifiant 25 caractères alphanumériques
Longueur comptes 
généraux
3 à 13
Longueur flottante
Longueur fixe
Longueur comptes 
analytiques
3 à 13
Longueur flottante
Longueur fixe
Format quantité 31 caractères alphanumériques
Format prix unitaire 31 caractères alphanumériques
Arrondi de pied 0 à 10 Liste des arrondis (paramètres société)
Champ analytique article 0
1 à 10
Si aucun champ désigné
Numéro de champ

Champ Code Correspondance/Commentaire
Champ analytique Affaire 0
1 à 10
Si aucun champ désigné
Numéro de champ
Délai livraison 0
2
Date
Semaine
Julien
Confirmation suppression 0
2
Aucune
Elément
Liste
Gestion stock négatif 0
Non
Oui
Marge en saisie 0
Non
Oui
Import en mise à jour 0
2
Sans modification
Modification
Choix manuel
Choix remise 0
2
4
6
8
10
12
Manuelle
Remise article
Remise famille
Remise client
Remise en cumul
Remise en cascade
Choix manuel et cat./ famille
Remise article et cat./ famille
Remise famille par client et cat./ famille
Remise famille par cat. Tarifaire
Remise client et cat./ famille
Remise cumulée et cat./ famille
Remise en cascade et cat./ famille
Unité de poids 0
2
4
Tonne
Quintal
Kilogramme
Gramme
Milligramme
Article escompte 18 caractères alphanumériques
Alerte agenda 0
Aucune
A l'ouverture

Champ Code Correspondance/Commentaire
Délai pré-alerte 0-999
Interprétation EAN 0
Non
Oui
Préfixe 20 (EAN) 0
Appel du prix
Lecture du prix
Unité des prix (EAN) 0
Centimes
Décimes
Unité des poids (EAN) 0
2
4
Tonne
Quintal
Kilogramme
Gramme
Milligramme
Article TVA non perçue 18 caractères alphanumériques majuscules
Compte général client 13 caractères alphanumériques majuscules
Compte général 
fournisseur
13 caractères alphanumériques majuscules
Valeur en devise 0
Conversion valeurs
Cumul des lignes
Gestion des indisponibilités 0
2
Bon de commande
Préparation de livraison
Bon de livraison
Aucun
Calcul des échéances 0
2
4
Bon de commande
Préparation de livraison
Bon de livraison
Facture
Facture/date de livraison réalisée
Affichage stock en saisie 0
Oui
Non

Champ Code Correspondance/Commentaire
Contrôle encours client 0
2
Aucun
Création de l’en-tête
Validation de la ligne
Fermeture du document
Base encours client 0
2
Solde comptable
Solde + FA
Solde + FA + BL
Solde + FA + BL + BC
Contremarque 0
Manuelle
Automatique
Monnaie de tenue 
commerciale
1 à 32 Liste des devises
Devise d’équivalence 0
1 à 32
Aucune
Liste des devises
Report section en achat 0
1 à 10
Pas de report
Plan analytique de report
Code journal ventes 6 caractères alphanumériques
Code journal achats 6 caractères alphanumériques
Règlements ventes 6 caractères alphanumériques
Règlements achats 6 caractères alphanumériques
N° de pièce 0
N° facture
Automatique
Référence 0
N° facture
Référence
Avoirs et retours 
(engagement)
1
Inverser le sens
Valeur négative
Libellé ventes 
(engagement)
35 caractères alphanumériques
Libellé achats 
(engagement)
35 caractères alphanumériques

Champ Code Correspondance/Commentaire
Devise (transfert comptable 
engagement)
1
3
Aucune
Devise
Tenue commerciale
Les deux
Transfert devise 
(engagement)
1
3
Compte tiers
Selon option saisie devise
Tous les comptes
Tous les comptes avec équilibre
Analytique (engagement) 0
2
4
Aucun
Article
Affaire
Les deux
Tous
Quantité (engagement) 0
2
Aucun
Compte HT
Selon option saisie quantité
Tous les comptes
Infos libres entête 
(engagement)
1
3
Aucun
Compte TTC
Compte HT
Compte TVA
Tous les comptes
Appel des tiers en saisie 0
2
Sur le numéro
Sur l’abrégé
Sur le code postal
Seuil 0 Zone réservée pour version ultérieure
Transfert document de 
caisse
1
Non
Oui
Journal de caisse 6 caractères alphanumériques
Mouvementer la caisse 0
Non
Oui
Compte écart conversion 
débit
Format Compte

Champ Code Correspondance/Commentaire
Compte écart conversion 
crédit
Format Compte
N° de pièce écriture 0
Numéro pièce
Automatique
Référence pièce écriture 0
Numéro pièce
Référence
Code journal écart 
règlement
6 caractères alphanumériques
Ecart maximum de 
règlement
Format Montant
Compte débit écart 
règlement
Format Compte
Compte crédit écart 
règlement
Format Compte
Comptabilisation 
mouvement divers caisse
1
Non
Oui
Compte débit mouvement 
divers caisse
Format Compte
Compte crédit mouvement 
divers caisse
Format Compte
Identifier le caissier à 
chaque opération
1
Non
Oui
Client vente comptoir 17 caractères alphanumériques majuscules
Type de tarif par défaut 0
HT
TTC
Compte virement interne Format Compte
Souche clôture caisse 0.49 Numéro de la souche
Regroupement ticket 0 Par jour

Champ Code Correspondance/Commentaire
2
4
Par semaine
Par quinzaine
Par mois
Une facture par ticket
Regroupement règlement 0
2
Aucun
Espèce uniquement
Tous les règlements
Dépôt émetteur 35 caractères alphanumériques
Adresse E-mail site 
principal
69 caractères alphanumériques
Nombre lignes afficheur 0..999
Nombre colonnes afficheur 0..999
Code journal écart 
conversion
6 caractères alphanumériques
Ecart maximum conversion Format Montant
Articles non livrés 0
2
Aucune
En indisponibilité totale
Quantité à zéro
Les deux
Recalcul modèles 0
Non coché
Coché
Téléphone 21 caractères alphanumériques
Télécopie 21 caractères alphanumériques
E-mail 69 caractères alphanumériques
Site 69 caractères alphanumériques
Mise à jour du prix d’achat 
en saisie
1
Aucune
BA
PC
BC

Champ Code Correspondance/Commentaire
4
BL
FA
Création des références 
fournisseurs
1
Aucune
Création automatique
Création avec confirmation
Date des factures 
générées
1
Premier jour période
Dernier jour période
Générer la facture sur le 
compte client associé à la 
caisse
1
Non
Oui
Mode de règlement 
mouvements caisse
1 à 30
Contrôle unicité des lots 0
Non
Oui
Monnaie de tenue 
comptable
1 à 32 Liste des devises
Application norme IFRS 0
Non
Oui
Saisie IFRS 0
Journaux
Tous
Plan analytique IFRS 0
1..11
Aucun
Numéro de plan analytique
Transfert IFRS 0
2
Aucun
Comptes HT
Tous les comptes
Compte factures comptoir 
débit
13 caractères alphanumériques majuscules
Compte factures comptoir 
crédit
13 caractères alphanumériques majuscules

Champ Code Correspondance/Commentaire
Unité de temps 0
2
Heure centième
Minutes
Heures
Priorité livraison 1 0
2
4
Date de livraison
Priorité client
Reliquat
Montant HT
Date document
Priorité livraison 2 0
2
4
Date de livraison
Priorité client
Reliquat
Montant HT
Date document
Priorité livraison 3 0
2
4
Date de livraison
Priorité client
Reliquat
Montant HT
Date document
Echéance commandes à 
livrer
0 à 999
Unité échéance 
commandes à livrer
1
Jours
Semaines
Mois
Gestion reliquat livraison 0
2
Aucun
Ligne de document
Document complet
Quantité à préparer 0
2
Disponible
Aucune
Stock négatif
Génération des PL 0
Une préparation par BC
Une préparation par client
Statut des PL 0
2
Saisi
Préparé
A livrer
Valeur en devise 
(engagement)
1
Conversion valeurs
Cumul des lignes

Champ Code Correspondance/Commentaire
Analytique 0
2
4
Aucun
Article
Affaire
Les deux
Tous
Devise (transfert 
comptable)
1
3
Aucun
Devise
Tenue commerciale
Les deux
Transfert devise 0
2
Compte tiers
Selon option saisie devise
Tous les comptes
Tous les comptes avec équilibre
Code journal ventes 
(engagement)
6 caractères alphanumériques
Code journal achats 
(engagement)
6 caractères alphanumériques
N° de pièce (engagement) 0
N° pièce
Automatique
Référence (engagement) 0
N° pièce
Référence
Avoirs et retours 0
Inverser le sens
Valeur négative
Libellé ventes 35 caractères alphanumériques
Libellé achats 35 caractères alphanumériques
Quantité (engagement) 0
2
Aucun
Compte HT
Selon option saisie quantité
Tous les comptes

Champ Code Correspondance/Commentaire
Infos libres entête 
(engagement)
1
3
Aucun
Compte TTC
Compte HT
Compte TVA
Tous les comptes
Transfert IFRS 
(engagement)
1
Aucun
Compte HT
Tous les comptes
Type série/lot 0
2
4
Alphanumérique
Numérique
EAN8
EAN13
SSCC-18
Type complément série/lot 0
2
4
Alphanumérique
Numérique
EAN8
EAN13
SSCC-18
Déclaration fond de caisse 0
Globale
Détail billets et pièces
Intégration des fichiers 
reçus
1
Tous
Fichiers pour le dossier
Comptabilisation des bons 
d’achat
1
Non
Oui
Exercice prévision Format Date
Périodicité prévisions 0
2
4
Année
Semestre
Trimestre
Mois
Semaine
Saisie données en sommeil 0
Non
Oui

Champ Code Correspondance/Commentaire
Gestion multi-emplacement 0
Non
Oui
Priorité de déstockage 0
2
Emplacement non principal
Emplacement principal
Zone emplacement
Gestion des emplacements 
de contrôle
1
Non
Oui
Report des informations 
liées
1
3
Aucun
Ventes vers achats
Achats vers ventes
Les deux
Report du prix de revient lié 0
Non
Oui
Montant maximum ticket Format Montant
Comptabilisation des 
règlements
1
Non
Oui
Base calcul marge 0
2
4
Prix de revient
CMUP
Dernier prix d’achat
Prix d’achat
Coût standard
Gestion planning 0
Non
Oui
Evénement planning 0
Automatique
Manuel
Nom contact émetteur 35 caractères alphanumériques
Prénom contact émetteur 35 caractères alphanumériques
Format factures 0 Par défaut Réservé EXPORT
Période de validité de 
saisie
3 chiffres maximum (0 à 999)

Champ Code Correspondance/Commentaire
Référence structurée 0
Non
Oui
Certificat 69 caractères alphanumériques
Intitulé libellé poids net 21 caractères alphanumériques
Intitulé libellé poids brut 21 caractères alphanumériques
Création article en saisie 0
Non
Oui
Création tiers en saisie 0
Non
Oui
Création affaire en saisie 0
Non
Oui
Intitulé libelle 
conditionnement
21 caractères alphanumériques
Intitulé libellé entête 1 21 caractères alphanumériques
Intitulé libellé entête 2 21 caractères alphanumériques
Intitulé libellé entête 3 21 caractères alphanumériques
Intitulé libellé entête 4 21 caractères alphanumériques
Intitulé libellé référence 21 caractères alphanumériques
Taux escompte Format double
Mention d'exonération de 
TVA
60 caractères alphanumériques
Capital Format double
Forme juridique 35 caractères alphanumériques
Mode de saisie 0 Aucun

Champ Code Correspondance/Commentaire
2
Afficher la fenêtre à la validation de l’entête
Afficher la fenêtre à la validation de la ligne
Afficher la fenêtre dans les deux cas
Compte Facebook 35 caractères alphanumériques
Compte LinkedIn 35 caractères alphanumériques
Prospect en création client 0
Non
Oui
Calendrier société 35 caractères alphanumériques
Créer un rendez-vous 
Outlook
1
Non
Oui
Alerte stock négatif 0
Non
Oui
Article facture d’acompte 18 caractères alphanumériques majuscules
Appliquer mise en forme 0
Non
Oui
Apposer logo Factur-X 0
Non
Oui
Emplacement logo FacturX0
2
En haut à droite
En haut à gauche
En bas à droite
En bas à gauche
Option paiement TVA/Débit 0
Non
Oui
Date application Format Date
Date résiliation Format Date
Régime 0 Réel normal – CA3

Champ Code Correspondance/Commentaire
2
4
Mini-réel – CA3
Réel simplifié – CA12
Réel simplifié agriculture – CA3
Non assujetti TVA
Franchise en base TVA
Format facture 0
Facture au format PDF respectant la norme FacturX
Facture au format PDF
Export de la personnalisation de la langue

## #MPLB — Export de la personnalisation de la langue
*Export modèle : 1 occurrence(s), 3 lignes.*

Champ Code Correspondance/Commentaire
Intitulé personnalisé 
langue Aucune
21 caractères alphanumériques
Intitulé personnalisé 
langue 1
21 caractères alphanumériques
Intitulé personnalisé 
langue 2
21 caractères alphanumériques
Export de la personnalisation du bouton Actions

## #CBTNACT — Export de la personnalisation du bouton Actions
*Export modèle : 1 occurrence(s), 20 lignes.*

Champ Code Correspondance/Commentaire
Vente : Bouton 1 0 à 14
Vente : Bouton 2 0 à 14
Vente : Bouton 3 0 à 14

Champ Code Correspondance/Commentaire
Vente : Bouton 4 0 à 14
Vente : Bouton 5 0 à 14
Achat : Bouton 1 0 à 10
Achat : Bouton 2 0 à 10
Achat : Bouton 3 0 à 10
Achat : Bouton 4 0 à 10
Achat : Bouton 5 0 à 10
Stock : Bouton 1 0 à 13
Stock : Bouton 2 0 à 13
Stock : Bouton 3 0 à 13
Stock : Bouton 4 0 à 13
Stock : Bouton 5 0 à 13
Interne : Bouton 1 0 à 11
Interne : Bouton 2 0 à 11
Interne : Bouton 3 0 à 11
Interne : Bouton 4 0 à 11

Champ Code Correspondance/Commentaire
Interne : Bouton 5 0 à 11
Ordre d’affectation des boutons (tout domaine confondu) :
• 0 : Aucune
• 1 : Insérer une ligne
• 2 : Associer un texte complémentaire
• 3 : Insérer un sous-total
• 4 : Saisir les emplacements
• 5 : Intégrer des documents
• 6 : Utiliser un modèle/ prestations type
• 7 : Recalculer les modèles d’enregistrement
• 8 : Voir les informations sur une ligne
• 9 : Voir les informations sur le document lié
• 10 : Consulter l’historique du document
• 11 : Afficher le planning
• 12 : Voir les informations sur le projet rattaché
• 13 : Interroger le stock prévisionnel
• 14 : Recalculer le PR du composé
Les affectations possibles par domaine sont les suivantes : Vente de 0 à 14, Achat de 0 à 10, Stock 
0,1,2,4,7,8,9,12,14, Internes 0,1,2,3,4,6,7,8,11
Communication

## #CCOM — Communication
*Export modèle : 1 occurrence(s), 19 lignes.*

Champ Code Correspondance/Commentaire
Catégorie tarifaire 1 à 32
Catégorie comptable 1 à 50
Souche par défaut 0 à 49
Dépôt de stockage 35 caractères alphanumériques
Article d’attente 18 caractères alphanumériques

Champ Code Correspondance/Commentaire
Dernier numéro de 
commande site Réservé pour une future version
Modèle Réservé pour une future version
Envoi accusé de réception Réservé pour une future version
Nom du site marchand Réservé pour une future version
Mot de passe du site Réservé pour une future version
Condition livraison 1 à 30
Mode expédition 1 à 50
Périodicité 1 à 10
Statut BC
1
Saisi
Confirmé
A livrer
Régime 2 caractères numériques 0 à 99
Transaction 2 caractères numériques 0 à 99
Nb facture 0 à 99
Colisage 0 à 999
Type colis 1 à 10
Groupes d’événements agenda - Paramètres société

## #CGAG — Groupes d’événements agenda - Paramètres société
*Export modèle : 1 occurrence(s), 200 lignes.*

Champ Code Correspondance/Commentaire
Intitulé 35 caractères alphanumériques
Intéressé
2
4
6
Dépôt
Client
Fournisseur
Représentant
Article
Ressource
Rendre la ressource 
indisponible
1
Non
Oui
Créer un rendez-vous 
Outlook
1
Non
Oui
Le fichier doit comporter 50 groupes d’événements agenda soit 200 lignes au total.
Evénements agenda - Paramètres société

## #CEAG — Evénements agenda - Paramètres société
*Export modèle : 8 occurrence(s), lignes 2, 3, 4, 5.*

Champ Code Correspondance/Commentaire
N° groupe événements 1 à 50
Evénement 21 caractères alphanumériques
Le numéro de groupe doit être rappelé pour chaque groupe d'événement.
Catégories comptables - Paramètres société

## #CCCO — Catégories comptables - Paramètres société
*Export modèle : 1 occurrence(s), 250 lignes.*

Champ Code Correspondance/Commentaire
Catégories comptables 35 caractères alphanumériques

Champ Code Correspondance/Commentaire
Taxation hors France
(unique pour catégorie 
Vente et Achat)
1
Non
Oui
Le fichier doit comporter 50 catégories comptables pour chacun des intitulés soit 250 lignes au total.
Paramètres société

## #CCATAL — Paramètres société
*Export modèle : 39 occurrence(s), 5 lignes.*

Champ Code Correspondance/Commentaire
Intitulé 35 caractères alphanumériques
Code 2 caractères alphanumériques
Suivi stock 0
Oui
Non
Niveau 0
2
Niveau 1
Niveau 2
Niveau 3
Niveau 4
Intitulé parent 35 caractères alphanumériques
Catégories tarifaires - Paramètres société

## #CCCL — Catégories tarifaires - Paramètres société
*Export modèle : 1 occurrence(s), 64 lignes.*

Champ Code Correspondance/Commentaire
Catégories de clients 35 caractères alphanumériques
Type tarif catégorie 0
HT
TTC
Le fichier peut comporter jusqu’à 32 catégories tarifaires soit 64 lignes.
Le programme Sage 100c Gestion Commerciale permet de gérer 32 catégories tarifaires différentes. 
Le programme Sage 30 Gestion Commerciale n’en gère que 16. En cas d’importation d’un fichier 

généré avec une version de la ligne 100, seules les 16 premières catégories tarifaires seront reprises 
dans une version de la ligne 30.
Les zones Intitulé et Type de tarif sont répétées 16 fois.
Champs statistiques articles - Paramètres société

## #CSTA — Champs statistiques articles - Paramètres société
*Export modèle : 1 occurrence(s), 5 lignes.*

Champ Code Correspondance/Commentaire
Champs statistiques 35 caractères alphanumériques
Le fichier doit comporter 5 champs statistiques articles.
Enumérés statistiques articles - Paramètres société

## #CSAV — Enumérés statistiques articles - Paramètres société
*Export modèle : 2 occurrence(s), lignes 3, 4.*

Champ Code Correspondance/Commentaire
Champs statistiques 1 à 5
Enumérés statistiques 21 caractères alphanumériques
Le numéro de champ doit être rappelé pour chaque énuméré statistique.
Champs statistiques tiers - Paramètres société

## #CSTT — Champs statistiques tiers - Paramètres société
*Export modèle : 1 occurrence(s), 10 lignes.*

Champ Code Correspondance/Commentaire
Champs statistiques 35 caractères alphanumériques
Le fichier doit comporter 10 champs statistiques tiers.
Enumérés statistiques tiers - Paramètres société

## #CSTV — Enumérés statistiques tiers - Paramètres société
*Export modèle : 8 occurrence(s), 2 lignes.*

Champ Code Correspondance/Commentaire
Champs statistiques 1 à 10
Enumérés statistiques 21 caractères alphanumériques
Le numéro de champ doit être rappelé pour chaque énuméré statistique.
Codes risques- Paramètres société

## #CRIS — Codes risques- Paramètres société
*Export modèle : 1 occurrence(s), 40 lignes.*

Champ Code Correspondance/Commentaire
Intitulé 35 caractères alphanumériques
Action 1
3
A livrer
A surveiller
A bloquer
Minimum Format Double
Maximum Format Double
Le fichier doit comporter 10 codes risques soit 40 lignes au total.
Conditions de livraison - Paramètres société

## #CCOL — Conditions de livraison - Paramètres société
*Export modèle : 1 occurrence(s), 60 lignes.*

Champ Code Correspondance/Commentaire
Intitulé 35 caractères alphanumériques entrelacées avec le 
champ suivant
Code livraison 4 caractères alphanumériques
Le fichier doit comporter 30 conditions de livraison soit 60 lignes.
Intitulés Conditionnement - Paramètres société

## #CCON — Intitulés Conditionnement - Paramètres société
*Export modèle : 1 occurrence(s), 20 lignes.*

Champ Code Correspondance/Commentaire
Intitulé 35 caractères alphanumériques
Le fichier doit comporter 20 intitulés de conditionnement.
Enumérés conditionnement - Paramètres société

## #CUA1 — Enumérés conditionnement - Paramètres société
*Export modèle : 1 occurrence(s), 10 lignes.*

Champ Code Correspondance/Commentaire
N° intitulé 1 à 20
Enuméré conditionnement 35 caractères alphanumériques
Quantités Format Quantité
Code EDI 3 caractères alphanumériques majuscules
Le numéro d’intitulé doit être rappelé pour chaque conditionnement.
Devises - Paramètres société

## #CDEV — Devises - Paramètres société
*Export modèle : 1 occurrence(s), 640 lignes.*

Champ Code Correspondance/Commentaire
Intitulé 35 caractères alphanumériques
Format 31 caractères alphanumériques
Cours Format Double
Cours période Format Double
Unité monétaire 21 caractères alphanumériques
Sous-unité monétaire 21 caractères alphanumériques

Champ Code Correspondance/Commentaire
Code ISO 5 caractères alphanumériques
Sigle 5 caractères alphanumériques
Mode de cotation 0
Certain
Incertain
Devise de cotation 1 à 32 Numéro de la devise
Cours clôture 14 caractères numériques
Date limite Format Date
Cours ancienne cotation 14 caractères numériques
Mode ancienne cotation 0
Certain
Incertain
Ancienne devise de 
cotation
1 à 32 Numéro de la devise
Code remise 0
2
Aucun
Blanc
Franc
Euro
Zone euro 0
Non
Oui
Code ISO num 5 caractères alphanumériques
Date mise à jour Date
Heure mise à jour Heure
Le fichier doit comporter 32 devises soit 640 lignes au total.
Gammes articles - Paramètres société

## #CGAM — Gammes articles - Paramètres société
*Export modèle : 1 occurrence(s), 100 lignes.*

Champ Code Correspondance/Commentaire
Type 1
3
Produit
Remise par quantité
Remise par montant
Prix net
Intitulé 35 caractères alphanumériques
Le fichier doit comporter 50 gammes soit 100 lignes au total.
Enumérés gamme - Paramètres société

## #CDGA — Enumérés gamme - Paramètres société
*Export modèle : 7 occurrence(s), lignes 3, 4, 6, 7, 9.*

Champ Code Correspondance/Commentaire
Numéro gamme 1 à 50
Intitulé 35 caractères alphanumériques si Type 1 (Produit)
Format Quantité si Type 2 (Remise par quantité)
Format Montant si Type 3 (Remise par montant)
Le numéro de gamme doit être rappelé pour chaque gamme.
Informations libres - Paramètres société

## #CINF — Informations libres - Paramètres société
*Export modèle : 7 occurrence(s), lignes 6, 11, 16, 21, 41.*

Champ Code Correspondance/Commentaire
Fichier 0
2
4
6
Articles
Comptes généraux
Sections analytiques
Clients/Fournisseurs
En-têtes des documents
Lignes de document
Numéro série/lot
Ressources
Intitulé de l’information 31 caractères alphanumériques

Champ Code Correspondance/Commentaire
Type de l’information 0
2
4
Texte
Valeur
Date
Date longue
Montant
Table
Longueur du champ 69 caractères alphanumériques si Type = 0, sinon 
laisser à blanc
Application source Zone vide si application source = «Toutes»
COLU si application source = «Gestion 
commerciale/SCD»
Formule Formule de calcul si Valeur calculée (1024 
caractères)
Vide dans les autres cas
Le fichier doit comporter 64 informations libres, soit 384 lignes, mais seulement en création de fichier.
Modes arrondi - Paramètres société

## #CARR — Modes arrondi - Paramètres société
*Export modèle : 1 occurrence(s), 20 lignes.*

Champ Code Correspondance/Commentaire
Valeur Format Montant
Type 1
3
5
Proche
Supérieur
Inférieur
Fin proche
Fin supérieur
Fin inférieur
Le fichier doit comporter 10 modes d’arrondi soit 20 lignes au total.
Modes expédition - Paramètres société

## #CEXP — Modes expédition - Paramètres société
*Export modèle : 1 occurrence(s), 500 lignes.*

Champ Code Correspondance/Commentaire
Intitulé 35 caractères alphanumériques
Mode transport 3 caractères alphanumériques
Article frais 18 caractères alphanumériques majuscules
Type frais 0
2
4
Montant forfaitaire
Quantité
Poids net
Poids brut
Colisage
Valeur frais Format Montant si type frais égale Montant forfaitaire 
0 sinon Format prix
Type valeur frais 0
HT
TTC
Type franco 0
Montant forfaitaire
Quantité
Valeur franco Format Montant si type frais égale Montant forfaitaire 
0 sinon Format prix
Type valeur franco 0
HT
TTC
Type calcul 0
2
Valeur
Grille / Frais fixe
Grille / Frais variable
Le fichier doit comporter 50 modes d’expédition soit 500 lignes au total.
Grilles d’expédition - Paramètres société

## #CEXPGRI — Grilles d’expédition - Paramètres société
*Absent de l'export modèle — structure non vérifiée sur fichier réel.*

Champ Code Correspondance/Commentaire
Mode expédition 1 à 50

Champ Code Correspondance/Commentaire
Borne Format double
Frais Format Montant
Modes règlement - Paramètres société

## #CREG — Modes règlement - Paramètres société
*Export modèle : 1 occurrence(s), 420 lignes.*

Champ Code Correspondance/Commentaire
Intitulé 35 caractères alphanumériques
Code 3 caractères alphanumériques
Type de règlement 0
2
Aucun
Espèce
Chèque
Carte bancaire
Mode paiement débit Non utilisé en Gestion commerciale
Mode paiement crédit Non utilisé en Gestion commerciale
Code journal vente 6 caractères alphanumériques
Code journal achat 6 caractères alphanumériques
Code AFB décaissement 
principal
3 caractères numériques
Code AFB encaissement 
principal
3 caractères numériques
Abrégé RIB décaissement 5 caractères alphanumériques majuscules
Abrégé RIB encaissement 5 caractères alphanumériques majuscules
Code EDI 3 caractères alphanumériques majuscules
Paiement en ligne 0
Non
Oui

Champ Code Correspondance/Commentaire
Arrondi 0
Non
Oui
Le fichier doit comporter 30 modes de règlement soit 420 lignes au total.
Niveaux d'analyse - Paramètres société

## #CNIC — Niveaux d'analyse - Paramètres société
*Export modèle : 1 occurrence(s), 30 lignes.*

Champ Code Correspondance/Commentaire
Intitulé 35 caractères alphanumériques
Le fichier doit comporter 30 niveaux d’analyse.
Organisation Documents - Paramètres société

## #CORG — Organisation Documents - Paramètres société
*Export modèle : 1 occurrence(s), 2101 lignes.*

Champ Code Correspondance/Commentaire
Domaine 1
3
Ventes
Achats
Stocks
Type Si Domaine 1 
Ventes
Type 1
3
5
7
9
11
Devis
Bon de commande
Préparation de livraison
Bon de livraison
Bon de retour
Bon d’avoir financier
Facture
Facture de retour
Facture d’avoir
Facture comptabilisée
Réservé export
Type Si Domaine 2 
Achats

Champ Code Correspondance/Commentaire
Type 2
4
6
8
10
Préparation de commande
Bon de commande
Bon de livraison
Bon de retour
Bon d’avoir financier
Facture
Facture de retour
Facture d’avoir
Facture comptabilisée
Réservé export
Type Si Domaine 3 
Stocks
Type 1
3
5
7
Mouvement d’entrée
Mouvement de sortie
Virement de dépôt à dépôt
Dépréciation
Préparation de fabrication
Ordre de fabrication
Bon de fabrication
Validité 0
Non valide
Valide
Saisie 0
Non
Oui
Confirmé 0
Non
Oui
Souche par défaut 0 à 49 Souche sélectionnée par défaut
1er numéro de pièce 
souche 1
13 caractères alphanumériques
1er numéro de pièce 
souche 2
13 caractères alphanumériques
…
1er numéro de pièce 
souche 50
13 caractères alphanumériques
Colonnes 0
Colonne disponible pour le fichier
Colonne obligatoire pour l’application

Champ Code Correspondance/Commentaire
3
Colonne non disponible
Colonne obligatoire pour le fichier
Colonne masquée pour le fichier
Nombre d’exemplaires 
Langue Aucune
2 caractères numériques
Nombre d’exemplaires 
Langue 1
2 caractères numériques
Nombre d’exemplaires 
Langue 2
2 caractères numériques
Intitulé libellé saisie 21 caractères alphanumériques
Intitulé libellé confirmé 21 caractères alphanumériques
Intitulé libellé validé 21 caractères alphanumériques
Intitulé souche 1 à 50 
ventes/achats
35 caractères alphanumériques
Validité souche 0
Non
Oui
Code journal vente/achat 6 caractères alphanumériques
Code journal situation 
vente/achat
6 caractères alphanumériques
La structure du fichier est la suivante :
• Domaine (vente, achat, stock),
• Type de document.
Pour chaque type de document :
o Validité,
o Saisie (sauf documents des stocks),
o Confirmé (sauf documents des stocks),
o Souche par défaut (sauf documents des stocks),
o Premier numéro de pièce souche 1,
o Premier numéro de pièce souche 2 (sauf documents des stocks),
o Premier numéro de pièce souche 3 (sauf documents des stocks),
o …
o Premier numéro de pièce souche 50 (sauf documents des stocks),
o Paramétrage des colonnes du type de document sur une seule ligne,
o Nombre d’exemplaires Langue Aucune (sauf documents des stocks),
o Nombre d’exemplaires Langue 1 (sauf documents des stocks),
o Nombre d’exemplaires Langue 2 (sauf documents des stocks).

Ces 60 lignes doivent être répétées 11 fois pour les documents des ventes et 10 fois pour les 
documents des achats.
Pour les documents des stocks, ce sont 54 lignes qui doivent être répétées pour les 7 documents des 
stocks.
Les documents des stocks n’utilisant pas les souches 2 à 50, les positions correspondantes sont 
remplacées par des lignes vides.
La disposition des colonnes sera saisie sur une seule ligne. Le nombre de colonnes est de 119 en ce 
qui concerne les pièces de vente, d’achat et de stocks. Chaque colonne est représentée par un chiffre 
de 0 à 4 qui représente sa disponibilité dans la fenêtre correspondante.
Exemple
Les colonnes par défaut d’un bon de livraison client pourront être saisies de la façon suivante :
300300000430003330020000033000203000000000000024222222200000000000000000000000000
00000000000000000000000000000000000000
La codification des colonnes des pièces de vente, d’achat ou de stock doit être faite systématiquement sur 133 positions.
En fin de fichier, le programme mentionne :
• Intitulé de souche,
• Validité de la souche,
• Code journal vente/achat
• Code journal situation vente/achat
pour les domaines 1 et 2 (ventes et achats) seulement soit 400 lignes pour les 50 souches ventes et 
les 50 souches achats.
Pour les documents internes n’utilisant pas les codes journaux, les positions correspondantes sont 
remplacées par des lignes vides.
Drapeau d’en-tête #CORG.
20 groupes de 12 lignes représentant les informations suivantes :
• Domaine
• Type
• Validité
• Saisie
• Confirmé
• Souche par défaut
• Numéro de pièce souche 1
• Numéro de pièce souche 2
• Numéro de pièce souche 3
• Numéro de pièce souche 4
• Numéro de pièce souche 5
• Disposition des colonnes
• 14 groupes de 2 lignes représentant :
• Intitulé de souche
• Validité de la souche
Ce qui représente un total de 268 lignes.
Il n’y a que 14 groupes d’intitulés de souche contre 20 groupes de documents car les documents des 
stocks n’utilisent pas les souches.

Organisation Documents internes - Paramètres 
société

## #CORGINT — société
*Export modèle : 1 occurrence(s), 527 lignes.*

Champ Code Correspondance/Commentaire
Intitulé 65 caractères alphanumériques
Mouvement stock 0
2
4
Aucun
Entrée en stock
Sortie de stock
Gain financier
Perte financière
Saisie du réalisé
Validité souche 0
Non
Oui
Saisie 0
Non
Oui
Confirmé 0
Non
Oui
Souche par défaut 0 à 4 Numéro de souche
Premier n° de pièce 13 caractères alphanumériques 5 fois
Colonnes 0
2
4
Colonne disponible pour le fichier
Colonne obligatoire pour l’application
Colonne non disponible
Colonne obligatoire pour le fichier
Colonne masquée pour le fichier
Dépôt par défaut 35 caractères alphanumériques
Intitulé libellé saisie 21 caractères alphanumériques
Intitulé libellé confirmé 21 caractères alphanumériques
Intitulé libellé validé 21 caractères alphanumériques
Intitulé souche 1 à 50 
interne
35 caractères alphanumériques

Champ Code Correspondance/Commentaire
Validité souche 0
Non
Oui
La structure du fichier est la suivante :
• Intitulé
• Mouvement de stock
• Validité
• Saisie
• Confirmé
• Souche par défaut
• 1er numéro de pièce souche 1
• …
• 1er numéro de pièce souche 50
• Paramétrage des colonnes
• Dépôt par défaut
Ces 58 lignes doivent être répétées 7 fois pour les documents internes.
A chaque répétition, le numéro de pièce souche indique le numéro correspondant au type de 
document interne.
Le paramétrage des colonnes sera saisi sur une seule ligne. Le nombre de colonnes est de 133. 
Chaque colonne est représentée par un chiffre de 0 à 4 qui représente sa disponibilité dans la fenêtre 
correspondante.
Les colonnes par défaut d’un document interne de type Mouvement d’entrée en stock pourront être 
saisies de la façon suivante :
344344444422223432222244422223242222232444444422222222200000000000000000000000000
00000000000000000000000000000000000000
En fin de fichier, le programme mentionne :
• Intitulé de souche
• Validité de la souche
pour les 50 souches soit 100 lignes.
Organisation Autres fonctions - Paramètres société

## #COLO — Organisation Autres fonctions - Paramètres société / définie dans le fichier #COLR.
*Export modèle : 1 occurrence(s), 46 lignes.*

Ce fichier gère le paramétrage des colonnes des autres fonctions du programme dont on peut 
paramétrer la présence ou l’absence de certaines colonnes à l’écran.
Champ Code Correspondance/Commentaire
Colonnes 0
2
Colonne disponible pour le fichier
Colonne obligatoire pour l’application
Colonne non disponible

Champ Code Correspondance/Commentaire
4
Colonne obligatoire pour le fichier
Colonne masquée pour le fichier
La codification de masquage ou de non masquage des colonnes est la même pour tous les documents. Nous la rappelons ici pour plus de commodité.
Voir l’exemple donné sous le titre précédent.
Le tableau suivant précise d’une part le nombre de colonnes utilisées par chaque fonction du 
programme et d’autre part l’ordre dans lequel les lignes doivent apparaître dans le fichier #COLO.
Champ Code Correspondance/Commentaire
Colonnage tiers 142 colonnes
Colonnage Interro commerciale article 142 colonnes
Colonnage Interrogation stock article 24 colonnes
Colonnage Interrogation tarifs article 19 colonnes
Colonnage Réapprovisionnement 24 colonnes
Colonnage abonnements clients 133 colonnes
Colonnage abonnements fournisseurs 133 colonnes
Génération commande fournisseurs Contremarque 19 colonnes
Affectation livraisons fournisseurs Contremarque 22 colonnes
Régularisation d’inventaire 25 colonnes
Recherche de documents En-tête 110 colonnes
Recherche lignes 136 colonnes
Affaires 142 colonnes
Liste mouvements caisse 20 colonnes
Liste des documents 11 colonnes
Liste détaillée des mouvements 34 colonnes

Champ Code Correspondance/Commentaire
Liste des tickets archivés 12 colonnes
Remise en banque 15 colonnes
Liste des commandes à livrer 103 colonnes
Détail des commandes à livrer 117 colonnes
Liste des articles des commandes 120 colonnes
Validation unitaire des préparations 121 colonnes
Validation globale des préparations 124 colonnes
Interrogation stock nomenclatures 29 colonnes
Interrogation commerciale nomenclatures 142 colonnes
Interrogation tarifs nomenclatures 19 colonnes
Interrogation charges ressource 8 colonnes
Interrogation document affaire 85 colonnes
Interrogation commerciale représentant 142 colonnes
Interrogation liste documents représentants 85 colonnes
Colonnage abonnement interne 133 colonnes
Colonnage traçabilité documents 43 colonnes
Colonnage Projets fabrication : origine 88 colonnes
Colonnage Projets fabrication : planning 14 colonnes
Colonnage Projets fabrication : suivi 15 colonnes
Colonnage Projets fabrication : historique 10 colonnes
Projets fabrication : Numéro 9 caractères alphanumériques majuscules

Champ Code Correspondance/Commentaire
Colonnage Saisie d'avancement 21 colonnes
Interrogation compte ressource 142 colonnes
Colonnage Projets affaire : origine 88 colonnes
Colonnage Projets affaire : planning 14 colonnes
Colonnage Projets affaire : suivi 15 colonnes
Colonnage Projet affaire : historique 10 colonnes
Projets d’affaire : Numéro 9 caractères alphanumériques majuscules
Colonnage facturation affaire : liste 96 colonnes
Colonnage facturation affaire : détail 108 colonnes
L’organisation des colonnes des règlements est 
définie dans le fichier #COLR.

Champ Code Correspondance/Commentaire
Interrogation tiers 
commerciale
Zone non gérée : 1 ligne de 125 caractères 
numériques (1)
Interrogation tiers comptable Zone non gérée : 1 ligne de 62 caractères numériques (1)
Interrogation stock article Zone non gérée : 1 ligne de 24 caractères numériques (1)
Interrogation tarifs article Zone non gérée : 1 ligne de 19 caractères numériques (1)
Interrogation commerciale 
article
Zone non gérée : 1 ligne de 125 caractères 
numériques (1)

Champ Code Correspondance/Commentaire
Interrogation commerciale 
affaires
Zone non gérée : 1 ligne de 62 caractères numériques (1)
Interrogation comptable 
affaires
Zone non gérée : 1 ligne de 47 caractères numériques (1)
Réapprovisionnement Zone non gérée : 1 ligne de 20 caractères numériques (1)
Génération commande 
fournisseurs Contremarque
Zone non gérée : 1 ligne de 19 caractères numériques (1)
Affectation livraisons 
fournisseurs Contremarque
Zone non gérée : 1 ligne de 22 caractères numériques (1)
Abonnements clients Zone non gérée : 1 ligne de 120 caractères 
numériques (1)
Abonnements fournisseurs Zone non gérée : 1 ligne de 120 caractères 
numériques (1)
Génération commande 
fournisseurs Contremarque
Zone non gérée : 1 ligne de 19 caractères numériques (2)
Affectation livraisons 
fournisseurs Contremarque
Zone non gérée : 1 ligne de 22 caractères numériques (3)
Régularisation d’inventaire 17 colonnes (2)
Recherche de documents EntêteZone non gérée : 1 ligne de 105 caractères 
numériques (1)
Recherche de documents 
Lignes
Zone non gérée : 1 ligne de 120 caractères 
numériques (1)
Réception fournisseur Zone non gérée : 1 ligne de 119 caractères 
numériques (1)
Liste mouvements caisse Zone non gérée : 1 ligne de 20 caractères numériques (1)
Liste des documents Zone non gérée : 1 ligne de 11 caractères numériques (1)

Champ Code Correspondance/Commentaire
Liste détaillée des 
mouvements
Zone non gérée : 1 ligne de 31 caractères numériques (1)
Liste des tickets archivés Zone non gérée : 1 ligne de 119 caractères 
numériques (1)
Remise en banque Zone non gérée : 1 ligne de 119 caractères 
numériques (1)
Commandes en attente Zone non gérée : 1 ligne de 9 caractères 
numériques (1)
Liste des commandes à livrer Zone non gérée : 1 ligne de 103 caractères 
numériques (1)
Détail des commandes à livrer Zone non gérée : 1 ligne de 111 caractères 
numériques (1)
Liste des articles des 
commandes
Zone non gérée : 1 ligne de 114 caractères 
numériques (1)
Validation unitaire des 
préparations
Zone non gérée : 1 ligne de 115 caractères 
numériques (1)
Validation globale des 
préparations
Zone non gérée : 1 ligne de 118 caractères 
numériques (1)
Interrogation stock 
nomenclatures
Zone non gérée : 1 ligne de 29 caractères numériques (1)
Interrogation commerciale 
nomenclatures
Zone non gérée : 1 ligne de 125 caractères 
numériques (1)
Interrogation tarifs 
nomenclatures
Zone non gérée : 1 ligne de 19 caractères numériques (1)
Interrogation charges 
ressource
Zone non gérée : 1 ligne de 8 caractères 
numériques (1)
Interrogation document affaire Zone non gérée : 1 ligne de 81 caractères numériques (1)
Interrogation commerciale 
représentant
Zone non gérée : 1 ligne de 125 caractères 
numériques (1)

Champ Code Correspondance/Commentaire
Interrogation liste documents 
représentants
Zone non gérée : 1 ligne de 81 caractères numériques (1)
Abonnements internes Zone non gérée, 1 ligne de 120 caractères 
numériques (1)
(1) Les chiffres doivent être compris entre 0 et 4.
(2) Les chiffres doivent être compris entre 0 et 4.
(3) Les chiffres doivent être compris entre 0 et 4.
Nous indiquons également, par fonction, le nombre de colonnes maximum qu’elles peuvent 
comporter. Cette valeur devra correspondre au nombre de codes enregistrés sur la ligne correspondant à la fonction pour indiquer la disponibilité des colonnes.
Le paramétrage des colonnes par défaut de la régularisation d’inventaire pourra être paramétré de la 
façon suivante : 14443314333331431
Ce qui représente bien 17 colonnes.
Rappelons que les colonnes disponibles pour chaque fonction sont détaillées dans la fonction 
Colonnage des Paramètres société.
Règlements – Paramètres société

## #COLR — Règlements – Paramètres société
*Export modèle : 1 occurrence(s), 5 lignes.*

Champ Code Correspondance/Commentaire
Numérotation ventes 0
Automatique
Manuelle
Numéro en cours ventes 13 caractères alphanumériques majuscules
Numérotation achats 0
Automatique
Manuelle
Numéro en cours achats 13 caractères alphanumériques majuscules
Règlements 27 colonnes
Le paramétrage des colonnes doit être réalisé selon les informations données plus haut.
Pays - Paramètres société

## #CPAI — Pays - Paramètres société
*Export modèle : 15 occurrence(s), 8 lignes.*

Champ Code Correspondance/Commentaire
Intitulé 35 caractères alphanumériques
Code pays 3 caractères alphanumériques
Code DEI 3 caractères alphanumériques
Coef. assurance Format Double
Coef. transport Format Double
Code ISO2 2 caractères alphanumériques
SEPA 0
Non
Oui
Localisation 0
2
4
Union Européenne
France
Hors Union Européenne
DROM
COM
Le nombre de pays est illimité. Le drapeau d’en-tête doit être rappelé avant chaque nouveau pays et 
les champs qui lui correspondent.
Périodicités - Paramètres société

## #CPER — Périodicités - Paramètres société
*Export modèle : 1 occurrence(s), 10 lignes.*

Champ Code Correspondance/Commentaire
Intitulé 35 caractères alphanumériques
Il est possible d’importer jusqu’à 10 périodicités.
Plans analytiques - Paramètres société

## #CANA — Plans analytiques - Paramètres société
*Export modèle : 1 occurrence(s), 253 lignes.*

Champ Code Correspondance/Commentaire
Intitulé 35 caractères alphanumériques
Section analytique 
d’attente
13 caractères alphanumériques majuscules (vide si 
aucune section d’attente)
Gestion en colonne 0
Non
Oui
Type d’imputation 0
2
Aucune
Les comptes de charge et produit
Tous les comptes
Obligatoire 0
Non
Oui
Intitulé rupture analytique 21 caractères alphanumériques
Longueur rupture 
analytique
6 * 3 caractères alphanumériques. La longueur 
totale doit être inférieure ou égale à 113.
Type rupture analytique 0
2
Aucun
Zone géographique
Secteur d’activité
Les trois dernières lignes sont répétées 6 fois pour chaque plan analytique importé. Le fichier doit 
comporter 11 plans analytiques soit 242 lignes au total. La somme des 6 longueurs de chaque rupture 
pour un plan analytique donné doit être inférieure ou égale à 13.
Enumérés analytiques - Paramètres société

## #CENA — Enumérés analytiques - Paramètres société
*Export modèle : 6 occurrence(s), 4 lignes.*

Champ Code Correspondance/Commentaire
Numéro du plan analytique 1 à 10
Numéro de rupture 1 à 6
Particule du numéro 1 à 13 caractères alphanumériques
Intitulé du particule 21 caractères alphanumériques

Résiliations abonnements - Paramètres société

## #CRES — Résiliations abonnements - Paramètres société
*Export modèle : 1 occurrence(s), 30 lignes.*

Champ Code Correspondance/Commentaire
Intitulé 35 caractères alphanumériques
Le fichier doit comporter 30 intitulés de résiliation d’abonnement.
Service contact - Paramètres société

## #MSCT — Service contact - Paramètres société
*Export modèle : 1 occurrence(s), 60 lignes.*

Champ Code Correspondance/Commentaire
Intitulé 35 caractères alphanumériques
Abrégé 3 caractères alphanumériques majuscules
Il est possible de créer jusqu’à 30 services contacts. Les zones inutilisées doivent être remplacées par 
des lignes vides.
Comptoir (Saisie de caisse décentralisée) Caisse -
Ecran de saisie – Paramètres société
En arrêt de maintenance depuis le 31/05/2023. Ces informations concernent uniquement les versions 
9.00 et antérieures.

## #CCPT — 9.00 et antérieures.
*Export modèle : 1 occurrence(s), 790 lignes.*

Champ Code Correspondance/Commentaire
Intitulé 35 caractères alphanumériques
Modèle 0
2
Modèle écran 1
Modèle écran 2
Modèle écran 3
Modèle écran 4
Affichage 37 colonnes *

Champ Code Correspondance/Commentaire
Colonnes 93 colonnes *
Type document par défaut 0
2
4
6
8
Ticket
Devis
Bon de commande
Préparation de livraison
Bon de livraison
Bon de retour
Bon d’avoir financier
Facture
Facture de retour
Facture d’avoir
Texte bouton 14 caractères alphanumériques
Fonction bouton 0
2
4
6
8
10
12
14
16
18
20
Créer un document
Fin de saisie
Valider
Annuler
Changement de tarif
Liste des vendeurs
Liste des devises
Liste des modes de règlement
Liste des raccourcis clavier
Multi-règlement
Impression facture
Impression ticket
Supprimer un règlement
Supprimer la dernière ligne saisie
Modifier une ligne
Liste des clients
Mise en attente
Devise à rendre
Rappel ticket
Acomptes
Appliquer les barèmes

Champ Code Correspondance/Commentaire
22
24
26
28
30
32
34
36
38
40
42
44
46
48
Créer un ticket
Créer un devis
Créer un bon de commande
Créer une préparation de livraison
Créer un bon de livraison
Créer un bon d’avoir financier
Créer un bon de retour
Créer une facture
Créer une facture d’avoir
Créer une facture de retour
Envoyer le document par e-mail
Imprimer document
Informations libres
Informations sur le document
Intégrer un document
Imputer un règlement existant
Saisir un mouvement de caisse
Saisir un règlement
Solvabilité
Transformer
Valorisation TTC
Echéancier
Liste des dépôts
Liste des documents
Liste des tickets
Imputer un bon d’achat
Comptabiliser le document
Liste des centrales d’achat
Les 2 dernières lignes apparaissent 37 fois.
Il est possible d’avoir jusqu’à 10 intitulés Comptoir
*Ce fichier gère le paramétrage des colonnes des autres fonctions du programme dont on peut 
paramétrer la présence ou l’absence de certaines colonnes à l’écran.

Champ Code Correspondance/Commentaire
Colonnes 0
2
4
Colonne disponible pour le fichier
Colonne obligatoire pour l’application
Colonne non disponible
Colonne obligatoire pour le fichier
Colonne masquée pour le fichier
Clavier (Saisie de caisse décentralisée) 
Périphériques de caisse – Clavier
En arrêt de maintenance depuis le 31/05/2023. Ces informations concernent uniquement les versions 
9.00 et antérieures.

## #CCLA — 9.00 et antérieures.
*Export modèle : 1 occurrence(s), 10 lignes.*

Champ Code Correspondance/Commentaire
Intitulé 35 caractères alphanumériques
Il est possible d’avoir jusqu’à 10 intitulés Clavier
Structure banque - Paramètres société

## #CSBQ — Structure banque - Paramètres société
*Export modèle : 1 occurrence(s), 40 lignes.*

Champ Code Correspondance/Commentaire
Structure EDI 0
Non
Oui
Longueur code banque 0 à 14
Type code banque 0
Numérique
Alphanumérique
Longueur code guichet 0 à 17
Type code guichet 0
Numérique
Alphanumérique
Longueur compte 0 à 17

Champ Code Correspondance/Commentaire
Type compte 0
Numérique
Alphanumérique
Longueur clé 0 à 2
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
Type contact

## #MTCO — Type contact
*Export modèle : 1 occurrence(s), 30 lignes.*

Champ Code Correspondance/Commentaire
Intitulé 35 caractères alphanumériques
Types de tiers - Paramètres société

## #CTTI — Types de tiers - Paramètres société
*Export modèle : 1 occurrence(s), 136 lignes.*

Champ Code Correspondance/Commentaire
Compte principal 1 à 10 Position du compte principal
Type numérotation 0
2
Manuelle
Automatique
Manuelle avec racine
Longueur 17 caractères alphanumériques
Racine 17 caractères alphanumériques majuscules
Intitulé 17 caractères alphanumériques

Champ Code Correspondance/Commentaire
Type compte 0
Radical
Compte
Compte Format Compte
La structure de ce fichier est la suivante :
• une ligne pour le Compte principal
• une ligne pour le Type numérotation
• une ligne pour la Longueur
• une ligne pour la Racine et
• un bloc de trois lignes répété 10 fois :
• Intitulé
• Type compte
• Compte
Ces 34 lignes sont répétées pour chacun des 4 types de tiers existants (Client, Fournisseur, Salarié et 
Autres) soit 136 lignes.
Le programme ne gère que les clients et les fournisseurs mais la totalité du fichier doit être importée.
La ligne Compte principal indique la position du compte paramétré comme principal dans le bloc de 30 
lignes concernant l’ Intitulé , le Type de compte et le Compte .
La structure de ce fichier est la suivante :
• Drapeau d’en-tête #CTTI
• 4 lignes représentant la position du compte Principal dans la liste des tiers. Chacune de ces 
lignes est suivie de 10 groupes de 3 lignes représentant les informations suivantes :
• Intitulé du type de tiers
• Type de compte (code 0 ou 1)
• Compte
Soit un total de 125 lignes.
Les types de tiers se suivent systématiquement dans l’ordre :
• Clients
• Fournisseurs
• Salariés
• Autres
Le programme ne permet de paramétrer que les types de tiers Client et Fournisseur.
Unités achat / vente - Paramètres société

## #CUAV — Unités achat / vente - Paramètres société
*Export modèle : 1 occurrence(s), 150 lignes.*

Champ Code Correspondance/Commentaire
Intitulé 21 caractères alphanumériques

Champ Code Correspondance/Commentaire
Correspondance 0
Non
Oui
Nombre unité 3 chiffres maximum (0 à 999)
Unité temps 0
2
4
6
Minute
Heure
Jour
Mois
Trimestre
Semestre
Année
Code EDI 3 caractères alphanumériques
Le fichier doit comporter 30 intitulés d’unités d’achat et de vente.
Echanges électroniques

## #CECH — Echanges électroniques
*Export modèle : 1 occurrence(s), 12 lignes.*

Champ Code Correspondance/Commentaire
Sous-traiter l’envoi des 
factures
1
Non
Oui
Sous-traiter l’envoi des 
commandes
1
Non
Oui
Taux remise Format double
Article remise 18 caractères Majuscules
Le couple Taux et Article apparaît 5 fois.
Echanges électroniques comptables

## #MECE — Echanges électroniques comptables
*Export modèle : 1 occurrence(s), 9 lignes.*

Champ Code Correspondance/Commentaire
Type code EDI
1
GLN
DUNS
Autre
Code EDI 23 caractères alphanumériques
Identifiant EDI Sage 8 caractères numériques
Nom contact dossier 35 caractères alphanumériques
Prénom contact dossier 35 caractères alphanumériques
Code journal
6 caractères alphanumériques
Visible dans la comptabilité
Type autre identifiant
1
3
5
Aucun
Union Européenne Hors France
Hors Union Européenne
RIDET
TAHITI
Particulier
Autre
Valeur autre identifiant 80 caractères alphanumériques
Option traitement factures
5
2
Non géré (valeur par défaut)
Tester l’émission et la réception des factures 
(phase pilote)
Tester l’émission et la réception des factures
Emettre des factures vers les entités publiques 
uniquement
Recevoir des factures électroniques

Champ Code Correspondance/Commentaire
4 Emettre et recevoir des factures électroniques
Bon à payer

## #MBAP — Bon à payer
*Export modèle : 1 occurrence(s), 5 lignes.*

Champ Code Correspondance/Commentaire
Autorisation 0
2
Aucun
Responsable financier uniquement
Acheteur et responsable financier
Nom collaborateur 35 caractères alphanumériques
Prénom collaborateur 35 caractères alphanumérique
Facture à valider 0
Toutes les factures
Selon montant
Seuil Format montant
Contacts dossier

## #MCTD — Contacts dossier
*Export modèle : 1 occurrence(s), 19 lignes.*

Champ Code Correspondance/Commentaire
Nom 35 caractères alphanumériques
Prénom 35 caractères alphanumériques
Service 1 à 30 Position dans la liste des services (paramètres 
société)
Fonction 35 caractères alphanumériques
Téléphone 21 caractères alphanumériques

Champ Code Correspondance/Commentaire
Portable 21 caractères alphanumériques
Télécopie 21 caractères alphanumériques
E-mail 69 caractères alphanumériques
Civilité 0
2
M.
Mme
Mlle
Contact 1 à 30 Correspond au n° d'index des types de contact (1)
Adresse 35 caractères alphanumériques
Complément 35 caractères alphanumériques
Code postal 9 caractères alphanumériques
Ville 35 caractères alphanumériques
Région 25 caractères alphanumériques
Pays 35 caractères alphanumériques
Compte Facebook 35 caractères alphanumériques
Compte LinkedIn 35 caractères alphanumériques
Compte Skype 35 caractères alphanumériques
(1) Voir Type contact.
Il est possible de créer un nombre illimité de contacts dossier. Les quatorze lignes doivent être 
répétées pour chaque dossier.
Enuméré information libre
Ce fichier n’est utilisé que pour les informations libres de type Table.

## #CEIN — Ce fichier n’est utilisé que pour les informations libres de type Table.
*Export modèle : 3 occurrence(s), 3 lignes.*

Champ Code Correspondance/Commentaire
Numéro de fichier 0
2
4
6
Articles
Comptes généraux
Sections analytiques
Clients/Fournisseurs
En-têtes des documents
Lignes de document
Numéro série/lot
Ressources
Numéro d’information libre Numéro d’ordre de l’information libre de type Table
Intitulé 35 caractères alphanumériques
Codification automatique

## #CGEN — Codification automatique
*Export modèle : 1 occurrence(s), 44 lignes.*

Champ Code Correspondance/Commentaire
Numérotation article 0
Manuelle
Automatique
Longueur article 2 caractères numériques
Type racine article 0
Racine fixe
Racine famille
Racine article 18 caractères alphanumériques majuscules
Numérotation gamme 0
Non
Oui
Incrémentation gamme 0
Non
Oui
Longueur gamme 2 caractères numériques
Type racine gamme 0
2
Aucune
Racine fixe
Racine famille
Racine article

Champ Code Correspondance/Commentaire
Longueur racine gamme 2 caractères numériques
Racine gamme 18 caractères alphanumériques majuscules
Complément gamme 0
Aucun
Intitulé énuméré
Longueur complément 
gamme
2 caractères numériques
Numérotation 
conditionnement
1
Manuelle
Automatique
Incrémentation 
conditionnement
1
Non
Oui
Longueur conditionnement 2 caractères numériques
Type racine 
conditionnement
1
3
Aucune
Racine fixe
Racine famille
Racine article
Longueur racine 
conditionnement
2 caractères numériques
Racine conditionnement 18 caractères alphanumériques majuscules
Complément 
conditionnement
1
Aucun
Intitulé énuméré
Qté conditionnement
Longueur complément 
conditionnement
2 caractères numériques
Numérotation code-barres
article
1
Manuelle
Automatique
Norme code-barres article 0
2
4
Aucune
C39
EAN8
EAN13
EAN128

Champ Code Correspondance/Commentaire
Longueur code-barres
article
2 caractères numériques
Type racine code-barres
article
1
Racine fixe
Racine code-barres famille
Référence article
Longueur racine codebarres article2 caractères numériques
Racine code-barres article 18 caractères alphanumériques majuscules
Numérotation code-barres
gamme
1
Manuelle
Automatique
Incrémentation code-barres
gamme
1
Non
Oui
Norme code-barres gamme 0
2
4
Aucune
C39
EAN8
EAN13
EAN128
Longueur code-barres
gamme
2 caractères numériques
Type racine code-barres
gamme
1
3
Aucune
Racine fixe
Racine famille
Racine article
Longueur racine codebarres gamme2 caractères numériques
Racine code-barres
gamme
18 caractères alphanumériques majuscules
Complément code-barres
gamme
1
Aucun
Intitulé énuméré
Longueur complément 
code-barres gamme
2 caractères numériques

Champ Code Correspondance/Commentaire
Numérotation code-barres
conditionnement
1
Manuelle
Automatique
Incrémentation code-barres
conditionnement
1
Non
Oui
Norme code-barres
conditionnement
1
3
Aucune
C39
EAN8
EAN13
EAN128
Longueur code-barres
conditionnement
2 caractères numériques
Type racine code-barres
conditionnement
1
3
Aucune
Racine fixe
Racine famille
Racine article
Longueur racine codebarres conditionnement2 caractères numériques
Racine code-barres
conditionnement
18 caractères alphanumériques majuscules
Complément code-barres
conditionnement
1
Aucun
Intitulé énuméré
Qté conditionnement
Longueur complément 
code-barres
conditionnement
2 caractères numériques
Calendrier

## #MCAL — Calendrier
*Export modèle : 2 occurrence(s), 53 lignes.*

Champ Code Correspondance/Commentaire
Intitulé 35 caractères alphanumériques

Champ Code Correspondance/Commentaire
Numéro Nombre entier
Premier jour de la semaine
5
Lundi
Samedi
Dimanche
Première semaine de 
l'année
1
Commence le 1er janvier
Première semaine de 4 jours
Première semaine entière
Jours ouvrés
1
Non
Oui
Répété 7 fois : une fois / jour
Plage matin + Plage soir Format heure (7 fois)
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
Date jour exception Format date (n fois)
Motif jour exception 35 caractères alphanumériques
Les 2 dernières lignes apparaissent n fois
Fiche - Familles d’articles

## #CFAM — Fiche - Familles d’articles
*Export modèle : 19 occurrence(s), 42 lignes.*

Champ Code Correspondance/Commentaire
Code famille 10 caractères alphanumériques majuscules
Type 1
3
Détail
Total
Centralisateur
Intitulé 69 caractères alphanumériques
Unité de vente 1 à 30 Numéro de l’unité de vente/achat
Coefficient Format Double
Suivi stock 0
2
4
Aucun
Sérialisé
CMUP
FIFO
LIFO
Par lot
Garantie 4 caractères numériques
Pays origine 35 caractères alphanumériques
Code fiscal 25 caractères alphanumériques
Famille centralisatrice 10 caractères alphanumériques
Enuméré statistique 1 21 caractères alphanumériques
Enuméré statistique 2 21 caractères alphanumériques
Enuméré statistique 3 21 caractères alphanumériques
Enuméré statistique 4 21 caractères alphanumériques
Enuméré statistique 5 21 caractères alphanumériques
Unité de poids 1
3
5
Tonne
Quintal
Kilogramme
Gramme
Milligramme

Champ Code Correspondance/Commentaire
Hors statistiques 0
Non
Oui
Vente au débit 0
Non
Oui
Non impression 0
Non
Oui
Non soumis à l’escompte 0
Non
Oui
Délai livraison 0 à 999
Intitulé frais 1 21 caractères alphanumériques
Frais 1 Format double
Intitulé frais 2 21 caractères alphanumériques
Frais 2 Format double
Intitulé frais 3 21 caractères alphanumériques
Frais 3 Format double
Contremarque 0
Non
Oui
Facturation sur le poids 0
Non
Oui
Facturation forfaitaire 0
Non
Oui
Publié sur le site marchand 0
Non
Oui
Racine référence 18 caractères alphanumériques majuscules
Racine code barre 18 caractères alphanumériques majuscules
Enuméré catalogue 1 35 caractères alphanumériques

Champ Code Correspondance/Commentaire
Enuméré catalogue 2 35 caractères alphanumériques
Enuméré catalogue 3 35 caractères alphanumériques
Enuméré catalogue 4 35 caractères alphanumériques
Nature 0 à 3
Nombre de colis 0 à 999
Réserver à la soustraitance0 à 1
Gérer en tant que fictif 0 à 1
Niveau de criticité 0 à 2
Les champs Frais doivent préciser le type de la remise en mentionnant le symbole %, F, U ou 
l’opérateur + dans le cas de remise en cascade.
Comptabilité - Familles d’articles

## #CFAC — Comptabilité - Familles d’articles
*Export modèle : 13 occurrence(s), lignes 0, 84, 98.*

Champ Code Correspondance/Commentaire
Type 1
3
Ventes
Achats
Stocks
Catégorie comptable 1 à 50 Numéro de catégorie comptable
Compte général Format Compte
Section analytique Format Section analytique
Compte taxe 1 5 caractères alphanumériques majuscules
Compte taxe 2 5 caractères alphanumériques majuscules
Compte taxe 3 5 caractères alphanumériques majuscules

Champ Code Correspondance/Commentaire
Type facture 1 à 3 Mettre 1 : Facture (particularité pour version
étrangère)
Date application 1 Date
Date application 2 Date
Date application 3 Date
Ancien code taxe 1 5 caractères alphanumériques majuscules
Ancien code taxe 2 5 caractères alphanumériques majuscules
Ancien code taxe 3 5 caractères alphanumériques majuscules
Ces lignes doivent être répétées pour toutes les catégories comptables existantes (maximum 30 fois). 
Les catégories comptables des familles ne pourront pas être importées séparément, elles devront 
toujours être précédées de la famille #CFAM à laquelle elles se rapportent.
Références fournisseurs - Familles d’articles

## #CFFR — Références fournisseurs - Familles d’articles
*Export modèle : 8 occurrence(s), 13 lignes.*

Champ Code Correspondance/Commentaire
Numéro fournisseur 17 caractères alphanumériques majuscules
Unité achat/vente 1 à 30 Numéro d’unité vente/achat
Remise Format double
Conversion Format Double
Délai d’approvisionnement 4 caractères numériques
Garantie 4 caractères numériques
Colisage Format Quantité
Q.E.C. Format Quantité

Champ Code Correspondance/Commentaire
Gamme remise Qté/Mont. 0
1 à 50
Pas de gamme remise quantité/montant
N° de la gamme
Principal 0
Non principal
Principal
Devise 0
1 à 32
Aucune
N° de la devise
Type remise 0
Remise
Hors remise
Diviseur conversion 1 Zone réservée pour une version ultérieure
Les références fournisseurs ne sont pas obligatoires s’il n’y a pas de fournisseur pour la famille.
Ce fichier peut être suivi d’un #CATG (Tarif par énuméré de gamme) ou d’un #CFTQ (Famille Tarif 
quantité).
Tarifs par quantités - Familles d’articles

## #CFTQ — Tarifs par quantités - Familles d’articles
*Absent de l'export modèle — structure non vérifiée sur fichier réel.*

Champ Code Correspondance/Commentaire
Type tarif 0
Remise par quantité
Remise par montant
Borne supérieure Format Quantité si Type = 0
Format Montant si Type = 1
Remise 45 caractères alphanumériques
Cette dernière valeur doit préciser le type de la remise en mentionnant le symbole % , F , U ou 
l’opérateur + dans le cas de remises en cascade. Voir la fonction Articles pour des informations 
complémentaires.
Les tarifs sont facultatifs.
Ce fichier peut apparaître à la suite d’un fichier #CFFR (Référence fournisseur par famille) ou d’un 
fichier #CFCL (Famille Catégorie tarifaire)
Catégories tarifaires - Familles d’articles

## #CFCL — Catégories tarifaires - Familles d’articles
*Export modèle : 7 occurrence(s), 9 lignes.*

Champ Code Correspondance/Commentaire
Catégorie tarifaire 1 à 32 Numéro de catégorie tarifaire
Coefficient Format Double
Remise Format Double
Mode arrondi 0
1 à 10
Aucun
N° de l’arrondi
Gamme remise Qté/Mont. 0
1 à 50
Pas de gamme remise quantité/montant
N° de la gamme
Type prix de vente 0
HT
TTC
Devise 0
1 à 32
Aucun
N° de la devise
Calcul PV/PR 0
Oui
Non
Type remise 0
Remise
Hors remise
Ce fichier peut être suivi d’un #CFTQ (Famille Tarif quantité).
Remises par client - Familles d’articles

## #CFRC — Remises par client - Familles d’articles
*Export modèle : 7 occurrence(s), 2 lignes.*

Champ Code Correspondance/Commentaire
N° de client 17 caractères alphanumériques
Remise Format Double
Modèle d’enregistrement - Familles d’articles

## #CFMO — Modèle d’enregistrement - Familles d’articles
*Absent de l'export modèle — structure non vérifiée sur fichier réel.*

Champ Code Correspondance/Commentaire
Intitulé modèle 35 caractères alphanumériques
Type 0
2
4
Tous les domaines
Ventes
Achats
Stocks
Ventes comptoir
Fiches Articles

## #CART — Fiches Articles
*Export modèle : 71 occurrence(s), lignes 76, 82, 86.*

Champ Code Correspondance/Commentaire
Référence 18 caractères alphanumériques majuscules 
(obligatoire)
Désignation 69 caractères alphanumériques (obligatoire)
Code famille 10 caractères alphanumériques majuscules 
(obligatoire)
Substitution 18 caractères alphanumériques majuscules
Raccourci 6 caractères alphanumériques majuscules
Garantie 4 caractères numériques
Unité de poids
2
4
Tonne
Quintal
Kilogramme
Gramme
Milligramme
Poids net Format Quantité

Champ Code Correspondance/Commentaire
Poids brut Format Quantité
Unité de vente 1 à 30 Numéro de l’unité de vente/achat
Prix d’achat Format Prix
Coefficient Format Double
Prix de vente Format Prix
Gamme 1 0
1 à 50
Pas de gamme produit
Numéro de la gamme produit
Gamme 2 0
1 à 50
Pas de gamme produit
Numéro de la gamme produit
Conditionnement 0
1 à 20
Pas de conditionnement
Numéro du conditionnement
Nomenclature
1
3
Aucune
Fabrication
Commerciale composé
Commerciale composant
Articles liés
Suivi stock
1
3
5
Aucun
Sérialisé
CMUP
FIFO
LIFO
Par lot
Enuméré statistique 1 à 5 21 caractères alphanumériques
Type prix de vente 0
HT
TTC

Champ Code Correspondance/Commentaire
Hors statistiques 0
Non
Oui
Vente au débit 0
Non
Oui
Non impression 0
Non
Oui
Mise en sommeil 0
Non
Oui
Non soumis à l’escompte 0
Non
Oui
Délai livraison 0 - 999
Langue 1 69 caractères alphanumériques
Langue 2 69 caractères alphanumériques
Code EDI 1 44 caractères alphanumériques
Code-barres 18 caractères alphanumériques
Code fiscal 25 caractères alphanumériques
Pays origine 35 caractères alphanumériques
Intitulé frais 1 21 caractères alphanumériques
Frais 1 45 caractères alphanumériques

Champ Code Correspondance/Commentaire
Intitulé frais 2 21 caractères alphanumériques
Frais 2 45 caractères alphanumériques
Intitulé frais 3 21 caractères alphanumériques
Frais 3 45 caractères alphanumériques
Contremarque 0
Non
Oui
Facturation sur le poids 0
Non
Oui
Facturation forfaitaire 0
Non
Oui
Saisie variable 0
Non
Oui
Date de création Format Date
Date modification Format Date
Publié sur le site 
marchand
1
Non
Oui
Dernier prix d’achat Format Prix
Date application tarif Format Date
Nouveau prix d’achat Format Prix

Champ Code Correspondance/Commentaire
Nouveau coefficient Format Double
Nouveau prix de vente Format Prix
Coût standard Format Montant
Quantité composant Format Quantité
Quantité économique Format Quantité
Conditionnement par 
défaut 35 caractères alphanumériques
Réappro / prévision 0
Non
Oui
Enuméré catalogue 1 35 caractères alphanumériques
Enuméré catalogue 2 35 caractères alphanumériques
Enuméré catalogue 3 35 caractères alphanumériques
Enuméré catalogue 4 35 caractères alphanumériques
Type article
1
3
Standard
Gamme
Ressource multiple
Ressource unitaire
Nature (GPAO)
1
3
Composant
Pièce détachée
Produit fini
Produit semi-fini
Non gérée

Champ Code Correspondance/Commentaire
Délai de fabrication 0 à 999
Nombre de colis 0 à 9999 0..9999
Délai de péremption 0 à 999 0..999
Délai de sécurité 0 à 999 0..999
Gérer en tant que fictif 0
Non
Oui
Réserver à la soustraitance0
Non
Oui
Type de lancement 0
Standard
Spécifique
Cycle de vie
1
Lancement
Maturité
Déclin
Niveau de criticité
1
Mineur
Majeur
Critique
Interdire les commandes 0
Non
Oui
Exclure du 
réapprovisionnement
1
Non
Oui
Enuméré gamme 35 caractères alphanumériques

Champ Code Correspondance/Commentaire
Type de gamme 0
Gamme 1
Gamme 2
Les critères Enuméré gamme et Type gamme doivent être répétés autant de fois que nécessaire. Ils 
ne peuvent être enregistrés que si Gamme différent de 0.
Si Nomenclature différent de0, une entrée d’article doit être suivie d’une liste nomenclature (#CANO).
Si Nomenclature = 1, une entrée d’article doit être suivie d’une liste gamme opératoire (#CAOP). Les 
éléments seront importés dans l’ordre de la liste.
Informations libres élémentsArticles/nomenclatures

## #CIVA — Informations libres élémentsArticles/nomenclatures
*Export modèle : 63 occurrence(s), lignes 2, 3, 4, 8.*

Champ Code Correspondance/Commentaire
Information libre 1 à 64 69 caractères alphanumériques
Les informations figurant dans ce fichier doivent respecter le paramétrage effectué dans l’option 
correspondante. Il doit figurer autant de lignes d’informations libres que paramétrées dans l’option 
correspondante. Ce fichier doit être importé immédiatement après le #CART auquel il se rapporte.
Ce fichier peut suivre également un #CART, #CCLI, #CFOU, #CHEN, #CHLI ou #CRESPROD.
Dans le cas d’informations libres de type Valeur calculée , l’intitulé de l’information libre est suivi d’une 
barre oblique (/) et de la formule de calcul associée.
Liste nomenclatures - Articles

## #CANO — Liste nomenclatures - Articles
*Export modèle : 27 occurrence(s), 12 lignes.*

Champ Code Correspondance/Commentaire
Référence article 18 caractères alphanumériques
Quantité Format Quantité
Enuméré gamme 1 21 caractères alphanumériques

Champ Code Correspondance/Commentaire
Enuméré gamme 2 21 caractères alphanumériques
Type composants 0
Fixe
Variable
Répartition 14 caractères numériques
Opération 10 caractères alphanumériques
Commentaire 69 caractères alphanumériques
Dépôt de sortie 35 caractères alphanumériques
Enuméré gamme 
composé 1 21 caractères alphanumériques
Enuméré gamme 
composé 2 21 caractères alphanumériques
Sous-traitance 0
Non
Oui
Conditionnements - Articles

## #CACO — Conditionnements - Articles
*Export modèle : 6 occurrence(s), 6 lignes.*

Champ Code Correspondance/Commentaire
Intitulé conditionnement 35 caractères alphanumériques
Quantité conditionnée Format Quantité
Référence énuméré 18 caractères alphanumériques

Champ Code Correspondance/Commentaire
Code-barres énuméré 18 caractères alphanumériques majuscules
Principal 0
Non
Oui
Code EDI 3 caractères alphanumériques
Ce fichier ne doit être importé que si le fichier #CART mentionne un conditionnement.
Enumérés de gamme - Articles

## #CREF — Enumérés de gamme - Articles
*Export modèle : 9 occurrence(s), 10 lignes.*

Champ Code Correspondance/Commentaire
Intitulé énuméré de 
gamme 1 21 caractères alphanumériques
Intitulé énuméré de 
gamme 2 21 caractères alphanumériques
Référence énuméré 18 caractères alphanumériques
Prix d’achat de l’énuméré Format Prix
Code-barres énuméré 18 caractères alphanumériques
Dernier prix d’achat 
énuméré Format Prix
Nouveau prix achat de 
l’énuméré Format Prix
Coût standard de 
l’énuméré Format Montant

Champ Code Correspondance/Commentaire
Code EDI énuméré 45 caractères alphanumériques
Mise en sommeil énuméré 0
Non
Oui
Ce fichier ne doit être importé que si le fichier #CART mentionne une ou plusieurs gammes de 
type Produit .
Gamme opératoire – Articles

## #CAOP — Gamme opératoire – Articles
*Export modèle : 67 occurrence(s), 12 lignes.*

Champ Code Correspondance/Commentaire
Ressource 10 caractères alphanumériques majuscules
Numéro opération 10 caractères alphanumériques
Temps total ressource Format Temps
Type 0
Fixe
Variable
Description 255 caractères alphanumériques si indication 
Ressource sinon 69 caractères alphanumériques
Enuméré gamme 1 
composé 21 caractères alphanumériques
Enuméré gamme 2 
composé 21 caractères alphanumériques
Chevauchement 0
Non
Oui

Champ Code Correspondance/Commentaire
Démarrage
1
A la fin de
Au cours de
En même temps que
N° opération 
chevauchement 10 caractères alphanumériques
Valeur chevauchement Nombre réel (14 caractères)
Type chevauchement 0
Unité
Pourcentage
Prévisions – Articles

## #CAPR — Prévisions – Articles
*Export modèle : 826 occurrence(s), 5 lignes.*

Champ Code Correspondance/Commentaire
Référence composante 18 caractères alphanumériques majuscules
Enuméré gamme 1 
composé 21 caractères alphanumériques
Enuméré gamme 2 
composé 21 caractères alphanumériques
Dépôt 35 caractères alphanumériques
Date Format Date
Quantité Format quantité
Glossaires - Articles

## #CAGL — Glossaires - Articles
*Export modèle : 10 occurrence(s), 1 lignes.*

Champ Code Correspondance/Commentaire
Intitulé glossaire 35 caractères alphanumériques
La ligne d’intitulé peut être répétée autant de fois que nécessaire.
Comptabilité - Articles

## #CACP — Comptabilité - Articles
*Export modèle : 61 occurrence(s), lignes 28, 42, 56, 84, 98.*

Champ Code Correspondance/Commentaire
Type
2
Ventes
Achats
Stocks
Catégorie comptable 1 à 50 Numéro de catégorie comptable
Compte général Format Compte
Section analytique Format Section analytique
Compte taxe 1 5 caractères alphanumériques majuscules
Compte taxe 2 5 caractères alphanumériques majuscules
Compte taxe 3 5 caractères alphanumériques majuscules
Type facture 1 à 3 Mettre 1 : Facture (particularité pour version
étrangère)
Date application 1 Date
Date application 2 Date

Champ Code Correspondance/Commentaire
Date application 3 Date
Ancien code taxe 1 5 caractères alphanumériques majuscules
Ancien code taxe 2 5 caractères alphanumériques majuscules
Ancien code taxe 3 5 caractères alphanumériques majuscules
Ces lignes doivent être répétées pour toutes les catégories comptables existantes (maximum 30 fois). 
Les catégories comptables des articles ne pourront pas être importées séparément de la fiche article à 
laquelle elles correspondent.
Références fournisseurs - Articles

## #CAFR — Références fournisseurs - Articles
*Export modèle : 54 occurrence(s), 19 lignes.*

Champ Code Correspondance/Commentaire
Numéro fournisseur 17 caractères alphanumériques majuscules
Référence fournisseur 18 caractères alphanumériques
Prix d’achat Format Prix
Remise Format Double
Unité achat/vente 1 à 30 Numéro de l’unité de vente/achat
Conversion Format Double
Délai d’approvisionnement 3 caractères numériques
Garantie 4 caractères numériques
Colisage Format Quantité
QEC Format Quantité

Champ Code Correspondance/Commentaire
Gamme remise Qté/Mont. 0
1 à 50
Pas de gamme remise quantité/montant
Numéro de la gamme
Principal 0
Non principal
Principal
Devise 0
1 à 32
Aucune
Numéro de la devise
Type remise 0
Remise
Hors remise
Diviseur conversion 1 Format Double
Code-barres fournisseur 18 caractères alphanumériques
Date application tarif Format Date
Nouveau prix d’achat ou 
Nouveau prix devise (1)
Format Prix
Nouvelle remise Format Double
(1) Une seule zone pour les deux valeurs.
Ce fichier peut être suivi d’un #CATG (Tarif par énuméré de gamme) et/ou d’un #CATQ (Gamme de 
remise du tarif).
Les références fournisseurs ne sont pas obligatoires s’il n’y a pas de fournisseur pour l’article.
Tarifs par énumérés de gamme -
Articles/nomenclatures

## #CATG — Articles/nomenclatures
*Export modèle : 4 occurrence(s), lignes 12, 18, 36.*

Champ Code Correspondance/Commentaire
Intitulé énuméré gamme 1 21 caractères alphanumériques
Intitulé énuméré gamme 2 21 caractères alphanumériques

Champ Code Correspondance/Commentaire
Prix de l’énuméré Format Prix
Référence énuméré 
fournisseur 18 caractères alphanumériques
Code-barres énuméré 
fournisseur 18 caractères alphanumériques
Nouveau prix Format Prix
Cette information est obligatoire si l’article mentionne une gamme de produit. Elle doit être répétée 
autant de fois qu’il y a d’énumérés dans la gamme.
Ce fichier peut faire suite à un #CAFR (Référence fournisseur) ou un #CACL (Tarif de vente de 
l’article).
S’il fait suite à un fichier #CACL, la ligne Code-barres énuméré fournisseur est vide.
Gammes de remise du tarif - Articles/ nomenclatures

## #CATQ — Gammes de remise du tarif - Articles/ nomenclatures
*Export modèle : 8 occurrence(s), lignes 16, 24, 28.*

Champ Code Correspondance/Commentaire
Type tarif
1
Remise par quantité
Remise par montant
Prix net
Borne supérieure Format Quantité si Type = 0 ou 2
Format Montant si Type = 1
Remise 45 caractères alphanumériques
Prix net Format Prix
Cette dernière valeur doit préciser le type de la remise en mentionnant le symbole %, F, U ou 
l’opérateur + dans le cas de remises en cascade. Voir les commandes Articles et Nomenclatures pour 
des informations complémentaires.
Les tarifs sont facultatifs.

Ce fichier peut apparaître à la suite d’un #CAFR (Référence fournisseur) ou d’un #CACL (Tarif de 
vente de l’article).
Tarifs de vente - Articles

## #CACL — Tarifs de vente - Articles
*Export modèle : 100 occurrence(s), 16 lignes.*

Champ Code Correspondance/Commentaire
Catégorie tarifaire 0
1 à 32
Si import de tarif client
Numéro de la catégorie tarifaire
Prix de vente Format Prix
Coefficient Format Double
Remise Format Double
Mode arrondi 0
1 à 10
Aucun
Numéro de l’arrondi
Gamme remise Qté/Mont. 0
1 à 50
Pas de gamme remise qté/montant
Numéro de la gamme
Type prix de vente 0
HT
TTC
Devise 0
1 à 32
Aucun
Numéro de la devise
N° de client 17 caractères alphanumériques majuscules
Calcul PV/PR 0
Non
Oui
Type remise 0
Remise
Hors remise

Champ Code Correspondance/Commentaire
Référence client 18 caractères alphanumériques
Date application tarif Format Date
Nouveau prix de vente ou 
Nouveau prix devise (1) Format Prix 
Nouveau coefficient Format Double
Nouvelle remise Format Double
(1) Une seule zone pour les deux valeurs.
Ce format permet l’importation, soit d’une catégorie tarifaire, soit d’un tarif client. La saisie du numéro 
de client est obligatoire dans le cas d’une importation d’un tarif client. Dans ce cas, indiquez 0 pour la 
zone catégorie tarifaire.
Ce fichier peut être suivi d’un #CATG (Tarif par énuméré de gamme) et/ou d’un #CATQ (Gamme de 
remise du tarif).
Tarifs par énuméré de conditionnement - Articles

## #CATC — Tarifs par énuméré de conditionnement - Articles
*Absent de l'export modèle — structure non vérifiée sur fichier réel.*

Champ Code Correspondance/Commentaire
Intitulé conditionnement 35 caractères alphanumériques
Quantité conditionnée Format Quantité
Prix de l’énuméré Format Prix
Nouveau prix 
conditionnement Format Prix
Cette information est obligatoire si l’article mentionne un conditionnement. Elle doit être répétée autant 
de fois qu’il y a d’énumérés de conditionnement.

Dépôts de stockage - Articles

## #CAST — Dépôts de stockage - Articles
*Export modèle : 83 occurrence(s), 6 lignes.*

Champ Code Correspondance/Commentaire
Intitulé dépôt 35 caractères alphanumériques
Quantité mini Format Quantité
Quantité maxi Format Quantité
Dépôt principal 0
Non principal
Principal
Emplacement principal 13 caractères alphanumériques
Emplacement contrôle 13 caractères alphanumériques
Articles / stock énuméré- Articles

## #CASTGAM — Articles / stock énuméré- Articles
*Export modèle : 18 occurrence(s), 7 lignes.*

Champ Code Correspondance/Commentaire
Intitulé dépôt 35 caractères alphanumériques
Enuméré 1 21 caractères alphanumériques
Enuméré 2 21 caractères alphanumériques
Quantité mini Format Quantité
Quantité maxi Format Quantité

Champ Code Correspondance/Commentaire
Emplacement principal 13 caractères alphanumériques
Emplacement contrôle 13 caractères alphanumériques
Modèles d’enregistrement - Articles

## #CAMO — Modèles d’enregistrement - Articles
*Absent de l'export modèle — structure non vérifiée sur fichier réel.*

Champ Code Correspondance/Commentaire
Intitulé modèle 35 caractères alphanumériques
Type
1
3
5
Tous les domaines
Ventes
Achats
Stocks
Ventes comptoir
Documents internes
Articles / Ressources

## #CARTRES — Articles / Ressources
*Export modèle : 7 occurrence(s), lignes 1, 2, 4, 6.*

Champ Code Correspondance/Commentaire
Ressources défaut C39 (18)
Ressources C39 (18) n fois
Fichier comptable

Plan comptable

## #MPLG — Plan comptable
*Export modèle : 314 occurrence(s), 23 lignes.*

Champ Code Correspondance/Commentaire
Numéro compte Format Compte
Type 0
Détail,
Total
Intitulé 35 caractères alphanumériques
Classement 17 caractères alphanumériques
Nature
1
3
5
7
9
11
13
Aucune
Client
Fournisseur
Salarié
Banque
Caisse
Amortissement / Provision
Résultat - Bilan
Charge
Produit
Résultat – Gestion
Immobilisations
Capitaux
Stock
Titre
Report à nouveau
1
Aucun
Solde
Détail
Compte reporting Format Compte
Raccourci 6 caractères alphanumériques majuscules
Pagination 0
1 à 99
Saut de page
Sauts de lignes

Champ Code Correspondance/Commentaire
Regroupement 0
Non
Oui
Saisie analytique 0
Non
Oui
Saisie échéance 0
Non
Oui
Saisie Quantités 0
Non
Oui
Lettrage automatique 0
Non
Oui
Saisie tiers 0
Non
Oui
Date de création Format Date
Bloc notes 255 caractères alphanumériques
Option devises 0
Non
Oui
Numéro devise 0 à 32 Numéro de la devise
Code taxe 3 caractères alphanumériques majuscules
Mise en sommeil 0
Non
Oui
Report analytique 0
Non
Oui

Champ Code Correspondance/Commentaire
Lettrage en saisie 0
Non
Oui
Ce fichier peut être suivi d’un #CIVA (Information libre éléments).
Répartition analytique - Comptes généraux

## #MPGA — Répartition analytique - Comptes généraux
*Export modèle : 43 occurrence(s), 4 lignes.*

Champ Code Correspondance/Commentaire
Plan analytique 1 à 11 Numéro du plan analytique
Numéro Section 
analytique 13 caractères alphanumériques majuscules
Type répartition
1
Pourcentage
Equilibre
Montant
Valeur répartition montant 14 caractères numériques
Ce fichier doit suivre un #MPLG (Plan comptable) dans le cas d’un compte avec ventilation.
Fichier Plan analytique (Codes affaires)

## #MPCA — Fichier Plan analytique (Codes affaires)
*Export modèle : 62 occurrence(s), 22 lignes.*

Champ Code Correspondance/Commentaire
Numéro plan 1 à 11 Numéro du plan analytique
Numéro section (ou code 
affaire) Format Section analytique
Intitulé 35 caractères alphanumériques

Champ Code Correspondance/Commentaire
Type 0
Détail
Total
Classement 17 caractères alphanumériques
Raccourci 6 caractères alphanumériques majuscules
Report 0
Non
Oui
Niveau d'analyse 1 à 10 Numéro du niveau d’analyse
Pagination 0
1 à 99
Saut de page
Sauts de lignes
Mise en sommeil 0
Non
Oui
Date de création Format Date
Domaine
1
Les deux
Ventes
Achats
Objectif chiffre affaire 
achats 14 caractères numériques
Objectif chiffre affaire 
ventes 14 caractères numériques
Nom collaborateur 35 caractères alphanumériques
Prénom collaborateur 35 caractères alphanumériques

Champ Code Correspondance/Commentaire
Statut
1
3
5
Proposition
Accepté
Perdu
En cours
En attente
Terminé
Date création affaire Format Date
Date acceptation affaire Format Date
Date début affaire Format Date
Date fin affaire Format Date
Mode facturation 0
Forfaitaire
A l’avancement
Ce fichier peut être suivi d’un #CIVA (Information libre éléments).
Fichier Contacts analytiques (Codes affaires)

## #MCTA — Fichier Contacts analytiques (Codes affaires)
*Absent de l'export modèle — structure non vérifiée sur fichier réel.*

Champ Code Correspondance/Commentaire
Nom 35 caractères alphanumériques
Prénom 35 caractères alphanumériques
Service 0 à 30
Fonction 35 caractères alphanumériques
Téléphone 21 caractères alphanumériques

Champ Code Correspondance/Commentaire
Portable 21 caractères alphanumériques
Télécopie 21 caractères alphanumériques
Email 69 caractères alphanumériques
Civilité
1
M
Mme
Melle
Numéro contact 1 à 30
Compte Facebook 35 caractères alphanumériques
Compte LinkedIn 35 caractères alphanumériques
Compte Skype 35 caractères alphanumériques
Taux de taxes

## #MTAX — Taux de taxes
*Export modèle : 21 occurrence(s), lignes 15, 16, 17, 18, 21, 23, 42.*

Champ Code Correspondance/Commentaire
Intitulé 35 caractères alphanumériques
Type de taux
1
Taux (%)
Montant (F)
Montant unitaire (U)
Taux Si Type de taux = 0 : Format Double
sinon Format Montant

Champ Code Correspondance/Commentaire
Type
1
3
5
7
9
TVA/Débit
TVA/Encaissement
Tp/Ht
Tp/Ttc
Tp/Poids
TVA/CEE
Surtaxe
IRPF (réservé version Espagnole)
IRPF Agraire (réservé version Espagnole)
IGIC (réservé version Espagnole)
Numéro compte taxe Format Compte
Code taxe 3 caractères alphanumériques majuscules
Taxe non perçue 0
Non
Oui
Sens 0
Déductible
Collectée
Provenance
1
3
5
7
Nationale
Intra-communautaire
Export
Divers 1
Divers 2
Divers 3
Divers 4
Divers 5
Code regroupement 5 caractères alphanumériques
Assujettissement 14 caractères alphanumériques
Grille base 3 caractères alphanumériques
Grille taxe 3 caractères alphanumériques

Champ Code Correspondance/Commentaire
Code EDI 3 caractères alphanumériques majuscules
Mention exonération TVA 100 caractères alphanumériques
Comptes associés x fois Format Compte
Mentions d’exonération de taxes

## #MMEX — Mentions d’exonération de taxes
*Export modèle : 8 occurrence(s), 3 lignes.*

Champ Code Correspondance/Commentaire
Intitulé 100 caractères alphanumériques
Code motif 200 caractères alphanumériques
Code catégorie 2 caractères alphanumériques majuscules
Codes routage

## #MFAR — Codes routage
*Absent de l'export modèle — structure non vérifiée sur fichier réel.*

Réservé Facture électronique et disponible Sage100 v10.X
Champ Code Correspondance/Commentaire
Type code routage
1
3
Code service
GLN
ODETTE
SWIFT
Autre
Code routage 100 caractères alphanumériques

Champ Code Correspondance/Commentaire
Application préférée
1
Gestion commerciale
Comptabilité
Application externe
Cadre de facturation

## #CCAF — Cadre de facturation
*Export modèle : 20 occurrence(s), 4 lignes.*

Réservé Facture électronique et disponible Sage100 v10.X
Champ Code Correspondance/Commentaire
Intitulé 100 caractères alphanumériques
Code 3 caractères alphanumériques
Type
1
3
Bien 
Service
Mixte
Entité publique
Géré pour les factures
1
Non
Oui
Non supprimable
Motifs de refus facture

## #MMRE — Motifs de refus facture
*Export modèle : 26 occurrence(s), 6 lignes.*

Réservé Facture électronique et disponible Sage100 v10.X
Champ Code Correspondance/Commentaire
Intitulé 100 caractères alphanumériques

Champ Code Correspondance/Commentaire
Code motif 20 caractères alphanumériques
Refusée 0
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
Codes journaux

## #MCJR — Codes journaux
*Export modèle : 18 occurrence(s), 16 lignes.*

Champ Code Correspondance/Commentaire
Code journal 6 caractères alphanumériques
Intitulé 35 caractères alphanumériques
Compte trésorerie Format Compte
Type
1
3
Achat
Vente
Trésorerie
Général
Situation

Champ Code Correspondance/Commentaire
Numérotation pièces
1
Manuelle
Continue pour le journal
Continue pour le fichier
Contrepartie à chaque 
ligne
1
Non
Oui
Saisie analytique 0
Non
Oui
Type rapprochement
1
Aucun
Contrepartie
Trésorerie
Mise en sommeil 0
Non
Oui
Masquer les totaux 0
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
Lettrage en saisie 0
Non
Oui
Protection journal 0
Non
Oui
Personnalisation libellé 69 caractères alphanumériques

Modèles de règlement

## #MMDR — Modèles de règlement
*Export modèle : 4 occurrence(s), lignes 12, 23, 34.*

Champ Code Correspondance/Commentaire
Intitulé 35 caractères alphanumériques
Mode règlement 1 à 30 Numéro du mode de règlement
Condition
1
Jours nets
Fin de mois civil
Fin de mois
Nbre jours 0 à 999
Jours de tombée 0 à 31 Ligne à répéter 6 fois
Type répartition
1
Pourcentage
Equilibre
Montant
Valeur répartition Format Montant
Les 6 dernières lignes sont répétées n fois
Banques

## #MBQE — Banques
*Export modèle : 5 occurrence(s), lignes 192, 237.*

Champ Code Correspondance/Commentaire
Intitulé 35 caractères alphanumériques
Adresse 35 caractères alphanumériques
Complément 35 caractères alphanumériques

Champ Code Correspondance/Commentaire
Code postal 9 caractères alphanumériques
Ville 35 caractères alphanumériques
Région 25 caractères alphanumériques
Pays 35 caractères alphanumériques
Contact 35 caractères alphanumériques
Abrégé 17 caractères alphanumériques
Mode remise
1
Fichier magnétique
Télétransmission
Papier
Bordereau en devise 0
Non
Oui
Date convention Dailly Format Date
Nature juridique Dailly 35 caractères alphanumériques
Adresse Dailly 35 caractères alphanumériques
Complément Dailly 35 caractères alphanumériques
Code postal Dailly 9 caractères alphanumériques
Ville Dailly 35 caractères alphanumériques
Registre commerce 
Société Dailly 35 caractères alphanumériques

Champ Code Correspondance/Commentaire
Code BIC 13 caractères alphanumériques
Code identification 16 caractères alphanumériques
Achat en devise 0
Non
Oui
Remise
1
3
Mono Devise/ Mono Date d'exécution 
Mono Devise/ Multi Date d'exécution 
Multi Devise/ Mono Date d'exécution
Multi Devise/ Multi Date d'exécution
Donneur ordre adresse 0
Non
Oui
Donneur ordre ville 0
Non
Oui
Donneur ordre code postal 0
Non
Oui
Donneur ordre numéro de 
Siret
1
Non
Oui
Donneur ordre code 
identification
1
Non
Oui
Donneur ordre ville 
agence
1
Non
Oui
Donneur ordre code postal 
agence
1
Non
Oui

Champ Code Correspondance/Commentaire
Donneur ordre type 
identifiant
1
Non
Oui
Donneur ordre clé RIB 0
Non
Oui
Virement adresse 0
Non
Oui
Virement ville 0
Non
Oui
Virement code postal 0
Non
Oui
Virement numéro de Siret 0
Non
Oui
Virement pays 0
Non
Oui
Virement référence du 
contrat de change
1
Non
Oui
Virement date achat 0
Non
Oui
Virement taux de change 0
Non
Oui
Virement instruction 
particulière
1
Non
Oui
Banque bénéficiaire 
intitulé
1
Non
Oui

Champ Code Correspondance/Commentaire
Banque bénéficiaire BIC 0
Non
Oui
Banque bénéficiaire 
adresse
1
Non
Oui
Banque bénéficiaire ville 0
Non
Oui
Banque bénéficiaire code 
postal
1
Non
Oui
Banque bénéficiaire 
compte bancaire
1
Non
Oui
Banque intermédiaire 
intitulé
1
Non
Oui
Banque intermédiaire BIC 0
Non
Oui
Banque intermédiaire 
adresse
1
Non
Oui
Banque intermédiaire ville 0
Non
Oui
Banque intermédiaire code 
postal
1
Non
Oui
Banque intermédiaire pays 0
Non
Oui
Téléphone 21 caractères alphanumériques

Champ Code Correspondance/Commentaire
Télécopie 21 caractères alphanumériques
E-mail 69 caractères alphanumériques
Site 69 caractères alphanumériques
Conditions découvert Type 
plafond
1
Intervalle
Seuil
Conditions découvert Base 
calcul intérêts
1
Non
Oui
Conditions découvert Taux 
effectif Format Montant
2 fois
Conditions découvert 
Valeur plafond
Format Montant
2 fois
Conditions découvert 
Marge
Format Montant
Type application intérêt
créditeurs
1
Fictive
Réelle
Taux effectif intérêt
créditeurs Format double
Assiette intérêt créditeurs 0
Total créditeur
Solde créditeur : débiteur
Limite intérêt créditeurs 0
Commission mouvement
Intérêt trimestriel

Champ Code Correspondance/Commentaire
2 Solde débiteur moyen
Base calcul intérêts 
créditeurs
1
Total créditeur
Solde créditeur / débiteur
Type calcul commission
1
Plafond mensuel
Plafond trimestriel
Solde débiteur moyen
Limite commission 0 à 999999
Taux CPFD commission Format double
Commission mouvement 
frais Format double
Montant frais tenue 
compte frais Format montant
Périodicité 
comptabilisation frais
1
Mensuelle
Trimestrielle
Annuelle
Seuil exonération frais Format montant
Type exonération frais
1
Aucune
Commission mouvement
Solde créditeur moyen
Seuil exonération solde 
créditeur frais Format montant
Mode de perception 0 Aucun

Champ Code Correspondance/Commentaire
1 Ligne
Montant variable HT Format montant
Minimum perçu Format montant
Maximum perçu Format montant
Assujettir la 
commission/TVA
1
Non
Oui
Assujettir les frais/TVA
1
Non
Oui
Transfert/Adresse eMail 
envoi 69 caractères alphanumérique
Transfert/Site 69 caractères alphanumérique
Format virements
1
AFB
SEPA
Format virements 
internationaux
1
AFB
SEPA
12 fois
Délai 
télétransmission
0 à 99
Délai fichier 0 à 99

Champ Code Correspondance/Commentaire
Heure limite 
télétransmission Heure
Heure limite fichier Heure
Virement code service 4 caractères alphanumériques Majuscule
Format prélèvements 0
AFB
SEPA
Version format 
prélèvements
1
0 = PAIN00800101
1 = PAIN00800102
Version format virements 0
0 = PAIN00800101
1 = PAIN00800102
Compte général frais 
OPCVM Format compte
Compte général TVA 
OPCVM Format compte
Compte général Moins 
value OPCVM Format compte
Compte général Plus 
value OPCVM Format compte
Virement imputation
1
0 = Bénéficiaire / Emetteur
1 = Bénéficiaire
2 = Emetteur
Format extraits
1
AFB
XML

Champ Code Correspondance/Commentaire
Version format extraits 0
Les informations suivantes 
doivent être répétées 
autant de fois qu’il y a de 
comptes à la banque.
Champ Code Correspondance/Commentaire
Code banque 14 caractères alphanumériques
Code guichet 17 caractères alphanumériques
Compte 34 caractères alphanumériques
Clé 2 caractères alphanumériques
Commentaire 69 caractères alphanumériques
Code journal 6 caractères alphanumériques
Structure banque
1
3
Locale
Etranger
BIN
IBAN
Devise 1 à 32 Numéro de la devise
Abrégé 5 caractères alphanumériques majuscules
Numéro émetteur 1 3 fois 7 caractères alphanumériques
Numéro émetteur 2 3 fois 7 caractères alphanumériques

Champ Code Correspondance/Commentaire
Numéro émetteur 3 3 fois 7 caractères alphanumériques
Adresse agence 35 caractères alphanumériques
Complément agence 35 caractères alphanumériques
Code postal agence 9 caractères alphanumériques
Ville agence 35 caractères alphanumériques
Pays agence 35 caractères alphanumériques
BIC 11 caractères alphanumériques
Code IBAN 34 caractères alphanumériques
Calcul IBAN
1
Non
Oui
Nom agence 35 caractères alphanumériques
Code journal escompte 6 caractères alphanumériques
Code journal 
encaissement
6 caractères alphanumériques
Compte intra-groupe
1
Oui
Non
Raison sociale bénéficiaire 35 caractères alphanumériques
Adresse bénéficiaire 35 caractères alphanumériques

Champ Code Correspondance/Commentaire
Complément bénéficiaire 35 caractères alphanumériques
Code postal bénéficiaire 9 caractères alphanumériques
Ville bénéficiaire 35 caractères alphanumériques
Pays bénéficiaire 35 caractères alphanumériques
Siret bénéficiaire 14 caractères alphanumériques
Code région bénéficiaire 25 caractères alphanumériques
Code région agence 25 caractères alphanumériques
Pays agence 35 caractères alphanumériques
Compte dépôts Trésor 
Public
1
Oui
Non
Compte Banque de 
France
1
Oui
Non
Trésor Public Service 
dépôts
70 caractères alphanumériques
Trésor Public Type 
Service
1
Non
Oui
Trésor Public Codique 
service
7 caractères alphanumériques majuscules
Trésor Public IBAN 35 caractères alphanumériques

Champ Code Correspondance/Commentaire
Trésor Public BIC 11 caractères alphanumériques
Trésor Public Service 
Remise ESI
1
Non
Oui
Trésor Public Identifiant 51 9 caractères alphanumériques
BDF code remettant 5 caractères alphanumériques
Mise en sommeil 0
Non
Oui
Contacts banque

## #MCTB — Contacts banque
*Export modèle : 2 occurrence(s), 13 lignes.*

Champ Code Correspondance/Commentaire
Nom 35 caractères alphanumériques
Prénom 35 caractères alphanumériques
Service 1 à 30 Position dans la liste des services (paramètres 
société)
Fonction 35 caractères alphanumériques
Téléphone 21 caractères alphanumériques
Portable 21 caractères alphanumériques
Télécopie 21 caractères alphanumériques

Champ Code Correspondance/Commentaire
E-mail 69 caractères alphanumériques
Civilité
1
M.
Mme
Mlle
Type contact 1 à 30 Correspond au n° d'index des types de contact
Compte Facebook 35 caractères alphanumériques
Compte LinkedIn 35 caractères alphanumériques
Compte Skype 35 caractères alphanumériques
(1) Voir Type contact.
Il est possible de créer un nombre illimité de contacts dossier. Les 13 lignes doivent être répétées 
pour chaque dossier.
Conditions de valeurs banque

## #MCVB — Conditions de valeurs banque
*Absent de l'export modèle — structure non vérifiée sur fichier réel.*

Champ Code Correspondance/Commentaire
Code AFB 2 caractères alphanumériques majuscules
Sens 0
Décaissement ou Crédit comptable
Encaissement ou Débit comptable
Nombre de jours de 
valeurs 0 à 999
Type de jour
1
Aucun
Calendaire
Ouvré

Champ Code Correspondance/Commentaire
Echéance reportée 0
Non
Oui
Exonération commission 
de mouvement
1
Non
Oui
Modèles de grille

## #MMDG — Modèles de grille
*Export modèle : 4 occurrence(s), lignes 11, 15.*

Champ Code Correspondance/Commentaire
Type 0
Général (pas utilisé en gestion commerciale)
Analytique
Intitulé 35 caractères alphanumériques
Raccourci 6 caractères alphanumériques
Les informations suivantes doivent être répétées autant de fois qu’il y a de sections analytiques dans 
la grille.
Champ Code Correspondance/Commentaire
Plan analytique 1 à 10 Numéro de plan analytique
Section analytique Format Section analytique (si Type = Analytique)
Type répartition
1
Pourcentage
Equilibre
Montant
Valeur répartition 14 caractères numériques

Fiche client

## #CCLI — Fiche client
*Export modèle : 25 occurrence(s), lignes 120, 121.*

Champ Code Correspondance/Commentaire
N° Client 17 caractères alphanumériques majuscules
Prospect 0
Non
Oui
N° compte principal Format Compte
Qualité 17 caractères alphanumériques
Intitulé 69 caractères alphanumériques
Abrégé 17 caractères alphanumériques
Contact 35 caractères alphanumériques
Adresse 35 caractères alphanumériques
Complément 35 caractères alphanumériques
Code postal 9 caractères alphanumériques
Ville 35 caractères alphanumériques
Région 25 caractères alphanumériques
Pays 35 caractères alphanumériques
Enuméré statistique 1 à 10 21 caractères alphanumériques

Champ Code Correspondance/Commentaire
En-cours maximum Format Montant
Plafond ass. crédit Format Montant
Centrale d’achat 17 caractères alphanumériques
Payeur 17 caractères alphanumériques majuscules
Taux remise Format Double
Taux escompte Format Double
Taux relevé Format Double
Taux RFA Format Double
Catégorie comptable 1 à 50 Numéro de la catégorie comptable vente
Devise 0 à 32 Numéro de la devise
Code risque 1 à 10 Numéro du code risque
Nom représentant 35 caractères alphanumériques
Prénom représentant 35 caractères alphanumériques
Catégorie tarifaire 1 à 32 Numéro de la catégorie tarifaire
Périodicité 1 à 10 Numéro de la périodicité

Champ Code Correspondance/Commentaire
Langue
1
Aucune
Langue 1
Langue 2
Raccourci 6 caractères alphanumériques
Nb Facture 2 caractères numériques
1 BL/Facture 0
Plusieurs BL/Fact.
1 BL/Fact
Siret 14 caractères alphanumériques
NAF (APE) 5 caractères alphanumériques
N° identifiant 25 caractères alphanumériques
Type Code EDI
1
GLN
DUNS
Autre
Code EDI 23 caractères alphanumériques
Commentaire 35 caractères alphanumériques
Contrôle d’encours
1
Contrôle automatique
Selon code risque
Compte bloqué
Dépôt par défaut 35 caractères alphanumériques
Mise en sommeil 0
Non
Oui

Champ Code Correspondance/Commentaire
Plan analytique 0 à 11 Numéro de plan analytique
Code affaire Format Section analytique
Date création Format Date
Téléphone 21 caractères alphanumériques
Télécopie 21 caractères alphanumériques
E-mail 69 caractères alphanumériques
Site 69 caractères alphanumériques
N° Coface 25 caractères alphanumériques
Placé sous surveillance 0
Non
Oui
Date création société Format Date
Forme juridique 32 caractères alphanumériques
Effectif 10 caractères numériques
Chiffre d’affaires Format double
Résultat net Format double
Incidents de paiement 0
Non
Oui

Champ Code Correspondance/Commentaire
Date du dernier incident Format Date
Privilèges
1
Aucun privilège
Présence privilège
Privilège inconnu
Régularités de paiement 0 à 99
Cotation de la solvabilité 4 caractères alphanumériques majuscules
Date dernière mise à jour Format Date
Objet dernière mise à jour 60 caractères alphanumériques
Date arrêté de bilan Date au format JJMMAA ou vide
Nombre de mois du bilan 0..99
Priorité livraison 0 à 999
Livraison partielle 0
Oui
Non
Modèle de règlement 35 caractères alphanumériques
Ventilation IFRS Format Section analytique
Date début fermeture Format date
Date fin fermeture Format date
Format factures 0 Réservé Export

Champ Code Correspondance/Commentaire
Type identifiant 0 Réservé Export
Intitulé représentant légal Réservé Export
NIF représentant légal Réservé Export
Identifiant EDI Sage 8 caractères numériques
Profils du tiers
1
3
Non défini
Non inscrit
Accepte la dématérialisation
Refuse la dématérialisation
Statut d’échange
1
3
Aucun
Invitation en cours
Accepte l’échange
Refuse l’échange
Echange révoqué
Date actualisation 
informations Format Date
Délai de transport 0 à 999
Code langue EDI 2 caractères numériques
Transmettre Compte 
rendu rapprochement
1
Non
Oui
Transmettre autorisation 
de bon à payer
1
Non
Oui
Compte Facebook 35 caractères alphanumériques
Compte LinkedIn 35 caractères alphanumériques

Champ Code Correspondance/Commentaire
Exclure des traitements 0
Non
Oui
Bloc-notes 2000 caractères
Jours de commande (ligne 
répétée 7 fois)
1
Non
Oui
Jours de livraison (ligne 
répétée 7 fois)
1
Non
Oui
Calendrier 35 caractères alphanumériques
Assujettissement
1
Assujetti à TVA
Particulier ou Non assujetti à TVA
Type autre identifiant
1
3
5
Aucun
Union Européenne Hors France
Hors Union européenne
RIDET
TAHITI
Particulier
Autre
Valeur autre identifiant 80 caractères alphanumériques
Type entité
1
Non référencée annuaire
Privée assujettie TVA France
Publique
Contrôles émission
1
Aucun
Code service obligatoire
Référence engagement obligatoire

Champ Code Correspondance/Commentaire
4
Code service et Référence engagement 
obligatoires
Code service ou référence engagement obligatoire
Compte bancaire société
Banque
14 caractères alphanumériques
Compte bancaire société
Guichet
17 caractères alphanumériques
Compte bancaire société
Compte
34 caractères alphanumériques
Compte bancaire société
Devise
1 à 32 N° de devise
Comptes rattachés x fois Format Compte
Ce fichier peut être (immédiatement) suivi d’un #CIVA (Informations libres éléments) et/ou d’un 
#CBQT (Banques du tiers) et/ou d’un #CRLT (Conditions de règlement du tiers) et d’un #MCTT 
(contacts tiers) et/ou d’un #MCIC (informations complémentaires).
Jours de commande et jour de livraison sont à indiquer 7 fois pour indiquer chaque jour de la semaine 
du lundi au dimanche.
Banques – Tiers (clients ou fournisseurs)

## #CBQT — Banques – Tiers (clients ou fournisseurs)
*Export modèle : 44 occurrence(s), 21 lignes.*

Champ Code Correspondance/Commentaire
Principale 0
Non principale
Principale
Intitulé 35 caractères alphanumériques

Champ Code Correspondance/Commentaire
Rib banque 14 caractères alphanumériques
Rib guichet 17 caractères alphanumériques
Rib compte 34 caractères alphanumériques
Rib Clé 2 caractères alphanumériques
Commentaire 69 caractères alphanumériques
Structure banque
1
3
Locale
Etranger
BIN
IBAN
Devise 1 à 32 N° de devise
Adresse agence 35 caractères alphanumériques
Complément agence 35 caractères alphanumériques
Code postal agence 9 caractères alphanumériques
Ville agence 35 caractères alphanumériques
Pays agence 35 caractères alphanumériques
BIC 11 caractères alphanumériques
Code routage 35 caractères alphanumériques
Code IBAN 34 caractères alphanumériques

Champ Code Correspondance/Commentaire
Calcul IBAN 0
Non
Oui
Nom agence 35 caractères alphanumériques
Code région agence 25 caractères alphanumériques
Pays agence 35 caractères alphanumériques
Ce fichier doit être importé immédiatement après le #CCLI (Fiche tiers client) ou le #CFOU (Fiche tiers 
fournisseur) auquel il se rapporte.
Conditions de règlement – Tiers (clients ou 
fournisseurs)

## #CRLT — fournisseurs)
*Export modèle : 40 occurrence(s), 11 lignes.*

Champ Code Correspondance/Commentaire
Mode règlement 1 à 30 Numéro du mode de règlement
Condition
1
Jours nets
Fin de mois civil
Fin de mois
Nbre jours 0 à 999
Jours de tombée 0 à 31 Ligne répétée 6 fois
Type répartition
1
Pourcentage
Equilibre
Montant
Valeur répartition Format Montant

Ce fichier doit être importé immédiatement après le #CCLI (Fiche tiers client) ou le #CFOU (Fiche tiers 
fournisseur) auquel il se rapporte.
Dépôts de livraison clients

## #CCDL — Dépôts de livraison clients
*Export modèle : 26 occurrence(s), 17 lignes.*

Champ Code Correspondance/Commentaire
Intitulé 69 caractères alphanumériques
Adresse 35 caractères alphanumériques
Complément 35 caractères alphanumériques
Code postal 9 caractères alphanumériques
Ville 35 caractères alphanumériques
Région 25 caractères alphanumériques
Pays 35 caractères alphanumériques
Contact 35 caractères alphanumériques
Expédition 1 à 50 Numéro du mode d’expédition
Condition livraison 1 à 30 Numéro de la condition de livraison
Principal 0
Non principal
Principal
Téléphone 21 caractères alphanumériques
Télécopie 21 caractères alphanumériques

Champ Code Correspondance/Commentaire
E-mail 69 caractères alphanumériques
Commentaire 69 caractères alphanumériques
Délai de transport 0 à 999
Adresse de facturation
1
Non
Oui
Les informations sur les dépôts de livraison devront obligatoirement se trouver à la suite de la fiche 
tiers.
Contacts clients

## #MCTT — Contacts clients / Contacts fournisseurs
*Export modèle : 23 occurrence(s), 13 lignes.*

Champ Code Correspondance/Commentaire
Nom 35 caractères alphanumériques
Prénom 35 caractères alphanumériques
Service 1 à 30 Position dans la liste des services (paramètres 
société)
Fonction 35 caractères alphanumériques
Téléphone 21 caractères alphanumériques
Portable 21 caractères alphanumériques
Télécopie 21 caractères alphanumériques

Champ Code Correspondance/Commentaire
E-mail 69 caractères alphanumériques
Civilité
1
M.
Mme
Mlle
Type contact 1 à 30 Correspond au n° d'index des types de contact (1)
Compte Facebook 35 caractères alphanumériques
Compte LinkedIn 35 caractères alphanumériques
Compte Skype 35 caractères alphanumériques
(1) Voir Type contact.
Il est possible de créer un nombre illimité de contacts dossier. Les dix lignes doivent être répétées 
pour chaque dossier.
Information complémentaire tiers

Même structure que Contacts client #MCTT

Fichier Agenda

## #MCIC — Information complémentaire tiers
*Absent de l'export modèle — structure non vérifiée sur fichier réel.*

Champ Code Correspondance/Commentaire
Code 13 caractères alphanumériques
Intitulé 35 caractères alphanumériques
Domaine
1
Client
Entête
Ligne
Type
1
3
Texte
Date
Montant
Valeur

Champ Code Correspondance/Commentaire
Valeur 35 caractères en fonction du type
Les informations sur Informations complémentaires devront obligatoirement se trouver à la suite de la 
fiche tiers.
Codes routages tiers

## #MFRT — Codes routages tiers
*Absent de l'export modèle — structure non vérifiée sur fichier réel.*

Champ Code Correspondance/Commentaire
Type code routage
1
3
Code service
GLN
ODETTE
SWIFT
Autre
Code routage 100 caractères alphanumériques
Intitulé code routage 100 caractères alphanumériques
Actif
1
Non
Oui
Fiche Fournisseur

## #CFOU — Fiche Fournisseur
*Export modèle : 28 occurrence(s), lignes 114, 115.*

Champ Code Correspondance/Commentaire
N° Fournisseur 17 caractères alphanumériques
N° compte principal Format Compte

Champ Code Correspondance/Commentaire
Qualité 17 caractères alphanumériques
Intitulé 69 caractères alphanumériques
Abrégé 17 caractères alphanumériques
Contact 35 caractères alphanumériques
Adresse 35 caractères alphanumériques
Complément 35 caractères alphanumériques
Code postal 9 caractères alphanumériques
Ville 35 caractères alphanumériques
Région 25 caractères alphanumériques
Pays 35 caractères alphanumériques
Enuméré statistique 1 à 10 21 caractères alphanumériques
En-cours maximum Format Montant
Encaisseur 17 caractères alphanumériques majuscules
Taux remise Format Double
Taux escompte Format Double
Taux relevé Format Double

Champ Code Correspondance/Commentaire
Taux RFA Format Double
Catégorie comptable 1 à 50 Numéro de la catégorie comptable achat
Devise 0 à 32 Numéro de la devise
Langue
1
Aucune
Langue 1
Langue 2
Raccourci 6 caractères alphanumériques
1 BL / Facture 0
Non
Oui
Siret 14 caractères alphanumériques
NAF (APE) 5 caractères alphanumériques
N° identifiant 25 caractères alphanumériques
Type code EDI
1
GLN
DUNS
Autre
Code EDI 23 caractères alphanumériques
Commentaire 35 caractères alphanumériques
Expédition 1 à 50 Numéro du mode d’expédition
Condition livraison 1 à 30 Numéro de la condition de livraison

Champ Code Correspondance/Commentaire
Dépôt par défaut 35 caractères alphanumériques
Mise en sommeil 0
Non
Oui
Plan analytique 1 à 11 Numéro du plan analytique
Code affaire Format Section analytique
Date création Format Date
Téléphone 21 caractères alphanumériques
Télécopie 21 caractères alphanumériques
E-mail 69 caractères alphanumériques
Site 69 caractères alphanumériques
N° COFACE 25 caractères alphanumériques
Placé sous surveillance 0
Non
Oui
Date création société Format Date
Forme juridique 32 caractères alphanumériques
Effectif 10 caractères alphanumériques
Chiffre d’affaire Format double

Champ Code Correspondance/Commentaire
Résultat net Format double
Incidents de paiement 0
Non
Oui
Date du dernier incident Format Date
Privilèges
1
Aucun privilège
Présence privilège
Privilège inconnu
Régularités de paiement 0 à 99
Cotation de la solvabilité 4 caractères alphanumériques majuscules
Date dernière mise à jour Format Date
Objet dernière mise à jour 60 caractères alphanumériques
Date arrêté de bilan Date au format JJMMAA ou vide
Nombre de mois du bilan 0..99
Modèle de règlement 35 caractères alphanumériques
Ventilation IFRS Format Section analytique
Non soumis à pénalité de 
retard
1
Non
Oui
Acheteur nom 35 caractères alphanumériques
Acheteur prénom 35 caractères alphanumériques

Champ Code Correspondance/Commentaire
Date début fermeture Format date
Date fin fermeture Format date
Type identifiant 0 Réservé Export
Intitulé représentant légal Réservé Export
NIF représentant légal Réservé Export
Identifiant EDI Sage 8 caractères numériques
Profils du tiers
1
3
Non défini
Non inscrit
Accepte la dématérialisation
Refuse la dématérialisation
Statut d’échange
1
3
Aucun
Invitation en cours
Accepte l’échange
Refuse l’échange
Echange révoqué
Date actualisation 
informations Format date
Rapprochement facture 0
Bon de livraison
Bon de livraison et Bon de commande
Transmettre le Compte 
rendu de rapprochement
1
Non
Oui
Transmettre l’autorisation 
de Bon à Payer
1
Non
Oui
Délai d’approvisionnement 0 à 999

Champ Code Correspondance/Commentaire
Code langue EDI 2 caractères numériques
Compte Facebook 35 caractères alphanumériques
Compte LinkedIn 35 caractères alphanumériques
Exclure des traitements 0
Non
Oui
Bloc-notes 2000 caractères
Jours de commande (ligne 
répétée 7 fois)
1
Non
Oui
Jours de livraison (ligne 
répétée 7 fois)
1
Non
Oui
Calendrier 35 caractères alphanumériques
Assujettissement
1
Assujetti à TVA
Particulier ou Non assujetti à TVA
Type autre identifiant
1
3
5
Aucun
Union Européenne Hors France
Hors Union européenne
RIDET
TAHITI
Particulier
Autre
Valeur autre identifiant 80 caractères alphanumériques
Type entité 0 Non référencée annuaire

Champ Code Correspondance/Commentaire
2
Privée assujettie TVA France
Publique
Application préférée
Réservé Facture 
électronique et disponible 
Sage100 v10.X
1
3
Aucune
Gestion commerciale
Comptabilité
Application externe
Selon code routage
Compte bancaire société
Banque
14 caractères alphanumériques
Compte bancaire société
Guichet
17 caractères alphanumériques
Compte bancaire société
Compte
34 caractères alphanumériques
Compte bancaire société
Devise
1 à 32 N° de devise
Comptes rattachés x fois Format Compte
Ce fichier peut être (immédiatement) suivi d’un #CIVA (Information libre tiers) et/ou d’un #CBQT 
(Banques du tiers) et/ou d’un #CRLT (Conditions de règlement du tiers) et d’un #MCTT (contacts 
tiers).
Jours de commande et jour de livraison sont à indiquer 7 fois pour indiquer chaque jour de la semaine 
du lundi au dimanche.
Contacts fournisseurs

## #CAGE — Fichier Agenda
*Export modèle : 3 occurrence(s), 14 lignes.*

Champ Code Correspondance/Commentaire
Intéressé
2
4
6
Dépôt
Client
Fournisseur
Représentant
Article
Ressource
Si intéressé = 1 (Dépôt)
Intitulé 35 caractères alphanumériques
Si intéressé = 2 (Client)
N° Client 17 caractères alphanumériques
Si intéressé = 3 
(Fournisseur)
N° Fournisseur 17 caractères alphanumériques
Si intéressé = 4 
(Représentant)
Nom 35 caractères alphanumériques
Si intéressé = 5 (Article)
Référence 18 caractères alphanumériques
Si intéressé = 6
(Ressource)

Champ Code Correspondance/Commentaire
Code 10 caractères alphanumériques majuscules
Groupe d’événement 1 à 50 Numéro du groupe d’événements
Evénement 21 caractères alphanumériques
Type période (1)
2
4
Le
Jusqu’au
A partir du
Pendant
Date début Format Date
Date fin Format Date
Alerte 0
Pas d’alerte
Alerte
Commentaire 69 caractères alphanumériques
Confirmé 0
Non
Oui
Heure début Format de temps
Heure fin Format de temps
Créer un rendez-vous 
Outlook
1
Non
Oui
Contact 71 caractères alphanumériques
(1) Quatre possibilités pour définir la durée d’application d’un événement :
• Le : saisir la date de début,
• Jusqu’au : renseigner uniquement la date de fin,

• A partir du : saisir uniquement la date de début,
• Pendant : saisir les dates de début et de fin.
Fichier Barème
Commissions

## #CTAR — Commissions
*Export modèle : 2 occurrence(s), 9 lignes.*

Champ Code Correspondance/Commentaire
Intitulé 35 caractères alphanumériques
Type 1
Commission représentant
Commission globale
Type période (1)
2
4
En permanence
Le
Jusqu’au
A partir du
Pendant
Date début Format Date
Date fin Format Date
Objectif
2
Quantité
Montant
Taux de remise
Domaine
2
4
Commande
Préparation
Livraison
Facturation
Encaissement
Base 1
CA HT
Marge HT
Calcul 1
Tranche, uniquement si Objectif = 2
Global

(1) Cinq possibilités pour définir la durée d’application d’un barème :
• En permanence : laisser vides les dates de début et de fin
• Le : saisir la date de début
• Jusqu’au : renseigner uniquement la date de fin
• A partir du : saisir uniquement la date de début
• Pendant : saisir les dates de début et de fin
L’importation de ce fichier devra être suivie d’un fichier #CTRE.
Rabais, remises et ristournes clients

## #CRAB — Rabais, remises et ristournes clients
*Export modèle : 1 occurrence(s), 7 lignes.*

Champ Code Correspondance/Commentaire
Intitulé 35 caractères alphanumériques
Type période (1)
2
4
En permanence
Le
Jusqu’au
A partir du
Pendant
Date début Format Date
Date fin Format Date
Objectif 1
Quantité
Montant
Calcul 1
Tranche
Global
Article remise 18 caractères alphanumériques majuscules
(1) Cinq possibilités pour définir la durée d’application d’un barème :
• En permanence : laisser vides les dates de début et de fin
• Le : saisir la date de début
• Jusqu’au : renseigner uniquement la date de fin
• A partir du : saisir uniquement la date de début
• Pendant : saisir les dates de début et de fin

Rabais, remises et ristournes fournisseurs

## #CRABF — Rabais, remises et ristournes fournisseurs
*Export modèle : 1 occurrence(s), 8 lignes.*

Champ Code Correspondance/Commentaire
Intitulé 35 caractères alphanumériques
Fournisseur 17 caractères alphanumériques majuscules
Type période (1)
2
4
En permanence
Le
Jusqu’au
A partir du
Pendant
Date début Format Date
Date fin Format Date
Objectif 1
Quantité
Montant
Calcul 1
Tranche
Global
Article remise 18 caractères alphanumériques majuscules
(1) Cinq possibilités pour définir la durée d’application d’un barème :
• En permanence : laisser vides les dates de début et de fin
• Le : saisir la date de début
• Jusqu’au : renseigner uniquement la date de fin
• A partir du : saisir uniquement la date de début
• Pendant : saisir les dates de début et de fin
Soldes et promotions clients

## #CSOL — Soldes et promotions clients
*Export modèle : 1 occurrence(s), 5 lignes.*

Champ Code Correspondance/Commentaire
Intitulé 35 caractères alphanumériques

Champ Code Correspondance/Commentaire
Type période (1)
2
4
En permanence
Le
Jusqu’au
A partir du
Pendant
Date début Format Date
Date fin Format Date
Remise 45 caractères alphanumériques
Cette dernière valeur doit préciser le type de la remise en mentionnant le symbole % , F , U ou 
l’opérateur + dans le cas de remises en cascade. Voir la fonction Articles pour des informations 
complémentaires.
(1) Cinq possibilités pour définir la durée d’application d’un barème :
• En permanence : laisser vides les dates de début et de fin
• Le : saisir la date de début
• Jusqu’au : renseigner uniquement la date de fin
• A partir du : saisir uniquement la date de début
• Pendant : saisir les dates de début et de fin
Soldes et promotions fournisseurs

## #CSOLF — Soldes et promotions fournisseurs
*Export modèle : 1 occurrence(s), 6 lignes.*

Champ Code Correspondance/Commentaire
Intitulé 35 caractères alphanumériques
Fournisseur 17 caractères alphanumériques majuscules
Type période (1)
2
4
En permanence
Le
Jusqu’au
A partir du
Pendant
Date début Format Date

Champ Code Correspondance/Commentaire
Date fin Format Date
Remise 45 caractères alphanumériques
Cette dernière valeur doit préciser le type de la remise en mentionnant le symbole % , F , U ou 
l’opérateur + dans le cas de remises en cascade. Voir la fonction Articles pour des informations 
complémentaires.
(1) Cinq possibilités pour définir la durée d’application d’un barème :
• En permanence : laisser vides les dates de début et de fin
• Le : saisir la date de début
• Jusqu’au : renseigner uniquement la date de fin
• A partir du : saisir uniquement la date de début
• Pendant : saisir les dates de début et de fin
Sélection articles/familles, clients/catégories du barème

## #CTAA — Sélection articles/familles, clients/catégories du barème
*Export modèle : 6 occurrence(s), lignes 2, 4, 6.*

Champ Code Correspondance/Commentaire
Intéressé
2
4
Famille d’article
Article
Catégorie client
Client
Représentant
Si intéressé = 1 (Famille 
d’article)
Code famille 10 caractères alphanumériques majuscules
Si intéressé = 2 (Article)
Référence Article 18 caractères alphanumériques
Si intéressé = 3 (Catégorie 
client)
N° Catégorie client 1 à 32 Numéro de la catégorie tarifaire

Champ Code Correspondance/Commentaire
Si intéressé = 4 (Client)
N° Client 17 caractères alphanumériques majuscules
Si intéressé = 5 
(Représentant)
Nom représentant 35 caractères alphanumériques
Ces informations sont facultatives et doivent toujours suivre un fichier Commission (#CTAR) valeur 
Intéressé de 1 à 5, Rabais, remise et ristourne (#CRAB) ou Soldes et promotions (#CSOL) valeur 
Intéressé de 1 à 4.
Ces informations sont facultatives et doivent toujours suivre un fichier Rabais, remise et ristourne 
fournisseurs (#CRABF) ou Soldes et promotions fournisseurs (#CSOLF) valeur Intéressé de 1 à 2.
Gamme de commission du barème

## #CTRE — Gamme de commission du barème
*Export modèle : 4 occurrence(s), lignes 8, 10, 12.*

Champ Code Correspondance/Commentaire
Borne supérieure Jusqu’à Format Quantité ou Montant ou Double selon 
objectif fichier Barème
Remise 45 caractères alphanumériques (Valeur + type 
%,U et F)
Ce fichier est facultatif et est toujours importé à la suite des informations Sélection articles/familles ou 
clients/catégories. Si ces dernières informations ne sont pas transférées, le #CTRE doit suivre un 
fichier Commission (#CTAR) ou Rabais, remise et ristourne (#CRAB) ou Rabais, remise et ristourne 
fournisseurs (#CRABF).
Fichier Glossaire

## #CGLO — Fichier Glossaire
*Export modèle : 8 occurrence(s), 8 lignes.*

Champ Code Correspondance/Commentaire
Intitulé 35 caractères alphanumériques
Domaine 1
Article
Document
Raccourci 6 caractères alphanumériques majuscules
Date début Format Date
Date fin Format Date
Texte 1980 caractères alphanumériques
+ Retour chariot et Tabulations.
Texte langue 1 1980 caractères alphanumériques
+ Retour chariot et Tabulations.
Texte langue 2 1980 caractères alphanumériques
+ Retour chariot et Tabulations.
Les informations du glossaire doivent être répétées autant de fois qu’il y a de glossaires.
Les retours à la ligne à l’intérieur d’un glossaire doivent être codifiés par \n.
Fichier Collaborateurs

## #CREP — Fichier Collaborateurs
*Export modèle : 11 occurrence(s), lignes 29, 30.*

Champ Code Correspondance/Commentaire
Nom 35 caractères alphanumériques
Prénom 35 caractères alphanumériques

Champ Code Correspondance/Commentaire
Fonction 20 caractères alphanumériques
Acheteur 0
Non
Oui
Vendeur/représentant 0
Non
Oui
Caissier 0
Non
Oui
Date création Format Date
Niveau d’utilisateur 31 caractères alphanumériques
Adresse 35 caractères alphanumériques
Complément 35 caractères alphanumériques
Code postal 9 caractères alphanumériques
Ville 35 caractères alphanumériques
Région 25 caractères alphanumériques
Pays 35 caractères alphanumériques
Service 35 caractères alphanumériques
Téléphone 21 caractères alphanumériques
Télécopie 21 caractères alphanumériques

Champ Code Correspondance/Commentaire
E-mail 69 caractères alphanumériques
Contrôleur 0
Non
Oui
Portable 21 caractères alphanumériques
Chargé de recouvrement 0
Non
Oui
Matricule 10 caractères alphanumériques
Responsable financier 0
Non
Oui
Transmission 0..2
Compte Facebook 35 caractères alphanumériques
Compte LinkedIn 35 caractères alphanumériques
Compte Skype 35 caractères alphanumériques
Mis en sommeil 0
Non
Oui
Chef des ventes 0
Non
Oui
Intitulé tarif (1) 35 caractères alphanumériques
(1) La ligne Intitulé tarif doit être répétée autant de fois que nécessaire.
Si le représentant possède un taux de commissionnement, l’importation du fichier #CREP devra être 
précédée de l’importation du fichier #CTAR concerné, lequel sera suivi d’un fichier #CTRE.

Fichier Dépôts de stockage
Dépôts de stockage

## #CDEP — Dépôts de stockage
*Export modèle : 2 occurrence(s), 18 lignes.*

Champ Code Correspondance/Commentaire
Intitulé 35 caractères alphanumériques
Adresse 35 caractères alphanumériques
Complément 35 caractères alphanumériques
Code postal 9 caractères alphanumériques
Ville 35 caractères alphanumériques
Région 25 caractères alphanumériques
Pays 35 caractères alphanumériques
Responsable 35 caractères alphanumériques
Principal 0
Dépôt Principal
Dépôt Non principal
Catégorie comptable 1 à 50 Numéro de la catégorie comptable de stock
E-mail 69 caractères alphanumériques
Code dépôt 8 caractères alphanumériques majuscules
Téléphone 21 caractères alphanumériques
Télécopie 21 caractères alphanumériques

Champ Code Correspondance/Commentaire
Exclure du 
réapprovisionnement
1
Non
Oui
Souches ventes
1..50
Souche du document
N° souche (paramètres société)
Souches Achats
1..50
Souche du document
N° souche (paramètres société)
Souches Internes
1..50
Souche du document
N° souche (paramètres société)
Le fichier #CDEP doit être suivi d’un fichier #CDEE.
Utilisateurs dépôts

## #CDUS — Utilisateurs dépôts
*Absent de l'export modèle — structure non vérifiée sur fichier réel.*

Champ Code Correspondance/Commentaire
Utilisateur 35 caractères alphanumériques
Doit suivre #CEDEP
Emplacement dépôt

## #CDEE — Emplacement dépôt
*Export modèle : 111 occurrence(s), 5 lignes.*

Champ Code Correspondance/Commentaire
Code 13 caractères alphanumériques
Intitulé 35 caractères alphanumériques

Champ Code Correspondance/Commentaire
Zone
1
3
Aucune
A
B
C
Type
1
Standard
Contrôle
Transit
Défaut 0
Non
Oui
Doit suivre un #CDEP
Contacts dépôt

## #CDEC — Contacts dépôt
*Export modèle : 2 occurrence(s), 13 lignes.*

Champ Code Correspondance/Commentaire
Civilité
1
M.
Mme
Mlle
Nom 35 caractères alphanumériques
Prénom 35 caractères alphanumériques
Service 1 à 30 Position dans la liste des services (paramètres 
société)
Fonction 35 caractères alphanumériques
Téléphone 21 caractères alphanumériques
Portable 21 caractères alphanumériques

Champ Code Correspondance/Commentaire
Télécopie 21 caractères alphanumériques
E-mail 69 caractères alphanumériques
Type contact 1 à 30 Correspond au n° d'index des types de contact
Compte Facebook 35 caractères alphanumériques
Compte LinkedIn 35 caractères alphanumériques
Compte Skype 35 caractères alphanumériques
Doit suivre un #CDEP
Fichier Documents
Les trois fichiers du fichier Document doivent obligatoirement se suivre dans l’ordre défini ci-dessous, 
car ils constituent ensemble un document.
Pour éviter les problèmes lors de l’importation des documents, respectez les règles suivantes :
• Si vous voulez importer des documents des achats, des ventes, des documents internes et 
des stocks, commencez toujours par importer les documents d’entrée en stock (Stock, Interne 
de type Entrée et Achat),
• Dans le cas de l’importation de documents de sortie de stock (BL vente, facture vente, 
mouvement de sortie...) vérifiez auparavant l’état de votre stock.
Lors de l’import des documents il est impossible d’indiquer les informations suivantes :
• les liens d’une ligne de vente avec une ligne d’achat dans les cas d’articles en contremarque.
• les numéros de pièces et dates du bon de commande ou du bon de livraison d’origine.
• la référence à l’abonnement et à la périodicité d’abonnement du document.
En-têtes de documents

## #CHEN — En-têtes de documents
*Export modèle : 74 occurrence(s), 86 lignes.*

Champ Code Correspondance/Commentaire
Domaine
2
4
Vente
Achat
Stock
Interne
Type Si Domaine 1 
(Ventes)
2
4
6
8
Devis
Bon de commande
Préparation de livraison
Bon de livraison
Bon de retour
Bon d’avoir financier
Facture, Facture de retour, Facture d’avoir
Facture comptabilisée
Document compacté
Si Domaine 2 
(Achats)
2
4
6
8
Demande d’achat
Préparation de commande
Bon de commande
Bon de livraison
Bon de retour
Bon d’avoir financier
Facture, facture de retour, facture d’avoir
Facture comptabilisée
Document compacté
Si Domaine 3 
(Stocks)
2
4
6
Mouvement d’entrée
Mouvement de sortie
Dépréciation
Virement dépôt à dépôt
Préparation de fabrication

Champ Code Correspondance/Commentaire
8 Ordre de fabrication
Bon de fabrication
Document compacté
Si Domaine 4 
(Documents 
internes)
2
4
6
8
1er document interne
2ème document interne
3ème document interne
4ème document interne
5ème document interne
6ème document interne
Saisie du réalisé
Document compacté
Provenance Si Domaine 1 
(Ventes)
2
4
Normale
Retour
Avoir
Ticket
Réservé export (1)
Si Domaine 2 
(Achats)
2
4
Normale
Retour
Avoir
Réservé export (1)
Si Domaine 3 
(Stocks)
1 Normale

Champ Code Correspondance/Commentaire
Si Domaine 4 
(Documents 
internes)
1 Normale
Souche 1 à 50 Numéro de la souche de numérotation (si 
Domaine Achat, Vente ou Interne)
N° de pièce 13 caractères alphanumériques majuscules
Date Format Date
Référence 17 caractères alphanumériques
Livraison Format Date
Livraison réalisée Format Date
Date expédition (1) Réservé export (1)
Tiers 17 caractères alphanumériques majuscules ( si 
Domaine Achat, Vente ou Interne)
Dépôt de stockage 35 caractères alphanumériques (pour un virement 
de dépôt à dépôt : dépôt d’origine)
Dépôt de livraison
35 caractères alphanumériques (dépôt de livraison 
du client). (dans le cas d’un virement de dépôt à 
dépôt : dépôt de destination)
Périodicité 1 à 10 Numéro de périodicité (Vente uniquement)
Devise 0 à 32 Numéro de la devise (Achat/Vente)

Champ Code Correspondance/Commentaire
Cours Format Double (Achat/Vente)
Payeur/encaisseur 17 caractères alphanumériques majuscules 
(Achat/Vente/Interne)
Expédition 1 à 50 Numéro du mode d’expédition 
(Achat/Vente/Interne)
Condition livraison 1 à 30 Numéro de condition de livraison 
(Achat/Vente/Interne)
Langue
1
Aucune (Achat/Vente/Interne, vide pour Domaine 
Stock)
Langue 1
Langue 2
Nom représentant 35 caractères alphanumériques (Vente/Interne)
Prénom représentant 35 caractères alphanumériques (Vente/Interne)
Entête 1 25 caractères alphanumériques (Achat/Vente)
Entête 2 25 caractères alphanumériques 
(Achat/Vente/Interne)
Entête 3 25 caractères alphanumériques 
(Achat/Vente/Interne)
Entête 4 25 caractères alphanumériques 
(Achat/Vente/Interne)
Affaire Format compte analytique (Achat/Vente/Interne)
Catégorie tarifaire 1 à 32 Numéro de la catégorie tarifaire (Vente 
uniquement)

Champ Code Correspondance/Commentaire
Régime 0 à 99 2 caractères numériques (Achat/Vente)
Transaction 0 à 99 2 caractères numériques (Achat/vente)
Colisage 0 à 999 Format quantité (Vente uniquement)
Unité colisage 1 à 30 Numéro de colisage (Vente uniquement)
Nbre exemplaires 0 à 99 (Vente, Interne)
1 BL/Facture
1
Plusieurs BL/Fact.
1 BL/Fact
Taux d’escompte Format Double. (Achat/Vente)
Ecart valorisation Format Double. (Achat : facture uniquement)
Catégorie comptable 1 à 50 Numéro de la catégorie comptable
Frais 0
Non ventilé
Ventilé (Achat : FA et FC uniquement)
Statut
1
Statut 1 (Domaine Stock : 0 systématiquement)
Statut 2
Statut 3
Compte général Format Compte
Heure Format Heure
Caisse 35 caractères alphanumériques
Caissier nom 35 caractères alphanumériques

Champ Code Correspondance/Commentaire
Caissier prénom 35 caractères alphanumériques
Clôturé 0
Non
Oui
Numéro de commande 
site marchand 17 caractères alphanumériques
Ventilation IFRS Format Section analytique (Vente/Achat)
Base de calcul frais 
d’expédition
1
3
Montant forfaitaire
Quantité
Poids net
Poids brut
Colisage
Valeur frais d’expédition
Si Base de calcul frais d’expédition est égale à 0
Montant forfaitaire alors format Montant sinon 
format Prix.
14 caractères numériques gérés en fonction du 
type de valeur :
Montant forfaitaire : format Monnaie de tenue commerciale,
Quantité, Poids net, Poids brut, Colisage : format 
Prix unitaire
Type valeur frais 
expédition
1
HT
TTC
Type valeur calcul franco 
de port
1
Montant forfaitaire
Quantité
Valeur franco de port
14 caractères numériques gérés en fonction du 
type de valeur :
Montant forfaitaire : format Monnaie de tenue commerciale,
Quantité : format Prix unitaire

Champ Code Correspondance/Commentaire
Type valeur franco de port 0
HT
TTC
Type calcul frais 
expédition (3)
1
Calcul en valeur
Calcul avec grille fixe
Calcul avec grille variable
Taux taxe 1 (2) Format Double
Type taux taxe 1 (2)
1
Pourcentage
Montant
Quantité
Type de taxe 1 (2)
1
3
5
TVA/débit
TVA/encaissement
TP/HT
TP/TTC
TP/poids
TVA CEE
Surtaxe
Taux taxe 2 (2) Format Double
Type taux taxe 2 (2)
1
Pourcentage
Montant
Quantité
Type de taxe 2 (2)
1
3
5
TVA/débit
TVA/encaissement
TP/HT
TP/TTC
TP/poids
TVA CEE
Surtaxe
Taux taxe 3 (2) Format Double

Champ Code Correspondance/Commentaire
Type taux taxe 3 (2)
1
Pourcentage
Montant
Quantité
Type de taxe 3 (2)
1
3
5
TVA/débit
TVA/encaissement
TP/HT
TP/TTC
TP/poids
TVA CEE
Surtaxe
Motif 35 caractères alphanumériques. Réservé export.
Centrale d’achat 17 caractères alphanumériques
Contact 35 caractères alphanumériques
Facturation électronique
1
Facture
Facture générée
Facture envoyée
Type transaction (1) Réservé Export
Validé 0
VENTE uniquement
Non validée
Validée
N° FA origine 13 caractères alphanumériques (A à Z, 0 à 9)
Code taxe 1 5 caractères alphanumériques (A à Z, 0 à 9)
Code taxe 2 5 caractères alphanumériques (A à Z, 0 à 9)

Champ Code Correspondance/Commentaire
Code taxe 3 5 caractères alphanumériques (A à Z, 0 à 9)
Non soumis à l'escompte 
(4)
1
Soumis
Non Soumis
N° Facture fournisseur 35 caractères alphanumériques
Réservé au domaine achat
Motif devis perdu 0 à 29
Option TVA/Débit 0
Non
Oui
Réservé Facture électronique et disponible 
Sage100 v10.X
Banque 5 caractères alphanumériques majuscules
Réservé Facture électronique et disponible 
Sage100 v10.X
Référence externe 50 caractères alphanumériques
Réservé Facture électronique et disponible 
Sage100 v10.X
Code routage 100 caractères alphanumériques
Réservé Facture électronique et disponible 
Sage100 v10.X
Cadre de facturation 3 caractères alphanumériques
Réservé Facture électronique et disponible 
Sage100 v10.X
Exclure de la transmission 0
Non
Oui
Réservé Facture électronique et disponible 
Sage100 v10.X

Champ Code Correspondance/Commentaire
Code service 100 caractères alphanumériques
Réservé Facture électronique et disponible 
Sage100 v10.X
Flux fiscal 0 à 6
0 à 5 vente
0,1,2,6 achat
et 0 autres
Réservé Facture électronique et disponible 
Sage100 v11.X
Exclure flux encaissement
1
Non
Oui
Réservé Facture électronique et disponible 
Sage100 v11.X
(1) Réservé export : destiné à une version du programme vendue à l’exportation.
(2) Sauf Documents internes.
Certains champs sont réservés à certains types de document seulement (Domaines). Ces champs 
doivent être présents dans tous les cas. Ils sont renseignés s’ils correspondent au type de document 
défini, sinon ils restent à blanc (vides).
Le champ Représentant ne concerne que les documents de ventes. Pour les documents des achats 
et des stocks il faudra le laisser à blanc.
(3) Type calcul frais d’expédition uniquement pour les bases de calcul frais d’expédition Quantité, 
Poids net, Poids brut, Colisage.
(4) pour l’article de frais d’expédition du mode d’expédition.
Grilles d’expédition – Entête document

## #CHGRI — Grilles d’expédition – Entête document
*Absent de l'export modèle — structure non vérifiée sur fichier réel.*

Champ Code Correspondance/Commentaire
Borne Format Double
Frais Format Montant
Indiqué lorsque le mode d’expédition du document utilise une grille pour le mode de calcul des frais 
d’expédition.
Doit obligatoirement suivire le #CHEN

Informations complémentaires eFacture

## #CINC — Informations complémentaires eFacture
*Absent de l'export modèle — structure non vérifiée sur fichier réel.*

Champ Code Correspondance/Commentaire
Code 13 caractères alphanumériques
Intitulé 35 caractères alphanumériques
Type 0
2
Texte
Date
Montant
Valeur
Valeur 35 caractères en fonction du type
Si ce fichier comporte des données liées au Factures dématérialisées, il peut suivre un #CAEN, un 
#CALI, un #CHEN ou #CHLI.
Si ce fichier comporte des données liées au Factures dématérialisées, il peut suivre un #CHEN ou 
#CHLI.
Ces données doivent correspondre aux informations complémentaires enregistrées dans les fiches 
Tiers avec les mêmes codes, domaine et type.
Lignes de documents

## #CHLI — Lignes de documents
*Export modèle : 281 occurrence(s), lignes 62, 64.*

Champ Code Correspondance/Commentaire
Référence ligne 17 caractères alphanumériques
Référence article 18 caractères alphanumériques
Désignation 69 caractères alphanumériques
Texte complémentaire 1980 caractères alphanumériques
+ Retour chariot et Tabulations.
Le Retour chariot doit être codifié par \n
Enuméré de gamme 1 21 caractères alphanumériques.
Obligatoire si article à gamme sinon laisser à blanc.

Champ Code Correspondance/Commentaire
Enuméré de gamme 2 21 caractères alphanumériques.
Obligatoire si article à double gamme sinon laisser 
à blanc.
N° de série & Lot 30 caractères alphanumériques majuscules.
Tous les documents en version 100 Pack Plus tous 
modules sauf :
Devis (Vente),
Préparation de commande (Achat)
Dépréciation (Stock). Uniquement dans les 
documents internes :
Entrée en stock,
Sortie de stock.
Complément série/lot 30 caractères alphanumériques majuscules
Date fabrication Format Date
Date péremption Format Date
Type de prix 0
HT
TTC (Vente uniquement)
Prix unitaire Format Montant
Prix unitaire en devise Format Montant (Achat/Vente/Interne)
Quantité Format Quantité
Quantité colisée Format Quantité (Achat/Vente/Interne)
Conditionnement 35 caractères alphanumériques
Poids net global Format Quantité (A exprimer en grammes)
Poids brut global Format Quantité (A exprimer en grammes)
Remise 45 caractères alphanumériques (0 à 9, +, -, %, F, 
U, f, u) sauf Documents internes
Type de ligne 0
Normale
Remise provenant d’un barème (pied de pièce, 
vente uniquement)
Remise exceptionnelle (Achat/Vente)
Composants (Bon de fabrication/Stock)

Champ Code Correspondance/Commentaire
3
Totalisation
Prix de revient unitaire Format Prix (Vente uniquement)
Vide pour les documents internes de types :
Aucun,
Gain financier,
Perte financière.
Frais Format Montant
CMUP Format Prix
Vide pour les documents internes de types :
Aucun,
Gain financier,
Perte financière.
Provenance facture 0
2
4
Normale
Bon de retour (Achat/vente)
Avoir financier (Achat/vente/Interne)
Rectificative valeur
Rectificative quantité
Nom représentant 35 caractères alphanumériques (Vente/Interne)
Prénom représentant 35 caractères alphanumériques (Vente/Interne)
Date livraison Format Date
Dépôt de stockage 35 caractères alphanumériques
Affaire Format Section analytique
Valorisation 0
Non valorisé
Normale (1 pour les Domaines Achat/Stock/Interne 
sauf ceux de types : Aucun, Entrée en stock, Sortie 
de stock)
Référence composé 18 caractères alphanumériques (Vente/Stock pour 
les types : Préparation de fabrication, Ordre de 
fabrication, Bon de fabrication)
Article non livré 0
Aucune ligne générée pour les articles non livrés
Ligne générée à zéro pour l’article non livré

Champ Code Correspondance/Commentaire
Taux taxe 1 (1) Format Double
Type taux taxe 1 (1) 0
2
Pourcentage
Montant
quantité
Type de taxe 1 (1) 0
2
4
6
TVA/débit
TVA/encaissement
TP/HT
TP/TTC
TP/poids
TVA CEE
Surtaxe
Taux taxe 2 (1) Format Double
Type taux taxe 2 (1) 0
2
Pourcentage
Montant
quantité
Type de taxe 2 (1) 0
2
4
6
TVA/débit
TVA/encaissement
TP/HT
TP/TTC
TP/poids
TVA CEE
Surtaxe
Taux taxe 3 (1) Format Double
Type taux taxe 3 (1) 0
2
Pourcentage
Montant
quantité
Type de taxe 3 (1) 0
2
4
6
TVA/débit
TVA/encaissement
TP/HT
TP/TTC
TP/poids
TVA CEE
Surtaxe
Numéro tiers 17 caractères alphanumériques majuscules

Champ Code Correspondance/Commentaire
Référence fournisseur 18 caractères alphanumériques (sauf Documents 
internes)
Référence client ou
Référence client énuméré 
si article à gamme(s)
18 caractères alphanumériques
Facturation sur le poids net 
(1)
1
Non
Oui
Hors escompte (1) 0
Non
Oui
Numéro de colis 18 caractères alphanumériques
Code ressource 10 caractères alphanumériques majuscules
Quantité ressource Entier supérieur ou égal à 0
Existence agenda 0
Non
Oui
Date avancement Format date
Projet 9 caractères alphanumériques majuscules
Date Format date
Code taxe 1 5 caractères alphanumériques (A à Z, 0 à 9)
Code taxe 2 5 caractères alphanumériques (A à Z, 0 à 9)
Code taxe 3 5 caractères alphanumériques (A à Z, 0 à 9)
N° d'OF Gestion de 
production
9 caractères alphanumériques
N° d'opération 10 caractères alphanumériques
Quantité facture Format Quantité
Ligne de totalisation Entier supérieur ou égal à 0

Champ Code Correspondance/Commentaire
Ligne de totalisation 
associée
Entier supérieur ou égal à 0
Référence externe 50 caractères alphanumériques
Réservé Facture électronique et disponible 
Sage100 v10.X
Code emplacement 13 caractères alphanumériques n fois
Quantité emplacement 1 à 9999 Format Quantité n fois
(1) Sauf Documents internes.
Les informations sur les lignes de document devront obligatoirement se trouver à la suite de l’entête 
du document. Certains champs sont réservés à certains types de document seulement (Domaines). 
Ces champs doivent être présents dans tous les cas. Ils sont renseignés s’ils correspondent au type 
de document défini, sinon ils restent à blanc (vides).
Acomptes / échéances

## #CHRE — Acomptes / échéances
*Export modèle : 73 occurrence(s), 10 lignes.*

Champ Code Correspondance/Commentaire
Type 0
2
Acompte
Bon d’achat
Echéance
Demande d’acompte
Date Format Date
Libellé 35 caractères alphanumériques.
Uniquement si Type=0 sinon laisser à blanc
Montant Format Montant (0 à 9 , %).
Il est possible de saisir, soit un montant, soit un 
pourcentage pour les #CHRE de type 1.
Si #CHRE de type 0 : montant uniquement.
Montant en devise Si #CHRE de type 0 : Format Montant
Mode de règlement 1 à 30 Numéro du mode de règlement
Si #CHRE de type 1 - Echéance uniquement

Champ Code Correspondance/Commentaire
Clôturé 0
Non clôturé
Clôturé
Numéro de pièce 13 caractères alphanumériques
Numéro de pièce facture 
d’acompte
13 caractères alphanumériques
Pourcentage acompte Format double
Ces informations doivent être répétées autant de fois qu’il y a d’acomptes et d’échéances. Les fichiers 
#CHRE sont obligatoirement à la suite des lignes des documents des achats et des ventes.
Informations libres série/lot

## #CIVL — Informations libres série/lot
*Absent de l'export modèle — structure non vérifiée sur fichier réel.*

Champ Code Correspondance/Commentaire
Information libre 1 à 64 69 caractères alphanumériques
Règlements

## #CRGT — Règlements
*Absent de l'export modèle — structure non vérifiée sur fichier réel.*

Champ Code Correspondance/Commentaire
Type de règlement 0
3
5
7
Règlement
Fond de caisse
Remise en banque
Sortie de caisse
Entrée de caisse
Remise à zéro
Contrôle de caisse
Bon d’achat
N° Tiers 17 caractères alphanumériques majuscules
Date Format Date

Champ Code Correspondance/Commentaire
Référence 17 caractères alphanumériques
Libellé 35 caractères alphanumériques
Montant Format Montant
Devise 1 à 32 Numéro de la devise
Cours devise Format Double
Montant en devise Format Montant
Mode de règlement 1 à 30 Numéro du mode de règlement
Etat comptabilisé 0
Non
Oui
Etat validé 0
Non
Oui
Code journal 6 caractères alphanumériques
Compte contrepartie Format Compte
Date impayé Format Date
Compte d'écart de 
règlement (1)
Format Compte
Montant écart de règlement 
(1)
Format Montant (positif ou négatif)
Code journal écart de 
règlement (1)
6 caractères alphanumériques
Compte général Format Compte
N° de pièce 13 caractères alphanumériques
Heure Format Heure
Caisse 35 caractères alphanumériques

Champ Code Correspondance/Commentaire
Caissier nom 35 caractères alphanumériques
Caissier prénom 35 caractères alphanumériques
Mise en banque 0
Non
Oui
Clôturé 0
Non
Oui
Souche 0 à 49 Numéro de souche
Numéro tiers d’origine 17 caractères alphanumériques majuscules
Echéance contrepartie Format Date
Imputé antérieur Montant
(1) Ces informations ne doivent être renseignées que s’il existe un écart de règlement sans quoi les 
laisser vides.
Liens règlements / échéances

## #CREC — Liens règlements / échéances
*Absent de l'export modèle — structure non vérifiée sur fichier réel.*

Champ Code Correspondance/Commentaire
N° pièce 13 caractères alphanumériques
Date Format Date
Montant imputé Format Montant
Fichier des abonnements

Abonnements

## #CABO — Abonnements
*Export modèle : 12 occurrence(s), 44 lignes.*

Champ Code Correspondance/Commentaire
Domaine 0
2
Client
Fournisseur
Interne
Type 0
2
Proposition d’abonnement
Abonnement
Résiliation
Modèle
Tiers 17 caractères alphanumériques majuscules
Modèle 10 caractères alphanumériques majuscules
Intitulé 35 caractères alphanumériques
Contrat 35 caractères alphanumériques
Périodicité 3 caractères numériques
Type périodicité 0
2
4
Jour
Semaine
Mois
Année
Mois civil
Année civile
Durée 3 caractères numériques
Type durée 0
2
4
Jour
Semaine
Mois
Année
Mois civil
Année civile
Date début Format Date
Date fin Format Date
Date résiliation Format Date
Motif résiliation 1 à 30 Numéro du motif de résiliation

Champ Code Correspondance/Commentaire
Délai préavis 3 caractères numériques
Type délai préavis 0
2
Jour
Semaine
Mois
Année
Date fin résiliation Format Date
Reconduction 0
2
Aucune
Tacite
A confirmer
Pièce générée Pour les ventes
1
3
5
Devis
Préparation de livraison
Bon de commande
Bon de livraison
Bon de retour
Bon d’avoir financier
Facture
Pour les achats
1
3
5
Demande d’achat
Préparation de commande
Bon de commande
Bon de livraison
Bon de retour
Bon d’avoir financier
Facture
Souche 0 à 49 Numéro de la souche sur laquelle sera généré le 
document
Génération 4 caractères numériques
Type génération 0
Date début
Date fin
Jour tombée génération 1 0 à 31
Jour tombée génération 2 0 à 31

Champ Code Correspondance/Commentaire
Jour tombée génération 3 0 à 31
Jour tombée génération 4 0 à 31
Jour tombée génération 5 0 à 31
Jour tombée génération 6 0 à 31
Livraison 4 caractères numériques
Type livraison 0
Date début
Date fin
Jour tombée livraison 1 0 à 31
Jour tombée livraison 2 0 à 31
Jour tombée livraison 3 0 à 31
Jour tombée livraison 4 0 à 31
Jour tombée livraison 5 0 à 31
Jour tombée livraison 6 0 à 31
En-tête 0
Modèle
Fiche client
Catégorie tarifaire 0
Modèle
Fiche client
Remise 0
Modèle
Fiche client
Catégorie comptable 0
Modèle
Fiche client
Représentant 0
Modèle
Fiche client
Dépôt 0
Modèle
Fiche client

Champ Code Correspondance/Commentaire
Escompte 0
Modèle
Fiche client
Condition échéance 0
Modèle
Fiche client
Contact 0
Modèle
Aucun
Historique et périodicité de l’abonnement

## #CAPE — Historique et périodicité de l’abonnement
*Export modèle : 46 occurrence(s), 5 lignes.*

Champ Code Correspondance/Commentaire
Etat périodicité 0
2
Périodicité générée
Périodicité non générée
Périodicité suspendue
Renouvellement
Début périodicité Format Date
Fin périodicité Format Date
Génération Format Date
Livraison Format Date
En-tête des abonnements

## #CAEN — En-tête des abonnements
*Export modèle : 12 occurrence(s), 35 lignes.*

Champ Code Correspondance/Commentaire
Référence 17 caractères alphanumériques
Dépôt de stockage 35 caractères alphanumériques
Dépôt de livraison 35 caractères alphanumériques
Périodicité 1 à 10 Numéro de la périodicité

Champ Code Correspondance/Commentaire
Devise 0 à 32 Numéro de la devise
Cours Format Double
Compte payeur 17 caractères alphanumériques majuscules
Expédition 1 à 50 Numéro du mode d’expédition
Condition livraison 1 à 30 Numéro de la condition de livraison
Langue 0
2
Aucune
Langue 1
Langue 2
Nom représentant 35 caractères alphanumériques
Prénom représentant 35 caractères alphanumériques
En-tête 1 25 caractères alphanumériques
En-tête 2 25 caractères alphanumériques
En-tête 3 25 caractères alphanumériques
En-tête 4 25 caractères alphanumériques
Affaire Format Section analytique
Catégorie tarifaire 1 à 32 Numéro de la catégorie tarifaire
Régime 0..99 2 caractères numériques
Transaction 0..99 2 caractères numériques
Colisage 0..99 3 caractères numériques
Type colisage 1 à 30 Numéro de l’unité achat/vente
Nbre factures 0..99 2 caractères numériques
1 BL/Facture 0
Non
Oui

Champ Code Correspondance/Commentaire
Taux d’escompte Format Double
Catégorie comptable 1 à 50 Numéro de la catégorie comptable
Base calcul échéances 0
2
Date document
Date début périodicité
Date fin périodicité
Compte général 13 caractères alphanumériques majuscules
Ventilation IFRS Format Section analytique
Centrale d’achat 17 caractères alphanumériques
Contact 35 caractères alphanumériques
Banque 5 caractères alphanumériques majuscules
Réservé Facture électronique et disponible 
Sage100 v10.X
Référence externe 50 caractères alphanumériques
Réservé Facture électronique et disponible 
Sage100 v10.X
Code routage 100 caractères alphanumériques
Réservé Facture électronique et disponible 
Sage100 v10.X
Code service 100 caractères alphanumériques
Réservé Facture électronique et disponible 
Sage100 v10.X
Lignes d’abonnement

## #CALI — Lignes d’abonnement
*Export modèle : 40 occurrence(s), 52 lignes.*

Champ Code Correspondance/Commentaire
Référence ligne 17 caractères alphanumériques

Champ Code Correspondance/Commentaire
Référence article 18 caractères alphanumériques
Désignation 69 caractères alphanumériques
Texte complémentaire 1980 caractères alphanumériques
+ Retour chariot et Tabulations.
Le Retour chariot doit être codifié par \n
Enuméré de gamme 1 21 caractères alphanumériques.
Obligatoire si article à gamme sinon laisser à blanc.
Enuméré de gamme 2 21 caractères alphanumériques.
Obligatoire si article à double gamme sinon laisser 
à blanc.
Type de prix 0
HT
TTC (Vente uniquement)
Prix unitaire Format Montant
Prix unitaire en devise Format Montant (Achat/Vente)
Quantité Format Quantité
Quantité colisée Format Quantité (Achat/vente)
Conditionnement 35 caractères alphanumériques
Poids net global Format Quantité (A exprimer en grammes)
Poids brut global Format Quantité (A exprimer en grammes)
Remise 45 caractères alphanumériques (0..9 ,+ ,- , %, F, U, 
f, u)
Type de ligne 0
2
Normale
Remise provenant d’un barème (Vente 
uniquement)
Ligne de remise (Achat/Vente)
Composants (Bon de fabrication/Stock)
Prix de revient unitaire Format Montant

Champ Code Correspondance/Commentaire
CMUP Format Montant
Nom représentant 35 caractères alphanumériques (Vente 
uniquement)
Prénom représentant 35 caractères alphanumériques (Vente 
uniquement)
Dépôt de stockage 35 caractères alphanumériques
Affaire Format Section analytique
Périodicité 0
2
Toutes
Unique
Date
Nb périodes 0 à 99
Début périodicité Format Date (si Périodicité = 2)
Fin périodicité Format Date (si Périodicité = 2)
Gestion de l’année 0
Non
Oui
Gestion prorata 0
2
4
Aucun
Quantité
Valeur
Quantité totale
Valeur totale
Reconduction 0
Non
Oui
Valorisation 0
Non valorisé
Normale (1 si Domaine Achat / Stock)
Référence composé 18 caractères alphanumériques (Vente 
uniquement)
Taux taxe 1 Format Double

Champ Code Correspondance/Commentaire
Type taux taxe 1 0
2
Pourcentage
Montant
Quantité
Type de taxe 1 0
2
4
6
TVA/débit
TVA/encaissement
TP/HT
TP/TTC
TP/poids
TVA/CEE
Surtaxe
Taux taxe 2 Format Double
Type taux taxe 2 0
2
Pourcentage
Montant
Quantité
Type de taxe 2 0
2
4
6
TVA/débit
TVA/encaissement
TP/HT
TP/TTC
TP/poids
TVA/CEE
Surtaxe
Taux taxe 3 Format Double
Type taux taxe 3 0
2
Pourcentage
Montant
Quantité
Type de taxe 3 0
2
4
6
TVA/débit
TVA/encaissement
TP/HT
TP/TTC
TP/poids
TVA/CEE
Surtaxe
Référence fournisseur 18 caractères alphanumériques

Champ Code Correspondance/Commentaire
Référence client ou
Référence client énuméré 
si article à gamme(s)
18 caractères alphanumériques
Facturation sur le poids 
net
1
Non
Oui
Hors escompte 0
Non
Oui
Code ressource 10 caractères alphanumériques majuscules
Quantité ressource Entier supérieur ou égal à 0
Code taxe 1 5 caractères alphanumériques (A à Z, 0 à 9)
Code taxe 2 5 caractères alphanumériques (A à Z, 0 à 9)
Code taxe 3 5 caractères alphanumériques (A à Z, 0 à 9)
Ligne de totalisation Entier supérieur ou égal à 0
Ligne de totalisation 
associée
Entier supérieur ou égal à 0
Référence externe 50 caractères alphanumériques
Réservé Facture électronique et disponible 
Sage100 v10.X
Conditions de règlement de l’abonnement

## #CARG — Conditions de règlement de l’abonnement
*Export modèle : 5 occurrence(s), 11 lignes.*

Champ Code Correspondance/Commentaire
Mode de règlement 1 à 30 N° du mode de règlement
Condition 0
2
Jours nets
Fin de mois civil
Fin de mois

Champ Code Correspondance/Commentaire
Nombre de jours 0 à 999
Jour de tombée 1 0 à 31
Jour de tombée 2 0 à 31
Jour de tombée 3 0 à 31
Jour de tombée 4 0 à 31
Jour de tombée 5 0 à 31
Jour de tombée 6 0 à 31
Type répartition 0
2
Pourcentage
Equilibre
Montant
Valeur répartition Format Montant
Modèles d’enregistrement

## #CMOD — Modèles d’enregistrement
*Absent de l'export modèle — structure non vérifiée sur fichier réel.*

Champ Code Correspondance/Commentaire
Intitulé 35 caractères alphanumériques
Formule de calcul 1980 caractères alphanumériques
Ressources

## #CRESPROD — Ressources
*Export modèle : 18 occurrence(s), lignes 58, 59, 60.*

Champ Code Correspondance/Commentaire
Code 10 caractères alphanumériques majuscules
Type 0
Machine
Homme

Champ Code Correspondance/Commentaire
3
Outil
Centralisateur
Intitulé 69 caractères alphanumériques
Complément 69 caractères alphanumériques
Centralisation 10 caractères alphanumériques majuscules
Date prochaine révision Format Date
Coût horaire standard Format Montant
Temps d’utilisation Format Heure
Mise en sommeil 0
Non
Oui
Commentaire 69 caractères alphanumériques
Capacité Nombre entier strictement supérieur à 0
Date de création Format date
Type ressource/centre 0
Ressource
Centre
Code externe 30 caractères alphanumériques
Dépôt 35 caractères alphanumériques
Adresse 35 caractères alphanumériques
Complément adresse 35 caractères alphanumériques
Code postal 9 caractères alphanumériques
Ville 35 caractères alphanumériques
Région 35 caractères alphanumériques
Pays 35 caractères alphanumériques

Champ Code Correspondance/Commentaire
Téléphone 21 caractères alphanumériques
Portable 21 caractères alphanumériques
Mail 69 caractères alphanumériques
Unité 1 à 30
Utilisation continue 0
Non
Oui
Calendrier 35 caractères alphanumériques
Plage 1 heure début Format de temps (apparaît 7 fois)
Plage 1 heure fin Format de temps (apparaît 7 fois)
Plage 2 heure début Format de temps (apparaît 7 fois)
Plage 2 heure fin Format de temps (apparaît 7 fois)
Compte Facebook 35 caractères alphanumériques
Compte LinkedIn 35 caractères alphanumériques
Compte Skype 35 caractères alphanumériques
Ressource / centre associé 10 caractères alphanumériques majuscules (1)
(1) Cette ligne doit être répétée autant de fois que de centres associés.
Ressources / Articles

## #CRESART — Ressources / Articles
*Export modèle : 16 occurrence(s), lignes 1, 2.*

Champ Code Correspondance/Commentaire
Article défaut C39 (18)
Article C39 (18) n fois

Projet

## #CPROJFAB — Projet
*Export modèle : 5 occurrence(s), 10 lignes.*

Champ Code Correspondance/Commentaire
Type 0
Fabrication
Affaire
Numéro 9 caractères alphanumériques majuscules
Statut 0
2
Saisi
Validé
En attente
Terminé
Intitulé 69 caractères alphanumériques
Dépôt 35 caractères alphanumériques
Affaire 13 caractères alphanumériques majuscules
Date début Format date
Date fin Format date
Numéro de pièce 13 caractères alphanumériques majuscules
Client 17 caractères alphanumériques
Projet ligne

## #CPROJLIG — Projet ligne
*Export modèle : 1 occurrence(s), 5 lignes.*

Champ Code Correspondance/Commentaire
Numéro de pièce 13 caractères alphanumériques majuscules
Article 18 caractères alphanumériques
Gamme 1 21 caractères alphanumériques
Gamme 2 21 caractères alphanumériques

Champ Code Correspondance/Commentaire
Quantité Format Quantité
Projet planning

## #CPROJPLAN — Projet planning
*Export modèle : 92 occurrence(s), 27 lignes.*

Champ Code Correspondance/Commentaire
Type 0
2
Composé
Opération
Composant
Ressource
Composé 18 caractères alphanumériques
Gamme 1 composé 21 caractères alphanumériques
Gamme 2 composé 21 caractères alphanumériques
Opération 10 caractères alphanumériques
Composant 18 caractères alphanumériques
Gamme 1 composant 21 caractères alphanumériques
Gamme 2 composant 21 caractères alphanumériques
Ressource 10 caractères alphanumériques majuscules
Intitulé 69 caractères alphanumériques
Quantité Format Quantité
Temps Format temps
Prix unitaire Format prix
Date début Format date
Date fin Format date

Champ Code Correspondance/Commentaire
Dépôt 35 caractères alphanumériques
Elément ajouté 0
Non
Oui
Sous-traitance 0
Non
Oui
Chevauchement 0
Non
Oui
Démarre 0
2
A la fin de
Au cours de
En même temps que
Opération chevauchement 10 caractères alphanumériques
Valeur chevauchement Nombre réel (14 caractères)
Type chevauchement 0
Unité
Pourcentage
Type nomenclature 0
Fixe
Variable
Heure début Format date
Heure fin Format date
Coût standard Format montant
Projet historique

## #CPROJHISTO — Projet historique
*Export modèle : 23 occurrence(s), 18 lignes.*

Champ Code Correspondance/Commentaire
Date Format date
Quantité réalisée Format quantité
Temps réalisé Format temps

Champ Code Correspondance/Commentaire
Domaine 0
2
Aucun
Achats
Stocks
Numéro de pièce 13 caractères alphanumériques majuscules
Intitulé 69 caractères alphanumériques
Type 0
2
4
Réservation
Commande fournisseur
Sortie de stock
Entrée en stock
Ressource
Rebut
Composé 18 caractères alphanumériques
Gamme 1 composé 21 caractères alphanumériques
Gamme 2 composé 21 caractères alphanumériques
Opération 10 caractères alphanumériques
Composant 18 caractères alphanumériques
Gamme 1 composant 21 caractères alphanumériques
Gamme 2 composant 21 caractères alphanumériques
Ressource 10 caractères alphanumériques
Type planning 0
2
Composé
Opération
Composant
Ressource
Quantité réservée Format quantité
Coût réalisé Format montant
Billet/Pièces

## #CBIL — Billet/Pièces
*Absent de l'export modèle — structure non vérifiée sur fichier réel.*

Champ Code Correspondance/Commentaire
Devise 1 à 32
Intitulé 35 caractères alphanumériques
Valeur Format double 4 décimales
Afficheur

## #CAFF — Afficheur
*Absent de l'export modèle — structure non vérifiée sur fichier réel.*

Champ Code Correspondance/Commentaire
Action 0 
2
4
6
Ouverture caisse
Validation ligne
Fin de ticket
Mode de règlement
Rendu
Validation document
Caisse fermée
Cadrage 0
2
Gauche
Droite
Centré
Texte 69 caractères alphanumériques
Caisse

## #CCAI — Caisse
*Absent de l'export modèle — structure non vérifiée sur fichier réel.*

Champ Code Correspondance/Commentaire
Intitulé 35 caractères alphanumériques
Dépôt 35 caractères alphanumériques
Caissier nom 35 caractères alphanumériques

Champ Code Correspondance/Commentaire
Caissier prénom 35 caractères alphanumériques
Vendeur nom 35 caractères alphanumériques
Vendeur prénom 35 caractères alphanumériques
Client comptoir 17 caractères alphanumériques
Code journal 6 caractères alphanumériques
Identifier le caissier 0
Non
Oui
Ecran de saisie 1 à 10
Paramètre clavier 1 à 10
Nombre de lignes 0 à 999
Nombre de colonnes 0 à 999
Date création Format Date
Imprimer le ticket 0
Non
Oui
Saisie du vendeur 
obligatoire
1
Non
Oui
Souche 0 à 49 Numéro de souche
Caissier nom (1) 35 caractères alphanumériques
Caissier prénom (1) 35 caractères alphanumériques
(1)Les deux dernières lignes apparaissent autant de fois que le nombre de caissiers attachés à la 
caisse sans tenir compte du caissier par défaut.
Le nom et le prénom du caissier par défaut se trouvent en 3ème et 4ème lignes du fichier
Afficheur caisse

## #CAFC — Afficheur caisse
*Absent de l'export modèle — structure non vérifiée sur fichier réel.*

Champ Code Correspondance/Commentaire
Action 0 
2
4
Ouverture caisse
Validation ligne
Fin de ticket
Mode de règlement
Rendu
Validation document
Cadrage 0
2
Gauche
Droite
Centré
Texte 69 caractères alphanumériques
Clavier

## #CRAC — Clavier
*Export modèle : 7 occurrence(s), 9 lignes.*

Champ Code Correspondance/Commentaire
Clavier 1 à 10
Fonction 0
2
4
Commande
Vendeur
Article
Devise
Mode de règlement
Intéressé Si Fonction = 0 commande alors de 1 à 47
Si Fonction = 3 Devise alors de 1 à 32
Si Fonction = 4 Mode de règlement alors de 1 à 30
Sinon O
Article Si Fonction = 2 Article alors 18 caractères 
alphanumériques sinon vide
Vendeur Nom Si Fonction = 1 Vendeur alors 35 caractères 
alphanumériques sinon vide

Champ Code Correspondance/Commentaire
Vendeur Prénom Si Fonction = 1 Vendeur alors 35 caractères 
alphanumériques sinon vide
Raccourci
Touche de contrôle
Affichage 0
Non
Oui
Ticket

## #CTIA — Ticket
*Absent de l'export modèle — structure non vérifiée sur fichier réel.*

Champ Code Correspondance/Commentaire
Type 0
Ticket
Ticket archivé
Caisse 35 caractères alphanumériques
Caissier nom 35 caractères alphanumériques
Caissier prénom 35 caractères alphanumériques
N° de pièce 13 caractères alphanumériques
Date Format Date
Heure Format Heure
Catégorie tarifaire 1 à 32
Vendeur Nom 35 caractères alphanumériques
Vendeur Prénom 35 caractères alphanumériques
N° de pièce facture 13 caractères alphanumériques
Client 17 caractères alphanumériques

Le numéro de pièce facture et le client ne sont renseignés que pour les articles archivés.
Ligne ticket (ou archive ticket)

## #CLIA — Ligne ticket (ou archive ticket)
*Absent de l'export modèle — structure non vérifiée sur fichier réel.*

Champ Code Correspondance/Commentaire
Référence article 18 caractères alphanumériques
Désignation 69 caractères alphanumériques
Type de prix 0
HT
TTC
Prix unitaire Format Prix
Quantité Format Quantité
Quantité colisée Format Quantité
Conditionnement 35 caractères alphanumériques
Remise 45 caractères alphanumériques + symboles des 
remises (+,-,%,F,U,f,u)
Enuméré gamme 1 21 caractères alphanumériques
Enuméré gamme 2 21 caractères alphanumériques
Numéro de série/lot 30 caractères alphanumériques
Complément série/lot 30 caractères alphanumériques
Poids net global Format Double (exprimé en grammes)
Nom vendeur 35 caractères alphanumériques
Prénom vendeur 35 caractères alphanumériques
Type de ligne 0
Normal
Remise exceptionnelle
Prix de revient unitaire Format Prix

Champ Code Correspondance/Commentaire
CMUP Format Prix
Taux taxe 1 Format Double
Type taux taxe 1 0
2
Pourcentage
S
U
Type de taxe 1 0
2
4
6
TVA/débit
TVA/encaissement
TP/HT
TP/TTC
TP/poids
TVA/CEE
Surtaxe
Taux taxe 2 Format Double
Type taux taxe 2 0
2
Pourcentage
S
U
Type de taxe 2 0
2
4
6
TVA/débit
TVA/encaissement
TP/HT
TP/TTC
TP/poids
TVA/CEE
Surtaxe
Taux taxe 3 Format Double
Type taux taxe 3 0
2
Pourcentage
S
U
Type de taxe 3 0
2
4
6
TVA/débit
TVA/encaissement
TP/HT
TP/TTC
TP/poids
TVA/CEE
Surtaxe
Facturation sur le poids 
net
1
Non
Oui

Champ Code Correspondance/Commentaire
Hors escompte 0
Non
Oui
Valorisation 0
Non
Oui
Code taxe 1 5 caractères alphanumériques (A à Z, 0 à 9)
Code taxe 2 5 caractères alphanumériques (A à Z, 0 à 9)
Code taxe 3 5 caractères alphanumériques (A à Z, 0 à 9)
Règlement ticket

## #CRGA — Règlement ticket
*Absent de l'export modèle — structure non vérifiée sur fichier réel.*

Champ Code Correspondance/Commentaire
Montant règlement Format Montant
Devise règlement 0 à 32 Numéro de la devise
Montant devise règlement Format Montant devise
Mode règlement 0 à 30 Numéro du mode de règlement
Date Format Date
Caisse 35 caractères alphanumériques
