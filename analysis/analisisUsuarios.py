from data.ListaUsuarios import usuarios
from helpers.CrearCSV import createCSVUsers
import pandas as pd
from helpers.CrearHTML import createTable

#Using function createCSVUsers 
createCSVUsers(usuarios, 'bdUsers.csv')

#Creating dataframe from a csv source
dataFrameUsers=pd.read_csv('data/bdUsers.csv')
print(dataFrameUsers)

#Convert Dataframe to a HTML table
createTable(dataFrameUsers, 'users')