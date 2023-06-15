"""
En el gran concurso de Monaco de formula 1 se genero una lista, una con la informacion de cada
contenedor. Esta sublista contienen 4 datos: el nombre del corredor (string), el tiempo que estuvo en
carrera en segundos (flotante), el tiempo de su mejor vuelta (la mas rapida) en segundos (flotante) y la
cantidad de vueltas totales (entero).
Ejemplo: [["Leclerc",6593.87,75.773,78],["Verstappen",6531.98,76.604,78],["Stroll",4165.81,76.820,50],etc]
La carrera consistia en 78 vueltas. El ganador es el quien completo las 78 vueltas en el menor tiempo (segundo dato).
El ganador tendra 25 puntos, el segundo 18,etc. Segun la siguiente lista:
PUNTOS = [25,18,15,12,10,8,6,4,2,1]
A partir del pusto 11, los corredores tendran 0 puntos.
Ademas, se ortorga un punto adiccional al corredor que haya hecho la vuelta mas rapida (tercer dato), solo si
ese corredor esta entre los diez primeros.
Se pide que escriba un programa en Python que procese esa lista y genere un diccionario con clave 
corredor y valor puntaje.
Luego, debe listar:corredores-puntaje, ordenados por puntaje de mayor a menor por puntaje.
"""

def mostrar_resultado(candidatos_puntaje):
    for nombre, puntaje in candidatos_puntaje.items():
        print(f"El participante {nombre} tiene {puntaje} puntos")


def cargar_puntos(candidatos, candidato_puntaje):
    nombre = 0
    PUNTOS = [25, 18, 15, 12, 10, 8, 6 ,4, 2, 1]
    contador = 0
    for pos in range(len(candidatos)):
        if(contador <= 10):
            candidato_puntaje[candidatos[pos][nombre]] = PUNTOS[pos]
        else:
            candidato_puntaje[candidato_puntaje[pos][nombre]] = 0
        contador += 1

    return candidato_puntaje


def cargar_datos_competencia(resultados):
    TOTAL_VUELTAS = 78
    nombre = 0
    tiempo_c = 1
    vuelta_mejor = 2
    cant_vueltas = 3
    candidatos_puntaje = {}

    posibles_ganadores = [dato_participante for dato_participante in resultados if (dato_participante[cant_vueltas] == TOTAL_VUELTAS)]
    candidatos = sorted(posibles_ganadores, reverse = False, key = lambda x : x[tiempo_c])
    candidatos_puntaje = cargar_puntos(candidatos, candidatos_puntaje)
    cand_mejor_vuelta = min(posibles_ganadores, key = lambda x : x[vuelta_mejor])
    candidatos_puntaje[cand_mejor_vuelta[nombre]] += 1
    mostrar_resultado(candidatos_puntaje)
    


resultados = [["Leclerc", 6593.87, 75.773, 78], ["Verstappen", 6531.98, 76.604, 78], ["Stroll", 4165.81, 76.820, 50]]
cargar_datos_competencia(resultados)