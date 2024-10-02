# Projet de Data Lake avec DuckDB

## Description

Ce projet implémente un simple data lake en utilisant DuckDB. Il permet d'ingérer automatiquement des fichiers CSV stockés dans un dossier 'sources' dans une base de données DuckDB.

## Fonctionnement

Le script principal `import.py` effectue les opérations suivantes :

1. Parcourt tous les fichiers dans le dossier 'sources'.
2. Pour chaque fichier CSV trouvé :
   - Crée une table dans la base de données DuckDB avec le même nom que le fichier (sans l'extension).
   - Importe les données du CSV dans la table créée.
   - Affiche le nombre de lignes insérées et un aperçu des 5 premières lignes.

## Prérequis

- Python 3.12
- DuckDB

## Installation

1. Clonez ce dépôt :
   ```
   git clone https://github.com/BlaCkMatiK/collecte_donnees_a1.git
   cd collecte_donnees_a1
   ```

2. Création de l'environnement virtuel :
   ```
   python -m venv env
   env/bin/activate
   ```

3. Installez les dépendances :
   ```
   pip install requirements.txt
   ```

## Utilisation

1. Placez vos fichiers CSV dans le dossier 'sources' à la racine du projet.

2. Exécutez le script d'importation :
   ```
   python import.py
   ```

3. Les données seront importées dans la base de données 'datalake.db'.