import sqlite3 as sq

def fechar_sessao():
    con = sq.connect("NutriTrack/backend/source/models/database.db")
    cursor = con.cursor()
    query = "UPDATE sessao SET status = 0 WHERE status = 1"
    cursor.execute(query)
    con.commit()
    cursor.close()
    con.close()

fechar_sessao()