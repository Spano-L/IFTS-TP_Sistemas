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
        enConstruccion() #Facturas
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
    elif seleccionSubmenu == 4: #Logistica
        enConstruccion()
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
    elif seleccionSubmenu == 4: #Logistica
        enConstruccion()
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
    elif seleccionSubmenu == 3: #Facturas
        enConstruccion()
    elif seleccionSubmenu == 4: #Logistica
        enConstruccion()
    elif seleccionSubmenu == 5:
        buscarProducto()
    elif seleccionSubmenu == 6: #Proveedores
        enConstruccion()
    elif seleccionSubmenu == 7: #Venta_items
        enConstruccion()
    elif seleccionSubmenu == 8: 
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
   
