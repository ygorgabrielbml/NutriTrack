import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname("registrarUsuario"), "NutriTrack\source\models")))
from registrarUsuario import adicionar_usuarioDB


class Usuario:
    def __init__(self, nome, senha, tokenAcesso, genero, peso, idade, altura):
        self.nome = nome
        self.senha = senha
        self.tokenAcesso = tokenAcesso
        self.genero = genero
        self.peso = peso
        self.idade = idade
        self.altura = altura

    def adicionar_usuario(self):
        adicionar_usuarioDB(self.nome, self.senha, self.tokenAcesso, self.genero, self.peso, self.idade, self.altura)

