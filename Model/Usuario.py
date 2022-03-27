
class Usuario:

    def __init__(self, nome, senha):
        self.nome = nome
        self.senha = senha

    def getNomeUsuario(self):
        return self.nome

    def getSenhaUsuario(self):
        return self.senha