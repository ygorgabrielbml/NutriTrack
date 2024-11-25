import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname("atualizarSenha"), "NutriTrack/backend/source/models")))
from atualizarSenha import atualizar_senha # type: ignore
from login import Login


class MudarSenha(Login):
    def __init__(self, nome, senha):
        super().__init__(nome, senha)

    def mudar_senha(self):
        atualizar_senha(self.senha, self.nome)