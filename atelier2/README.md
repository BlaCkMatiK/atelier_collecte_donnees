# Atelier 2 - Collecte en ligne (scraping)

*Mateo LALANNE DE MIRAS* et *Samuel RESSIOT*

## Projet de Scrapping avec Requests et BeautifulSoup4

Afin d'enrichir nos données avec des informations touristiques, nous décidons de collecter des données
directement sur le site [Bordeaux Tourisme](https://www.bordeaux-tourisme.com) (nous supposons que ces informations ne sont pas disponibles en open data).

### Étape 1 - Aspect légal

**Nous ne scrappons pas :**

- les données NON publiques, qui nécessiteraient de contourner les mécanismes de sécurité (CAPTCHAs, logins, ...)
- les contenus protégés par droit d'auteur
- les contenus exclus aux robots (robots.txt)
- les données en dehors des conditions d'utilisation
- les données dans un but malveillant

### Étape 2 - Structure du projet

Le fichier `ingest/main.py` contient le script principal. Il récupère une liste d'urls présente dans le fichier `ingest/urls.py`.

On écrit ensuite dans la base de données `datalake.db` présenta à la racine de l'atelier général.

### Étape 3 - Récupération d'une liste

Nous utilisons une combinaison de requests et BeautifulSoup pour récupérer une liste d'éléments d'une page web.

Nous donnons à notre script une liste d'urls du site [Bordeaux Tourisme](https://www.bordeaux-tourisme.com), et nous récupérons chaque lien du type de la page. Par exemple, sur la page musées, nous récupérons tous les liens de musées.

```python
response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        div = soup.find('div', class_='ListSit-wrapper')
        links = div.find_all('a') if div else []
```

Le code ci dessus, permet de récupérer une liste de tous les liens présents dans la div qui présente des *cards* de tous les musées.

### Étape 4 - Exploration de lien

```python
for link in links:
            href = link.get('href')
            full_url = href if href.startswith('http') else url + href

            new_response = requests.get(full_url)
            if new_response.status_code == 200:
                new_soup = BeautifulSoup(new_response.text, 'html.parser')
                
                address = new_soup.find('address')
```

Le code ci dessus parcours chaque lien de la *nouvelle* liste, et récupère l'adresse présente dans le tag `<adress>`

### Étape 5 - Intégration des données

```python
with duckdb.connect(db_file) as conn:
                        conn.execute(f"""
                            CREATE TABLE IF NOT EXISTS "{title}" (
                                url TEXT,
                                address TEXT
                            );
                        """)

                        # Insertion de l'URL et de l'adresse dans la table
                        conn.execute(f"""
                            INSERT INTO "{title}" (url, address) VALUES (?, ?)
                        """, (full_url, address_text))
```

Le code ci dessus, crée un table en fonction de l'url de la page.

Par exemple, pour <https://www.bordeaux-tourisme.com/nature/parcs-jardins>, la table générée sera parcs-jardins.
