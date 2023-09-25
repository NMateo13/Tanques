import pygame, sys, os, random, math

class Canon:
    def __init__(self, tanque, screen):
        if tanque.num == 1:
            imagen = self.load_image("canon1.png", "Assets", True)
            self.image = pygame.transform.scale(imagen, (imagen.get_width() // 4, imagen.get_height() // 4))
        elif tanque.num == 2:
            imagen = self.load_image("canon2.png", "Assets", True)
            self.image = pygame.transform.scale(imagen, (imagen.get_width() // 4, imagen.get_height() // 4))
        elif tanque.num == 3:
            imagen = self.load_image("canon3.png", "Assets", True)
            self.image = pygame.transform.scale(imagen, (imagen.get_width() // 4, imagen.get_height() // 4))
        elif tanque.num == 4:
            imagen = self.load_image("canon4.png", "Assets", True)
            self.image = pygame.transform.scale(imagen, (imagen.get_width() // 4, imagen.get_height() // 4))
        self.angle = 0  # Ángulo inicial del cañón

    def update_position(self, tanque, screen):
        # Calcular la posición del cañón con respecto al tanque
        screen.blit(self.image, (tanque.x + 20, tanque.y - 20))

    def draw(self, screen, tanque, angulo):
        # Dibujar el cañón en la pantalla
        #self.image = pygame.transform.rotate(self.image, angulo)
        #screen.blit(self.image,(tanque.x + 20, tanque.y - 20))
        surf = pygame.transform.rotate(self.image, angulo)
        offset = pygame.math.Vector2(20, -20)

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