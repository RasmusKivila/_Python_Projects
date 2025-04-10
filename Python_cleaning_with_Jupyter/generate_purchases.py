import csv
import random
#from datetime import datetime, timedelta

NUMBER_OF_ROWS = 500

with open('product_purchases.csv', 'w', newline='', encoding='UTF-8') as csvfile:
    fieldnames = ['customer_id', 'product_id', 'purchase_id', 'purchase_date']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()

    for i in range(NUMBER_OF_ROWS):
        product_id = random.randint(0, NUMBER_OF_ROWS)
        purchase_id = i + 1
        customer_id = i + 1
        #current_date = datetime.now()
        #purchase_date = current_date - timedelta(days=random.randint(1, 365))
        month = random.randint(1,12)
        day = random.randint(1,28)
        year = random.randint(2010,2023)
        
        month = f"0{}"
        
        writer.writerow({'customer_id': customer_id ,'product_id': product_id, 'purchase_id': purchase_id, 'purchase_date': purchase_date})

print("Products data saved to 'product_purchases.csv'")

