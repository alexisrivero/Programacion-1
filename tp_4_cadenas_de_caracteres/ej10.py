"""
Escribir un programa que permita ingresar una cadena de caracteres e imprima un mensaje indicando cuántas letras y cuántos números contiene. 
Por ejemplo, si se ingresa "Hola Mundo 123" debe indicar que se ingresaron 9 letras y 3 números.
"""

from funciones_tp4 import contar_letras_y_numeros

def main():
    texto = input("Ingresar texto: ")
    contar_letras_y_numeros(texto)

if __name__ == '__main__':
    main()