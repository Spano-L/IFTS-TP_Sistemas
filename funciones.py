import sqlite3 as sql

def crearDB():
    conexion = sql.conexionect("streamers.db")
    conexion.commit()
    conexion.close()

def crearTabla():
    conexion = sql.conexionect("streamers.db")
    cursor = conexion.cursor()
    cursor.execute(
        """CREATE TABLE streamers(
            name text,
            followers integer,
            subs integer
        )"""
    )
    conexion.commit()
    conexion.close()

def insertarFila(nombre, followers, subs):
    conexion = sql.conexionect("streamers.db")
    cursor = conexion.cursor()
    instruccion = f"INSERT INTO streamers values ('{nombre}',{followers},{subs})"
    cursor.execute(instruccion)
    conexion.commit()
    conexion.close()
    #Modificacion
    print("Datos cargados exitosamente.",nombre,followers,subs)

def leerFilas():
    conexion = sql.conexionect("streamers.db")
    cursor = conexion.cursor()
    instruccion = f"SELECT * from streamers"
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    conexion.commit()
    conexion.close()
    print(datos)

def insertarFilas(streamersList):
    conexion = sql.conexionect("streamers.db")
    cursor = conexion.cursor()
    instruccion = f"INSERT INTO streamers values (?,?,?)"
    cursor.executemany(instruccion, streamersList)
    conexion.commit()
    conexion.close()

def leerOrdenadoPor(field):
    conexion = sql.conexionect("streamers.db")
    cursor = conexion.cursor()
    instruccion = f"SELECT * from streamers ORDER BY {field} DESC"
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    conexion.commit()
    conexion.close()
    print(datos)

def buscar():
    conexion = sql.conexionect("streamers.db")
    cursor = conexion.cursor()
    instruccion = f"SELECT * from streamers WHERE subs < 21000"
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    conexion.commit()
    conexion.close()
    print(datos)

def actualizarCampos():
    conexion = sql.conexionect("streamers.db")
    cursor = conexion.cursor()
    instruccion = f"UPDATE streamers SET followers=1200 where name like 'elxo%'"
    cursor.execute(instruccion)
    conexion.commit()
    conexion.close()

def borrarFila():
    conexion = sql.conexionect("streamers.db")
    cursor = conexion.cursor()
    instruccion = f"DELETE  FROM streamers WHERE name='Ibai'"
    cursor.execute (instruccion)
    conexion.commit()
    conexion.close()


if __nombre__ == "__main__":
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