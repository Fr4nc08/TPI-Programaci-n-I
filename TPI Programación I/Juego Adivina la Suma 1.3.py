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

def guardar_puntajes(nombre, puntaje):
   """
   Recibe los usuarios y puntaje obtenidos en el juego, los muestra en pantalla y los registra en los archivos correspondientes
   """

   with open("usuarios.txt", "a") as archivo_usuarios:
    archivo_usuarios.write(nombre + "\n")

    print(f"Has obtenido {puntaje} puntos")

   with open("puntajes.txt", "a") as archivo_puntajes:
    archivo_puntajes.write(f"{nombre}: {puntaje} puntos\n")

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
  

adivina_la_suma()
while True:
      
  nombre, puntaje = jugar()
  # Extraemos los datos ingresados en la partida 
  guardar_puntajes(nombre, puntaje)
  # Guardamos los datos ingresados para luego registrarlos en los archivos  
  print("\nQuieres volver a jugar? ")
  opción = input("Presiona 1 para volver a jugar o 2 para salir del juego: ")
  if opción == "1":
    print("¡Genial! Reiniciando el juego...")
  elif opción == "2": 
   print("\n==============================================")
   print("\n¡Gracias por jugar! Hasta la próxima.")
   print("\n==============================================")
   break
  """  
   Se crea un bucle donde en caso de que el usuario quiera jugar de vuelta se reinicie el juego y 
   en caso contrario se le muestra un mensaje de despedida.
  """  
guardar_ranking(nombre, "Adivina la Suma", puntaje)
guardar_historial(nombre, "Adivina la Suma", puntaje)
guardar_estadistica("Adivina la Suma")
  
input("\nPresione ENTER para volver al menú...")