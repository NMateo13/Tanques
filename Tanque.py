import pygame, datos, imagenes, Pantalla
import random
from Bala import Bala



class Tanque:
    def __init__(self, x, y, num):
        self.x = x
        self.y = y
        self.ancho = 60
        self.altura = 10 
        self.num = num
        self.vida = 100 # vida tanque
        self.cantBala60mm = 3 #cantidad de balas 
        self.cantBala80mm = 10
        self.cantBala105mm = 3
        self.Bala60mm = 30 # daño de las balas
        self.Bala80mm = 40
        self.Bala105mm = 50

    def dibujar(self, screen):
        pygame.draw.rect(screen, datos.RED, (self.x, self.y, self.ancho, self.altura))

    def disparar(self, pos_inicial_x, pos_inicial_y, angulo, velocidad_inicial, tiempo, screen, color, tipo_bala):
        bala = Bala(pos_inicial_x, pos_inicial_y, angulo, velocidad_inicial, tipo_bala  )
        if tipo_bala == 1:
            bala.verificacion(tiempo, screen, color)
            self.cantBala105mm -= 1
            print(self.cantBala105mm)
            return bala
        elif tipo_bala == 2:
            bala.verificacion(tiempo, screen, color)
            self.cantBala80mm -= 1
            print(self.cantBala80mm)
            return bala
        elif tipo_bala == 3:
            bala.verificacion(tiempo, screen, color)
            self.cantBala60mm -= 1
            print(self.cantBala60mm)
            return bala

    def ia(self):
        #61 valores disponibles en el arrayist ang_tank
        #numero aleatorio entre 0 y 60
        angulo = random.randint(0, 60)
        #Velocidad aleatoria entre 0 y 150 
        velocidad = random.randint(0, 150)
        #Tipo de bala aleatoria entre 1 y 3
        if self.cantBala105mm == 0:
            tipo_bala = random.randint(2, 3)
        elif self.cantBala80mm == 0:
            tipo_bala = random.randint(1, 3)
            while tipo_bala == 2:
                tipo_bala = random.randint(1, 3)
        elif self.cantBala60mm == 0:
            tipo_bala = random.randint(1, 2)
        elif self.cantBala105mm == 0 and self.cantBala80mm == 0:
            tipo_bala = 3
        elif self.cantBala105mm == 0 and self.cantBala60mm == 0:
            tipo_bala = 2
        elif self.cantBala80mm == 0 and self.cantBala60mm == 0:
            tipo_bala = 1
        else:
            tipo_bala = random.randint(1, 3)
        return angulo, velocidad, tipo_bala
    
    def crearTanques(self, terreno):

        posX_Tanque1 = random.randint(0, 550) 
        posX_Tanque2 = random.randint(0, 550)

        indice = posX_Tanque1
        indice2 = (1199 - posX_Tanque2)

        posY_Tanque1 = terreno.alto - terreno.terreno[indice] - 26
        posY_Tanque2 = 600 -  terreno.terreno[indice2] - 24
        while posY_Tanque2 < 0:
            posX_Tanque2 = random.randint(0, 550)
            indice2 = (1199 - posX_Tanque2)
           
        tank1 = Pantalla.pantalla.tank1 #Imagenes tanques
        tank2 = Pantalla.pantalla.tank2 #Imagenes tanques 

        tanque1 = Tanque(posX_Tanque1 - 10, posY_Tanque1 + 10, tank1) #Muestra visualmente los tanques
        tanque2 = Tanque(datos.PANT_ANCHO - imagenes.Tanque2.get_width() - posX_Tanque2 + 20, posY_Tanque2 + 10, tank2) 

        return tanque1, tanque2
