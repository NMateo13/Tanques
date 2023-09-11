import Pantalla, pygame, sys, Terreno

pygame.init()

size = (Pantalla.pantalla.ancho, Pantalla.pantalla.alto)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Juego de Tanques")

while True:
    for event in pygame.event.get(): 

        #print(event) linea de codigo que nos servira para saber que eventos ocurren en la pantalla 

        if event.type == pygame.QUIT: 
            sys.exit()

    screen.fill(Pantalla.pantalla.WHITE)


    #Zona de programación

    Pantalla.pantalla.crearMatriz(Pantalla.pantalla.alto, Pantalla.pantalla.ancho)
    Terreno.terreno.genTerreno(Terreno.terreno.Xpos, Terreno.terreno.Ypos)
    Pantalla.pantalla.dibujar(screen)

    #Rectángulo con medidas del HUD
    pygame.draw.rect(screen, Pantalla.pantalla.GRAY, (0, 540, 1200, 120))


    #Zona de programación


    pygame.display.flip()




