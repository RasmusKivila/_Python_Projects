#UPPGIFT 1
import requests

API_KEY = '68bbf8aed81c35ecfecb666dd5a55418'

url = f'https://api.openweathermap.org/data/2.5/forecast?q=Stockholm&appid={API_KEY}'
response = requests.get(url)

if response.status_code == 200:
    data = response.json()

#Hämta vädret för dagarna
    for weather in data['list']:
        date = weather['dt_txt'].split()[0]
        description = weather['weather'][0]['description']
        temperature = round(weather['main']['temp'] - 273.15, 1) 
        print(f'Datum: {date}, Beskrivning: {description}, Temperatur: {temperature}°C')

else:
    print(f'Fel vid hämtning av API! Statuskod: {response.status_code}')
    

#- Uppgift: Använd BeautifulSoup för att scrapa den populära webbplatsen IMDb.com för att hämta ut title, år och betyg för de 20 först populära filmerna - 
#- skriv också ut genomsnittsbetyget för de filmerna du har plockat ut ([https://www.imdb.com/chart/moviemeter/](https://www.imdb.com/chart/moviemeter/))
#- Skapa en Python-fil som hämtar datan från webbplatsen och skriver ut titlar och betyg för de senaste fem filmerna.

import requests
from bs4 import BeautifulSoup

# Skicka en GET-förfrågan till webbplatsen IMDb.com och hämta HTML-innehållet
url = 'https://www.imdb.com/chart/moviemeter/'
response = requests.get(url)
html_content = response.content

# Analysera HTML-innehållet med BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Hitta alla div-element med klassen "titleColumn"
title_columns = soup.find_all('div', {'class': 'titleColumn'})

print(title_columns)