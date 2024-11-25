import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname("registrarUsuario"), "NutriTrackbackend/source/models")))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname("gerarTokenAcesso"), "NutriTrack/backend/source/utils")))
from registrarUsuario import adicionar_usuarioDB # type: ignore
from gerarTokenAcesso import gerarToken # type: ignore


class Registro:
    def __init__(self, nome, senha, genero, peso, idade, altura):
        self.nome = nome
        self.senha = senha
        self.genero = genero
        self.peso = peso
        self.idade = idade
        self.altura = altura

    def adicionar_usuario(self):
        tokenAcesso = gerarToken()
        adicionar_usuarioDB(self.nome, self.senha, tokenAcesso, self.genero, self.peso, self.idade, self.altura)

