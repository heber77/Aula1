from Pessoa import Pessoa
import string
from random import choice

class Aluno(Pessoa):
    def __init__(self, nome, cpf, data_de_nascimento, email, telefone, senha):
        super().__init__(nome, cpf, data_de_nascimento, email, telefone)
        self.senha = senha
        self.codigo = self.geraCodigo()
        self.cursosMatriculados = []
        self.inadimplente = None
        self.situacaoMtricula = None


    def geraCodigo(self):
        tamanho = 9
        valores = string.digits
        codigo = ''
        for i in range(tamanho):
            codigo += choice(valores)
        return codigo

    def assistirAulas(self):
        pass

    def pagarMensalidade(self):
        if self.inadimplente:
            print("Não é necessário pagamento!")
        else:
            print("Pagamento será afetuado!")

    def escolherCurso(self, curso):



    def cancelaMatricula(self):
        if self.situacaoMtricula:
            self.situacaoMtricula = False
        else:
            print("Nada a ser feito.")


    def login(self, email, senha):
        cadastro = open("cadastros.txt", "r")
        loging = False
        #Le as linhas do arquivo
        for linha in cadastro.readlines():
            linha = linha.strip().split("|")
            email_arquivo = linha[1]
            senha_arquivo = linha[4]
            #Se as informações coincidirem loging = True
            if email == email_arquivo:
                if senha == senha_arquivo:
                    cadastro.close()
                    loging = True
                    print("Login efetuado!")
                    break
        if loging:
            print("E-mail ou senha incorretos!")
            return loging
        return loging



    def cadastro(self, nome, email, telefone,data_de_nascimento, senha):
        #Cadastro das informações em um arquivo
        cadastro = open("cadastros.txt", "w")
        cadastro.write(f"{nome}  {email}  {telefone}  {data_de_nascimento}  {senha}\n")
        cadastro.close()

    def cadastroTesteGratis(self, nome, email, telefone):
        cadastro = open("cadastros_teste.txt", "w")

        #Gerar senha
        tamanho = 10
        valores = string.ascii_lowercase + string.digits
        senha = ''
        for i in range(tamanho):
            senha += choice(valores)

        cadastro.write(f"{nome}|{email}|{telefone}|#|{senha}\n")
        cadastro.close()