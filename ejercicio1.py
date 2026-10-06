class TicketSoporte:
    def __init__(self, numero, usuario, sector, problema, prioridad, estado):
        self.numero = numero
        self.usuario = usuario
        self.sector = sector
        self.problema = problema
        self.prioridad = prioridad
        self.estado = estado

    def mostrar_datos(self):
        print("------------------------------")
        print(f"Nro. de ticket : {self.numero}")
        print(f"Usuario        : {self.usuario}")
        print(f"Sector         : {self.sector}")
        print(f"Problema       : {self.problema}")
        print(f"Prioridad      : {self.prioridad}")
        print(f"Estado         : {self.estado}")
        print("------------------------------")


def crear_tickets():
    tickets = [
        TicketSoporte(1001, "Luna Fernandez", "Sistemas", "No puede acceder al correo institucional", "Alta", "Pendiente"),
        TicketSoporte(1002, "Diego Sosa", "Administracion", "Solicita alta de usuario para nuevo empleado", "Media", "Pendiente"),
        TicketSoporte(1003, "Marta Ruiz", "Laboratorio", "Impresora del aula 2 no reconoce cartuchos", "Media", "En proceso"),
        TicketSoporte(1004, "Nico Peralta", "Sistemas", "Red lenta en el segundo piso", "Alta", "Pendiente"),
        TicketSoporte(1005, "Carla Medina", "Secretaria", "Falta instalar el driver de PDF para escanear", "Baja", "Resuelto"),
        TicketSoporte(1006, "Tomas Vega", "Laboratorio", "Monitor parpadea al conectar un proyector", "Media", "Pendiente"),
        TicketSoporte(1007, "Roja Benitez", "Biblioteca", "Bloqueo del sistema al cerrar el navegador", "Alta", "En proceso"),
        TicketSoporte(1008, "Ivan Lopez", "Colectoria", "Pide Restoration Point de su equipo", "Baja", "Pendiente"),
        TicketSoporte(1009, "Sonia Nunez", "Sistemas", "Backup automatico desconfigurado", "Media", "Resuelto"),
    ]
    return tickets


def buscar_ticket(lista_tickets, numero):
    ticket_encontrado = None
    for ticket in lista_tickets:
        if ticket.numero == numero:
            ticket_encontrado = ticket
            break
    return ticket_encontrado


def filtrar_por_estado(lista_tickets, estado):
    seleccion = []
    for ticket in lista_tickets:
        if ticket.estado == estado:
            seleccion.append(ticket)
    return seleccion


def contar_por_estado(lista_tickets, estado):
    cantidad = 0
    for ticket in lista_tickets:
        if ticket.estado == estado:
            cantidad = cantidad + 1
    return cantidad


def mostrar_lista(lista_tickets):
    if len(lista_tickets) == 0:
        print("No hay tickets para mostrar.")
        return
    for ticket in lista_tickets:
        ticket.mostrar_datos()


def pedir_numero(mensaje):
    while True:
        dato = input(mensaje).strip()
        try:
            return int(dato)
        except ValueError:
            print("Debe ingresar un numero entero.")


def consultar_ticket(lista_tickets):
    numero = pedir_numero("Ingrese el numero de ticket a consultar: ")
    ticket = buscar_ticket(lista_tickets, numero)
    print("")
    if ticket is None:
        print("Ticket no encontrado")
    else:
        ticket.mostrar_datos()


def consultar_pendientes(lista_tickets):
    pendientes = filtrar_por_estado(lista_tickets, "Pendiente")
    print("")
    print("TICKETS EN ESTADO PENDIENTE")
    mostrar_lista(pendientes)
    print(f"Cantidad de tickets pendientes: {contar_por_estado(lista_tickets, 'Pendiente')}")


def main():
    lista_tickets = crear_tickets()

    print("=== CONSULTA DE TICKETS - MESA DE AYUDA ===")
    print(f"Tickets cargados en el sistema: {len(lista_tickets)}")
    print("")

    consultar_ticket(lista_tickets)
    consultar_pendientes(lista_tickets)


main()