"""
Listas enlazadas

Las listas enlazadas son estructuras de datos semejantes a los arrays (Arreglos o listas en python) salvo que el acceso
a un elemento no se hace mediante un indice sino mediante un puntero

Lista enlazada simple

La lista enlazada básica es la lista enlazada simple la cual tiene un enlace por nodo, este enlace apunta al siguiente
nodo en la lista o al valor null o None si es el último nodo
"""
from pyfiglet import Figlet

objFiglet = Figlet(font='slant')

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class ListaEnlazada:
    def __init__(self):
        self.primero = None
        self.siguiente = None

    def empty(self):
        return not self.primero

    def agregar_ultimo(self, dato):
        if self.empty():
            self.primero = Node(dato)
            self.siguiente = self.primero
        else:
            aux = Node(dato)
            self.siguiente.next = aux
            self.siguiente = aux

    def elimina_ultimo(self):
        aux = self.primero
        while aux.next != self.siguiente:
            aux = aux.next
        aux.siguiente = None
        self.siguiente = aux

    def agregar_inicio(self, dato):
        if self.empty():
            self.primero = Node(dato)
            self.siguiente = self.primero
        else:
            aux = Node(dato)
            aux.next = self.primero
            self.primero = aux

    def eliminar_inicio(self):
        self.primero = self.primero.next

    def recorrido(self):
        aux = self.primero
        while aux:
            print(aux.val)
            aux = aux.next

objListaEnlazada = ListaEnlazada()
objListaEnlazada.agregar_ultimo(1)
objListaEnlazada.agregar_ultimo(2)
objListaEnlazada.agregar_ultimo(4)
objListaEnlazada.agregar_ultimo(3)
objListaEnlazada.agregar_ultimo(4)
objListaEnlazada.agregar_ultimo(5)
print(objFiglet.renderText('Recorrido 1'))
objListaEnlazada.recorrido()
objListaEnlazada.elimina_ultimo()
print(objFiglet.renderText('Recorrido 2'))
objListaEnlazada.recorrido()
print(objFiglet.renderText('Primero'))
print(objListaEnlazada.primero)
print(objListaEnlazada.primero.val)
print(objListaEnlazada.primero.next)
print(objFiglet.renderText('Siguiente'))
print(objListaEnlazada.siguiente)
print(objListaEnlazada.siguiente.val)
print(objListaEnlazada.siguiente.next)
print(objFiglet.renderText('Recorrido 3'))
objListaEnlazada.agregar_inicio(0)
objListaEnlazada.agregar_ultimo(6)
objListaEnlazada.recorrido()
print(objFiglet.renderText('Recorrido 4'))
objListaEnlazada.eliminar_inicio()
objListaEnlazada.recorrido()
