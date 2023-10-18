import pygame
import math
from Bala import Bala

class Tanque:
    def __init__(self, x, y, color, num):
        self.x = x
        self.y = y
        self.color = color
        self.ancho = 60
        self.altura = 10
        self.num = num
        self.vida = 100 # vida tanque
        self.cantBala35mm = 10 #cantidad de balas 
        self.cantBala40mm = 5
        self.cantBala50mm = 2 
        self.Bala35mm = 35
        self.Bala40mm = 40
        self.Bala50mm = 50


    def dibujar(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.ancho, self.altura))

    def disparar(self, pos_inicial_x, pos_inicial_y, angulo, velocidad_inicial, tiempo, screen, color, tipo_bala):
        bala = Bala(pos_inicial_x, pos_inicial_y, angulo, velocidad_inicial, tipo_bala  )
        bala.verificacion(tiempo, screen, color)
        return bala


        