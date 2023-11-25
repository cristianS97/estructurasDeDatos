"""
Método de ordenamiento por inserción

Funcionamiento:
- Recorremos cada elemento de la lista
- Cada elemento de la lista se ordena si a su izquierda tiene un elemento mayor que el actual
- Si es correcto el paso anterior, se hace el intercambio de valores
- El elemento se sigue recorriendo hacia la izquierda hasta que tenga un elemento mayor que el
"""
lista = [5, 10, 3, 12, 10, 6]

for i in range(1, len(lista)):
    aux = lista[i]
    j = i - 1
    while j >= 0:
        if aux < lista[j]:
            lista[j + 1] = lista[j]
            lista[j] = aux
        j -= 1
print(lista)