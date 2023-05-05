"""
Escribir una funcion elegir en python para decidir asociarse o no a un club. Esta funcion debe 
devolver True si es el club es aceptado, False de lo contrario.
La funcion recibe dos lista y un entero: una de actividades (actividades que se realizan en el club),
otra de actividades_deseadas (son las actividades que al usuario le gustaria realizar) y un valor de cuota.
El club se acptara si:
    - Si realizan por lo menos dos actividades deseadas y el valor de la cuota es menor o igual a
    MAX_CUOTA (asumir como predefinida)
Ejemplos:
lista_1 = ["natcion","gimnasio","voley","fulbol"]
lista_2 = ["gimnasio","voley","natacion"]
lista_3 = ["karate","natacion","fulbol"]
elegir(lista_1,lista_2,5000) => True si 5000 <= MAX_CUOTA
elegir(lista_1,lista_3,5000) => True si 5000 <= MAX_CUOTA
elegir(lista_2,lista_3,100) => False
"""

MAX_CUOTA=5000
def elegir(actividades,actividades_deseadas,cuota):
    aceptacion=False
    lista_de_comparacion=[]
    for caracter in actividades:
        if caracter in actividades_deseadas:
            lista_de_comparacion+=[caracter]
    if len(lista_de_comparacion)>=2 and cuota<=MAX_CUOTA:
        aceptacion=True
    return(aceptacion)

lista_1=["natacion","gimnasio","voley","futbol"]
lista_2=["natacion","voley","gimnasio"]
lista_3=["natacion","futbol","karate"]
print(elegir(lista_1,lista_2, 5000))
print(elegir(lista_1,lista_3, 5000))
print(elegir(lista_2,lista_3, 100))

"----------------------------------------------------------------------------------------------------------------------"

def elegir2(actividades, actividades_deseadas, cuota):
    if len(actividades_deseadas) == 0:
        return False
    if len([actividad for actividad in actividades if actividad in actividades_deseadas]) >= 2 and cuota <= MAX_CUOTA:
        return True
    else:
        return False

print(elegir2(lista_1,lista_2,5000))
print(elegir2(lista_1,lista_3,5000))
print(elegir2(lista_2,lista_3,100))

"----------------------------------------------------------------------------------------------------------------------"