
# Modela un componente electrónico del laboratorio, con métodos para verificar
# disponibilidad de stock y mostrar su detalle.
class Componente:
    def __init__(self, codigo, nombre, tipo, marca, stock, ubicacion):
        self.codigo = codigo
        self.nombre = nombre
        self.tipo = tipo
        self.marca = marca
        self.stock = stock
        self.ubicacion = ubicacion

    def hay_stock(self):
        return self.stock > 0

    def mostrar_datos(self):
        estado = "Disponible" if self.hay_stock() else "Sin stock"
        print("------------------------------")
        print(f"Codigo   : {self.codigo}")
        print(f"Nombre   : {self.nombre}")
        print(f"Tipo     : {self.tipo}")
        print(f"Marca    : {self.marca}")
        print(f"Stock    : {self.stock} ({estado})")
        print(f"Ubicacion: {self.ubicacion}")
        print("------------------------------")



# Retorna el inventario inicial de componentes del laboratorio.
def crear_componentes():
    componentes = [
        Componente("CMP-001", "Resistencia 220 ohm", "Resistencia", "Philips", 120, "Estante A1"),
        Componente("CMP-002", "Capacitor 100uF", "Capacitor", "Samsung", 0, "Estante A1"),
        Componente("CMP-003", "Diodo 1N4007", "Diodo", "ON Semiconductor", 45, "Estante A2"),
        Componente("CMP-004", "LED rojo 5mm", "LED", "Kingbright", 300, "Estante A2"),
        Componente("CMP-005", "Transistor BC547", "Transistor", "STMicroelectronics", 18, "Estante A3"),
        Componente("CMP-006", "Microcontrolador Arduino Uno", "Microcontrolador", "Arduino", 6, "Estante B1"),
        Componente("CMP-007", "Sensor de temperatura DHT11", "Sensor", "Aosong", 25, "Estante B1"),
        Componente("CMP-008", "Protoboard 830 puntos", "Protoboard", "Banes", 34, "Estante B2"),
        Componente("CMP-009", "Cable jumper M-M 20cm", "Cable", "JST", 500, "Estante B2"),
        Componente("CMP-010", "Fuente de alimentacion 5V 3A", "Fuente", "Mean Well", 9, "Estante C1"),
        Componente("CMP-011", "Display LCD 16x2", "Display", "Hitachi", 12, "Estante C1"),
        Componente("CMP-012", "Potenciometro 10k", "Potenciometro", "Alpha", 0, "Estante C2"),
        Componente("CMP-013", "Motor DC 3V", "Motor", "Johnson", 21, "Estante C2"),
        Componente("CMP-014", "Zener 5.1V", "Diodo", "Motorola", 4, "Estante A3"),
    ]
    return componentes



#  Funciones auxiliares de texto

def normalizar(texto):
    return texto.strip().lower()

# Verifica insensible a mayúsculas si `texto` está contenido en `valor`.
def contiene(valor, texto):
    return normalizar(texto) in normalizar(valor)



# Validaciones de entrada del usuario

def pedir_texto(mensaje):
    while True:
        dato = input(mensaje).strip()
        if dato != "":
            return dato
        print("Debe ingresar al menos un dato.")

def pedir_entero_positivo(mensaje):
    while True:
        dato = input(mensaje).strip()
        try:
            numero = int(dato)
            if numero < 0:
                print("El valor no puede ser negativo.")
                continue
            return numero
        except ValueError:
            print("Debe ingresar un numero entero valido.")



#  Consultas y filtrado de catálogo
# Extrae y muestra los tipos únicos de componentes disponibles.
def mostrar_catalogo(lista_componentes):
    print("TIPOS DISPONIBLES EN EL LABORATORIO")
    tipos = []
    for componente in lista_componentes:
        repetido = False
        for tipo in tipos:
            if tipo == componente.tipo:
                repetido = True
        if not repetido:
            tipos.append(componente.tipo)
    for tipo in tipos:
        print(f"- {tipo}")
    print("")

# Filtra componentes por tipo/nombre y stock mínimo, determinando además el de mayor stock.
def consultar_componentes(lista_componentes):
    tipo = pedir_texto("Ingrese el tipo de componente: ")
    stock_minimo = pedir_entero_positivo("Ingrese la cantidad minima de stock: ")

    print("")
    print(f'CRITERIOS: tipo contiene "{tipo}" y stock >= {stock_minimo}')
    print("")

    cantidad = 0
    componente_mayor_stock = None

    for componente in lista_componentes:
        coincide_tipo = contiene(componente.tipo, tipo) or contiene(componente.nombre, tipo)
        suficiente_stock = componente.stock >= stock_minimo

        if coincide_tipo and suficiente_stock:
            cantidad = cantidad + 1
            print(f"[{cantidad}] {componente.codigo} - {componente.nombre}")
            print(f"      Tipo: {componente.tipo} | Marca: {componente.marca}")
            print(f"      Stock: {componente.stock} | Ubicacion: {componente.ubicacion}")
            if componente_mayor_stock is None or componente.stock > componente_mayor_stock.stock:
                componente_mayor_stock = componente

    print("")
    if cantidad == 0:
        print("Ningun componente cumple con las condiciones indicadas.")
        return

    print(f"Cantidad de componentes que cumplen ambas condiciones: {cantidad}")
    print("")
    print("COMPONENTE CON MAYOR STOCK")
    componente_mayor_stock.mostrar_datos()



#  Función principal y ejecución

def main():
    lista_componentes = crear_componentes()

    print("=== LABORATORIO - FILTRO COMBINADO DE COMPONENTES ===")
    print(f"Componentes cargados: {len(lista_componentes)}")
    print("")

    mostrar_catalogo(lista_componentes)
    consultar_componentes(lista_componentes)


main()