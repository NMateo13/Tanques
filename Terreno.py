import pygame, Datos, random
import math

class Terreno:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
        self.terreno = self.generar_terreno()

    def generar_terreno(self):
        terreno = []
        altura2 = []

        aux = 0
        flotante = 2.0
        auxAltura = 0
        x = 0

        while aux <= Datos.PANT_ANCHO:
            amplitud = random.randint(50, 90)  # Ajusta esta amplitud según tus necesidades
            frecuencia = random.randint(50, 90)  # Ajusta esta frecuencia según tus necesidades

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
                if aux == Datos.PANT_ANCHO or altura < 130:
                    break

            if aux == Datos.PANT_ANCHO:
                break

            x += 1
        
        return terreno
            
    def dibujar(self, pantalla):
        for x, altura in enumerate(self.terreno):
            pygame.draw.rect(pantalla, Datos.BROWN, (x, self.alto - altura, 1, altura))

    def verificar_colision(self, bala):
        for x, y in bala.trayectoria:
            if 0 <= x < self.ancho and self.alto - y >= self.terreno[int(x)]:
                return False
        return True
    

    def modificar_terreno(self, terreno, tanque):
        centro_explosion = self.calcular_centro_explosion()
        puntosx, puntosy = self.calcular_puntos_explosion(centro_explosion, tanque)
        puntos_x, puntos_y = self.obtener_puntos_x_y(puntosx, puntosy)
        self.actualizar_terreno(terreno, puntos_x, puntos_y)
        return centro_explosion

    def calcular_centro_explosion(self):
        centro_explosion = []
        for x, y in Datos.bala_tanque.trayectoria:
            centro_explosion.append(int(x))
            centro_explosion.append(int(y))
        return centro_explosion

    def calcular_puntos_explosion(self, centro_explosion, tanque):
        num_puntos_explosion = int(2 * math.pi * tanque.radioExplosion)
        puntosx = []
        puntosy = []
        for i in range(num_puntos_explosion):
            angle = (2 * math.pi / num_puntos_explosion) * i
            x = int(centro_explosion[0] + tanque.radioExplosion * math.cos(angle))
            y = int(centro_explosion[1] + tanque.radioExplosion * math.sin(angle))
            puntosx.append(x)
            puntosy.append(y)
        return puntosx, puntosy

    def obtener_puntos_x_y(self, puntosx, puntosy):
        puntos_explosion = []
        for i in range(len(puntosx)):
            puntos_explosion.append((puntosx[i], puntosy[i]))
        puntos_x = [x for x, _ in puntos_explosion]
        puntos_y = [y for _, y in puntos_explosion]
        return puntos_x, puntos_y

    def actualizar_terreno(self, terreno, puntos_x, puntos_y):
        for i in range(len(puntos_x)):
            x = puntos_x[i]
            y = puntos_y[i]
            if self.es_punto_valido(x):
                y = Datos.PANT_ALTO - y
                if x < Datos.PANT_ANCHO and x > 0 and terreno.terreno[x] > y:
                    terreno.terreno[x] = y

    def es_punto_valido(self, x):
        return x < Datos.PANT_ANCHO and x > 0

