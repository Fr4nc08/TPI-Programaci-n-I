import random 

def jugar_ahorcado():
    palabras = ["python", "codigo", "juego", "programa"]
    palabra = random.choice(palabras)
    adivinado = ["_"] * len(palabra)
    intentos = 6
    puntos = 0
    puntaje = 0

    print("Bienvenido al Ahorcado")
    print("las palabras son relacionadas con la programacion")
    print("Tienes que adivinar la palabra. Tienes 6 intentos.")
    nombre = input("Ingresa tu nombre jugador: ")

    
    while intentos > 0 and "_" in adivinado:
        print("Palabra:", " ".join(adivinado))
        letra = input("Adivina una letra: ").lower()
        
        if letra in palabra:
            for i, char in enumerate(palabra):
                if char == letra:
                    adivinado[i] = letra
        else:
            intentos -= 1
            print(f"Incorrecto. Te quedan {intentos} intentos.")