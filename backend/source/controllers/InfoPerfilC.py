import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname("InfoPerfilM"), "NutriTrack/backend/source/models")))
from InfoPerfilM import reqPerfil # type: ignore

def infoPerfil(token):
    infoBruta = reqPerfil(token)
    if infoBruta:
        if infoBruta[4]:
            genero = "masculino"
        else:
            genero = "feminino"
        infosDict = {"nome": infoBruta[1], "genero": genero,
                    "peso": infoBruta[5], "idade": infoBruta[6],
                    "altura": infoBruta[7]}
        return infosDict
    else:
        return None