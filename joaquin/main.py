import diccionario_etapa1
from Parte_1 import jugar_turno, mostrar_resumen, calcular_puntaje


"""
Esta seria la funcion Main, la que coordina todo el juego. Esta funcion comienza inicializando las variables: puntaje_total, aciertos, errores, lista2, pocision,
lista_palabras_ingresadas. Utiliza un bucle for para para recorrer cada palabra y definición en el diccionario importado. 
Dentro del bucle, llama a la función jugar_turno() para que el usuario juegue su turno. También registra la palabra ingresada por el usuario 
en la lista lista_palabras_ingresadas. Después de completar todos los turnos, llama a la función mostrar_resumen() para mostrar un resumen de la partida. 
Por ultimo llama a la función calcular_puntaje() para que imprima el puntaje total.
"""
def pasapalabra():
    puntaje_total = 0
    aciertos = 0
    errores = 0
    lista_2 = [" ", " ", " "]
    posicion = 0
    lista_palabras_ingresadas = []

    for clave, valor in diccionario_etapa1.dicc.items():
        palabra = clave
        definicion = valor
        lista = [" ", " ", " "]

        for letra_1, clave_1 in enumerate(diccionario_etapa1.dicc.keys()):
            lista[letra_1] = clave_1[0]

        aciertos, errores, palabra_ingresada = jugar_turno(aciertos, errores, posicion, lista, lista_2, clave, definicion)
        lista_palabras_ingresadas.append(palabra_ingresada)

        posicion += 1

    mostrar_resumen(diccionario_etapa1.dicc, lista_palabras_ingresadas, lista_2)

    puntaje_total = calcular_puntaje(aciertos)
    print(f"\nPuntaje total: {puntaje_total}")

pasapalabra()



#Autor: Osorio Joaquin Emmanuel