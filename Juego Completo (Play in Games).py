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

import random

def jugar_ahorcado():
    # Lista de palabras relacionadas con programación
    palabras = ["python", "codigo", "juego", "programa", "variable", "bucle", "funcion"]
    palabra_secreta = random.choice(palabras)
    
    # Inicialización de variables
    adivinado = ["_"] * len(palabra_secreta)
    intentos = 6
    letras_usadas = []
    puntaje = 0

    print("=== BIENVENIDO AL AHORCADO ===")
    print("Las palabras están relacionadas con la programación.")
    nombre = input("Ingresa tu nombre jugador: ")
    print(f"\n¡Hola {nombre}! Tienes {intentos} intentos para adivinar la palabra.\n")

    # Bucle principal del juego
    while intentos > 0 and "_" in adivinado:
        print("Palabra actual:", " ".join(adivinado))
        print(f"Intentos restantes: {intentos} | Letras usadas: {', '.join(letras_usadas)}")
        
        letra = input("Adivina una letra: ").lower()

        # Validaciones de entrada
        if len(letra) != 1 or not letra.isalpha():
            print(" Por favor, ingresa una sola letra válida.")
            continue
        if letra in letras_usadas:
            print(f" Ya intentaste la letra '{letra}'. Prueba con otra.")
            continue
        
        letras_usadas.append(letra)

        # Lógica de comprobación
        if letra in palabra_secreta:
            print(f"¡Bien hecho! La letra '{letra}' está en la palabra.")
            for i, char in enumerate(palabra_secreta):
                if char == letra:
                    adivinado[i] = letra
        else:
            intentos -= 1
            print(f"Incorrecto. La letra '{letra}' no está. Te quedan {intentos} intentos.")

    # Resultado final (fuera del bucle)
    # Resultado final (fuera del while)
    print("\n" + "=" * 30)

    if "_" not in adivinado:
        print(f"🏆 ¡GANASTE {nombre}! La palabra era: {palabra_secreta}")
        puntaje = 1
        print("Has ganado 1 punto.")
    else:
        print(f"😢 PERDISTE {nombre}. La palabra era: {palabra_secreta}")
        puntaje = 0

    print(f"Tu puntaje final es: {puntaje}")

    guardar_puntaje(nombre, "Ahorcado", puntaje)
    guardar_ranking(nombre, "Ahorcado", puntaje)

    if puntaje == 1:
        guardar_historial(nombre, "Ahorcado", "Ganó")
    else:
        guardar_historial(nombre, "Ahorcado", "Perdió")

    guardar_estadistica("Ahorcado")

    input("\nPresione ENTER para volver al menú...")

import random

preguntas = [
    {
        "pregunta": "¿Quien salio campeon en el mundial 1998?",
        "opciones": ["A) Francia", "B) Brasil", "C) Italia", "D) Paises bajos"],
        "respuesta": "A"
    },
    {
        "pregunta": "¿Donde se jugo el mundial 1990?",
        "opciones": ["A) Mexico", "B) Argentina", "C) Italia", "D) Estados unidos"],
        "respuesta": "C"
    },
    {
        "pregunta": "¿Maximo goleador de la historia de los mundiales?",
        "opciones": ["A) Klose", "B) Higuain", "C) Cristiano Ronaldo", "D) Messi"],
        "respuesta": "D"
    },
    {
        "pregunta": "¿Maximo asistidor de la historia de los mundiales?",
        "opciones": ["A) Messi", "B) Maradona", "C) Messi y Maradona", "D) Pele"],
        "respuesta": "C"
    },
    {
        "pregunta": "¿Jugador en recibir mas tarjetas rojas en mundiales?",
        "opciones": ["A) Pepe", "B) Zidane", "C) Ramos", "D)Ruggeri"],
        "respuesta": "B"
    },
]

def Trivia():
    print("=" * 40)
    print("       🎯 JUEGO DE TRIVIA 🎯")
    print("=" * 40)
    nombre = input("¿Cómo te llamás? ").strip()  # ← LÍNEA NUEVA
    print(f"\n¡Buena suerte, {nombre}!\n")        # ← LÍNEA NUEVA

    puntos = 0
    seleccion = random.sample(preguntas, len(preguntas))
    for i, item in enumerate(seleccion, 1):
        print(f"\nPregunta {i}/{len(seleccion)}:")
        print(item["pregunta"])
        for opcion in item["opciones"]:
            print("  ", opcion)
        respuesta = input("\nTu respuesta (A/B/C/D): ").strip().upper()
        if respuesta == item["respuesta"]:
            print("✅ ¡Correcto!")
            puntos += 1
        else:
            print(f"❌ Incorrecto. La respuesta era: {item['respuesta']}")

        print("\n" + "=" * 40)
        print(f"  {nombre}, tu resultado: {puntos}/{len(seleccion)} puntos")  # ← MODIFICADA
    if puntos == len(seleccion):
        print("  🏆 ¡Perfecto! ¡Lo lograste!")
    elif puntos >= len(seleccion) // 2:
        
        print("  👍 ¡Buen trabajo!")
    else:
        
        print("  💪 ¡Sigue practicando!")
        print("=" * 40)
        
    if puntos >= len(seleccion) // 2:
        puntaje = 1
    else:
        puntaje = 0

    guardar_puntaje(nombre, "JUEGO TRIVIA", puntaje)
    guardar_ranking(nombre, "JUEGO TRIVIA", puntaje) 

    if puntaje == 1:
        guardar_historial(nombre, "JUEGO TRIVIA", "Ganó")
    else:
        guardar_historial(nombre, "JUEGO TRIVIA", "Perdió")

    guardar_estadistica("JUEGO TRIVIA")

    input("\nPresione ENTER para volver al menú...")

def adivina_la_suma():
    print("==============================================")
    print("\n¡¡Bienvenido al juego Adivina la suma!!")
    print("Tendrás que descubrir la suma de dos números naturales para obtener el resultado secreto.")
    print("\n==============================================")
    input("Escribe 1 para ingresar... ")
    print("\n¡Comencemos!")
    print("Tienes 5 intentos para adivinar el resultado correcto.")
    print("El puntaje que obtendras depende de la cantidad de intentos que utilices.")
    """
    Mostramos el texto de bienvenida, explicamos las reglas del juego 

    """

def guardar_puntajes(nombre,juego, puntaje):
   """
   Recibe los usuarios y puntaje obtenidos en el juego, los muestra en pantalla y los registra en los archivos correspondientes
   """

   with open("usuarios.txt", "a") as archivo_usuarios:
    archivo_usuarios.write(nombre + "\n")

    print(f"Has obtenido {puntaje} puntos")

   with open("puntajes.txt", "a") as archivo_puntajes:
    archivo_puntajes.write(f"{nombre} - {juego} - {puntaje}\n")

import random
def jugar():
   num1 = random.randint(1, 1000)
   num2 = random.randint(1,1000)
   """
   Generación de dos números aleatorios entre 1 y 1000 para que el jugador adivine el resultado correspondiente.
   """
   usuario = input("\nIngresa tu nombre completo:" )
    # Pedimos que ingresen su nombre 
   puntaje = 0
   suma = num1 + num2
   # Generamos la variable de la suma de los números y una para el puntaje.
   for i in range(5):
      print(f"\nDescubre el resultado a obtener de la suma: {num1} + {num2} ")
      print(f"Intento {i + 1}")
      # Mostramos los numeros que se suman y el número de intentos actuales

      try:
        resultado = int(input("Ingresa el resultado que crees correcto:"))
      except ValueError:
        print("Por favor, ingresa un número natural válido")
        continue
    
      if resultado == suma:
        print("\n¡Felicidades! Has adivinado el resultado")
        puntaje = 5 - i
        break
       # Mensaje de felicitación y generación de puntaje 
      else:
        print("\nLo siento, el resultado ingresado es incorrecto.")
        print("¡Intentalo de nuevo!")
        print(f"Intentos restantes: {4 - i}")

   if puntaje == 0:
     print("\n¡Lo siento! Te has quedado sin intentos")
   return usuario, puntaje
  

def adivina_la_suma():

    # Mostrar bienvenida

    while True:

        nombre, puntaje = jugar()

        guardar_puntajes(nombre,"Adivina la suma", puntaje)
        guardar_ranking(nombre, "Adivina la Suma", puntaje)

        if puntaje > 0:
            guardar_historial(nombre, "Adivina la Suma", "Ganó")
        else:
            guardar_historial(nombre, "Adivina la Suma", "Perdió")

        guardar_estadistica("Adivina la Suma")

        opcion = input("1- Jugar otra vez\n2- Volver al menú\n")

        if opcion == "2":
            break

    input("\nPresione ENTER para volver al menú...")

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

opcion = ""

while opcion != "0":

    print("\n****************************************************")
    print("BIENVENIDOS A PLAY.IN EDUGAMES")
    print("****************************************************")
    print("1 - PIEDRA,PAPEL Y TIJERA")
    print("2 - Ahorcado")
    print("3 - TRIVIA")
    print("4 - SUMAS")
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
        adivina_la_suma()

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