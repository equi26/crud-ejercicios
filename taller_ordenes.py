ordenes = [
    {"numero": "ORD-1001", "cliente": "Marta Rios", "equipo": "Notebook Lenovo", "falla": "No enciende", "estado": "En reparacion", "costo": 45000.0},
    {"numero": "ORD-1002", "cliente": "Diego Paz", "equipo": "PC Dell", "falla": "Falla de fuente", "estado": "Pendiente", "costo": 32000.0},
    {"numero": "ORD-1003", "cliente": "Sofia Lara", "equipo": "MacBook Air", "falla": "Bateria degradada", "estado": "En reparacion", "costo": 78000.0},
    {"numero": "ORD-1004", "cliente": "Nestor Juarez", "equipo": "Monitor Samsung", "falla": "Pantalla con lineas", "estado": "Entregado", "costo": 28000.0},
    {"numero": "ORD-1005", "cliente": "Camila Ortiz", "equipo": "Impresora HP", "falla": "Atasco de papel", "estado": "Pendiente", "costo": 15000.0},
    {"numero": "ORD-1006", "cliente": "Bruno Diaz", "equipo": "Tablet Samsung", "falla": "Puerto de carga", "estado": "En reparacion", "costo": 52000.0},
    {"numero": "ORD-1007", "cliente": "Lucia Estevez", "equipo": "Desktop Asus", "falla": "Overclock inestable", "estado": "Entregado", "costo": 22000.0},
    {"numero": "ORD-1008", "cliente": "Ruben Acosta", "equipo": "Notebook Lenovo", "falla": "Teclado descompuesto", "estado": "Pendiente", "costo": 19500.0},
    {"numero": "ORD-1009", "cliente": "Paula Nunez", "equipo": "Proyector Epson", "falla": "Luz intermitente", "estado": "En reparacion", "costo": 64000.0},
    {"numero": "ORD-1010", "cliente": "Gonzalo Vega", "equipo": "Impresora Canon", "falla": "Cabezal sucio", "estado": "Entregado", "costo": 12500.0},
]


def mostrar_orden(o):
    print(f"  {o['numero']} | {o['cliente']} | {o['equipo']} | {o['falla']} | {o['estado']} | ${o['costo']:.2f}")


def buscar_orden(numero):
    for o in ordenes:
        if o["numero"] == numero:
            return o
    return None


def filtrar_por_estado(estado):
    coincidencias = [o for o in ordenes if o["estado"] == estado]
    if not coincidencias:
        print(f"No hay ordenes en estado '{estado}'.")
        return
    print(f"Ordenes en estado '{estado}' ({len(coincidencias)}):")
    for o in coincidencias:
        mostrar_orden(o)


def filtrar_por_costo(limite):
    coincidencias = sorted(ordenes, key=lambda o: o["costo"])
    economicas = 0
    for o in coincidencias:
        if o["costo"] <= limite:
            economicas += 1
            mostrar_orden(o)
    if economicas == 0:
        print(f"No hay ordenes con costo estimado menor o igual a ${limite:.2f}.")
    else:
        print(f"Ordenes con costo estimado <= ${limite:.2f}: {economicas} (de menor a mayor costo)")


def mostrar_todas():
    print(f"Listado completo de ordenes ({len(ordenes)}):")
    for o in ordenes:
        mostrar_orden(o)


def menu():
    opciones = (
        "\n=== Taller: consultas de ordenes ===\n"
        "1. Buscar orden por numero\n"
        "2. Filtrar ordenes por estado\n"
        "3. Filtrar ordenes por costo maximo\n"
        "4. Mostrar todas las ordenes\n"
        "5. Salir\n"
    )
    while True:
        print(opciones)
        opcion = input("Seleccione una opcion: ").strip()
        if opcion == "1":
            numero = input("Numero de orden (ej. ORD-1003): ").strip().upper()
            orden = buscar_orden(numero)
            if orden is None:
                print("Orden no encontrada.")
            else:
                print("Orden encontrada:")
                mostrar_orden(orden)
        elif opcion == "2":
            estados = sorted({o["estado"] for o in ordenes})
            print("Estados disponibles: " + ", ".join(estados))
            filtrar_por_estado(input("Estado a consultar: ").strip())
        elif opcion == "3":
            try:
                limite = float(input("Costo maximo estimado: "))
            except ValueError:
                print("Debe ingresar un valor numerico.")
                continue
            filtrar_por_costo(limite)
        elif opcion == "4":
            mostrar_todas()
        elif opcion == "5":
            print("Programa finalizado.")
            break
        else:
            print("Opcion invalida. Intente nuevamente.")


if __name__ == "__main__":
    menu()