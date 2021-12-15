from tkinter.constants import CHAR
from lista_simple import lista_simple
from tkinter import messagebox, filedialog
import xml.etree.ElementTree as ET
from os import system
class logica:

    def __init__(self):
        self.contactos = lista_simple()

    def leer_archivo(self):
        try:
            ruta = filedialog.askopenfilename(defaultextension = ".xml")
            tree = ET.parse(ruta)
            root = tree.getroot()
            
            for contacto in root:
                estado = True
                telefono = contacto[0].text
                nombre = contacto[1].text
                apellido = contacto[2].text
                a = self.contactos.tamanio()
                val_pos = 0
                for i in range(a):
                    if self.contactos[i].telefono == telefono:
                        messagebox.showerror("numero", "El numero {0} ya existe en la agenda".format(telefono))
                        estado = False
                    if apellido > self.contactos[i].apellido:
                        val_pos += 1

                if estado:
                    if val_pos >= self.contactos.tamanio():
                        self.contactos.agregar_final(nombre, apellido, telefono)
                    else:    
                        self.contactos.agregar_cualquier(nombre, apellido, telefono, val_pos)

            messagebox.showinfo("Archivo","Archivo leído exitosamente")

        except Exception as err:
            messagebox.showerror("Archivo", "Error al abrir el archivo")
            print(err)
    
    def mostrar(self):
        self.contactos.recorrer()

    def grafica(self):
        try:
            grafica_canciones = """
            digraph grid{
                node[shape = circle]
                rankdir="LR"
            """
            for i in range(self.contactos.tamanio()):
                grafica_canciones+="{0}[label=\"{1} {2}\n{0}\"];\n".format(self.contactos[i].telefono, self.contactos[i].nombre, self.contactos[i].apellido)
                if i != 0:
                    grafica_canciones+="{0} -> {1};\n".format(self.contactos[i-1].telefono,self.contactos[i].telefono)
            
            grafica_canciones += "}"

            archivo_grafica = open('grafica.dot', 'w')
            archivo_grafica.write(grafica_canciones)
            archivo_grafica.close()

            system('dot -Tpdf grafica.dot -o grafica.pdf')
            system('evince grafica.pdf')
            return

            messagebox.showinfo("Archivo","Archivo creado exitosamente")
        except Exception as err:
            messagebox.showerror("Archivo", "Error al crear el archivo")
            print(err)