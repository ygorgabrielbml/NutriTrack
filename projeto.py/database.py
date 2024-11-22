import sqlite3


#função para adcionar usuário
def adcionar_usuario(login, senha):
    con = sqlite3.connect("./NutriTrack/source/models/database.db")
    cursor = con.cursor()
    
    try:
        cursor.execute("INSERT INTO dados (login, senha) VALUES (?, ?)", (login, senha))
        con.commit()
        print("Usuário adcionado com sucesso!")
    except sqlite3.Error as erro:
        print("Erro ao inserir novo usuário: ", erro)
    finally:
        cursor.close()
        con.close()

#função para remover usuário
def deletar_usuario(nome):
    con = sqlite3.connect("./NutriTrack/source/models/database.db")
    cursor = con.cursor()

    cursor.execute("DELETE FROM usuario where nome = ?", (nome,))
    con.commit()
    print("Usuário removido com sucesso.")

    cursor.close()
    con.close()

deletar_usuario("henrique")