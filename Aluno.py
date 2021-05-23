from Pessoa import Pessoa

class Aluno(Pessoa):
    def __init__(self, nome, cpf, data_de_nascimento, email, telefone, senha):
        super().__init__(nome, cpf, data_de_nascimento, email, telefone)
        self.senha = senha

    def assistirAulas(self):
        pass

    def pagarMensalidade(self):


    def escolherCurso(self, curso):


    def cancelaMatricula(self):
        pass

    def login(self):
        pass

    def cadastro(self):
        pass

    def cadastroTesteGratis(self):
        pass