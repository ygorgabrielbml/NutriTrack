import sqlite3 as sq
con = sq.connect("NutriTrack/backend/source/models/database.db")
cursor = con.cursor()
cursor.execute("DELETE FROM sessao")
con.commit()
cursor.close()
con.close()