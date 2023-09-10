import pygame

class Pantalla:

    WHITE = (225, 225, 225)
    BLACK = (0, 0, 0)
    GREEN = (0, 153, 0)
    GRAY = (128, 139, 150)

    medidaHUD = 120

    def __init__(self, ancho, alto):
        
        self.ancho = ancho
        self.alto = alto

    
    def crearMatriz(self, alto, ancho):

        Pantalla.matriz = [[0] * ancho for _ in range(alto - Pantalla.medidaHUD)]

    def dibujar(self, screen):
        
        for filas in range(0, (pantalla.alto - pantalla.medidaHUD)):
            for columnas in range (0, pantalla.ancho):
                if pantalla.matriz[filas][columnas] == 1:
                    pygame.draw.rect(screen, pantalla.GREEN, (columnas, filas, 6, 6))

        
pantalla = Pantalla(1200, 660)
matriz = []

    
