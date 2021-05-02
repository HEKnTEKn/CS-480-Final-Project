import mysql.connector


def instantiateDB():
    database = mysql.connector.connect(
        host="localhost",
        user="root",
        password=""
    )
    print(database)
    return database


