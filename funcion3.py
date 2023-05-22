# #3. Crear una función que se llame ordenarCaracteres que reciba una cadena de caracteres como parámetro
#   y su responsabilidad es ordenar los caracteres de manera ascendente dentro de la cadena. 
# Ejemplo si le pasamos "algoritmo" la deja como "agilmoort"

def ordenar_cadenas(cadena:str)->str:
    for i in cadena:
        for j in cadena:
            if (i > j):
                aux = i
                i = j
                j = aux
    print (cadena)
