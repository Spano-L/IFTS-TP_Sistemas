import sqlite3 as sql
import os
import sys

def borrarPantalla():
    os.system("cls")

def menu():
    menuPrincipal = """///  Menú principal - Seleccione una acción  ///
            \n[1] - Alta
            \n[2] - Modificacion
            \n[3] - Baja
            \n[4] - Busqueda
            \n[5] - Salir\n"""
    print(menuPrincipal)

def submenuTablas():
    submenu = """
        \n[1] - Categoria
        \n[2] - Clientes
        \n[3] - Facturas
        \n[4] - Logistica
        \n[5] - Productos
        \n[6] - Proveedores
        \n[7] - Venta_items
        \n"""
    print(submenu)
    seleccionSubmenu = input("Seleccione una tabla: ")
    borrarPantalla()
    if seleccionSubmenu ==str(1):
        print("Seleccion 1 - Categoria\n")
        seleccionSub = "uno"
        return seleccionSub
    elif seleccionSubmenu ==str(2):
        print("Seleccion 2 - Clientes\n")
        seleccionSub = "dos"
        return seleccionSub
    elif seleccionSubmenu ==str(3):
        print("Seleccion 3 - Facturas\n")
        seleccionSubmenu = "tres"
        return seleccionSubmenu
    elif seleccionSubmenu ==str(4):
        print("Seleccion 4 - Logistica\n")
        seleccionSubmenu = "cuatro"
        return seleccionSubmenu
    elif seleccionSubmenu ==str(5):
        print("Seleccion 5 - Productos\n")
        seleccionSubmenu = "cinco"
        return seleccionSubmenu
    elif seleccionSubmenu ==str(6):
        print("Seleccion 6 - Proveedores\n")
        seleccionSubmenu = "seis"
        return seleccionSubmenu
    elif seleccionSubmenu ==str(7):
        print("Seleccion 7 - Venta_items\n")
        seleccionSubmenu = "siete"
        return seleccionSubmenu


def insertarFila(campo1, campo2, campo3):
    conexion = sql.connect("sistema.sqlite")
    cursor = conexion.cursor()
    instruccion = f"INSERT INTO nombre_tabla VALUES ('{nombre_columna1}',{nombre_columna2},{nombre_columna3})"
    cursor.execute(instruccion)
    conexion.commit()
    conexion.close()
    #Modificacion
    print("Datos cargados exitosamente.",campo1, campo2, campo3)

#Descubri que al poner {la variable dentro de llaves} funciona dentro del comando sqlite :)
#Dejo moficada la funcion, para luego adaptarla correctamente.
def leerFilas():
    conexion = sql.connect("sistema.sqlite")
    cursor = conexion.cursor()
    nombreTabla = input("Ingrese el nombre de la tabla:")
    instruccion = f"SELECT * FROM {nombreTabla}"
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    conexion.commit()
    conexion.close()
    print(datos)

#prueba
def leerFilas123():
    conexion = sql.connect("sistema.sqlite")
    cursor = conexion.cursor()
    nombreTabla = input("Ingrese el nombre de la tabla:")
    instruccion = f"SELECT * FROM {nombreTabla}"
    for row in cursor.execute(instruccion):
        print(row)
    #datos = cursor.fetchall()
    conexion.commit()
    conexion.close()
    #print(datos)

def insertarFilas(nombre_lista):
    conexion = sql.connect("sistema.sqlite")
    cursor = conexion.cursor()
    instruccion = f"INSERT INTO nombre_tabla VALUES (?,?,?)"
    cursor.executemany(instruccion, nombre_lista)
    conexion.commit()
    conexion.close()

def leerOrdenadoPor(nombre_columna):
    conexion = sql.connect("sistema.sqlite")
    cursor = conexion.cursor()
    instruccion = f"SELECT * FROM nombre_tabla ORDER BY {nombre_columna} DESC"
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    conexion.commit()
    conexion.close()
    print(datos)

def buscar():
    conexion = sql.connect("sistema.sqlite")
    cursor = conexion.cursor()
    instruccion = f"SELECT * FROM nombre_tabla WHERE campo3 < 21000"
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    conexion.commit()
    conexion.close()
    print(datos)

def actualizarCampos():
    conexion = sql.connect("sistema.sqlite")
    cursor = conexion.cursor()
    instruccion = f"UPDATE nombre_tabla SET campo2=1200 WHERE columna1 LIKE 'elxo%'"
    cursor.execute(instruccion)
    conexion.commit()
    conexion.close()

def borrarFila():
    conexion = sql.connect("sistema.sqlite")
    cursor = conexion.cursor()
    instruccion = f"DELETE  FROM nombre_tabla WHERE campo1='Ibai'"
    cursor.execute (instruccion)
    conexion.commit()
    conexion.close()

"""Before executing code, Python interpreter reads source file and define few special variables/global variables. 
If the python interpreter is running that module (the source file) as the main program, it sets the special __name__ variable to have a value “__main__”. If this file is being imported from another module, __name__ will be set to the module’s name. Module’s name is available as value to __name__ global variable.
A module is a file containing Python definitions and statements. The file name is the module name with the suffix .py appended. """
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


# Probando funciones

def confirmarOperacion():
    print("Los datos fueron cargados exitosamente.\n")

def enConstruccion():
    print("Esta seccion del programa se encuentra en construccion.\n")

def insertarEntidadCategoria():
    conexion = sql.connect("sistema.sqlite")
    cursor = conexion.cursor()
    categoria_nombre = input("Ingrese nombre de categoria: ")
    categoria_info = input("Ingrese informacion de la categoria: ")
    instruccion = f"INSERT INTO categorias (categoria_nombre,categoria_info) VALUES ('{categoria_nombre}','{categoria_info}')"
    cursor.execute(instruccion)
    conexion.commit()
    conexion.close()
    confirmarOperacion()

def insertarEntidadCliente():
    conexion = sql.connect("sistema.sqlite")
    cursor = conexion.cursor()
    cliente_nombre = input("Ingrese nombre de cliente: ")
    cliente_zona = input("Ingrese zona de cliente: ")
    cliente_direccion = input("Ingrese direccion de cliente: ")
    cliente_telefono = input("Ingrese telefono de cliente: ")
    cliente_email = input("Ingrese email de cliente:")
    cliente_mayorista = int(input("Ingrese 1 si el cliente es mayorista. Ó ingrese 0 si es minorista."))
    instruccion = f"INSERT INTO clientes (cliente_nombre,cliente_zona,cliente_direccion,cliente_telefono,cliente_email,cliente_mayorista) VALUES ('{cliente_nombre}','{cliente_zona}','{cliente_direccion}','{cliente_telefono}','{cliente_email}','{cliente_mayorista}')"
    cursor.execute(instruccion)
    conexion.commit()
    conexion.close()
    confirmarOperacion()

def insertarFactura():
    conexion = sql.connect("sistema.sqlite")
    cursor = conexion.cursor()
    instruccion = f"INSERT INTO facturas (categoria_nombre,categoria_info) VALUES ('{categoria_nombre}','{categoria_info}')"
    cursor.execute(instruccion)
    conexion.commit()
    conexion.close()