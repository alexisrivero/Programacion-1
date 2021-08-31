""" Desarrolar una funcion que reciba tres numeros positivos y devuelva el mayor de los tres, solo si este es unico(mayor estricto).
En caso de no existir el mayor escricto devolver -1. No utilizar operadores logicos (and, or, not). Desarrollar tambien un programa
para ingresar los tres valores, invocar la funcion y mostrar el maximo hallado, o un mensaje informativo si este no existe """

from funciones import mayor_estricto

def main():
    x = int(input("Ingresar primer numero: "))
    y = int(input("Ingresar segundo numero: "))
    z = int(input("Ingresar tercero numero: "))

    mayor = mayor_estricto(x, y, z)

    if mayor != -1:
        print(f"el numero mayor ingresado es el: {mayor}")
    else:
        print(f"no existe ningun mayor stricto: {mayor}")

if __name__ == '__main__':
    main()