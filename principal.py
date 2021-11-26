import sqlite3 as sql
from funciones import *

def menuDevuelveCodigo():  
    menu()
    seleccion=input("Ingrese una opcion:")

    if seleccion==str(1):
        menuAltas()
        seleccionSubmenu = input("Seleccione el tipo de alta: ")
        if seleccionSubmenu ==str(1):
            print("Seleccion 1 - Categoria")
        elif seleccionSubmenu ==str(2):
            print("Seleccion 2 - Clientes")
        elif seleccionSubmenu ==str(3):
            print("Seleccion 3 - Facturas")
        elif seleccionSubmenu ==str(4):
            print("Seleccion 4 - Logistica")
        elif seleccionSubmenu ==str(5):
            print("Seleccion 5 - Productos")
        elif seleccionSubmenu ==str(6):
            print("Seleccion 6 - Proveedores")
        elif seleccionSubmenu ==str(7):
            print("Seleccion 7 - Venta_items")

        #Funcion 1
    elif seleccion==str(2):
        editar = print("Edit")
        return editar
    elif seleccion==str(3):
        borrar = print("Delete")
        return borrar
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