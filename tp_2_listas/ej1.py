"""
Desarrollar cada una de las siguientes funciones y escribir un programa que permita verificar su funcionamiento imprimiendo
la lista luego de invocar a cada función:
a. Cargar una lista con números al azar de cuatro dígitos. La cantidad de elementos también será un número al azar de dos dígitos.
b. Calcular y devolver la sumatoria de todos los elementos de la lista anterior.
c. Eliminar todas las apariciones de un valor en la lista anterior. El valor a eliminar se ingresa desde el teclado y la función lo recibe
 como parámetro.
d. Determinar si el contenido de una lista cualquiera es capicúa, sin usar listas auxiliares. Un ejemplo de lista capicúa es [50, 17, 91, 17, 50].
"""

from funciones_listas import cargar_lista_al_azar, sumar_elementos_de_lista_anterior, eliminar_apariciones_de_valor

def main():
    valor_a_eliminar = int(input("Ingresar valor a eliminar: "))
    #cargar_lista_al_azar()
    #sumar_elementos_de_lista_anterior(cargar_lista_al_azar())
    eliminar_apariciones_de_valor(cargar_lista_al_azar(), valor_a_eliminar)

if __name__ == '__main__':
    main()