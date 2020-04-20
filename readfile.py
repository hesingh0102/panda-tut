import pandas as pd

#read the csv
dc = pd.read_csv('pokemon_data.csv')
dx = pd.read_excel('pokemon_data.xlsx')
dt = pd.read_csv('pokemon_data.txt', delimiter='\t')

#print head and tail from CSV
print(dc.head(2))
print(dc.tail(3))

#Print from Excel
print(dx.head(3))

#Print from txt
print(dt.head(3))
#read columns
print(dc.columns)

# Print specific columns
print(dc.Name.head, dc.Attack)
print(dc[['Name', 'Type 1']])



for index, row in dc.iterrows():
    print(index, row['Name'])


print(dc.loc[dc['Type 1'] == 'Fire'])

print(dc.describe())
print(dc.sort_values('Type 1'))
