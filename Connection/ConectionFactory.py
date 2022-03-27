import mysql.connector


class Banco:

    def __init__(self):
        self.getConnection()

    @staticmethod
    def getConnection():
        banco = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="admin",
            database="dbajudaponto"
        )
        return banco