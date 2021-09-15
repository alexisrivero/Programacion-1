from dataclasses import dataclass
import random

@dataclass
class Reportes:
    apellido: str
    nombre: str
    edad: int
    carrera: int
    cant_materias_aprobadas: int

class ErrorCadenaVacia(Exception):
    pass

def contar_numeros(texto):
    contador = 0
    numeros = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    if texto == "":
        raise ErrorCadenaVacia
    
    for i in range(len(texto)):
        if texto[i] in numeros:
            contador += 1

    return f"La cantidad de numeros en la cadena es de: {contador}"

def main_ej1():
    print(contar_numeros("h0l4"))
    print(contar_numeros(""))


def crear_matriz(filas, columnas):
    matriz = []
    for i in range(filas):
        lista = []
        for j in range(columnas):
            lista.append(random.randint(0, 50))
        matriz.append(lista)
    print(matriz)

    return matriz


def buscar_mayor(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    vector = []

    numero_mayor = 0
    fila_del_mayor = 0
    columna_del_mayor = 0

    for fila in range(filas):
        for columna in range(columnas):
            if matriz[fila][columna] > numero_mayor:
                numero_mayor = matriz[fila][columna]
                fila_del_mayor = fila
                columna_del_mayor = columna

    vector.append(fila_del_mayor)
    vector.append(columna_del_mayor)
                
    return vector

def main_ej2():
    matriz = crear_matriz(3, 3)
    print(buscar_mayor(matriz))


def ingresar_texto(mensaje):
    texto = input(mensaje)

    return texto

def ingresar_numero(mensaje):
    numero = int(input(mensaje))

    return numero


def cargar_reportes(reportes):
    reporte = Reportes("", "", 0, 0, 0)
    reporte.apellido = ingresar_texto("Ingresar apellido del alumno: ")
    reporte.nombre = ingresar_texto("Ingresar nombre del alumno: ")
    reporte.edad = ingresar_numero("Ingresar edad del alumno: ")
    reporte.carrera = ingresar_numero("Ingresar carrera del alumno: 1-Contador, 2-Abogado, 3-Software:  ")
    reporte.cant_materias_aprobadas = ingresar_numero("Ingresar cantidad de materias aprobadas: ")

    return reporte

def chequear_cant_materias_aprobadas(reportes):

    for i in range(len(reportes)):
        try:
            alumno_con_mas_aprobadas = reportes[i]
            if reportes[i].cant_materias_aprobadas > reportes[i+1].cant_materias_aprobadas:
                continue
            elif reportes[i].cant_materias_aprobadas == reportes[i+1].cant_materias_aprobadas:
                continue
            else:
                alumno_con_mas_aprobadas = reportes[i+1] 
            return alumno_con_mas_aprobadas
        except IndexError:
            print("Error de indice")

def imprimir_alumno(alumno):
    print("Apellido del alumno: ", alumno.apellido)
    print("Nombre del alumno: ", alumno.nombre)
    print("Edad del alumno: ", alumno.edad)


def promedio_edad_alumnos_por_carrera(carrera, alumnos):
    cant_alumnos = 0
    suma_edades = 0
    for i in range(len(alumnos)):
        if alumnos[i].carrera == carrera:
            cant_alumnos += 1
            suma_edades += alumnos[i].edad
    promedio = suma_edades / cant_alumnos

    return f"La edad promedio de la carrera {carrera} es de: {promedio}"

def imprimir_alumnos_por_carrera(carrera, alumnos, edad):
    for i in range(len(alumnos)):
        if alumnos[i].carrera == carrera:
            if alumnos[i].edad > edad:
                print(f"{alumnos[i].nombre} | {alumnos[i].apellido} | {alumnos[i].edad}")

def menu():
    reportes = []
    while True:
        print("-" * 55)
        print("0-salir")
        print("1-cargar reportes")
        print("2-chequear alumno con mas materias aprobadas")
        print("3- imprimir promedio de edad de alumno para la carrera de Software")
        print("4- imprimir alumnos de la carrera Contador mayores de 30")
        seleccion = input("Seleccionar del 0 al 3")
        print("-" * 55)
    
        if seleccion == "0":
            break
        elif seleccion == "1":
            reporte = cargar_reportes(reportes)
            reportes.append(reporte)
            print("Reporte cargado")
        elif seleccion == "2":
            mejor_alumno = chequear_cant_materias_aprobadas(reportes)
            imprimir_alumno(mejor_alumno)
        elif seleccion == "3":
            promedio_edad = promedio_edad_alumnos_por_carrera(3, reportes)
            print(promedio_edad)
        elif seleccion == "4":
            imprimir_alumnos_por_carrera(1, reportes, 30)

def main_ej3():
    menu()


if __name__ == "__main__":
    #main_ej1()
    main_ej2()
    #main_ej3()