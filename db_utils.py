import mysql.connector
from mysql.connector import Error

def create_db_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            port='3305',
            user='root',
            password='sandun123',
            database='Student'
        )

        if connection.is_connected():
            print("Connection to MySQL DB successful")
            return connection
        else:
            print("Connection to MySQL DB failed")
            return None
    except Error as e:
        print(f"The error '{e}' occurred while trying to connect to the database")
        return None
