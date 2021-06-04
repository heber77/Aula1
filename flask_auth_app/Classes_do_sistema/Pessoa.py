class Pessoa:
    def __init__(self, nome, cpf, data_de_nascimento, email, telefone):
        self.nome = nome
        self.cpf = cpf
        self.data_de_nascimento = data_de_nascimento
        self.email = email
        self.telefone = telefone

    def alteraNome(self, nome):
        self.nome = nome

    def alteraDataNascimento(self, data_de_nascimento):
        self.data_de_nascimento = data_de_nascimento

    def alteraTelefone(self, telefone):
        self.telefone = telefone