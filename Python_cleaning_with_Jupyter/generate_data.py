import csv
import random #vi slumpar

NUMBERS_OF_ROW = 100
first_names= ["Alice", "Bob", "Charlie", "Rafael", "Kivilä"]
last_names= ["Larsson","Smith", "Jackson","Becker", "Rasmus"]

with open('customer_data.csv', 'w', newline='', encoding='UTF-8') as csvfile:
    fieldnames = ['name', 'age', 'phone', 'email', 'purchase_frequency']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)#for each row you write to the CSV file, you'd provide a dictionary where the keys match the field names you provided.
    writer.writeheader()#this code only sets up the CSV file with the headers
    
    for i in range(NUMBERS_OF_ROW):

        first_name = random.choice(first_names)
        last_name = random.choice(last_names)
        name = first_name + ' ' + last_name #'' skapar uttryme mellan namn och efternamn
 

        age = random.randint(18, 65)

        phone = f'07{random.randint(1,9)}--{random.randint(100000,999999)}  ' #siffrorna är oxå mängden siffror vi vill ha i telefonummret
        email = f'{first_name.lower()}.{last_name.lower()}@distansakademin.se'

        #email = email.replace('ö', 'o')#byter ö mot o, samma om man vill göra med ä
        purchase_frequency = random.choice(['medium', 'high', 'low'])

        #Var femte ålder ska vara 'invalid_age':
        if random.randint(0,5) == 0:
            age = 'invalid_age'
        #Var sjunde mail ska vara 'inavlid_mail':
        if random.randint(0,7) == 0:

            age = 'invalid_mail'
        
        writer.writerow({'name': name, 'age': age, 'phone': phone, 'email' : email, 'purchase_frequency': purchase_frequency})

 

        #writer.writerow({'fn': first_name, 'ln':last_name} ) #writerow skriver en rad, viktigt att inte blanda s på fist_names och first_name

 

 

