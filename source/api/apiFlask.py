import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname("InfoPerfilC."), "NutriTrack\source\controllers")))
from flask import Flask, jsonify, request
from flask_cors import CORS
from InfoPerfilC import infoPerfil

app = Flask(__name__)
CORS(app)

@app.route('/api/perfil', methods=['GET'])
def get_userInfo():
    perfil = infoPerfil(1)
    return jsonify(perfil)


if __name__ == "__main__":
    with app.app_context():  # Criar um contexto manualmente
        a = get_userInfo()
        print(a.get_data(as_text=True))  # Para testar a saída

