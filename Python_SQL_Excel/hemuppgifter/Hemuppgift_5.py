import pandas as pd
import xlsxwriter

order_data_1 = pd.read_csv("order_data_1.csv")
order_data_2 = pd.read_csv("order_data_2.csv")
customer_details = pd.read_csv("customer_details.csv")

order_data_2 = order_data_2.rename(columns={'client_id': 'customer_id'})
#print(order_data_2)

order_data = pd.concat([order_data_1, order_data_2])
#print(order_data)
merged_data = pd.merge(order_data, customer_details, on='customer_id')

merged_data = merged_data.drop_duplicates().fillna("")

merged_data['order_date'] = pd.to_datetime(merged_data['order_date'], errors='coerce').dt.strftime('%Y-%m-%d %H:%M:%S')

merged_data = merged_data.sort_values(by='total_price')

merged_data['average_product_price'] = merged_data.apply(lambda row: row['total_price'] / (len(row['product_list'].split(','))), axis=1)

print(merged_data)

writer = pd.ExcelWriter('Hemuppgift_5.xlsx', engine='xlsxwriter')
merged_data.to_excel(writer, sheet_name='Lektion5', index=False)
workbook = writer.book
worksheet = writer.sheets['Lektion5']
bold = workbook.add_format({'bold': True})

for col_num, value in enumerate(merged_data.columns.values): worksheet.write(0, col_num, value, bold)
cover_page = workbook.add_worksheet('Cover Page')
cover_page.write(0, 0, 'Data Description:', bold)
cover_page.write(1, 0, 'Hemuppgift for Lektion 5 in OOP 2.')

writer.save()