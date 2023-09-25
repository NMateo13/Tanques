import pygame, sys, os, random

import pygame
import math

class Canon:
    def __init__(self, tank_rect, canon_sprite_path):
        self.image = pygame.image.load(canon_sprite_path).convert()  # Carga la imagen del cañón
        self.rect = self.image.get_rect()
        self.angle = 0  # Ángulo inicial del cañón
        self.tank_rect = tank_rect  # Rectángulo del tanque al que está asociado el cañón
        self.update_position()

    def update_position(self):
        # Calcular la posición del cañón con respecto al tanque
        self.rect.centerx = self.tank_rect.centerx
        self.rect.centery = self.tank_rect.centery

    def rotate(self, angle):
        # Girar el cañón según el ángulo proporcionado
        self.angle += angle
        self.angle = max(0, min(90, self.angle))  # Limitar el ángulo entre 0 y 90 grados

    def fire(self):
        # Lógica para disparar desde el cañón
        pass  # Agrega aquí la lógica de disparo

    def draw(self, screen):
        # Dibujar el cañón en la pantalla
        rotated_image = pygame.transform.rotate(self.image, self.angle)
        rotated_rect = rotated_image.get_rect(center=self.rect.center)
        screen.blit(rotated_image, rotated_rect)