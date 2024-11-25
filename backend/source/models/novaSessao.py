import sqlite3 as sq

def nova_sessao(status, tokenAcesso):
    con = sq.connect("NutriTrack/backend/source/models/database.db")
    cursor = con.cursor()
    query = "INSERT INTO sessao (status, tokenAcesso) VALUES (?, ?)"
    cursor.execute(query, (status, tokenAcesso))
    con.commit()
    cursor.close()
    con.close()
    