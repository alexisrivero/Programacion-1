""" Para un numero entero N menor de 100 recibido como parametro, escribir un programa que utilice una funcion para devolver la suma de los
cuadrados de aquellos numeros entre 1 y N que estan separados entre si por cuatro unidades.(1**2 + 5**2 + 9**2 + 13**2 + ...)."""

from funciones import sumar_cuadrados

def main():
    numero = int(input("Ingresar numero menor a 100: "))
    while numero > 100:
        print("Por favor, ingresar numero valido")
        numero = int(input("Ingresar numero menor a 100: "))

    sumar_cuadrados(numero)

if __name__ == '__main__':
    main()