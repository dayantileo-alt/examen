import validacion_biblioteca as lbrs

def main():
    libros = []
    while True:
        lbrs.mostrar_menu()
        opcion = lbrs.leer_opcion()

        if opcion == 1:
            (libros)

        elif opcion == 2:
            print("\n----Buscar libro----")
            busqueda = input("ingresa el nombre del libro: ")
            posicion = (libros, busqueda)

            if posicion != -1:
                libro = libros[posicion]
                print(f"titulo: {libro['titulo']}")
                print(F"autor: {libro['autor']}")
                print(f"año: {libro['año']}")
                print(f"copias: {libro['copias']}")
                print(f"agotado:{'SI' if libro['agotado'] else 'NO'}")
            else:
                print(f"El libro '{busqueda}' no se encuentra registrado.  ")
        
        elif opcion == 3:
            print("\n ---Eliminar Libro----")
            eliminar = input("Ingrese el nombre del libro a eliminar ")
            posicion =  (libros,eliminar)
            
            if posicion != -1:
                libros.pop(posicion)
                print(f"El Libro a sido {eliminar} eliminado exitosamente")
            else:
                print(f"El Libro {eliminar} no se enceuntra registrado. ")

        elif opcion == 4:
            
            print("Estado Actualizado ")

        elif opcion == 5:
            print("\n -----LISTA DE LIBROS-----")
            if not libros:
                print("No hay libros registrados ")
        
              

        elif opcion == 6:
            print("Saliendo del sistema")
            break
        else:
            print("Opcion invalida, intente nuevamente. ")


       


if __name__ == "__amin__":
    main()



