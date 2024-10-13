# Atelier 3 - Préparation des données

*Mateo LALANNE DE MIRAS* et *Samuel RESSIOT*

## Projet de transformation de données avec dbt

Dans la continuité des deux précédents ateliers, vous amorcer une préparation des données (nettoyage,
consolidation, ...) selon une architecture en médaillon avec dbt. Vous pouvez vous appuyer sur les commits de
l'ébauche de projet <https://github.com/labasse/dbt-park-bx>.

### Étape 1 - Lancement du projet
```bash
cd transform
dbt run
```

### Étape 2 - Création du schéma
```bash
dbt docs build
```

### Étape 3 - Lancement du serveur en localhost
```bash
dbt docs serve
```