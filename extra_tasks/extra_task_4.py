#Vilken är den mest handlade produktkategorin?

import requests

api_url = "https://dummyjson.com/carts"

response = requests.get(api_url)
carts = response.json()['carts']

product_quantities = {}

for cart in carts:
    for product in cart['products']:
        product_id = product['id']
        product_quantity = product['quantity']
        if product_id in product_quantities:
            product_quantities[product_id] += product_quantity
        else:
            product_quantities[product_id] = product_quantity


api_url = "https://dummyjson.com/products?limit=999"

response = requests.get(api_url)
products = response.json()['products']

print(products)

product_category_count={}

for product_quantity_id in product_quantities.keys():
    for product in products:
        product_category = product['category']
        if product['id'] == product_quantity_id:
            if product_category in product_category_count:
                product_category_count[product_category] += product_quantities[product_quantity_id]

            else:
                 product_category_count[product_category] = product_quantities[product_quantity_id]

max_product_category_count = max(product_category_count, key=product_category_count.get)
print(max_product_category_count)
        