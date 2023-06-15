"""
Se cuenta con una lista partidos, ya cargada, que contiene sublistas,  cada una de eses sublistas 
tiene los datos de un partido del mundiasl: pais1, pais2, goles1, goles2.
ejemplo:
[["argentina", 4, "francia", 3], ["brasil", 2, "argentina", 3], ["brasil", 1, "japon", 1], ...]
Se pide que escribas un programa en python que procese esa lista y genere un diccionario con claves pais y valor
total_puntos. Los puntos son 3 al ganador, 1 por empate y 0 por perder. Gana el pais que hizo mas goles.
Luego, debe listar pais-total_puntos, ordenados de mayor a menor por total_puntos. Antes igualdad de puntos, 
el orden indistinto.
"""

partidos = [["argentina", 4, "francia", 3], ["brasil", 2, "argentina", 3], ["brasil", 1, "japon", 1]]

puntos = {}

for partido in partidos:
    pais1, goles1, pais2, goles2 = partido
    
    # Verificar el ganador o empate
    if goles1 > goles2:
        puntos[pais1] = puntos.get(pais1, 0) + 3
        puntos[pais2] = puntos.get(pais2, 0)
    elif goles1 < goles2:
        puntos[pais1] = puntos.get(pais1, 0)
        puntos[pais2] = puntos.get(pais2, 0) + 3
    else:
        puntos[pais1] = puntos.get(pais1, 0) + 1
        puntos[pais2] = puntos.get(pais2, 0) + 1

# Ordenar el diccionario por los valores (total_puntos)
puntos_ordenados = sorted(puntos.items(), key=lambda x: x[1], reverse=True)

# Imprimir pais-total_puntos ordenados de mayor a menor
for pais, total_puntos in puntos_ordenados:
    print(pais, "-", total_puntos)

