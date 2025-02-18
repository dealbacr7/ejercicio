import numpy as np

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

    def distancia_a(self, otra_persona):
        return np.sqrt((self.coord_x - otra_persona.coord_x) ** 2 + (self.coord_y - otra_persona.coord_y) ** 2)

    def __repr__(self):
        return f"Persona({self.nombre}, {self.coord_x}, {self.coord_y})"


def obtener_personas_cercanas(persona, personas, distancia):
    return [p for p in personas if persona.distancia_a(p) <= distancia and p != persona]


def calcular_persona_mas_cercana(persona, personas):
    if not personas:
        return None
    return min((p for p in personas if p != persona), key=lambda p: persona.distancia_a(p), default=None)


espacio1 = Espacio(0, 50, 0, 50)
espacio2 = Espacio(50, 100, 50, 100)

persona1 = Persona("Juan", 80, 35)
persona2 = Persona("Ana", 40, 35)
persona3 = Persona("Luis", 85, 40)

todas_las_personas = [persona1, persona2, persona3]

personas_cercanas = obtener_personas_cercanas(persona1, todas_las_personas, 50)
print(f"Personas cercanas a {persona1.nombre}: {personas_cercanas}")

persona_mas_cercana = calcular_persona_mas_cercana(persona1, todas_las_personas)
print(f"Persona más cercana a {persona1.nombre}: {persona_mas_cercana}")

print(persona1)

print(f"Distancia entre {persona1.nombre} y {persona2.nombre}: {persona1.distancia_a(persona2)}")
