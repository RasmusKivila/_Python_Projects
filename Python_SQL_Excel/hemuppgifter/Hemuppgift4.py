import pandas as pd
import datetime

data = pd.read_csv('sales_data.csv')
df = pd.DataFrame(data)

print(df)
# Ta bort dubbletter från 'order_id'
df.drop_duplicates(subset='order_id', inplace=True)

print(f"Efter rensning: \n{df}")

# Ersätt saknade värden med Unkown
df['customer_email'].fillna('Unknown', inplace=True)
df['product_list'].fillna('Unknown', inplace=True)

print(f"Efter rensning av email och total_price: \n{df}")

# Konvertera datumformat till YYYY-MM-DD med to_datetime()
#df['order_date'] = pd.to_datetime(df['order_date'])
#print(df)

# Identifiera outlier data och ta bort dessa rader, 
# fundera på vilka kolumner som kanske kan ha outliers (det vill säga väldigt höga eller låga värden)

df['total_price'] = df['total_price'].round(2)

print(df) 