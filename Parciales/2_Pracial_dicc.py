"""
Se cuenta con una lista votacion, ya cargada, que contiene sublistas, cada una de esas sublistas tiene los
siguuientes valores: partido (string), diputados (enteros), senadores (enteros). Ejemplo:
[ ["PP", 19, 35],["PSOE", 20, 30],["VOX", 15, 15], ["PP", 0, 15], ...]. Los recuentos son
de diferentes mesas por lo que los partidos apareceran varias veces.
Se pide que escribas un programa en Python que procese esa lista y genere un diccionario con claves
partido y valor total_votos. El total de votos es la suma de diputados y senadores.
Luego, debe listar los partido-total_votos, ordenados de mayor a menor por total_votos.
"""

def suma_de_votos(lista):
        lista_con_votos_sumados = []
        suma_por_partido=0
        for partido in lista:
                suma_por_partido+=(partido[1]+partido[2])
                lista_con_votos_sumados+=[[partido[0],suma_por_partido]]
                suma_por_partido=0
        return lista_con_votos_sumados

def generador_de_lista(lista_resumida):
        diccionario={}
        for sublista in lista_resumida:
                if not(sublista[0] in diccionario):
                        diccionario[sublista[0]]=sublista[1]
                else:
                        diccionario[sublista[0]]+=sublista[1]
        return sorted(diccionario.items(), key=lambda items : items[1], reverse=True)

def generador_de_diccionario(lista_ordenada):
        diccionario_final_con_recuento_de_votos={}
        for partido in lista_ordenada:
                if not(partido[0] in diccionario_final_con_recuento_de_votos):
                        diccionario_final_con_recuento_de_votos[partido[0]]=partido[1]
                else:
                        diccionario_final_con_recuento_de_votos[partido[0]]+=partido[1]
        return diccionario_final_con_recuento_de_votos

lista = [["PP",19,35],["PSOE",20,30],["VOX",15,15],["PP",0,15],["UNAG",58,45],["PP",1,2],["HH",20,15],["LGA",20,22]]
lista_resumida = suma_de_votos(lista)
lista_final=generador_de_lista(lista_resumida)
diccionario=generador_de_diccionario(lista_final)
print(diccionario)

"----------------------------------------------------------------------------------------------------------------------"

def suma_votos2(lista):
    diccionario = {}
    for partido in lista:
        if partido[0] not in diccionario:
            diccionario[partido[0]] = partido[1] + partido[2]
        else:
            diccionario[partido[0]] += partido[1] + partido[2]
    return diccionario

def ordenar_diccionario2(diccionario):
    lista = list(diccionario.items())
    lista.sort(key=lambda x: x[1], reverse=True)
    return dict(lista)

lista = [["PP",19,35],["PSOE",20,30],["VOX",15,15],["PP",0,15],["UNAG",58,45],["PP",1,2],["HH",20,15],["LGA",20,22]]
diccionario = suma_votos2(lista)
lista_ordenada = ordenar_diccionario2(diccionario)
print(lista_ordenada)

"----------------------------------------------------------------------------------------------------------------------"

def ordenar_diccionario3(diccionario):
    lista = list(diccionario.items())
    for i in range(len(lista)-1):
        for j in range(i+1, len(lista)):
            if lista[i][1] < lista[j][1]:
                lista[i], lista[j] = lista[j], lista[i]
    return dict(lista)

lista = [["PP",19,35],["PSOE",20,30],["VOX",15,15],["PP",0,15],["UNAG",58,45],["PP",1,2],["HH",20,15],["LGA",20,22]]
print(ordenar_diccionario3(diccionario))
"----------------------------------------------------------------------------------------------------------------------"
def suma_votos4(lista):
    diccionario = {}
    for partido in lista:
        if partido[0] not in diccionario:
            diccionario[partido[0]] = partido[1] + partido[2]
        else:
            diccionario[partido[0]] += partido[1] + partido[2]
    return diccionario

def ordenar_diccionario4(diccionario):
    lista = list(diccionario.items())
    lista.sort(key=lambda x: x[1], reverse=True)
    return dict(lista)

lista = [("PP",19,35),("PSOE",20,30),("VOX",15,15),("PP",0,15),("UNAG",58,45),("PP",1,2),("HH",20,15),("LGA",20,22)]
diccionario = suma_votos4(lista)
diccionario_ordenado = ordenar_diccionario4(diccionario)
print(diccionario_ordenado)

"----------------------------------------------------------------------------------------------------------------------"

votacion = [["PP",19,35],["PSOE",20,30],["VOX",15,15],["PP",0,15],["UNAG",58,45],["PP",1,2],["HH",20,15],["LGA",20,22]]

total_votos = {}

for partido, diputados, senadores in votacion:
    if partido in total_votos:
        total_votos[partido] += diputados + senadores
    else:
        total_votos[partido] = diputados + senadores

# Ordenamos el diccionario por valor
total_votos_ordenado = {k: v for k, v in sorted(total_votos.items(), key=lambda item: item[1], reverse=True)}

# Imprimimos los resultados
for partido, votos in total_votos_ordenado.items():
    print(partido, votos)
print("fin del programa")
"----------------------------------------------------------------------------------------------------------------------"

def votacion(lista):
    total_votos = {}
    for partido, diputados, senadores in lista:
        if partido in total_votos:
            total_votos[partido] += diputados + senadores
        else:
            total_votos[partido] = diputados + senadores
    total_votos_ordenado = {partido: votos for partido, votos in sorted(total_votos.items(), key=lambda item: item[1], reverse=True)}
    for partido, votos in total_votos_ordenado.items():
        print(partido, votos)

lista = [["PP",19,35],["PSOE",20,30],["VOX",15,15],["PP",0,15],["UNAG",58,45],["PP",1,2],["HH",20,15],["LGA",20,22]]
votacion(lista)

print("fin del programa 2")

"----------------------------------------------------------------------------------------------------------------------"

def votacion2(lista):
    total_votos = {}
    for partido, diputados, senadores in lista:
        total_votos[partido] = total_votos.get(partido, 0) + diputados + senadores
    #print(total_votos)
    total_votos_ordenado = dict(sorted(total_votos.items(), key=lambda item: item[1], reverse=True))
    #print(total_votos_ordenado)
    for partido, votos in total_votos_ordenado.items():
        print(partido, votos)

lista = [["PP",19,35],["PSOE",20,30],["VOX",15,15],["PP",0,15],["UNAG",58,45],["PP",1,2],["HH",20,15],["LGA",20,22]]
votacion2(lista)

