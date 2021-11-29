import sqlite3 as sql
import os

def borrarPantalla():
    os.system("cls")

def conexionSQL(instruccion):
    conexion = sql.connect("sistema.sqlite")
    cursor = conexion.cursor()
    cursor.execute(instruccion)
    conexion.commit()
    conexion.close()
  
# Funciones con mensajes de información.

def confirmarAlta():
    print("Los datos fueron cargados exitosamente.\n")

def confirmarModificacion():
    print("El campo fue modificado exitosamente.\n")

def confirmarBaja():
    print("La entidad fue borrada exitosamente.\n")

def enConstruccion():
    print("Esta sección del programa se encuentra en construcción.\n")
    input("Presione cualquier tecla para continuar")
    borrarPantalla() 

# Funciones de alta.

def altaCategoria():
    categoria_nombre = input("Ingrese nombre de categoria: ")
    categoria_info = input("Ingrese información de la categoria: ")
    instruccion = f"INSERT INTO categorias (categoria_nombre, categoria_info) VALUES ('{categoria_nombre}','{categoria_info}')"
    conexionSQL(instruccion)
    confirmarAlta()

def altaCliente():
    cliente_nombre = input("Ingrese nombre de cliente: ")
    cliente_zona = input("Ingrese zona de cliente: ")
    cliente_direccion = input("Ingrese dirección de cliente: ")
    cliente_telefono = input("Ingrese teléfono de cliente: ")
    cliente_email = input("Ingrese email de cliente:")
    cliente_mayorista = int(input("Ingrese 1 si el cliente es mayorista. ó ingrese 0 si es minorista."))
    instruccion = f"INSERT INTO clientes (cliente_nombre, cliente_zona, cliente_direccion, cliente_telefono, cliente_email, cliente_mayorista) VALUES ('{cliente_nombre}','{cliente_zona}','{cliente_direccion}','{cliente_telefono}','{cliente_email}','{cliente_mayorista}')"
    conexionSQL(instruccion)
    confirmarAlta()

def altaLogistica():
    nombre = input("Ingrese nombre de la zona: ")
    horario = input("Ingrese horario de la zona: ")
    repartidor = input("Ingrese repartidor de la zona: ")
    instruccion = f"INSERT INTO logistica (zona_nombre, zona_horario, zona_repartidor) VALUES ('{nombre}','{horario}','{repartidor}')"
    conexionSQL(instruccion)
    confirmarAlta()

def altaProducto():
    producto_nombre = input("Ingrese nombre del producto: ")
    producto_categoria = int(input("Ingrese categoría del producto: "))
    producto_precio = float(input("Ingrese el precio del producto: "))
    producto_proveedor_id = int(input("Ingrese el ID del proveedor: "))
    instruccion = f"INSERT INTO productos (producto_nombre, producto_categoria, producto_precio, proveedor_id) VALUES ('{producto_nombre}','{producto_categoria}','{producto_precio}','{producto_proveedor_id}')"
    conexionSQL(instruccion)
    confirmarAlta()

def altaProveedor():
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
    opcion = int(input("(1) para cambiar el nombre de la categoría\n(2) para cambiar la información de la categoría\nIngrese su opcion: "))
    if opcion == 1:
        valor = input("Ingrese nuevo nombre: ")
        campo = "categoria_nombre"
    elif opcion == 2:
        valor = input("Ingrese nueva información: ")
        campo = "categoria_info" 
    instruccion = f"UPDATE categorias SET '{campo}'='{valor}' WHERE categoria_id='{campoId}'"
    conexionSQL(instruccion)
    confirmarModificacion()

def modificarCliente():
    campoId = int(input("Ingrese ID del cliente que desea modificar: "))
    opcion = int(input("(1) para cambiar nombre de cliente\n(2) para cambiar zona del cliente\n(3) para cambiar dirección del cliente\n(4) para cambiar teléfono del cliente\n(5) para cambiar email del cliente\nIngrese su opción: "))
    if opcion == 1:
        valor = input("Ingrese nuevo nombre del cliente: ")
        campo = "cliente_nombre"
    elif opcion == 2:
        valor = input("Ingrese nueva zona del cliente: ")
        campo = "cliente_zona"
    elif opcion == 3:
        valor = input("Ingrese nueva dirección: ")
        campo = "cliente_direccion"
    elif opcion == 4:
        valor = input("Ingrese nuevo teléfono: ")
        campo = "cliente_telefono"
    elif opcion == 5:
        valor = input("Ingrese nuevo email : ")
        campo = "cliente_email"
    instruccion = f"UPDATE clientes SET '{campo}'='{valor}' WHERE cliente_id='{campoId}'"
    conexionSQL(instruccion)
    confirmarModificacion()

def modificarLogistica():
    campoNombre = input("Ingrese el nombre de la zona que desea modificar: ")
    opcion = int(input("(1) Horario\n(2) Repartidor\nIngrese la opción del campo que desea modificar: "))
    if opcion == 1:
        valor = input("Ingrese nuevo horario: ")
        campo = "zona_horario"
    elif opcion == 2:
        valor = input("Ingrese nuevo repartidor: ")
        campo = "zona_repartidor" 
    instruccion = f"UPDATE Logistica SET '{campo}'='{valor}' WHERE zona_nombre='{campoNombre}'"
    conexionSQL(instruccion)
    confirmarModificacion()

def modificarProducto():
    campoId = int(input("Ingrese ID del producto que desea modificar: "))
    opcion = int(input("(1) para cambiar el nombre\n(2) para cambiar la categoría\n(3) para cambiar el precio\n(4) para cambiar el id del proveedor\nIngrese su opcion: "))
    if opcion == 1:
        valor = input("Ingrese nuevo nombre: ")
        campo = "producto_nombre"
    elif opcion == 2:
        valor = input("Ingrese nueva categoría: ")
        campo = "producto_categoria" 
    elif opcion == 3:
        valor = input("Ingrese nuevo precio: ")
        campo = "producto_precio"
    elif opcion == 4:
        valor = input("Ingrese id del nuevo proveedor: ")
        campo = "proveedor_id"  
    instruccion = f"UPDATE categorias SET '{campo}'='{valor}' WHERE categoria_id='{campoId}'"
    conexionSQL(instruccion)
    confirmarModificacion()

def modificarProveedor():
    campoId = int(input("Ingrese ID del proveedor que desea modificar: "))
    opcion = int(input("(1) Nombre\n(2) Dirección\n(3) Ciudad\n(4) Provincia\n(5) País\n(6) Email\n(4) Teléfono\nIngrese la opción del campo que desea modificar: "))
    if opcion == 1:
        valor = input("Ingrese nuevo nombre: ")
        campo = "proveedor_nombre"
    elif opcion == 2:
        valor = input("Ingrese nueva dirección: ")
        campo = "proveedor_direccion" 
    elif opcion == 3:
        valor = input("Ingrese nueva ciudad: ")
        campo = "proveedor_ciudad"
    elif opcion == 4:
        valor = input("Ingrese nuevo país: ")
        campo = "proveedor_pais"
    elif opcion == 5:
        valor = input("Ingrese nuevo email: ")
        campo = "proveedor_email"
    elif opcion == 6:
        valor = input("Ingrese nuevo teléfono: ")
        campo = "proveedor_telefono"
    instruccion = f"UPDATE categorias SET '{campo}'='{valor}' WHERE categoria_id='{campoId}'"
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
    opcion = int(input("(1) para buscar en toda la tabla\n(2) para buscar por ID\nIngrese la opción: "))
    if opcion == 1:
            instruccion = f"SELECT * FROM categorias"
            for row in cursor.execute(instruccion):
                print(row)
            input("Presione cualquier tecla para continuar")
            borrarPantalla()             
    elif opcion == 2:
            campoId = input("Ingrese el ID que desea buscar: ")
            instruccion = f"SELECT categoria_nombre, categoria_info FROM categorias WHERE categoria_id='{campoId}'"
            cursor.execute(instruccion)
            datos = cursor.fetchall()
            print(datos)
            input("Presione cualquier tecla para continuar")
            borrarPantalla()  
    conexion.commit()
    conexion.close()

def buscarCliente():
    conexion = sql.connect("sistema.sqlite")
    cursor = conexion.cursor()
    opcion = int(input("(1) para buscar en toda la tabla\n(2) para buscar por ID\nIngrese la opción: "))
    if opcion == 1:
            instruccion = f"SELECT * FROM clientes"
            for row in cursor.execute(instruccion):
                print(row) 
            input("Presione cualquier tecla para continuar")
            borrarPantalla()             
    elif opcion == 2:
            campoId = input("Ingrese el ID de cliente que desea buscar: ")
            instruccion = f"SELECT cliente_nombre, cliente_zona, cliente_direccion, cliente_telefono, cliente_email FROM clientes WHERE cliente_id='{campoId}'"
            cursor.execute(instruccion)
            datos = cursor.fetchall()
            print(datos)
            input("Presione cualquier tecla para continuar")
            borrarPantalla()  
    conexion.commit()
    conexion.close()

def buscarLogistica():
    conexion = sql.connect("sistema.sqlite")
    cursor = conexion.cursor()
    opcion = int(input("(1) para buscar en toda la tabla\n(2) para buscar por nombre\nIngrese la opción: "))
    if opcion == 1:
            instruccion = f"SELECT * FROM logistica"
            for row in cursor.execute(instruccion):
                print(row)
            input("Presione cualquier tecla para continuar")
            borrarPantalla()          
    elif opcion == 2:
            zona = input("Ingrese el nombre de la zona que desea buscar: ")
            instruccion = f"SELECT zona_nombre, zona_horario, zona_repartidor FROM Logistica WHERE zona_nombre='{zona}'"
            cursor.execute(instruccion)
            datos = cursor.fetchall()
            print(datos)
            input("Presione cualquier tecla para continuar")
            borrarPantalla()  
    conexion.commit()
    conexion.close()    
    
def buscarProducto():
    conexion = sql.connect("sistema.sqlite")
    cursor = conexion.cursor()
    opcion = int(input("(1) para buscar en toda la tabla\n(2) para buscar por ID\nIngrese la opción: "))
    if opcion == 1:
            instruccion = f"SELECT * FROM productos"
            for row in cursor.execute(instruccion):
                print(row)
            input("Presione cualquier tecla para continuar")
            borrarPantalla()          
    elif opcion == 2:
            campoId = input("Ingrese el ID de producto que desea buscar: ")
            instruccion = f"SELECT producto_nombre, producto_precio, categoria_nombre, proveedor_nombre FROM Productos JOIN Proveedores ON Proveedores.proveedor_id=Productos.proveedor_id JOIN Categorias ON Categorias.categoria_id=Productos.producto_categoria WHERE producto_id='{campoId}'"
            cursor.execute(instruccion)
            datos = cursor.fetchall()
            print(datos)
            input("Presione cualquier tecla para continuar")
            borrarPantalla()  
    conexion.commit()
    conexion.close()

def buscarProveedor():
    conexion = sql.connect("sistema.sqlite")
    cursor = conexion.cursor()
    opcion = int(input("(1) para buscar en toda la tabla\n(2) para buscar por ID\nIngrese la opción: "))
    if opcion == 1:
            instruccion = f"SELECT * FROM proveedores"
            for row in cursor.execute(instruccion):
                print(row)
            input("Presione cualquier tecla para continuar")
            borrarPantalla()          
    elif opcion == 2:
            campoId = input("Ingrese el ID de producto que desea buscar: ")
            instruccion = f"SELECT proveedor_nombre, proveedor_direccion, proveedor_ciudad, proveedor_provincia, proveedor_pais, proveedor_email, proveedor_telefono FROM Proveedores WHERE proveedor_id='{campoId}'"
            cursor.execute(instruccion)
            datos = cursor.fetchall()
            print(datos)
            input("Presione cualquier tecla para continuar")
            borrarPantalla()  
    conexion.commit()
    conexion.close()