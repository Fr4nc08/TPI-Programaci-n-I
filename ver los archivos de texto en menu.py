def ver_puntajes():

    print("\n****************************************************")
    print("PUNTAJES GUARDADOS")
    print("****************************************************")

    try:

        archivo = open("puntajes.txt", "r")

        for linea in archivo:
            print(linea, end="")

        archivo.close()

    except:
        print("Todavía no hay puntajes guardados.")

    input("\nPresione ENTER para volver al menú...")

def ver_ranking():

    print("\n****************************************************")
    print("RANKING DE JUGADORES")
    print("****************************************************")

    try:

        archivo = open("ranking.txt", "r")

        ranking = []

        # Leer el archivo
        for linea in archivo:

            datos = linea.strip().split(";")

            # Si la línea está mal escrita, la salta
            if len(datos) != 3:
                continue

            nombre = datos[0]
            juego = datos[1]
            puntaje = int(datos[2])

            ranking.append([nombre, juego, puntaje])

        archivo.close()

        # Ordenar de mayor a menor
        for i in range(len(ranking) - 1):

            for j in range(i + 1, len(ranking)):

                if ranking[j][2] > ranking[i][2]:

                    aux = ranking[i]
                    ranking[i] = ranking[j]
                    ranking[j] = aux

        # Mostrar el ranking
        print("\nPOS\tJUGADOR\t\tJUEGO\t\t\tPUNTAJE")
        print("------------------------------------------------------------")

        puesto = 1

        for jugador in ranking:

            print(puesto, "-", jugador[0], "-", jugador[1], "-", jugador[2])

            puesto = puesto + 1

    except:

        print("Todavía no hay ranking.")

    input("\nPresione ENTER para volver al menú...")
def ver_historial():

    print("\n******** HISTORIAL DE PARTIDAS ********")

    try:

        archivo = open("historial.txt", "r")

        for linea in archivo:
            print(linea, end="")

        archivo.close()

    except:
        print("Todavía no hay historial.")

    input("\nPresione ENTER para volver...")
def ver_estadisticas():

    print("\n******** ESTADÍSTICAS ********")

    try:

        archivo = open("estadisticas.txt", "r")

        contador = 0

        for linea in archivo:
            print(linea, end="")
            contador = contador + 1

        archivo.close()

        print("\nTotal de juegos iniciados:", contador)

    except:
        print("Todavía no hay estadísticas.")

    input("\nPresione ENTER para volver...")