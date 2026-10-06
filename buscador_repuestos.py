repuestos = [
    {"codigo": "R-001", "descripcion": "SSD Kingston 480 GB", "categoria": "Almacenamiento", "marca": "Kingston", "precio": 42000.0, "stock": 8},
    {"codigo": "R-002", "descripcion": "SSD Crucial 1 TB", "categoria": "Almacenamiento", "marca": "Crucial", "precio": 95000.0, "stock": 3},
    {"codigo": "R-003", "descripcion": "Disco Duro HDD 1 TB", "categoria": "Almacenamiento", "marca": "Seagate", "precio": 58000.0, "stock": 0},
    {"codigo": "R-004", "descripcion": "Memoria RAM DDR4 8 GB", "categoria": "Memoria", "marca": "Corsair", "precio": 32000.0, "stock": 14},
    {"codigo": "R-005", "descripcion": "Bateria de laptop 14Wh", "categoria": "Baterias", "marca": "HP", "precio": 21500.0, "stock": 6},
    {"codigo": "R-006", "descripcion": "Bateria de notebook 10Wh", "categoria": "Baterias", "marca": "Lenovo", "precio": 19800.0, "stock": 0},
    {"codigo": "R-007", "descripcion": "Fuente de poder 600W", "categoria": "Energia", "marca": "Cooler Master", "precio": 27500.0, "stock": 5},
    {"codigo": "R-008", "descripcion": "Ventilador cooler 120mm", "categoria": "Refrigeracion", "marca": "Noctua", "precio": 14900.0, "stock": 11},
    {"codigo": "R-009", "descripcion": "Teclado mecanico RGB", "categoria": "Perifericos", "marca": "Redragon", "precio": 36500.0, "stock": 2},
    {"codigo": "R-010", "descripcion": "Placa de video RTX 3060", "categoria": "Componentes", "marca": "Asus", "precio": 320000.0, "stock": 0},
    {"codigo": "R-011", "descripcion": "Conector USB-C a HDMI", "categoria": "Perifericos", "marca": "Anker", "precio": 18900.0, "stock": 9},
    {"codigo": "R-012", "descripcion": "Toner negro compatible", "categoria": "Insumos", "marca": "Generic", "precio": 7400.0, "stock": 22},
]

texto = input("Ingrese el texto a buscar en la descripcion del repuesto: ").strip()

coincidencias = 0
disponibles = 0

print("\nCoincidencias encontradas:")
for r in repuestos:
    if texto.lower() in r["descripcion"].lower():
        coincidencias += 1
        hay_stock = r["stock"] > 0
        if hay_stock:
            disponibles += 1
        estado = f"DISPONIBLE (stock: {r['stock']})" if hay_stock else "SIN STOCK"
        print(f"  {r['codigo']} | {r['descripcion']} | {r['categoria']} | {r['marca']} | ${r['precio']:.2f} | {estado}")

if coincidencias == 0:
    print("  La busqueda no produjo resultados.")

print(f"\nCantidad total de coincidencias: {coincidencias}")
print(f"Coincidencias disponibles (stock > 0): {disponibles}")