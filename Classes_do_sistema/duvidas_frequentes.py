class video:
    def __init__(self, video, descricao, titulo, Nome_prof, Nome_alun):
        self.sistema_vid = video
        self.sistema_des = descricao
        self.Nome_prof = Nome_prof
        self.titulo = titulo
        self.Nome_alun = Nome_alun
        
    def usuario(self, Professor, Aluno ):
        self.usuario_1 = Professor
        self.usuario_2 = Aluno
        if Professor == Professor:
            print('Título:{} ',self.titulo)
            return '{}: {} = {} /n Descrição:{}'.format(self.usuario_1, self.Nome_prof,self.sistema_vid,self.sistema_des )
        else:
             print('Título:{} ',self.titulo)
             return '{}: {} = {} /n Descrição:{}'.format(self.usuario_2, self.Nome_alun,self.sistema_vid,self.sistema_des )

            