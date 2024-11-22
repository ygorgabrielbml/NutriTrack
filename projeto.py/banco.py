import sqlite3 as sq

#criação do código e do cursos
con = sq.connect("registro.db")
cursor = con.cursor()

#criação do banco de dados, tabela para tela de login
cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    login TEXT NOT NULL UNIQUE,
    senha TEXT NOT NULL,
    criado_em DATETIME DEFAULT CURRENT_TIMESTAMP
    )
""")

#criação de um banco de dados, informações do usuário após o login bem sucedido
cursor.execute("""
    CREATE TABLE IF NOT EXISTS perfil(
    sessao_id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    genero INTEGER COLLATE BINARY,
    peso NUMERIC,
    idade INTEGER,
    altura NUMERIC,
    FOREIGN KEY (sessao_id) REFERENCES usuarios (id)
    )
""")

con.commit()
cursor.close()
con.close()

def adicionar_usuario(login, senha):
    con = sq.connect("registro.db")
    cursor = con.cursor()
    try:
        cursor.execute("INSERT INTO usuarios (login, senha) VALUES (?, ?)", (login, senha))
        con.commit()
        print(f"Usário '{login}' adicionado com sucesso!")
    except sq.IntegrityError:
        print(f"Erro, o login '{login}' já existe.")
    except Exception as e:
        print(f"Erro ao adicionar o usuário: {e}")
    finally:
        cursor.close()
        con.close()

def deletar_usuario(login):
    con = sq.connect("registro.db")
    cursor = con.cursor()
    try:
        cursor.execute("DELETE FROM usuarios where login = ?", (login,))
        con.commit()
        if cursor.rowcount > 0:
            print(f"Usuário {login} deletado com sucesso!")
        else:
            print(f"Erro: usuário {login} não encontrado.")
    except Exception as e:
        print(f"Erro ao deletar usuário {e}")
    finally:
        cursor.close()
        con.close()
        