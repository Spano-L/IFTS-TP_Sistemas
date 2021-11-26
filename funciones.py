import sqlite3 as sql

def crearDB():
    conexion = sql.connect("nombreBBDD.db")
    conexion.commit()
    conexion.close()

def crearTabla():
    conexion = sql.connect("nombreBBDD.db")
    cursor = conexion.cursor()
    cursor.execute(
        """CREATE TABLE nombre_tabla(
            nombre_columna1 text,
            nombre_columna2 integer,
            nombre_columna3 integer
        )"""
    )
    conexion.commit()
    conexion.close()

def insertarFila(campo1, campo2, campo3):
    conexion = sql.connect("nombreBBDD.db")
    cursor = conexion.cursor()
    instruccion = f"INSERT INTO nombre_tabla VALUES ('{nombre_columna1}',{nombre_columna2},{nombre_columna3})"
    cursor.execute(instruccion)
    conexion.commit()
    conexion.close()
    #Modificacion
    print("Datos cargados exitosamente.",campo1, campo2, campo3)

def leerFilas():
    conexion = sql.connect("nombreBBDD.db")
    cursor = conexion.cursor()
    instruccion = f"SELECT * FROM nombre_tabla"
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    conexion.commit()
    conexion.close()
    print(datos)

def insertarFilas(nombre_lista):
    conexion = sql.connect("nombreBBDD.db")
    cursor = conexion.cursor()
    instruccion = f"INSERT INTO nombre_tabla VALUES (?,?,?)"
    cursor.executemany(instruccion, nombre_lista)
    conexion.commit()
    conexion.close()

def leerOrdenadoPor(nombre_columna):
    conexion = sql.connect("nombreBBDD.db")
    cursor = conexion.cursor()
    instruccion = f"SELECT * FROM nombre_tabla ORDER BY {nombre_columna} DESC"
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    conexion.commit()
    conexion.close()
    print(datos)

def buscar():
    conexion = sql.connect("nombreBBDD.db")
    cursor = conexion.cursor()
    instruccion = f"SELECT * FROM nombre_tabla WHERE campo3 < 21000"
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    conexion.commit()
    conexion.close()
    print(datos)

def actualizarCampos():
    conexion = sql.connect("nombreBBDD.db")
    cursor = conexion.cursor()
    instruccion = f"UPDATE nombre_tabla SET campo2=1200 WHERE columna1 LIKE 'elxo%'"
    cursor.execute(instruccion)
    conexion.commit()
    conexion.close()

def borrarFila():
    conexion = sql.connect("nombreBBDD.db")
    cursor = conexion.cursor()
    instruccion = f"DELETE  FROM nombre_tabla WHERE campo1='Ibai'"
    cursor.execute (instruccion)
    conexion.commit()
    conexion.close()


if __name__ == "__main__":
    #crearDB()
    #crearTabla()
    #insertarFila("Ibai",700000,24000)
    #insertFila("Emiliano",800000,10000)
    #leerFilas()
    lista = [
        ("ElXokas", 1000000, 50000),
        ("Crisada",2000000,21000),
        ("Aurplay",800000,20000)
    ]
    #insertarFilas(nombre_tabla)
    #leerOrdenadoPor("nombre_columna3")
    #buscar()
    #actualizarCampos()
    #borrarFila()