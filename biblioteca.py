from preguntas import *
import csv
import random

tablero = [0, 1, 0, 0, 0 , 3, 0, 0, 0, 0, 0, 1, 0, 0, 2, 1, 1, 0, 0, 0, 1, 0, 0, 2, 0, 0, 0, 1, 0, 0, 0]
posicion = 15

def archivo_ya_existe():
    """Función que verifica la existencia o no del archivo 'score.csv'.
    No recibe parámetros.
    Devuelve un bool que determina si existe o no."""
    
    existe = False
    try:
        with open("score.csv", "r", newline="") as archivo:
            existe = bool(archivo.readline())
    except FileNotFoundError:
        existe = False
        
    return existe

def crear_archivo_score(usuario, posicion): #verificar que exista con un if en otra funcion
    """Función que crea un archivo score.csv. Una vez que ya existe, agrega los valores de las variables 'usuario' y 'posicion'.
    Recibe como parámetros 'usuario' y posicion'.
    Devuelve el archivo score.csv, actualizado con cada ejecución del juego."""
    
    nombre_columnas = not archivo_ya_existe()

    with open("score.csv", "a", newline="") as archivo:
        escritor = csv.writer(archivo, delimiter=';')
        if nombre_columnas:
            escritor.writerow(["Usuario", "Puntaje final"])
        escritor.writerow([usuario, posicion])
    

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
    
    respuesta_usuario = validar_datos_input("Ingrese la respuesta", ['a', 'b', 'c']).lower()
    
    return respuesta_usuario

def comparar_respuesta(pregunta, respuesta_usuario):
    """Función que compara respuesta_usuario con el value de la key respuesta_correcta, ubicada en el diccionario 'pregunta'.
    Recibe como parámetros pregunta y respuesta_usuario.
    Devuelve un mensaje impreso según la respuesta del usuario."""
    
    if respuesta_usuario == pregunta["respuesta_correcta"]:
        print(f"¡Respuesta correcta!")
    else:
        print(f"¡Respuesta incorrecta!")      

def avanzar_casillas(tablero, posicion, respuesta_usuario, pregunta):
    """Función que calcula los movimientos en el tablero, según las respuestas a las preguntas.
    Recibe como parámetros 'tablero', 'posición', 'respuesta_usuario' y 'pregunta'.
    Devuelve la variable 'posicion'."""
    
    #Usuario responde correctamente y avanza a una casilla != 0
    if respuesta_usuario == pregunta["respuesta_correcta"]:
        posicion += 1
        if tablero[posicion] != 0:
            print(f"¡Casilla premio! Avanza {tablero[posicion]} casilla/s.")
            posicion += tablero[posicion]
            
    #Usuario responde incorrectamente y retrocede a una casilla != 0
    else:
        posicion -= 1
        if tablero[posicion] != 0:
            print(f"¡Casilla de castigo!. Retrocede {tablero[posicion]} casilla/s. ")
            posicion -= tablero[posicion]
            
    return posicion

def borrar_pregunta(preguntas, pregunta_respondida):
    """Función que borra una pregunta ya impresa y respondida por el usuario.
    Recibe como parámetros pregunta y pregunta_respondida."""
    
    if pregunta_respondida in preguntas:
        preguntas.remove(pregunta_respondida)

def informar_posicion(posicion):
    """Función que imprime un mensaje informando la posición del jugador.
    Recibe como parámetro 'posicion'.
    Devuelve un mensaje informando la posición actual."""
    
    print(f"\nEstás en la posición {posicion}")

def validar_datos_input(mensaje, opciones):
    """Función para validar la entrada de datos de un input.
    Recibe como parámetros el mensaje que pide la entrada de datos y las opciones a validar.
    Retorna la entrada validada."""
    
    opciones_str = "/".join(opciones)
    entrada = input(f"{mensaje} ({opciones_str}): ").lower()
    while entrada not in opciones:
        entrada = input(f"ERROR: Ingrese una opción válida ({opciones_str}): ").lower()
    
    return entrada

def desea_continuar(usuario, posicion):
    """Función que solicita al usuario continuar o no con la ejecución del juego.
    Recibe como parámetros 'usuario' y 'posicion'
    Retorna la variable jugar en True si desea seguir jugando, o False si decide dejar de jugar."""
    
    jugar = True
    continuar = validar_datos_input("\n¿Deseas continuar jugando?", ['s', 'n']).lower()
    if continuar == 'n':
        crear_archivo_score(usuario, posicion)
        mensaje_fin_juego()
        mensaje_posicion_final(posicion)
        jugar = False
    
    return jugar

def victoria(posicion):
    """Función para controlar la condición de victoria.
    Recibe como parámetro 'posicion'.
    Retorna la variable 'posicion' cuando vale 30."""
    
    return posicion == 30

def derrota(posicion):
    """Función para controlar la condición de derrota.
    Recibe como parámetro 'posicion'.
    Retorna la variable 'posicion' cuando vale 0."""
    
    return posicion == 0

def sin_preguntas(preguntas):
    """Función para controlar la condición de derrota cuando la lista de preguntas queda vaca.
    Recibe como parámetro 'posicion'.
    Retorna True si la lista está vacía, False en caso contrario."""
    
    return not preguntas

def estado_juego(posicion, preguntas, usuario):
    """Función que define el estado del juego según la posición del jugador, estado de la lista de diccionarios o si el jugador decide seguir jugando.
    Recibe como parámetros 'posicion' y la lista de diccionarios 'preguntas' y 'usuario'.
    Devuelve la variable 'jugar' en True o False o la variable 'continuar'."""
    
    hay_victoria = victoria(posicion)
    hay_derrota = derrota(posicion)
    no_hay_preguntas = sin_preguntas(preguntas)
    
    if hay_victoria or hay_derrota or no_hay_preguntas:
        printear_mensajes(posicion, preguntas)
        mensaje_fin_juego()
        crear_archivo_score(usuario, posicion)
        jugar = False
    
    else:
        jugar = desea_continuar(usuario, posicion)

    return jugar

def representacion_tablero(tablero):
    """Función para imprimir el tablero del juego.
    Recibe como parámetro 'tablero'.
    Devuelve un print del tablero."""
    
    for i in range(len(tablero)):
        print(f"{tablero[i]} ({i})", end='|')

def printear_mensajes(posicion, preguntas):
    """Función que imprime mensajes según la condición de finalización del juego(victoria, derrota).
    Recibe como parámetros 'posicion' y 'preguntas'
    Devuelve mensajes impresos."""
   
    if victoria(posicion):
        print("\n¡FELICITACIONES, GANASTE :D!")
    
    if derrota(posicion):
        print("\n¡PERDISTE D:!")
    
    if sin_preguntas(preguntas):
        mensaje_posicion_final(posicion)
        print("¡Te quedaste sin preguntas!")

def mensaje_fin_juego():
    """Función para imprimir un mensaje que indica que terminó el juego.
    Devuelve un mensaje impreso."""
    
    print("¡Fin del juego!")

def mensaje_posicion_final(posicion):
    """Función para imprimir un mensaje que informa la posición final.
    Recibe como parámetro 'posicion'.
    Devuelve un mensaje impreso."""
    
    print(f"Tu posición final es la {posicion}.")

def preguntas_restantes(preguntas):
    """Función para imprimir un mensaje que informa la cantidad de preguntas restantes.
    Recibe como parámetro 'preguntas'.
    Devuelve un mensaje impreso."""
    
    print("\nCantidad de preguntas restantes:", len(preguntas))

