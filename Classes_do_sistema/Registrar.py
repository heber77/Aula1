class registrar:

    itens = 0
    seq = 0
    objects = []

    def __init__(self, nome, valor, ):
        self.codigo = None
        self.nome_do_curso = nome
        self.valor = valor

    def save (self):
        self.__class__.seq += 1
        self.codigo = self.__class__.seq
        self.__class__.objects.append(self)

    def __str__(self):
        return self.nome_do_curso

    def __repr__(self):
        return '<{}: {:0>4} - {} - {}>\n'.format(self.__class__.__name__, self.codigo,self.nome_do_curso,self.valor)

    @classmethod
    def all(cls):
        return cls.objects


    def criando_arquivo(self, Nome_arquivo):
         self.Nome_arquivo = input()
         arquivo = open(Nome_arquivo+'.txt', 'w')
         arquivo.close()

    def insere_dado (self,Nome_arquivo, Nome_curso, Valor_curso, R ):
        self.Nome_curso = input()
        for itens in Nome_arquivo +'.txt':
            R[itens] = registrar(Nome_curso, Valor_curso)
            R[itens].save()
            arquivo = open( '{}'+'.txt', 'a').__format__(Nome_arquivo)
            arquivo.write(print(registrar.all()))
            arquivo.close()
