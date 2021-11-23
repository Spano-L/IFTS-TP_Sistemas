import sqlite3 as sql

def createDB():
    conn = sql.connect("streamers.db")
    conn.commit()
    conn.close()

def createTable():
    conn = sql.connect("streamers.db")
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE streamers(
            name text,
            followers integer,
            subs integer
        )"""
    )
    conn.commit()
    conn.close()

def insertRow(nombre, followers, subs):
    conn = sql.connect("streamers.db")
    cursor = conn.cursor()
    instruccion = f"INSERT INTO streamers values ('{nombre}',{followers},{subs})"
    cursor.execute(instruccion)
    conn.commit()
    conn.close()
    #Modificacion
    print("Datos cargados exitosamente.",nombre,followers,subs)

def readRows():
    conn = sql.connect("streamers.db")
    cursor = conn.cursor()
    instruccion = f"SELECT * from streamers"
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()
    print(datos)

def insertRows(streamersList):
    conn = sql.connect("streamers.db")
    cursor = conn.cursor()
    instruccion = f"INSERT INTO streamers values (?,?,?)"
    cursor.executemany(instruccion, streamersList)
    conn.commit()
    conn.close()

def readOrdered(field):
    conn = sql.connect("streamers.db")
    cursor = conn.cursor()
    instruccion = f"SELECT * from streamers ORDER BY {field} DESC"
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()
    print(datos)

def search():
    conn = sql.connect("streamers.db")
    cursor = conn.cursor()
    instruccion = f"SELECT * from streamers WHERE subs < 21000"
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()
    print(datos)

def updateFields():
    conn = sql.connect("streamers.db")
    cursor = conn.cursor()
    instruccion = f"UPDATE streamers SET followers=1200 where name like 'elxo%'"
    cursor.execute(instruccion)
    conn.commit()
    conn.close()

def deleteRow():
    conn = sql.connect("streamers.db")
    cursor = conn.cursor()
    instruccion = f"DELETE  FROM streamers WHERE name='Ibai'"
    cursor.execute (instruccion)
    conn.commit()
    conn.close()


if __name__ == "__main__":
    #createDB()
    #createTable()
    #insertRow("Ibai",700000,24000)
    #insertRow("Emiliano",800000,10000)
    #readRows()
    streamers = [
        ("ElXokas", 1000000, 50000),
        ("Crisada",2000000,21000),
        ("Aurplay",800000,20000)
    ]
    #insertRows(streamers)
    #readOrdered("subs")
    #search()
    #updateFields()
    #deleteRow()