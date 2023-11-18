from data.ListaRefrigerios import *
from helpers.CrearCSV import createCSVSnacks
import pandas as pd
from helpers.CrearHTML import createTable
import matplotlib.pyplot as plt

#Using the funciont createCSVSnacks
createCSVSnacks(snacks, 'bdSnacks.csv')

#Creating dataframe from a csv source
dataFrameSnacks=pd.read_csv('data/bdSnacks.csv')


#Convert Dataframe to a HTML table
createTable(dataFrameSnacks, 'snacks')


#Precio 15mil
#Cantidad 500-5mil

#Precio total
#Refrigerios precio unitario <20000
#Refrigerios costo total <1000000
#Refrigerios cantidad <1000

unitPriceFilter = dataFrameSnacks.query("Price<20000")
print(f"Unit price: {unitPriceFilter}")
createTable(unitPriceFilter,'unitPriceFilter')
# Filtrar los 5 refrigerios con precio unitario menor a 20000
top_5_unit_price = unitPriceFilter.nsmallest(5, 'Price')

# Crear la gráfica
plt.figure(figsize=(10, 6))
bars = plt.bar(top_5_unit_price['Name'], top_5_unit_price['Price'], color='blue')
plt.xlabel('Refrigerio')
plt.ylabel('Precio Unitario')
plt.title('Top 5 Refrigerios con Precio Unitario Menor a 20000')
plt.xticks(rotation=45, ha='right')  # Rotar etiquetas en el eje x para mayor claridad

# Mostrar el valor numérico de cada barra
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, round(yval, 2), ha='center', va='bottom')

# Guardar la gráfica como imagen
plt.savefig('top_5_unit_price.png')

totalPriceFilter = dataFrameSnacks.query("totalPrice <1000000")
print(f"Total price: {totalPriceFilter}")
createTable(totalPriceFilter,'totalPriceFilter')
# Filtrar los 5 refrigerios con precio total menor a 1000000
top_5_total_price = totalPriceFilter.nsmallest(5, 'totalPrice')

# Crear la gráfica
plt.figure(figsize=(10, 6))
bars = plt.bar(top_5_total_price['Name'], top_5_total_price['totalPrice'], color='green')
plt.xlabel('Refrigerio')
plt.ylabel('Precio Total')
plt.title('Top 5 Refrigerios con Precio Total Menor a 1000000')
plt.xticks(rotation=45, ha='right')  # Rotar etiquetas en el eje x para mayor claridad


# Mostrar el valor numérico de cada barra
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, round(yval, 2), ha='center', va='bottom')

# Guardar la gráfica como imagen
plt.savefig('top_5_total_price.png')


quantityFilter = dataFrameSnacks.query("Cuantity<1000")
print(f"Cuantity: {quantityFilter}")
createTable(quantityFilter,'quantityFilter')
# Filtrar los 5 refrigerios con cantidad menor a 1000
top_5_quantity = quantityFilter.nsmallest(5, 'Cuantity')

# Crear la gráfica
plt.figure(figsize=(10, 6))
bars = plt.bar(top_5_quantity['Name'], top_5_quantity['Cuantity'], color='orange')
plt.xlabel('Refrigerio')
plt.ylabel('Cantidad')
plt.title('Top 5 Refrigerios con Cantidad Menor a 1000')
plt.xticks(rotation=45, ha='right')  # Rotar etiquetas en el eje x para mayor claridad


# Mostrar el valor numérico de cada barra
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, round(yval, 2), ha='center', va='bottom')

# Guardar la gráfica como imagen
plt.savefig('top_5_quantity.png')

