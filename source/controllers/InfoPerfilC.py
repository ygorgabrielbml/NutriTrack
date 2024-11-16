from InfoPerfilM import reqPerfil 

def infoPerfil(token):
    infoBruta = reqPerfil(token)
    print(infoBruta)

infoPerfil(1)
