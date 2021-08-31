from funciones import concatenar_numeros

"""
Desarrollar una función que reciba como parámetros dos números enteros y devuelva el número que resulte de concatenar ambos valores.
Por ejemplo, si recibe 1234 y 567 debe devolver 1234567. No se permite utilizar facilidades de Python no vistas en clase.
"""

def main():
    numero1 = input("Ingresar primer secuencia de numeros: ")
    numero2 = input("Ingresar segunda secuencia de numeros: ")
    concatenar_numeros(numero1, numero2)

if __name__ == '__main__':
    main()