from preguntas import *
import csv
import random
tablero = [0, 1, 0, 0, 0 , 3, 0, 0, 0, 0, 0, 1, 0, 0, 2, 1, 1, 0, 0, 0, 1, 0, 0, 2, 0, 0, 0, 1, 0, 0, 0]
posicion = 15

def pedir_usuario():
    """Función para solicitar y almacenar un nombre de usuario.
    No recibe parámetros.
    Devuelve la variable 'usuario'."""
    usuario = input("Ingrese su nombre de usuario: ")
    return usuario

def mostrar_preguntas(preguntas):   
    """Función que imprime una pregunta aleatoria de la lista de diccionarios 'preguntas'.
    Recibe como parámetro la lista de preguntas.
    Devuelve el diccionario de la pregunta seleccionada aleatoriamente."""
    pregunta = random.choice(preguntas)
    
    print("---------------------------"
        f"\n{pregunta["pregunta"]}\n"
    f"A. {pregunta["respuesta_a"]}\n"
    f"B. {pregunta["respuesta_b"]}\n"
    f"C. {pregunta["respuesta_c"]}\n"
    "---------------------------")

    return pregunta

def registrar_respuesta():
    """Función para registrar la respuesta del usuario.
    No recibe parámetros.
    Devuelve la variable 'respuesta_usuario'."""
    respuesta_usuario = input("Ingrese la respuesta (a/b/c): ").lower()
    while respuesta_usuario != 'a' and respuesta_usuario != 'b' and respuesta_usuario != 'c':
        respuesta_usuario = input("ERROR: Ingrese la respuesta (a/b/c): ").lower()
    
    return respuesta_usuario

def comparar_respuesta(pregunta, respuesta_usuario):
    """Función que compara respuesta_usuario con el value de la key respuesta_correcta, ubicada en el diccionario 'pregunta'.
    Recibe como parámetros pregunta y respuesta_usuario.
    Devuelve un mensaje impreso según la respuesta del usuario."""
    if respuesta_usuario == pregunta["respuesta_correcta"]:
        print(f"¡Respuesta correcta!")
    else:
        print(f"¡Respuesta incorrecta!")      

def borrar_pregunta(pregunta, pregunta_respondida):
    """Función que borra una pregunta ya impresa y respondida por el usuario.
    Recibe como parámetros pregunta y pregunta_respondida."""
    if pregunta_respondida in preguntas:
        preguntas.remove(pregunta_respondida)

def avanzar_casillas(tablero, posicion, respuesta_usuario, pregunta):
    """Función que calcula los movimientos en el tablero, según las respuestas a las preguntas.
    Recibe como parámetros 'tablero', 'posición', 'respuesta_usuario' y 'pregunta'.
    Devuelve la variable 'posicion'."""
    if respuesta_usuario == pregunta["respuesta_correcta"]:
        posicion += 1
        if tablero[posicion] != 0:
            print(f"¡Casilla premio! Avanza {tablero[posicion]} casilla/s.")
            posicion += tablero[posicion]
            
    else:
        posicion -= 1
        if tablero[posicion] != 0:
            print(f"¡Casilla de castigo!. Retrocede {tablero[posicion]} casilla/s. ")
            posicion -= tablero[posicion]
            
    return posicion

def informar_posicion(posicion):
    """Función que imprime un mensaje informando la posición del jugador."""
    print(f"\nEstás en la posición {posicion}")

def estado_juego(posicion, preguntas, usuario):
    """Función que define el estado del juego según la posición del jugador, estado de la lista de diccionarios o si el jugador decide seguir jugando.
    Recibe como parámetros 'posicion' y la lista de diccionarios 'preguntas' y 'usuario'.
    Devuelve la variable 'jugar' en True o False o la variable 'continuar'."""
    jugar = True
    if posicion == 30:
        print("\n¡FELICITACIONES, GANASTE :D!")
        print("¡Fin del juego!")
        crear_archivo_score(usuario, posicion)
        jugar = False
    elif posicion == 0:
        print("\n¡PERDISTE D:!")
        print("¡Fin del juego!")
        crear_archivo_score(usuario, posicion)
        jugar = False
    elif not preguntas:
        print("\n¡Te quedaste sin preguntas! ¡PERDISTE D:!")
        print("¡Fin del juego!")
        print(f"Tu posición final es la {posicion}.")
        crear_archivo_score(usuario, posicion)
        jugar = False
    else:
        continuar = input("\n¿Deseas continuar jugando? (s/n): ").lower()
        while continuar != 's' and continuar != 'n':
            continuar = input("\nERROR: Ingrese una opción válida (s/n): ").lower()
        if continuar == 'n':
            crear_archivo_score(usuario, posicion)
            print("¡Fin del juego!")
            print(f"Tu posición final es la {posicion}.")

            
    
        return continuar == 's'

def representacion_tablero(tablero):
    """Función para imprimir el tablero del juego.
    Recibe como parámetro 'tablero'."""
    for i in range(len(tablero)):
        print(f"{tablero[i]} ({i})", end='|')

def crear_archivo_score(usuario, posicion):
    """Función que crea un archivo score.csbv. Una vez que ya existe, agrega los valores de las variables 'usuario' y 'posicionh'.
    Recibe como parámetros 'usuario' y posicion'.
    Devuelve el archivo score.csv."""
    with open("score.csv", mode="a", newline="") as archivo:
        escritor = csv.writer(archivo, delimiter=';')
        escritor.writerow(["Usuario", "Puntaje final"])
        escritor.writerow([usuario, posicion])
