# 1. Crear una función llamada aplicarAumento que reciba como parámetro el precio de un producto
# y devuelva el valor del producto con un aumento del 5%. Realizar la llamada desde el main.

def aumentar_precio(precio:float)->float: #recive un valor y le aumenta un 5%, 
    aumento=precio+(precio*5/100)
    return aumento