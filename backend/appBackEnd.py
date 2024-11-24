from flask import Flask, jsonify, request
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname("InfoPerfilC"), "NutriTrack/backend/source/controllers")))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname("verificarSessao"), "NutriTrack/backend/source/models")))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname("login"), "NutriTrack/backend/source/controllers")))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname("atualizarPeso"), "NutriTrack/backend/source/models")))
from InfoPerfilC import infoPerfil # type: ignore
from verificarSessao import verificar_sessao # type: ignore
from login import Login # type: ignore
from atualizarPeso import atualizar_peso # type: ignore



app = Flask(__name__)


@app.route("/login", methods=["POST"])
def fazer_login():
    try:    
        usuario = request.json.get("usuario")
        senha = request.json.get("senha")
        login = Login(usuario, senha)
        login_autenticado = login.autenticar_login()
        if login_autenticado:
            login.criar_sessao()
            return jsonify({"login": "bem sucedido"})
        else:
            return jsonify({"login": "mal sucedido"})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route("/perfil/mostrar_infos", methods=["GET"])
def get_infoPerfil():
    token = verificar_sessao()
    info_perfil = infoPerfil(token)
    return jsonify(info_perfil)

@app.route("/perfil/mudar_peso", methods=["POST"])
def update_peso():
    token = verificar_sessao()
    novo_peso = request.json.get("peso")
    print(novo_peso, token)
    atualizar_peso(novo_peso, token)
    return jsonify({"atualização": "bem sucedida"})


if __name__ == "__main__":
    app.run(debug=True)