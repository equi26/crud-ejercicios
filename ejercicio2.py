class RecursoDigital:
    def __init__(self, codigo, titulo, categoria, autor, anio, disponible):
        self.codigo = codigo
        self.titulo = titulo
        self.categoria = categoria
        self.autor = autor
        self.anio = anio
        self.disponible = disponible

    def mostrar_resumen(self):
        estado = "Disponible" if self.disponible else "Prestado"
        print("----------------------------------")
        print(f"Codigo      : {self.codigo}")
        print(f"Titulo      : {self.titulo}")
        print(f"Categoria   : {self.categoria}")
        print(f"Disponibilidad: {estado}")
        print("----------------------------------")

    def coincide_con(self, texto):
        return texto in self.titulo.lower()


def crear_recursos():
    recursos = [
        RecursoDigital("LIB-001", "Introduccion a la programacion con Python", "Libro digital", "Ana Gomez", 2021, True),
        RecursoDigital("LIB-002", "Algoritmos y estructuras de datos", "Libro digital", "Luis Fernandez", 2019, False),
        RecursoDigital("TUT-001", "Tutorial de Python desde cero", "Tutorial", "Carlos Diaz", 2022, True),
        RecursoDigital("TUT-002", "Taller de bases de datos relacionales", "Tutorial", "Marta Ruiz", 2020, True),
        RecursoDigital("MAN-001", "Manual de uso del laboratorio de informatica", "Manual", "Instituto Tecnico", 2018, False),
        RecursoDigital("MAN-002", "Manual de seguridad e higiene en los espacios tecnologicos", "Manual", "Instituto Tecnico", 2023, True),
        RecursoDigital("REV-001", "Revista de novedades en inteligencia artificial", "Revista", "Redaccion Central", 2024, True),
        RecursoDigital("REV-002", "Revista de educacion digital e inclusion", "Revista", "Redaccion Central", 2022, False),
        RecursoDigital("VID-001", "Video curso: Python basico en 2 horas", "Video educativo", "Diego Sosa", 2021, True),
        RecursoDigital("VID-002", "Video curso: Redes y mantenimiento de equipos", "Video educativo", "Nico Peralta", 2019, True),
        RecursoDigital("VID-003", "Video: guia rapida de Excel para el aula", "Video educativo", "Roja Benitez", 2024, False),
        RecursoDigital("LIB-003", "Programacion web con HTML, CSS y JavaScript", "Libro digital", "Tomas Vega", 2020, True),
    ]
    return recursos


def normalizar(texto):
    return texto.strip().lower()


def buscar_por_titulo(lista_recursos, texto):
    coincidencias = []
    palabra = normalizar(texto)
    if palabra == "":
        return coincidencias
    for recurso in lista_recursos:
        if palabra in normalizar(recurso.titulo):
            coincidencias.append(recurso)
    return coincidencias


def contar_disponibles(lista_recursos):
    cantidad = 0
    for recurso in lista_recursos:
        if recurso.disponible:
            cantidad = cantidad + 1
    return cantidad


def mostrar_coincidencias(coincidencias):
    for recurso in coincidencias:
        recurso.mostrar_resumen()
        if recurso.disponible:
            print(">> Se encuentra DISPONIBLE para préstamo")
        else:
            print(">> NO se encuentra disponible (prestado)")
        print("")


def pedir_texto(mensaje):
    while True:
        dato = input(mensaje).strip()
        if dato != "":
            return dato
        print("Debe ingresar al menos una palabra.")


def mostrar_busqueda(lista_recursos):
    texto = pedir_texto("Ingrese una palabra o parte de un titulo: ")
    coincidencias = buscar_por_titulo(lista_recursos, texto)

    print("")
    print(f'RESULTADOS PARA: "{texto}"')
    print("")

    if len(coincidencias) == 0:
        print("No se encontraron coincidencias con ese texto.")
        return

    mostrar_coincidencias(coincidencias)

    total = len(coincidencias)
    disponibles = contar_disponibles(coincidencias)
    print(f"Cantidad total de coincidencias: {total}")
    print(f"Coincidencias disponibles: {disponibles}")
    print(f"Coincidencias no disponibles: {total - disponibles}")


def main():
    lista_recursos = crear_recursos()

    print("=== BIBLIOTECA MULTIMEDIA - BUSQUEDA FLEXIBLE ===")
    print(f"Recursos cargados en el catalogo: {len(lista_recursos)}")
    print("")

    mostrar_busqueda(lista_recursos)


main()