import pygame, sys, Terreno, Pantalla, datos, imagenes, random
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

def draw_text(text, font, x, y):
    textobj = font.render(text, 1, datos.BLACK)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    screen.blit(textobj, textrect)

def menu():
    while True:
        screen.fill(datos.WHITE)
        draw_text('TANK WARS', fuente, (datos.PANT_ANCHO / 2) - 70, (datos.PANT_ALTO / 2) - 200)

        play_button = pygame.Rect((datos.PANT_ANCHO / 2) - 50, (datos.PANT_ALTO / 2) - 50, 100, 50)
        control_button = pygame.Rect((datos.PANT_ANCHO / 2) - 50, (datos.PANT_ALTO / 2) + 50, 100, 50)
        quit_button = pygame.Rect((datos.PANT_ANCHO / 2) - 50, (datos.PANT_ALTO / 2) + 150, 100, 50)

        draw_text('Jugar', fuente, (datos.PANT_ANCHO / 2) - 30, (datos.PANT_ALTO / 2) - 35)
        draw_text('Controles', fuente, (datos.PANT_ANCHO / 2) - 55, (datos.PANT_ALTO / 2) + 65)
        draw_text('Salir', fuente, (datos.PANT_ANCHO / 2) - 25, (datos.PANT_ALTO / 2) + 165)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.collidepoint(event.pos):
                    juego()
                if control_button.collidepoint(event.pos):
                    controles()
                if quit_button.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

def controles():
    while True:
        screen.fill(datos.WHITE)
        draw_text('Controles', fuente, (datos.PANT_ANCHO / 2) - 100, (datos.PANT_ALTO / 2) - 250)
        draw_text('Jugador 1', fuente, (datos.PANT_ANCHO / 2) - 550, (datos.PANT_ALTO / 2) - 200)
        draw_text('Jugador 2', fuente, (datos.PANT_ANCHO / 2), (datos.PANT_ALTO / 2) - 200)
        draw_text('W: Aumentar ángulo', fuente, (datos.PANT_ANCHO / 2) - 550, (datos.PANT_ALTO / 2) - 150)
        draw_text('Arriba: Aumentar ángulo', fuente, (datos.PANT_ANCHO / 2), (datos.PANT_ALTO / 2) - 150)
        draw_text('S: Disminuir ángulo', fuente, (datos.PANT_ANCHO / 2) - 550, (datos.PANT_ALTO / 2) - 100)
        draw_text('Abajo: Disminuir ángulo', fuente, (datos.PANT_ANCHO / 2), (datos.PANT_ALTO / 2) - 100)
        draw_text('A: Disminuir potencia', fuente, (datos.PANT_ANCHO / 2) - 550, (datos.PANT_ALTO / 2) - 50)
        draw_text('Izquierda: Disminuir potencia', fuente, (datos.PANT_ANCHO / 2), (datos.PANT_ALTO / 2) - 50)
        draw_text('D: Aumentar potencia', fuente, (datos.PANT_ANCHO / 2) - 550, (datos.PANT_ALTO / 2))
        draw_text('Derecha: Aumentar potencia', fuente, (datos.PANT_ANCHO / 2), (datos.PANT_ALTO / 2))
        draw_text('1: Bala 105mm   2: Bala 80mm   3: Bala 60mm', fuente, (datos.PANT_ANCHO / 2) - 550, (datos.PANT_ALTO / 2) + 100)
        draw_text('Espacio: Disparar', fuente, (datos.PANT_ANCHO / 2) - 550, (datos.PANT_ALTO / 2) + 150)
        draw_text('Para volver al menú presione Esc :)', fuente, (datos.PANT_ANCHO / 2) - 550, (datos.PANT_ALTO / 2) + 250)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                menu()


def juego():
    terreno = Terreno(datos.PANT_ANCHO, datos.PANT_ALTO)

    # Crear dos hitboxes

    posX_Tanque1 = random.randint(0, 550) 
    posX_Tanque2 = random.randint(0, 550)
    
    indice = posX_Tanque1
    indice2 = (1199 - posX_Tanque2)

    posY_Tanque1 = terreno.alto - terreno.terreno[indice] - 26

    posY_Tanque2 = 600 -  terreno.terreno[indice2] - 24
    while posY_Tanque2 < 0:
        posX_Tanque2 = random.randint(0, 550)
        indice2 = (1199 - posX_Tanque2)
        posY_Tanque1 = terreno.alto - terreno.terreno[indice] - 26



    tank1 = Pantalla.pantalla.tank1
    tank2 = Pantalla.pantalla.tank2
    tanque1 = Tanque(posX_Tanque1 - 10, posY_Tanque1 + 10, datos.RED, tank1)
    tanque2 = Tanque(datos.PANT_ANCHO - imagenes.Tanque2.get_width() - posX_Tanque2 + 20, posY_Tanque2 + 10, datos.RED, tank2)

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

    pivote1 = [posX_Tanque1 + 10, posY_Tanque1+5]
    pivote2 = [datos.PANT_ANCHO - imagenes.IMG_Canon2.get_width() - posX_Tanque2 + 5, posY_Tanque2+5]
            
    angulo_jugador1 = 30 # Ángulo inicial
    extremo_canonx_1, extremo_canony_1 = Pantalla.pantalla.prerotate(screen, 1, datos.ang_tank[angulo_jugador1], pivote1)
    velocidad_jugador1 = 50  # Velocidad inicial

    angulo_jugador2 = 30  # Ángulo inicial
    extremo_canonx_1, extremo_canony_1 =Pantalla.pantalla.prerotate(screen, 2, datos.ang_tank[angulo_jugador2]-90, pivote2)
    velocidad_jugador2 = 100  # Velocidad inicial

    tiempo_transcurrido = 0
    incremento = 0.035

    salir = screen.blit(imagenes.Exit, (Pantalla.pantalla.ancho - imagenes.Exit.get_width() - 650, 10))
    reset = screen.blit(imagenes.Restart, (Pantalla.pantalla.ancho - imagenes.Restart.get_width() - 550, 10))

    while True:
        Clock.tick(datos.FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if reset.collidepoint(pygame.mouse.get_pos()):
                    juego()  # Reiniciar el juego
                if salir.collidepoint(pygame.mouse.get_pos()):
                    menu()  # Volver al menú principal
        
        keys = pygame.key.get_pressed()

        if keys[pygame.K_ESCAPE]:
            menu()
        
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
        screen.blit(imagenes.HUD, (0, 480))
        tanque1.dibujar(screen)
        tanque2.dibujar(screen)



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



        Pantalla.pantalla.muestra_salud(screen, fuente)
        Pantalla.pantalla.muestra_potencia(screen, fuente,velocidad_jugador1,velocidad_jugador2)
        Pantalla.pantalla.muestra_angulo(screen, fuente,datos.ang_tank[angulo_jugador1-30],datos.ang_tank[angulo_jugador2-30])
        Pantalla.pantalla.muestra_texto(screen, fuente)
        Pantalla.pantalla.muestra_imagen(screen, tipo_bala1, tipo_bala2, posX_Tanque1, posX_Tanque2, posY_Tanque1, posY_Tanque2)
        Pantalla.pantalla.muestra_altura(screen, fuente, altura_maxima, mostrar_altura1, mostrar_altura2)
        extremo_canonx_1, extremo_canony_1 = Pantalla.pantalla.prerotate(screen, 1, -(datos.ang_tank[angulo_jugador1]-90), pivote1)
        extremo_canonx_2, extremo_canony_2 = Pantalla.pantalla.prerotate(screen, 2, -(datos.ang_tank[angulo_jugador2]-90), pivote2)
        pygame.display.flip()

menu()