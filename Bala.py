import pygame
import math

class Bala:
    def __init__(self, pos_inicial_x, pos_inicial_y, angulo, velocidad_inicial):
        self.pos_inicial_x = pos_inicial_x
        self.pos_inicial_y = pos_inicial_y
        self.angulo = math.radians(angulo)
        self.velocidad_inicial = velocidad_inicial
        self.gravedad = 9.8
        self.incremento = 0.05
        self.trayectoria = []

    def calcular_posiciones(self, time):
        x = self.pos_inicial_x + self.velocidad_inicial * math.cos(self.angulo) * time
        y = self.pos_inicial_y - (self.velocidad_inicial * math.sin(self.angulo) * time - 0.5 * self.gravedad * time ** 2)
        return x, y

    def verificacion(self, tiempo, screen, color):
        self.tiempo = tiempo
        posiciones = self.calcular_posiciones(self.tiempo)
        self.trayectoria.append(posiciones)
        max_points = 1
        if len(self.trayectoria) > max_points:
            self.trayectoria.pop(0)
        for point in self.trayectoria:
            pygame.draw.circle(screen, color, (int(point[0]), int(point[1])), 4)
    

    def verificar_impacto_ancho(self, ancho_pantalla):
        for x, _ in self.trayectoria:
            if x < 4 or x > ancho_pantalla:
                return True
        return False

    def verificar_impacto_tanque(self, tanque):
        for punto in self.trayectoria:
            x, y = punto
            if (tanque.x <= x <= (tanque.x + tanque.ancho)) and (tanque.y <= y <= (tanque.y + tanque.altura)):
                return True
        return False
    
    def verificar_impacto_terreno(self, terreno):
        for punto in self.trayectoria:
            x, y = punto
            if 0 <= x < len(terreno.terreno) and y >= terreno.terreno[int(x)]:
                return True
        return False
    