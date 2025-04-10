# Webscraping - **BeautifulSoup**

#- BeautifulSoup är ett Python-bibliotek som används för “web scraping” och analys av HTML- och XML-dokument. Det ger en enkel och intuitiv metod för att söka, navigera och manipulera dokumentstrukturer.
#- BeautifulSoup gör det enklare att arbeta med HTML- och XML-dokument genom att ge en enkel och intuitiv syntax för att söka, navigera och manipulera dokumentstrukturer.
#- Detta gör det möjligt att automatisera uppgifter som annars skulle vara svåra eller tidskrävande att utföra manuellt.
#- Till exempel kan du använda BeautifulSoup för att extrahera data från webbsidor och använda denna data för att utföra analys eller skapa rapporter.
#- Du kan också använda det för att automatisera web scraping av data från flera sidor, vilket kan spara tid och göra det möjligt att samla in och analysera stora mängder data på ett effektivt sätt.
#- BeautifulSoup är en kraftfull och flexibel lösning för web scraping som kan användas av utvecklare och forskare inom många olika områden, inklusive dataanalys, maskininlärning och forskning.


from bs4 import BeautifulSoup

html_doc = """
<html>
<head>
    <title>Min första websida</title>
</head>
<body>
    <h1>Välkommen till min websida</h1>
    <p>Detta är en demo-sida för BeautifulSoup.</p>
    <ul>
        <li><a href="https://www.example.com">Exempellänk</a></li>
        <li><a href="https://www.google.com">Google</a></li>
    </ul>
</body>
</html>
"""

soup = BeautifulSoup(html_doc, 'html.parser')

# Sök efter det första h1-elementet
h1 = soup.find('h1')
print(h1)

# Sök efter alla a-element
links = soup.find_all('a')
print(links)

# **Hämta elementattribut**
#- Du kan också hämta attributvärden från HTML-element med hjälp av funktionen **`get()`**.
#- Hämta href-attributet från den första a-länken
first_link = links[0]
href = first_link.get('href')
print(href)

# **Iterera över element**
#- Om du har flera element av samma typ kan du iterera över dem med hjälp av en for-loop.
#- Skriv ut alla länktexter
for link in links:
    print(link.text)

#---------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------#
# **Bearbeta HTML-kod**
# Du kan också manipulera HTML-kod med hjälp av BeautifulSoup. Till exempel kan du lägga till eller ta bort element.

# Lägg till en ny p-tag
#new_tag = soup.new_tag('p')
#new_tag.string = 'Detta är en ny paragraf.'
#soup.body.append(new_tag)

# Ta bort den första länken
#first_link = links[0]
#first_link.extract()

# Skriv ut den modifierade HTML-koden
print(soup.prettify())
