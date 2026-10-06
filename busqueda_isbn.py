biblioteca = [
    {"isbn": "978-950-0001-1", "titulo": "El nombre de la rosa", "autor": "Umberto Eco", "disponible": True},
    {"isbn": "978-950-0002-2", "titulo": "Cien anos de soledad", "autor": "Gabriel Garcia Marquez", "disponible": False},
    {"isbn": "978-950-0003-3", "titulo": "Ficciones", "autor": "Jorge Luis Borges", "disponible": True},
    {"isbn": "978-950-0004-4", "titulo": "Rayuela", "autor": "Julio Cortazar", "disponible": False},
    {"isbn": "978-950-0005-5", "titulo": "Pedro Paramo", "autor": "Juan Rulfo", "disponible": True},
]


def buscar_con_return(catalogo, isbn_buscado):
    for libro in catalogo:
        if libro["isbn"] == isbn_buscado:
            return libro
    return None


def buscar_con_bandera(catalogo, isbn_buscado):
    encontrado = None
    for libro in catalogo:
        if libro["isbn"] == isbn_buscado:
            encontrado = libro
            break
    return encontrado


def imprimir_resultado(resultado):
    if resultado is None:
        print("Libro no encontrado")
        return
    estado = "disponible para préstamo" if resultado["disponible"] else "no disponible (prestado)"
    print("Libro encontrado:")
    print(f"  ISBN: {resultado['isbn']}")
    print(f"  Titulo: {resultado['titulo']}")
    print(f"  Autor: {resultado['autor']}")
    print(f"  Estado: {estado}")


def version_incorrecta(catalogo, isbn_buscado):
    for libro in catalogo:
        if libro["isbn"] == isbn_buscado:
            print("Libro encontrado:")
            print(f"  {libro['titulo']} - {libro['autor']}")
            return
        else:
            print("Libro no encontrado")


print("=== VERSION INCORRECTA (el else pertenece al for, no al if) ===")
isbn = input("Ingrese el ISBN a buscar: ").strip()
version_incorrecta(biblioteca, isbn)

print("\n=== VERSION CORREGIDA (con return) ===")
resultado = buscar_con_return(biblioteca, isbn)
imprimir_resultado(resultado)

print("\n=== VERSION CORREGIDA (con variable booleana) ===")
resultado = buscar_con_bandera(biblioteca, isbn)
imprimir_resultado(resultado)