import numpy as np
import random

class Espacio:
    def __init__(self, coord_x1, coord_x2, coord_y1, coord_y2):
        self.coord_x1 = coord_x1
        self.coord_x2 = coord_x2
        self.coord_y1 = coord_y1
        self.coord_y2 = coord_y2

    def contiene(self, persona):
        return (self.coord_x1 <= persona.coord_x <= self.coord_x2 and
                self.coord_y1 <= persona.coord_y <= self.coord_y2)

    def __repr__(self):
        return f"Espacio({self.coord_x1}, {self.coord_x2}, {self.coord_y1}, {self.coord_y2})"


class Persona:
    def __init__(self, nombre, coord_x, coord_y):
        self.nombre = nombre
        self.coord_x = coord_x
        self.coord_y = coord_y
        self.monedas = 0

    def distancia_a(self, otra_persona):
        return np.sqrt((self.coord_x - otra_persona.coord_x) ** 2 + (self.coord_y - otra_persona.coord_y) ** 2)

    def mover(self, coord_x, coord_y):
        self.coord_x = coord_x
        self.coord_y = coord_y

    def agregar_moneda(self):
        self.monedas += 1

    def __repr__(self):
        return f"Persona({self.nombre}, {self.coord_x}, {self.coord_y}, Monedas: {self.monedas})"


class Moneda:
    def __init__(self, coord_x, coord_y):
        self.coord_x = coord_x
        self.coord_y = coord_y

    def __repr__(self):
        return f"Moneda({self.coord_x}, {self.coord_y})"


def mover_todas_las_personas(personas, espacio):
    for persona in personas:
        nueva_coord_x = random.randint(espacio.coord_x1, espacio.coord_x2)
        nueva_coord_y = random.randint(espacio.coord_y1, espacio.coord_y2)
        persona.mover(nueva_coord_x, nueva_coord_y)


def persona_recoge_moneda(personas, monedas):
    for persona in personas:
        for moneda in monedas[:]:
            if persona.coord_x == moneda.coord_x and persona.coord_y == moneda.coord_y:
                persona.agregar_moneda()
                monedas.remove(moneda)


def cuantas_monedas_tiene_persona(persona):
    return persona.monedas


def riqueza_total(personas):
    return sum(persona.monedas for persona in personas)


def combate(persona1, persona2):
    if persona1.coord_x == persona2.coord_x and persona1.coord_y == persona2.coord_y:
        if persona1.monedas > persona2.monedas:
            return f"{persona1.nombre} gana el combate contra {persona2.nombre}"
        elif persona2.monedas > persona1.monedas:
            return f"{persona2.nombre} gana el combate contra {persona1.nombre}"
        else:
            return f"El combate entre {persona1.nombre} y {persona2.nombre} termina en empate"
    else:
        return "No hay combate, las personas no están en la misma posición"


espacio1 = Espacio(0, 50, 0, 50)
espacio2 = Espacio(50, 100, 50, 100)

persona1 = Persona("Juan", 80, 35)
persona2 = Persona("Ana", 40, 35)
persona3 = Persona("Luis", 85, 40)

todas_las_personas = [persona1, persona2, persona3]

moneda1 = Moneda(80, 35)
moneda2 = Moneda(40, 35)
moneda3 = Moneda(85, 40)

todas_las_monedas = [moneda1, moneda2, moneda3]

print("Posiciones iniciales de las personas:")
for persona in todas_las_personas:
    print(persona)

print("\nMonedas iniciales en el espacio:")
for moneda in todas_las_monedas:
    print(moneda)

mover_todas_las_personas(todas_las_personas, espacio1)
print("\nPosiciones después de mover a todas las personas:")
for persona in todas_las_personas:
    print(persona)

persona_recoge_moneda(todas_las_personas, todas_las_monedas)
print("\nMonedas restantes en el espacio:")
for moneda in todas_las_monedas:
    print(moneda)

print("\nMonedas recogidas por cada persona:")
for persona in todas_las_personas:
    print(f"{persona.nombre} tiene {cuantas_monedas_tiene_persona(persona)} monedas")

print(f"\nRiqueza total: {riqueza_total(todas_las_personas)}")

print("\nResultado del combate entre persona1 y persona2:")
print(combate(persona1, persona2))

print("\nResultado del combate entre persona1 y persona3:")
print(combate(persona1, persona3))