import numpy as np

class Espacio:
    def __init__(self,coord_x1, coord_x2, coord_y1, coord_y2):
        self.coord_x1 = coord_x1
        self.coord_x2 = coord_x2
        self.coord_y1 = coord_y1
        self.coord_y2 = coord_y2
    
    def posicion(self):
        print(f"El espacio 1 va de en x = {Espacio1.coord_x1} a x = {Espacio1.coord_x2} e y = {Espacio1.coord_y1} a y = {Espacio1.coord_y2} ")


Espacio1 = Espacio(0,50,0,50) 
Espacio2 = Espacio(50,100,50,100) 

Espacio1.posicion()
Espacio2.posicion()


class Persona:
    def __init__(self, coord_x, coord_y):
        self.coord_x = coord_x
        self.coord_y = coord_y 

    def posicion(self):
        print(f"La persona 1 esta en x = {persona1.coord_x} y = {persona1.coord_y}")
        print(f"La persona 2 esta en x = {persona2.coord_x} y = {persona2.coord_y}")

    def distancia(self):
        x1 = persona1.coord_x
        y1 = persona1.coord_y
        x2 = persona2.coord_x
        y2 = persona2.coord_y
        distancia_parte1 = ((x2 - x1)**2) + ((y2 - y1)**2)
        distancia_final = np.sqrt(distancia_parte1)
        print(f"La persona uno se encuentra a {distancia_final} metros de la persona dos")
                
        if x1 == x2 and y1 == y2:
            print(f"Estan en la misma posición")
            persona1.coord_x = persona1.coord_x + 20
            persona1.coord_y = persona1.coord_y + 20
            print(f"la persona 1 se ha ido a x = {persona1.coord_x} y = {persona1.coord_y} para alejarse de la persona 2")

        else:
            print(f"No estan en la misma posición")
            print(f"Por eso la persona 1 se ha quedado en su sitio")



persona1 = Persona(80,35) 
persona2 = Persona(40, 35)
persona1.posicion()
persona2.posicion()
persona1.distancia()