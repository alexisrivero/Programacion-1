"""
Escribir una función que reciba una lista como parámetro y devuelva True si la lista está ordenada en forma ascendente
o False en caso contrario. Por ejemplo, ordenada([1,  2,  3]) retorna True y ordenada(['b',  'a']) retorna False.
Desarrollar además un programa para verificar el comportamiento de la función. 
"""
from funciones_listas import ordenada

def main():
    print(ordenada([1, 2, 3, 4, 5]))
    print(ordenada(["b", "a"]))

if __name__ == '__main__':
    main()