from data.ListaUsuarios import usuarios
from helpers.CrearCSV import createCSVUsers

#Using function createCSVUsers 
createCSVUsers(usuarios, 'bdUsers.csv')