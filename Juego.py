import pygame, sys, Terreno, Pantalla, datos, imagenes
from Bala import Bala
from Tanque import Tanque
from Terreno import Terreno
from Canon import Canon

pygame.init()
pygame.display.set_caption("TANK WARS") 
pygame.display.set_icon(imagenes.IMG_Explosion) 

fuente = pygame.font.Font(None, 36)
size = (datos.PANT_ANCHO, datos.PANT_ALTO)
screen = pygame.display.set_mode(size)
terreno = Terreno(datos.PANT_ANCHO, datos.PANT_ALTO)

# Crear dos hitboxes
tank1 = Pantalla.pantalla.tank1
tank2 = Pantalla.pantalla.tank2
tanque1 = Tanque(Pantalla.pantalla.posX_Tanque1, Pantalla.pantalla.posY_Tanque1 + 10, datos.RED, tank1)
tanque2 = Tanque(datos.PANT_ANCHO - imagenes.Tanque2.get_width() - Pantalla.pantalla.posX_Tanque2, Pantalla.pantalla.posY_Tanque2 + 10, datos.RED, tank2)

bala_tanque1 = None
bala_tanque2 = None

canon1 = Canon(tanque1)
canon2 = Canon(tanque2)

#Inicio de variables para elegir el tipo de bala
tipo_bala1 = 1
tipo_bala2 = 1

turno1 = True
turno2 = False

extremo_canonx_1 = 0
extremo_canony_1 = 0
extremo_canonx_2 = 0
extremo_canony_2 = 0

mostrar_altura1 = False
mostrar_altura2 = False
altura_maxima = 0

Clock = pygame.time.Clock()
tecla_espacio_presionada = False

pivote1 = [Pantalla.pantalla.posX_Tanque1 + 20, Pantalla.pantalla.posY_Tanque1+5]
pivote2 = [datos.PANT_ANCHO - imagenes.IMG_Canon2.get_width() - Pantalla.pantalla.posX_Tanque2 - 15, Pantalla.pantalla.posY_Tanque2+5]
        
angulo_jugador1 = 30 # Ángulo inicial
extremo_canonx_1, extremo_canony_1 = Pantalla.pantalla.prerotate(screen, 1, datos.ang_tank[angulo_jugador1], pivote1)
velocidad_jugador1 = 50  # Velocidad inicial

angulo_jugador2 = 30  # Ángulo inicial
extremo_canonx_1, extremo_canony_1 =Pantalla.pantalla.prerotate(screen, 2, datos.ang_tank[angulo_jugador2]-90, pivote2)
velocidad_jugador2 = 100  # Velocidad inicial

tiempo_transcurrido = 0
incremento = 0.035

while True:
    Clock.tick(datos.FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_SPACE]:
        tecla_espacio_presionada = True
    
    # Controles del jugador 1
    if turno1:
        if keys[pygame.K_w]:
            if angulo_jugador1 == 66:
                angulo_jugador1 = 0
            else:
                angulo_jugador1 += 1
        elif keys[pygame.K_s]:
            if angulo_jugador1 == 0:
                angulo_jugador1 = 66
            else:
                angulo_jugador1 -= 1
        elif keys[pygame.K_a]:
            velocidad_jugador1 -= 5
            velocidad_jugador1 = max(0, velocidad_jugador1)
        elif keys[pygame.K_d]:
            velocidad_jugador1 += 5
            velocidad_jugador1 = min(150, velocidad_jugador1)

        # Cambio de bala J1
        elif keys[pygame.K_1]:
            tipo_bala1 = 1
        elif keys[pygame.K_2]:
            tipo_bala1 = 2
        elif keys[pygame.K_3]:
            tipo_bala1 = 3

    # Controles del jugador 2
    if turno2:
        if keys[pygame.K_UP]:
            if angulo_jugador2 == 66:
                angulo_jugador2 = 0
            else:
                angulo_jugador2 += 1
        elif keys[pygame.K_DOWN]:
            if angulo_jugador2 == 0:
                angulo_jugador2 = 66
            else:
                angulo_jugador2 -= 1
        elif keys[pygame.K_LEFT]:
            velocidad_jugador2 -= 5
            velocidad_jugador2 = max(0, velocidad_jugador2)
        elif keys[pygame.K_RIGHT]:
            velocidad_jugador2 += 5
            velocidad_jugador2 = min(150, velocidad_jugador2)

        # Cambio de bala J2
        elif keys[pygame.K_1]:
            tipo_bala2 = 1
        elif keys[pygame.K_2]:
            tipo_bala2 = 2
        elif keys[pygame.K_3]:
            tipo_bala2 = 3

    screen.blit(imagenes.Background, (0, 0))
    terreno.dibujar(screen)
    screen.blit(datos.HUD, (0, 540))
    #tanque1.dibujar(screen)
    #tanque2.dibujar(screen)

    if tecla_espacio_presionada and turno1:
        if bala_tanque1 is None:
            mostrar_altura1 = True
            mostrar_altura2 = False
            altura_maxima = 0
            bala_tanque1 = tanque1.disparar(extremo_canonx_1, extremo_canony_1, datos.ang_tank[angulo_jugador1], velocidad_jugador1, tiempo_transcurrido, screen, datos.BLACK, tipo_bala1)
        else:
            altura_maxima = bala_tanque1.punto_maximo(altura_maxima)
            bala_tanque1.verificacion(tiempo_transcurrido, screen, datos.BLACK)
            impacto_tanque = bala_tanque1.verificar_impacto_tanque(tanque2)
            impacto_terreno = terreno.verificar_colision(bala_tanque1)
            impacto_borde = bala_tanque1.verificar_impacto_ancho(datos.PANT_ANCHO)
            if impacto_tanque:
                sys.exit()  # Cierra el programa si hubo impacto
            elif impacto_borde or impacto_terreno:
                bala_tanque1 = None
                tecla_espacio_presionada = False
                turno1 = False
                turno2 = True
                tiempo_transcurrido = 0

        tiempo_transcurrido += incremento

    if tecla_espacio_presionada and turno2:
        if bala_tanque2 is None:
            mostrar_altura1 = False
            mostrar_altura2 = True
            altura_maxima = 0
            bala_tanque2 = tanque1.disparar(extremo_canonx_2, extremo_canony_2, datos.ang_tank[angulo_jugador2], velocidad_jugador2, tiempo_transcurrido, screen, datos.BLACK, tipo_bala2)
        else:
            altura_maxima = bala_tanque2.punto_maximo(altura_maxima)
            bala_tanque2.verificacion(tiempo_transcurrido, screen, datos.BLACK)
            impacto_tanque = bala_tanque2.verificar_impacto_tanque(tanque1)
            impacto_terreno = terreno.verificar_colision(bala_tanque2)
            impacto_borde = bala_tanque2.verificar_impacto_ancho(datos.PANT_ANCHO)
            if impacto_tanque:
                sys.exit()  # Cierra el programa si hubo impacto
            elif impacto_borde or impacto_terreno:
                bala_tanque2 = None
                tecla_espacio_presionada = False
                turno2 = False
                turno1 = True
                tiempo_transcurrido = 0
                 
        tiempo_transcurrido += incremento

    Pantalla.pantalla.muestra_salud(screen, font)
    Pantalla.pantalla.muestra_potencia(screen, font,velocidad_jugador1,velocidad_jugador2)
    Pantalla.pantalla.muestra_angulo(screen, font,datos.ang_tank[angulo_jugador1-30],datos.ang_tank[angulo_jugador2-30])
    Pantalla.pantalla.muestra_texto(screen, font)
    #Pantalla.pantalla.muestra_imagen(screen, tipo_bala1, tipo_bala2)
    Pantalla.pantalla.muestra_altura(screen, font, altura_maxima, mostrar_altura1, mostrar_altura2)
    #extremo_canonx_1, extremo_canony_1 = Pantalla.pantalla.prerotate(screen, 1, -(datos.ang_tank[angulo_jugador1]-90), pivote1)
    #extremo_canonx_2, extremo_canony_2 = Pantalla.pantalla.prerotate(screen, 2, -(datos.ang_tank[angulo_jugador2]-90), pivote2)
    pygame.display.flip()
