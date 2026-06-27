import random 

def jugar_ahorcado():
    palabras = ["python", "codigo", "juego", "programa"]
    palabra = random.choice(palabras)
    adivinado = ["_"] * len(palabra)
    intentos = 6
    puntos = 0
    puntaje = 0
