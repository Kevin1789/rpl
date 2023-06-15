"""
Escribir en python una funcion posibles_amistades que recibe dos listas: una de personas y otra de intereses_afines.
La lista de personaas intercala nombres con lista de intereses, es decir, en la primera posicion tiene un nombre y 
en la segunda, una lista de intereses, etc. La funcion debe devolver una lista solo con los nomnbres de las personas
que tengan dos o mas intereses en comun.
ejemplos:
personas = ["camila",["futbol","natacion","voley","gimnasio"],"mario",["natacion","basquet","gimnasio","cine"],"rosa",["cine","natacion","teatro"]]]
intereses_afines = ["natacion","teatro","cine","tenis"]
intereses_afines2 = ["cine","tenis","ajedrez"]]
posibles_amistades(personas,intereses_afines) => ["mario","rosa"]
posibles_amistades(personas,intereses_afines2) => []  
"""

def posibles_amistades(personas, intereses_afines):
    amistades = []
    for i in range(0, len(personas), 2):
        nombre = personas[i]
        intereses = personas[i+1]
        intereses_comunes = set(intereses) & set(intereses_afines)
        if len(intereses_comunes) >= 2:
            amistades.append(nombre)
    return amistades

personas = ["camila", ["futbol", "natacion", "voley", "gimnasio"],
            "mario", ["natacion", "basquet", "gimnasio", "cine"],
            "rosa", ["cine", "natacion", "teatro"]]
intereses_afines = ["natacion", "teatro", "cine", "tenis"]
intereses_afines2 = ["cine", "tenis", "ajedrez"]

print(posibles_amistades(personas, intereses_afines))
print(posibles_amistades(personas, intereses_afines2))
