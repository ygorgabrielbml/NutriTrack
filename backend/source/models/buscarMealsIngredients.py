import sqlite3 as sq

def buscar_meals_ingredients(meal_id):
    con = sq.connect("NutriTrack/backend/source/models/database.db")
    cursor = con.cursor()
    query = "SELECT ingredient FROM meal_igredients WHERE meal_id = ?"
    cursor.execute(query, (meal_id,))
    resultado = cursor.fetchone()
    cursor.close()
    con.close()
    return resultado