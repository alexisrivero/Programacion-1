"""
Escribir una función para eliminar una subcadena de una cadena de caracteres, a partir de una posición y cantidad de caracteres dadas, 
devolviendo la cadena resultante. Escribir también un programa para verificar el comportamiento de la misma. 
Escribir una función para cada uno de los siguientes casos:
a. Utilizando rebanadas
b. Sin utilizar rebanadas
"""

from funciones_tp4 import eliminar_substring_con_slice, eliminar_substring_sin_slice

def main():
    texto = input("Ingresar texto: ")
    posicion = int(input("Ingresar posicion: "))
    cantidad = int(input("Ingresar cantidad: "))
    eliminar_substring_con_slice(texto, posicion, cantidad)
    eliminar_substring_sin_slice(texto, posicion, cantidad)

if __name__ == '__main__':
    main()