"""
Escribir una función que reciba una lista de números enteros como parámetro y la normalice, es decir
que todos sus elementos deben sumar 1.0, respetando las proporciones relativas que cada elemento tiene en la lista original.
Desarrollar también un programa que permita verificar el comportamiento de la función. 
Por ejemplo, normalizar([1, 1, 2]) debe devolver [0.25, 0.25, 0.50].
"""
from funciones_listas import normalizar

def main():
    normalizar([1, 1, 2])

if __name__ == '__main__':
    main()