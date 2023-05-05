"""
Escribir un programa que solicite al usuario que ingrese su edad y que imprima por pantalla si el usuario es 
mayor de edad o no.

Ejemplos:

    >>> Ingrese edad: 18
    Es mayor de edad
    >>> Ingrese edad: 17
    Es menor de edad
"""

edad = int (input ('Ingrese edad: '))
if edad >= 18:
    print ("Es mayor de edad")
else:
    print("Es menor de edad")