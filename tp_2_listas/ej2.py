from funciones_listas import generar_lista_aleatoria, chequear_repeticion, crear_lista_con_elem_unicos

"""Escribir funciones para:
a. Generar una lista de 50 numeros aleatorios del 1 al 100.
b. Recibir una lista como parametro y devolver True si la misma tiene algun elemento repetido. La funcion no debe modificar la lista.
c. Recibir una lista como parametro y devolver una nueva lista con los elementos unicos de la lista original, sin importar el orden.
Combinar estas tres funciones en un mismo programa.
"""

def main():
    lista = generar_lista_aleatoria(0, 50, 0, 100)
    if chequear_repeticion(lista):
        print(f"{True}, La lista contiene repetidos.")
    else:
        print(f"{False}, la lista no contiene repetidos.")
    crear_lista_con_elem_unicos(lista)

if __name__ == '__main__':
    main()