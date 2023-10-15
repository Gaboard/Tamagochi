# Creación del menú de opciones para tamagochi
import os
runProgram = True # Variable de control para el while de la función menu.
energia = 100
hambre = 0
name = ""
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
    global energia, hambre, name
    while energia>30 and hambre<30:
        status()
        print("¿A qué deseas jugar?\n")
        print("1) Jugar al frifayer.")
        print("2) Jugar a romper PR en press banca.")
        print("3) No jugar.")
        opc = int(input("Ingresa una opción para jugar (1, 2 o 3): "))
        match opc:
            case 1:
                print(f"Jugar al frifayer hará que {name} girte como niño rata.\n")
                energia = energia-20
                hambre = hambre+10
                os.system("cls")
            case 2:
                print(f"Jugar a que {name} rompa su PR en press banca lo pondrá mamadisimo hdsptm.\n")
                energia = energia-30
                hambre =  hambre+30
                os.system("cls")
            case 3:
                print("Jugar más tarde.\n")
                break
            case _: 
                print("ERROR. Opción no válida. Ingresa una opción correcta (1, 2, o 3): \n")

#Función para el submenú COMER
def comer():
    global energia, hambre, name
    while energia>15 and hambre>0:
        status()
        print("¿Qué deseas jugar?\n")
        print("1) Comer prote + preworkout.")
        print("2) Comer atún + plátano.")
        print("3) No comer.")
        opc = int(input("Ingresa una opción para jugar (1, 2 o 3): "))
        match opc:
            case 1:
                print(f"Comer la prote + el preworkout pondrá a {name} mamadismo hdsptm.")
                energia = energia-15
                hambre = hambre-30
                os.system("cls")
            case 2:
                print("Comer atún + plátano también pondrá a {name} mamadismo hdsptm pero sin taquicardias.")
                energia = energia-5
                hambre = hambre-30
                os.system("cls")
            case 3:
                print("Come algo más tarde.")
                break
            case _: 
                print("ERROR. Opción no válida. Ingresa una opción correcta (1, 2, o 3): ")

#Función para el submenú DORMIR
def dormir():
    global energia, hambre, name
    while energia>0 and hambre<30:
        status()
        print("¿Qué tanto tiempo deseas dormir?\n")
        print("1) Dormir 1 hora (sin poner alarma).")
        print("2) Dormir toda la noche (sin soñar con ella).")
        print("3) No dormir.")
        opc = int(input("Ingresa una opción para jugar (1, 2 o 3): "))
        match opc:
            case 1:
                print(f"Dormir 1 hora sin alarma hará que {name} duerma alrededor de 3 horas xd")
                hambre = hambre+10
                energia = energia+50
                os.system("cls")
            case 2:
                print(f"Dormir toda la noche sin pensar en ella hará que {name} recupere toda su energía")
                hambre = hambre+30
                energia = 100
                os.system("cls")
            case 3:
                print(f"Dormir a {name} más tarde.")
                break
            case _: 
                print("ERROR. Opción no válida. Ingresa una opción correcta (1, 2, o 3): ")

# Función para interactuar con las opciones del menú.
def menu():
    global runProgram # Llamamos de forma global a la variable runProgram.
    print(".: Bienvenido al menú de tamagochi :.")
    name = str(input("Ingresa el nombre de tu tamagochi: "))

    while runProgram:
        showMenuOptions() # Invocamos la función para que el usuario vea las opciones.
        opc = int(input("Ingresa una opción (1, 2 , 3 , 4 o 5):"))
        match opc:
            case 1:
                os.system("cls")
                if energia>30 and hambre<30:
                    play()
                else:
                    print(f"La energía de {name}: {energia}% o hambre: {hambre}% , no son suficientes para jugar ahora.")
                    print("Descansa y/o come un poco para que puedas jugar.")
            case 2:
                os.system("cls")
                if energia>15 and hambre>0:
                    comer()
                else:
                    print(f"La energía de {name}: {energia}%, no es suficiente para comer ahora.")
                    print("Descansa un poco para que puedas comer.")
            case 3:
                os.system("cls")
                if energia>0 and hambre>30:
                    dormir()
                else:
                    print(f"El hambre de {name}: {hambre}% , es demasiado baja para dormir ahora.")
                    print("Come un poco para que puedas dormir.")
            case 4:
                os.system("cls")
                status()
            case 5:
                print("Hasta luego")
                runProgram = False
            case _:
                os.system("cls")
                print("ERROR. Opción no válida. Ingresa una opción correcta (1, 2, 3, ,4 o 5): ")

# Llama a la función principal 
if __name__ == '__main__':
    menu()