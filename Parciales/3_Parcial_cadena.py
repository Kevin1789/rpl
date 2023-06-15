"""
Escribir una funcion validadr que resiba una cadean de caracteres y devuelve Treu si una clave contiene las restrinciones requeridas, False de lo contrario.
requerida, False de lo contrario. incluir en la funcion las pruebas indicadas debajo.
Debe contener entre 6 y 12 caracteres
Debe contener por lo menos dos caracter alfabetico en mayuscula (sin acentuar)
Debe contener por lo menos dos caracter alfabetico en minuscula (sin acentuar)
Puede contener a lo sumo dos digitos numericos
Puede contener alguno de los siguientes simbolos: [*,-,$,@]
Cualquier otro simbolo que no este en el grupo indicado rechazara la validacion

Ejemplos:
validar("Algoritmo $1") ---> False
validar("AprObé-con-7") ---> False
validar("AlgOritmo$1") ---> True
validar("AproBe-con-7") ---> True
"""

def validar(clave):
    # Verificar la longitud de la clave
    if len(clave) < 6 or len(clave) > 12:
        return False

    # Contadores de caracteres, dígitos y símbolos
    mayusculas = 0
    minusculas = 0
    digitos = 0
    simbolos = 0
    otros = 0

    # Verificar cada carácter de la clave
    for caracter in clave:
        if caracter.isalpha():
            if caracter.isupper():
                mayusculas += 1
            else:
                minusculas += 1
        elif caracter.isdigit():
            digitos += 1
        elif caracter in ['*', '-', '$', '@']:
            simbolos += 1
        else:
            otros += 1

    # Verificar las restricciones de caracteres
    if mayusculas < 2 or minusculas < 2 or digitos > 2 or simbolos == 0 or otros > 0:
        return False

    return True

# Pruebas
print(validar("Algoritmo $1"))  # False
print(validar("AprObé-con-7"))  # False
print(validar("AlgOritmo$1"))  # True
print(validar("AproBe-con-7"))  # True
