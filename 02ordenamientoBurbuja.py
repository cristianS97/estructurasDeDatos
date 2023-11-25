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