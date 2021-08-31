"""
Generar una lista con números al azar entre 0 y 100, donde su cantidad de elementos será un número par también obtenido al azar
entre 10 y 50. Luego se solicita partir la lista por la mitad a través de la técnica de las rebanadas, creando dos nuevas listas.
Imprimir las tres listas por pantalla.
"""

from funciones_listas import generar_lista_con_par_de_elementos, slicear_lista


def main():
    slicear_lista(generar_lista_con_par_de_elementos())

if __name__ == '__main__':
    main()