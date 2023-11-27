"""
Pila:

Una pila es una lista ordenada o estructura de datos en la que el modo de acceso a sus elementos es de tipo LIFO
(Last In First Out) que permite almacenar datos

Para el manejo de los datos se cuenta con dos operaciones básicas: Apilar(push), que coloca un objeto en la pila,
y su operaci[on inversa, retirar (o desapilar, pop), que retira el último elemento apilado

Operaciones:
Crear: Se crea una pila vacía (constructor)
Tamaño: Regresa el número de elementos de la pila (size)
Apilar: Se añade un elemento a la pila (push)
Desapilar: Se elemina el elemento frontal de la pila (pop)
Cima: Devuelve el elemento que esta en la cima de al pila (top o peek)
Vacía: Devuelve True si la pila esta sin elementos o False en caso de que contenga elementos (empty)

Las pilas pueden ser de tamaño estatico o dinamico, se pueden implementar en listas, arreglos, colecciones de datos
o en listas enlazadas
"""
class Pila:
    def __init__(self):
        self.__lista = []

    def empty(self):
        return len(self.__lista) == 0

    def push(self, dato):
        self.__lista.append(dato)

    def pop(self):
        if self.empty():
            raise Exception("La lista no tiene elementos")
        return self.__lista.pop()

    def size(self):
        return len(self.__lista)

    def seek(self):
        return self.__lista[len(self.__lista) - 1]

    def show(self):
        for i, elemento in enumerate(self.__lista[::-1]):
            print(f"({i})\t{elemento}")

objPila = Pila()
objPila.push(1)
objPila.push(2)
objPila.push(3)
objPila.push(4)
objPila.push(5)
objPila.push(6)
objPila.show()
print(objPila.pop())
objPila.show()