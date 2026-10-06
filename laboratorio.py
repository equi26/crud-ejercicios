inventario = [
    {"inventario": "LAB-001", "tipo": "PC de escritorio", "marca": "Dell", "estado": "Disponible", "anio": 2019},
    {"inventario": "LAB-002", "tipo": "Notebook", "marca": "Lenovo", "estado": "Disponible", "anio": 2022},
    {"inventario": "LAB-003", "tipo": "Monitor", "marca": "Samsung", "estado": "En reparación", "anio": 2021},
    {"inventario": "LAB-004", "tipo": "Proyector", "marca": "Epson", "estado": "Disponible", "anio": 2023},
    {"inventario": "LAB-005", "tipo": "Impresora 3D", "marca": "Creality", "estado": "Disponible", "anio": 2024},
    {"inventario": "LAB-006", "tipo": "Osciloscopio", "marca": "Rigol", "estado": "Baja", "anio": 2018},
    {"inventario": "LAB-007", "tipo": "Multímetro", "marca": "Fluke", "estado": "Disponible", "anio": 2022},
    {"inventario": "LAB-008", "tipo": "Estación de soldadura", "marca": "JBC", "estado": "Disponible", "anio": 2020},
    {"inventario": "LAB-009", "tipo": "Servidor", "marca": "HP", "estado": "En reparación", "anio": 2023},
    {"inventario": "LAB-010", "tipo": "Microscopio", "marca": "Nikon", "estado": "Disponible", "anio": 2024},
]


def mostrar(equipos):
    for e in equipos:
        print(f"  {e['inventario']} | {e['tipo']} | {e['marca']} | {e['anio']}")


anio_minimo = int(input("Ingrese el año mínimo para el uso de equipos: "))

disponibles = [e for e in inventario if e["estado"] == "Disponible"]

print("\nEquipos en estado 'Disponible':")
mostrar(disponibles)

cumple = 0

print(f"\nEquipos 'Disponible' del año {anio_minimo} en adelante:")
for e in inventario:
    if e["estado"] == "Disponible" and e["anio"] >= anio_minimo:
        cumple += 1
        print(f"  {e['inventario']} | {e['tipo']} | {e['marca']} | {e['anio']}")

print(f"\nEquipos que cumplen ambas condiciones: {cumple}")

if cumple == 0:
    print("No existe ningún equipo que cumpla las condiciones solicitadas.")