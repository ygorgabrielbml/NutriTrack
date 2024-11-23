import os 
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname("buscarLogin"), "NutriTrack/backend/source/models")))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname("novaSessao"), "NutriTrack/backend/source/models")))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname("resgatarToken"), "NutriTrack/backend/source/models")))
from buscarLogin import buscarLogin
from novaSessao import nova_sessao
from resgatarToken import resgatar_token
class Login:
    def __init__(self, nome, senha):
        self.nome = nome
        self.senha = senha
    
    def criar_sessao(self):
        tokenAcesso = resgatar_token(self.nome)
        nova_sessao(True, tokenAcesso)

    def autenticar_login(self):
        senhaBD = buscarLogin(self.nome)
        if senhaBD == self.senha:
            self.criar_sessao()
            return "Login efetuado com sucesso"
        else:
            return "Nome de usuário ou senha incorretos, tente novamente"