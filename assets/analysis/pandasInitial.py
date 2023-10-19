import pandas as pd
import random
from funcionCrearDatos import createDataframe
from funcionCrearDatos import generateData
import matplotlib.pyplot as plt
#Analyze a list of data
cities = ['Medellín', 'Bogotá', 'Cali', 'Barranquilla', 'Santa Marta', 'Montería', 'Ciénaga', 'Valledupar', 'Sincelejo', 'Manizales']


#Analyze an list of dictionaries
students = [
    {'id':1, 'nombre':'Juan', 'promedio':2.8},
    {'id':2,'nombre':'María','promedio':2.5},
    {'id':3, 'nombre':'Carlos', 'promedio':2.9},
    {'id':4, 'nombre': 'Andrés', 'promedio':2.6},
    {'id':5,'nombre':'Jerónimo','promedio':2.3}
]

treePerMunicipality =[
    {'id':1,'municipality':'Girardota','treeType': 'Guayacanes','amount':1500}
]

# List of municipalities in Antioquia
municipalities = ['Medellin', 'Bello', 'Itagui', 'Envigado', 'Sabaneta', 'Rionegro', 'La Ceja', 'Girardota', 'Caldas', 'Copacabana', 'Barbosa', 'Others...']

# List of tree types
tree_types = ['Guayacanes', 'Acacias', 'Cedros', 'Pinos', 'Eucaliptos', 'Robles', 'Palmas', 'Mimosa', 'Madroño', 'Ficus', 'Olivos']


records = generateData(2000)
df = createDataframe(records)
print(df)

moda_cantidad_arboles = df['cantidad'].mode().values[0]
print(f"La moda de la cantidad de árboles es: {moda_cantidad_arboles}")
municipio_mas_comun = df['municipio'].value_counts().idxmax()
cantidad_repeticiones = df['municipio'].value_counts().max()
print(f"El municipio más común es '{municipio_mas_comun}' con {cantidad_repeticiones} repeticiones.")
media_cantidad_arboles = df['cantidad'].mean()
print(f"La media de la cantidad total de árboles es: {media_cantidad_arboles}")
mediana_cantidad_arboles = df['cantidad'].median()
print(f"La mediana de la cantidad de árboles es: {mediana_cantidad_arboles}")


# Crear una gráfica de barras para la media, mediana y moda
plt.figure(figsize=(10, 6))

# Media
plt.bar('Media', df['cantidad'].mean(), color='blue', label=f'Media: {df["cantidad"].mean()}')

# Mediana
plt.bar('Mediana', df['cantidad'].median(), color='green', label=f'Mediana: {df["cantidad"].median()}')

# Moda
plt.bar('Moda', moda_cantidad_arboles, color='red', label=f'Moda: {moda_cantidad_arboles}')

plt.title('Estadísticas de Cantidad de Árboles')
plt.xlabel('Estadística')
plt.ylabel('Valor')
plt.legend()

plt.show()

#Convert lists and list of dictionaries in DataFrames




#Analyze a CSV