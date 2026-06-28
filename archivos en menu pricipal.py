opcion = ""

while opcion != "0":

    print("\n****************************************************")
    print("BIENVENIDOS A PLAY.IN EDUGAMES")
    print("****************************************************")
    print("1 - PIEDRA,PAPEL Y TIJERA")
    print("2 - Ahorcado")
    print("3 - TRIVIA")
    print("4 - ")
    print("5 - Ver puntajes")
    print("6 - Ver ranking")
    print("7 - Ver historial")
    print("8 - Ver estadísticas")
    print("0 - Salir")
    print("****************************************************")

    opcion = input("Ingresa tu opción: ")

    if opcion == "1":
        piedra_papel_tijera()

    elif opcion == "2":
        jugar_ahorcado()

    elif opcion == "3":
        Trivia()

    elif opcion == "4":
        ()

    elif opcion == "5":
        ver_puntajes()

    elif opcion == "6":
        ver_ranking()

    elif opcion == "7":
        ver_historial()

    elif opcion == "8":
        ver_estadisticas()

    elif opcion == "0":
        print("\nGracias por usar Play.In EduGames")

    else:
        print("Opción inválida")