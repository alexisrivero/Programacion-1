from funciones import imprimir_patron, imprimir_patron_ascendente

def main():
    cant_filas = int(input("Ingresar cantidad de filas: "))
    imprimir_patron(cant_filas)
    imprimir_patron_ascendente(cant_filas)

if __name__ == '__main__':
    main()