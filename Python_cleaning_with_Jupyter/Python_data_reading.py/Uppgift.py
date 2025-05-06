import pandas as pd
import csv

df = pd.read_csv('customers.csv')

# Open the CSV file

with open('customers.csv', 'r') as f:

  # Create a CSV reader object

  reader = csv.reader(f)

  # Create a dictionary to store the customers and their sales

  customers = {}

  # Iterate over the rows of the CSV file

  for row in reader:

    # Get the customer name and sales from the row

    name = row[0]

    sales = row[1]

    # Add the customer and sales to the dictionary

    customers[name] = sales
  # Sort the dictionary by sales

  sorted_customers = sorted(customers.items(), key=lambda x: x[1])
  # Extract the top 5 customers

  top_customers = sorted_customers[:6]

# Print the top 5 customers

for customer in top_customers:

  print(customer[0])
