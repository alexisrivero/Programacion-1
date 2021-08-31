"""
Crear una lista con los cuadrados de los números entre 1 y N (ambos incluidos), donde N se ingresa desde el teclado.
Luego se solicita imprimir los últimos 10 valores de la lista. 
"""

from funciones_listas import crear_lista_con_cuadrados, imprimir_ultimos_diez_valores

def main():
    numero = int(input("Ingresar numero: "))
    imprimir_ultimos_diez_valores(crear_lista_con_cuadrados(numero))

if __name__ == '__main__':
    main()