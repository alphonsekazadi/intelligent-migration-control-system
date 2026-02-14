# Projet_3 — Analyse des données migratoires et modèle de risque

Description
-----------
Ce dépôt contient un petit projet d'analyse des données migratoires et d'entraînement d'un modèle de risque (classification/régression selon les notebooks). Le projet inclut des notebooks exploratoires, un script d'application minimal (`app.py`) et les données brutes.

Contenu principal
-----------------
- `donnees_migratoires_mbujimayi.csv` : jeu de données principal (données migratoires pour Mbuji-Mayi).
- `modele_risque.ipynb` et `modele_risque-Copy1.ipynb` : notebooks Jupyter montrant l'analyse, le pré-traitement et l'entraînement du/des modèles.
- `app.py` : script d'application minimal (ex. API ou démonstration). Vérifiez le contenu avant d'exposer en production.

Objectifs
---------
- Nettoyer et explorer les données migratoires.
- Construire et évaluer un modèle de risque (classification ou régression selon l'objectif des notebooks).
- Fournir un point d'entrée simple (`app.py`) pour tester le modèle ou exposer une API.

Installation (environnement Python)
----------------------------------
1. Créez et activez un environnement virtuel (PowerShell) :

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Installez les dépendances :

```powershell
pip install -r requirements.txt
```

Utilisation rapide
------------------
- Pour lancer les notebooks :

```powershell
jupyter notebook
```

- Pour exécuter le script d'application localement :

```powershell
python app.py
```

Notes importantes
-----------------
- Les notebooks contiennent l'ordre des opérations : exploration, pré-traitement, sélection de caractéristiques, entraînement et évaluation.
- Avant de publier `app.py` en production, vérifiez la gestion des secrets, l'entrée/sortie et effectuez des tests de charge.
- Si vos données sont volumineuses ou sensibles, ne les commitez pas dans le dépôt public ; utilisez un stockage sécurisé.

Contribuer
----------
1. Forkez le dépôt.
2. Créez une branche de travail : `feature/ma-fonctionnalite`.
3. Ouvrez une pull request décrivant les changements.

Licence
-------
Ajoutez ici la licence souhaitée (par ex. MIT) ou contactez l'auteur si vous n'êtes pas sûr.

Contact
-------
Pour toute question ou suggestion, contactez l'auteur du projet.

