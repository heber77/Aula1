
class Pedidos:
     
    def __init__(self, codigo):
         self.codigo = codigo


    def itens_selecionados(self, Nome_arquivo):
        arquivo = open('{}'+'.txt', 'a+').__format__(Nome_arquivo)
        for linha in arquivo:
            for itens in linha:
              linha= linha.rstrip()
              print([itens]+ linha)
        arquivo.close()


    def Calcular(self, Nome_arquivo, somar = 0):
        arquivo = open('{}'+'.txt', 'r').__format__(Nome_arquivo)
        for linha in arquivo:
              lin= linha.select(self.valor)
              somar = lin + somar
              print(somar)
        Total = somar
        return print(Total)

    def removendo_pedido(self,Nome_arquivo, codigo ):
        arquivo = open('{}'+'.txt', 'a+' ).__format__(Nome_arquivo)
        self.codigo = codigo
        for linha in arquivo:
            linha = linha.rstrip()
            lin = linha.select(self.codigo)
            if lin == True:
             retirar = lin.remove(linha)   
        arquivo.close()
        return '{} : Foi removido da lista de pedidos'.__format__(retirar)
        



