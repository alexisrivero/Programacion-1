"""
Definir una función superposición() que reciba como parámetros dos listas de cualquier tipo y
devuelva True si tienen al menos un elemento en común, o False en caso contrario.
Desarrollar un programa para verificar su comportamiento.
"""
from funciones_listas import superposicion

def main():
    superposicion([12, 15, 19, 20], [20, 78, 100, 90])
    print(superposicion([1, 2, 3], [4, 5, 6]))

if __name__ == '__main__':
    main()