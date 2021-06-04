from pagamentos import Pagamentos

class Pix(Pagamentos):
    def __init__(self, codigoPIX, qrcod, total, meio_pagamento, descricao):
        super().__init__(total, meio_pagamento, descricao)
        self.codigoPix = codigoPIX
        self.qrcod = qrcod

    def geraQrcode(self):
        print("Sua chave é {self.qrcod}")

    def setcodigoPix(self, codigoPix):
        self.codigoPix = codigoPix
        

    def getcodigoPix (self):
        return self.codigoPix

    def setqrcod(self, qrcod):
        self.qrcod = qrcod


    def getqrcod (self):
        return self.qrcod