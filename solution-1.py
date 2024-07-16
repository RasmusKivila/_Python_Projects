import csv
from openpyxl import Workbook
from openpyxl.chart import BarChart, Reference
import os
import pandas as pd

class MyClass:
    def __init__(self, input_path, output_path):
        self.input_path = input_path
        self.output_path = output_path
        self.df = pd.read_csv(input_path)
        
    def calculate_total_sales(self):
        # Lägg till en kolumn med total försäljning på varje rad
        self.df['Total Sales'] = self.df['Count sold'] * self.df['Price per item']

    def create_product_sales_sheet(self):
        # Skapa ett nytt ark där du skriver försäljning per produkt
        product_sales = self.df.groupby('Product')['Total Sales'].sum().reset_index()
        product_sales.to_excel(self.output_path, sheet_name='Product Sales', index=False)

    def create_sales_chart(self):
        # Skapa ett linjediagram som illustrerar försäljningen per månad
        workbook = Workbook()
        worksheet = workbook.active
        data = Reference(worksheet, min_col=4, min_row=2, max_col=4, max_row=len(self.df) + 1)
        categories = Reference(worksheet, min_col=3, min_row=2, max_row=len(self.df) + 1)
        chart = BarChart()
        chart.add_data(data, titles_from_data=True)
        chart.set_categories(categories)
        chart.title = "Sales per Month"
        worksheet.add_chart(chart, "E5")
        workbook.save(self.output_path)

    def generate_sales_report(self):
        # Ladda data, beräkna total försäljning, skapa produktförsäljningsark och försäljningsdiagram
        self.calculate_total_sales()
        self.create_product_sales_sheet()
        self.create_sales_chart()

# Använd klassen för att generera försäljningsrapporten
input_path = os.path.join(os.path.dirname(__file__), 'sales_data_v2.csv')
output_path = os.path.join(os.path.dirname(__file__), 'sales_output_v2.xlsx')

report = MyClass(input_path, output_path)
report.generate_sales_report()


# TODO

# SPECIFIKATION

# OBS - använd gärna variablerna ovan för att lösa uppgiften.
# Läs in filen sales_data_v2.csv och skriv över datan till en ny excel-fil kallad sales_output_v2.xlsx.
# - Lägg till en kolumn med total försäljning på varje rad
# - Skapa ett nytt ark där du skriver försäljning per produkt
# Skapa ett linjediagram som illustrerar försäljningen per månad.
# Organisera din kod i metoder och placera dem i en klass. Instantiera klassen och kalla på en metod med namn “generate_sales_report” som i sin tur anropar de andra metoderna.
