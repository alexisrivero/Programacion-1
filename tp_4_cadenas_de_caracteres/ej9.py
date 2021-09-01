"""
Desarrollar una función que devuelva una subcadena con los últimos N caracteres de una cadena dada. 
La cadena y el valor de N se pasan como parámetros.
"""
from funciones_tp4 import devolver_ultimos_n_chars_con_slice, devolver_ultimos_n_chars_sin_slice

def main():
    texto = input("Ingresar texto: ")
    cant_chars = int(input("Ingresar la cantidad de caracteres: "))
    devolver_ultimos_n_chars_con_slice(texto, cant_chars)
    devolver_ultimos_n_chars_sin_slice(texto, cant_chars)

if __name__ == '__main__':
    main()