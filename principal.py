import sqlite3 as sql
from funciones import *
import sys

def menuPrincipal(): 
    menu()
    seleccion=str(input("Ingrese una opcion: "))
    borrarPantalla()
#### ALTAS ####
    if seleccion==str(1):
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
#### MODIFICACION ####
    elif seleccion==str(2):
        borrarPantalla()
        print("SELECCIONE TIPO DE MODIFICACION")
        seleccionSub = submenuTablas()
        if seleccionSub == "uno": #Categorias
            modificarCategoria()
        elif seleccionSub == "dos": #Clientes
            modificarCliente()
        elif seleccionSub == "tres": #Facturas
            print("La factura no puede ser modificada. Realizar nota de credito.\n")
        elif seleccionSub == "cuatro": #Logistica
            enConstruccion()
        elif seleccionSub == "cinco": #Productos
            enConstruccion()
        elif seleccionSub == "seis": #Proveedores
            enConstruccion()
        elif seleccionSub == "siete": #Venta_items
            print("Los items no pueden ser modificados. Orden ya facturada.\n")
### BAJA ####
    elif seleccion==str(3):
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
### BUSQUEDA ###
    elif seleccion==str(4):
        print("SELECCIONE DONDE DESEA BUSCAR")
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
### SALIR ###
    elif seleccion==str(5):
        return False
        sys.exit()

while True:
    menuPrincipal()
    if menuPrincipal()==False:
        break
    