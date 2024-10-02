import requests
from bs4 import BeautifulSoup

from scripts.urls import urls

# url = 'https://www.bordeaux-tourisme.com/ville-patrimoine/musees.html'

for url in urls:
    response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    card_titles = soup.find_all('p', class_='Card-title')
    
    for card in card_titles:
        print(card.get_text(strip=True))  
else:
    print(f"Erreur lors de la récupération de la page : {response.status_code}")
