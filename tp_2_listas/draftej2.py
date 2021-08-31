"""Escribir funciones para:
a. Generar una lista de 50 numeros aleatorios del 1 al 100.
b. Recibir una lista como parametro y devolver True si la misma tiene algun elemento repetido. La funcion no debe modificar la lista.
c. Recibir una lista como parametro y devolver una nueva lista con los elementos unicos de la lista original, sin importar el orden.
Combinar estas tres funciones en un mismo programa.
"""

import random

def generar_lista_aleatoria():
    lista = []
    for i in range(0,50):
        lista.append(random.randint(1,100))
    return lista

print(generar_lista_aleatoria())


def chequear_repeticion(lista):
    for i in range(len(lista)):
        if lista.count(lista[i]) > 1:
            return True
    return False


print(chequear_repeticion(generar_lista_aleatoria()))