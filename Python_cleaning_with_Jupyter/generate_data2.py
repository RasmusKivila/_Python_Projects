import csv
import random

NUMBER_OF_ROWS = 10000

first_names = ['Jöhn', 'Jane', 'Jöe', 'Jack', 'Jill',
               'Jim', 'Jenny', 'Jesse', 'Jade', 'Jasper']
last_names = ['Smith', 'Jönes', 'Jöhnsön', 'Jacksön', 'Jenkins',
              'Jennings', 'Jensen', 'Jöhanssön', 'Janssen', 'Jensen']

with open('customer_data_only_valid.csv', 'w', newline='', encoding='UTF-8') as csvfile:
    # fieldnames = ['name', 'age', 'email', 'phone', 'purchase_frequency']
    fieldnames = ['name', 'age', 'email', 'phone', 'purchase_frequency']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()

    for i in range(NUMBER_OF_ROWS):
        first_name = random.choice(first_names)
        last_name = random.choice(last_names)
        name = first_name + ' ' + last_name
        age = random.randint(18, 65)
        email = f"{first_name.lower()}.{last_name.lower()}@distansakademin.se"
        email = email.replace('å', 'a').replace('ä', 'a').replace('ö', 'o')
        phone = f"07{random.randint(10, 99)}-{random.randint(100000, 999999)}"
        # purchase_frequency = något av "medium", "high", "low"
        purchase_frequency = random.choice(['medium', 'high', 'low'])

        # Var femte ålder ska vara "invalid_age"
        if random.randint(0, 5) == 0:
         age = 'invalid_age'
        
        #Var sjunde mail ska vara 'inavlid_mail':

        if random.randint(0,7) == 0:
            mail = 'invalid_mail'


        writer.writerow({'name': name,'age': age,'email': email,'phone': phone,'purchase_frequency': purchase_frequency})