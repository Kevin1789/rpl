"""
Realizar un programa en Python que solicite ingreso de un número organizador.
Luego permitir el ingreso de números; el final vendrá dado por 0.
Contabilizar en cuatro categorías según el número ingresado sea menor, mayor, múltiplo o divisor del inicial.
Un número puede ser contabilizado en más de una categoría.
"""

def organizar_numeros():
    num_organizador = int(input("Ingrese el número organizador: "))
    menores = 0
    mayores = 0
    multiplos = 0
    divisores = 0
    
    num = int(input("Ingrese un número (0 para finalizar): "))
    while num != 0:
        if num < num_organizador:
            menores += 1
        elif num > num_organizador:
            mayores += 1
        if num % num_organizador == 0:
            multiplos += 1
        if num_organizador % num == 0:
            divisores += 1        
        num = int(input("Ingrese un número (0 para finalizar): "))
            
    print(f"""
Número de números menores al organizador: {menores}
Número de números mayores al organizador: {mayores}
Número de múltiplos del organizador: {multiplos}
Número de divisores del organizador: {divisores}
    """)

organizar_numeros()