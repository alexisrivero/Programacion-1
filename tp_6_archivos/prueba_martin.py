def leer(archivo):
    lineas=[]
    with open(archivo,'r', encoding='utf-8') as tarea:
        for linea in tarea:
            lineas.append(linea[:])

    print(lineas)
    return(lineas)


def main():
   fin = leer('clase_10.py')

if __name__ == '__main__':
    main()
