import sqlite3 as sq

def reqPerfil(token):
    con = sq.connect("./NutriTrack/source/models/database.db")
    cursor = con.cursor()
    try:
        cursor.execute("SELECT * FROM usuario WHERE tokenAcesso = ?", (token,))
        busca = cursor.fetchone()
        return busca
    except sq.Error as erro:
        return erro
    finally:
        cursor.close()
        con.close()