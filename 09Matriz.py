"""
Matriz 5x5
                  Columnas
                0 1 2 3 4 5
             0| 1 2 3 4 5 6 |
             1| 8 1 2 8 9 5 |
Filas        2| 9 7 8 5 4 2 |
             3| 4 5 6 2 1 5 |
             4| 5 4 6 2 0 3 |
"""
matriz = [
    [1, 2, 3, 4, 5, 6],
    [8, 1, 2, 8, 9, 5],
    [9, 7, 8, 5, 4, 2],
    [4, 5, 6, 2, 1, 5],
    [5, 4, 6, 2, 0, 3]
]

print(matriz)

print('Impresión matriz')
for fila in matriz:
    print(fila)

print('Elemento particular:', matriz[0][3])

print("Matriz dinamica")
filas, columnas = 2, 3
matriz_dinamica = []
for i in range(filas):
    fila = []
    for j in range(columnas):
        fila.append(None)
    matriz_dinamica.append(fila)
print(matriz_dinamica)

print("Matriz con comprension de listas")
matriz_comprension = [list(range(columnas)) for i in range(filas)]
print(matriz_comprension)
