import pygame, os, sys, math, random

class tanque:
    def __init__(self, x, y, numero):
        self.x = x
        self.y = y
        self.imagen = self.load_image("Tanque4.png", "Assets", True)
        self.imagen = pygame.transform.scale(self.imagen, (40, 40))
        self.rect = self.imagen.get_rect()
        self.rect.center = (self.x, self.y)

    def dibujar(self):
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
        bala = Balas(self.x, self.y)
        bala.dibujar()
        bala.mover(self.velocidad_x)
