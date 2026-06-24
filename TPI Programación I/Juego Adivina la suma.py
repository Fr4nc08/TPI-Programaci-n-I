import random
resultado = random.randint(1, 1000)
""""
generación de un número aleatorio entre 1 y 1000 para que el jugador lo adivine realizando
 la suma de dos números naturales.
"""

print("¡¡Bienvenido al juego: Descubre la suma!!")
print("Tendrás que descubrir la suma de dos números naturales para obtener el resultado que se muestre en pantalla.")
input("Presiona enter para ingresar...")
print("\n¡Comencemos!")
print("Tienes 5 intentos para adivinar la suma correcta.")
"""
Mostramos el texto de bienvenida y explicamos las reglas del juego.
"""
suma = 0
for i in range(5):
    print(f"\nEl resultado a obtener es: {resultado} ")
    print(f"Intento {i + 1}")
    try:
      num1 = int(input("Ingresa el primer número natural:"))
      num2 = int(input("Ingresa el segundo número natural:"))
    except ValueError:
      print("Por favor, ingresa un número natural válido")
    suma = num1 + num2
    if suma == resultado:
        print("¡Felicidades! Has adivinado la suma correcta.")
        break
    else:
        print(f"Lo siento, la suma ingresada es incorrecta. Tu suma dió: {suma} ")
        print("¡Intentalo de nuevo!")
        print(f"Intentos restantes: {4 - i}")
if "Intentos restantes: 0":
        print("¡Lo siento! Te has quedado sin intentos")
        print("Quieres volver a jugar? ")
        input("Presiona 1 para volver a jugar o 2 para salir del juego: ")
if input == "1":
       print("¡Genial! Reiniciando el juego...")
       resultado = random.randint(1,1000)
       suma = 0
else:  
 print("¡Gracias por jugar! Hasta la próxima.")

    
    
