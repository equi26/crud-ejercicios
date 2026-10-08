# Definición de la clase que representa cada recurso digital (libros, tutoriales, revistas, videos, etc.)
class RecursoDigital:
    def __init__(self, codigo, titulo, categoria, autor, anio, disponible):
        # Inicialización de los atributos de la instancia
        self.codigo = codigo          # Código identificador único (ej: LIB-001)
        self.titulo = titulo          # Título del recurso
        self.categoria = categoria    # Categoría (Libro digital, Tutorial, Manual, Revista, Video)
        self.autor = autor            # Nombre del autor o entidad creadora
        self.anio = anio              # Año de publicación
        self.disponible = disponible  # Booleano: True si está disponible, False si está prestado

    # Método para imprimir en pantalla un resumen formateado de la información del recurso
    def mostrar_resumen(self):
        estado = "Disponible" if self.disponible else "Prestado"
        print("----------------------------------")
        print(f"Codigo      : {self.codigo}")
        print(f"Titulo      : {self.titulo}")
        print(f"Categoria   : {self.categoria}")
        print(f"Disponibilidad: {estado}")
        print("----------------------------------")

    # Método auxiliar para verificar si un texto está contenido dentro del título del recurso
    def coincide_con(self, texto):
        return texto in self.titulo.lower()


# Función para inicializar y retornar la lista con el catálogo de recursos digitales
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
        # Nuevos libros agregados al catálogo:
        RecursoDigital("LIB-004", "Harry Potter y la piedra filosofal", "Libro digital", "J.K. Rowling", 1997, True),
        RecursoDigital("LIB-005", "El Senor de los Anillos: La Comunidad del Anillo", "Libro digital", "J.R.R. Tolkien", 1954, True),
    ]
    return recursos


# Función de utilidad para limpiar espacios innecesarios y convertir el texto a minúsculas
def normalizar(texto):
    return texto.strip().lower()


# Función para buscar recursos en la lista cuyo título contenga la palabra o texto ingresado
def buscar_por_titulo(lista_recursos, texto):
    coincidencias = []
    palabra = normalizar(texto)
    
    # Si la palabra de búsqueda está vacía, no se retorna ninguna coincidencia
    if palabra == "":
        return coincidencias
        
    # Recorre la lista de recursos y agrega los que coinciden
    for recurso in lista_recursos:
        if palabra in normalizar(recurso.titulo):
            coincidencias.append(recurso)
            
    return coincidencias


# Función auxiliar para contar cuántos recursos de una lista están marcados como disponibles
def contar_disponibles(lista_recursos):
    cantidad = 0
    for recurso in lista_recursos:
        if recurso.disponible:
            cantidad = cantidad + 1
    return cantidad


# Función para iterar sobre una lista de coincidencias y mostrar el detalle de cada una en pantalla
def mostrar_coincidencias(coincidencias):
    for recurso in coincidencias:
        recurso.mostrar_resumen()
        if recurso.disponible:
            print(">> Se encuentra DISPONIBLE para préstamo")
        else:
            print(">> NO se encuentra disponible (prestado)")
        print("")


# Función para solicitar la entrada de datos al usuario y validar que no envíe un texto vacío
def pedir_texto(mensaje):
    while True:
        dato = input(mensaje).strip()
        if dato != "":
            return dato
        print("Debe ingresar al menos una palabra.")


# Función principal de búsqueda: solicita el término al usuario, realiza la búsqueda y muestra los resultados y estadísticas
def mostrar_busqueda(lista_recursos):
    texto = pedir_texto("Ingrese una palabra o parte de un titulo: ")
    coincidencias = buscar_por_titulo(lista_recursos, texto)

    print("")
    print(f'RESULTADOS PARA: "{texto}"')
    print("")

    if len(coincidencias) == 0:
        print("No se encontraron coincidencias con ese texto.")
        return

    # Muestra el detalle de cada recurso encontrado
    mostrar_coincidencias(coincidencias)

    # Cálculo y visualización de totales
    total = len(coincidencias)
    disponibles = contar_disponibles(coincidencias)
    print(f"Cantidad total de coincidencias: {total}")
    print(f"Coincidencias disponibles: {disponibles}")
    print(f"Coincidencias no disponibles: {total - disponibles}")


# Punto de entrada del programa
def main():
    # Se carga el catálogo completo de recursos
    lista_recursos = crear_recursos()

    print("=== BIBLIOTECA MULTIMEDIA - BUSQUEDA FLEXIBLE ===")
    print(f"Recursos cargados en el catalogo: {len(lista_recursos)}")
    print("")

    # Se inicia el flujo de búsqueda de la aplicación
    mostrar_busqueda(lista_recursos)


# Ejecución de la función principal
main()