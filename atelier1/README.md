# Atelier 1 - Sources d'un modèle prédictif de trafic

*Mateo LALANNE DE MIRAS* et *Samuel RESSIOT*

## Projet de Data Lake avec DuckDB

Pour établir un modèle prédictif de trafic sur la rocade bordelaise, nous devons constituer un jeu de données
d'entrainement. L'atelier consiste à identifier, qualifier et ingérer les sources d'information qui composeront ce
jeu de données dans un datalake.

### Étape 1 - Périmètre d'analyse

Nous avons établi la liste suivante de facteurs pouvant influer sur le trafic routier de la rocade bordelaise. Nous en avons relevé 14. Voici la liste dans un ordre décroissant d'importance :

- Gonflement de l'argile du sol (peut mener à des travaux)
- Stations de vélo en temps réel (peut donner une indication du trafic)
- Passages et franchissements en temps réel
- Points autopartage
- Points covoiturage
- Agenda de Bordeaux Métropole
- Arrêtés municipaux de Bordeaux
- Calendrier scolaire
- Radars
- Ouverture du pont Chaban Delmas
- Temps de parcours en temps réel
- Évenements de circulation
- Travaux
- État du trafic en temps réel

### Étape 2 - Soucres de données

Nous avons choisi de prendre nos données sur le site <https://opendata.bordeaux-metropole.fr>.

Nous récupérons les données au format `.csv`.

Nous avons un dossier `sources` qui contient tous ces fichiers.

### Étape 3 - Ingestion dans un datalake

Nous installons le module python `duckdb`.

Nous ouvrons une [connexion persistante](https://duckdb.org/docs/api/python/overview.html#persistent-storage) avec

```python
with duckdb.connect(db_file) as conn :
```

ce qui nous permet de stocker les données dans un fichier permanent et non en mémoire uniquement.

Notre code contient ensuite une boucle qui récupère tous les fichiers du dossier `sources` et qui intègre les données dans notre datalake.

## Description précise du projet

Ce projet implémente un simple data lake en utilisant DuckDB. Il permet d'ingérer automatiquement des fichiers CSV stockés dans un dossier `sources` dans une base de données DuckDB.

### Fonctionnement

Le script principal `import.py` effectue les opérations suivantes :

1. Parcourt tous les fichiers dans le dossier `sources`.
2. Pour chaque fichier CSV trouvé :
   - Crée une table dans la base de données DuckDB avec le même nom que le fichier (sans l'extension).
   - Importe les données du CSV dans la table créée.
   - Affiche le nombre de lignes insérées et un aperçu des 5 premières lignes.

### Prérequis

- Python 3.12
- DuckDB

### Installation

1. Clonez ce dépôt :

   ```shell
   git clone https://github.com/BlaCkMatiK/collecte_donnees_a1.git
   cd collecte_donnees_a1
   ```

2. Création de l'environnement virtuel :

   ```python
   python -m venv env
   env/bin/activate
   ```

3. Installez les dépendances :

   ```shell
   pip install requirements.txt
   ```

## Utilisation

1. Placez vos fichiers CSV dans le dossier 'sources' à la racine du projet.

2. Exécutez le script d'importation :

   ```shell
   python import.py
   ```

3. Les données seront importées dans la base de données `datalake.db`.
