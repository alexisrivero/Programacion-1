"""
Escribir un programa que permita ingresar una cadena de caracteres y coloque enmayúscula la primera letra posterior a un espacio, eliminando
todos los espacios que contenga. Imprimir por pantalla la cadena obtenida.
Ejemplo:
Cadena original:Platero es pequeño, peludo, suave; tan blando por fuera, que se diría todo de algodón, que no lleva huesos. 
Sólo los espejos de azabache de sus ojos son duros cual dos escarabajos de cristal negro.
Cadena final:PlateroEsPequeño,Peludo,Suave;TanBlandoPorFuera,QueSeDiríaTodoDeAlgodón,QueNoLlevaHuesos.
SóloLosEspejosDeAzabacheDeSusOjosSonDurosCualDosEscarabajosDeCristalNegro.
"""

from funciones_tp4 import uppercaser

def main():
    texto = input("Ingresar texto: ")
    uppercaser(texto)

if __name__ == '__main__':
    main()