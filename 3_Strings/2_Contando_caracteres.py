"""
Completar el cuerpo de la función. La misma recibe una cadena de caracteres y dos caracteres individuales. Debe 
retornar la suma de la cantidad de veces que aparecen cada uno de los caracteres en la cadena.

Hint: No utilizar la función .count() de las cadenas. Cada vez que la invocamos, Python realiza un recorrido 
por la cadena buscando la subcadena que la función recibe como parámetro. Resolver el ejercicio realizando una 
única iteración en toda la cadena.

Ejemplo:

    contar_caracteres("casa", "c", "a") => 3
    contar_caracteres("cosa", "c", "a") => 2
    contar_caracteres("algoritmos", "a", "o") => 3
    contar_caracteres("algoritmos", "w", "x") => 0
"""

def contar_caracteres(cadena, caracter1, caracter2):
    contador = 0
    for caracter in cadena:
        if caracter == caracter1 or caracter == caracter2:
            contador += 1
    return contador

print(contar_caracteres("casa", "c", "a"))
print(contar_caracteres("cosa", "c", "a"))
print(contar_caracteres("algoritmos", "a", "o"))
print(contar_caracteres("algoritmos", "w", "x"))