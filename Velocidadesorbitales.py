import math
import csv

# Constantes físicas
G = 6.674e-11          # constante gravitacional (m^3 kg^-1 s^-2)
M = 5.972e24           # masa de la Tierra (kg)
R = 6371000            # radio de la Tierra (m)

# Datos: (nombre, altitud_km, semieje_mayor_km)
satelites = [
    ("ISS", 408, None),
    ("Hubble", 547, None),
    ("GPS", 20200, None),
    ("Geostacionario", 35786, None),
    ("Luna", 384400, 384400)
]

def velocidad_orbital(altitud_km, semieje_mayor_km=None):
    """
    Calcula la velocidad orbital usando:
    - Órbita circular si no se especifica semieje mayor
    - Ecuación vis-viva si es elíptica
    """
    r = R + altitud_km * 1000

    if semieje_mayor_km is None:
        # Órbita circular
        v = math.sqrt(G * M / r)
    else:
        # Órbita elíptica (vis-viva)
        a = semieje_mayor_km * 1000
        v = math.sqrt(G * M * (2 / r - 1 / a))

    return v / 1000  # convertir a km/s


def calcular_satelites(datos):
    resultados = []

    for nombre, altitud, a in datos:
        v = velocidad_orbital(altitud, a)
        resultados.append({
            "nombre": nombre,
            "altitud_km": altitud,
            "velocidad_km_s": v
        })

    return resultados


def mostrar_tabla(resultados):
    print(f"{'Satélite':<20} {'Altitud (km)':<15} {'Velocidad (km/s)':<20}")
    print("-" * 60)

    for sat in resultados:
        print(f"{sat['nombre']:<20} {sat['altitud_km']:<15} {sat['velocidad_km_s']:.4f}")


def guardar_csv(resultados, filename="results.csv"):
    with open(filename, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["nombre", "altitud_km", "velocidad_km_s"])
        writer.writeheader()
        writer.writerows(resultados)


def main():
    resultados = calcular_satelites(satelites)

    # Ordenar por velocidad (de mayor a menor)
    resultados.sort(key=lambda x: x["velocidad_km_s"], reverse=True)

    mostrar_tabla(resultados)
    guardar_csv(resultados)

    print("\n✔ Resultados guardados en 'results.csv'")


if __name__ == "__main__":
    main()