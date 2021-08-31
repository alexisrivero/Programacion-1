def mayor_estricto(x, y, z):
    #ej 1
    print(x, y, z)
    if x > y:
        if x > z:
            return x
    elif y > x:
        if y > z:
            return y
    elif z > x:
        if z > y:
            return z
    return -1

def sumar_cuadrados(numero):
    #ej 3
    suma = 0
    for i in range(1, numero, 4):
        print(f"{i}**2 = {i**2}")
        suma += i**2
    print("la suma de los cuadrados equivale a:", suma)
    return suma


def calcular_total_gastado(cant_viajes):
    #ej 4
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
    print(f"Total mensual es de: {precio_final}")
    return precio_final

def imprimir_patron(cant_filas):
    #ej 6
    for i in range(cant_filas):
        print("**********")

def imprimir_patron_ascendente(cant_filas):
    #ej 6
    for i in range(1, cant_filas+1):
        for f in range(i):
            print("**", end='')
        print()
    return "listo"

def concatenar_numeros(numero1, numero2):
    #ej 7
    numero_concatenado = numero1 + numero2
    print(numero_concatenado)
    return numero_concatenado

def sumar(numero):
    #ej8
    primer_numero = numero
    segundo_numero = numero * 11
    tercer_numero = numero * 111
    cuarto_numero = numero * 1111
    suma = primer_numero + segundo_numero + tercer_numero + cuarto_numero
    print(f"{suma}, ({primer_numero}+{segundo_numero}+{tercer_numero}+{cuarto_numero})")