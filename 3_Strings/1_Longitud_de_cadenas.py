"""
Completar el cuerpo de la función. La misma recibe tres cadenas previamente inicializadas y debe 
retornar la suma de la longitud de la concatenación de las tres cadenas.

Ejemplo:

    longitud_cadenas("hola", "como", "estas") => 13
    longitud_cadenas("a", "b", "c") => 3
"""

def longitud_cadenas(cadena1, cadena2, cadena3):
    return len(cadena1 + cadena2 + cadena3)

print(longitud_cadenas("hola", "como", "estas"))
print(longitud_cadenas("a", "b", "c"))