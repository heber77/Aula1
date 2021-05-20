from pagamentos import Pagamentos

class Cartao(Pagamentos):
    def __init__(self, numCartao, nomeTitular, dataValidade, cpf, cvv, total, meio_pagamento, descricao):
        super().__init__(total, meio_pagamento, descricao)
        self.numCartao = numCartao
        self.nomeTitular = nomeTitular
        self.dataValidade = dataValidade
        self.cpf = cpf
        self.cvv = cvv

    def autorizaPagamento(self):
        print("Seu pagamento foi confirmado")

    def setnumCartao(self, numCartao):
        self.numCartao = numCartao

    def getnumCartao (self):
        return self.numCartao
        

    def setnomeTitular(self, nomeTitular):
        self.nomeTitular = nomeTitular

    def getnomeTitular (self):
        return self.nomeTitular

    def setdataValidade(self, dataValidade):
        self.dataValidade = dataValidade

    def getdataValidade (self):
        return self.dataValidade

    def setcpf(self, cpf):
        self.cpf = cpf

    def getcpf (self):
        return self.cpf

    def setcvv(self, cvv):
        self.cvv = cvv

    def getcvv (self):
        return self.cvv