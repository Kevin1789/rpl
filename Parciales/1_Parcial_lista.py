"""
Escribir una funcion ELEGIR en Python pra decidir si visitar o no una ciudad. Esta funcion
debe devolver True si la ciudad se tiene en cuenta en un itinerario, False de lo contrario.
La funcion recibe dos listas y un entero: una lista de atracciones (atracciones y/o actividadesque tiene o se
pueden hacer en la ciudad), otra de actividades_deseadas (son actividades que al usuario le gustaria realizar)
y con costo promerdio por actividad.
La ciudad de aseptara si:
Se realizan por lo menos tres actividades deaseadas y el costo promedio es menor o igual a MAX_COSTO
(asumir como predefinida)

Ejemplos:
lista_1 = ["museo","senderismo","bares","montañismo"]
lista_2 = ["museo","bares","senderismo","conciertos"]
lista_3 = ["bares","conciertos,"museo"]
elegir(lista_1,lista_2,5000) ---> True si 5000 <= MAX_COSTO
elegir(lista_1,lista_3,1000) ---> False
"""

MAX_COSTO = 5000

def elegir(atracciones, actividades_deseadas, costo_promedio):
    contador = 0
    for actividad in actividades_deseadas:
        if actividad in atracciones:
            contador += 1
    return contador >= 3 and costo_promedio <= MAX_COSTO

lista_1 = ["museo","senderismo","bares","montañismo"]
lista_2 = ["museo","bares","senderismo","conciertos"]
lista_3 = ["bares","conciertos","museo"]
print(elegir(lista_1,lista_2,5000))
print(elegir(lista_1,lista_3,1000))


"----------------------------------------------------------------------------------------------------------------------"

def elegir2(atracciones, actividades_deseadas, costo):
    actividades = []
    validar = False
    for actividad in actividades_deseadas:
        actividades = actividades_deseadas[actividad]
        if (actividades in atracciones) >=3 and (costo <= MAX_COSTO):
            validar = True
    return validar

lista_1 = ["museo","senderismo","bares","montañismo"]
lista_2 = ["museo","bares","senderismo","conciertos"]
lista_3 = ["bares","conciertos","museo"]
print(elegir2(lista_1,lista_2,5000))
print(elegir2(lista_1,lista_3,1000))