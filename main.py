from biblioteca import *

comenzar = validar_datos_input("¡Bienvenido a serpientes y escaleras! ¿Desea jugar?", ['s', 'n']).lower()

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
        preguntas_restantes(preguntas)
        jugar = estado_juego(posicion, preguntas, usuario)
else:
    mensaje_fin_juego()

    
