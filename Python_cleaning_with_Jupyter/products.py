import csv
import random

NUMBER_OF_ROWS = 20

products = ["chair", "table", "lamp", "couch", "bed", "desk", "bookshelf", "rug", "mirror", "vase",
            "mug", "plate", "bowl", "utensils", "pillow", "blanket", "clock", "candle", "basket", "lightsaber"]

with open('products_data.csv', 'w', newline='', encoding='UTF-8') as csvfile:
    fieldnames = ['product_id', 'product_name', 'product_price']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()

    for product_id in range(1, NUMBER_OF_ROWS + 1):
        product_name = random.choice(products)
        product_price = random.randint(1, 2500)
        
        writer.writerow({"product_id": product_id, "product_name": product_name, "product_price": product_price})

print("Products data saved to 'products_data.csv'")
