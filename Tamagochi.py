# Creación del menú de opciones para tamagochi
import os
runProgram = True # Variable de control para el while de la función menu.
energia = 100
hambre = 0

#Función para imprimir el status actual
def status():
    print(f"Tu energía actual es: {energia}%")
    print(f"Tu hambre actual es: {hambre}%\n")

#Función para mostrar las opciones del menú
def showMenuOptions():
    print("¿Qué actividad desas que realize tu tamagochi?")
    print("")
    print("1) Jugar.")
    print("2) Comer.")
    print("3) Dormir.")
    print("4) Ver estado.")
    print("5) Salir.\n")

# Función para el submenú JUGAR
def play():
    global energia, hambre
    print(f"Tu estatus actual es: energía: {energia}, hambre {hambre}")
    print("¿A qué deseas jugar?\n")
    print("1) Jugar al frifayer.")
    print("2) Jugar a romper PR en press banca.")
    print("3) No jugar.")
    while True:
        opc = int(input("Ingresa una opción para jugar (1, 2 o 3): "))
        match opc:
            case 1:
                print("Jugar al frifayer te hará gritar como niño rata.")
                energia = energia-20
                hambre = hambre+10
            case 2:
                print("Jugar a romper tu PR en press banca te podnrá mamadisimo hdsptm.")
                energia = energia-30
                hambre =  hambre+30
            case 3:
                print("Jugaremos más tarde.")
                break
            case _: 
                print("ERROR. Opción no válida. Ingresa una opción correcta (1, 2, o 3): ")

#Función para el submenú COMER
def comer():
    global energia, hambre
    print(f"Tu estatus actual es: energía: {energia}, hambre {hambre}")
    print("¿Qué deseas jugar?\n")
    print("1) Comer prote + preworkout.")
    print("2) Comer atún + plátano.")
    print("3) No comer.")
    while True:
        opc = int(input("Ingresa una opción para jugar (1, 2 o 3): "))
        match opc:
            case 1:
                print("Comer la prote + el preworkput te pondrá mamadismo hdsptm.")
                energia = energia-15
                hambre = hambre-30
            case 2:
                print("Comer atún + plátano también te pondra mamadismo hdsptm pero sin taquicardias.")
                energia = energia-5
                hambre = hambre-30
            case 3:
                print("Comeremos algo más tarde.")
                break
            case _: 
                print("ERROR. Opción no válida. Ingresa una opción correcta (1, 2, o 3): ")

#Función para el submenú DORMIR
def dormir():
    print(f"Tu estatus actual es: energía: {energia}, hambre {hambre}")
    global energia, hambre
    print("¿Qué tanto tiempo deseas dormir?\n")
    print("1) Dormir 1 hora (sin poner alarma).")
    print("2) Dormir toda la noche (sin soñar con ella).")
    print("3) No dormir.")
    while True:
        opc = int(input("Ingresa una opción para jugar (1, 2 o 3): "))
        match opc:
            case 1:
                print("Dormir 1 hora sin alarma hará que duermas alrededor de 3 horas xd")
                hambre = hambre+10
                energia = energia+50
            case 2:
                print("Dormir toda la noche sin pensar en ella hará que recuperes toda tu energía")
                hambre = hambre+30
                energia = 100
            case 3:
                print("Dormiremos más tarde.")
                break
            case _: 
                print("ERROR. Opción no válida. Ingresa una opción correcta (1, 2, o 3): ")

# Función para interactuar con las opciones del menú.
def menu():
    global runProgram # Llamamos de forma global a la variable runProgram.
    print(".: Bienvenido al menú de tamagochi :.")

    while runProgram:
        showMenuOptions() # Invocamos la función para que el usuario vea las opciones.
        opc = int(input("Ingresa una opción (1, 2 , 3 , 4 o 5): \n"))
        match opc:
            case 1:
                if energia<30 and hambre <30:
                    play()
                else:
                    print(f"Tu energía: {energia}% o hambre: {hambre}% , no son suficientes para jugar ahora")
                    print("Descansa y/o come un poco para que puedas jugar")
            case 2:
                comer()
            case 3:
                dormir()
            case 4:
                print("Hasta luego")
                runProgram = False
            case _:
                print("ERROR. Opción no válida. Ingresa una opción correcta (1, 2, 3, ,4 o 5): ")

# Evalua si la función con la que estamos trabajando es la principal en nuestra ejecución
if __name__ == "__menu__":
    menu()