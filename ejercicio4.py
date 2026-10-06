class Videojuego:
    def __init__(self, codigo, titulo, genero, plataforma, anio, horas_estimadas):
        self.codigo = codigo
        self.titulo = titulo
        self.genero = genero
        self.plataforma = plataforma
        self.anio = anio
        self.horas_estimadas = horas_estimadas

    def es_del_genero(self, genero):
        return self.genero.lower() == genero.strip().lower()

    def supera_horas(self, cantidad):
        return self.horas_estimadas > cantidad

    def mostrar_datos(self):
        print("----------------------------------")
        print(f"Codigo          : {self.codigo}")
        print(f"Titulo          : {self.titulo}")
        print(f"Genero          : {self.genero}")
        print(f"Plataforma      : {self.plataforma}")
        print(f"Anio            : {self.anio}")
        print(f"Horas estimadas : {self.horas_estimadas}")
        print("----------------------------------")


def crear_videojuegos():
    videojuegos = [
        Videojuego("VG-001", "LaLeyenda del Valle Perdido", "Aventura", "PC", 2018, 45),
        Videojuego("VG-002", "Mareas de Acero", "Estrategia", "PC", 2020, 120),
        Videojuego("VG-003", "Ritmo Cosmico", "Plataformas", "Switch", 2021, 12),
        Videojuego("VG-004", "Guardianes del Bosque", "Aventura", "PlayStation", 2017, 60),
        Videojuego("VG-005", "Torneo de Leyendas", "Deportes", "Xbox", 2022, 30),
        Videojuego("VG-006", "El Enigma de Kepler", "Misterio", "PC", 2019, 25),
        Videojuego("VG-007", "Batalla Estelar: Episodio II", "Estrategia", "PlayStation", 2023, 95),
        Videojuego("VG-008", "Ciudad Neon", "Carreras", "Switch", 2020, 18),
        Videojuego("VG-009", "Sombra del Norte", "Terror", "PC", 2016, 22),
        Videojuego("VG-010", "Feria de Talentos", "Deportes", "Switch", 2019, 40),
    ]
    return videojuegos


def buscar_por_codigo(lista_videojuegos, codigo):
    juego_encontrado = None
    for juego in lista_videojuegos:
        if juego.codigo.lower() == codigo.strip().lower():
            juego_encontrado = juego
            break
    return juego_encontrado


def pedir_texto(mensaje):
    while True:
        dato = input(mensaje).strip()
        if dato != "":
            return dato
        print("Debe ingresar al menos un dato.")


def pedir_entero(mensaje):
    while True:
        dato = input(mensaje).strip()
        try:
            return int(dato)
        except ValueError:
            print("Debe ingresar un numero entero valido.")


def mostrar_fila(juego, numero):
    print(f"[{numero}] {juego.codigo} - {juego.titulo}")
    print(f"      Genero: {juego.genero} | Plataforma: {juego.plataforma} | Anio: {juego.anio} | Horas: {juego.horas_estimadas}")


def consultar_por_genero(lista_videojuegos):
    genero = pedir_texto("Ingrese el genero a consultar: ")
    print("")
    print(f'VIDEOJUEGOS DEL GENERO: "{genero}"')
    print("")

    cantidad = 0
    for juego in lista_videojuegos:
        if juego.es_del_genero(genero):
            cantidad = cantidad + 1
            mostrar_fila(juego, cantidad)

    print("")
    if cantidad == 0:
        print(f'No se encontraron videojuegos del genero "{genero}".')
        return
    print(f"Cantidad de videojuegos encontrados: {cantidad}")


def consultar_por_horas(lista_videojuegos):
    horas = pedir_entero("Ingrese la cantidad de horas a superar: ")
    print("")
    print(f"VIDEOJUEGOS QUE SUPERAN LAS {horas} HORAS")
    print("")

    cantidad = 0
    for juego in lista_videojuegos:
        if juego.supera_horas(horas):
            cantidad = cantidad + 1
            mostrar_fila(juego, cantidad)

    print("")
    if cantidad == 0:
        print(f"Ningun videojuego supera las {horas} horas estimadas.")
        return
    print(f"Cantidad de videojuegos que superan las {horas} horas: {cantidad}")


def consultar_por_codigo(lista_videojuegos):
    codigo = pedir_texto("Ingrese el codigo del videojuego: ")
    juego = buscar_por_codigo(lista_videojuegos, codigo)
    print("")
    if juego is None:
        print("Videojuego no encontrado")
    else:
        juego.mostrar_datos()


def main():
    lista_videojuegos = crear_videojuegos()

    print("=== CATALOGO DE VIDEOJUEGOS ===")
    print(f"Videojuegos cargados: {len(lista_videojuegos)}")
    print("")

    consultar_por_genero(lista_videojuegos)
    consultar_por_horas(lista_videojuegos)
    consultar_por_codigo(lista_videojuegos)


main()