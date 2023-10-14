import pygame, datos, random
import math

class Terreno:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
        self.terreno = self.generar_terreno()

    def generar_terreno(self):
        terreno = []

        aux = 0
        flotante = 2.0
        auxAltura = 0
        x = 0

        while aux <= 1200:


            amplitud = random.randint(50, 90)  # Ajusta esta amplitud según tus necesidades
            frecuencia = random.randint(50, 90)  # Ajusta esta frecuencia según }<tus necesidades

            if x > 0:
                if altura > 130:
                    auxAltura = altura
                else: 
                    auxAltura = 131

            altura = int(self.alto / flotante + amplitud * math.sin(aux / frecuencia))


            while auxAltura != altura and x != 0:

                if auxAltura > altura:
                    flotante = flotante - 0.001
                    altura = int(self.alto / flotante + amplitud * math.sin(aux / frecuencia))
                elif auxAltura < altura:
                    flotante = flotante + 0.001
                    altura = int(self.alto / flotante + amplitud * math.sin(aux / frecuencia))

            for y in range(frecuencia*4):

                altura = int(self.alto / flotante + amplitud * math.sin(aux / frecuencia))
                terreno.append(altura)
                aux += 1
                if aux == 1200 or altura < 130:
                    break

            if aux == 1200:
                break

            x += 1
        
        return terreno
            



    def dibujar(self, pantalla):

        for x, altura in enumerate(self.terreno):
            pygame.draw.rect(pantalla, datos.BROWN, (x, self.alto - altura, 1, altura))

    def verificar_colision(self, bala):
        for x, y in bala.trayectoria:
            if 0 <= x < self.ancho and self.alto - y >= self.terreno[int(x)]:
                return False
        return True