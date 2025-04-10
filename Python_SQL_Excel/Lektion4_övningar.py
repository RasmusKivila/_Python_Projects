#ÖVNINGAR#

#Övning1
#Skriv ett program som frågar användaren efter deras namn och sparar det i en textfil "namn.txt".
#python

name = input("Vad är ditt namn? ")
with open('namn.txt', 'w') as f:
    f.write(name)
    
with open('namn.txt', 'r') as f:
    print(f.read())


#Skriv ett program som skapar en JSON-fil "data.json" och sparar en dictionary med följande data i filen:
#python
import json

data = {"namn": "Alice", "ålder": 25, "stad": "Stockholm"}

with open('data.json', 'w') as f:
    json.dump(data, f)

#Skriv ett program som skapar en CSV-fil "data.csv" och sparar en lista med följande data i filen:
#python
import csv

data = [["namn", "ålder", "stad"],
        ["Alice", 25, "Stockholm"],
        ["Bob", 30, "Göteborg"],
        ["Charlie", 35, "Malmö"]]

with open('data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(data)

#Skriv ett program som öppnar filen "data.txt" och lägger till en rad med texten "Detta är en till rad." utan att radera tidigare innehåll i filen.
#python
with open('data.txt', 'a') as f:
    f.write("Detta är en till rad.\n")

#Skriv ett program som öppnar filen "data.json", lägger till en dictionary med följande data (utan att ta bort tidigare datan) och sparar filen:
#python
import json

with open('data.json', 'r') as f:
    data = json.load(f)
    data["ny_data"] = {"namn": "Bob", "ålder": 30, "stad": "Göteborg"}

with open('data.json', 'w') as f:
    json.dump(data, f)

#Skriv ett program som öppnar filen data.csv och lägger till en rad med följande data utan att radera tidigare innehåll i filen:

#Övning2
#----------------------------------------------------------------#
import pandas as pd
import numpy as np

# Skapa en dataframe med namn och favoritfärg, inklusive saknade värden
data = {'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Gina'],
        'favorite_color': ['blue', 'red', np.nan, 'green', np.nan, 'purple', np.nan]}
df1 = pd.DataFrame(data)

# Ersätt saknade värden med "blue"
df1['favorite_color'].fillna('blue', inplace=True)

# Skapa en dataframe med namn och datum för anställning, inklusive olika datumformat
data = {'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Gina'],
        'hire_date': ['2021-05-01', '2022/03/15', '01/04/2023', '15-06-2022', '2020-10-01', '2023-01-01', '10-08-2021']}
df2 = pd.DataFrame(data)

# Konvertera datumformat till YYYY-MM-DD med to_datetime()
df2['hire_date'] = pd.to_datetime(df2['hire_date'])

# Visa de två dataframesen
print(df1)
print(df2)
