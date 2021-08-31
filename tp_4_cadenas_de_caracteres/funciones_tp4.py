def separador_de_claves(clave_maestra):
    #ej 3
    #clave1 se constituye con los digitos en posiciones impares
    #clave2 se constituye con los digitos en posiciones pares
    clave1 = ""
    clave2 = ""
    for indice in range(len(clave_maestra)):
        if indice % 2 == 0:
            clave1 += clave_maestra[indice]
        else:
            clave2 += clave_maestra[indice]
    return clave1, clave2
