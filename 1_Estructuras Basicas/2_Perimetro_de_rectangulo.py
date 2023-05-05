"""
Escribir un programa que solicite a un usuario la base y la altura de un rectángulo e imprima por pantalla 
cuál es el perímetro del mismo.

Ejemplo:

    >>> Ingrese la base del rectangulo: 5
    >>> Ingrese la altura del rectangulo: 20
    El perimetro del rectangulo es: 50
"""

altura = int (input ('Ingrese la base del rectangulo: '))
base = int (input ('Ingrese la altura del rectangulo: '))
area=altura*base
perimetro=altura+base+altura+base
print( "El perimetro del rectangulo es:" , perimetro)