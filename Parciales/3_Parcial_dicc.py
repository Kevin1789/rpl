"""
Se cuenta con una lista partidos, ya cargada, que contiene sublistas,  cada una de eses sublistas 
tiene los datos de un partido del mundiasl: pais1, pais2, goles1, goles2.
ejemplo:
[["argentina", 4, "francia", 3], ["brasil", 2, "argentina", 3], ["brasil", 1, "japon", 1], ...]
Se pide que escribas un programa en python que procese esa lista y genere un diccionario con claves pais y valor
total_puntos. Los puntos son 3 al ganador, 1 por empate y 0 por perder. Gana el pais que hizo mas goles.
Luego, debe listar pais-total_puntos, ordenados de mayor a menor por total_puntos. Antes igualdad de puntos, el orden indistinto.
"""

def partido(lista):
    total_goles = {}
    puntos = 0
    gano = puntos + 3
    empato = puntos + 1
    perdio = puntos
    for pais1, pais2 in lista:
        total_goles[pais1] = total_goles.get(pais1, 0) + puntos
        total_goles[pais2] = total_goles.get(pais2, 0) + puntos
        if total_goles[pais1] > total_goles[pais2]:
            return gano
        if total_goles[pais1] == total_goles[pais2]:
            return empato
        if total_goles[pais1] < total_goles[pais2]:
            return perdio
    return total_goles

def ordenar_partidos(total_goles):
    total_goles_or = dict(sorted(total_goles.items(), key=lambda item: item[1], reverse=True))
    total_goles_or = dict(sorted(total_goles.items(), key=lambda item: item[1], reverse=True))
    print(total_goles_or)
    

lista = [["argentina", 4, "francia", 3], ["brasil", 2, "argentina", 3], ["brasil", 1, "japon", 1]]

ordenar_partidos(partido(lista))