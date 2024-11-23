import sqlite3 as sq

def buscarLogin(nome):
    con = sq.connect("NutriTrack/backend/source/models/database.db")
    cursor = con.cursor()
    query = "SELECT senha FROM usuario where nome = ?"
    cursor.execute(query, (nome,))
    busca = cursor.fetchone()
    cursor.close()
    con.close()
    return busca