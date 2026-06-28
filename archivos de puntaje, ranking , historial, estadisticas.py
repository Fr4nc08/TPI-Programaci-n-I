def guardar_puntaje(nombre, juego, puntaje):

    archivo = open("puntajes.txt", "a")

    archivo.write(nombre)
    archivo.write(" - ")
    archivo.write(juego)
    archivo.write(" - ")
    archivo.write(str(puntaje))
    archivo.write("\n")

    archivo.close()

def guardar_ranking(nombre, juego, puntaje):

    archivo = open("ranking.txt", "a")

    archivo.write(nombre)
    archivo.write(";")
    archivo.write(juego)
    archivo.write(";")
    archivo.write(str(puntaje))
    archivo.write("\n")

    archivo.close()

def guardar_historial(nombre, juego, resultado):

    archivo = open("historial.txt", "a")

    archivo.write(nombre)
    archivo.write(" - ")
    archivo.write(juego)
    archivo.write(" - ")
    archivo.write(resultado)
    archivo.write("\n")

    archivo.close()

def guardar_estadistica(juego):

    archivo = open("estadisticas.txt", "a")

    archivo.write(juego)
    archivo.write("\n")

    archivo.close()