import requests
from bs4 import BeautifulSoup
import os
import json


class Scraper:
    def __init__(self, url):
        self.url = url

    def scrape_website(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.content, 'html.parser')
        jobs = []
        for job in soup.find_all('div', {'class': 'card-content'}):
            title = job.h2.text.strip()
            company = job.h3.text.strip()
            location = job.p.text.strip()
            jobs.append({'title': title, 'company': company, 'location': location})
        return jobs

    def normalize_locations(self, jobs):
        for job in jobs:
            job['location'] = job['location'].strip()

    def write_to_json(self, jobs):
        with open('job_search.json', 'w') as f:
            json.dump(jobs, f)

    def scrape_website_and_write_to_json(self):
        jobs = self.scrape_website()
        self.normalize_locations(jobs)
        self.write_to_json(jobs)

#Instansiera och skriv över till en JSON fil
scraper = Scraper('https://realpython.github.io/fake-jobs/')
scraper.scrape_website_and_write_to_json()

#Printa resultat
path = os.path.join(os.path.dirname(__file__), 'job_search.json')
with open(path, 'r') as f:
    data = json.load(f)

count = len(data)

print(f"Count of people: {count}")
print(f"Users: {json.dumps(data, indent=4)}")

# SPECIFIKATION

# TODO
# **G**

# - Scrapa sidan - [https://realpython.github.io/fake-jobs/](https://realpython.github.io/fake-jobs/)
# - Lägg in det i en lista av dictionaries, där varje dictionary skall innehålla jobtitel, företag, ort
#     - Ta bort alla mellanrum kring ortens namn
# - Skriv ned ditt resultat till en JSON-fil kallad job_search.json

# **VG**

# - Lägg din kod i metoder och lägg dem i en class, instantiera classen och kalla på en metod “scrape_website_and_write_to_json” som i sin tur anropar respektive metod
