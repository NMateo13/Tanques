import pygame, imagenes, Datos, Juego, sys

pygame.init()
pygame.display.set_icon(imagenes.IMG_Explosion) 
pygame.display.set_caption("PROYECTO TANQUE")
pygame.mixer.music.load('Assets/musica1.mp3')
pygame.mixer.music.set_volume(Datos.volumen)
#pygame.mixer.music.play(-1)
fuente = pygame.font.Font(None, 36)
size = (Datos.PANT_ANCHO, Datos.PANT_ALTO)
screen = pygame.display.set_mode(size)
reset = 0

def draw_text(text, font, x, y, color):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    screen.blit(textobj, textrect)

def seleccion(screen):
    j1_v,j2_v,j3_v,j4_v,j5_v,j6_v = 0,0,0,0,0,0
    while True:
        salir = False
        screen.blit(imagenes.FondoMenu_seleccion, (0, 0))
        #las divisiones son para que queden exactamente separados los rectangulos independiente de la resolucion
        pygame.draw.rect(screen, Datos.BLACK, (Datos.PANT_ANCHO / 10 , Datos.PANT_ALTO / 10, 100, 100))
        pygame.draw.rect(screen, Datos.BLACK, (Datos.PANT_ANCHO / 3, Datos.PANT_ALTO / 10, 100, 100))
        pygame.draw.rect(screen, Datos.BLACK, (Datos.PANT_ANCHO / 1.764, Datos.PANT_ALTO / 10, 100, 100))
        pygame.draw.rect(screen, Datos.BLACK, (Datos.PANT_ANCHO / 10, Datos.PANT_ALTO / 2, 100, 100))
        pygame.draw.rect(screen, Datos.BLACK, (Datos.PANT_ANCHO / 3, Datos.PANT_ALTO / 2, 100, 100))
        pygame.draw.rect(screen, Datos.BLACK, (Datos.PANT_ANCHO / 1.764, Datos.PANT_ALTO / 2, 100, 100))

        draw_text('1', fuente, Datos.PANT_ANCHO / 10, Datos.PANT_ALTO / 10, Datos.WHITE)
        draw_text('2', fuente, Datos.PANT_ANCHO / 3, Datos.PANT_ALTO / 10, Datos.WHITE)
        draw_text('3', fuente, Datos.PANT_ANCHO / 1.764, Datos.PANT_ALTO / 10, Datos.WHITE)
        draw_text('4', fuente, Datos.PANT_ANCHO / 10, Datos.PANT_ALTO / 2, Datos.WHITE)
        draw_text('5', fuente, Datos.PANT_ANCHO / 3, Datos.PANT_ALTO / 2, Datos.WHITE)
        draw_text('6', fuente, Datos.PANT_ANCHO / 1.764, Datos.PANT_ALTO / 2, Datos.WHITE)

        #justo debajo de los rectangulos se debe mostrar otro rectangulo de altura 20 y ancho 100 que muestre mediante texto si es jugador o IA y que responda a los clicks para cambiar entre uno u otro
        j1 = pygame.draw.rect(screen, Datos.BLACK, (Datos.PANT_ANCHO / 10, Datos.PANT_ALTO / 3.5, 100, 20))
        j2 = pygame.draw.rect(screen, Datos.BLACK, (Datos.PANT_ANCHO / 3, Datos.PANT_ALTO / 3.5, 100, 20))
        j3 = pygame.draw.rect(screen, Datos.BLACK, (Datos.PANT_ANCHO / 1.764, Datos.PANT_ALTO / 3.5, 100, 20))
        j4 = pygame.draw.rect(screen, Datos.BLACK, (Datos.PANT_ANCHO / 10, Datos.PANT_ALTO / 1.457, 100, 20))
        j5 = pygame.draw.rect(screen, Datos.BLACK, (Datos.PANT_ANCHO / 3, Datos.PANT_ALTO / 1.457, 100, 20))
        j6 = pygame.draw.rect(screen, Datos.BLACK, (Datos.PANT_ANCHO / 1.764, Datos.PANT_ALTO / 1.457, 100, 20))
        if j1_v== 0:
            t_j1 = draw_text('Jugador', fuente, Datos.PANT_ANCHO / 10, Datos.PANT_ALTO / 3.5, Datos.WHITE)
        elif j1_v== 1:
            t_j1 = draw_text('IA', fuente, Datos.PANT_ANCHO / 10, Datos.PANT_ALTO / 3.5, Datos.WHITE)
        else:
            t_j1 = draw_text('No juega', fuente, Datos.PANT_ANCHO / 10, Datos.PANT_ALTO / 3.5, Datos.WHITE)
        if j2_v== 0:
            t_j2 = draw_text('Jugador', fuente, Datos.PANT_ANCHO / 3, Datos.PANT_ALTO / 3.5, Datos.WHITE)
        elif j2_v== 1:
            t_j2 = draw_text('IA', fuente, Datos.PANT_ANCHO / 3, Datos.PANT_ALTO / 3.5, Datos.WHITE)
        else:
            t_j2 = draw_text('No juega', fuente, Datos.PANT_ANCHO / 3, Datos.PANT_ALTO / 3.5, Datos.WHITE)
        if j3_v== 0:
            t_j3 = draw_text('Jugador', fuente, Datos.PANT_ANCHO / 1.764, Datos.PANT_ALTO / 3.5, Datos.WHITE)
        elif j3_v== 1:
            t_j3 = draw_text('IA', fuente, Datos.PANT_ANCHO / 1.764, Datos.PANT_ALTO / 3.5, Datos.WHITE)
        else:
            t_j3 = draw_text('No juega', fuente, Datos.PANT_ANCHO / 1.764, Datos.PANT_ALTO / 3.5, Datos.WHITE)
        if j4_v== 0:
            t_j4 = draw_text('Jugador', fuente, Datos.PANT_ANCHO / 10, Datos.PANT_ALTO / 1.457, Datos.WHITE)
        elif j4_v== 1:
            t_j4 = draw_text('IA', fuente, Datos.PANT_ANCHO / 10, Datos.PANT_ALTO / 1.457, Datos.WHITE)
        else:
            t_j4 = draw_text('No juega', fuente, Datos.PANT_ANCHO / 10, Datos.PANT_ALTO / 1.457, Datos.WHITE)
        if j5_v== 0:
            t_j5 = draw_text('Jugador', fuente, Datos.PANT_ANCHO / 3, Datos.PANT_ALTO / 1.457, Datos.WHITE)
        elif j5_v== 1:
            t_j5 = draw_text('IA', fuente, Datos.PANT_ANCHO / 3, Datos.PANT_ALTO / 1.457, Datos.WHITE)
        else:
            t_j5 = draw_text('No juega', fuente, Datos.PANT_ANCHO / 3, Datos.PANT_ALTO / 1.457, Datos.WHITE)
        if j6_v== 0:
            t_j6 = draw_text('Jugador', fuente, Datos.PANT_ANCHO / 1.764, Datos.PANT_ALTO / 1.457, Datos.WHITE)
        elif j6_v== 1:
            t_j6 = draw_text('IA', fuente, Datos.PANT_ANCHO / 1.764, Datos.PANT_ALTO / 1.457, Datos.WHITE)
        else:
            t_j6 = draw_text('No juega', fuente, Datos.PANT_ANCHO / 1.764, Datos.PANT_ALTO / 1.457, Datos.WHITE)

        #botones para jugar, volver al menu principal o mostrar controles
        jugar = pygame.draw.rect(screen, Datos.BLACK, (Datos.PANT_ANCHO / 1.2, Datos.PANT_ALTO / 10, 100, 50))
        volver = pygame.draw.rect(screen, Datos.BLACK, (Datos.PANT_ANCHO / 1.2, Datos.PANT_ALTO / 1.53, 100, 50))
        controles = pygame.draw.rect(screen, Datos.BLACK, (Datos.PANT_ANCHO / 1.2, Datos.PANT_ALTO / 2.65, 100, 50))
        draw_text('Jugar', fuente, Datos.PANT_ANCHO / 1.2, Datos.PANT_ALTO / 10, Datos.WHITE)
        draw_text('Volver', fuente, Datos.PANT_ANCHO / 1.2, Datos.PANT_ALTO / 1.53, Datos.WHITE)
        draw_text('Controles', fuente, Datos.PANT_ANCHO / 1.2, Datos.PANT_ALTO / 2.65, Datos.WHITE)

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if j1.collidepoint(event.pos):
                    if j1_v==2:
                        j1_v = 0
                    else:
                        j1_v += 1
                    pygame.display.update()
                if j2.collidepoint(event.pos):
                    if j2_v == 2:
                        j2_v = 0
                    else:
                        j2_v += 1
                    pygame.display.update()
                if j3.collidepoint(event.pos):
                    if j3_v == 2:
                        j3_v = 0
                    else:
                        j3_v += 1
                    pygame.display.update()
                if j4.collidepoint(event.pos):
                    if j4_v == 2:
                        j4_v = 0
                    else:
                        j4_v += 1
                    pygame.display.update()
                if j5.collidepoint(event.pos):
                    if j5_v == 2:
                        j5_v = 0
                    else:
                        j5_v += 1
                    pygame.display.update()
                if j6.collidepoint(event.pos):
                    if j6_v == 2:
                        j6_v = 0
                    else:
                        j6_v += 1
                    pygame.display.update()
                if jugar.collidepoint(event.pos):
                    if j1_v == 2 and j2_v == 2 and j3_v == 2 and j4_v == 2 and j5_v == 2 and j6_v == 2:
                        print("No hay jugadores")
                    else:
                        #se devolverá una lista con los jugadores que jugarán y el color que eligió cada uno
                        Juego.juego(screen, fuente)
                if volver.collidepoint(event.pos):
                    salir = True
                if controles.collidepoint(event.pos):
                    Juego.controles(screen)
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                salir = True
        if salir:
            break


while True:
    if Datos.reiniciar == True:
        Datos.reiniciar = False
        screen.fill(Datos.WHITE)
        texto_espera = fuente.render(f"Cargando...", True, Datos.BLACK)
        screen.blit(texto_espera, (Datos.PANT_ANCHO / 2 - texto_espera.get_width() / 2, Datos.PANT_ALTO / 2 - texto_espera.get_height() / 2))
        pygame.display.flip()
        pygame.time.delay(300)
        Datos.bandera_tanque = True
        Juego.juego(screen, fuente)
    screen.blit(imagenes.FondoMenu, (0, 0))

    play_button = pygame.Rect((Datos.PANT_ANCHO / 2) + 95, (Datos.PANT_ALTO / 2) - 98, 100, 50)
    control_button = pygame.Rect((Datos.PANT_ANCHO / 2) + 75, (Datos.PANT_ALTO / 2) - 5, 100, 50)
    quit_button = pygame.Rect((Datos.PANT_ANCHO / 2) + 100, (Datos.PANT_ALTO / 2) + 90, 100, 50)

    draw_text('Jugar', fuente, (Datos.PANT_ANCHO / 2) + 95, (Datos.PANT_ALTO / 2) - 98, Datos.WHITE)
    draw_text('Opciones', fuente, (Datos.PANT_ANCHO / 2) + 75, (Datos.PANT_ALTO / 2) - 5, Datos.WHITE)
    draw_text('Salir', fuente, (Datos.PANT_ANCHO / 2) + 100, (Datos.PANT_ALTO / 2) + 88, Datos.WHITE)


    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if play_button.collidepoint(event.pos):
                seleccion(screen)
                #Juego.juego(screen, fuente)
            if control_button.collidepoint(event.pos):
                Juego.opciones(screen)
            if quit_button.collidepoint(event.pos):
                pygame.quit()
                sys.exit()

