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