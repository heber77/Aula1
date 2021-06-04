from topicos import Topicos


class subTopicos(Topicos):
    def __init__(self, nomeTopico, conteudoTopico, nomeSubTopico, conteudoSubTopico):
        super().__init__(nomeTopico, conteudoTopico)
        self.nomeSubTopico = nomeSubTopico
        self.conteudoSubTopico = conteudoSubTopico

    def criarSubTopico(self, nomeSubTopico, conteudoSubTopico):
        self.nomeSubTopico = nomeSubTopico
        self.conteudoSubTopico = conteudoSubTopico

    def gerenciarSubTopico(self, nomeSubTopico, conteudoSubTopico):
        self.nomeSubTopico = nomeSubTopico
        self.conteudoSubTopico = conteudoSubTopico


# P
