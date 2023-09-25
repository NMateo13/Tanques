import pygame, os, sys, math, random
from Bala import Bala

class Tanque:
    def __init__(self, x, y, color, num):
        self.x = x
        self.y = y
        self.color = color
        self.ancho = 60
        self.altura = 60
        if num == 1:
            imagen = self.load_image("Tanque1.png", "Assets", True)
            self.image = pygame.transform.scale(imagen, (imagen.get_width() // 4, imagen.get_height() // 4))
            self.num = 1
        elif num == 2:
            imagen = self.load_image("Tanque2.png", "Assets", True)
            self.image = pygame.transform.scale(imagen, (imagen.get_width() // 4, imagen.get_height() // 4))
            self.num = 2
        elif num == 3:
            imagen = self.load_image("Tanque3.png", "Assets", True)
            self.image = pygame.transform.scale(imagen, (imagen.get_width() // 4, imagen.get_height() // 4))
            self.num = 3
        elif num == 4:
            imagen = self.load_image("Tanque4.png", "Assets", True)
            self.image = pygame.transform.scale(imagen, (imagen.get_width() // 4, imagen.get_height() // 4))
            self.num = 4
        self.rect = self.image.get_rect()

    def dibujar(self, screen, color, ancho, altura, x, y, image):
        pygame.draw.rect(screen, color, (x, y, ancho, altura))
        screen.blit(image, (x, y))

    def disparar(self, pos_inicial_x, pos_inicial_y, angulo, velocidad_inicial, tiempo, ancho, screen, color):
        bala = Bala(pos_inicial_x, pos_inicial_y, angulo, velocidad_inicial)
        bala.verificacion(tiempo, ancho, screen, color)
        return bala

    def verificar_impacto(self, bala):
        # Verificar si la bala ha impactado en el rectángulo del tanque
        for punto in bala.trayectoria:
            x, y = punto
            if (self.x <= x <= (self.x + self.ancho)) and (self.y <= y <= (self.y + self.altura)):
                return True
        return False
    
    def load_image(self, nombre, dir_imagen, alpha_channel = False):
        ruta = os.path.join(dir_imagen, nombre)
        try:
            image = pygame.image.load(ruta)
        except:
            print("Error, no se puede cargar la imagen: ", ruta)
            sys.exit(1)
        if alpha_channel == True:
            image = image.convert_alpha()
        else:
            image = image.convert()
        return image