from data.ListaUsuarios import usuarios
from helpers.CrearCSV import createCSVUsers
import pandas as pd
from helpers.CrearHTML import createTable

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

ageFilter = dataFrameUsers.query('Age<20')
print(f"The sowers under 20yo are: {ageFilter}")

ageAndGenderFilter = dataFrameUsers.query("(Age>50) and (Gender=='H')")
print(f"Age and Gender Filter: {ageAndGenderFilter}")