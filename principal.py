import sqlite3 as sql
from funciones import *

def menuDevuelveCodigo(): 
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
        print("SELECCIONE TIPO DE MODIFICACION")
        submenuTablas()
### BAJA ####
    elif seleccion==str(3):
        print("SELECCIONE TIPO DE BAJA")
        submenuTablas()
### BUSQUEDA ###
    elif seleccion==str(4):
       enConstruccion()
### SALIR ###
    elif seleccion==str(5):
        sys.exit()


""" else:
        if seleccion != 1 or seleccion != 2 or seleccion != 3 or seleccion != 4 or seleccion != 5:
            while True:
                seleccion=input("Opcion invalida. Ingrese nuevamente:")
                print(menu)
                if seleccion==str(1):
                    enConstruccion()
                elif seleccion==str(2):
                    enConstruccion()
                elif seleccion==str(3):
                    enConstruccion()
                elif seleccion==str(4):
                    enConstruccion()"""
                    
menuDevuelveCodigo()