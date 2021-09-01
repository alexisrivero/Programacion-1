"""
Escribir una función que reciba como parámetro una cadena de caracteres en la que las palabras se encuentran separadas por uno o más espacios.
Devolver otra cadena con las palabras ordenadas alfabéticamente, dejando un espacio entre cada una.
"""
from funciones_tp4 import ordenar_alfabeticamente

def main():
   texto = input("Ingresar texto: ")
   ordenar_alfabeticamente(texto) 

if __name__ == '__main__':
    main()