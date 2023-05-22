#2. Crear una función que se llame reemplazarCaracteres 
#que reciba una cadena de caracteres como primer parámetro, un carácter como segundo y otro carácter  como tercero,  
#la misma deberá reemplazar cada ocurrencia del segundo parámetro por el tercero 
#y devolver la cantidad de veces que se reemplazo ese carácter  en la cadena

def remplazar_caracteres(cadena:str, caracter_anterior:str, catarcer_remplazo:str)->str:
    contador_de_remplazos=0
    for i in cadena:
        if caracter_anterior == i:
            cadena.replace(i,catarcer_remplazo)
            contador_de_remplazos+=1
    print("la cadena nueva es" + cadena +" y se reemplazo "+str(contador_de_remplazos)+ " veces")

