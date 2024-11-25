import sqlite3 as sq

def adicionar_meal(meal_name, tokenAcesso):
    con = sq.connect("NutriTrack/backend/source/models/database.db")
    cursor = con.cursor()
    query = "INSERT INTO meals (meal_name, tokenAcesso) VALUES (?, ?)"
    cursor.execute(query, (meal_name, tokenAcesso))
    con.commit()
    cursor.close()
    con.close()