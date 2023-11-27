"""
Cola:

Es una estructura de datos, caracterizada por ser una secuencia de elementos en la que la operación de inserción push
se realiza por un extremo y la operación de extracción pop por el otro. También se le llama estructura FIFO
(First In First Out), debido a que el primer elemento en entrar será también el primero en salir

Operaciones:
- Insertar
- Eliminar
- Buscar
- Estado de la cola (Vacía o con elementos)
- Retornar el elemento frontal
- Retornar el tamaño de la cola
"""
class Cola:
    def __init__(self):
        self.__lista = []

    def empty(self):
            return len(self.__lista) == 0

    def push(self, dato):
        self.__lista.append(dato)

    def pop(self):
        if self.empty():
            raise Exception("La cola esta vacía")
        dato = self.__lista[0]
        self.__lista = self.__lista[1:]
        return dato

    def show(self):
        for i, elemento in enumerate(self.__lista):
            print(f"({i})\t{elemento}")

    def front(self):
        if self.empty():
            raise Exception("La cola esta vacía")
        return self.__lista[0]

objCola = Cola()
objCola.push(1)
objCola.push(2)
objCola.push(3)
objCola.show()
print(objCola.front())
print(objCola.pop())
print(objCola.front())
objCola.show()
print(objCola.pop())
print(objCola.pop())