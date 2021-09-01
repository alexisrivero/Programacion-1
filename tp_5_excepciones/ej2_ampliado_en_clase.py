"""
Realizar una función que reciba como parámetros dos cadenas de caracteres conteniendo números reales, sume ambos valores y devuelva el
resultado como un número real. 
Devolver -1 si alguna de las cadenas no contiene un número válido, utilizando manejo de excepciones para detectar el error.
"""

class TextoNumeroError(Exception):
    pass

def sumar_numeros(num1, num2):
    try:
        return int(num1) + int(num2)
    except ValueError:
        #return -1
        raise TextoNumeroError

def main():
    try:
        a = sumar_numeros("a", "3")
        print(a)
    except TextoNumeroError:
        print("error")

if __name__ == '__main__':
    main()