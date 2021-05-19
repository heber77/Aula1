from pagamentos import Pagamentos

class Boleto(Pagamentos):
    def __init__(self, codigo, total, meio_pagamento, descricao):
        super().__init__(total, meio_pagamento, descricao)
        self.codigo = codigo

    def gera_boleto(self):
        print("O codigo do seu boleto eh {self.codigo}")


    def setCodigo(self, codigo):
        self.codigo = codigo

    def getCodigo (self):
        return self.codigo
