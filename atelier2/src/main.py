import requests
from bs4 import BeautifulSoup

from scripts.urls import urls

# url = 'https://www.bordeaux-tourisme.com/ville-patrimoine/musees.html'

for url in urls:
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        div = soup.find('div', class_='ListSit-wrapper')
        links = div.find_all('a') if div else []

        for link in links:
            href = link.get('href')
            full_url = href if href.startswith('http') else url + href

            new_response = requests.get(full_url)
            if new_response.status_code == 200:
                new_soup = BeautifulSoup(new_response.text, 'html.parser')
                
                # Utilisez new_soup pour extraire les données de la nouvelle page
                data = new_soup.find_all(class_='SitMap-content')
                if data:
                    for item in data:
                        # print(f'Données de {full_url}: {item.get_text(strip=True)}')
                        print(f'{item.get_text(strip=True)}')
                else:
                    print(f'Aucune donnée trouvée sur {full_url}')
            else:
                print(f"Erreur lors de la récupération de {full_url}: {new_response.status_code}")
    else:
        print(f"Erreur lors de la récupération de la page principale : {response.status_code}")
