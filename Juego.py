import Pantalla, pygame, sys, Terreno

pygame.init()

font = pygame.font.Font(None, 36)
size = (Pantalla.pantalla.ancho, Pantalla.pantalla.alto)
screen = pygame.display.set_mode(size)
FPS = 60
Clock = pygame.time.Clock()
pygame.display.set_caption("Juego de Tanques")

while True:
    Clock.tick(FPS) #Controla la velocidad de la pantalla (FPS)
    for event in pygame.event.get(): 

        #print(event) linea de codigo que nos servira para saber que eventos ocurren en la pantalla 

        if event.type == pygame.QUIT: 
            sys.exit()

    screen.fill(Pantalla.pantalla.WHITE)
    pygame.draw.rect(screen, Pantalla.pantalla.GRAY, (0, 540, 1200, 120))

    #Zona de programación

    Pantalla.pantalla.crearMatriz(Pantalla.pantalla.alto, Pantalla.pantalla.ancho)
    Terreno.terreno.genTerreno(Terreno.terreno.Xpos, Terreno.terreno.Ypos)
    Pantalla.pantalla.dibujar(screen)
    Pantalla.pantalla.muestra_salud(screen, font)
    Pantalla.pantalla.muestra_potencia(screen, font)
    Pantalla.pantalla.muestra_angulo(screen, font)
    Pantalla.pantalla.muestra_jugador(screen, font)
    Pantalla.pantalla.muestra_tanques(screen)

    #Zona de programación

    pygame.display.flip()

