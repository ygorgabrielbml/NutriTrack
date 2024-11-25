import sqlite3 as sq

def atualizar_senha(nova_senha, nome):
    con = sq.connect("NutriTrack/backend/source/models/database.db")
    cursor = con.cursor()
    query = "UPDATE usuario SET senha = ? WHERE nome = ?"
    cursor.execute(query, (nova_senha, nome))
    con.commit()
    cursor.close()
    con.close()