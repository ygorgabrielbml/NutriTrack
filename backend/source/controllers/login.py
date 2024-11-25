import os 
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname("buscarLogin"), "NutriTrack/backend/source/models")))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname("novaSessao"), "NutriTrack/backend/source/models")))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname("resgatarToken"), "NutriTrack/backend/source/models")))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname("fecharSessao"), "NutriTrack/backend/source/models")))
from buscarLogin import buscarLogin # type: ignore
from novaSessao import nova_sessao # type: ignore
from resgatarToken import resgatar_token # type: ignore
from fecharSessao import fechar_sessao # type: ignore


class Login:
    def __init__(self, nome, senha):
        self.nome = nome
        self.senha = senha
    
    def criar_sessao(self):
        tokenAcesso = resgatar_token(self.nome)
        fechar_sessao()
        nova_sessao(True, tokenAcesso[0][0])

    def autenticar_login(self):
        senhaBD = buscarLogin(self.nome)
        if senhaBD[0] == self.senha:
            return True
        else:
            return False