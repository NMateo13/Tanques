import Pantalla, pygame, sys

pygame.init()

size = (Pantalla.pantalla.ancho, Pantalla.pantalla.alto)
screen = pygame.display.set_mode(size)

while True:
    for event in pygame.event.get(): #Comienza a capturar todo evento que suceda en la pantalla

        #print(event) linea de codigo que nos servira para saber que eventos ocurren en la pantalla 

        if event.type == pygame.QUIT: #Cierra la pantalla al presionar el cerrar
            sys.exit()

    screen.fill(Pantalla.pantalla.WHITE)
    pygame.display.flip()




