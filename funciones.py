import sqlite3 as sql
import os
from conexionSQL import conexionSQL

def borrarPantalla():
    os.system("cls")

def menuPrincipal(): 
    menu()
    seleccion=str(input("Ingrese una opción: "))
    borrarPantalla()

def menu():
    menuPrincipal = """///  Menú principal - Seleccione una acción  ///
            \n[1] - Alta
            \n[2] - ModificaciÓn
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
        \n[8] - Atras
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
   
# Funciones con mensajes de información.

def menuPrincipal(): 
    menu()
    seleccion = str(input("Ingrese una opción: "))
    borrarPantalla()

def confirmarAlta():
    print("Los datos fueron cargados exitosamente.\n")

def confirmarModificacion():
    print("El campo fue modificado exitosamente.\n")

def confirmarBaja():
    print("La entidad fue borrada exitosamente.\n")

def enConstruccion():
    print("Esta sección del programa se encuentra en construcción.\n")

# Funciones de alta.

def insertarEntidadCategoria():
    categoria_nombre = input("Ingrese nombre de categoria: ")
    categoria_info = input("Ingrese información de la categoria: ")
    instruccion = f"INSERT INTO categorias (categoria_nombre, categoria_info) VALUES ('{categoria_nombre}','{categoria_info}')"
    conexionSQL(instruccion)
    confirmarAlta()

def insertarEntidadCliente():
    cliente_nombre = input("Ingrese nombre de cliente: ")
    cliente_zona = input("Ingrese zona de cliente: ")
    cliente_direccion = input("Ingrese dirección de cliente: ")
    cliente_telefono = input("Ingrese teléfono de cliente: ")
    cliente_email = input("Ingrese email de cliente:")
    cliente_mayorista = int(input("Ingrese 1 si el cliente es mayorista. ó ingrese 0 si es minorista."))
    instruccion = f"INSERT INTO clientes (cliente_nombre, cliente_zona, cliente_direccion, cliente_telefono, cliente_email, cliente_mayorista) VALUES ('{cliente_nombre}','{cliente_zona}','{cliente_direccion}','{cliente_telefono}','{cliente_email}','{cliente_mayorista}')"
    conexionSQL(instruccion)
    confirmarAlta()

def insertarProducto():
    producto_nombre = input("Ingrese nombre del producto: ")
    producto_categoria = int(input("Ingrese categoría del producto: "))
    producto_precio = float(input("Ingrese el precio del producto: "))
    producto_proveedor_id = int(input("Ingrese el ID del proveedor: "))
    instruccion = f"INSERT INTO productos (producto_nombre, producto_categoria, producto_precio, proveedor_id) VALUES ('{producto_nombre}','{producto_categoria}','{producto_precio}','{producto_proveedor_id}')"
    conexionSQL(instruccion)
    confirmarAlta()

def insertarProveedor():
    proveedor_nombre = input("Ingrese nombre del proveedor: ")
    proveedor_direccion = input("Ingrese dirección del proveedor: ")
    proveedor_ciudad = input("Ingrese ciudad del proveedor: ")
    proveedor_email = input("Ingrese el mail del proveedor: ")
    proveedor_telefono = input("Ingrese teléfono del proveedor: ")
    instruccion = f"INSERT INTO proveedores (proveedor_nombre, proveedor_direccion, proveedor_ciudad, proveedor_email, proveedor_telefono) VALUES ('{proveedor_nombre}','{proveedor_direccion}','{proveedor_ciudad}','{proveedor_email}','{proveedor_telefono}')"
    conexionSQL(instruccion)
    confirmarAlta()

# Funciones de modificación

def modificarCategoria():
    campoId = int(input("Ingrese ID de la categoría que desea modificar: "))
    flag = str(input("(1) para cambiar el nombre de la categoría\n(2) para cambiar la información de la categoría\nIngrese su opcion: "))
    if flag == str(1):
        valor = input("Ingrese nuevo nombre: ")
        campo = "categoria_nombre"
    elif flag == str(2):
        valor = input("Ingrese nueva información: ")
        campo = "categoria_info" 
    instruccion = f"UPDATE categorias SET '{campo}'='{valor}' WHERE categoria_id='{campoId}'"
    conexionSQL(instruccion)
    confirmarModificacion()

def modificarCliente():
    campoId = int(input("Ingrese ID del cliente que desea modificar: "))
    flag = str(input("(1) para cambiar nombre de cliente\n(2) para cambiar zona del cliente\n(3) para cambiar dirección del cliente\n(4) para cambiar teléfono del cliente\n(5) para cambiar email del cliente\nIngrese su opción: "))
    if flag == str(1):
        valor = input("Ingrese nuevo nombre del cliente: ")
        campo = "cliente_nombre"
    elif flag == str(2):
        valor = input("Ingrese nueva zona del cliente: ")
        campo = "cliente_zona"
    elif flag == str(3):
        valor = input("Ingrese nueva dirección: ")
        campo = "cliente_direccion"
    elif flag == str(4):
        valor = input("Ingrese nuevo teléfono: ")
        campo = "cliente_telefono"
    elif flag == str(5):
        valor = input("Ingrese nuevo email : ")
        campo = "cliente_email"
    instruccion = f"UPDATE clientes SET '{campo}'='{valor}' WHERE cliente_id='{campoId}'"
    conexionSQL(instruccion)
    confirmarModificacion()

# Funciones de baja

def borrarCategoria():
    valor = int(input("Ingrese ID de categoría que desea borrar: "))
    instruccion = f"DELETE FROM categorias WHERE categoria_id={valor}"
    conexionSQL(instruccion)
    confirmarBaja()

def borrarCliente():
    valor = int(input("Ingrese ID de cliente que desea borrar: "))
    instruccion = f"DELETE FROM clientes WHERE cliente_id={valor}"
    conexionSQL(instruccion)
    confirmarBaja()

def borrarProducto():
    valor = int(input("Ingrese ID de producto que desea borrar: "))
    instruccion = f"DELETE FROM productos WHERE producto_id={valor}"
    conexionSQL(instruccion)
    confirmarBaja()

def borrarProveedor():
    valor = int(input("Ingrese ID de proveedor que desea borrar: "))
    instruccion = f"DELETE FROM proveedores WHERE proveedor_id={valor}"
    conexionSQL(instruccion)
    confirmarBaja()

# Funciones de busqueda

def buscarCategoria():
    conexion = sql.connect("sistema.sqlite")
    cursor = conexion.cursor()
    flag = str(input("(1) para buscar en toda la tabla\n(2) para buscar por ID\nIngrese la opción: "))
    if flag == str(1):
            instruccion = f"SELECT * FROM categorias"
            for row in cursor.execute(instruccion):
                print(row)
            input()
            borrarPantalla()             
    elif flag == str(2):
            campoId = input("Ingrese el ID que desea buscar: ")
            instruccion = f"SELECT categoria_nombre, categoria_info FROM categorias WHERE categoria_id='{campoId}'"
            cursor.execute(instruccion)
            datos = cursor.fetchall()
            print(datos)
            input()
            borrarPantalla()  
    conexion.commit()
    conexion.close()

def buscarCliente():
    conexion = sql.connect("sistema.sqlite")
    cursor = conexion.cursor()
    flag = str(input("(1) para buscar en toda la tabla\n(2) para buscar por ID\nIngrese la opción: "))
    if flag == str(1):
            instruccion = f"SELECT * FROM clientes"
            for row in cursor.execute(instruccion):
                print(row) 
            input()
            borrarPantalla()             
    elif flag == str(2):
            campoId = input("Ingrese el ID de cliente que desea buscar: ")
            instruccion = f"SELECT cliente_nombre, cliente_zona, cliente_direccion, cliente_telefono, cliente_email FROM clientes WHERE cliente_id='{campoId}'"
            cursor.execute(instruccion)
            datos = cursor.fetchall()
            print(datos)
            input()
            borrarPantalla()  
    conexion.commit()
    conexion.close()
    
def buscarProducto():
    conexion = sql.connect("sistema.sqlite")
    cursor = conexion.cursor()
    flag = str(input("(1) para buscar en toda la tabla\n(2) para buscar por ID\nIngrese la opción: "))
    if flag == str(1):
            instruccion = f"SELECT * FROM productos"
            for row in cursor.execute(instruccion):
                print(row)
            input()
            borrarPantalla()          
    elif flag == str(2):
            campoId = input("Ingrese el ID de producto que desea buscar: ")
            instruccion = f"SELECT producto_nombre, producto_precio, categoria_nombre, proveedor_nombre FROM Productos JOIN Proveedores ON Proveedores.proveedor_id=Productos.proveedor_id JOIN Categorias ON Categorias.categoria_id=Productos.producto_categoria WHERE producto_id='{campoId}'"
            cursor.execute(instruccion)
            datos = cursor.fetchall()
            print(datos)
            input()
            borrarPantalla()  
    conexion.commit()
    conexion.close()