import pygame, sys, os
from Bala import Bala
#Inicializa la libreria
pygame.init()

#Tamaño pantalla 
size = (800, 600)

#Definicion de colores para la pantalla
WHITE = (225, 225, 225)
RED = (255, 0 , 0)
#Creamos la pantalla del juego
screen = pygame.display.set_mode(size)


current_time = 0
clock = pygame.time.Clock()
disparo = Bala(150,500,50,100,9.8,0.03)
#Las pantallas se abren a traves de un ciclo
while True:
    for event in pygame.event.get(): #Comienza a capturar todo evento que suceda en la pantalla

        print(event) #linea de codigo que nos servira para saber que eventos ocurren en la pantalla

        if event.type == pygame.QUIT: #Cierra la pantalla al presionar el cerrar
            sys.exit()
    
    screen.fill(WHITE) #Coloca el color de fondo
    
    ###Zona de dibujo o programacion 
    
    disparo.verificacion(current_time,800,500,screen,RED)
    
    clock.tick(60)
    ##Zona de dibujo o programacion
    current_time += disparo.incremento
    pygame.display.flip() #Actualiza pantalla