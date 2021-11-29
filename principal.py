import sqlite3 as sql
from funciones import *
import sys

#SUBMENÚ
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
    seleccionSubmenu = int(input("Seleccione una tabla: "))
    borrarPantalla()
    if seleccionSubmenu == 1:
        print("Seleccion 1 - Categoria\n")
        seleccionSub = "uno"
        return seleccionSub
    elif seleccionSubmenu == 2:
        print("Seleccion 2 - Clientes\n")
        seleccionSub = "dos"
        return seleccionSub
    elif seleccionSubmenu == 3:
        print("Seleccion 3 - Facturas\n")
        seleccionSubmenu = "tres"
        return seleccionSubmenu
    elif seleccionSubmenu == 4:
        print("Seleccion 4 - Logistica\n")
        seleccionSubmenu = "cuatro"
        return seleccionSubmenu
    elif seleccionSubmenu == 5:
        print("Seleccion 5 - Productos\n")
        seleccionSubmenu = "cinco"
        return seleccionSubmenu
    elif seleccionSubmenu == 6:
        print("Seleccion 6 - Proveedores\n")
        seleccionSubmenu = "seis"
        return seleccionSubmenu
    elif seleccionSubmenu == 7:
        print("Seleccion 7 - Venta_items\n")
        seleccionSubmenu = "siete"
        return seleccionSubmenu
   
### MENU DE ALTAS ###
def menuAltas():
    borrarPantalla()
    print("SELECCIONE TIPO DE ALTA")
    seleccionSub = submenuTablas()
    if seleccionSub == "uno":
        insertarEntidadCategoria()
    elif seleccionSub == "dos":
        insertarEntidadCliente()
    elif seleccionSub == "tres":
        enConstruccion()
    elif seleccionSub == "cuatro":
        enConstruccion()
    elif seleccionSub == "cinco":
        insertarProducto()
    elif seleccionSub == "seis":
        insertarProveedor()
    elif seleccionSub == "siete":
        enConstruccion()
    elif seleccionSub == "ocho":
        menuPrincipal()

### MENU MODIFICACIONES ###

def menuModificaciones():
    borrarPantalla()
    print("SELECCIONE TIPO DE MODIFICACIÓN")
    seleccionSub = submenuTablas()
    if seleccionSub == "uno": #Categorias
        modificarCategoria()
    elif seleccionSub == "dos": #Clientes
        modificarCliente()
    elif seleccionSub == "tres": #Facturas
        print("La factura no puede ser modificada. Debe realizar Nota de Crédito.\n")
    elif seleccionSub == "cuatro": #Logistica
        enConstruccion()
    elif seleccionSub == "cinco": #Productos
        enConstruccion()
    elif seleccionSub == "seis": #Proveedores
        enConstruccion()
    elif seleccionSub == "siete": #Venta_items
        print("Los items no pueden ser modificados. La orden ya fue facturada.\n")
    elif seleccionSub == "ocho": #Regresar menu Principal
        menuPrincipal()

def menuBaja():
    print("SELECCIONE TIPO DE BAJA")
    seleccionSub = submenuTablas()
    if seleccionSub == "uno": #Categorias
        borrarCategoria()
    elif seleccionSub == "dos": #Clientes
        borrarCliente()
    elif seleccionSub == "tres": #Facturas
        print("Factura emitida. No puede ser anulada.\n")
    elif seleccionSub == "cuatro": #Logistica
        enConstruccion()
    elif seleccionSub == "cinco": #Productos
        borrarProducto()
    elif seleccionSub == "seis": #Proveedores
        borrarProveedor()
    elif seleccionSub == "siete": #Venta_items
        print("Orden con factura emitida. No puede ser anulada.\n")
    elif seleccionSub == "ocho": #Regresar menu Principal
        menuPrincipal()

def menuBusqueda():
    print("SELECCIONE EN CUÁL TABLA DESEA BUSCAR:")
    seleccionSub = submenuTablas()
    if seleccionSub == "uno": #Categorias
        buscarCategoria()
    elif seleccionSub == "dos": #Clientes
        buscarCliente()
    elif seleccionSub == "tres": #Facturas
        enConstruccion()
    elif seleccionSub == "cuatro": #Logistica
        enConstruccion()
    elif seleccionSub == "cinco": #Productos
        buscarProducto()
    elif seleccionSub == "seis": #Proveedores
        enConstruccion()
    elif seleccionSub == "siete": #Venta_items
        enConstruccion()
    elif seleccionSub == "ocho": #Regresar menu Principal
     menuPrincipal()


###MENÚ PRINCIPAL
def menuPrincipal(): 
    menu = """///  Menú principal - Seleccione una acción  ///
            \n[1] - Alta
            \n[2] - ModificaciÓn
            \n[3] - Baja
            \n[4] - Busqueda
            \n[5] - Salir\n"""
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
   
