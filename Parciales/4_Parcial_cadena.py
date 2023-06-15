"""
Escribi una funcion frecuencia_maxima que reciba una cadena de caracateres y devuelve un entero que 
indica la frecuencia de caracateres alfabeticos que mas veces encuentra en la cadena. No debe distinguir
mayusculas de minusculas ni caracteres con tilde. Agregar los tres casos de prueba con doctest.
Ejemplos:
frecuencia_maxima("Aaaaáb") ---> 5
frecuencia_maxima("$_12 3*") ---> 0
frecuencia_maxima("Algoritmos y Programacion") ---> 4
"""
"""
def frecuencia_maxima(cadena):
    cadena = cadena.lower()
    cadena = cadena.replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú', 'u')
    simbolos_esp = "$_"
    letra = []
    contador = 0
    for i in len(cadena):
        cadena = cadena[i]
        if cadena not in simbolos_esp:
            letra.append(cadena)
        cadena = cadena[i]
    for c in letra:
        letra = letra[c]
        if letra in cadena:
            contador += 1
        else:
            letra = letra[c+1]
    puntaje = letra, contador
    return puntaje[1].sort(reverse=True)
print(frecuencia_maxima("Aaaaáb"))
print(frecuencia_maxima("$_12 3*"))
print(frecuencia_maxima("Algoritmos y Programacion"))
"""
def frecuencia_maxima(cadena):
    cadena = cadena.lower()
    cadena = cadena.replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú', 'u')
    caracteres_alfabeticos = [c for c in cadena if c.isalpha()]
    frecuencias = {}
    for c in caracteres_alfabeticos:
        if c in frecuencias:
            frecuencias[c] += 1
        else:
            frecuencias[c] = 1
    if frecuencias:
        return max(frecuencias.values())
    else:
        return 0
    
print(frecuencia_maxima("Aaaaáb"))
print(frecuencia_maxima("$_12 3*"))
print(frecuencia_maxima("Algoritmos y Programacion"))

"----------------------------------------------------------------------------------------------------------------"

def frecuencia_maxima2(cadena):
    cadena = cadena.lower()
    cadena = cadena.replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú', 'u')
    caracteres_alfabeticos = [c for c in cadena if c.isalpha()]
    frecuencias = {}
    for c in caracteres_alfabeticos:
        frecuencias[c] = frecuencias.get(c, 0) + 1
    return max(frecuencias.values(), default=0)

print(frecuencia_maxima2("Aaaaáb"))
print(frecuencia_maxima2("$_12 3*"))
print(frecuencia_maxima2("Algoritmos y Programacion"))
