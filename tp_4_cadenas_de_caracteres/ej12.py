"""
Desarrollar una función para reemplazar todas las apariciones de una palabra por otra en una cadena de caracteres y
devolver la cadena obtenida y un entero con la cantidad de reemplazos realizados.
Escribir también un programa para verificar el comportamiento de la función. 
"""
from funciones_tp4 import reemplazador_de_palabras

def main():
    texto = input("Ingresar texto: ")
    palabra_a_reemplazar = input("Ingresar palabra a reemplazar: ")
    reemplazar_por = input("Reemplazar por: ")
    reemplazador_de_palabras(texto, palabra_a_reemplazar, reemplazar_por)

if __name__ == '__main__':
    main()