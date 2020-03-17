import pyodbc

serverAddres = 'caca.com' 
databaseName = 'nono' 
username = 'yesyes' 
password = 'these are actually all the same everything' 
connection = pyodbc.connect('DRIVER={MySQL ODBC 8.0 ANSI Driver};UID='+username+';Password='+password+';Server='+serverAddres+';Database='+databaseName+';String Types=Unicode')
connection.setdecoding(pyodbc.SQL_CHAR, encoding='utf8')
connection.setdecoding(pyodbc.SQL_WCHAR, encoding='utf8')
connection.setencoding(encoding='utf8')

cursor = connection.cursor()

# get all emails already in the DB
sqlFile = open('getAllEmails.sql', 'r')
query = sqlFile.read()
sqlFile.close()
cursor.execute(query)
results = cursor.fetchall()
emails = [thing[0].lower() for thing in results] # emails is a sexy python list, my dear bro. Do not worry.

emailToDelete = input("Enter the email to be added to the DB: ").lower()

if emailToDelete in emails:
    cursor.execute("DELETE FROM `tEmail` WHERE `tEmail`.`Email` = '"+emailToDelete+"'")
    connection.commit() # damn line
    print(emailToDelete, "was removed from the DB.")
else:
    print("That email was not found in the DB. Nothing was changed.")