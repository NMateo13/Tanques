import pygame, os, sys, math, random

class tanque:
    def __init__(self, x, y, numero):
        self.x = x
        self.y = y
        if numero == 1:
            self.imagen = self.load_image("Tanque1.png", "Assets", True)
        elif numero == 2:
            self.imagen = self.load_image("Tanque2.png", "Assets", True)
        elif numero == 3:
            self.imagen = self.load_image("Tanque3.png", "Assets", True)
        elif numero == 4:
            self.imagen = self.load_image("Tanque4.png", "Assets", True)
        self.imagen = pygame.transform.scale(self.imagen, (40, 40))
        self.rect = self.imagen.get_rect()
        self.rect.center = (self.x, self.y)

    def dibujar(self, screen):
        screen.blit(self.imagen, self.rect)

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

    def disparar(self):
        bala = Balas(self.x, self.y, angulo, velocidad_inicial, incremento)
        bala.verificar()
    
    def verificar_imagen(self):
        return self.imagen
    
