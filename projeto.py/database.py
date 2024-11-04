import sqlite3

#criação do código e do cursos
con = sqlite3.connect("registro.db")
cursor = con.cursor()

#criação do banco de dados os valores de registro
cursor.execute("""
    CREATE TABLE IF NOT EXISTS dados(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    login TEXT UNIQUE NOT NULL,
    senha TEXT NOT NULL)
""")
con.commit()
cursor.close()
con.close()

#função para adcionar usuário
def adcionar_usuario(login, senha):
    con = sqlite3.connect("registro.db")
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
def deletar_usuario(login):
    con = sqlite3.connect("registro.db")
    cursor = con.cursor()

    cursor.execute("DELETE FROM dados where login = ?", (login,))
    con.commit()
    print("Usuário removido com sucesso.")

    cursor.close()
    con.close()
