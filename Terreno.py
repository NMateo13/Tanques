import pygame
import math

class Terreno:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
        self.terreno = self.generar_terreno()

    def generar_terreno(self):
        terreno = []
        amplitud = 100  # Ajusta esta amplitud según tus necesidades
        frecuencia = 100  # Ajusta esta frecuencia según tus necesidades
        for x in range(self.ancho):
            # Genera el valor de la altura del terreno usando una función seno
            altura = int(self.alto / 2 + amplitud * math.sin(x / frecuencia))
            terreno.append(altura)
        return terreno

    def dibujar(self, pantalla):
        color_terreno = (139, 69, 19)  # Color marrón para el terreno
        for x, altura in enumerate(self.terreno):
            pygame.draw.rect(pantalla, color_terreno, (x, self.alto - altura, 1, altura))

    def verificar_colision(self, bala):
        for x, y in bala.trayectoria:
            if 0 <= x < self.ancho and self.alto - y >= self.terreno[int(x)]:
                return False
        return True