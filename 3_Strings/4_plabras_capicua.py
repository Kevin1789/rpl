"""
Completar el cuerpo de la función. La misma debe retornar un valor booleano: True en caso de que las palabra 
que se recibe sea capicúa, False en caso contrario.

Intentar resolver el ejercicio en una línea.

Ejemplos:

    es_capicua("neuquen") => True
    es_capicua("mendoza") => False
    es_capicua("menem") => True
    es_capicua("alfonsin") => False
"""

def es_capicua(palabra):
    return palabra == palabra[::-1]

print(es_capicua("neuquen"))
print(es_capicua("mendoza"))
print(es_capicua("menem"))
print(es_capicua("alfonsin"))