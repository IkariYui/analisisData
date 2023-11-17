from data.ListaRefrigerios import *
from helpers.CrearCSV import createCSVSnacks
import pandas as pd
from helpers.CrearHTML import createTable

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
totalPriceFilter = dataFrameSnacks.query("totalPrice <1000000")
print(f"Total price: {totalPriceFilter}")
quantityFilter = dataFrameSnacks.query("Cuantity<1000")
print(f"Cuantity: {quantityFilter}")

