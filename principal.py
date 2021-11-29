import sqlite3 as sql
from funciones import *
import sys

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
        print("Seleccion 1 - Categoria\n")
        return seleccionSubmenu
    elif seleccionSubmenu == 2:
        print("Seleccion 2 - Clientes\n")
        return seleccionSubmenu
    elif seleccionSubmenu == 3:
        print("Seleccion 3 - Facturas\n")
        return seleccionSubmenu
    elif seleccionSubmenu == 4:
        print("Seleccion 4 - Logistica\n")
        return seleccionSubmenu
    elif seleccionSubmenu == 5:
        print("Seleccion 5 - Productos\n")
        return seleccionSubmenu
    elif seleccionSubmenu == 6:
        print("Seleccion 6 - Proveedores\n")
        return seleccionSubmenu
    elif seleccionSubmenu == 7:
        print("Seleccion 7 - Venta_items\n")
        return seleccionSubmenu
   
### MENU DE ALTAS ###
def menuAltas():
    borrarPantalla()
    print("SELECCIONE TIPO DE ALTA")
    seleccionSubmenu = submenuTablas()
    if seleccionSubmenu == 1:
        insertarEntidadCategoria()
    elif seleccionSubmenu == 2:
        insertarEntidadCliente()
    elif seleccionSubmenu == 3:
        enConstruccion()
    elif seleccionSubmenu == 4:
        enConstruccion()
    elif seleccionSubmenu == 5:
        insertarProducto()
    elif seleccionSubmenu == 6:
        insertarProveedor()
    elif seleccionSubmenu == 7:
        enConstruccion()
    elif seleccionSubmenu == 8:
        menuPrincipal()

### MENU MODIFICACIONES ###

def menuModificaciones():
    borrarPantalla()
    print("SELECCIONE TIPO DE MODIFICACIÓN")
    seleccionSubmenu = submenuTablas()
    if seleccionSubmenu == 1: #Categorias
        modificarCategoria()
    elif seleccionSubmenu == 2: #Clientes
        modificarCliente()
    elif seleccionSubmenu == 3: #Facturas
        print("La factura no puede ser modificada. Debe realizar Nota de Crédito.\n")
    elif seleccionSubmenu == 4: #Logistica
        enConstruccion()
    elif seleccionSubmenu == 5: #Productos
        modificarProducto()
    elif seleccionSubmenu == 6: #Proveedores
        modificarProveedor()
    elif seleccionSubmenu == 7: #Venta_items
        print("Los items no pueden ser modificados. La orden ya fue facturada.\n")
    elif seleccionSubmenu == 8: #Regresar menu Principal
        menuPrincipal()

def menuBaja():
    print("SELECCIONE TIPO DE BAJA")
    seleccionSubmenu = submenuTablas()
    if seleccionSubmenu == 1: #Categorias
        borrarCategoria()
    elif seleccionSubmenu == 2: #Clientes
        borrarCliente()
    elif seleccionSubmenu == 3: #Facturas
        print("Factura emitida. No puede ser anulada.\n")
    elif seleccionSubmenu == 4: #Logistica
        enConstruccion()
    elif seleccionSubmenu == 5: #Productos
        borrarProducto()
    elif seleccionSubmenu == 6: #Proveedores
        borrarProveedor()
    elif seleccionSubmenu == 7: #Venta_items
        print("Orden con factura emitida. No puede ser anulada.\n")
    elif seleccionSubmenu == 8: #Regresar menu Principal
        menuPrincipal()

def menuBusqueda():
    print("SELECCIONE EN CUÁL TABLA DESEA BUSCAR:")
    seleccionSubmenu = submenuTablas()
    if seleccionSubmenu == 1: #Categorias
        buscarCategoria()
    elif seleccionSubmenu == 2: #Clientes
        buscarCliente()
    elif seleccionSubmenu == 3: #Facturas
        enConstruccion()
    elif seleccionSubmenu == 4: #Logistica
        enConstruccion()
    elif seleccionSubmenu == 5: #Productos
        buscarProducto()
    elif seleccionSubmenu == 6: #Proveedores
        enConstruccion()
    elif seleccionSubmenu == 7: #Venta_items
        enConstruccion()
    elif seleccionSubmenu == 8: #Regresar menu Principal
     menuPrincipal()


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

while True:
    menuPrincipal()
    if menuPrincipal()==False:
        break
   
