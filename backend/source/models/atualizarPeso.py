import sqlite3 as sq

def atualizar_peso(peso, tokenAcesso):
    con = sq.connect("NutriTrack/backend/source/models/database.db")
    cursor = con.cursor()
    query = "UPDATE usuario SET peso = ? WHERE tokenAcesso = ?"
    cursor.execute(query, (peso, tokenAcesso))
    con.commit()
    cursor.close()
    con.close()

