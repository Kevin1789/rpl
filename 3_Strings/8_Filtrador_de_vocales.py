"""
Completar el cuerpo de la función. La misma recibe una cadena y debe retornar la misma habiendo filtrado todas las 
vocales que contenía.

Ejemplos:

    filtrador_de_vocales("hola") => "hl"
    filtrador_de_vocales("facultad") => "fcltd"
    filtrador_de_vocales("algoritmos") => "lgrtms"   
"""

def filtrador_de_vocales(cadena):
    resultado = ""
    for i in range(len(cadena)):
        if cadena[i] not in "aeiouAEIOU":
            resultado += cadena[i]
    return resultado

print(filtrador_de_vocales("hola"))
print(filtrador_de_vocales("facultad"))
print(filtrador_de_vocales("algoritmos"))
