from Classes_do_sistema.Upload_video import upload_video
from Upload_video import video


class Descricao:
    def __init__(self, Usuario, Descrição):
        self.Descricao = Descrição
        self.Usuario= Usuario


def __repr__(self):
    return '{}: {}-{}'.format(self.__class__.__name__, self.Usuario, self.Descricao)

class video_case(video): 
    def case_adicionar(req, fileRoute, options ):
        upload_video(req, fileRoute, options)
         
    
    
    


