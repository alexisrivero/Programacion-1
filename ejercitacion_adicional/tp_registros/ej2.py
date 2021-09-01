"""
Realizar las siguientes funciones para manejar “tiempos”: 
a) Ingresar un horario desde teclado, validando que sea correcto 
b) Calcular la diferencia de horas. En el caso que la primera fecha es mayor a la segunda, considerar que la 
primera hora corresponde a la hora del día anterior. La diferencia en horas no supera las 24 horas. 
c) Generar una cadena con formato hh:mm:ss
""" 
from ej1 import Horario


def cargar_horario():
    horario = Horario(0,0,0)
    horario.segundos = int(input("Ingresar hora: "))
    horario.minutos = int(input("Ingresar minutos: "))
    horario.segundos = int(input("Ingresar segundos: "))

def main():
    pass

if __name__ == '__main__':
    main()