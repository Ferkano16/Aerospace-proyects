#  Orbital Velocities (Python)

Proyecto en Python que calcula velocidades orbitales de diferentes satélites utilizando física real.

##  Características

- Cálculo de órbitas circulares
- Implementación de la ecuación vis-viva para órbitas elípticas
- Ordenación de resultados por velocidad
- Exportación a CSV
- Código modular y limpio (sin dependencias externas)

## Fórmulas utilizadas

Órbita circular:
v = √(GM / r)

Órbita elíptica (vis-viva):
v = √(GM (2/r - 1/a))

##  Ejemplo de salida

Satélite            Altitud (km)    Velocidad (km/s)
------------------------------------------------------------
ISS                 408             7.67
Hubble              547             7.59
GPS                 20200           3.87
Geostacionario      35786           3.07
Luna                384400          1.02

##  Archivos generados

- results.csv → datos exportados

##  Uso

```bash
py main.py# Aerospace-proyects
