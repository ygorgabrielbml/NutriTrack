import sqlite3 as sq

def adicionar_meal_ingredient(meal_id, ingredients):
    con = sq.connect("NutriTrack/backend/source/models/database.db")
    cursor =  con.cursor()
    query = "INSERT INTO meal_ingredients (meal_id, ingredient) VALUES (?, ?)"
    cursor.execute(query, (meal_id, ingredients))
    con.commit()
    cursor.close()
    con.close()