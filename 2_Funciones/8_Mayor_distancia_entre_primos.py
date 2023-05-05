"""
Completar el cuerpo de la función. La misma recibe como parámetro dos números que serán tomados como límite 
inferior y límite superior del cálculo que debemos realizar.
La función debe retornar la mayor distancia entre dos números primos existentes entre dichos límites, 
incluyéndolos.
Recordar que el 1 no es primo y el 2 sí lo es. Se puede asumir que los parámetros de entrada han sido 
validados previamente.
Si en el rango existiera un solo número primo hay que devolver 0.
Si en el rango no hay ningún número primo hay que devolver -1.

Ejemplos:

mayor_distancia_entre_primos(1, 3) => 1 (distancia entre 2 y 3)
mayor_distancia_entre_primos(1, 5) => 2 (distancia entre 3 y 5)
mayor_distancia_entre_primos(1, 15) => 4 (distancia entre 7 y 11)
mayor_distancia_entre_primos(14, 18) => 0 (hay un solo número primo)
mayor_distancia_entre_primos(14, 16) => -1 (no hay números primos)
Ayuda: Pueden utilizar la función es_primo(numero) definida en actividades anteriores de la categoría, 
logrando un mayor grado de modularización.
"""

def mayor_distancia_entre_primos(lim_inferior, lim_superior):
    # Definimos una función para verificar si un número es primo
    def es_primo(numero):
        if numero <= 1:
            return False  
        elif numero == 2:
            return True
        elif numero % 2 == 0:
            return False
        else:
            for elemento in range(3, int(numero**0.5) + 1, 2):
                if numero % elemento == 0:
                    return False
            return True

    # Buscamos los números primos en el rango dado
    primos = [num for num in range(lim_inferior, lim_superior + 1) if es_primo(num)]

    # Si no hay números primos, devolvemos -1
    if len(primos) == 0:
        return -1
    # Si solo hay un número primo, devolvemos 0
    elif len(primos) == 1:
        return 0
    # Si hay más de un número primo, buscamos la mayor distancia entre ellos
    else:
        max_distancia = 0
        for elemento in range(len(primos) - 1):
            distancia = primos[elemento+1] - primos[elemento]
            if distancia > max_distancia:
                max_distancia = distancia
        return max_distancia
    
print(mayor_distancia_entre_primos(1, 3))
print(mayor_distancia_entre_primos(1, 5))
print(mayor_distancia_entre_primos(1, 15))
print(mayor_distancia_entre_primos(14, 18))
print(mayor_distancia_entre_primos(14, 16))