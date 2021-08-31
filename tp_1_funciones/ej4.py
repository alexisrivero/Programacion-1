from funciones import calcular_total_gastado

""" Una persona desea llevar el control de los gastos realizados al viajar en el subterraneo dentro de un mes. Sabiendo que dicho medio de
transporte utiliza un esquema de tarifas decrecientes (detalladas en la tabla de abajo) se solicita desarrollar una funcion que reciba como
parametro la cantidad de viajes realizados en un determinado mes y devuelva el total gastado en viajes. Realizar tambien un programa para
verificar el comportamiento de la funcion.
    Cantidad de viajes      Valor del pasaje
    1 a 20                  Averiguar valor actualizado
    21 a 30                 20% de descuento sobre tarifa maxima
    31 a 40                 30% de descuento sobre tarifa maxima
    Mas de 40               40% de descuento sobre tarifa maxima
"""

def main():
    cant_viajes = int(input("Ingresar cantidad de viajes en un mes: "))
    calcular_total_gastado(cant_viajes)

if __name__ == "__main__":
    main()