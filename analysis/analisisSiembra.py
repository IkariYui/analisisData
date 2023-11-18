from data.ListaSiembras import createDataframe
from data.ListaSiembras import records
from helpers.CrearCSV import createCSVSowing
import pandas as pd
from helpers.CrearHTML import createTable


createCSVSowing(records, 'bdSowing.csv')

#Creating dataframe from a csv source
dataFrameSowing=pd.read_csv('data/bdSowing.csv')
#Convert Dataframe to a HTML table
createTable(dataFrameSowing, 'sowing')

ceibasFilter = dataFrameSowing.query("Treetype=='Ceibas'")
print(f"Los municipios con 'Ceibas' en 'Treetype' son:\n{ceibasFilter['Municipality']}")

lessTreesFilter = dataFrameSowing.query("Quantity<10")
print(f"Los municipios con menos de 10 árboles de algún tipo sembrados son: \n{lessTreesFilter['Municipality']}")

moreTreesFilter = dataFrameSowing.query("Quantity>90")
print(f"Los municipios con más de 90 árboles de algún tipo sembrados son: \n{moreTreesFilter['Municipality']}")