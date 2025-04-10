# Vilken user har fått mest total rabatt?

import requests



api_url = "https://dummyjson.com/carts"

response = requests.get(api_url)
carts = response.json()['carts']

users={}

for cart in carts:
    user_id = cart['userId']
    discount = cart['total'] - cart['discountedTotal']
    if user_id in users:
        users[user_id] += discount
    else:
        users[user_id] = discount

print(users)