from flask import Flask, jsonify, request
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname("InfoPerfilC"), "NutriTrack/backend/source/controllers")))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname("verificarSessao"), "NutriTrack/backend/source/models")))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname("login"), "NutriTrack/backend/source/controllers")))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname("registro"), "NutriTrack/backend/source/controllers")))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname("mudarSenha"), "NutriTrack/backend/source/controllers")))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname("atualizarPeso"), "NutriTrack/backend/source/models")))
from InfoPerfilC import infoPerfil # type: ignore
from verificarSessao import verificar_sessao # type: ignore
from login import Login # type: ignore
from atualizarPeso import atualizar_peso # type: ignore
from registro import Registro # type: ignore
from mudarSenha import MudarSenha # type: ignore



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
    atualizar_peso(novo_peso, token)
    return jsonify({"atualização": "bem sucedida"})

@app.route("/registro", methods=["POST"])
def fazer_registro():
    nome = request.json.get("usuario")
    senha = request.json.get("senha")
    csenha = request.json.get("csenha")
    peso = request.json.get("peso")
    genero = request.json.get("genero")
    idade = request.json.get("idade")
    altura = request.json.get("altura")
    if senha == csenha:
        registro = Registro(nome, senha, genero, peso, idade, altura)
        registro.adicionar_usuario()
        return "usuario adicionado com sucesso"
    else:
        return "as senhas são diferentes"
    
@app.route("/mudar_senha", methods={"POST"})
def alterar_senha():
    nome = request.json.get("usuario")
    senha = request.json.get("senha")
    nova_senha = MudarSenha(nome, senha)
    nova_senha.mudar_senha()
    return "senha alterada"
if __name__ == "__main__":
    app.run(debug=True)