"""
Escribir una funcion CONTADOR que reciba una cadena de caracteres y devuelve un entero que indica
la cantidad de caracteres alfanumerico distintos que tiene la cadena. No debe distinguir mayusculas de 
minusculas ni caracter con tilde.
Ejemplos:

contar("Aaaáb") devuelve 2
contar("$_123*") devuelve 0
contar("Algoritmos y Programación") devuelve 13
"""


def contador(cadena):
    cadena = cadena.lower().replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú', 'u')
    caracteres = set()
    for caracter in cadena:
        if caracter.isalpha():
            caracteres.add(caracter)
    return len(caracteres)


print(contador("Aaaáb"))
print(contador("$_123*"))
print(contador("Algoritmos y Programación"))
print("Fin de este modelo")

"-----------------------------------------------------------------------------------------------------------------"

def contador2(cadena):
    cadena = cadena.lower().replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú', 'u')
    caracteres = []
    for caracter in cadena:
        if caracter.isalpha() and caracter not in caracteres:
            caracteres.append(caracter)
    return len(caracteres)

print(contador2("Aaaáb"))
print(contador2("$_123*"))
print(contador2("Algoritmos y Programación"))
print("Fin de este modelo 2")

"-----------------------------------------------------------------------------------------------------------------"

def contador3(cadena):
    cadena = cadena.lower()
    cadena = cadena.replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú', 'u')
    caracteres_distintos = set()
    for c in cadena:
        if c.isalpha():
            caracteres_distintos.add(c)
    return len(caracteres_distintos)


print(contador3("Aaaáb"))
print(contador3("$_123*"))
print(contador3("Algoritmos y Programación"))
print("Fin de este modelo 3")

"-----------------------------------------------------------------------------------------------------------------"

def contador4(cadena):
    cadena = cadena.lower()
    caracteres = set()
    for c in cadena:
        if c.isalpha() and c not in ("á", "é", "í", "ó", "ú"):
            caracteres.add(c)
    return len(caracteres)

print(contador4("Aaaáb"))
print(contador4("$_123*"))
print(contador4("Algoritmos y Programación"))
print("Fin de este modelo 4")

"-----------------------------------------------------------------------------------------------------------------"

def contador5(cadena):
    cadena = cadena.lower()
    contador = 0
    caracteres = ''
    for c in cadena:
        if c.isalpha() and c not in 'áéíóú' and c not in caracteres:
            contador += 1
            caracteres += c
    return contador


print(contador5("Aaaáb"))
print(contador5("$_123*"))
print(contador5("Algoritmos y Programación"))
print("Fin de este modelo 5")

"-----------------------------------------------------------------------------------------------------------------"
def con_tilde(cadena):
    tildes = "áéíóúÁÉÍÓÚ"
    sin_tildes = "aeiouAEIOU"
    for i in range(len(tildes)):
        cadena = cadena.replace(tildes[i], sin_tildes[i])
    return cadena

def contador6(cadena):
    cadena = con_tilde(cadena.lower())
    letras = []
    contador = 0
    numeros = "0123456789"
    simbolos = "$-*"
    for caracter in cadena:
        if caracter not in letras and caracter not in numeros and caracter not in simbolos:
            letras.append(caracter)
            contador += 1
    return contador

print(contador6("Aaaáb"))
print(contador6("$_123*"))
print(contador6("Algoritmos y Programación"))
print("Fin de este modelo 6")