import pygame, sys, os, random, math

class Canon:
    def __init__(self, tanque, canon_sprite_path):
        if tanque.num == 1:
            self.image = self.load_image("canon1.png", "Assets", True)
        elif tanque.num == 2:
            self.image = self.load_image("canon2.png", "Assets", True)
        elif tanque.num == 3:
            self.image = self.load_image("canon3.png", "Assets", True)
        elif tanque.num == 4:
            self.image = self.load_image("canon4.png", "Assets", True)
        self.rect = self.image.get_rect()
        self.angle = 0  # Ángulo inicial del cañón
        self.update_position(tanque)

    def update_position(self, tanque):
        # Calcular la posición del cañón con respecto al tanque
        self.rect.centerx = tanque.rect.centerx
        self.rect.centery = tanque.rect.centery

    def draw(self, screen):
        # Dibujar el cañón en la pantalla
        rotated_image = pygame.transform.rotate(self.image, self.angle)
        rotated_rect = rotated_image.get_rect(center=self.rect.center)
        screen.blit(rotated_image, rotated_rect)

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