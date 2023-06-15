"""
Etapa 4 - Integración
En esta etapa debemos integrar las funcionalidades resueltas en cada una de las etapas
anteriores, haciendo un uso adecuado de las funciones escritas.
La secuencia del juego debe ser la siguiente:
1. Se deberá comenzar con la generación del diccionario de palabras.
2. Luego se deben seleccionar las 10 letras participantes.
3. El programa elegirá al azar la lista de palabras a adivinar por el jugador.
4. Luego se armará el tablero que visualizará el usuario, y dará comienzo la partida,
implementando así, lo realizado en la etapa 
"""

from Parte_3 import *

def datos_rosco(cargar_datos_para_rosco, cargar_letras, cargar_palabras):
    """
    Esta funcion integra las funcionalidades resueltas en cada una de las etapas anteriores.
    """
    diccionario_rosco = cargar_datos_para_rosco()
    lista = cargar_letras()
    palabra, definicion = cargar_palabras(diccionario_rosco, lista)
    return lista, palabra, definicion

def mostrar_tablero(aciertos, errores, lista, lista_2):
    """
    Esta funcion imprime lo que el usuario vizualiza.
    """
    print(f"""
[{lista[0]}][{lista[1]}][{lista[2]}][{lista[3]}][{lista[4]}][{lista[5]}][{lista[6]}][{lista[7]}][{lista[8]}][{lista[9]}]
[{lista_2[0]}][{lista_2[1]}][{lista_2[2]}][{lista_2[3]}][{lista_2[4]}][{lista_2[5]}][{lista_2[6]}][{lista_2[7]}][{lista_2[8]}][{lista_2[9]}]

Aciertos: {aciertos}
Errores: {errores}""")   
#mostrar_tablero(aciertos, errores, lista, lista_2)

def ingresar_palabra():
    """
    Esta funcion pide al usuario que ingrese una palabra y la devuelve en minuscula.
    """
    ingreso_usuario = input("Ingresa palabra: ").lower()
    while not ingreso_usuario.isalpha():
        print("Ingrese solo letras.")
        ingreso_usuario = input("Ingrese palabra: ").lower()
    return ingreso_usuario

def evaluar_palabra(palabra_ingresada, clave):
    """
    Esta funcion evalua si la palabra ingresada es igual a la palabra que se debe adivinar.
    """
    return "a" if palabra_ingresada == clave else "e"

def jugar_turno(aciertos, errores, posicion, lista, lista_2, clave, definicion):
    """
    Esta funcion muestra el tablero, la letra a jugar, la longitud de la palabra a adivinar
    y la definicion de la palabra.
    Luego pide al usuario que ingrese una palabra y la evalua.
    """
    letra = clave[0]
    longitud = len(clave)

    mostrar_tablero(aciertos, errores, posicion, lista, lista_2)
    print(f"Turno letra: {letra} Longitud palabra: {longitud}\nDefinicion: {definicion}")

    palabra_ingresada = ingresar_palabra()
    resultado = evaluar_palabra(palabra_ingresada, clave)
    lista_2[posicion] = resultado

    if resultado == "a":
        aciertos += 1
    else:
        errores += 1
    return aciertos, errores, palabra_ingresada

def mostrar_resumen(diccionario, lista_palabras_ingresadas, lista_2):
    """
    Esta funcion muestra el resumen de la partida.
    """
    print("\n--- Resumen de la Partida ---")
    print("-" * 50)
    for i, clave in enumerate(diccionario.keys()):
        letra = clave[0]
        long = len(clave)
        correccion = clave
        palabra_jugador = lista_palabras_ingresadas[i]
        result = "acierto" if lista_2[i] == "a" else "error"
        if result == "error":
            print(f"Turno de la letra: {letra} - Palabra de {long} letras - {palabra_jugador} - {result} - Palabra correcta es : {correccion}")
        else:
            print(f"Turno de la letra: {letra} - Palabra de {long} letras - {palabra_jugador} - {result}")
    print("-" * 50)

def calcular_puntaje(aciertos):
    """
    Esta funcion calcula el puntaje de la partida.
    """
    return aciertos * 10

def pasapalabra():
    """
    Esta funcion integra todas las funciones anteriores.
    """
    diccionario_rosco = cargar_datos_para_rosco()
    lista = cargar_letras()
    lista_palabras_ingresadas = []
    lista_2 = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
    aciertos = 0
    errores = 0
    for clave in datos_rosco(cargar_datos_para_rosco, cargar_letras, cargar_palabras):
        for posicion in range(len(lista)):
            palabra, definicion = cargar_palabras(diccionario_rosco, lista)
            aciertos, errores, palabra_ingresada = jugar_turno(aciertos, errores, posicion, lista, lista_2, clave, definicion)
            lista_palabras_ingresadas.append(palabra_ingresada)
    mostrar_resumen(diccionario_rosco, lista_palabras_ingresadas, lista_2)
    puntaje = calcular_puntaje(aciertos)
    print(f"Puntaje: {puntaje}")

pasapalabra()