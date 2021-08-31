"""Escribir una funcion que reciba como parametro numero del 1 al 9 y devuelva el resultado de sumar n + nn + nnn + nnnn, donde n corresponde
al numero recibido. Por ejemplo, si se ingresa 3 se debe devolver 3702 (3+33+333+3333). Escribir tambien un programa para verificar el
comportamiento de la funcion. No se permite utilizar facilidades de pyton no vistas en clase."""

def sumar(numero):
    primer_numero = numero
    segundo_numero = numero * 11
    tercer_numero = numero * 111
    cuarto_numero = numero * 1111
    return primer_numero + segundo_numero + tercer_numero + cuarto_numero

print(sumar(3))
