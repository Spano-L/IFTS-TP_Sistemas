import sqlite3 as sql
from funciones import *
import sys
   
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

def menuPrincipal(): 
    menu()
    seleccion = str(input("Ingrese una opción: "))
    borrarPantalla()

#### ALTAS ####
    if seleccion==str(1):
       menuAltas()

#### MODIFICACION ####
    elif seleccion==str(2):
        menuModificaciones()

### BAJA ####
    elif seleccion==str(3):
        menuBaja()

### BUSQUEDA ###
    elif seleccion==str(4):
        menuBusqueda()

### SALIR ###
    elif seleccion==str(5):
        return False
        sys.exit()

while True:
    menuPrincipal()
    if menuPrincipal()==False:
        break

