from data.ListaUsuarios import usuarios
from helpers.CrearCSV import createCSVUsers
import pandas as pd
from helpers.CrearHTML import createTable
import matplotlib.pyplot as plt

#Using function createCSVUsers 
createCSVUsers(usuarios, 'bdUsers.csv')

#Creating dataframe from a csv source
dataFrameUsers=pd.read_csv('data/bdUsers.csv')
#Convert Dataframe to a HTML table
createTable(dataFrameUsers, 'users')

#Filter the data
filterOne = dataFrameUsers.query('Age<30')
print(f"The filter one is: {filterOne}")


filterTwo = dataFrameUsers.query("(Age>20) and (Name=='Juan')")
print(f"The filter two is: {filterTwo}")

#Salary min 1160000
#genero (m-h)
#Encontrar sembradores mujeres de 40 años que ganen entre 1 y 2 salarios mínimos
#Encontrar sembradores menos de 20 años
#Encontrar sembradores hombres mayores de 50

salaryFilter = dataFrameUsers.query("(Gender=='M') and (Age>40) and (Salary>1160000) and (Salary<2320000)")
print(f"Salary Filter: {salaryFilter}")
createTable(salaryFilter, 'salaryFilter')
# Filtrar los 5 sembradores con salario entre 1 y 2 salarios mínimos
top_5_salary = salaryFilter.nlargest(5, 'Salary')

# Crear la gráfica
plt.figure(figsize=(10, 6))
bars = plt.bar(top_5_salary['Name'], top_5_salary['Salary'], color='purple')
plt.xlabel('Sembrador')
plt.ylabel('Salario')
plt.title('Top 5 Sembradores con Salario más alto entre 1 y 2 Salarios Mínimos')
plt.xticks(rotation=45, ha='right')  # Rotar etiquetas en el eje x para mayor claridad
plt.tight_layout()

# Mostrar el valor numérico de cada barra
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, round(yval, 2), ha='center', va='bottom')

# Guardar la gráfica como imagen
plt.savefig('top_5_salary.png')


ageFilter = dataFrameUsers.query('Age<20')
print(f"The sowers under 20yo are: {ageFilter}")
createTable(ageFilter, 'ageFilter')
# Filtrar los sembradores menores de 20 años
age_distribution = ageFilter['Age'].value_counts()

# Crear la gráfica
plt.figure(figsize=(10, 6))
age_distribution.plot(kind='bar', color='red')
plt.xlabel('Edad')
plt.ylabel('Número de Sembradores')
plt.title('Distribución de Edades de Sembradores Menores de 20 Años')
plt.xticks(rotation=0)  # No rotar etiquetas en el eje x para este caso
plt.tight_layout()
# Guardar la gráfica como imagen
plt.savefig('age_distribution.png')


ageAndGenderFilter = dataFrameUsers.query("(Age>50) and (Gender=='H')")
print(f"Age and Gender Filter: {ageAndGenderFilter}")
createTable(ageAndGenderFilter, 'ageAndGenderFilter')
# Filtrar los sembradores hombres mayores de 50
top_age_and_gender = ageAndGenderFilter.nlargest(5, 'Age')

# Crear la gráfica
plt.figure(figsize=(10, 6))
bars = plt.bar(top_age_and_gender['Name'], top_age_and_gender['Age'], color='blue')
plt.xlabel('Sembrador')
plt.ylabel('Edad')
plt.title('Top 5 Sembradores Hombres Mayores de 50 Años')
plt.xticks(rotation=45, ha='right')  # Rotar etiquetas en el eje x para mayor claridad
plt.tight_layout()

# Mostrar el valor numérico de cada barra
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, round(yval, 2), ha='center', va='bottom')

# Guardar la gráfica como imagen
plt.savefig('top_age_and_gender.png')
