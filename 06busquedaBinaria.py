""""
Busqueda binaria

Funcionamiento:
Buscar datos en una colección de datos

Ventajas:
Realiza menos comparaciones que la Busqueda lineal

Requisitos antes de realizar dicho algoritmo:
Tener la lista ordenada de manera ascendente

Algoritmo:
- Calcular el punto medio: (Izquierda + Derecha) / 2
- Comparar el punto medio con el dato a buscar
- Si es igual el dato al punto medio, devuelve el indice
- Si el dato a buscar es mayor al punto medio, izquierda es igual al valor del medio + 1
- Si el dato a buscar es menor al punto medio, derecha es igual al valor del medio - 1
- Se seguira ejecutando siempre y cuando Izquierda sea menor o igual a Derecha
"""
def busquedaBinaria(lista, dato):
    izquierda = 0
    derecha = len(lista)-1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == dato:
            return medio
        elif lista[medio] < dato:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return None

def buscar(lista, dato):
    indice = busquedaBinaria(lista, dato)
    if indice:
        print(f"El valor {dato} se encuentra en el indice {indice}")
    else:
        print(f"El valor {dato} no ha sido encontrado")

lista = [5, 12, 15, 30, 50, 65, 70, 87, 88, 96]
lista.sort()
buscar(lista, 12)
buscar(lista, 150)