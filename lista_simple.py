class Node:
    def __init__(self, nombre = None, telefono = None, next = None):
        self.nombre = nombre
        self.telefono = telefono
        self.next = next

class lista_simple:
    def __init__(self):
        self.head = None

    def esta_vacia(self):
        return self.head == None

    def agregar_inicio(self, nombre, telefono):
        self.head = Node(nombre, telefono,self.head)

    def agregar_final(self, nombre, telefono):
        if not self.head:
            self.head = Node(nombre, telefono)
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = Node(nombre, telefono)

    def recorrer(self):
        if not self.head:
            print("Lista Vacia")
            return
        contador = 1
        temp = self.head
        while(temp.next):
            print("{0}) {1} -- {2}".format(contador, temp.nombre, temp.telefono))
            contador += 1
            temp = temp.next
        print("{0}) {1} -- {2}".format(contador, temp.nombre, temp.telefono))