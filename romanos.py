"""
Tabla equivalencia
I - Uno
V - Cinco
X - Diez
L - Cincuenta
C - Cien
D - Quinientos
M - Mil
"""

def convertir_en_romano(numero):
    """
    Restricciones: 
     - Es un numero natural
     - entre 1 y 3999, incluidos
        - positivo
        - menos DE 3999
    Resultado es una cadena que contiene (I,V,X,L,C,D,M)

    1. Validar el dato de entrada
        a. Si no es válido, muestro el mensaje de error 
        b. Si es valido, lo convierto 
    
    """
   # try: 
      #  entrada = int(numero)
    #except ValueError:
     #   return("Error: no has introducido un numero entero")

    if not isinstance(numero,int):
        return "Error: no has introducido un numero entero"
    if numero < 1 or numero > 3999:
        return "Error, no cumple consigna"

    return "convertir"

print(convertir_en_romano("56t"))
print(convertir_en_romano(56))
print(convertir_en_romano("56"))
print(convertir_en_romano(-3))

