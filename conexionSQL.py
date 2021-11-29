import sqlite3 as sql

def conexionSQL(instruccion):
    conexion = sql.connect("sistema.sqlite")
    cursor = conexion.cursor()
    cursor.execute(instruccion)
    conexion.commit()
    conexion.close()