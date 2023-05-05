"""
Escribir una funcion validar que reciba una cadena de caracteres y devuelva True si una clave
contiene las restricciones requeridas, False de lo contrario.
- Debe contener entre 8 y 12 caracteres
- Debe contener por lo menos un caracter alfabetico en mayuscula (sin acentuar)
- Debe contener por lo menos un caracter alfabetico en minuscula (sin acentuar)
- Debe contener por lo menos alguno de los siguientes simbolos: [*,-,$,@]
Cualquier otro simbolo que no este en el grupo indicado rechazara la validacion

Ejemplos:
validar("Algoritmo $1") ---> False
validar("Aprobé-con-7") ---> False
validar("Algoritmo$1") ---> True
validar("Aprobe-con-7") ---> True
"""

def validar(cadena):
    valido=False
    tiene_simbolo=False
    letras_invalidas="áéíóúÁÉÍÓÚ"
    simbolos_validos="*-$@"
    contador=0
    for caracter in cadena:
        if caracter in simbolos_validos:
            tiene_simbolo=True
    if 8<=len(cadena)<=12 and tiene_simbolo:
        valido=True
        while contador<(len(cadena)) and valido:
            if cadena[contador] in letras_invalidas:
                valido=False
            elif not(cadena[contador].isupper()) and not(cadena[contador].islower()) and not (cadena[contador].isnumeric()) and not(cadena[contador] in simbolos_validos):
                valido=False
            contador+=1
    return (valido)

print(validar("Algoritmo $1"))
print(validar("Aprobé-con-7"))
print(validar("Algoritmo$1"))
print(validar("Aprobe-con-7"))
print("Fin de este modelo")

"-----------------------------------------------------------------------------------------------------------------"

def validar2(clave):
    if len(clave) < 8 or len(clave) > 12:
        return False
    acentos = ["á", "é", "í", "ó", "ú", "Á", "É", "Í", "Ó", "Ú"]
    for c in clave:
        if c in acentos:
            return False
    tiene_mayuscula = False
    tiene_minuscula = False
    for c in clave:
        if c.isupper():
            tiene_mayuscula = True
        elif c.islower():
            tiene_minuscula = True
    if not tiene_mayuscula or not tiene_minuscula:
        return False
    simbolos_permitidos = {"*", "-", "$", "@"}
    for c in clave:
        if c not in simbolos_permitidos and not c.isalpha() and not c.isdigit():
            return False
    
    return True

print(validar2("Algoritmo $1"))
print(validar2("Aprobé-con-7"))
print(validar2("Algoritmo$1"))
print(validar2("Aprobe-con-7"))
print("Fin de este modelo 2")

"-----------------------------------------------------------------------------------------------------------------"

def validar3(cadena):
    letras_invalidas = "áéíóúÁÉÍÓÚ"
    simbolos_validos = "*-$@"
    
    if len(cadena) < 8 or len(cadena) > 12:
        return False
    
    tiene_simbolo = any(c in simbolos_validos for c in cadena)
    print
    if not tiene_simbolo:
        return False
    
    for caracter in cadena:
        if caracter in letras_invalidas:
            return False
        elif not caracter.isalpha() and not caracter.isnumeric() and caracter not in simbolos_validos:
            return False
    
    return True

print(validar3("Algoritmo $1"))
print(validar3("Aprobé-con-7"))
print(validar3("Algoritmo$1"))
print(validar3("Aprobe-con-7"))
print("Fin de este modelo 3")

"-----------------------------------------------------------------------------------------------------------------"

def validar4(cadena):
    valido = False
    if 8<=len(cadena)<=12:
    #if len(cadena) >= 8 and len(cadena) <= 12:
        valido = True
    for caracter in cadena:
            if not caracter.isalpha() and not caracter.isnumeric() and caracter not in "*-$@":
                valido = False
            elif caracter in "áéíóú":
                valido = False
    return valido
    
print(validar4("Algoritmo $1"))
print(validar4("Aprobé-con-7"))
print(validar4("Algoritmo$1"))
print(validar4("Aprobe-con-7"))
print("Fin de este modelo 4")

"-----------------------------------------------------------------------------------------------------------------"