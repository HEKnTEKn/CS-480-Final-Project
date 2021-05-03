import mysql.connector


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


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

    def queryFromFile(self, fileName):
        fd = open('queries/' + fileName)
        sqlFile = fd.read()
        fd.close()

        sqlCommands = sqlFile.split(';')

        for command in sqlCommands:
            try:
                self.cursor.execute(command)
            except mysql.connector.Error as err:
                print("Command failed:", err)
                print("Error Code:", err.errno)
                print("SQLSTATE", err.sqlstate)
                print("Message", err.msg)

        return self.cursor.fetchall()

    def performInternalQuery(self, fileName):
        result = self.queryFromFile(fileName)
        # for x in result:
        #     print(x)
        return result

    def performTextQuery(self, query):
        self.queryFromFile("createGuest.sql")

        self.database.commit()
        self.disconnect()
        self.connect("guest", "")

        self.cursor.execute(query)

        result = self.cursor.fetchall()
        # for x in result:
        #     print(x)
        self.disconnect()
        self.connect("root", "")

        return result
