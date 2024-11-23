import sqlite3 as sq
def resgatar_token(nome):
    con = sq.connect("NutriTrack/source/models/database.db")
    cursor = con.cursor()
    query = "SELECT tokenAcesso FROM usuarios WHERE nome = ?"
    cursor.execute(query, (nome,))
    busca = cursor.fetchall()
    cursor.close()
    con.close()
    return busca