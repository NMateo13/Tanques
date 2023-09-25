import Pantalla, pygame, sys, Terreno
from Bala import Bala
from Tanque import Tanque
from Terreno import Terreno

pygame.init()
pygame.display.set_caption("Juego de Tanques") 
pygame.display.set_icon(Pantalla.pantalla.IMG_Explosion) 

font = pygame.font.Font(None, 36)
size = (Pantalla.pantalla.ancho, Pantalla.pantalla.alto)
screen = pygame.display.set_mode(size)
FPS = 60
terreno = Terreno(Pantalla.pantalla.ancho, Pantalla.pantalla.alto)

# Crear dos hitboxes (NO TOCAR)
tanque1 = Tanque(Pantalla.pantalla.posX_Tanque1, Pantalla.pantalla.posY_Tanque1 + 10, Pantalla.pantalla.RED)
tanque2 = Tanque(Pantalla.pantalla.ancho - Pantalla.pantalla.Tanque2.get_width() - Pantalla.pantalla.posX_Tanque2, Pantalla.pantalla.posY_Tanque2 + 10, Pantalla.pantalla.RED)

bala_tanque1 = None
bala_tanque2 = None

turno1 = True
turno2 = False

Clock = pygame.time.Clock()
tecla_espacio_presionada = False

angulo_jugador1 = 45  # Ángulo inicial
velocidad_jugador1 = 50  # Velocidad inicial

angulo_jugador2 = 135  # Ángulo inicial
velocidad_jugador2 = 100  # Velocidad inicial

tiempo_transcurrido = 0
incremento = 0.035

while True:
    Clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN: #Tecla espacio para disparar 
            if event.key == pygame.K_SPACE:
                tecla_espacio_presionada = True
            #Controles jugador 1
            elif event.key == pygame.K_w:
                angulo_jugador1 += 5
                angulo_jugador1 = min(90, angulo_jugador1) 
            elif event.key == pygame.K_s:
                angulo_jugador1 -= 5
                angulo_jugador1 = max(0, angulo_jugador1)   
            elif event.key == pygame.K_a:
                velocidad_jugador1 -= 5
                velocidad_jugador1 = max(0, velocidad_jugador1)
            elif event.key == pygame.K_d:
                velocidad_jugador1 += 5
                velocidad_jugador1 = min(100, velocidad_jugador1)

            #Controles jugador 2    
            elif event.key == pygame.K_UP:
                angulo_jugador2 += 5
                angulo_jugador2 = min(180, angulo_jugador2) 
            elif event.key == pygame.K_DOWN:
                angulo_jugador2 -= 5
                angulo_jugador2 = max(0, angulo_jugador2)   
            elif event.key == pygame.K_LEFT:
                velocidad_jugador2 -= 5
                velocidad_jugador2 = max(0, velocidad_jugador2)
            elif event.key == pygame.K_RIGHT:
                velocidad_jugador2 += 5
                velocidad_jugador2 = min(100, velocidad_jugador2)

    screen.fill(Pantalla.pantalla.WHITE)
    screen.blit(Pantalla.pantalla.Background, (0, 0))
    terreno.dibujar(screen)
    screen.blit(Pantalla.pantalla.HUD, (0, 540))
    tanque1.dibujar(screen)
    tanque2.dibujar(screen)

    if tecla_espacio_presionada and turno1:
        if bala_tanque1 is None:
            bala_tanque1 = tanque1.disparar(tanque1.x, tanque1.y, angulo_jugador1, velocidad_jugador1, tiempo_transcurrido, screen, Pantalla.pantalla.BLACK)
        else:
            bala_tanque1.verificacion(tiempo_transcurrido, screen, Pantalla.pantalla.BLACK)
            impacto_tanque = bala_tanque1.verificar_impacto_tanque(tanque2)
            impacto_terreno = terreno.verificar_colision(bala_tanque1)
            impacto_borde = bala_tanque1.verificar_impacto_ancho(Pantalla.pantalla.ancho)
            if impacto_tanque:
                sys.exit()  # Cierra el programa si hubo impacto
            elif impacto_borde:
                bala_tanque1 = None
                tecla_espacio_presionada = False
                turno1 = False
                turno2 = True
                tiempo_transcurrido = 0
            elif impacto_terreno:
                tecla_espacio_presionada = False
                bala_tanque1 = None
                tecla_espacio_presionada = False
                turno1 = False
                turno2 = True
                tiempo_transcurrido = 0

        tiempo_transcurrido += incremento

    if tecla_espacio_presionada and turno2:
        if bala_tanque2 is None:
            bala_tanque2 = tanque1.disparar(tanque2.x, tanque2.y, angulo_jugador2, velocidad_jugador2, tiempo_transcurrido, screen, Pantalla.pantalla.BLACK)
        else:
            bala_tanque2.verificacion(tiempo_transcurrido, screen, Pantalla.pantalla.BLACK)
            impacto_tanque = bala_tanque2.verificar_impacto_tanque(tanque1)
            impacto_terreno = terreno.verificar_colision(bala_tanque2)
            impacto_borde = bala_tanque2.verificar_impacto_ancho(Pantalla.pantalla.ancho)
            if impacto_tanque:
                sys.exit()  # Cierra el programa si hubo impacto
            elif impacto_borde:
                bala_tanque2 = None
                tecla_espacio_presionada = False
                turno2 = False
                turno1 = True
                tiempo_transcurrido = 0
            elif impacto_terreno:
                bala_tanque2 = None
                tecla_espacio_presionada = False
                turno2 = False
                turno1 = True
                tiempo_transcurrido = 0
                
        tiempo_transcurrido += incremento

    Pantalla.pantalla.muestra_salud(screen, font)
    Pantalla.pantalla.muestra_potencia(screen, font,velocidad_jugador1,velocidad_jugador2)
    Pantalla.pantalla.muestra_angulo(screen, font,angulo_jugador1,angulo_jugador2)
    Pantalla.pantalla.muestra_texto(screen, font)
    Pantalla.pantalla.muestra_imagen(screen)
    
    pygame.display.flip()