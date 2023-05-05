"""
Completar el cuerpo de la función. La misma debe devolver True en caso en el que el número recibido como 
parámetro recibido sea par, y False en caso contrario.

Ejemplos:

es_par(2) => True
es_par(3) => False
es_par(32) => True
es_par(33) => False
"""

def es_par(numero):
    return numero % 2 == 0

print(es_par(2))
print(es_par(3))
print(es_par(32))
print(es_par(33))
