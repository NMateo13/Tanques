import pygame
import math
from Bala import Bala

class Tanque:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.ancho = 60
        self.altura = 10

    def dibujar(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.ancho, self.altura))

    def disparar(self, pos_inicial_x, pos_inicial_y, angulo, velocidad_inicial, tiempo, screen, color):
        bala = Bala(pos_inicial_x, pos_inicial_y, angulo, velocidad_inicial)
        bala.verificacion(tiempo, screen, color)
        return bala

    def verificar_impacto1(self, bala):
        # Verificar si la bala ha impactado en el rectángulo del tanque
        for punto in Bala.trayectoria:
            x, y = punto
            if (self.x <= x <= (self.x + self.ancho)) and (self.y <= y <= (self.y + self.altura)):
                return True
        return False