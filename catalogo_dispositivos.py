class DispositivoRed:
    def __init__(self, codigo, tipo, marca, velocidad_mbps, precio, stock):
        self.codigo = codigo
        self.tipo = tipo
        self.marca = marca
        self.velocidad_mbps = velocidad_mbps
        self.precio = precio
        self.stock = stock

    def mostrar_datos(self):
        print(f"  Codigo: {self.codigo}")
        print(f"  Tipo: {self.tipo}")
        print(f"  Marca: {self.marca}")
        print(f"  Velocidad: {self.velocidad_mbps} Mbps")
        print(f"  Precio: ${self.precio:.2f}")
        print(f"  Stock: {self.stock}")

    def hay_stock(self):
        return self.stock > 0

    def __str__(self):
        return f"{self.codigo} | {self.tipo} | {self.marca} | {self.velocidad_mbps} Mbps | ${self.precio:.2f} | stock {self.stock}"


catalogo = [
    DispositivoRed("RED-001", "Router", "Cisco", 1000, 185000.0, 6),
    DispositivoRed("RED-002", "Router", "TP-Link", 300, 62000.0, 11),
    DispositivoRed("RED-003", "Switch", "Huawei", 1000, 245000.0, 0),
    DispositivoRed("RED-004", "Switch", "Netgear", 100, 48000.0, 9),
    DispositivoRed("RED-005", "Access Point", "Ubiquiti", 1200, 128000.0, 4),
    DispositivoRed("RED-006", "Access Point", "Aruba", 867, 95000.0, 7),
    DispositivoRed("RED-007", "Modem", "Motorola", 500, 88000.0, 0),
    DispositivoRed("RED-008", "Firewall", "Fortinet", 10000, 1750000.0, 2),
]


def buscar_por_codigo(codigo_buscado):
    for dispositivo in catalogo:
        if dispositivo.codigo == codigo_buscado:
            return dispositivo
    return None


def listar_por_velocidad(velocidad_minima):
    candidatos = [d for d in catalogo if d.velocidad_mbps >= velocidad_minima and d.hay_stock()]
    if not candidatos:
        print(f"  Ningun dispositivo con stock alcanza {velocidad_minima} Mbps.")
        return
    print(f"  Dispositivos con stock y velocidad >= {velocidad_minima} Mbps ({len(candidatos)}):")
    for d in candidatos:
        print(f"    {d}")


def listar_por_presupuesto(presupuesto_maximo):
    print(f"  Dispositivos con stock que no superan ${presupuesto_maximo:.2f}:")
    encontrados = 0
    for d in catalogo:
        if d.hay_stock() and d.precio <= presupuesto_maximo:
            encontrados += 1
            print(f"    {d}")
    if encontrados == 0:
        print("    Ningun dispositivo disponible dentro de ese presupuesto.")


print("=== Catalogo completo de dispositivos de red ===")
for dispositivo in catalogo:
    print(dispositivo)

velocidad = int(input("\nVelocidad minima requerida (Mbps): "))
print(f"\nConsulta por velocidad minima ({velocidad} Mbps):")
listar_por_velocidad(velocidad)

codigo = input("\nCodigo del dispositivo a buscar (ej. RED-005): ").strip().upper()
print(f"\nConsulta por codigo '{codigo}':")
dispositivo = buscar_por_codigo(codigo)
if dispositivo is None:
    print("  Dispositivo no encontrado en el catalogo.")
else:
    dispositivo.mostrar_datos()

presupuesto = float(input("\nPresupuesto maximo para la compra: "))
print(f"\nConsulta por presupuesto maximo (${presupuesto:.2f}):")
listar_por_presupuesto(presupuesto)