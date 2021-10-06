"""Desarrollar un programa para eliminar todos los comentarios de un programa escrito en lenguaje Python. 
Tener en cuenta que los comentarios comienzan con el signo # (siempre que éste no se encuentre encerrado entre comillas simples o dobles)
y que también se considera comentario a las cadenas de documentación(docstrings)."""

"""
r -> solo lectura, si no existe da error
w -> escritura, si existe lo sobreescribe, si no existe lo crea
a -> agregar, agrega al final del archivo, si no existe lo crea
x -> crear, si existe da error
"""
"""prueba = "0001Cliente 1"

slice = prueba[0:4]
slice2 = prueba[4:]

print(slice)
print(slice2)"""

def leer_archivo(nombre_archivo):
    lista = []
    with open(nombre_archivo, "r", encoding='utf-8') as arch:
        for linea in arch:
            lista.append(linea[:])
    
    print(lista)
    return lista


def eliminar_comentarios(lista):
    nuevos_str = []
    for linea in lista:
        if "#" in linea:
            continue
        else:
            nuevos_str.append(linea)
    
    print("nuevos: ", nuevos_str)
    return nuevos_str

def generar_archivo(lista):
    with open("archivo_generado.py", "w", encoding="utf-8") as arch:
        for linea in range(len(lista)):
            arch.write(lista[linea])

def main():
    leer = leer_archivo("prueba.py")
    elim_comment = eliminar_comentarios(leer) 
    generar_archivo(elim_comment)


if __name__ == "__main__":
    main()