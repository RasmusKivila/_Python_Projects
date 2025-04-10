import csv
from openpyxl import Workbook
from openpyxl.chart import BarChart, Reference
import os
import pandas as pd


class SalesData:
    def __init__(self):
        self.input_path = 'sales_data.csv'
        self.output_path = 'output.xlsx'

    def read_csv_data(self):
        data = pd.read_csv(self.input_path)
        df = pd.DataFrame(data)
        return df

    def add_total_sales_column(self, df):
        df['Total Sales'] = df['Price per item'] * df['Count sold']
        return df

    def write_to_excel(self, df):
        with pd.ExcelWriter(self.output_path) as writer:
            df.to_excel(writer, index=False)
            product_sales = df.groupby('Product')['Total Sales'].sum().reset_index()
            product_sales.to_excel(writer, sheet_name='Product Sales', index=False)

            chart = BarChart()
            chart.title = "Sales by Product"
            chart.y_axis.title = "Total Sales"
            chart.x_axis.title = "Product"

            data = Reference(writer.sheets['Product Sales'], min_col=2, min_row=2, max_col=3, max_row=11)
            chart.add_data(data, titles_from_data=True)
            categories = Reference(writer.sheets['Product Sales'], min_col=1, min_row=2, max_row=11)
            chart.set_categories(categories)
            writer.sheets['Product Sales'].add_chart(chart, "E2")

    def print_excel_data(self):
        print(pd.read_excel(self.output_path))

    def write_csv_data_to_excel(self):
        df = self.read_csv_data()
        df = self.add_total_sales_column(df)
        self.write_to_excel(df)
        self.print_excel_data()


# Instantiate the class and call the method
sales_data = SalesData()
sales_data.write_csv_data_to_excel()


# TODO

# SPECIFIKATION

# **G**

# - Läs in filen sales_data.csv och skriv över datan till en excel-fil kallad output.xlsx
# - Lägg till en kolumn med total försäljning på varje rad
# - Skapa ett nytt ark där du skriver försäljning per produkt
# - Skapa ett stapeldiagram som illustrerar försäljningen per region 

# **VG**

# - Lägg din kod i metoder och lägg dem i en class, instantiera classen och kalla på en metod “write_csv_data_to_excel” som i sin tur anropar respektive metod