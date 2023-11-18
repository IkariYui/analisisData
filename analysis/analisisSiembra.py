from data.ListaSiembras import createDataframe
from data.ListaSiembras import records
from helpers.CrearCSV import createCSVSowing
import pandas as pd
from helpers.CrearHTML import createTable
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

createCSVSowing(records, 'bdSowing.csv')

#Creating dataframe from a csv source
dataFrameSowing=pd.read_csv('data/bdSowing.csv')
# Crear una figura y un eje
fig, ax = plt.subplots(figsize=(10, 6)) 

# Ocultar ejes
ax.axis('off')

# Crear una tabla desde el DataFrame y agregarla al eje
tabla = ax.table(cellText=dataFrameSowing.values, colLabels=dataFrameSowing.columns, loc='center', cellLoc='center')

# Establecer el formato de la tabla
tabla.auto_set_font_size(False)
tabla.set_fontsize(10)

# Guardar la figura en un archivo PDF
with PdfPages('dataFrameSowing.pdf') as pdf:
    pdf.savefig(fig, bbox_inches='tight')


#Convert Dataframe to a HTML table
createTable(dataFrameSowing, 'sowing')

colores = ['blue', 'green', 'red', 'purple', 'orange']

ceibasFilter = dataFrameSowing.query("Treetype=='Ceibas'")
print(f"Los municipios con 'Ceibas' en 'Treetype' son:\n{ceibasFilter['Municipality']}")
createTable(ceibasFilter, 'ceibasFilter')
# Obtener los 5 municipios con más 'Ceibas'
top_ceibas_municipios = ceibasFilter.nlargest(5, 'Quantity')

# Crear la gráfica de barras con etiquetas
plt.figure(figsize=(10, 6))
bars = plt.bar(top_ceibas_municipios['Municipality'], top_ceibas_municipios['Quantity'], color=colores)
plt.xlabel('Municipio')
plt.ylabel('Cantidad de Árboles de Ceibas')
plt.title('Top 5 Municipios con Más Árboles de Ceibas')

# Agregar etiquetas con la cantidad exacta de árboles
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, round(yval, 2), ha='center', va='bottom')

plt.xticks(rotation=45, ha='right')  # Rotar etiquetas del eje x para una mejor legibilidad
plt.savefig('top_ceibas_municipios.png')


lessTreesFilter = dataFrameSowing.query("Quantity<10")
print(f"Los municipios con menos de 10 árboles de algún tipo sembrados son: \n{lessTreesFilter['Municipality']}")
createTable(lessTreesFilter, 'lessTreesFilter')

# Obtener los 5 municipios con menos árboles
bottom_municipios = lessTreesFilter.nsmallest(5, 'Quantity')

# Crear la gráfica de barras con etiquetas
plt.figure(figsize=(10, 6))
bars = plt.bar(bottom_municipios['Municipality'], bottom_municipios['Quantity'], color=colores)
plt.xlabel('Municipio')
plt.ylabel('Cantidad de Árboles')
plt.title('Top 5 Municipios con Menos Árboles')

# Agregar etiquetas con la cantidad exacta de árboles
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, round(yval, 2), ha='center', va='bottom')

plt.xticks(rotation=45, ha='right')  # Rotar etiquetas del eje x para una mejor legibilidad
plt.savefig('bottom_municipios_arboles.png')


moreTreesFilter = dataFrameSowing.query("Quantity>90")[['Municipality', 'Quantity']]
print(f"Los municipios con más de 90 árboles sembrados de algún tipo son:{moreTreesFilter}")
createTable(moreTreesFilter, 'moreTreesFilter')

# Obtener los 5 municipios con más árboles
top_municipios = moreTreesFilter.nlargest(5, 'Quantity')
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

