# Creación del menú de opciones para tamagochi
import os
runProgram = True # Variable de control para el while de la función menu.

#Función para mostrar las opciones del menú
def showMenuOptions():
    print("¿Qué actividad desas que realize tu tamagochi?")
    print("")
    print("1) Jugar")
    print("2) Comer")
    print("3) Dormir")
    print("4) Ver estado")
    print("5) Salir\n")

# Función para interactuar con las opciones del menú
def menu():
    global runProgram # Llamamos de forma global a la variable runProgram
    print(".: Bienvenido al menú de tamagochi :.")

    while runProgram:
        showMenuOptions() # Invocamos la función para que el usuario vea las opciones
        opc = int(input("Ingresa una opción (1, 2 , 3 , 4 o 5): \n"))
        match opc:
            case 1:
                pass
            case 2:
                pass
            case 3:
                pass
            case 4:
                pass
            case 5:
                pass
            case _:
                print("ERROR. Opción no válida. Ingresa una opción correcta (1, 2, 3, ,4 o 5)")
