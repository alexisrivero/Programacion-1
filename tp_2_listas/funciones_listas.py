import random

def cargar_lista_al_azar():
    #ej 1.a
    lista = []
    for i in range(random.randint(10, 99)):
        lista.append(random.randint(1000, 9999))
    print("lista original:", lista)
    return lista

def sumar_elementos_de_lista_anterior(lista):
    #ej 1.b
    suma = 0
    for i in range(len(lista)):
        suma += lista[i]
    print("la suma de elementos es:", suma)
    return suma

def eliminar_apariciones_de_valor(lista, valor):
    #ej 1.c
    for i in range(len(lista)):
        if valor == lista[i]:
            lista.pop(i)
    print("lista alterada:", lista)
    return lista

def generar_lista_aleatoria(emin, emax, nmin, nmax):
    #ej 2.a 
    #emin y emax se refiere a la cant de elementos
    #nmin y nmax se refiere a los numeros
    lista = []
    for i in range(emin, emax):
        lista.append(random.randint(nmin, nmax))
    print(lista)
    return lista

def chequear_repeticion(lista):
    #ej 2.b
    for i in range(len(lista)):
        if lista.count(lista[i]) > 1:
            return True
    return False

def crear_lista_con_elem_unicos(lista):
    #ej 2.c
    nueva_lista = []
    for i in range(len(lista)):
        if lista[i] not in nueva_lista:
            nueva_lista.append(lista[i])
    print("nueva lista sin repetidos: ", nueva_lista)
    return nueva_lista

def crear_lista_con_cuadrados(numero):
    #ej 3.a
    lista = []
    for i in range(1, numero+1):
        lista.append(i**2)
    print(lista)

    return lista

def imprimir_ultimos_diez_valores(lista):
    #ej 3.b
    ultimos_diez_valores = lista[-10:]
    print("ultimos diez valores de la lista:", ultimos_diez_valores)

    return ultimos_diez_valores
    
def superposicion(lista1, lista2):
    #ej 4
    for i in range(len(lista1)):
        if lista1[i] in lista2:
            print(True)
            return True
    
    return False

def generar_lista_a_partir_de_sumas():
    #ej 5
    lista = []
    nueva_lista = []
    suma = 0
    for i in range(3):
        lista.append(random.randint(1, 10))
    
    for i in range(len(lista)):
        suma += lista[i]
        nueva_lista.append(suma)
    print("lista original:", lista)
    print("nueva lista:", nueva_lista)

    return nueva_lista


def superposicion_palabras(lista_original, palabras_a_eliminar):
    #ej 6
    print("lista original:", lista_original)
    print("palabras a eliminar:", palabras_a_eliminar)

    for nombre in palabras_a_eliminar:
        if nombre in lista_original:
            lista_original.remove(nombre)

    print("lista resultante:", lista_original)
    return lista_original

def ordenada(lista):
    #ej 7
    ordenada = True
    for i in range(len(lista)-1):
        if lista[i] > lista[i+1]:
            ordenada = False

    return ordenada

def normalizar(lista):
    #ej 9
    lista_normalizada = []
    suma = 0
    for i in range(len(lista)):
        suma += lista[i]
    
    for i in range(len(lista)):
        lista_normalizada.append(lista[i]/suma)
    print(lista_normalizada)
    
    return lista_normalizada

def generar_lista_con_par_de_elementos():
    #ej10
    lista = []
    for i in range(10, 50):
        lista.append(random.randint(0, 100))
    if len(lista) % 2 == 1:
        lista.pop()

    print(lista)
    return lista

def slicear_lista(lista):
    #ej10
    mitad_de_lista = len(lista)//2
    primer_mitad = lista[:mitad_de_lista]
    segunda_mitad = lista[mitad_de_lista:]

    print("primer mitad:", primer_mitad)
    print("segunda mitad", segunda_mitad)
    return primer_mitad, segunda_mitad

def generar_lista_con_multiplos_de_siete():
    #ej13
    #la lista debe contener multiplos de 7 entre 2000 y 3500
    #que no sean multiplos de 5
    lista = []
    for i in range(2000, 3500, 7):
        if i % 5 != 0:
            lista.append(i)
    print(lista)

    return lista
