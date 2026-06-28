import random

def piedra_papel_tijera():

    print("\n****************************************************")
    print("5 - PIEDRA, PAPEL O TIJERA")
    print("****************************************************")

    nombre = input("Ingrese su nombre: ")

    print("1 - Piedra")
    print("2 - Papel")
    print("3 - Tijera")

    jugador = int(input("Elija una opción: "))

    computadora = random.randint(1, 3)

    if computadora == 1:
        print("La computadora eligió Piedra")
    elif computadora == 2:
        print("La computadora eligió Papel")
    else:
        print("La computadora eligió Tijera")

    if jugador == computadora:
        print("Empate")
        puntaje = 0

    elif (jugador == 1 and computadora == 3) or \
         (jugador == 2 and computadora == 1) or \
         (jugador == 3 and computadora == 2):

        print("¡Ganaste!")
        puntaje = 1

    else:
        print("Perdiste")
        puntaje = 0

        guardar_puntaje(nombre, "Piedra Papel Tijera", puntaje)

        guardar_ranking(nombre, "Piedra Papel Tijera", puntaje)

    if puntaje == 1:
        guardar_historial(nombre, "Piedra Papel Tijera", "Ganó")
    else:
        guardar_historial(nombre, "Piedra Papel Tijera", "Perdió")
    
    guardar_estadistica("Piedra Papel Tijera")
    input("\nPresione ENTER para volver al menú...")