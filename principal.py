import sqlite3 as sql
from funciones import *

menu = {
"///  Menú - Seleccione una opcion:  ///"
            "1.-Alta"
            "2.-Modificacion"
            "3.-Baja"
            "4.-Busqueda"
            "5.-Salir"
}

def menuDevuelveCodigo():  
  
    print(menu)
    seleccion=input("Ingrese una opcion:")

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
        salir = print("Exit")
        return salir
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
                    salir = print("Exit")
                return salir
                    
menuDevuelveCodigo()