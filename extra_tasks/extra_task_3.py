# Vad är snittsumman för alla kundvagnar?

import requests

api_url = "https://dummyjson.com/carts"

response = requests.get(api_url)
carts = response.json()['carts']

total_sum = sum([cart['total'] for cart in carts])
num_carts = len(carts)

avg_cart_sum = total_sum/num_carts

print(avg_cart_sum)