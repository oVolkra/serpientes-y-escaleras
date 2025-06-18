from biblioteca import *

comenzar = input("¡Bienvenido a serpientes y escaleras! ¿Desea jugar? (s/n): ").lower()
while comenzar != 's' and comenzar != 'n':
    comenzar = input("ERROR: Ingrese una opción válida (s/n): ").lower()

if comenzar == 's':
    usuario = pedir_usuario()
    jugar = True
    while jugar:
        pregunta = mostrar_preguntas(preguntas)
        respuesta_usuario = registrar_respuesta()
        comparar_respuesta(pregunta, respuesta_usuario)
        posicion = avanzar_casillas(tablero, posicion, respuesta_usuario, pregunta)
        borrar_pregunta(preguntas, pregunta)
        informar_posicion(posicion)
        representacion_tablero(tablero)
        jugar = estado_juego(posicion, preguntas, usuario)
   
else:
    print("¡Fin del juego!")

    