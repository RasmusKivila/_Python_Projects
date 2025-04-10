import requests
# Används för att formattera output
from pprint import pprint

# URL till API-endpointet för att hämta användare
url = 'https://jsonplaceholder.typicode.com/users'

# Skicka en GET-förfrågan till API:et
response = requests.get(url)

# Om förfrågan var framgångsrik (statuskod 200), hämta datan som JSON-format
if response.status_code == 200:
    data = response.json()
    print(f'Totalt antal användare: {len(data)}\n')
    print(f'Första användarens uppgifter:\n')
    pprint(data[0], indent=4)
else:
    print('Det gick inte att hämta data från API:et.')