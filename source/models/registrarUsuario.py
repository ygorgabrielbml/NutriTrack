import sqlite3

def adicionar_usuarioDB(nome, senha, tokenAcesso, genero, peso, idade, altura):
    con = sqlite3.connect("./NutriTrack/source/models/database.db")
    cursor = con.cursor()
    
    try:
        cursor.execute("INSERT INTO usuario (nome, senha, tokenAcesso, genero, peso, idade, altura) VALUES (?, ?, ?, ?, ?, ?, ?)", (nome, senha, tokenAcesso, genero, peso, idade, altura))
        con.commit()
    except sqlite3.Error as erro:
        return "Erro ao inserir novo usuário: ", erro
    finally:
        cursor.close()
        con.close()