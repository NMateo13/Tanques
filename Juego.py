import Pantalla, pygame, sys, Terreno
from Bala import Bala
from Tanque import Tanque

pygame.init()

font = pygame.font.Font(None, 36)
size = (Pantalla.pantalla.ancho, Pantalla.pantalla.alto)
screen = pygame.display.set_mode(size)
FPS = 60

# Crear dos tanques
tanque1 = Tanque(280, 360, Pantalla.pantalla.RED)
tanque2 = Tanque(850, 370, Pantalla.pantalla.RED)

bala_tanque1 = None

Clock = pygame.time.Clock()
tecla_espacio_presionada = False

tiempo_transcurrido = 0
incremento = 0.5
while True:
    Clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN: #Tecla espacio para disparar 
            if event.key == pygame.K_SPACE:
                tecla_espacio_presionada = True

    screen.fill(Pantalla.pantalla.WHITE)
    screen.blit(Pantalla.pantalla.Background, (0, 0))
    screen.blit(Pantalla.pantalla.HUD, (0, 540))

    tanque1.dibujar(screen)
    tanque2.dibujar(screen)

    if tecla_espacio_presionada:
        if bala_tanque1 is None:
            bala_tanque1 = tanque1.disparar(300, 375, 20, 94, tiempo_transcurrido, Pantalla.pantalla.ancho, screen, Pantalla.pantalla.BLACK)
        else:
            bala_tanque1.verificacion(tiempo_transcurrido, Pantalla.pantalla.ancho, screen, Pantalla.pantalla.BLACK)
            impacto = tanque2.verificar_impacto(bala_tanque1)
            if impacto:
                sys.exit()  # Cierra el programa si hubo impacto



        tiempo_transcurrido += incremento

    Pantalla.pantalla.crearMatriz(Pantalla.pantalla.alto, Pantalla.pantalla.ancho)
    Terreno.terreno.genTerreno(Terreno.terreno.Xpos, Terreno.terreno.Ypos)
    Pantalla.pantalla.dibujar(screen)
    Pantalla.pantalla.muestra_salud(screen, font)
    Pantalla.pantalla.muestra_potencia(screen, font)
    Pantalla.pantalla.muestra_angulo(screen, font)
    Pantalla.pantalla.muestra_texto(screen, font)
    Pantalla.pantalla.muestra_imagen(screen)
    
    pygame.display.flip()
