import pygame, Datos, imagenes, Pantalla
import random
from Bala import Bala



class Tanque:
    def __init__(self, x, y, num, indice):
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
        self.indice = indice
        self.pivote = []

    def dibujar(self, screen):
        pygame.draw.rect(screen, Datos.RED, (self.x, self.y, self.ancho, self.altura))

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
    
    def crearTanques(terreno, bandera):

        if bandera:

            posX_Tanque = random.randint(0, Datos.PANT_ANCHO // 2)
            indice = posX_Tanque
            posY_Tanque = terreno.alto - terreno.terreno[indice] - 26
            tank1 = Pantalla.pantalla.tank1
            tanque = Tanque(posX_Tanque - 10, posY_Tanque + 10, tank1, indice)
            Datos.bandera_tanque = False

            return tanque

        else:
            posX_Tanque = random.randint(0, (Datos.PANT_ANCHO // 2 - 50))
            indice = ((Datos.PANT_ANCHO - 1) - posX_Tanque)    
            posY_Tanque = terreno.alto -  terreno.terreno[indice] - 24
            tank2 = Pantalla.pantalla.tank2
            tanque = Tanque(Datos.PANT_ANCHO - imagenes.Tanque2.get_width() - posX_Tanque + 20, posY_Tanque + 10, tank2, indice)

            return tanque
