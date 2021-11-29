import sqlite3 as sql
import os
import sys

def borrarPantalla():
    os.system("cls")

def conexionSQL(instruccion):
    conexion = sql.connect("sistema.sqlite")
    cursor = conexion.cursor()
    cursor.execute(instruccion)
    conexion.commit()
    conexion.close()

###MENÚ PRINCIPAL
def menuPrincipal(): 
    menu = """
    ///  Menú principal - Seleccione una acción  ///
            [1] - Alta
            [2] - Modificación
            [3] - Baja
            [4] - Busqueda
            [5] - Salir\n"""
    print(menu)
    seleccion = int(input("Ingrese una opción: "))
    borrarPantalla()

#### ALTAS ####
    if seleccion==1:
       menuAltas()

#### MODIFICACION ####
    elif seleccion==2:
        menuModificaciones()

### BAJA ####
    elif seleccion==3:
        menuBaja()

### BUSQUEDA ###
    elif seleccion==4:
        menuBusqueda()

### SALIR ###
    elif seleccion==5:
        return False
        sys.exit()

#SUBMENÚ
def submenuTablas():
    submenu = """
        [1] - Categoria
        [2] - Clientes
        [3] - Facturas
        [4] - Logistica
        [5] - Productos
        [6] - Proveedores
        [7] - Venta_items
        [8] - Atras
        """
    print(submenu)
    seleccionSubmenu = int(input("Seleccione una tabla: "))
    borrarPantalla()
    if seleccionSubmenu == 1:
        print("Selección 1 - Categoria\n")
        return seleccionSubmenu
    elif seleccionSubmenu == 2:
        print("Selección 2 - Clientes\n")
        return seleccionSubmenu
    elif seleccionSubmenu == 3:
        print("Selección 3 - Facturas\n")
        return seleccionSubmenu
    elif seleccionSubmenu == 4:
        print("Selección 4 - Logistica\n")
        return seleccionSubmenu
    elif seleccionSubmenu == 5:
        print("Selección 5 - Productos\n")
        return seleccionSubmenu
    elif seleccionSubmenu == 6:
        print("Selección 6 - Proveedores\n")
        return seleccionSubmenu
    elif seleccionSubmenu == 7:
        print("Selección 7 - Venta_items\n")
        return seleccionSubmenu
   
### MENU DE ALTAS ###
def menuAltas():
    borrarPantalla()
    print("SELECCIONE TIPO DE ALTA")
    seleccionSubmenu = submenuTablas()
    if seleccionSubmenu == 1:
        altaCategoria()
    elif seleccionSubmenu == 2:
        altaCliente()
    elif seleccionSubmenu == 3:
        altaFactura()
    elif seleccionSubmenu == 4:
        altaLogistica()
    elif seleccionSubmenu == 5:
        altaProducto()
    elif seleccionSubmenu == 6:
        altaProveedor()
    elif seleccionSubmenu == 7:
        enConstruccion() #Venta_items
    elif seleccionSubmenu == 8:
        menuPrincipal()

### MENÚ MODIFICACIONES ###

def menuModificaciones():
    borrarPantalla()
    print("SELECCIONE TIPO DE MODIFICACIÓN")
    seleccionSubmenu = submenuTablas()
    if seleccionSubmenu == 1:
        modificarCategoria()
    elif seleccionSubmenu == 2:
        modificarCliente()
    elif seleccionSubmenu == 3:
        print("La factura no puede ser modificada. Debe realizar Nota de Crédito.\n")
    elif seleccionSubmenu == 4:
        modificarLogistica()
    elif seleccionSubmenu == 5:
        modificarProducto()
    elif seleccionSubmenu == 6:
        modificarProveedor()
    elif seleccionSubmenu == 7:
        print("Los items no pueden ser modificados. La orden ya fue facturada.\n")
    elif seleccionSubmenu == 8: 
        menuPrincipal()

def menuBaja():
    print("SELECCIONE TIPO DE BAJA")
    seleccionSubmenu = submenuTablas()
    if seleccionSubmenu == 1: 
        borrarCategoria()
    elif seleccionSubmenu == 2: 
        borrarCliente()
    elif seleccionSubmenu == 3: 
        print("Factura emitida. No puede ser anulada.\n")
    elif seleccionSubmenu == 4:
        borrarLogistica()
    elif seleccionSubmenu == 5: 
        borrarProducto()
    elif seleccionSubmenu == 6: 
        borrarProveedor()
    elif seleccionSubmenu == 7: 
        print("Orden con factura emitida. No puede ser anulada.\n")
    elif seleccionSubmenu == 8: 
        menuPrincipal()

def menuBusqueda():
    print("SELECCIONE EN CUÁL TABLA DESEA BUSCAR:")
    seleccionSubmenu = submenuTablas()
    if seleccionSubmenu == 1: 
        buscarCategoria()
    elif seleccionSubmenu == 2:
        buscarCliente()
    elif seleccionSubmenu == 3: 
        buscarFactura()
    elif seleccionSubmenu == 4:
        buscarLogistica()
    elif seleccionSubmenu == 5:
        buscarProducto()
    elif seleccionSubmenu == 6:
        buscarProveedor()
    elif seleccionSubmenu == 7: 
        buscarItemsFactura()
    elif seleccionSubmenu == 8: 
        menuPrincipal()
  
# Funciones con mensajes de información.

def confirmarAlta():
    print("Los datos fueron cargados exitosamente.\n")
    input("Presione cualquier tecla para continuar")
    borrarPantalla() 

def confirmarModificacion():
    print("El campo fue modificado exitosamente.\n")
    input("Presione cualquier tecla para continuar")
    borrarPantalla() 

def confirmarBaja():
    print("La entidad fue borrada exitosamente.\n")
    input("Presione cualquier tecla para continuar")
    borrarPantalla() 

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

def altaFactura():
    fecha = input("Ingrese fecha de factura: ")
    id_cliente = input("Ingrese id del cliente: ")
    instruccion = f"INSERT INTO facturas (factura_fecha, cliente_id) VALUES ('{fecha}','{id_cliente}')"
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

def altaItemsFactura():
    factura = input("Ingrese número de factura: ")
    producto = input("Ingrese id del producto")
    cantidad = input("Ingrese cantidad del producto: ")
    precio = 0 #implementar SUM (cantidad*item_precio) As Precio
    instruccion = f"INSERT INTO venta_items (factura_numero, cantidad, productos_id, item_precio) VALUES ('{factura}','{cantidad}','{producto}', '{precio}')"
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

def borrarLogistica():
    valor = input("Ingrese nombre de zona que desea borrar: ")
    instruccion = f"DELETE FROM logistica WHERE zona_nombre='{valor}'"
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

def buscarFactura():
    conexion = sql.connect("sistema.sqlite")
    cursor = conexion.cursor()
    opcion = int(input("(1) para buscar en toda la tabla\n(2) para buscar por ID\nIngrese la opción: "))
    if opcion == 1:
            instruccion = f"SELECT factura_numero, factura_fecha, cliente_nombre FROM facturas JOIN clientes ON clientes.cliente_id=facturas.cliente_id"
            for row in cursor.execute(instruccion):
                print(row) 
            input("Presione cualquier tecla para continuar")
            borrarPantalla()             
    elif opcion == 2:
            campo = input("Ingrese el número de factura que desea buscar: ")
            instruccion = f"SELECT factura_numero, factura_fecha, cliente_nombre FROM facturas JOIN clientes ON clientes.cliente_id=facturas.cliente_id WHERE factura_numero='{campo}'"
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

def buscarItemsFactura():
    conexion = sql.connect("sistema.sqlite")
    cursor = conexion.cursor()
    opcion = int(input("(1) para buscar en toda la tabla\n(2) para buscar por número de factura\nIngrese la opción: "))
    if opcion == 1:
            instruccion = f"SELECT venta_item, factura_numero, cantidad, producto_nombre, item_precio FROM venta_items JOIN productos USING (producto_id)"
            for row in cursor.execute(instruccion):
                print(row) 
            input("Presione cualquier tecla para continuar")
            borrarPantalla()             
    elif opcion == 2:
            campo = input("Ingrese el número de factura que desea buscar: ")
            instruccion = f"SELECT factura_numero, factura_fecha, cliente_nombre FROM facturas JOIN clientes ON clientes.cliente_id=facturas.cliente_id WHERE factura_numero='{campo}'"
            cursor.execute(instruccion)
            datos = cursor.fetchall()
            print(datos)
            input("Presione cualquier tecla para continuar")
            borrarPantalla()  
    conexion.commit()
    conexion.close()

print ("\nEjecute el archivo principal.py\n")