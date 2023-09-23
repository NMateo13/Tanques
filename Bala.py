import pygame
import math

class Bala:
    def __init__(self,pos_inicial_x,pos_inicial_y,angulo,velocidad_inicial,gravedad,incremento):
        self.pos_inicial_x = pos_inicial_x
        self.pos_inicial_y = pos_inicial_y
        self.angulo = math.radians(angulo) 
        self.velocidad_inicial = velocidad_inicial
        self.gravedad = gravedad
        self.incremento = incremento
        self.trayectoria = []

    def calcular_posiciones(self,time):
        x = self.pos_inicial_x + self.velocidad_inicial * math.cos(self.angulo) * time
        y = self.pos_inicial_y - (self.velocidad_inicial * math.sin(self.angulo) * time - 0.5 * self.gravedad * time ** 2)
        return x, y
    
    def verificacion(self,tiempo, WIDTH, HEIGHT,screen,color):
        self.tiempo = tiempo
        posiciones = self.calcular_posiciones(self.tiempo)
        #self.trayectoria.append(posiciones)
        if 0 <= posiciones[0] < WIDTH and 0 <= posiciones[1] < HEIGHT:
            self.trayectoria.append(posiciones)
        max_points = 1
        if len(self.trayectoria) > max_points:
            self.trayectoria.pop(0)
        for point in self.trayectoria:
            pygame.draw.circle(screen,color, (int(point[0]), int(point[1])), 4)




