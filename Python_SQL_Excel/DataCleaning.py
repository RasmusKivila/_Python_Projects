import csv
import random
from datetime import datetime, timedelta

# Helper functions


def random_price():
    return round(random.uniform(10, 500), 2)

def random_date(start, end):
    return start + timedelta(seconds=random.randint(0, int((end - start).total_seconds())))

def random_index(last_index):
    return random.randint(0, last_index)

# Define product and customer data
products = ['T-shirt', 'Jeans', 'Sneakers', 'Jacket', 'Watch']
customers = [
    'john@example.com',
    'jane@example.com',
    'bob@example.com',
    'johndoe1234@example.com',
    'sarahjones5678@gmail.com',
    'brianwilson4321@hotmail.com',
    'katewilliams7890@outlook.com',
    'davidlee2468@yahoo.com',
    'laurensmith1357@gmail.com',
    'adamjohnson2468@yahoo.com',
    'amybrown7890@outlook.com',
    'jenniferwhite1234@gmail.com',
    'matthewjackson5678@hotmail.com',
    'chrisgreen2468@outlook.com',
    'rachelgray7890@yahoo.com',
    'ericmorris1234@example.com',
    'stephaniebrown5678@gmail.com',
    'nickjones2468@outlook.com',
    'laurawilson7890@example.com',
    'patricktaylor1357@yahoo.com',
    'jessicasmith5678@gmail.com',
    'andrewbrown2468@outlook.com',
    'emilydavis7890@example.com',
]

# Define order count and date range
order_count = 1000
start_date = datetime(2022, 1, 1)
end_date = datetime(2023, 3, 17)

# Generate sales dataset
orders = []
for i in range(order_count):
    order_date = random_date(start_date, end_date)
    order_id = i + 1
    customer_email = random.choice(customers)
    product_count = random.randint(1, 5)
    product_list = random.sample(products, product_count)
    total_price = sum(random_price() for _ in range(product_count))
    order = {
        'order_id': order_id,
        'customer_email': customer_email,
        'product_list': ', '.join(product_list),
        'total_price': total_price,
        'order_date': order_date.strftime('%m/%d/%Y %H:%M:%S')
    }
    orders.append(order)

# Add incomplete data, outliers, duplicate data, and inconsistent date formats
for x in range(14):
    orders[random_index(len(orders)- 1)]['product_list'] = ''
    orders[random_index(len(orders)- 1)]['total_price'] = 10000
    orders[random_index(len(orders)- 1)]['customer_email'] = ''
    orders[random_index(len(orders)- 1)]['order_date'] = '01/2022/01 01:00:00'

for x in range(6):
    rand_index = random_index(len(orders)- 1)
    order_id_first_order = orders[rand_index]['order_id']
    other_rand_index = random_index(len(orders)- 1)
    if not rand_index == other_rand_index:
        print('order_id_first_order', order_id_first_order)
        orders[other_rand_index]['order_id'] = order_id_first_order

# Save sales dataset to CSV file
with open('sales_data.csv', mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=[
                            'order_id', 'customer_email', 'product_list', 'total_price', 'order_date'])
    writer.writeheader()
    for order in orders:
        writer.writerow(order)
#................................................................#    
import csv
import random
import datetime

products = [
    'A',
    'B',
    'C',
    'D',
    'E',
]

first_order_id = 1001

def random_date(start, end):
    return start + datetime.timedelta(seconds=random.randint(0, int((end - start).total_seconds())))

customer_ids = [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10
]

orders_header = ['OrderID', 'CustomerID', 'Product', 'Quantity', 'Price']


start_date = datetime.datetime(2022, 1, 1)
end_date = datetime.datetime(2023, 3, 17)

order_rows = []
for x in range(10):
    order = [
        first_order_id + x,
        random.choice(customer_ids),
        random.choice(products),
        random_date(start_date, end_date)
    ]
    order_rows.append(order)

print(order_rows)



# with open('customer_orders.csv', mode='w', newline='') as orders_file:
#     orders_writer = csv.writer(orders_file)
#     orders_writer.writerow(orders_header)
#     orders_writer.writerows(orders_rows)

# # Create a CSV file for customer details
# details_header = ['CustomerID', 'Name', 'Address', 'Phone']
# details_rows = [    [101, 'John Doe', '123 Main St', '555-1234'],
#     [102, 'Jane Smith', '456 Elm St', '555-5678'],
#     [103, 'Bob Johnson', '789 Oak St', '555-9012'],
#     [104, 'Alice Brown', '321 Pine St', '555-3456']
# ]

# with open('customer_details.csv', mode='w', newline='') as details_file:
#     details_writer = csv.writer(details_file)
#     details_writer.writerow(details_header)
#     details_writer.writerows(details_rows)

import random
import csv

# Skapa en lista med produkter och regioner
produkter = ["Produkt A", "Produkt B", "Produkt C", "Produkt D"]
regioner = ["Region 1", "Region 2", "Region 3", "Region 4"]

# Öppna en CSV-fil för att skriva data
with open("sales_data.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)

    # Skriv kolumnrubriker
    writer.writerow(["Datum", "Produkt", "Region", "Antal sålda", "Pris per enhet"])

    # Skriv 100 rader med slumpmässig data
    for i in range(100):
        datum = f"2022-{random.randint(1, 12):02d}-{random.randint(1, 28):02d}"
        produkt = random.choice(produkter)
        region = random.choice(regioner)
        antal = random.randint(10, 100)
        pris = round(random.uniform(10, 100), 2)
        writer.writerow([datum, produkt, region, antal, pris])
        
#................................................................#
import csv
import random
from datetime import date, timedelta

def generate_sales_data(num_rows):
    product_ids = range(1, 11)
    product_names = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E', 'Product F', 'Product G', 'Product H', 'Product I', 'Product J']
    regions = ['North', 'South', 'East', 'West']

    sales_data = []

    for _ in range(num_rows):
        product_index = random.randint(0, len(product_ids) - 1)
        region = random.choice(regions)
        unit_price = round(random.uniform(10, 100), 2)
        quantity = random.randint(1, 20)
        sale_date = date.today() - timedelta(days=random.randint(1, 365))

        sales_data.append({
            'date': sale_date,
            'product_id': product_ids[product_index],
            'product_name': product_names[product_index],
            'region': region,
            'unit_price': unit_price,
            'quantity': quantity,
        })

    return sales_data

def write_sales_data_to_csv(sales_data, file_name):
    with open(file_name, 'w', newline='') as csvfile:
        fieldnames = ['date', 'product_id', 'product_name', 'region', 'unit_price', 'quantity',]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for row in sales_data:
            writer.writerow(row)

if __name__ == '__main__':
    num_rows = 1000
    file_name = 'sales_data.csv'

    sales_data = generate_sales_data(num_rows)
    write_sales_data_to_csv(sales_data, file_name)
    print(f"Generated {num_rows} rows of sales data and saved it to {file_name}.")