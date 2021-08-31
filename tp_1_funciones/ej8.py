from funciones import sumar

"""Escribir una funcion que reciba como parametro numero del 1 al 9 y devuelva el resultado de sumar n + nn + nnn + nnnn, donde n corresponde
al numero recibido. Por ejemplo, si se ingresa 3 se debe devolver 3702 (3+33+333+3333). Escribir tambien un programa para verificar el
comportamiento de la funcion. No se permite utilizar facilidades de pyton no vistas en clase."""

def main():
    numero = int(input("Ingresar numero: "))
    sumar(numero)


if __name__ == '__main__':
    main()