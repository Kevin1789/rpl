"""
Escribir un programa que solicite el ingreso de un número y que luego calcule e imprima su factorial.

    >>> Ingrese un numero: 5
    120
"""

num = int(input("Ingrese un número: "))
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print(factorial)
