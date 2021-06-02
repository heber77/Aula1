
class cursosParaCompra:

    def lista_cursos(self, Nome_arquivo):
        arquivo = open( Nome_arquivo+'.txt', 'r')
        for linha in arquivo:
            for itens in linha:
             linha = linha.rstrip()
             return '{}: {},'.format(itens, linha)
        arquivo.close()


    def Meu_switch( opcoes, Nome_arquivo):
       opcoes = {
            print(cursosParaCompra.lista_cursos(Nome_arquivo))
       }
       return opcoes.get( opcoes, "Opção inválida")


class registro_de_pedidos:

    def selecionado(self, Nome_arquivo, numero_item = 0 ):
        self.Nome_arquivo = Nome_arquivo
        arquivo = open(Nome_arquivo +'.txt', 'w' )
        arquivo.write(cursosParaCompra.Meu_switch(numero_item))
        arquivo.close()

    def selecionar_mais(self, numero_item = 0):
        arquivo= open(self.Nome_arquivo +'.txt', 'a+')
        arquivo.seek(0)
        arquivo.write(cursosParaCompra.Meu_switch(numero_item))



