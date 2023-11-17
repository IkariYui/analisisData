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

quatityTreeFilter = dataFrameSowing.query("")