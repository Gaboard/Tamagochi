# Creación del menú de opciones para tamagochi
import os
runProgram = True # Variable de control para el while de la función menu.
energia, hambre = 0

#Función para mostrar las opciones del menú
def showMenuOptions():
    print("¿Qué actividad desas que realize tu tamagochi?")
    print("")
    print("1) Jugar.")
    print("2) Comer.")
    print("3) Dormir.")
    print("4) Ver estado.")
    print("5) Salir.\n")

# Función para interactuar con las opciones del menú.
def menu():
    global runProgram # Llamamos de forma global a la variable runProgram.
    print(".: Bienvenido al menú de tamagochi :.")

    while runProgram:
        showMenuOptions() # Invocamos la función para que el usuario vea las opciones.
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
                print("Hasta luego")
                break
            case _:
                print("ERROR. Opción no válida. Ingresa una opción correcta (1, 2, 3, ,4 o 5): ")

# Función para el submenú JUGAR
def play():
    print("¿A qué deseas jugar?\n")
    print("1) Jugar al parque.")
    print("2) Jugar con un juguete.")
    print("3) No jugar.")
    while True:
        opc = int(input("Ingresa una opción para jugar (1, 2 o 3): "))
        match opc:
            case 1:
                print("Jugemos en el parque.")
            case 2:
                print("Jugemos con un juguete.")
            case 3:
                print("Jugaremos más tarde.")
                break
            case _: 
                print("ERROR. Opción no válida. Ingresa una opción correcta (1, 2, o 3): ")
