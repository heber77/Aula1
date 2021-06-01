from Pessoa import Pessoa

class Professor(Pessoa):
    def __init__(self, nome, cpf, data_de_nascimento, email, telefone, salario, especialidade):
        super().__init__(nome, cpf, data_de_nascimento, email, telefone)
        self.salario = salario
        self.especialidade = especialidade

    def gravarAula(self):
        pass

    def darAulasAoVivo(self):
        pass
