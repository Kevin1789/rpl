"""
Completar los cuerpos de las distintas funciones. A continuación se encuentran los requerimientos que deben cumplir 
cada una de las funciones. Las funciones deben ser resueltas realizando iteraciones sobre las listas, no se pueden 
usar funciones de ordenamiento.

filtrar_pares: Recibe una lista con variables numéricas enteras. Retorna una nueva lista con todos los números pares 
que estaban en la lista que se recibió como parámetro. Los elementos de la lista devuelta deben estar en el orden 
original.

Ejemplo:

    filtrar_pares([5,6,13,7,11,9,10,11]) => [6,10]

filtrar_primos: Recibe una lista con variables numéricas enteras. Retorna una nueva lista con todos los números primos 
que estaban en la lista que se recibió como parámetro Los elementos de la lista devuelta deben estar en el orden 
original.

Hint: Utilizar la función programada en otra actividad que determina si un número es primo o no.

Ejemplo:

    filtrar_primos([5,6,13,7,11,9,10,11]) => [5,13,7,11,11]
sumar_elementos: Recibe una lista con variables numéricas. Retorna la suma de todos sus elementos.
No se puede utilizar la función sum(), ya existente en Python.

Ejemplo:

    sumar_elementos([5,6,13,7,11,9,10,11]) => 72
esta_ordenada: Recibe una lista con variables numericas. Retorna True en caso de que la lista este ordenada 
ascendentemente (es decir, los mas chicos en las primeras posiciones), False en caso contrario.

Ejemplos:

    esta_ordenada([5,6,13,7,11,9,10,11]) => False
    esta_ordenada([5,6,7,11]) => True
producto_escalar: Recibe dos listas de variables numéricas con la misma longitud. Interpretarlas como vectores. 
Retorna el producto escalar entre ambos vectores.

Ejemplos:

    producto_escalar([2,5,3], [4,6,7]) => 59
letras_en_palabras: Recibe una lista de letras y una cadena. La lista contiene en cada índice de la misma una 
letra (string de longitud 1). Retorna True en caso de que todas las letras se encuentren en la palabra, False en caso 
contrario.

Ejemplos:

    letras_en_palabras(["a","h","e"], "hola como estas") => True
    letras_en_palabras(["a","h","e"], "ola como estas") => False 
"""

def filtrar_pares(lista):
    lista_pares = []
    for i in range(len(lista)):
        if lista[i] % 2 == 0:
            lista_pares.append(lista[i])
    return lista_pares

print(filtrar_pares([5,6,13,7,11,9,10,11]))

def filtrar_primos(lista):
    lista_primos = []
    for i in range(len(lista)):
        if es_primo(lista[i]):
            lista_primos.append(lista[i])
    return lista_primos

def es_primo(numero):
    if numero == 1:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

print(filtrar_primos([5,6,13,7,11,9,10,11]))

def sumar_elementos(lista):
    suma = 0
    for i in range(len(lista)):
        suma += lista[i]
    return suma

print(sumar_elementos([5,6,13,7,11,9,10,11]))

def esta_ordenada(lista):
    for i in range(len(lista)-1):
        if lista[i] > lista[i+1]:
            return False
    return True

print(esta_ordenada([5,6,13,7,11,9,10,11]))
print(esta_ordenada([5,6,7,11]))

def producto_escalar(vector_1, vector_2):
    producto = 0
    for i in range(len(vector_1)):
        producto += vector_1[i] * vector_2[i]
    return producto

print(producto_escalar([2,5,3], [4,6,7]))

def letras_en_palabras(letras, frase):
    for i in range(len(letras)):
        if letras[i] not in frase:
            return False
    return True

print(letras_en_palabras(["a","h","e"], "hola como estas"))
print(letras_en_palabras(["a","h","e"], "ola como estas"))
