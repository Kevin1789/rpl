"""
Escribir un programa que solicite al usuario la base y la altura de un triángulo e imprima por pantalla 
cuál es el área del triángulo.

Ejemplo:

    >>> Ingrese la base del triangulo: 5
    >>> Ingrese la altura del triangulo: 20
    El area del triangulo es: 50.0
Recordar que para que el ejercicio sea calificado como correcto, los mensajes que se muestran al usuario 
tanto para solicitarle el ingreso de datos como para mostrarle el resultado deben ser los mismos que los del ejemplo.
"""


base = float(input("Ingrese la base del triangulo: "))
altura = float(input("Ingrese la altura del triangulo: "))
area = base * altura / 2
print("El area del triangulo es:", area)