#Hemuppgift 4

#- Filerna ligger under lektion 5, hemuppgift
#- Kombinera order-datan för order_data_1 och order_data_2 till en gemensam tabell med order-datum
#- Kombinera den kombinerade order tabellen med tabellen med kund_detaljer
#- Ta bort eventuell duplicerade värden
#- Fyll tomma värden (NAN) med en tom sträng
#- Se till att alla datumformat är i samma format
#- Sortera på totalt pris
#- Skapa en ny kolumn “average product price” som tar totala order_värdet genom antalet produkter för ordern
#- Spara tabellen till ett excel-dokument via pandas
#- Gör rubrikerna i fet stil
#- Gör ett försättsblad som förklarar innehållet på dokumentet
import pandas as pd

orders_1 = pd.read_csv('order_data_1.csv')
orders_2 = pd.read_csv('order_data_2.csv')
customer_details = pd.read_csv("customer_details.csv")

#Concat - Gemensam tabell
orders = pd.concat([orders_1, orders_2])

print(orders)
#Merge - Kombinera ordertabell och kund detaljer
merged_data = pd.merge(orders, customer_details, on='customer_id', how='left')

print(merged_data)
# Ta bort eventuell duplicerade värden
merged_data.drop_duplicates(inplace=True)

#Fylla i tommavärden (NAN) med en tom sträng med funktionen fillna()
merged_data.fillna("", inplace=True)

#order_date - för att se till att datumet stämmer in i datasetet med datetime--#
merged_data['order_date'] = pd.to_datetime(merged_data['order_date'], format='%Y/%d/%m %H:%M:%S', errors='coerce')

# För att sortera på total_price med funktionen .sort() i detta fall min .sort_values()
merged_data.sort_values(by=['total_price'], inplace = True)

#För att skapa en ny kolumn "average product price" använder jag funktionen .apply() tillsammans lambda-funktion:
merged_data['average_product_price'] = orders.apply(lambda row: row['total_price'] / row['num_products'], axis=1)

# Spara tabellen till ett excel-dokument via pandas
with pd.ExcelWriter('merged_data.xlsx') as writer:
    merged_data.to_excel(writer, index=False, sheet_name='Hemuppgift från Lektion 5')
    workbook = writer.book
    worksheet = writer.sheets['Hemuppgift från Lektion 5']
    
    # Gör rubrikerna i fet stil
    bold = workbook.add_format({'bold': True})
    for col_num, value in enumerate(merged_data.columns.values):
        worksheet.write(0, col_num, value, bold)

    # Gör ett försättsblad som förklarar innehållet på dokumentet
    intro_worksheet = workbook.add_worksheet('Introduction')
    intro_worksheet.write('A1', 'This Excel file contains merged data from orders and customer details.')
    intro_worksheet.write('A2', 'The Merged Data sheet contains the following columns:')
    for i, col_name in enumerate(merged_data.columns):
        intro_worksheet.write(i+3, 0, f'{i+1}. {col_name}')

