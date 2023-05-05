"""
Completar el cuerpo de la función. La misma debe devolver True en caso de que el número que se recibe como 
parámetro sea primo, y False en caso contrario.

Ejemplos:

es_primo(3) => True
es_primo(4) => False
es_primo(11) => True
es_primo(15) => False
"""

def es_primo(numero):
    if numero == 1:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

print(es_primo(3))
print(es_primo(4))
print(es_primo(11))
print(es_primo(15))
