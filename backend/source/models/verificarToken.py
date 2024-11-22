import sqlite3 as sq

def verificarTokenAcesso():
    con = sq.connect("./NutriTrack/source/models/database.db")
    cursor = con.cursor()
    query = "SELECT tokenAcesso FROM usuario ORDER BY id DESC"
    cursor.execute(query)
    resultado = cursor.fetchone()
    return resultado