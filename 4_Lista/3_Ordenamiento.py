"""
Para este apartado, se propone la utilización de las funciones de sorting brindadas por Python para realizar 
ordenamientos sobre listas.

ordenar_lista_menor_a_mayor: Recibe una lista que contiene únicamente números. Retorna la lista ordenada de 
menor a mayor.

Ejemplo:

ordenar_lista_menor_a_mayor([5,2,6,23,4]) => [2,4,5,6,23]
ordenar_lista_mayor_a_menor: Recibe una lista que contiene únicamente números. Retorna la lista ordenada de 
mayor a menor.

Ejemplo:

ordenar_lista_menor_a_mayor([5,2,6,23,4]) => [23,6,5,4,2]
ordenar_lista_alfabeticamente: Recibe una lista que contiene únicamente strings.
Retorna la lista ordenada alfabeticamente.

Ejemplo:

ordenar_lista_alfabeticamente(["hola", "estas", "como", "si"]) => ["como", "estas", "hola", "si"]
ordenar_palabras_por_longitud: Recibe una lista que contiene únicamente strings. Retorna la lista ordenada en 
forma descendente (los mas grandes
en las primeras posiciones) según la longitud de cada string.

Ejemplo:

ordenar_palabras_por_longitud(["a", "hola", "si", "string largo", "string"]) => ["string largo", "string", 
"hola", "si", "a"]
ordenar_lista_por_tupla: Recibe una lista de tuplas de longitud 2, cuyos índices contienen únicamente 
variables numéricas. Retorna una lista ordenada de mayor a menor teniendo en cuenta únicamente el valor del 
segundo elemento de la tupla.

Ejemplo:

ordenar_lista_por_tupla([(1,2), (2,3), (6,7), (5,4), (7,1)] => [(6,7), (5,4), (2,3), (1,2), (7,1)])
ordenar_lista_por_suma_tupla: Recibe una lista de tuplas de longitud 2, cuyos índices contienen únicamente 
variables numéricas. Retorna la lista ordenada de mayor a menor según la suma de ambos elementos de la tupla.

Ejemplo:

ordenar_lista_por_suma_tupla([(1, 5), (7, 3), (5, 4), (4, 3)]) => [(7,3),(5,4),(4,3),(1,5)] 
"""

def ordenar_lista_menor_a_mayor(lista):
    return sorted(lista)

def ordenar_lista_mayor_a_menor(lista):
    return sorted(lista, reverse=True)

def ordenar_lista_alfabeticamente(lista):
    return sorted(lista)

def ordenar_palabras_por_longitud(lista):
    return sorted(lista, key=len, reverse=True)

def ordenar_lista_por_tupla(lista):
    return sorted(lista, key=lambda x: x[1], reverse=True)

def ordenar_lista_por_suma_tupla(lista):
    return sorted(lista, key=lambda x: sum(x), reverse=True)

print(ordenar_lista_menor_a_mayor([5,2,6,23,4]))
print(ordenar_lista_mayor_a_menor([5,2,6,23,4]))
print(ordenar_lista_alfabeticamente(["hola", "estas", "como", "si"]))
print(ordenar_palabras_por_longitud(["a", "hola", "si", "string largo", "string"]))
print(ordenar_lista_por_tupla([(1,2), (2,3), (6,7), (5,4), (7,1)]))
print(ordenar_lista_por_suma_tupla([(1, 5), (7, 3), (5, 4), (4, 3)]))
