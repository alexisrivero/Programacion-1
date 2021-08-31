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

def caldular_total_gastado(cant_viajes):
    precio_por_pasaje = 100
    total = precio_por_pasaje * cant_viajes
    descuento = 0
    
    if cant_viajes <= 0:
        return "Se necesita al menos 1 pasaje"
    elif cant_viajes > 0 and cant_viajes <= 20:
        precio_final = total
    elif cant_viajes > 20 and cant_viajes <= 30:
        descuento = total * 0.20
    elif cant_viajes > 30 and cant_viajes <= 40:
        descuento = total * 0.30
    else:
        descuento = total * 0.40
    
    precio_final = total - descuento

    return precio_final

print(caldular_total_gastado(0))
print(caldular_total_gastado(1))
print(caldular_total_gastado(25))
print(caldular_total_gastado(40))
print(caldular_total_gastado(50))