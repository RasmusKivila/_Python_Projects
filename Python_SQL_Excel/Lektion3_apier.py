import requests

main_url = "https://jsonplaceholder.typicode.com"

def get_post(post_id):
    url = f"{main_url}/posts/{post_id}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error retrieving post {post_id}. Response status code: {response.status_code}")

def get_all_posts():
    url = f"{main_url}/posts"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error retrieving posts. Response status code: {response.status_code}")

def create_post(title, body, user_id):
    url = f"{main_url}/posts"
    data = {"title": title, "body": body, "userId": user_id}
    response = requests.post(url, json=data)
    if response.status_code == 201:
        return response.json()
    else:
        raise Exception(f"Error creating post. Response status code: {response.status_code}")

def update_post(post_id, title, body, user_id):
    url = f"{main_url}/posts/{post_id}"
    data = {"title": title, "body": body, "userId": user_id}
    response = requests.put(url, json=data)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error updating post {post_id}. Response status code: {response.status_code}")

def update_post_partial(post_id, data):
    url = f"{main_url}/posts/{post_id}"
    response = requests.patch(url, json=data)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error updating post {post_id}. Response status code: {response.status_code}")

# Instans - Kalla en specfik post med id : 1
post_id = 1
post = get_post(post_id)
print(post)

# instans - Hämta alla posts
posts = get_all_posts()
print(posts)

# Instans - Skapar med en ny POST
new_post = create_post("Ny POST", "Ny POST body", 1)
print(new_post)

# Instans - Kallar på funktionen update_post för att updatera en existerande post 
post_id = 1
updated_post = update_post(post_id, "Uppdaterad POST", "Uppdaterad POST body", 1)
print(updated_post)

# instans - Kalla update_post_partial funktionen för att updatera en del av posten inuti APIET
post_id = 1
partial_data = {"title": "Uppdaterad del av POSTEN"}
updated_post_partial = update_post_partial(post_id, partial_data)
print(updated_post_partial)
#----------------------------------------------------------------
#----------------------------------------------------------------
#----------------------------------------------------------------
#----------------------------------------------------------------
#----------------------------------------------------------------
#----------------------------------------------------------------
#----------------------------------------------------------------
# Webscraping - **BeautifulSoup**

#- BeautifulSoup är ett Python-bibliotek som används för “web scraping” och analys av HTML- och XML-dokument. Det ger en enkel och intuitiv metod för att söka, navigera och manipulera dokumentstrukturer.
#- BeautifulSoup gör det enklare att arbeta med HTML- och XML-dokument genom att ge en enkel och intuitiv syntax för att söka, navigera och manipulera dokumentstrukturer.
#- Detta gör det möjligt att automatisera uppgifter som annars skulle vara svåra eller tidskrävande att utföra manuellt.
#- Till exempel kan du använda BeautifulSoup för att extrahera data från webbsidor och använda denna data för att utföra analys eller skapa rapporter.
#- Du kan också använda det för att automatisera web scraping av data från flera sidor, vilket kan spara tid och göra det möjligt att samla in och analysera stora mängder data på ett effektivt sätt.
#- BeautifulSoup är en kraftfull och flexibel lösning för web scraping som kan användas av utvecklare och forskare inom många olika områden, inklusive dataanalys, maskininlärning och forskning.

