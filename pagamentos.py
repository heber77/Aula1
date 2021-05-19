class Pagamentos():
    def __init__(self, total, meio_pagamento, descricao):
        self.total = total
        self.meio_pagamento = meio_pagamento
        self.descricao = descricao

    def calculaTotal(self):
        print("O total é: {self.total}")

    def fazerPagamento(self):
        print("quer fazer o pagamento?")

    def escolherMeioPgt(self):
        print("O meio escolhido foi {self.meio_pagamento}")

    def validaPagamento(self):
        print("pagamento feito com sucesso")

    def setTotal(self, total):
        self.total = total

    def getTotal (self):
        return self.total

    def setmeio_pagamento(self, meio_pagamento):
        self.meio_pagamento = meio_pagamento

    def getmeio_pagamento (self):
        return self.meio_pagamento

    def setdescricao(self, descricao):
        self.descricao = descricao

    def getdescricao(self):
        return self.descricao
