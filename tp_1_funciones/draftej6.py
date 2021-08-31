"""Escribir dos funciones para imprimir por pantalla cada uno de los siguientes patrones de asteriscos, donde la cantidad de filas se recibe
como parametro
**********      **
**********      ****
**********      ******
**********      ********
**********      **********
"""

def imprimir_patron(cant_filas):
    lista = []
    asteriscos = "**********"
    for i in range(cant_filas):
        lista.append(asteriscos)
    return lista

def imprimir_patron_ascendente(cant_filas):
    lista = []
    asteriscos_minimos = "**"
    for i in range(1, cant_filas+1):
        lista.append(asteriscos_minimos*i)
    for i in range(len(lista)): #para que funcione con el print
        print(lista[i])         #que no esta comentado
    return lista


#print('\n'.join(map(str, imprimir_patron(5))))
#print('\n'.join(map(str, imprimir_patron_ascendente(5))))

#print(*imprimir_patron(5), sep="\n")
#print(*imprimir_patron_ascendente(5), sep="\n")
print(imprimir_patron_ascendente(5))