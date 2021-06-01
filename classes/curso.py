class Curso:
    def __init__(self, nome, imagem):
        self.nome = nome
        self.imagem = imagem

    def armazelaAula(self, nomeDaAula, numeroDaAula):
        self.nomeDaAula = nomeDaAula
        self.numeroDaAula = numeroDaAula

    def gerenciarCurso(self, nome, imagem):
        self.nome = nome
        self.imagem = imagem

    def excluirCurso(self):
        cursoExcluido = input("Qual curso deseja excluir?\n")
