import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname("verificarToken"), "NutriTrack/backend/source/models")))
from verificarToken import verificarTokenAcesso

def gerarToken():
    token = verificarTokenAcesso()
    if not token:
        novo_token = 1
    else:
        novo_token =  token[0] + 1
    return novo_token
