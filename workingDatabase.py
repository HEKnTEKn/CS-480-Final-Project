import mysql.connector
import sqlite3


class Singleton(type):
    _instances = {}

    def __call__(classObject, *args, **kwargs):
        if classObject not in classObject._instances:
            classObject._instances[classObject] = super(Singleton, classObject).__call__(*args, **kwargs)
        return classObject._instances[classObject]


class DB(metaclass=Singleton):

    def __init__(self):
        DB.instance = self
        self.database = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="esports"
        )
        self.cursor = self.database.cursor()

    def disconnect(self):
        self.database.disconnect()
        self.cursor.close()

    def connect(self, _user, _pass):
        self.database = mysql.connector.connect(
            host="localhost",
            user=_user,
            password=_pass,
            database="esports"
        )
        self.cursor = self.database.cursor()

    def checkDataBases(self):
        self.cursor.execute("SHOW DATABASES")

        for x in self.cursor:
            print(x)

    def performQuery(self, query):
        with open('queries/createGuest.sql', 'r') as sql_file:
            self.cursor.execute(sql_file.read(), multi=True)

        self.disconnect()
        self.connect("guest", "")

        self.cursor.execute(query)

        result = self.cursor.fetchall()

        for x in result:
            print(x)

        self.disconnect()
        self.connect("root", "")

        # return result


