#Övning 2:
import requests
from bs4 import BeautifulSoup

url = "https://www.reddit.com/r/sweden/"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

posts = soup.find_all("div", class_="Post")

post_list = []

for post in posts:
    title = post.find("h3", class_="_eYtD2XCVieq6emjKBH3m").text
    comments = post.find("span", class_="FHCV02u6Cp2zYL0fhQPsO").text.split()[0]
    post_list.append({"title": title, "comments": int(comments)})
    
sorted_list = sorted(post_list, key=lambda x: x["comments"])
print(sorted_list)


#Importera nödvändiga bibliotek - requests och BeautifulSoup.
#Ange URL-adressen för webbplatsen som du vill hämta data från - i detta fall Reddit-sidan för Sverige.
#Använd requests.get () för att hämta HTML-svaret för webbplatsen.
#Skapa ett BeautifulSoup-objekt som parsar HTML-svaret och skapar en läsbar trädstruktur av element och attribut.
#Använd soup.find_all () för att hitta alla "div" -element med en klassattribut "Post" och lagra dem i en variabel som heter "posts".
#Skapa en tom lista med namnet "post_list" för att lagra information om varje inlägg på webbplatsen.
#Använd en för-loop för att loopa igenom varje "post" i listan "posts".
#För varje "post", använd post.find () för att hitta elementet som innehåller titeln och kommentarerna och extrahera texten med .text.
#För kommentarer används .split () för att ta bort onödig text från strängen och spara endast antalet kommentarer som en integer.
#Lägg till en dictionary som innehåller titeln och antalet kommentarer för varje post i listan "post_list".
#Sortera listan med hjälp av nyckelordet "lambda" och sortera efter antalet kommentarer i omvänd ordning för att få en sorterad lista som går från mest till minst kommentarer.
#Skriv ut den sorterade listan.

