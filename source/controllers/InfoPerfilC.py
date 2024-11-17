import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname("InfoPerfilM"), "NutriTrack\source\models")))
from InfoPerfilM import reqPerfil 

def infoPerfil(token):
    infoBruta = reqPerfil(token)
    imc = infoBruta[5] / (infoBruta[7] * infoBruta[7])
    if infoBruta[4]:
        genero = "masculino"
    else:
        genero = "feminino"
    infosDict = {"nome": infoBruta[1], "senha": infoBruta[2],
                 "token de acesso": infoBruta[3], "gênero": genero,
                 "peso": infoBruta[5], "idade": infoBruta[6],
                 "altura": infoBruta[7], "imc": imc}
    return infosDict
