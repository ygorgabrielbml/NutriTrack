import sqlite3 as sq

def verificar_sessao():
    con = sq.connect("NutriTrack/backend/source/models/database.db")
    cursor = con.cursor()
    query = "SELECT tokenAcesso FROM sessao WHERE status = 1"
    cursor.execute(query)
    resultado = cursor.fetchone()
    if resultado:
        print(resultado[0])
        return resultado[0]
    else:
        print("nenhuma sessao")
    cursor.close()
    con.close()

verificar_sessao()