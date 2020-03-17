import pyodbc
import re, sys

serverAddres = 'noahbroyles.club' 
databaseName = 'go there' 
username = 'now' 
password = 'it\'s super cool my bro'  
connection = pyodbc.connect('DRIVER={MySQL ODBC 8.0 ANSI Driver};UID='+username+';Password='+password+';Server='+serverAddres+';Database='+databaseName+';String Types=Unicode')
connection.setdecoding(pyodbc.SQL_CHAR, encoding='utf8')
connection.setdecoding(pyodbc.SQL_WCHAR, encoding='utf8')
connection.setencoding(encoding='utf8')

cursor = connection.cursor()


def isEmail(emailAddr):
    regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    if (re.search(regex, emailAddr)):  
        return True
    else:  
        return False



def insertEmails(listOfEmails):
    """
    Adds emails from a list to the DB.
    """
    # get all emails already in the DB
    sqlFile = open('getAllEmails.sql', 'r')
    query = sqlFile.read()
    sqlFile.close()
    cursor.execute(query)
    results = cursor.fetchall()
    dbEmails = [thing[0].lower() for thing in results] # emails is a sexy python list, my dear bro. Do not worry.

    if len(listOfEmails) == 0:
        print("No emails were in the list, nothing was changed.")

    elif len(listOfEmails) == 1:
        email = listOfEmails[0]
        if isEmail(email):
            if not email in dbEmails:
                sqlStatement = "INSERT INTO `tEmail` (`EmailID`, `Email`) VALUES (NULL, '"+email+"')"
                cursor.execute(sqlStatement)
                cursor.commit()
                print(email, "was added to the DB.")
            else:
                print(email, "is already in the DB. Nothing was changed.")
        else:
            print(email, "is not a valid email address. Nothing was changed.")
        
    else: # There are more than one email
        sqlStatement = "INSERT INTO `tEmail` (`Email`) VALUES "
        for email in listOfEmails:
            if isEmail(email):
                if not email in dbEmails:
                    sqlStatement += "('"+email+"'),"
                    dbEmails.append(email)
                    print("Added:", email)
                else:
                    print("Did not add:", email, "Already Present")
            else:
                print("Did not add:", email, "Invalid Address.")
        sqlStatement = sqlStatement[:-1] # bite off last comma
        cursor.execute(sqlStatement)
        cursor.commit() # damn line




            


if __name__ == "__main__":
    email = input("Enter the email to be added to the DB: ").lower()
    listEmail = [email]
    insertEmails(listEmail)
