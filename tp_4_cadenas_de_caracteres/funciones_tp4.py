def chequear_capicua(string):
    #ej 1
    '''determina si una cadena es capicua'''
    es_capicua = False
    if string == string[::-1]:
        es_capicua = True

    return es_capicua
    
def centrar_string(string, ancho):
    #ej2
    ''' imprime una cadena de texto "string"
        centrada dentro de un "ancho" '''
    string_centrada = string.center(ancho)
    print(string_centrada)

    return string_centrada

def separador_de_claves(clave_maestra):
    #ej 3
    '''Extrae las claves 1 y 2 de la clave maestra'''
    clave1 = ""
    clave2 = ""
    for indice in range(len(clave_maestra)):
        if indice % 2 == 0:
            clave1 += clave_maestra[indice]
        else:
            clave2 += clave_maestra[indice]
    return clave1, clave2


def convertir_a_romano(numero):
    #ej 4
    simbolos = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    valores = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    romano = ""

    for i, valor in enumerate(valores):
        cant = numero // valores[i]
        romano += (simbolos[i] * cant)
        numero %= valor
    print(romano)

    return romano

def extraer_sub_cadena_con_slice(string, posicion, cantidad):
    #ej 6.a
    substring = string[posicion:posicion+cantidad]
    print(substring)

    return substring


def extraer_sub_cadena_sin_slice_v1(string, posicion, cantidad):
    #ej 6.b
    #desconforme con esta version, la v2 me parece mucho mas legible
    substring = ''
    suma = 0
    for _ in range(posicion, len(string)):
        substring += string[(posicion)+suma]
        suma += 1
        if suma == cantidad:
            break

    print(substring)

    return substring

def extraer_sub_cadena_sin_slice_v2(string, posicion, cantidad):
    #ej 6.2 v2
    substring = ''
    fin = posicion + cantidad if posicion + cantidad < len(string) else len(string) #oneliner para el if de abajo
    '''if posicion + cantidad < len(string):
        fin = posicion + cantidad
    else:
        fin = len(string)'''
    for i in range(posicion, fin):
        substring += string[i]

    print(substring)

    return substring

def eliminar_substring_con_slice(string, posicion, cantidad):
    #ej 7.a
    string_resultante = string[:posicion] + string[posicion+cantidad:]
    print(string_resultante)
    
    return string_resultante

def eliminar_substring_sin_slice(string, posicion, cantidad):
    #ej 7.b
    substring = ''
    for i in range(len(string)):
        if i < posicion or i >= posicion+cantidad:
            substring += string[i]
    print(substring)

    return substring

def ordenar_alfabeticamente(string):
    #ej 8
    '''casteamos el string a lista y luego hacemos un bubble sort, luego casteamos la lista a string nuevamente'''
    lista = list(string.split())
    for i in range(len(lista)): #recorremos el array
        for j in range(len(lista)-i-1): #magia
            if lista[j] > lista[j+1]: #si el elemento actual es mayor al siguiente
                lista[j], lista[j+1] = lista[j+1], lista[j] #los swapeamos
    nuevo_string = " ".join(lista)
    print(nuevo_string)

    return nuevo_string

def devolver_ultimos_n_chars_con_slice(string, cant_chars):
    #ej 9
    substring = string[cant_chars:]
    print(substring)

    return substring

def devolver_ultimos_n_chars_sin_slice(string, cant_chars):
    #ej 9 sin slices
    substring = ''
    for i in range(cant_chars, len(string)):
        substring += string[i]
    print(substring)

    return substring

def contar_letras_y_numeros(string):
    #ej 10
    numeros = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    cant_chars = 0
    cant_numeros = 0
    str_sin_espacios = string.replace(" ", "")
    for i in range(len(str_sin_espacios)):
        cant_chars += 1
        if str_sin_espacios[i] in  numeros:
            cant_numeros += 1
    cant_letras = cant_chars - cant_numeros

    print(f"Se ingresaron {cant_letras} letras y {cant_numeros} numeros")

    return f"Se ingresaron {cant_letras} letras y {cant_numeros} numeros"

def uppercaser(string):
    #ej 11
    string_mayuscula = string.title()
    string_final = string_mayuscula.replace(" ", "")
    print(string_final)

    return string_final

def reemplazador_de_palabras(string, palabra_a_reemplazar, reemplazar_por):
    #ej 12
    nuevo_string = string.replace(palabra_a_reemplazar, reemplazar_por)
    cant_reemplazos = 0

    for palabra in string.split():
        if palabra.lower() == palabra_a_reemplazar.lower():
            cant_reemplazos += 1

    print(nuevo_string)
    print("cantidad de reemplazos:", cant_reemplazos)

    return nuevo_string