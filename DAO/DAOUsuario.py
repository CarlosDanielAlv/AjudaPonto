from Connection.ConectionFactory import Banco
import mysql.connector


class DaoUsuario:

    def __init__(self, usuario):
        self.user = usuario
        self.myBank = Banco()
        self.myConnection = self.myBank.getConnection()

    def insert(self):
        cursor = self.myConnection.cursor()

        try:
            SQLUserValid = "SELECT * FROM usuario WHERE nome = %s"
            dadosUser = (str(self.user.getNomeUsuario()),)
            cursor.execute(SQLUserValid, dadosUser)

            myUserExist = cursor.fetchall()

            if not myUserExist:
                comando_SQL = "INSERT INTO usuario (nome, senha) VALUES (%s,%s)"
                dados = (str(self.user.getNomeUsuario()), str(self.user.getSenhaUsuario()))
                cursor.execute(comando_SQL, dados)

                self.myConnection.commit()
                self.myConnection.close()

                if cursor.rowcount > 0:
                    return True
            else:
                return -1
        except mysql.connector.Error as err:
            print("Houve um erro na operação insert: ", err)
            return False

    def authenticate(self):
        cursor = self.myConnection.cursor()

        try:
            SQLUserValid = "SELECT * FROM usuario WHERE nome = %s"
            dadosUser = (str(self.user.getNomeUsuario()),)
            cursor.execute(SQLUserValid, dadosUser)

            result = cursor.fetchall()

            if result:
                SQL = "SELECT * FROM usuario WHERE nome = %s and senha = %s"
                dados = (str(self.user.getNomeUsuario()), str(self.user.getSenhaUsuario()))
                cursor.execute(SQL, dados)

                myResult = cursor.fetchall()

                return myResult
            else:
                return -1

        except mysql.connector.Error as err:
            print("Houve um erro na operação authenticate: ", err)
            return False