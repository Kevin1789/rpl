"""
Completar el cuerpo de la función. La misma debe devolver True en caso de que el número recibido sea una 
potencia de dos, y False en caso contrario.

Ejemplos:

es_potencia_de_dos(1) => True
es_potencia_de_dos(2) => True
es_potencia_de_dos(3) => False
es_potencia_de_dos(4) => True
es_potencia_de_dos(15) => False
es_potencia_de_dos(16) => True
es_potencia_de_dos(30) => False
es_potencia_de_dos(32) => True
"""

def es_potencia_de_dos(numero):
    potencia = 1
    while potencia < numero:
        potencia *= 2
    return potencia == numero

print(es_potencia_de_dos(1))
print(es_potencia_de_dos(2))
print(es_potencia_de_dos(3))
print(es_potencia_de_dos(4))
print(es_potencia_de_dos(15))
print(es_potencia_de_dos(16))
print(es_potencia_de_dos(30))
print(es_potencia_de_dos(32))
