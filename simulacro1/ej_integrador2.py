from dataclasses import dataclass

@dataclass
class Departamento:
    numero_unidad: int
    descripcion: str
    metros_cuadrados: int
    estado: int
    precio_venta: float

class ValMinMaxError(Exception):
    pass

def validar_valor(numero, min=None, max=None):
    if min != None:
        if numero < min:
            raise ValMinMaxError
    if max != None:
        if numero > max:
            raise ValMinMaxError

def ingresar_numero(mensaje, min, max=None):
    while True:
        try:
            numero = int(input(mensaje))
            validar_valor(numero, min, max)
            return numero
        except ValueError:
            print("Debe ingresar un numero")
        except ValMinMaxError:
            print("Error")

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

def cargar_departamentos(departamentos):
    departamento = Departamento(0, "", 0, 0, 0.0)
    departamento.numero_unidad = len(departamentos) + 1
    departamento.descripcion = input("Ingresar descripcion del departamento: ")
    departamento.metros_cuadrados = ingresar_numero("Ingresar metros cuadrados del departamento: ", 1)
    departamento.estado = convertir_numero_a_string("Ingresar estado del departamento: 1-Libre, 2-Reservado, 3-Vendido", 1, 3)
    departamento.precio_venta = float(input("Ingresar precio de venta"))

    return departamento


def meter_en_lista_deptos_por_estado(estado, departamentos):
    """ Una opción para emitir un listado a pantalla de todos los departamentos en estado “Libre”, 
        ordenados por descripción (utilizar método de la burbuja para ordenar)"""
    lista = []
    for departamento in range(len(departamentos)):
        if departamentos[departamento].estado != estado:
            continue
        else:
            lista.append(departamentos[departamento])

    return lista
            

def bubble_sort(departamentos):
    n = len(departamentos)

    for i in range(n):
        for j in range(0, n-i-1):
            if departamentos[j].descripcion > departamentos[j + 1].descripcion:
                departamentos[j].descripcion, departamentos[j+1].descripcion = departamentos[j+1].descripcion, departamentos[j].descripcion

    return departamentos

def imprimir_departamentos_libres(departamentos):
    for i in range(len(departamentos)):
        print(f"Imprimiendo los departamentos libres de forma ordenada por descripcion: {departamentos[i]}")

    return "wawa"

def contar_departamentos_por_estado(departamentos):
    cant_libres = 0
    cant_reservados = 0
    cant_vendidos = 0

    for departamento in range(len(departamentos)):
        if departamentos[departamento].estado == "Libre":
            cant_libres +=1
        elif departamentos[departamento].estado == "Reservado":
            cant_reservados += 1
        elif departamentos[departamento].estado == "Vendido":
            cant_vendidos += 1

    return f"Cantidad de departamentos Libres: {cant_libres}\nCantidad de departamentos Reservados: {cant_reservados}\nCantidad de departamentos Vendidos: {cant_vendidos}"
        

def menu():
    departamentos = []
    while True:
        print("=" * 55)
        print("0-Salir")
        print("1-Cargar departamentos")
        print("2-Mostrar departamentos libres")
        print("3-Mostrar cantidad de departamentos por estado")
        seleccion = int(input("Seleccione la opcion que desea"))
        if seleccion == 0:
            print("Gracias por utilizar el programa")
            break
        if seleccion == 1:
            departamento = cargar_departamentos(departamentos)
            departamentos.append(departamento)
            print("Departamento cargado con exito")
        if seleccion == 2:
            deptos_libres = meter_en_lista_deptos_por_estado("Libre", departamentos)
            ordenamiento = bubble_sort(deptos_libres)
            imprimir_departamentos_libres(ordenamiento)
        if seleccion == 3:
            print(contar_departamentos_por_estado(departamentos))


        print(departamentos)


def main():
    menu()

if __name__ == '__main__':
    main()