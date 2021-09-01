"""
Desarrollar una función que determine si una cadena de caracteres es capicúa, sin utilizar cadenas auxiliares.
Escribir además un programa que permita verificar su funcionamiento.
"""
from funciones_tp4 import chequear_capicua

def main():
    texto = input("Ingresar texto: ")
    if chequear_capicua(texto):
        print(f"{texto} es una cadena de texto capicua!")
    else:
        print(f"{texto} no es capicua")

if __name__ == '__main__':
    main()