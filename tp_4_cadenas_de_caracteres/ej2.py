"""
Leer una cadena de caracteres e imprimirla centrada en pantalla. Suponer que la misma tiene 80 columnas.
"""
from funciones_tp4 import centrar_string

def main():
    texto = input("ingresar texto: ")
    columnas = int(input("Ingresar cantidad de columnas: "))
    centrar_string(texto, columnas)

if __name__ == '__main__':
    main()