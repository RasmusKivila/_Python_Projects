# **Hämta in data från en textfil**
#- En av de vanligaste filtyperna som vi vill hämta in data från är en textfil. 
#En textfil kan innehålla allt från en enkel textsträng till en stor mängd data i tabellform. 
#Här är en enkel metod för att läsa in data från en textfil i Python:

import os

path = os.path.join(os.path.dirname(__file__), 'name_list.txt')
with open(path, 'r') as f:
    data = f.read()

name_list = data.split('\n')
name_count = len(name_list)

print(f"Names: {name_list}")
print(f"Count of names: {name_count}")


#I det här exemplet öppnar vi filen `name_list.txt` i läsläge `'r'` och läser in hela filen med hjälp av **`f.read()`**. 
# Vi använder en **`with`**-sats för att se till att filen stängs korrekt när vi är klara med den.
# Vi använder oss utav `os.path.dirname(__file__)` för att vi ska leta efter filen i samma katalog som vårt skript ligger. 
# Utan denna rad så kommer python att leta efter filen i samma katalog som skriptet körs.

#----------------------------------------------------------------#

#En annan vanlig filtyp som vi ofta vill hämta in data från är en CSV-fil. 
# CSV står för "Comma Separated Values" och används vanligtvis för att lagra data i tabellform. 
# Här är en metod för att hämta in data från en CSV-fil i Python
import csv
import os

path = os.path.join(os.path.dirname(__file__), 'product_list.csv')

with open(path, 'r') as f:
    reader = csv.reader(f)
    data = list(reader)

# Det första elementet i listan är rubrikerna följt av produkterna
print(data[0])
for product in data[1:]:
    print(product)

# Därför är antalet produkter längden på listan minus 1
count_products = len(data) - 1
print(f"Count products: {count_products}")

#I det här exemplet öppnar vi filen `product_list.csv` i läsläge `'r'` och använder **`csv.reader`**-funktionen för att läsa in data från filen. Vi använder också **`list()`**-funktionen för att omvandla datan till en lista.

#----------------------------------------------------------------#


## **Hämta in data från en Excel-fil**

#- En tredje vanlig filtyp som vi ibland vill hämta in data från är en Excel-fil. 
# Excel-filer kan innehålla stora mängder data i tabellform och det kan vara användbart att kunna läsa in denna data till Python. 
# Här är en metod för att hämta in data från en Excel-fil i Python:
import pandas as pd
import os

path = os.path.join(os.path.dirname(__file__), 'sales.xlsx')
data = pd.read_excel(path)

print(data)
total_sales = data['Total Sales'].sum()

print(f"Total sales: {total_sales}")

#I det här exemplet använder vi **`pandas`**-biblioteket för att läsa in data från filen `sales.xlsx`. 
#Vi använder också **`read_excel()`**-funktionen för att läsa in data från filen.

#----------------------------------------------------------------#

# **Hämta in data från en JSON-fil**
#En fjärde vanlig filtyp som vi ofta vill hämta in data från är en JSON-fil. 
# JSON står för "JavaScript Object Notation" och används för att lagra data i strukturerat format. 
# Här är en metod för att hämta in data från en JSON-fil i Python:

import json
import os

path = os.path.join(os.path.dirname(__file__), 'users.json')
with open(path, 'r') as f:
    data = json.load(f)

count_users = len(data)

print(f"Count users: {count_users}")
print(f"Users: {json.dumps(data, indent=4)}")