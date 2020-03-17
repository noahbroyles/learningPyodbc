import pyodbc
from pyodbc import connect

serverAddres = 'not quite' 
databaseName = 'urfunny' 
username = 'haelnah' 
password = 'gBk' 
connection = connect('DRIVER={MySQL ODBC 8.0 ANSI Driver};UID='+username+';Password='+password+';Server='+serverAddres+';Database='+databaseName+';String Types=Unicode')
connection.setdecoding(pyodbc.SQL_CHAR, encoding='utf8')
connection.setdecoding(pyodbc.SQL_WCHAR, encoding='utf8')
connection.setencoding(encoding='utf8')
cursor = connection.cursor()

# Read query from file
sqlFile = open('getAllEmails.sql', 'r')
query = sqlFile.read()
sqlFile.close()

# execute the query
cursor.execute(query)
results = cursor.fetchall()
emails = [thing[0] for thing in results] # emails is a sexy python list, my dear bro. Do not worry.

print(emails)
print(str(len(emails)), "total emails")