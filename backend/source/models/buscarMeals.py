import sqlite3 as sq

def buscar_meals(tokenAcesso):
    con = sq.connect("NutriTrack/backend/source/models/database.db")
    cursor = con.cursor()
    query = "SELECT meal_name FROM meals WHERE tokenAcesso = ?"
    cursor.execute(query, (tokenAcesso,))
    resultado = cursor.fetchall()
    cursor.close()
    con.close()
    return resultado