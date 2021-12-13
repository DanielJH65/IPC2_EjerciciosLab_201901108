from logica import logica

if __name__ == "__main__":
    opcion = 0
    l = logica()
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
            l.leer_archivo()
        elif opcion == 2:
            l.mostrar()
        elif opcion == 3:
            break
        else:
            print("Debe ingresar un valor válido")