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
                
                # Extraire le contenu de l'élément <address>
                address = new_soup.find('address')
                if address:
                    # Récupérer tout le texte dans <address> (y compris les <br> et autres balises)
                    address_text = address.get_text(separator=" ", strip=True)
                    print(f"Adresse complète : {address_text}")
                else:
                    print(f'Aucune adresse trouvée sur {full_url}')
            else:
                print(f"Erreur lors de la récupération de {full_url}: {new_response.status_code}")
    else:
        print(f"Erreur lors de la récupération de la page principale : {response.status_code}")
