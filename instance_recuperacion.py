alumnos = [
    {"nombre": "Ana Gomez", "curso": "3A", "promedio": 8.5, "trabajos": 6},
    {"nombre": "Bruno Diaz", "curso": "3A", "promedio": 6.2, "trabajos": 4},
    {"nombre": "Carla Ruiz", "curso": "3B", "promedio": 9.1, "trabajos": 8},
    {"nombre": "Diego Paz", "curso": "3B", "promedio": 7.0, "trabajos": 7},
    {"nombre": "Elena Soto", "curso": "3A", "promedio": 8.8, "trabajos": 5},
    {"nombre": "Facundo Vega", "curso": "3C", "promedio": 5.4, "trabajos": 2},
    {"nombre": "Gisela Nunez", "curso": "3C", "promedio": 7.8, "trabajos": 9},
    {"nombre": "Hugo Lara", "curso": "3B", "promedio": 6.9, "trabajos": 6},
    {"nombre": "Irene Cabrera", "curso": "3A", "promedio": 9.5, "trabajos": 4},
    {"nombre": "Javier Rios", "curso": "3C", "promedio": 7.2, "trabajos": 3},
    {"nombre": "Karina Molina", "curso": "3B", "promedio": 8.1, "trabajos": 10},
    {"nombre": "Lucas Ferreyra", "curso": "3A", "promedio": 6.5, "trabajos": 5},
]

promedio_minimo = float(input("Ingrese el promedio minimo requerido: "))
trabajos_minimos = int(input("Ingrese la cantidad minima de trabajos entregados: "))

cumplen = 0
no_cumplen = 0

mejor_nombre = None
mejor_promedio = -1.0

print(f"\nAlumnos con promedio >= {promedio_minimo} y trabajos >= {trabajos_minimos}:")
for a in alumnos:
    cumple_criterios = a["promedio"] >= promedio_minimo and a["trabajos"] >= trabajos_minimos
    if cumple_criterios:
        cumplen += 1
        print(f"  {a['nombre']} | Curso {a['curso']} | Promedio {a['promedio']} | Trabajos {a['trabajos']}")
        if a["promedio"] > mejor_promedio:
            mejor_promedio = a["promedio"]
            mejor_nombre = a["nombre"]
    else:
        no_cumplen += 1

total = cumplen + no_cumplen
print(f"\nTotal de alumnos: {total}")
print(f"Alumnos que cumplen: {cumplen}")
print(f"Alumnos que NO cumplen: {no_cumplen}")

if cumplen == 0:
    print("Ningun alumno cumple las condiciones solicitadas.")
else:
    print(f"\nMejor promedio entre los que cumplen: {mejor_nombre} ({mejor_promedio})")