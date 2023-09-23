import Pantalla, pygame, sys, Terreno
from Bala import Bala
pygame.init()

current_time = 0
font = pygame.font.Font(None, 36)
size = (Pantalla.pantalla.ancho, Pantalla.pantalla.alto)
screen = pygame.display.set_mode(size)
FPS = 60
Clock = pygame.time.Clock()
disparo = Bala(300,350,20,100,9.8,0.5)
pygame.display.set_caption("Juego de Tanques")
pygame.display.set_icon(Pantalla.pantalla.IMG_Explosion)

while True:
    Clock.tick(FPS) #Controla la velocidad de la pantalla (FPS)
    for event in pygame.event.get(): 

        #print(event) linea de codigo que nos servira para saber que eventos ocurren en la pantalla 

        if event.type == pygame.QUIT: 
            sys.exit()    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                tecla_espacio_presionada = True
    #Zona de programación  
    screen.fill(Pantalla.pantalla.WHITE)
    screen.blit(Pantalla.pantalla.Background, (0, 0))
    screen.blit(Pantalla.pantalla.HUD, (0, 540))

    #Zona de programación
    disparo.verificacion(current_time,1200,600,screen,Pantalla.pantalla.BLACK)
    Pantalla.pantalla.crearMatriz(Pantalla.pantalla.alto, Pantalla.pantalla.ancho)
    Terreno.terreno.genTerreno(Terreno.terreno.Xpos, Terreno.terreno.Ypos)
    Pantalla.pantalla.dibujar(screen)
    Pantalla.pantalla.muestra_salud(screen, font)
    Pantalla.pantalla.muestra_potencia(screen, font)
    Pantalla.pantalla.muestra_angulo(screen, font)
    Pantalla.pantalla.muestra_texto(screen, font)
    Pantalla.pantalla.muestra_imagen(screen)
    current_time += disparo.incremento

    #Zona de programación
    pygame.display.flip()

