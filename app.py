from lista_simple import lista_simple

if __name__ == "__main__":
    opcion = 0
    nums = lista_simple()
    while(opcion != 3):
        try:
            opcion = int(input("""
###############--Menú--###############
#                                    #
#   Elija una opción:                #
#   1) Ingresar Datos                #
#   2) Mostrar Datos                 #
#   3) Salir                         #
#                                    # 
######################################  
    """))
        except:
            print("Debe ingresar un valor válido")

        if opcion == 1:
            nombre = input("Ingrese el nombre: \n")
            telefono = input("ingrese el número de teléfono: \n")
            nums.agregar_final(nombre, telefono)
        elif opcion == 2:
            nums.recorrer()
        elif opcion == 3:
            break
        else:
            print("Debe ingresar un valor válido")