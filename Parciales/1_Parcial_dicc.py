"""
El progrma "Camino a la fama", los participantes muestran sus aptitudes baile, canto, etc.
Un jurado vota a los participantes colocando un puntaje del 1 al 10.
Esto genera una lista de lista (cada sublista es una votacion).
Ejemplo: [["Luisa",4],["Mariano",10],["Luisa",5],etc...]. Las votaciones
son de distintos jueces y por distintas actuaciones por lo que los participantes apareceran varias veces.
Se pide que se escriba un programa compuesto por funciones en python, que procese esa lista y 
genere un diccionario con claves participante y valores sumatoria_puntaje, cantidad_puntajes, promedio_puntaje.
Luego, debe listar: participantes-promedio_puntaje, ordenados de mayor a menor por promedio_puntaje.
Con el ejemplo anterior deberia quedar.
Mariano 10
Luisa 4.5
"""

def procesar_votaciones(votaciones):
    resultados = {}
    for participante, puntaje in votaciones:
        if participante in resultados:
            resultados[participante]["sumatoria_puntaje"] += puntaje
            resultados[participante]["cantidad_puntajes"] += 1
        else:
            resultados[participante] = {"sumatoria_puntaje": puntaje, "cantidad_puntajes": 1}
    for participante in resultados:
        resultados[participante]["promedio_puntaje"] = resultados[participante]["sumatoria_puntaje"]/resultados[participante]["cantidad_puntajes"]
    return resultados

def listar_participantes(resultados):
    participantes_ordenados = sorted(resultados.items(), key=lambda x: x[1]["promedio_puntaje"], reverse=True)
    for participante, datos in participantes_ordenados:
        print(participante, datos["promedio_puntaje"])

votaciones = [["Luisa",4],["Mariano",10],["Luisa",5]]
resultados = procesar_votaciones(votaciones)

listar_participantes(resultados)

"---------------------------------------------------------------------------------------------------------------------------------------------------"

def procesar_votaciones2(votaciones):
    resultados = {}
    for participante, puntaje in votaciones:
        resultados.setdefault(participante, {"sumatoria_puntaje": 0, "cantidad_puntajes": 0})
        resultados[participante]["sumatoria_puntaje"] += puntaje
        resultados[participante]["cantidad_puntajes"] += 1
    for participante in resultados:
        resultados[participante]["promedio_puntaje"] = resultados[participante]["sumatoria_puntaje"] / resultados[participante]["cantidad_puntajes"]
    return resultados

def listar_participantes2(resultados):
    for participante, datos in sorted(resultados.items(), key=lambda x: x[1]["promedio_puntaje"], reverse=True):
        print(participante, datos["promedio_puntaje"])

listar_participantes2(resultados)

"---------------------------------------------------------------------------------------------------------------------------------------------------"

def procesar_votaciones3(votaciones):
    resultados = {}
    for participante, puntaje in votaciones:
        if participante not in resultados:
            resultados[participante] = {"sumatoria_puntaje": 0, "cantidad_puntajes": 0}
        resultados[participante]["sumatoria_puntaje"] += puntaje
        resultados[participante]["cantidad_puntajes"] += 1
    for participante in resultados:
        resultados[participante]["promedio_puntaje"] = resultados[participante]["sumatoria_puntaje"] / resultados[participante]["cantidad_puntajes"]
    return resultados

def listar_participantes3(resultados):
    for participante, datos in sorted(resultados.items(), key=lambda x: x[1]["promedio_puntaje"], reverse=True):
        print(participante, datos["promedio_puntaje"])

listar_participantes3(resultados)

"---------------------------------------------------------------------------------------------------------------------------------------------------"
def procesar_votaciones4(votaciones):
    resultados = {}
    for participante, puntaje in votaciones:
        resultados[participante] = resultados.get(participante, {"sumatoria_puntaje": 0, "cantidad_puntajes": 0})
        resultados[participante]["sumatoria_puntaje"] += puntaje
        resultados[participante]["cantidad_puntajes"] += 1
    for participante in resultados:
        resultados[participante]["promedio_puntaje"] = resultados[participante]["sumatoria_puntaje"] / resultados[participante]["cantidad_puntajes"]
    return resultados

def listar_participantes4(resultados):
    total_resultados = dict(sorted(resultados.items(), key=lambda x: x[1]["promedio_puntaje"], reverse=True))
    return total_resultados

def mostrar_resultados(total_resultados):
    for participante, datos in total_resultados.items():
        print(participante, datos["promedio_puntaje"])
    return total_resultados

votaciones = [["Luisa",4],["Mariano",10],["Luisa",5]]
mostrar_resultados(listar_participantes4(procesar_votaciones4(votaciones)))

"---------------------------------------------------------------------------------------------------------------------------------------------------"

