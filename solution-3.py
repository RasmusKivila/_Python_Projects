import pandas as pd
import csv
import os

input_path = os.path.join(os.path.dirname(__file__), 'sales_data_v2.csv')
output_path = os.path.join(os.path.dirname(__file__), 'cleaned_sales_data.csv')

class OrderDataCleaner():
    def __init__(self, filename):
        self.df = pd.read_csv(filename)

        #Ta bort dubbletter från 'order_id'
    def remove_duplicated_orders(self):
        self.df.drop_duplicates(subset='order_id', inplace=True)
    
        #Ta bort outliers från 'total_price där värdet är mer än 800 kr'
    def remove_extreme_amount(self):
        self.df = self.df[self.df['total_price'] <= 800]

        #Ta bort outlier ytterligare outlier värden
    def remove_outlier_columns(self):
        self.df.dropna(subset=['product_list'], inplace=True)   # Ta bort NaN values
        self.df = self.df[self.df['product_list'] != ""]         # Ta bort string values
        
        #Runda av total_price
    def round_amount(self):
        self.df['total_price'] = self.df['total_price'].round(2)

        #Konvertera datumformat till YYYY-MM-DD med to_datetime()
    def convert_to_datetime(self):
        self.df['order_date'] = pd.to_datetime(self.df['order_date'], format='%d/%m/%Y').dt.strftime('%Y-%m-%d')

    def clean_data(self):
        self.remove_duplicated_orders()
        self.remove_extreme_amount()
        self.round_amount()
        self.remove_outlier_columns()
        #self.convert_to_datetime()
        self.df.to_csv('cleaned_order_data.csv', encoding='utf-8', index=False)

#instansiera klassen
cleaner = OrderDataCleaner('sales_data_v2.csv')
cleaner.clean_data()

#Läsa av/printa resultatet
print(pd.read_csv('cleaned_order_data.csv'))

# TODO


# SPECIFIKATION

# OBS - använd gärna variablerna ovan för att lösa uppgiften.
# Läs in filen sales_data_v2.csv.
# - Använd pandas för att:
#     - Ta bort rader med duplicerade ordernummer
#     - Ta bort rader some har outliers i sitt total_price (över 800)
#     - Ta bort rader som har tomma product_list
#     - Konvertera datum som är i annat format till en enhetlig skala
# - Spara ner den till en ny fil kallad cleaned_order_data.csv
# Organisera din kod i metoder och placera dem i en klass. Instantiera klassen och kalla på en metod med namn “process_data” som i sin tur anropar de andra metoderna.
