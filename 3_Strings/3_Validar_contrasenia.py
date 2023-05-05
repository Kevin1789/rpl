"""
Completar el cuerpo de la función. La misma debe retornar un valor booleano: True en caso de que la contraseña sea válida, False en caso contrario.
Se considera válida una contraseña si:

Tiene al menos un número.
Tiene al menos una mayúscula.
Tiene al menos una minúscula.
Tiene al menos un carácter no alfanumérico
(Hint: Se puede evaluar utilizando la conjunción de la negación entre .isalpha() y
la negación de .isnumeric())
Tiene una longitud mayor a 7 caracteres pero menor a 15.
Ejemplo:

   validar_contraseña("!Algoritmos123") => True
   validar_contraseña("!Algoritmos123!Algoritmos123") => False
   validar_contraseña("algoritmos") => False
   validar_contraseña("algoritmos123") => False
   validar_contraseña("Algoritmos123") => False
   validar_contraseña("!Alg123") => False
   validar_contraseña("!ALGORITMOS123") => False
"""

def validar_contraseña(contraseña):
    tiene_numero = False
    tiene_mayuscula = False
    tiene_minuscula = False
    tiene_caracter_especial = False
    if len(contraseña) < 8 or len(contraseña) > 14:
        return False
    for caracter in contraseña:
        if caracter.isnumeric():
            tiene_numero = True
        elif caracter.isupper():
            tiene_mayuscula = True
        elif caracter.islower():
            tiene_minuscula = True
        else:
            tiene_caracter_especial = True
    return tiene_numero and tiene_mayuscula and tiene_minuscula and tiene_caracter_especial

print(validar_contraseña("!Algoritmos123"))
print(validar_contraseña("!Algoritmos123!Algoritmos123"))
print(validar_contraseña("algoritmos"))
print(validar_contraseña("algoritmos123"))
print(validar_contraseña("Algoritmos123"))
print(validar_contraseña("!Alg123"))
print(validar_contraseña("!ALGORITMOS123"))

"---------------------------------------------------------------------------------------------------------------"

def validar_contraseña2(contraseña):
    return (len(contraseña) >= 8 and len(contraseña) <= 14 and 
            any(caracter.isnumeric() for caracter in contraseña) and
            any(caracter.isupper() for caracter in contraseña) and
            any(caracter.islower() for caracter in contraseña) and
            any(not caracter.isalnum() for caracter in contraseña))
"---------------------------------------------------------------------------------------------------------------"

def validar_contraseña3(contraseña):
    return all([
        len(contraseña) >= 8,
        len(contraseña) <= 14,
        any(char.isdigit() for char in contraseña),
        any(char.isupper() for char in contraseña),
        any(char.islower() for char in contraseña),
        not all(char.isalnum() for char in contraseña)
    ])
"---------------------------------------------------------------------------------------------------------------"

def validar_contraseña4(contraseña):
    numeros = "0123456789"
    mayusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    minusculas = "abcdefghijklmnopqrstuvwxyz"
    caracteres_especiales = "!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
    
    if len(contraseña) < 8 or len(contraseña) > 14:
        return False
    
    tiene_numero = False
    for i in range(len(contraseña)):
        if contraseña[i] in numeros:
            tiene_numero = True
    
    tiene_mayuscula = False
    for i in range(len(contraseña)):
        if contraseña[i] in mayusculas:
            tiene_mayuscula = True
    
    tiene_minuscula = False
    for i in range(len(contraseña)):
        if contraseña[i] in minusculas:
            tiene_minuscula = True
    
    tiene_caracter_especial = False
    for i in range(len(contraseña)):
        if contraseña[i] in caracteres_especiales:
            tiene_caracter_especial = True
    
    return tiene_numero and tiene_mayuscula and tiene_minuscula and tiene_caracter_especial

"---------------------------------------------------------------------------------------------------------------"

def validar_contrasenia5(contrasenia):
    if not any(c.isdigit() for c in contrasenia):
        return False
    if not any(c.isupper() for c in contrasenia):
        return False
    if not any(c.islower() for c in contrasenia):
        return False
    if not any(not c.isalnum() for c in contrasenia):
        return False
    if len(contrasenia) <= 7 or len(contrasenia) >= 15:
        return False
    return True