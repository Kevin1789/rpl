def procesar_votaciones5(votaciones):
    resultado = {}
    for participante, puntaje, promedio in votaciones:
        resultado[participante] = resultado.get(participante, 0) + puntaje / promedio
    resultado_ordenado = dict(sorted(resultado.items(), key=lambda x: x[1], reverse=True))
    for participante, promedio in resultado_ordenado.items():
        print(participante, promedio)
    return resultado_ordenado

votaciones = [("Juan", 10, 2), ("Pedro", 20, 3), ("Juan", 30, 4), ("Pedro", 40, 5), ("Juan", 50, 6), ("Pedro", 60, 7), ("Juan", 70, 8), ("Pedro", 80, 9), ("Juan", 90, 10), ("Pedro", 100, 11)]
procesar_votaciones5(votaciones)