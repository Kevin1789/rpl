#1
def contador(cadena):
    cadena = cadena.lower()
    cadena = cadena.replace("a", "á").replace("e", "é").replace("i", "í").replace("o", "ó").replace("u", "ú")
    letra = []
    for i in cadena:
        if i.isalpha() and i not in letra:
            letra.append(i)
    return len(letra)
print("cadena 1")
print(contador("Aaaáb"))
print(contador("$_123*"))
print(contador("Algoritmos y Programación"))
#2
def validar(cadena):
    valido = False
    if len(cadena) >= 8 and len(cadena) <= 12:
        valido = True
        for i in cadena:
            if not i.isalpha() and not i.isnumeric() and i not in "*-$@":
                valido = False
            elif i in "áéíóúÁÉÍÓÚ":
                valido = False
    return valido
print("cadena 2")
print(validar("Algoritmos $1"))
print(validar("Aprobé-con-7"))
print(validar("Algoritmos$1"))
print(validar("Aprobe-con-7"))
#3
def validar2(cadena):
    simbolos = 0 
    mayusculas = 0
    minusculas = 0
    valido = False
    if len(cadena) >= 6 and len(cadena) <= 12:
        valido = True
        for i in cadena:
            if i.isupper():
                mayusculas += 1
            elif i.islower():
                minusculas += 1
            elif i in "*-$@" or i in "1234567890":
                simbolos += 1
    if simbolos >= 2 and mayusculas >= 2 and minusculas >= 2:
        valido = True
        for i in cadena:
            if i in "áéíóúÁÉÍÓÚ":
                valido = False
    return valido
print("cadena 3")
print(validar2("Algoritmos $1"))
print(validar2("AprObé-con-7"))
print(validar2("AlgOritmos$1"))
print(validar2("AproBe-con-7"))
#4
def tildes(cadena):
    vocales_con_tildes = "áéíóúÁÉÍÓÚ"
    vocales_sin_tildes = "aeiouAEIOU"
    for i in range(len(vocales_con_tildes)):
        cadena = cadena.replace(vocales_con_tildes[i], vocales_sin_tildes[i])
    return cadena

def frecuencia_maxima(cadena):
    cadena = tildes(cadena)
    frecuencias = {}
    for caracter in cadena:
        if caracter.isalpha():
            caracter = caracter.lower()
            frecuencias[caracter] = frecuencias.get(caracter, 0) + 1

    if not frecuencias:
        return 0

    return max(frecuencias.values())
print("cadena 4")
print(frecuencia_maxima("Aaaaáb"))  # 5
print(frecuencia_maxima("$_12 3*"))  # 0
print(frecuencia_maxima("Algoritmos y Programacion"))  # 4
#5
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
print("lista 5")
print(elegir(lista_1,lista_2,5000))
print(elegir(lista_1,lista_3,1000))
#6
def elegir2(actividades, actividades_deseadas, cuota):
    contador = 0
    for actividad in actividades_deseadas:
        if actividad in actividades:
            contador += 1
    return contador >= 2 and cuota <= MAX_COSTO

lista_1=["natacion","gimnasio","voley","futbol"]
lista_2=["natacion","voley","gimnasio"]
lista_3=["natacion","futbol","karate"]
print("lista 6")
print(elegir2(lista_1,lista_2, 5000))
print(elegir2(lista_1,lista_3, 5000))
print(elegir2(lista_2,lista_3, 100))
#7
def comidas_permitidas(comidas, no_permitidos):
    nombres = []
    for i in range(0, len(comidas), 2):
        nombre = comidas[i]
        ingredientes = comidas[i + 1]
        if len(no_permitidos) not in ingredientes:#not any(ingrediente in no_permitidos for ingrediente in ingredientes):
            nombres.append(nombre)
    return nombres
comidas = ["lomo strogonoff",["lomo", "manteca", "vino tinto", "harina", "crema de leche", "cebolla", "chanpignones",
"tomates","caldo"], "milanesa napolitana",["filete de ternera", "huevo", "harina", "pan rallado", "muzarella", "aceite",
"salsa de tomate"],"zapallitos rellenos",["zapallitos", "jamon", "queso", "puerro", "cebolla de verdeo", "morron",
"ajo", "pan rallado"]]
no_permitidos = ["almendra","manteca","huevo"]
no_permitidos2 = ["almendra","puerro"]
print(comidas_permitidas(comidas,no_permitidos))#[zapallitos rellenos]
print(comidas_permitidas(comidas,no_permitidos2))#[lomo strogonoff, milanesa napolitana, zapallitos rellenos]