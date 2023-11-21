import pygame, sys, os, random, math

class Canon:
    def __init__(self, tanque):
        if tanque.color == 1:
            imagen = self.load_image("canon1.png", "Assets", True)
            self.image = pygame.transform.scale(imagen, (imagen.get_width() // 4, imagen.get_height() // 4))
        elif tanque.color == 2:
            imagen = self.load_image("canon2.png", "Assets", True)
            self.image = pygame.transform.scale(imagen, (imagen.get_width() // 4, imagen.get_height() // 4))
        elif tanque.color == 3:
            imagen = self.load_image("canon3.png", "Assets", True)
            self.image = pygame.transform.scale(imagen, (imagen.get_width() // 4, imagen.get_height() // 4))
        elif tanque.color == 4:
            imagen = self.load_image("canon4.png", "Assets", True)
            self.image = pygame.transform.scale(imagen, (imagen.get_width() // 4, imagen.get_height() // 4))
        elif tanque.color == 5:
            imagen = self.load_image("canon5.png", "Assets", True)
            self.image = pygame.transform.scale(imagen, (imagen.get_width() // 4, imagen.get_height() // 4))
        elif tanque.color == 6:
            imagen = self.load_image("canon6.png", "Assets", True)
            self.image = pygame.transform.scale(imagen, (imagen.get_width() // 4, imagen.get_height() // 4))
        self.angle = 0  # Ángulo inicial del cañón

    def update_position(self, tanque, screen):
        # Calcular la posición del cañón con respecto al tanque
        screen.blit(self.image, (tanque.x, tanque.y))

    def draw(self, screen, tanque, angulo):
        # Dibujar el cañón en la pantalla
        self.image = pygame.transform.rotate(self.image, angulo)
        screen.blit(self.image,(tanque.x, tanque.y))
        

    def load_image(self, nombre, dir_imagen, alpha_channel = False):
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
