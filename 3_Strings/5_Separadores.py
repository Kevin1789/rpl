"""
Completar el cuerpo de la función. La misma debe tomar la cadena que se pasa como parámetro e insertar el 
separador cada tantos caracteres como indique el parámetro "espaciado".

Ejemplos:

   insertar_separadores("255255255255", ".", 3) => "255.255.255.255"
   insertar_separadores("holacomoestas", "|", 4) => "hola|como|esta|s"  
"""

def insertar_separadores(cadena, separador, espaciado):
    resultado = ""
    for i in range(len(cadena)):
        resultado += cadena[i]
        if (i+1) % espaciado == 0 and i != len(cadena)-1:
            resultado += separador
    return resultado

print(insertar_separadores("255255255255", ".", 3))
print(insertar_separadores("holacomoestas", "|", 4))