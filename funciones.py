import sqlite3 as sql
import os

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

# Funciones con mensajes de informacion.

def confirmarAlta():
    print("Los datos fueron cargados exitosamente.\n")

def confirmarModificacion():
    print("El campo fue modificado exitosamente.\n")

def confirmarBaja():
    print("La entidad fue borrada exitosamente.\n")

def enConstruccion():
    print("Esta seccion del programa se encuentra en construccion.\n")

# Funciones de alta.

def insertarEntidadCategoria():
    conexion = sql.connect("sistema.sqlite")
    cursor = conexion.cursor()
    categoria_nombre = input("Ingrese nombre de categoria: ")
    categoria_info = input("Ingrese informacion de la categoria: ")
    instruccion = f"INSERT INTO categorias (categoria_nombre, categoria_info) VALUES ('{categoria_nombre}','{categoria_info}')"
    cursor.execute(instruccion)
    conexion.commit()
    conexion.close()
    confirmarAlta()

def insertarEntidadCliente():
    conexion = sql.connect("sistema.sqlite")
    cursor = conexion.cursor()
    cliente_nombre = input("Ingrese nombre de cliente: ")
    cliente_zona = input("Ingrese zona de cliente: ")
    cliente_direccion = input("Ingrese dirección de cliente: ")
    cliente_telefono = input("Ingrese teléfono de cliente: ")
    cliente_email = input("Ingrese email de cliente:")
    cliente_mayorista = int(input("Ingrese 1 si el cliente es mayorista. Ó ingrese 0 si es minorista."))
    instruccion = f"INSERT INTO clientes (cliente_nombre, cliente_zona, cliente_direccion, cliente_telefono, cliente_email, cliente_mayorista) VALUES ('{cliente_nombre}','{cliente_zona}','{cliente_direccion}','{cliente_telefono}','{cliente_email}','{cliente_mayorista}')"
    cursor.execute(instruccion)
    conexion.commit()
    conexion.close()
    confirmarAlta()

def insertarProducto():
    conexion = sql.connect("sistema.sqlite")
    cursor = conexion.cursor()
    producto_nombre = input("Ingrese nombre del producto: ")
    producto_categoria = int(input("Ingrese categoria del producto: "))
    producto_precio = float(input("Ingrese el precio del producto: "))
    producto_proveedor_id = int(input("Ingrese el ID del proveedor: "))
    instruccion = f"INSERT INTO productos (producto_nombre,producto_categoria,producto_precio,proveedor_id) VALUES ('{producto_nombre}','{producto_categoria}','{producto_precio}','{producto_proveedor_id}')"
    cursor.execute(instruccion)
    conexion.commit()
    conexion.close()
    confirmarAlta()

def insertarProveedor():
    conexion = sql.connect("sistema.sqlite")
    cursor = conexion.cursor()
    proveedor_nombre = input("Ingrese nombre del proveedor: ")
    proveedor_direccion = input("Ingrese direccion del proveedor: ")
    proveedor_ciudad = input("Ingrese ciudad del proveedor: ")
    proveedor_email = input("Ingrese el mail del proveedor: ")
    proveedor_telefono = input("Ingrese teléfono del proveedor: ")
    instruccion = f"INSERT INTO proveedores (proveedor_nombre, proveedor_direccion, proveedor_ciudad, proveedor_email, proveedor_telefono) VALUES ('{proveedor_nombre}','{proveedor_direccion}','{proveedor_ciudad}','{proveedor_email}','{proveedor_telefono}')"
    cursor.execute(instruccion)
    conexion.commit()
    conexion.close()
    confirmarAlta()

# Funciones de modificacion

def modificarCategoria():
    conexion = sql.connect("sistema.sqlite")
    cursor = conexion.cursor()
    campoId = int(input("Ingrese ID de la categoria que desea modificar: "))
    flag = str(input("(1) para cambiar el nombre de la categoria\n(2) para cambiar la informacion de la categoria\nIngrese su opcion: "))
    if flag == str(1):
        valor = input("Ingrese nuevo nombre: ")
        campo = "categoria_nombre"
    elif flag == str(2):
        valor = input("Ingrese nueva informacion: ")
        campo = "categoria_info" 
    instruccion = f"UPDATE categorias SET '{campo}'='{valor}' WHERE categoria_id='{campoId}'"
    cursor.execute(instruccion)
    conexion.commit()
    conexion.close()
    confirmarModificacion()

def modificarCliente():
    conexion = sql.connect("sistema.sqlite")
    cursor = conexion.cursor()
    campoId = int(input("Ingrese ID del cliente que desea modificar: "))
    flag = str(input("(1) para cambiar nombre de cliente\n(2) para cambiar zona de cliente\n(3) para cambiar direccion de cliente\n(4) para cambiar telefono de cliente\n(5) para cambiar email de cliente\nIngrese su opcion: "))
    if flag == str(1):
        valor = input("Ingrese nuevo nombre de cliente: ")
        campo = "cliente_nombre"
    elif flag == str(2):
        valor = input("Ingrese nueva zona de cliente: ")
        campo = "cliente_zona"
    elif flag == str(3):
        valor = input("Ingrese nueva direccion: ")
        campo = "cliente_direccion"
    elif flag == str(4):
        valor = input("Ingrese nuevo telefono: ")
        campo = "cliente_telefono"
    elif flag == str(5):
        valor = input("Ingrese nuevo email : ")
        campo = "cliente_email"
    instruccion = f"UPDATE clientes SET '{campo}'='{valor}' WHERE cliente_id='{campoId}'"
    cursor.execute(instruccion)
    conexion.commit()
    conexion.close()
    confirmarModificacion()

# Funciones de baja

def borrarCategoria():
    conexion = sql.connect("sistema.sqlite")
    cursor = conexion.cursor()
    valor = int(input("Ingrese ID de categoria que desea borrar: "))
    instruccion = f"DELETE FROM categorias WHERE categoria_id={valor}"
    cursor.execute (instruccion)
    conexion.commit()
    conexion.close()
    confirmarBaja()

def borrarCliente():
    conexion = sql.connect("sistema.sqlite")
    cursor = conexion.cursor()
    valor = int(input("Ingrese ID de cliente que desea borrar: "))
    instruccion = f"DELETE FROM clientes WHERE cliente_id={valor}"
    cursor.execute (instruccion)
    conexion.commit()
    conexion.close()
    confirmarBaja()

def borrarProducto():
    conexion = sql.connect("sistema.sqlite")
    cursor = conexion.cursor()
    valor = int(input("Ingrese ID de producto que desea borrar: "))
    instruccion = f"DELETE FROM productos WHERE producto_id={valor}"
    cursor.execute (instruccion)
    conexion.commit()
    conexion.close()
    confirmarBaja()

def borrarProveedor():
    conexion = sql.connect("sistema.sqlite")
    cursor = conexion.cursor()
    valor = int(input("Ingrese ID de proveedor que desea borrar: "))
    instruccion = f"DELETE FROM proveedores WHERE proveedor_id={valor}"
    cursor.execute(instruccion)
    conexion.commit()
    conexion.close()
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
    elif flag == str(2):
            campoId = input("Ingrese el ID que desea buscar: ")
            instruccion = f"SELECT categoria_nombre, categoria_info FROM categorias WHERE categoria_id='{campoId}'"
            cursor.execute(instruccion)
            datos = cursor.fetchall()
            print(datos)
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
    elif flag == str(2):
            campoId = input("Ingrese el ID de producto que desea buscar: ")
            instruccion = f"SELECT producto_nombre, producto_precio, categoria_nombre, proveedor_nombre FROM Productos JOIN Proveedores ON Proveedores.proveedor_id=Productos.proveedor_id JOIN Categorias ON Categorias.categoria_id=Productos.producto_categoria WHERE producto_id='{campoId}'"
            cursor.execute(instruccion)
            datos = cursor.fetchall()
            print(datos)
    conexion.commit()
    conexion.close()