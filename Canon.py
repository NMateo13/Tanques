import pygame, sys, os, random, math
from Tanque import Tanque

class Canon:

    canones = []

    def __init__(self):
        self.imagen = None
        self.angle = 0  # Ángulo inicial del cañón

    def update_position(self, tanque, screen):
        # Calcular la posición del cañón con respecto al tanque
        screen.blit(self.image, (tanque.x + 20, tanque.y - 20))

    def draw(self, screen, tanque, angulo):
        # Dibujar el cañón en la pantalla
        self.image = pygame.transform.rotate(self.image, angulo)
        screen.blit(self.image,(tanque.x + 20, tanque.y - 20))
        

    def load_imagen(self, nombre, dir_imagen, alpha_channel = False):
        ruta = os.path.join(dir_imagen, nombre)
        try:
            image = pygame.image.load(ruta)
        except:
            print("Error, no se puede cargar la imagen:  ", ruta)
            sys.exit(1)
        if alpha_channel == True:
            image = image.convert_alpha()
        else:
            image = image.convert()
        return image

    def definirCanon():
        for tanque in Tanque.tanques:
            if tanque.color == 1:
                canon = Canon()
                imagen = canon.load_imagen("canon1.png", "Assets", True)
                canon.imagen = pygame.transform.scale(imagen, (imagen.get_width() // 4, imagen.get_height() // 4))
                Canon.canones.append(canon)
            elif tanque.color == 2:
                canon = Canon()
                imagen = canon.load_imagen("canon2.png", "Assets", True)
                canon.imagen = pygame.transform.scale(imagen, (imagen.get_width() // 4, imagen.get_height() // 4))
                Canon.canones.append(canon)
            elif tanque.color == 3:
                canon = Canon()
                imagen = canon.load_imagen("canon3.png", "Assets", True)
                canon.imagen = pygame.transform.scale(imagen, (imagen.get_width() // 4, imagen.get_height() // 4))
                Canon.canones.append(canon) 
            elif tanque.color == 4:
                canon = Canon()
                imagen = canon.load_imagen("canon4.png", "Assets", True)
                canon.imagen = pygame.transform.scale(imagen, (imagen.get_width() // 4, imagen.get_height() // 4))
                Canon.canones.append(canon)
            elif tanque.color == 5:
                canon = Canon()
                imagen = canon.load_imagen("canon5.png", "Assets", True)
                canon.imagen = pygame.transform.scale(imagen, (imagen.get_width() // 4, imagen.get_height() // 4))
                Canon.canones.append(canon)
            elif tanque.color == 6:
                canon = Canon()
                imagen = canon.load_imagen("canon6.png", "Assets", True)
                canon.imagen = pygame.transform.scale(imagen, (imagen.get_width() // 4, imagen.get_height() // 4))
                Canon.canones.append(canon)