"""
Método de ordenamiento burbuja

Revisa cada elemento de la lista con el siguiente elemento, intercambiandolos de posición
si están en el orden equivocado
"""
lista = [4, 2, 6, 8, 5, 7]

# Menor a mayor
for i in range(len(lista)):
    for j in range(len(lista)-1):
        if lista[j] > lista[j+1]:
            temp = lista[j+1]
            lista[j+1] = lista[j]
            lista[j] = temp

print(lista)

lista = [4, 2, 6, 8, 5, 7]

# Mayor a menor
for i in range(len(lista)):
    for j in range(len(lista)-1):
        if lista[j] < lista[j+1]:
            temp = lista[j+1]
            lista[j+1] = lista[j]
            lista[j] = temp

print(lista)