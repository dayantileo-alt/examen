def mostrar_menu():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Copias por género")
    print("2. Búsqueda de libros por rango de multa")
    print("3. Actualizar multa de libro")
    print("4. Agregar libro")
    print("5. Eliminar libro")
    print("6.Salir")
    print("=====================================")

def leer_opcion():
    try:
        opcion = int(input("Ingrese una opcion: "))
        return opcion
    except ValueError:
        return -1
    
def validar_titulo(titulo_libro):
    return len(titulo_libro.strip()) >0

def validar_autor(nombre):
    return len(nombre.strip()) >0

def validar_genero(genero_literario):
    return len(genero_literario.strip()) >0

def validar_anio(año_publicado):
    anio = int(año_publicado)
    return  0 <= anio

def validar_editorial(editorial):
    return len(editorial.strip()) >0

def copias_genero(genero):
    return genero
def agregar_libro(lista_libros):
    print("\n---- Agregar Libro------")
    titulo = input("ingrese nombre del titulo del libro ")
    autor = input("ingrese el nombre del autor del libro ")
    anio = input("ingrese el año del libro")
    copia = input("ingrese, cuantas copías desea ")

    if not validar_titulo(titulo):
        print("Error: el nombre no puede estar vacio ")
        return
    if not validar_autor(autor):
        print("Error: el nombre del autor no puede estar vacio. ")
        return
    if not validar_anio(anio):
        print("Error: tiene que ser numero entero entre 1800 - 2026")
        return
 

    

    lista_libros.append()
    print("libro ingresado exitosamente. ")

def localizar_libro(lista_libros, buscar):
    for i in range(len(lista_libros)):
        if lista_libros[i]["titulo"].lower() == buscar.strip().lower():
            return i
    return -1

def actualizar_estados(lista_libros):
    for libro in lista_libros:
        if libro["copias"]  == 0:
            libro["agotado"] = True
        else:
            libro["agotado"] = False
    


    



