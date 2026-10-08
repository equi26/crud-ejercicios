
# Clase que representa una orden de reparación de servicio técnico.
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



# Retorna la lista con todas las órdenes de reparación precargadas.
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


# =================