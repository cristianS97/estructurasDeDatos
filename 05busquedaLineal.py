""""
Busqueda lineal

Funcionamiento:
- Recorrrer cada elemento de la lista
- Ir comparando el elemento que se desea con cada elemento de la lista
- En caso de ser encontrado, retornar el indice en el que se encuentra, en caso contrario retornar falso, none, etc
"""
def busquedaLineal(lista, dato):
    for i in range(len(lista)):
        if lista[i] == dato:
            return i
    return None

def buscar(lista, dato):
    indice = busquedaLineal(lista, dato)
    if not indice:
        return f"El dato {dato} no ha sido encontrado"
    return f"El dato {dato} ha sido encontrado en el indice {indice}"

lista = [12, 45, 78, 9, 6, 5, 4, 2, 1, 0, 12, 45, 78, 63, 25, 98]
print(lista)
print(buscar(lista, 22))
print(buscar(lista, 45))
