"""
Escribir una función que reciba como parámetro un número entero entre 0 y 3999 y lo convierta en un número romano,
devolviéndolo en una cadena de caracteres. 
¿En qué cambiaría la función si el rango de valores fuese diferente?
"""
from funciones_tp4 import convertir_a_romano

def main():
    numero = int(input("Ingresar numero que desea convertir a romano: "))
    convertir_a_romano(numero)

if __name__ == '__main__':
    main()