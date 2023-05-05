"""
Escribe un programa con las siguientes caracteristicas:

Solicitar al usuario un valor de gravedad(m/s^2) y un peso(kg)
Calcular e imprimir el peso con respecto a la nueva gravedad
Si la gravedad es mayor o igual a 5G, antes del peso imprimir un aviso:
"Alerta, gravedad peligrosamente alta"
    >>> Ingrese el valor de la gravedad: 3.721
    >>> Ingrese su peso: 50
    Su peso seria: 18.97 kg

    >>> Ingrese el valor de la gravedad: 50
    >>> Ingrese su peso: 50
    Alerta, gravedad peligrosamente alta
    Su peso seria: 254.92 kg
~ Tener en cuenta ~

G (gravedad en la tierra) = 9.807

Imprimir numeros con solo 2 digitos decimales:

"print("{:.2f}".format(TU_NUMERO))"

Input de gravedad siempre sera positivo
"""

G = 9.807
gravedad = float(input("Ingrese el valor de la gravedad: "))
peso = float(input("Ingrese su peso: "))
if gravedad >= 5*G:
    print("Alerta, gravedad peligrosamente alta")
peso_nueva_gravedad = peso * gravedad / G
print("Su peso seria: {:.2f} kg".format(peso_nueva_gravedad))


