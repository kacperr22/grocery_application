import mysql.connector
def get_sql_connection():

    cnx = mysql.connector.connect(user='root', password='Kapikl0817@1234',
                                  host='127.0.0.1',
                                  database='grocery_store')
    return cnx