import pygame, Datos, Terreno
import math

class Bala:
    def __init__(self, pos_inicial_x, pos_inicial_y, angulo, velocidad_inicial, tipo):
        self.pos_inicial_x = pos_inicial_x
        self.pos_inicial_y = pos_inicial_y
        self.angulo = math.radians(angulo)
        self.velocidad_inicial = velocidad_inicial
        self.incremento = 0.05
        self.trayectoria = []
        self.pretrayectoria = []
        self.tipo = tipo
        if tipo == 1:
            self.imagen = pygame.image.load(f"Assets/bala105.png")
            self.imagen = pygame.transform.scale(self.imagen, (self.imagen.get_width() // 7, self.imagen.get_height() // 7))
            self.anguloBala = angulo
            self.imagen = pygame.transform.rotate(self.imagen, self.anguloBala)
        elif tipo == 2:
            self.imagen = pygame.image.load(f"Assets/bala80.png")
            self.imagen = pygame.transform.scale(self.imagen, (self.imagen.get_width() // 7, self.imagen.get_height() // 7))
            self.anguloBala = angulo
            self.imagen = pygame.transform.rotate(self.imagen, self.anguloBala)
        elif tipo == 3:
            self.imagen = pygame.image.load(f"Assets/bala60.png")
            self.imagen = pygame.transform.scale(self.imagen, (self.imagen.get_width() // 7, self.imagen.get_height() // 7))
            self.anguloBala = angulo
            self.imagen = pygame.transform.rotate(self.imagen, self.anguloBala)
        self.rect = self.imagen.get_rect()
        self.xanterior = pos_inicial_x
        self.yanterior = pos_inicial_y

    def calcular_posiciones(self, time):
        x = self.pos_inicial_x + self.velocidad_inicial * math.cos(self.angulo) * time
        y = self.pos_inicial_y - (self.velocidad_inicial * math.sin(self.angulo) * time - 0.5 * Datos.gravedad * time ** 2)
        return x, y

    def verificacion(self, tiempo, screen, color):
        self.tiempo = tiempo
        posiciones = self.calcular_posiciones(self.tiempo)
        self.trayectoria.append(posiciones)
        max_points = 1
        if len(self.trayectoria) > max_points:
            self.trayectoria.pop(0)
        for point in self.trayectoria:
            x2, y2 = point
            screen.blit(self.imagen, (x2, y2))

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
    
    def punto_maximo(self, valor=0):
        for punto in self.trayectoria:
            _ , y = punto
            y = y-540
            y = y * -1
            if y > valor:
                valor = y
        valor = int(valor)
        return valor
    
    def distancia_maxima(self, xt, valor=0):
        for punto in self.trayectoria:
            x, _ = punto
            valor = x - xt
            #si el valor de x es negativo, se convierte en positivo
            if valor < 0:
                valor = valor * -1
        valor = int(valor)
        return valor
    
    def visualizar(self):
        for punto in self.trayectoria:
            _, y = punto
            if y < 0:
                return True
        return False
    
    def xactual(self):
        for punto in self.trayectoria:
            x, _ = punto
            return x
        
    def verificar_impacto_tanque_explosion(self, tanque, puntosx, puntosy):
        for i in range(len(puntosx)):
            if (tanque.x <= puntosx[i] <= (tanque.x + tanque.ancho)) and (tanque.y <= puntosy[i] <= (tanque.y + tanque.altura)):
                return True
        return False
    
    def calcular_puntos_explosion(self, bala, radioExplosion):
        centroExplosion = Terreno.calcular_centro_explosion(bala)
        puntox = []
        puntoy = []
        for x in range(centroExplosion[0] - radioExplosion, centroExplosion[0] + radioExplosion + 1):
            for y in range(centroExplosion[1] - radioExplosion, centroExplosion[1] + radioExplosion + 1):
                if (x - centroExplosion[0])**2 + (y - centroExplosion[1])**2 <= radioExplosion**2:
                    puntox.append(x)
                    puntoy.append(y)
        return puntox, puntoy
    
    


    