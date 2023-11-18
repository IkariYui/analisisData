from data.ListaSiembras import createDataframe
from data.ListaSiembras import records
from helpers.CrearCSV import createCSVSowing
import pandas as pd
from helpers.CrearHTML import createTable
import matplotlib.pyplot as plt

createCSVSowing(records, 'bdSowing.csv')

#Creating dataframe from a csv source
dataFrameSowing=pd.read_csv('data/bdSowing.csv')
#Convert Dataframe to a HTML table
createTable(dataFrameSowing, 'sowing')

ceibasFilter = dataFrameSowing.query("Treetype=='Ceibas'")
print(f"Los municipios con 'Ceibas' en 'Treetype' son:\n{ceibasFilter['Municipality']}")
createTable(ceibasFilter, 'ceibasFilter')

lessTreesFilter = dataFrameSowing.query("Quantity<10")
print(f"Los municipios con menos de 10 árboles de algún tipo sembrados son: \n{lessTreesFilter['Municipality']}")
createTable(lessTreesFilter, 'lessTreesFilter')

moreTreesFilter = dataFrameSowing.query("Quantity>90")[['Municipality', 'Quantity']]
print(f"Los municipios con más de 90 árboles sembrados de algún tipo son:{moreTreesFilter}")
createTable(moreTreesFilter, 'moreTreesFilter')

# Obtener los 5 municipios con más árboles
top_municipios = moreTreesFilter.nlargest(5, 'Quantity')
colores = ['blue', 'green', 'red', 'purple', 'orange']
# Crear la gráfica de barras con etiquetas
fig, ax = plt.subplots()
bars = plt.bar(top_municipios['Municipality'], top_municipios['Quantity'], color=colores)
plt.xlabel('Municipio')
plt.ylabel('Cantidad de Árboles')
plt.title('Top 5 Municipios con Más Árboles')

# Agregar etiquetas con la cantidad exacta de árboles
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, round(yval, 2), ha='center', va='bottom')

plt.savefig('top_municipios_arboles.png')
plt.show()
