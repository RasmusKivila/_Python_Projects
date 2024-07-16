import requests
from bs4 import BeautifulSoup
import json
import os

url = "https://realpython.github.io/fake-jobs/"
output_path = "job_search_v2.json"

class Scraper():
    def __init__(self, url, output_path):
        self.url = url
        self.output_path = output_path
        self.jobs = []

    def scrape_jobs(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.content, 'html.parser')
        for job in soup.find_all('div', {'class': 'card-content'}):
            title = job.h2.text.strip()
            company = job.h3.text.strip()
            location = job.p.text.strip().capitalize()
            
            # Kontrollera om det finns ett publiceringsdatum
            published_elem = job.find('time', {'class': 'has-text-grey'})
            published = published_elem.text.strip() if published_elem else "Okänt"

            self.jobs.append({'title': title, 'company': company, 'location': location, 'published': published})

    def save_to_json(self):
        with open(self.output_path, 'w') as f:
            json.dump(self.jobs, f, indent=4)

    def collect_and_save_jobs(self):
        self.scrape_jobs()
        self.save_to_json()

# Skapa en instans av Scraper-klassen och anropa metoden för att samla och spara jobbdata
example = Scraper(url, output_path)
example.collect_and_save_jobs()

# Skriv ut resultatet
with open(output_path, 'r') as f:
    data = json.load(f)
count = len(data)

print(f"Count of jobs: {count}")
print(f"Jobs: {json.dumps(data, indent=4)}")


# TODO

# SPECIFIKATION

# OBS - använd gärna variablerna ovan för att lösa uppgiften.
# Scrapa sidan - https://realpython.github.io/fake-jobs/
# Lägg in det i en lista av dictionaries, där varje dictionary skall innehålla jobtitel, företag, ort, och publiceringsdatum.
# Se till att varje ort är korrekt formaterad med första bokstaven i versal.
# Skriv ned ditt resultat till en JSON-fil kallad job_search_v2.json.
# Organisera din kod i metoder och placera dem i en klass. Instantiera klassen och kalla på en metod med namn “collect_and_save_jobs” som i sin tur anropar de andra metoderna.