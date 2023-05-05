"""
Escribir un programa que solicite al usuario el ingreso de un número e imprima por pantalla si el número 
ingresado es positivo, negativo o cero.

Ejemplo:

    >>> Ingrese un numero: 5
    Es positivo
    >>> Ingrese un numero: -4
    Es negativo
    >>> Ingrese un numero: 0
    Es igual a 0
"""

num = int(input("Ingrese un número: ")) 
if num > 0:
    print("Es positivo")
elif num < 0:
    print("Es negativo")
else:
    print("Es igual a 0")

