# Vilken kundvagn har fått mest rabatt?

import requests



api_url = "https://dummyjson.com/carts"

response = requests.get(api_url)
carts = response.json()['carts']

max_discount = 0
max_discount_cart_id = 0


for cart in carts:
    cart_discount_total = cart['total'] - cart['discountedTotal']
    if max_discount < cart_discount_total:
        max_discount = cart_discount_total
        max_discount_cart_id = cart['id']
    print("")

print(f'Max discounted cart: {max_discount_cart_id}')


max_discount_cart_id = max(carts, key=lambda cart: cart['total'] - cart['discountedTotal'])['id']


print(f'Max discounted cart: {max_discount_cart_id}')


