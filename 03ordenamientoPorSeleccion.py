"""
Método de ordenamiento por selección

Es un algoritmo que consiste en ordenar los elementos de manera ascendente o descendente

Funcionamiento:
- Busca el dato mas pequeño de la lista
- Lo intercambia por el actual
- Sigue buscando el dato mas pequeño de la lista
- Lo intercambia por el actual
- Esto se repetira hasta recorrer todas las posiciones
"""
lista = [4, 2, 6, 8, 5, 7, 0]

for i in range(len(lista)):
    minimo = i
    for j in range(i, len(lista)):
        if lista[j] < lista[minimo]:
            minimo = j
    aux = lista[i]
    lista[i] = lista[minimo]
    lista[minimo] = aux

print(lista)