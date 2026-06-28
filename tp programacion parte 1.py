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
