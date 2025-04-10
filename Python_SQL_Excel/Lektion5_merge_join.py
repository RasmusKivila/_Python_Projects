import pandas as pd

orders = pd.read_csv('customer_orders.csv')
details = pd.read_csv('customer_details1.csv')

#Enklel merge
merged_data = pd.merge(orders, details, on='CustomerID')
#Inner join
inner_data = pd.merge(orders, details, on='CustomerID', how = "inner")
#Left join
left_join_data = pd.merge(orders, details, on='CustomerID', how='left')
#Right join
right_join_data = pd.merge(orders,details, on='CustomerID', how='right')
#Outer join
outer_data = pd.merge(orders,details, on='CustomerID', how='outer')

print("This is the merged data:")
print (merged_data)
print("This is the inner join:")
print(inner_data)
print("This is the left join:")
print (left_join_data)
print("This is the right join:")
print (right_join_data)
print("This is the outer join:")
print (outer_data)

# Övning 2
#- Läs in dataseten från `exercise_2` i pandas
#- Kombinera dessa
#- Stöter du på problem?
#- Inspektera dataseten och se vad problemet kan bero på
#
#Enkel merge: Använder den gemensamma kolumnen 'CustomerID' som nyckel och kombinerar rader med samma värde för 'CustomerID' i båda tabellerna. Denna typ av join resulterar i en tabell med alla rader från båda tabellerna där det finns matchande värden för 'CustomerID'.
#Inner join: Returnerar bara rader där det finns matchande värden för 'CustomerID' i båda tabellerna. Denna typ av join resulterar i en mindre tabell än den enkla merge-varianten.
#Left join: Returnerar alla rader från vänster tabell (i detta fall 'orders'), inklusive de rader där det inte finns matchande värden i höger tabell (i detta fall 'details'). Om det inte finns några matchande rader i höger tabell kommer de saknade värdena att vara null.
#Right join: Returnerar alla rader från höger tabell, inklusive de rader där det inte finns matchande värden i vänster tabell. Om det inte finns några matchande rader i vänster tabell kommer de saknade värdena att vara null.
#Outer join: Returnerar alla rader från båda tabellerna, inklusive de rader där det inte finns matchande värden i den andra tabellen. Om det inte finns några matchande rader i en tabell kommer de saknade värdena att vara null. Denna typ av join resulterar i en tabell som innehåller alla rader från båda tabellerna, med null-värden för de rader som inte har matchande värden i den andra tabellen.
#Skillnaden mellan dessa joins är hur de behandlar rader som saknas matchande värden i den andra tabellen. Enkla merge och inner join returnerar bara rader med matchande värden, medan left join och right join returnerar alla rader från den vänstra eller högra tabellen, inklusive de som inte har matchande värden i den andra tabellen. Outer join returnerar alla rader från båda tabellerna, inklusive de som saknar matchande värden i den andra tabellen.
