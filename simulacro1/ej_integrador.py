from dataclasses import dataclass

@dataclass
class Departamento:
    numero_unidad: int
    descripcion: str
    metros_cuadrados: int
    estado: int
    precio_venta: float

def ingresar_numero(mensaje, min=None, max=None):
    numero = int(input(mensaje))

    return numero

def convertir_numero_a_string(mensaje, min, max):
    numero = int(input(mensaje))
    cadena = ""
    if numero < min:
        print("Ingresar numero valido")
    elif numero > max:
        print("Ingresar numero valido")

    if numero == 1:
        cadena = "Libre"
    elif numero == 2:
        cadena = "Reservado"
    elif numero == 3:
        cadena = "Vendido"
    
    return cadena

def guardar_departamentos(departamentos):
    departamento = Departamento(0, "", 0, 0, 0.0)
    departamento.numero_unidad = len(departamentos) + 1
    departamento.descripcion = input("Ingresar descripcion del departamento: ")
    departamento.metros_cuadrados = ingresar_numero("Ingresar metros cuadrados del departamento: ")
    departamento.estado = convertir_numero_a_string("Ingresar estado del departamento: 1-Libre, 2-Reservado, 3-Vendido", 1, 3)
    departamento.precio_venta = float(input("Ingresar precio de venta: "))

    return departamento

def bubble_sort_por_descripcion(estado, departamentos):
    '''bubble sort para ordenar los departamentos por descripcion teniendo en cuenta su estado'''
    lista = []
    for departamento in range(len(departamentos)):
        if departamentos[departamento].estado != estado:
            continue
        else:
            lista.append(departamentos[departamento])

    n = len(lista)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if lista[j].descripcion > lista[j + 1].descripcion:
                lista[j].descripcion, lista[j + 1].descripcion = lista[j + 1].descripcion, lista[j].descripcion

    return lista

def imprimir_departamentos_libres(departamentos):
    for i in range(len(departamentos)):
        print(f"Imprimiendo los departamentos libres de forma ordenada por descripcion: {departamentos[i]}")
    
    return "wawa"

def cant_departamentos_por_estado(departamentos):
    cant_libres = 0
    cant_reservados = 0
    cant_vendidos = 0
    for departamento in range(len(departamentos)):
        if departamentos[departamento].estado == "Libre":
            cant_libres += 1
        elif departamentos[departamento].estado == "Reservado":
            cant_reservados += 1
        elif departamentos[departamento].estado == "Vendido":
            cant_vendidos += 1

    return f"Cantidad de departamentos libres: {cant_libres}\nCantidad de departamentos reservados: {cant_reservados}\nCantidad de departamentos vendidos: {cant_vendidos}"

def menu():
    departamentos = []
    while True:
        print("=" * 55)
        print("Seleccione la opcion que desea: ")
        print("0-Salir")
        print("1-Cargar departamentos")
        print("2-Mostrar departamentos Libres")
        print("3-Mostrar cantidad de departamentos por estado")
        print("=" * 55)
        seleccion = int(input(""))

        if seleccion == 0:
            print("Gracias por utilizar el programa")
            break
        if seleccion == 1:
            departamento = guardar_departamentos(departamentos)
            departamentos.append(departamento)
            print("Departamento cargado con exito")
        if seleccion == 2:
            ordenar_libres = bubble_sort_por_descripcion("Libre", departamentos)
            imprimir_departamentos_libres(ordenar_libres)
        if seleccion == 3:
            print(cant_departamentos_por_estado(departamentos))

        for i in range(len(departamentos)):
            print(f"IMPRIMIENDO EL DEPARTAMENTO NUMERO: {len(departamentos)}: {departamentos[i]}")

def main():
    menu()


if __name__ == '__main__':
    main()