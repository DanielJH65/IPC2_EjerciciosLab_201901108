class Node:
    def __init__(self, nombre = None, apellido = None, telefono = None, next = None):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.next = next

class lista_simple:
    def __init__(self):
        self.head = None

    def esta_vacia(self):
        return self.head == None

    def agregar_inicio(self, nombre, apellido, telefono):
        self.head = Node(nombre, apellido, telefono, self.head)

    def agregar_final(self, nombre, apellido, telefono):
        if not self.head:
            self.head = Node(nombre, apellido, telefono)
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = Node(nombre, apellido, telefono)

    def agregar_cualquier(self, nombre, apellido, telefono, posicion):
        temp = self.buscar(posicion)
        if posicion != 0:            
            temp2 = self.buscar(posicion -1)
            temp3 = Node(nombre, apellido, telefono, temp)
            temp2.next = temp3
        if posicion == 0:
            self.head = Node(nombre, apellido, telefono, self.head)


    def recorrer(self):
        if not self.head:
            print("Lista Vacia")
            return
        contador = 1
        temp = self.head
        while(temp.next):
            print("{0}) {1} {3} -- {2}".format(contador, temp.nombre, temp.telefono, temp.apellido))
            contador += 1
            temp = temp.next
        print("{0}) {1} {3} -- {2}".format(contador, temp.nombre, temp.telefono, temp.apellido))

    def tamanio(self):
        if self.esta_vacia():
            return 0
        else:
            tamanio = 1
            temp = self.head
            while temp.next:
                temp = temp.next
                tamanio += 1
            return tamanio
    
    def buscar(self, posicion):
        if posicion < 0 or posicion > self.tamanio()-1:
            print("Valor fuera de rango")
        elif self.esta_vacia():
            print("Lista Vacia")
        else:
            temp = self.head
            for i in range(posicion):
                temp = temp.next
            return temp

    def __getitem__(self, posicion):
        temp = self.buscar(posicion)
        if temp != None:
            return temp if temp != None else None