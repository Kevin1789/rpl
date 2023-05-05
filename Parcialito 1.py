#Realizar un programa en Python que solicite ingreso de un número organizador.
#Luego permitir el ingreso de números; el final vendrá dado por 0.
#Contabilizar en cuatro categorías según el número ingresado sea menor, mayor, múltiplo o divisor del inicial.
#Un número puede ser contabilizado en más de una categoría.


print("""Este programa cuenta 4 categorías de un grupo ingresado
Los que están por encima, por debajo, divisores y multiplos de un número a eleccion; 0 para finalizar""")

número=int(input("Ingrese el número clasificador de todos "))
veces=int(input("¿Cuántos números desea ingresar? "))
contmenor=0
contmayor=0
contmult=0
contdiv=0

for i in range(veces):
    num=int(input("Ingrese un número "))
    if num<número:
        contmenor+=1
    elif num>número:
        contmayor+=1
    if num%número==0:
        contmult+=1
    if número%num==0:
        contdiv+=1

print(f"""Ingresó {contmenor} números menores que {número} y {contmayor} números mayores. Además de {contmult} números multiplos de {número}""")