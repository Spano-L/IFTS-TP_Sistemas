import sqlite3 as sql
from funciones import *

def menuDevuelveCodigo():  

    print("///  Menú - Seleccione una opcion  ///")
    print("1.-Alta")
    print("2.-Modificacion")
    print("3.-Baja")
    print("4.-Busqueda")
    print("5.-Salir")
    seleccion=input("Ingrese una opcion:")

    if seleccion==str(1):
        nombre = input("Ingrese su nombre:")
        follower = int(input("Ingrese followers:"))
        subs = int(input("Ingreseasdsadas: "))
        insertRow(nombre,follower,subs)
        readRows()
        #Funcion 1
    elif seleccion==str(2):
        editar = print("Edit")
        return editar
    elif seleccion==str(3):
        borrar = print("Delete")
        return borrar
    elif seleccion==str(4):
        salir = print("Exit")
        return salir
    else:
        if seleccion != 1 or seleccion != 2 or seleccion != 3 or seleccion != 4:
            while True:
                print("///  Menú - Seleccione una opcion  ///")
                print("1.-Nuevo")
                print("2.-Editar")
                print("3.-Borrar")
                print("4.-Salir")
                seleccion=str(input("Opcion invalida. Ingrese nuevamente:"))
                if seleccion==str(1):
                    nuevo = print("New")
                    return nuevo
                elif seleccion==str(2):
                    editar = print("Edit")
                    return editar
                elif seleccion==str(3):
                    borrar = print("Delete")
                    return borrar
                elif seleccion==str(4):
                    salir = print("Exit")
                    return salir
                    
menuDevuelveCodigo()