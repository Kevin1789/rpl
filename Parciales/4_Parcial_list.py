"""
Escribir una funcion en Python que sera de utilidad para las personas que deban cumplir alguna dieta. La
Funcion se llamara comidas_permitidas y recibira dos listas: La primera alterara nombres de la comidas
(string) con sus respectivos ingredientes (lista de strings). El segundo sera la lista de los ingredientes no permitidos.
Se debe armar y devolver una lista con los nombres de las comidas cuyos ingredientes no 
contengan ni uno solo de los no permitidos.
Ejemplos:
comidas = ["lomo strogonoff",["lomo", "manteca", "vino tinto", "harina", "crema de leche", "cebolla", "chanpignones",
"tomates","caldo"], "milanesa napolitana",["filete de ternera", "huevo", "harina", "pan rallado", "muzarella", "aceite",
"salsa de tomate"],"zapallitos rellenos",["zapallitos", "jamon", "queso", "puerro", "cebolla de verdeo", "morron",
"ajo", "pan rallado"]]
no_permitidos = ["almendra","manteca","huevo"]
no_permitidos2 = ["almendra","puerro"]
comidas_permitidas(comidas,no_permitidos) => ["zapallitos rellenos"]
comidas_permitidas(comidas,no_permitidos2) => ["lomo strogonoff","milanesa napolitana","zapallitos rellenos"]
"""
"""
def comidas_permitidas(comidas, no_permitidas):
    nombres = []
    for comida, ingredientes in len(comidas):
        comidas = comida, ingredientes
        if ingredientes not in no_permitidas:
            nombres.append(comida)
    return nombres
"""
comidas = ["lomo strogonoff",["lomo", "manteca", "vino tinto", "harina", "crema de leche", "cebolla", "chanpignones",
"tomates","caldo"], "milanesa napolitana",["filete de ternera", "huevo", "harina", "pan rallado", "muzarella", "aceite",
"salsa de tomate"],"zapallitos rellenos",["zapallitos", "jamon", "queso", "puerro", "cebolla de verdeo", "morron",
"ajo", "pan rallado"]]
no_permitidos = ["almendra","manteca","huevo"]
no_permitidos2 = ["almendra","puerro"]
#print(comidas_permitidas(comidas,no_permitidos))
#print(comidas_permitidas(comidas,no_permitidos2))
"---------------------------------------------------------------------------------------------------------------"

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