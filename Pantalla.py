import pygame, sys, os
from Tanque import tanque
#Inicializa la libreria
pygame.init()

#Tamaño pantalla 
size = (800, 500)

#Definicion de colores para la pantalla
WHITE = (225, 225, 225)

#Creamos la pantalla del juego
screen = pygame.display.set_mode(size)

#Las pantallas se abren a traves de un ciclo
while True:
    for event in pygame.event.get(): #Comienza a capturar todo evento que suceda en la pantalla

        #print(event) linea de codigo que nos servira para saber que eventos ocurren en la pantalla 

        if event.type == pygame.QUIT: #Cierra la pantalla al presionar el cerrar
            sys.exit()
    
    screen.fill(WHITE) #Coloca el color de fondo
    
    ###Zona de dibujo o programacion 
    tanque1 = tanque(100, 100)
    screen.blit(tanque1.imagen, tanque1.rect)

    ##Zona de dibujo o programacion

    pygame.display.flip() #Actualiza pantalla