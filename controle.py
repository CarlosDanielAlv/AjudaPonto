from PyQt5 import uic, QtWidgets
from Model.Usuario import Usuario
from DAO.DAOUsuario import DaoUsuario
import time


class Controller:

    @staticmethod
    def CadastrarUsuario():
        formularioCadastro.lbAlertaGeral.setText("")
        # Capturando o usuario no formulário
        usuario = formularioCadastro.tbUsuario.text()
        # Capturando senha no formulário
        senha = formularioCadastro.tbSenha.text()

        if usuario != "" and senha != "":
            # Preenchendo usuário no meu objeto
            user = Usuario(usuario, senha)
            # Chamada do banco de dados
            userDao = DaoUsuario(user)

            # Inserindo os dados no banco de dados
            resultInserUser = userDao.insert()
            if resultInserUser == -1:   # Usuário já existe na base de dados
                formularioCadastro.lbAlertaGeral.setStyleSheet("color: red;")
                formularioCadastro.lbAlertaGeral.setText("Este usuário já está cadastrado em nosso sistema")
            elif resultInserUser:
                formularioCadastro.tbUsuario.setText("")
                formularioCadastro.tbSenha.setText("")
                formularioCadastro.lbAlertaGeral.setStyleSheet("color: green;")
                formularioCadastro.lbAlertaGeral.setText("Novo usuário cadastrado com sucesso ! ! !")

        else:
            formularioCadastro.lbAlertaGeral.setStyleSheet("color: red;")
            formularioCadastro.lbAlertaGeral.setText("Preencha todos os campos *")

    @staticmethod
    def authenticate():
        formularioLogin.lbAlertaGeral.setText("")
        # Capturando o usuario no formulário
        usuario = formularioLogin.tbUsuario.text()
        # Capturando senha no formulário
        senha = formularioLogin.tbSenha.text()

        if usuario != "" and senha != "":
            # Preenchendo usuário no meu objeto
            user = Usuario(usuario, senha)
            # Chamada do banco de dados
            userDao = DaoUsuario(user)

            # Verificando se o usuário existe na base de dados
            author = userDao.authenticate()
            if author == -1:    # Usuário não existe
                formularioLogin.lbAlertaGeral.setStyleSheet("color: red;")
                formularioLogin.lbAlertaGeral.setText("Usuario não cadastrado !!!")

            elif author:    # Usuário aprovado
                formularioLogin.lbAlertaGeral.setStyleSheet("color: green;")
                time.sleep(2)  # Sleep for 3 seconds
                formularioLogin.lbAlertaGeral.setText("Bem Vindo, redirecionando. . .")

            else:   # Login ou Senha incorretos
                formularioLogin.lbAlertaGeral.setStyleSheet("color: red;")
                formularioLogin.lbAlertaGeral.setText("Usuario ou senha incorretos")

        else:
            formularioLogin.lbAlertaGeral.setStyleSheet("color: red;")
            formularioLogin.lbAlertaGeral.setText("Preencha todos os campos *")

    @staticmethod
    def abrirTelaLogin():
        formularioLogin.show()
        formularioCadastro.close()

    @staticmethod
    def abrirTelaCadastro():
        formularioCadastro.show()
        formularioLogin.close()


app = QtWidgets.QApplication([])
# Formulário de Cadastro
formularioCadastro = uic.loadUi("Forms/form_cadastro.ui")
formularioCadastro.btnCadastrar.clicked.connect(Controller.CadastrarUsuario)
formularioCadastro.btnIrLogin.clicked.connect(Controller.abrirTelaLogin)

# Formulário de Login
formularioLogin = uic.loadUi("Forms/form_login.ui")
formularioLogin.btnLogar.clicked.connect(Controller.authenticate)
formularioLogin.btnIrCadastro.clicked.connect(Controller.abrirTelaCadastro)

formularioLogin.show()
app.exec()
