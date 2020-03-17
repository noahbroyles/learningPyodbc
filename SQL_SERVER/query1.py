from pyodbc import connect
import pandas as pd

serverAddres = 'not for litle eyes' 
databaseName = 'GroceryStore' 
username = 'hawt' 
password = 'squeeze me' 
sqlServer = connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+serverAddres+';DATABASE='+databaseName+';UID='+username+';PWD='+ password)
cursor = sqlServer.cursor()

sqlFile = open("SQLQuery_1.sql", "r")
query = sqlFile.read()
sqlFile.close()

# Allow printing the full thinggy
pd.set_option('display.max_rows', None)

cursor.execute(query)
results = cursor.fetchall()
descriptions = [thing[0] for thing in results]



# Execute the query using pandas
# tableResult = pd.read_sql(query, sqlServer) 

# Make a pandas dataframe from the the query results
sexyData = pd.DataFrame(descriptions)

print(sexyData)

# Make an excel file out of the query results
sexyData.to_excel("FileExample.xlsx",sheet_name='Results')