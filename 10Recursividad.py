"""
Recursividad: Es una función que se llama a si misma
Ejemplo: Factorial de 4 -> 4! = 4 * 3 * 2 * 1
"""
def factorial(num):
    if num > 1:
        return num * factorial(num - 1)
    return num

def suma_arreglo(arreglo):
    if len(arreglo) == 1:
        return arreglo[0]
    return arreglo[0] + suma_arreglo(arreglo[1:])

print(factorial(4))
print(suma_arreglo([1, 2, 3, 4]))