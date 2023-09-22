import pygame
import math
from Bala import Bala
pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Animación de Trayectoria")

WHITE = (255, 255, 255)
RED = (255, 0, 0)
COLOR = (0, 0, 255)
fps = 60
disparo = Bala(100,350,20,100)
running = True
clock = pygame.time.Clock()
current_time = 0
tecla_espacio_presionada = False      
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                tecla_espacio_presionada = True
                print("hola")
            
    
    screen.fill(WHITE)
    if tecla_espacio_presionada:
        disparo.verificacion(current_time,1200,600,screen,RED)
    pygame.display.flip()
    current_time += disparo.incremento
    clock.tick(fps)
pygame.quit()
