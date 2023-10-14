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
    print("1) Jugar al frifayer.")
    print("2) Jugar a romper PR en press banca.")
    print("3) No jugar.")
    while True:
        opc = int(input("Ingresa una opción para jugar (1, 2 o 3): "))
        match opc:
            case 1:
                print("Jugar al frifayer te hará gritar como niño rata.")
            case 2:
                print("Jugar a romper tu PR en press banca te podnrá mamadisimo hdsptm.")
            case 3:
                print("Jugaremos más tarde.")
                break
            case _: 
                print("ERROR. Opción no válida. Ingresa una opción correcta (1, 2, o 3): ")

#Función para el submenú COMER
def comer():
    print("¿Qué deseas jugar?\n")
    print("1) Comer prote + preworkout.")
    print("2) Comer atún + plátano.")
    print("3) No comer.")
    while True:
        opc = int(input("Ingresa una opción para jugar (1, 2 o 3): "))
        match opc:
            case 1:
                print("Comer la prote + el preworkput te pondrá mamadismo hdsptm.")
            case 2:
                print("Comer atún + plátano también te pondra mamadismo hdsptm pero sin taquicardias.")
            case 3:
                print("Comeremos algo más tarde.")
                break
            case _: 
                print("ERROR. Opción no válida. Ingresa una opción correcta (1, 2, o 3): ")

#Función para el submenú DORMIR
def dormir():
    print("¿Qué tanto tiempo deseas dormir?\n")
    print("1) Dormir 1 hora (sin poner alarma).")
    print("2) Dormir toda la noche (sin soñar con ella).")
    print("3) No dormir.")
    while True:
        opc = int(input("Ingresa una opción para jugar (1, 2 o 3): "))
        match opc:
            case 1:
                print("Dormir 1 hora sin alarma hará que duermas alrededor de 3 horas xd")
            case 2:
                print("Dormir toda la noche sin pensar en ella hará que recuperes toda tu energía")
            case 3:
                print("Dormiremos más tarde.")
                break
            case _: 
                print("ERROR. Opción no válida. Ingresa una opción correcta (1, 2, o 3): ")
