import sqlite3 as sq
def resgatar_token(nome):
    con = sq.connect("NutriTrack/backend/source/models/database.db")
    cursor = con.cursor()
    query = "SELECT tokenAcesso FROM usuario WHERE nome = ?"
    cursor.execute(query, (nome,))
    busca = cursor.fetchall()
    cursor.close()
    con.close()
    return busca