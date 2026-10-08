# Representa un ticket de soporte técnico individual con sus propiedades y
# un método para mostrar sus datos formateados en consola.
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



# Función encargada de instanciar y retornar una lista predefinida de tickets.
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


# ==========================================
# BLOQUE 3: Funciones de búsqueda y filtrado
# ==========================================
# Busca un ticket por su número único. Retorna el objeto o None si no existe.
def buscar_ticket(lista_tickets, numero):
    ticket_encontrado = None
    for ticket in lista_tickets:
        if ticket.numero == numero:
            ticket_encontrado = ticket
            break
    return ticket_encontrado

# Retorna una sublista con los tickets que coinciden con el estado especificado.
def filtrar_por_estado(lista_tickets, estado):
    seleccion = []
    for ticket in lista_tickets:
        if ticket.estado == estado:
            seleccion.append(ticket)
    return seleccion

# Cuenta la cantidad de tickets que se encuentran en un determinado estado.
def contar_por_estado(lista_tickets, estado):
    cantidad = 0
    for ticket in lista_tickets:
        if ticket.estado == estado:
            cantidad = cantidad + 1
    return cantidad


# ==========================================
# BLOQUE 4: Entrada/Salida e Interacción
# ==========================================
# Muestra por pantalla la lista de tickets especificada.
def mostrar_lista(lista_tickets):
    if len(lista_tickets) == 0:
        print("No hay tickets para mostrar.")
        return
    for ticket in lista_tickets:
        ticket.mostrar_datos()

# Solicita y valida la entrada de un número entero desde el teclado.
def pedir_numero(mensaje):
    while True:
        dato = input(mensaje).strip()
        try:
            return int(dato)
        except ValueError:
            print("Debe ingresar un numero entero.")

# Solicita un número de ticket al usuario y muestra el resultado de la búsqueda.
def consultar_ticket(lista_tickets):
    numero = pedir_numero("Ingrese el numero de ticket a consultar: ")
    ticket = buscar_ticket(lista_tickets, numero)
    print("")
    if ticket is None:
        print("Ticket no encontrado")
    else:
        ticket.mostrar_datos()

# Filtra y muestra todos los tickets con estado "Pendiente".
def consultar_pendientes(lista_tickets):
    pendientes = filtrar_por_estado(lista_tickets, "Pendiente")
    print("")
    print("TICKETS EN ESTADO PENDIENTE")
    mostrar_lista(pendientes)
    print(f"Cantidad de tickets pendientes: {contar_por_estado(lista_tickets, 'Pendiente')}")


# Coordina la carga inicial y la ejecución de las consultas principales.
def main():
    lista_tickets = crear_tickets()

    print("=== CONSULTA DE TICKETS - MESA DE AYUDA ===")
    print(f"Tickets cargados en el sistema: {len(lista_tickets)}")
    print("")

    consultar_ticket(lista_tickets)
    consultar_pendientes(lista_tickets)


main()