"""
Escribir un programa que solicite al usuario el ingreso del nombre del equipo local de un partido con la cantidad 
de goles que hizo. Luego, debe ingresar el nombre del equipo visitante y la cantidad de goles.
Debe imprimir por pantalla el nombre del ganador o un mensaje indicando "Empate".

    >>> Ingrese equipo local: Boca
    >>> Ingrese goles equipo local: 3
    >>> Ingrese equipo visitante: River
    >>> Ingrese goles equipo visitante: 1
    Boca
    >>> Ingrese equipo local: Boca
    >>> Ingrese goles equipo local: 0
    >>> Ingrese equipo visitante: River
    >>> Ingrese goles equipo visitante: 2
    River
    >>> Ingrese equipo local: Boca
    >>> Ingrese goles equipo local:2
    >>> Ingrese equipo visitante: River
    >>> Ingrese goles equipo visitante: 2
    Empate
"""

equipo_local = input("Ingrese equipo local: ")
goles_local = int(input("Ingrese goles equipo local: "))
equipo_visitante = input("Ingrese equipo visitante: ")
goles_visitante = int(input("Ingrese goles equipo visitante: "))
if goles_local > goles_visitante:
    print(equipo_local)
elif goles_local < goles_visitante:
    print(equipo_visitante)
else:
    print("Empate")
    