import sqlite3 as sql
from funciones import *

def menuDevuelveCodigo():  
    menu()
    seleccion=input("Ingrese una opcion: ")
    borrarPantalla()

    if seleccion==str(1):
        print("SELECCIONE TIPO DE ALTA")
        if submenuTablas() == "uno":
            insertarEntidadCategoria()






    elif seleccion==str(2):
        print("SELECCIONE TIPO DE MODIFICACION")
        submenuTablas()
    elif seleccion==str(3):
        print("SELECCIONE TIPO DE BAJA")
        submenuTablas()
    elif seleccion==str(4):
        print("Seleccion 4.")
        leerFilas123()
        #print("/////////////////////////////////////")
        #leerFilas()
        input()
    else:
        if seleccion != 1 or seleccion != 2 or seleccion != 3 or seleccion != 4:
            while True:
                seleccion=input("Opcion invalida. Ingrese nuevamente:")
                print(menu)
                if seleccion==str(1):
                    campo1 = input("Ingrese campo 1:")
                    campo2 = int(input("Ingrese campo 2:"))
                    campo3 = int(input("Ingrese campo 3: "))
                    insertarFila(campo1, campo2, campo3)
                    leerFilas()()
                    #Funcion 1
                elif seleccion==str(2):
                    editar = print("Edit")
                    return editar
                elif seleccion==str(3):
                    borrar = print("Delete")
                    return borrar
                elif seleccion==str(4):
                    leerFilas123()
                    input()
                    
menuDevuelveCodigo()