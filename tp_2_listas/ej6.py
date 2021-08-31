"""
Eliminar de una lista de palabras las palabras que se encuentren en una segundalista.
Imprimir la lista original, la lista de palabras a eliminar y la lista resultante.
"""
from funciones_listas import superposicion_palabras

def main():
    superposicion_palabras(["diego", "barrientos", "trevisan"], ["trevisan", "barrientos"])

if __name__ == '__main__':
    main()