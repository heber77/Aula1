from curso import Curso

class cursosParaCompra(Curso):
    def __init__(self, nome, imagem, valor):
         super().__init__(nome, imagem)
         self.valor = valor

    def alteraPreço(self, valor):
        self.valor = valor

#P
