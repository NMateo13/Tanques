import pygame, sys, Terreno, random, math
from Bala import Bala
from Tanque import Tanque
from Canon import Canon
import Pantalla
pygame.init()

angulo = 0
velocidad_rotacion = 5
current_time = 0
font = pygame.font.Font(None, 36)
size = (Pantalla.pantalla.ancho, Pantalla.pantalla.alto)
screen = pygame.display.set_mode(size)
FPS = 60
Clock = pygame.time.Clock()
disparo = Bala(300,350,20,100,9.8,0.5)
pygame.display.set_caption("Juego de Tanques")
pygame.display.set_icon(Pantalla.pantalla.IMG_Explosion)
num1 = random.randint(1, 4)
num2 = random.randint(1, 4)
while num1 == num2:
    num2 = random.randint(1, 4)


while True:
    Clock.tick(FPS) #Controla la velocidad de la pantalla (FPS)
    for event in pygame.event.get(): 

        #print(event) #linea de codigo que nos servira para saber que eventos ocurren en la pantalla 

        if event.type == pygame.QUIT: 
            sys.exit()

    screen.fill(Pantalla.pantalla.WHITE)
    screen.blit(Pantalla.pantalla.Background, (0, 0))
    screen.blit(Pantalla.pantalla.HUD, (0, 540))
    tanque1 = Tanque(300, 350, Pantalla.pantalla.RED, num1)
    tanque2 = Tanque(900, 350, Pantalla.pantalla.GREEN, num2)
    tanque1.dibujar(screen, tanque1.color, tanque1.ancho, tanque1.altura, tanque1.x, tanque1.y, tanque1.image)
    tanque2.dibujar(screen, tanque2.color, tanque2.ancho, tanque2.altura, tanque2.x, tanque2.y, tanque2.image)
    canon1 = Canon(tanque1, screen)
    canon2 = Canon(tanque2, screen)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        angulo += velocidad_rotacion
    if keys[pygame.K_RIGHT]:
        angulo -= velocidad_rotacion
    canon1.draw(screen, tanque1, angulo)
    #Zona de programación
    #disparo.verificacion(current_time,1200,600,screen,Pantalla.pantalla.BLACK)
    Pantalla.pantalla.crearMatriz(Pantalla.pantalla.alto, Pantalla.pantalla.ancho)
    Terreno.terreno.genTerreno(Terreno.terreno.Xpos, Terreno.terreno.Ypos)
    Pantalla.pantalla.dibujar(screen)
    Pantalla.pantalla.muestra_salud(screen, font)
    Pantalla.pantalla.muestra_potencia(screen, font)
    Pantalla.pantalla.muestra_angulo(screen, font)
    Pantalla.pantalla.muestra_texto(screen, font)
    current_time += disparo.incremento

    #Zona de programación
    pygame.display.flip()

