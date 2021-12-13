from tkinter.constants import CHAR
from lista_simple import lista_simple
from tkinter import messagebox, filedialog
import xml.etree.ElementTree as ET
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