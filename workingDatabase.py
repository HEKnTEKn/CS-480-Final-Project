import mysql.connector


class DB:
    instance = None

    @staticmethod
    def getInstance():
        if DB.instance is None:
            DB()
        return DB.instance

    def __init__(self):
        if DB.instance is not None:
            raise Exception("This class is a singleton!")
        else:
            DB.instance = self
            self.instance.database = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="cs480-esports"
            )
            self.instance.cursor = self.instance.database.cursor()

    def checkDataBases(self):
        self.instance.cursor.execute("SHOW DATABASES")

        for x in self.instance.cursor:
            print(x)

    def performQuery(self, query):
        self.instance.cursor.execute(query)

        result =  self.instance.cursor.fetchall()

        for x in result:
            print(x)