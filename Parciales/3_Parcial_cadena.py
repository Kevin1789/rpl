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

def validar (cadena):
    valido = False
    if 6>=len(cadena)<=12:
        valido = True
    for letra in cadena:
            if not letra.isupper()<=2  and not letra.islower()<=2 and not letra.isdigit()>=2 and letra not in "*-$@":
                valido=False
            elif letra in "áéíóúÁÉÍÓÚ":
                valido=False
    return (valido)
print(validar("Algoritmo $1"))
print(validar("Aprobé-con-7"))
print(validar("AlgOritmo$1"))
print(validar("AproBe-con-7"))

"-----------------------------------------------------------------------------------------------------------------"

def validar(clave):
    # Debe contener entre 6 y 12 caracteres
    if not 6 <= len(clave) <= 12:
        return False

    # Debe contener por lo menos dos caracteres alfabéticos en mayúscula
    if sum(1 for c in clave if c.isupper()) < 2:
        return False

    # Debe contener por lo menos dos caracteres alfabéticos en minúscula
    if sum(1 for c in clave if c.islower()) < 2:
        return False

    # Puede contener a lo sumo dos dígitos numéricos
    if sum(1 for c in clave if c.isdigit()) > 2:
        return False

    # Puede contener alguno de los siguientes símbolos: [*,-,$,@]
    if not all(c.isalnum() or c in ['*', '-', '$', '@'] for c in clave):
        return False

    # Cualquier otro símbolo que no esté en el grupo indicado rechazará la validación
    if not all(c.isalnum() or c in ['*', '-', '$', '@'] for c in clave):
        return False

    return True

