class Reparacion:
    def __init__(self, orden, cliente, equipo, falla, estado, tecnico, costo_estimado):
        self.orden = orden
        self.cliente = cliente
        self.equipo = equipo
        self.falla = falla
        self.estado = estado
        self.tecnico = tecnico
        self.costo_estimado = costo_estimado

    def mostrar_datos(self):
        print("----------------------------------")
        print(f"Orden          : {self.orden}")
        print(f"Cliente        : {self.cliente}")
        print(f"Equipo         : {self.equipo}")
        print(f"Falla          : {self.falla}")
        print(f"Estado         : {self.estado}")
        print(f"Tecnico        : {self.tecnico}")
        print(f"Costo estimado : ${self.costo_estimado:.2f}")
        print("----------------------------------")


def crear_reparaciones():
    reparaciones = [
        Reparacion(501, "Luna Fernandez", "Notebook Lenovo ThinkPad", "No enciende el equipo al conectar el cargador", "En reparacion", "Diego Sosa", 8500.0),
        Reparacion(502, "Marta Ruiz", "Monitor Samsung 24\"", "Pantalla con manchas y parpadeo constante", "Pendiente", "Diego Sosa", 6200.5),
        Reparacion(503, "Nico Peralta", "Impresora HP LaserJet", "Imprime en blanco y se traba el papel", "Entregado", "Carla Medina", 3400.0),
        Reparacion(504, "Roja Benitez", "Celular Motorola G54", "Bateria se descarga de forma repentina", "En reparacion", "Carla Medina", 9800.0),
        Reparacion(505, "Tomas Vega", "PC de escritorio AMD", "No detecta el disco duro interno", "Listo para entrega", "Ivan Lopez", 11200.75),
        Reparacion(506, "Carla Medina", "Tablet Samsung Galaxy Tab", "Puerto de carga suelto", "Pendiente", "Ivan Lopez", 4500.0),
        Reparacion(507, "Sonia Nunez", "Notebook Acer Aspire", "Tecla M y barra espaciadora sin respuesta", "En reparacion", "Roja Benitez", 7200.0),
        Reparacion(508, "Luna Fernandez", "Router TP-Link", "Se reinicia solo cada pocos minutos", "Listo para entrega", "Roja Benitez", 2800.0),
        Reparacion(509, "Diego Sosa", "Disco externo Seagate", "No lo reconoce la computadora", "Pendiente", "Carla Medina", 3900.25),
        Reparacion(510, "Roja Benitez", "Proyector Epson", "Imagen desenfocada y sin color", "Entregado", "Ivan Lopez", 5600.0),
        Reparacion(511, "Marta Ruiz", "Notebook Lenovo ThinkPad", "Ventilador muy ruidoso y sobrecalentamiento", "En reparacion", "Carla Medina", 6700.5),
        Reparacion(512, "Nico Peralta", "Teclado mecanico Redragon", "Algunas teclas no registran la pulsacion", "Pendiente", "Roja Benitez", 3100.0),
    ]
    return reparaciones


def mostrar_todas(lista_reparaciones):
    print("")
    print(f"TOTAL DE REPARACIONES REGISTRADAS: {len(lista_reparaciones)}")
    print("")
    for indice in range(len(lista_reparaciones)):
        reparacion = lista_reparaciones[indice]
        print(f"--- Orden {reparacion.orden} ---")
        reparacion.mostrar_datos()


def buscar_por_orden(lista_reparaciones, numero):
    reparacion_encontrada = None
    for reparacion in lista_reparaciones:
        if reparacion.orden == numero:
            reparacion_encontrada = reparacion
            break
    return reparacion_encontrada


def filtrar_por_estado(lista_reparaciones, estado):
    print("")
    print(f"REPARACIONES EN ESTADO: {estado}")
    print("")

    encontradas = 0
    entregadas = 0
    pendientes_atencion = 0
    equipos = []

    for reparacion in lista_reparaciones:
        if reparacion.estado.lower() == estado.strip().lower():
            encontradas = encontradas + 1
            reparacion.mostrar_datos()
            equipos.append(reparacion.equipo)
            if reparacion.estado == "Entregado":
                entregadas = entregadas + 1
            else:
                pendientes_atencion = pendientes_atencion + 1

    print("")
    if encontradas == 0:
        print(f'No hay reparaciones en estado "{estado}".')
        return

    print(f"Reparaciones encontradas: {encontradas}")
    print(f"Ya entregadas al cliente: {entregadas}")
    print(f"Aun en taller: {pendientes_atencion}")
    print(f"Equipos distintos: {len(equipos)}")


def filtrar_por_tecnico(lista_reparaciones, tecnico):
    print("")
    print(f"REPARACIONES ASIGNADAS A: {tecnico}")
    print("")

    asignadas = 0
    facturado = 0.0
    ordenes = []

    for reparacion in lista_reparaciones:
        if tecnico.strip().lower() in reparacion.tecnico.lower():
            asignadas = asignadas + 1
            facturado = facturado + reparacion.costo_estimado
            ordenes.append(reparacion.orden)
            reparacion.mostrar_datos()

    print("")
    if asignadas == 0:
        print(f'No hay reparaciones asignadas a "{tecnico}".')
        return

    print(f"Ordenes asignadas a {tecnico}: {asignadas}")
    print(f"Numero de ordenes: {ordenes}")
    print(f"Monto total estimado a facturar: ${facturado:.2f}")


def filtrar_por_costo(lista_reparaciones, limite):
    print("")
    print(f"REPARACIONES CON COSTO MENOR O IGUAL A ${limite:.2f}")
    print("")

    economicas = 0
    ahorro_presupuestario = 0.0
    reparacion_mas_barata = None

    for reparacion in lista_reparaciones:
        if reparacion.costo_estimado <= limite:
            economicas = economicas + 1
            ahorro_presupuestario = ahorro_presupuestario + reparacion.costo_estimado
            if reparacion_mas_barata is None or reparacion.costo_estimado < reparacion_mas_barata.costo_estimado:
                reparacion_mas_barata = reparacion
            print(f"Orden {reparacion.orden} | {reparacion.equipo}")
            print(f"      Cliente: {reparacion.cliente} | Tecnico: {reparacion.tecnico}")
            print(f"      Costo estimado: ${reparacion.costo_estimado:.2f}")

    print("")
    if economicas == 0:
        print(f"No hay reparaciones con costo menor o igual a ${limite:.2f}.")
        return

    print(f"Reparaciones dentro del limite: {economicas} de {len(lista_reparaciones)}")
    print(f"Sumatoria de costos estimados: ${ahorro_presupuestario:.2f}")
    print("")
    print("REPARACION MAS BARATA DENTRO DEL LIMITE")
    reparacion_mas_barata.mostrar_datos()


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


def pedir_float(mensaje):
    while True:
        dato = input(mensaje).strip()
        try:
            valor = float(dato)
            if valor < 0:
                print("El importe no puede ser negativo.")
                continue
            return valor
        except ValueError:
            print("Debe ingresar un importe numerico valido.")


def mostrar_menu():
    print("")
    print("=== SERVICIO TECNICO - MENU DE CONSULTAS ===")
    print("1) Mostrar todas las reparaciones")
    print("2) Buscar por orden")
    print("3) Filtrar por estado")
    print("4) Filtrar por tecnico")
    print("5) Filtrar por costo")
    print("6) Salir")


def main():
    lista_reparaciones = crear_reparaciones()
    salir = False

    while not salir:
        mostrar_menu()
        opcion = input("Seleccione una opcion: ").strip()

        if opcion == "1":
            mostrar_todas(lista_reparaciones)

        elif opcion == "2":
            numero = pedir_entero("Ingrese el numero de orden: ")
            reparacion = buscar_por_orden(lista_reparaciones, numero)
            print("")
            if reparacion is None:
                print("Reparacion no encontrada")
            else:
                reparacion.mostrar_datos()

        elif opcion == "3":
            estado = pedir_texto("Ingrese el estado a consultar: ")
            filtrar_por_estado(lista_reparaciones, estado)

        elif opcion == "4":
            tecnico = pedir_texto("Ingrese el nombre del tecnico: ")
            filtrar_por_tecnico(lista_reparaciones, tecnico)

        elif opcion == "5":
            limite = pedir_float("Ingrese el limite de costo: ")
            filtrar_por_costo(lista_reparaciones, limite)

        elif opcion == "6":
            salir = True
            print("Saliendo del sistema.")

        else:
            print("Opcion invalida. Elija un numero del 1 al 6.")

    print("Programa finalizado.")


main()
