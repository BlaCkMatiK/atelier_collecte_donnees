import requests
import duckdb
from bs4 import BeautifulSoup
from scripts.urls import urls
from urllib.parse import urlparse

db_file = "datalake.db"

for url in urls:
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        div = soup.find('div', class_='ListSit-wrapper')
        links = div.find_all('a') if div else []

        for link in links:

            path = urlparse(url).path
            # Séparer le chemin en segments et prendre le premier mot utile
            title = path.split('/')[-1].replace('.html', '').replace('-', '_')

            href = link.get('href')
            full_url = href if href.startswith('http') else url + href

            new_response = requests.get(full_url)
            if new_response.status_code == 200:
                new_soup = BeautifulSoup(new_response.text, 'html.parser')
                
                # Extraire le contenu de l'élément <address>
                address = new_soup.find('address')
                if address:
                    # Récupérer tout le texte dans <address> (y compris les <br> et autres balises)
                    address_text = address.get_text(separator=" ", strip=True)
                    print(f"Adresse complète : {address_text}")

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
                else:
                    print(f'Aucune adresse trouvée sur {full_url}')
            else:
                print(f"Erreur lors de la récupération de {full_url}: {new_response.status_code}")
    else:
        print(f"Erreur lors de la récupération de la page principale : {response.status_code}")
