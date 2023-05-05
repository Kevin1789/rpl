"""
La idea de esta sección es completar las distintas funciones de acuerdo a los requerimientos especificados para 
cada una de ellas, tal como se hizo para el resto del módulo de listas.

filtrar_primos: Recibe una lista de números enteros y un número adicional. Retorna una nueva lista filtrada, 
que contiene aquellos números que sean primos y además sean mayores al segundo número que se recibió como parámetro.

HINT: Pueden utilizar la función es_primo(), correspondiente al módulo de funciones.

Ejemplos:

    filtrar_primos([3, 7, 11, 13], 8) => [11, 13]
    filtrar_primos([11, 7, 3, 19], 15) => [19]
ordenar_por_longitud_de_tuplas: Recibe una lista de tuplas. Retorna una nueva lista ordenada de mayor a 
menor por la longitud de las mismas. Aclaración: No importa el tipo de los elementos que se encuentran 
contenidos en las tuplas.

Ejemplo:

    lista_tuplas = [(1,5,6), (1,2), (1,), (6,4,5,6), ("asd", 9, 5.6, "l", "s")]
    ordenar_por_longitud_de_tuplas(lista_tuplas) => [("asd", 9, 5.6, "l", "s"), (6,4,5,6), (1,5,6), (1,2), (1,)]
concatenar_primeros_elementos: Recibe una lista de lista de listas. Se puede asumir que cada una de las 
listas internas tiene una longitud mayor a 3. Retorna una única lista, que resulta de la concatenación 
de los primeros 3 elementos de cada una de las listas internas, en el orden original.

Ejemplo:

    lista = [[1,4,5,6], [2,3,4,5], [6,4,4,6,7,8], [5,6,7,3,5,6,4]]
    concatenar_primeros_elementos(lista) => [1,4,5,2,3,4,6,4,4,5,6,7]
"""

def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

def filtrar_primos(lista, numero):
    return [n for n in lista if n > numero and es_primo(n)]

def ordenar_por_longitud_de_tuplas(lista_tuplas):
    return sorted(lista_tuplas, key=lambda tupla: len(tupla), reverse=True)

def concatenar_primeros_elementos(lista_listas):
    result = []
    for lista in lista_listas:
        result.extend(lista[:3])
    return result

print(filtrar_primos([3, 7, 11, 13], 8))
print(filtrar_primos([11, 7, 3, 19], 15))
print(ordenar_por_longitud_de_tuplas([(1,5,6), (1,2), (1,), (6,4,5,6), ("asd", 9, 5.6, "l", "s")]))
print(concatenar_primeros_elementos([[1,4,5,6], [2,3,4,5], [6,4,4,6,7,8], [5,6,7,3,5,6,4]]))