"""
Completar el cuerpo de la función. La misma recibe un texto y debe retornar cuál es la palabra más larga del mismo. 
Se puede asumir que todas las palabras están separadas por espacios y no hay caracteres especiales.

No se pueden utilizar funciones de otras estructuras de datos. El ejercicio se debe resolver iterando la cadena, 
llevando el registro de las variables que se consideren adecuadas.

Ayuda: Tener cuidado con el caso en el que la palabra más larga es la última de todo el texto.

Ejemplos:

    palabra_mas_larga("Hola como estas este es un texto de prueba") => "prueba"
    palabra_mas_larga("Quiero aprobar algoritmos y algebra") => "algoritmos"
"""

def palabra_mas_larga(texto):
    palabra_actual = ""
    palabra_mas_larga = ""
    for i in range(len(texto)):
        if texto[i] != " ":
            palabra_actual += texto[i]
        else:
            if len(palabra_actual) > len(palabra_mas_larga):
                palabra_mas_larga = palabra_actual
            palabra_actual = ""
    if len(palabra_actual) > len(palabra_mas_larga):
        palabra_mas_larga = palabra_actual
    return palabra_mas_larga

print(palabra_mas_larga("Hola como estas este es un texto de prueba"))
print(palabra_mas_larga("Quiero aprobar algoritmos y algebra"))