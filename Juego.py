import pygame, sys, Terreno, Pantalla, Imagenes, random, math, Datos
from Bala import Bala
from Tanque import Tanque
from Terreno import Terreno
from Canon import Canon
from Jugador import Jugador

def draw_button(rect, text, font, text_color, button_color, hover_color, screen):
    pygame.draw.rect(screen, hover_color if rect.collidepoint(pygame.mouse.get_pos()) else button_color, rect)
    text_surface = font.render(text, True, text_color)
    text_rect = text_surface.get_rect(center=rect.center)
    screen.blit(text_surface, text_rect)

def draw_text(text, font, x, y, color, screen):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    screen.blit(textobj, textrect)

class Juego:
    def draw_text(text, font, x, y, color, screen):
        textobj = font.render(text, 1, color)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        screen.blit(textobj, textrect)

    def draw_button(rect, text, font, text_color, button_color, hover_color, screen):
        pygame.draw.rect(screen, hover_color if rect.collidepoint(pygame.mouse.get_pos()) else button_color, rect)
        text_surface = font.render(text, True, text_color)
        text_rect = text_surface.get_rect(center=rect.center)
        screen.blit(text_surface, text_rect)

    def manejar_controles(keys): # Función que maneja los controles del juego
        if keys[pygame.K_w]:
            if Tanque.tanques[Datos.turnos].angulo == 66:
                Tanque.tanques[Datos.turnos].angulo = 0
            else:
                Tanque.tanques[Datos.turnos].angulo += 1   
        elif keys[pygame.K_s]:
            if Tanque.tanques[Datos.turnos].angulo == 0:
                Tanque.tanques[Datos.turnos].angulo = 66
            else:
                Tanque.tanques[Datos.turnos].angulo -= 1
        elif keys[pygame.K_a]:
            Tanque.tanques[Datos.turnos].velocidad -= 5
            Tanque.tanques[Datos.turnos].velocidad = max(0, Tanque.tanques[Datos.turnos].velocidad)
        elif keys[pygame.K_d]:
            Tanque.tanques[Datos.turnos].velocidad += 5
            Tanque.tanques[Datos.turnos].velocidad = min(200, Tanque.tanques[Datos.turnos].velocidad)
        elif keys[pygame.K_1]:
            Tanque.tanques[Datos.turnos].tipo_bala = 1
            Tanque.tanques[Datos.turnos].radioExplosion = 75
        elif keys[pygame.K_2]:
            Tanque.tanques[Datos.turnos].tipo_bala = 2
            Tanque.tanques[Datos.turnos].radioExplosion = 50
        elif keys[pygame.K_3]:
            Tanque.tanques[Datos.turnos].tipo_bala = 3
            Tanque.tanques[Datos.turnos].radioExplosion = 25

    def opciones(screen): # Función que maneja la pestaña de opciones del juego
        while True:
            salir = False
            Pantalla.pantalla.fondoseleccion(screen)

            boton_800 = pygame.Rect((Datos.PANT_ANCHO / 8), (Datos.PANT_ALTO / 3.25), 100, 50)
            boton_default = pygame.Rect((Datos.PANT_ANCHO / 8), (Datos.PANT_ALTO / 2.5), 100, 50)
            boton_768 = pygame.Rect((Datos.PANT_ANCHO / 8), (Datos.PANT_ALTO / 2.025), 100, 50)
            boton_1080 = pygame.Rect((Datos.PANT_ANCHO / 8), (Datos.PANT_ALTO / 1.7), 100, 50)
            boton_gravedad_baja = pygame.Rect((Datos.PANT_ANCHO / 1.4), (Datos.PANT_ALTO / 3.25), 100, 50)
            boton_gravedad_default = pygame.Rect((Datos.PANT_ANCHO / 1.4), (Datos.PANT_ALTO / 2.5), 100, 50)
            boton_gravedad_alta = pygame.Rect((Datos.PANT_ANCHO / 1.4), (Datos.PANT_ALTO / 2), 100, 50)
            boton_viento_habilitado = pygame.Rect((Datos.PANT_ANCHO / 2.3), (Datos.PANT_ALTO / 2.8), 100, 50)
            boton_viento_deshabilitado = pygame.Rect((Datos.PANT_ANCHO / 2.3), (Datos.PANT_ALTO / 2.2), 100, 50)

            draw_button(boton_800, '800x800', pygame.font.Font(None, 36), Datos.WHITE, Datos.BLACK, Datos.GREEN, screen)
            draw_button(boton_default, 'Default', pygame.font.Font(None, 36), Datos.WHITE, Datos.BLACK, Datos.GREEN, screen)
            draw_button(boton_768, '1366x768', pygame.font.Font(None, 36), Datos.WHITE, Datos.BLACK, Datos.GREEN, screen)
            draw_button(boton_1080, '1920x1080', pygame.font.Font(None, 36), Datos.WHITE, Datos.BLACK, Datos.GREEN, screen)
            draw_button(boton_gravedad_baja, 'Baja', pygame.font.Font(None, 36), Datos.WHITE, Datos.BLACK, Datos.GREEN, screen)
            draw_button(boton_gravedad_default, 'Default', pygame.font.Font(None, 36), Datos.WHITE, Datos.BLACK, Datos.GREEN, screen)
            draw_button(boton_gravedad_alta, 'Alta', pygame.font.Font(None, 36), Datos.WHITE, Datos.BLACK, Datos.GREEN, screen)
            draw_button(boton_viento_habilitado, 'Habilitar', pygame.font.Font(None, 36), Datos.WHITE, Datos.BLACK, Datos.GREEN, screen)
            draw_button(boton_viento_deshabilitado, 'Deshabilitar', pygame.font.Font(None, 36), Datos.WHITE, Datos.BLACK, Datos.GREEN, screen)

            fuente = pygame.font.Font(None, 50)
            draw_text('Opciones', fuente, (Datos.PANT_ANCHO / 2.25), (Datos.PANT_ALTO / 7), Datos.WHITE, screen)
            fuente = pygame.font.Font(None, 36)
            draw_text('Resolucion', fuente, (Datos.PANT_ANCHO / 8), (Datos.PANT_ALTO / 5), Datos.WHITE, screen)
            draw_text('Gravedad', fuente, (Datos.PANT_ANCHO / 1.4), (Datos.PANT_ALTO / 5), Datos.WHITE, screen)
            draw_text('Volver: Escape', fuente, (Datos.PANT_ANCHO / 2.3), (Datos.PANT_ALTO / 1.4), Datos.WHITE, screen)
            draw_text('Resolución actual: ' + str(Datos.PANT_ANCHO) + 'x' + str(Datos.PANT_ALTO), fuente, (Datos.PANT_ANCHO / 10), (Datos.PANT_ALTO / 1.5), Datos.WHITE, screen)
            draw_text('Gravedad actual: ' + str(Datos.gravedad), fuente, (Datos.PANT_ANCHO / 1.5), (Datos.PANT_ALTO / 1.5), Datos.WHITE, screen)
            draw_text('Viento', fuente, (Datos.PANT_ANCHO / 2.3), (Datos.PANT_ALTO / 4), Datos.WHITE, screen)
            draw_text('Viento actual: ' + str(Datos.viento_habilitado), fuente, (Datos.PANT_ANCHO / 2.5), (Datos.PANT_ALTO / 1.75), Datos.WHITE, screen)
            

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                keys = pygame.key.get_pressed()
                if keys[pygame.K_ESCAPE]:
                    salir = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if boton_800.collidepoint(event.pos):
                        Datos.PANT_ANCHO = 800
                        Datos.PANT_ALTO = 800
                        screen = pygame.display.set_mode((Datos.PANT_ANCHO, Datos.PANT_ALTO))

                    if boton_default.collidepoint(event.pos):
                        Datos.PANT_ANCHO = 1200
                        Datos.PANT_ALTO = 600
                        screen = pygame.display.set_mode((Datos.PANT_ANCHO, Datos.PANT_ALTO))

                    if boton_768.collidepoint(event.pos):
                        Datos.PANT_ANCHO = 1366
                        Datos.PANT_ALTO = 768
                        screen = pygame.display.set_mode((Datos.PANT_ANCHO, Datos.PANT_ALTO))

                    if boton_1080.collidepoint(event.pos):
                        Datos.PANT_ANCHO = 1920
                        Datos.PANT_ALTO = 1080
                        screen = pygame.display.set_mode((Datos.PANT_ANCHO, Datos.PANT_ALTO), pygame.FULLSCREEN)

                    if boton_gravedad_baja.collidepoint(event.pos):
                        Datos.gravedad = 5
                    if boton_gravedad_default.collidepoint(event.pos):
                        Datos.gravedad = 9.8
                    if boton_gravedad_alta.collidepoint(event.pos):
                        Datos.gravedad = 40
                    
                    #botones de la configuracion del viento
                    if boton_viento_habilitado.collidepoint(event.pos):
                        Datos.viento_habilitado = True
                        
                    if boton_viento_deshabilitado.collidepoint(event.pos):
                        Datos.viento_habilitado = False

            if salir:
                break

    def controles(screen): # Función para la pestaña que muestra los controles del juego
        while True: 
            salir = False   
            Pantalla.pantalla.fondocontroles(screen)
            pygame.display.update()
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT: 
                    pygame.quit() 
                    sys.exit() 
                keys = pygame.key.get_pressed() 
                if keys[pygame.K_ESCAPE]: 
                    salir = True     
            if salir: 
                break         
    
    def verificar_creditos(boton, fuente, screen): # Función que verifica si el jugador tiene los créditos suficientes para comprar una bala
        if boton == 1:
            if Jugador.jugadores[Datos.turnos].creditos < 4000:
                Juego.draw_text('No te alcanzan los creditos', fuente, Datos.PANT_ANCHO / 2, Datos.PANT_ALTO / 2 -100, Datos.BLACK, screen)
                pygame.display.flip()
                pygame.time.delay(1000)
            else:
                Jugador.jugadores[Datos.turnos].cantBala105mm += 1
                Jugador.jugadores[Datos.turnos].creditos -= 4000
        if boton == 2:
            if Jugador.jugadores[Datos.turnos].creditos < 2500:
                Juego.draw_text('No te alcanzan los creditos', fuente, Datos.PANT_ANCHO / 2, Datos.PANT_ALTO / 2 -100, Datos.BLACK, screen)
                pygame.display.flip()
                pygame.time.delay(1000)
            else:
                Jugador.jugadores[Datos.turnos].cantBala80mm += 1
                Jugador.jugadores[Datos.turnos].creditos -= 2500
        if boton == 3:
            if Jugador.jugadores[Datos.turnos].creditos < 1000:
                Juego.draw_text('No te alcanzan los creditos', fuente, Datos.PANT_ANCHO / 2, Datos.PANT_ALTO / 2-100, Datos.BLACK, screen)
                pygame.display.flip()
                pygame.time.delay(1000)
            else:
                Jugador.jugadores[Datos.turnos].cantBala60mm += 1
                Jugador.jugadores[Datos.turnos].creditos -= 1000

    def mostrar_tabla_jugadores(screen, fuente, jugadores_2, finalpartida): # Función que muestra el leaderboard
        tabla_abierta = True
        tab_presionada = False


        if finalpartida:
            for indice, jugadores in enumerate(jugadores_2):
                #por cada kill el jugador recibe 5000 creditos y por cada suicido pierde 5000 creditos
                Jugador.jugadores[indice].creditos += Jugador.jugadores[indice].kills * 5000
                Jugador.jugadores[indice].creditos -= Jugador.jugadores[indice].suicidios * 5000
                Jugador.jugadores[indice].ktotales += Jugador.jugadores[indice].kills
                Jugador.jugadores[indice].mtotales += Jugador.jugadores[indice].muertes
                Jugador.jugadores[indice].stotales += Jugador.jugadores[indice].suicidios
            while tabla_abierta:
                Pantalla.pantalla.fondoblanco(screen)

                # Título de la tabla
                Juego.draw_text('Tabla de Jugadores', fuente, Datos.PANT_ANCHO / 2 - 200, 20, Datos.BLACK, screen)

                # Encabezados de las columnas
                Juego.draw_text('Jugador', fuente, 250, 80, Datos.BLACK, screen)
                Juego.draw_text('Kills', fuente, 400, 80, Datos.BLACK, screen)
                Juego.draw_text('Muertes', fuente, 550, 80, Datos.BLACK, screen)
                Juego.draw_text('Suicidios', fuente, 700, 80, Datos.BLACK, screen)

                salir_button = pygame.Rect(40, Datos.PANT_ALTO - 60, 120, 30)
                Juego.draw_button(salir_button, 'Cerrar', fuente, Datos.BLACK, Datos.WHITE, Datos.GREEN, screen)

                # Mostrar información de cada jugador en la tabla
                for i, jugador in enumerate(jugadores_2):
                    Juego.draw_text(f'Jugador {jugador.indice + 1}', fuente, 250, 170 + i * 60, Datos.BLACK, screen)
                    Juego.draw_text(str(jugador.ktotales), fuente, 400, 170 + i * 60, Datos.BLACK, screen)
                    Juego.draw_text(str(jugador.mtotales), fuente, 550, 170 + i * 60, Datos.BLACK, screen)
                    Juego.draw_text(str(jugador.stotales), fuente, 700, 170 + i * 60, Datos.BLACK, screen)

                    # Muestra la imagen del tanque asociado al jugador
                    for i, jugador in enumerate(jugadores_2):
                        if i < len(jugadores_2):
                            #screen.blit(imagenes.Tanque_HUDs[aux[i].color], (50, 150 + i * 60))
                            screen.blit(Imagenes.Tanque_HUDs[jugadores_2[i].color_tanque], (50, 150 + i * 60))
                
        
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        tabla_abierta = False

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if salir_button.collidepoint(event.pos):
                            tabla_abierta = False

                    if event.type == pygame.KEYDOWN and event.key == pygame.K_TAB:
                        tabla_abierta = False
                        tab_presionada = True

                pygame.display.flip()
        else:
            while tabla_abierta:
                Pantalla.pantalla.fondoblanco(screen)

                # Título de la tabla
                Juego.draw_text('Tabla de Jugadores', fuente, Datos.PANT_ANCHO / 2 - 200, 20, Datos.BLACK, screen)

                # Encabezados de las columnas
                Juego.draw_text('Jugador', fuente, 250, 80, Datos.BLACK, screen)
                Juego.draw_text('Kills', fuente, 400, 80, Datos.BLACK, screen)
                Juego.draw_text('Muertes', fuente, 550, 80, Datos.BLACK, screen)
                Juego.draw_text('Suicidios', fuente, 700, 80, Datos.BLACK, screen)

                salir_button = pygame.Rect(40, Datos.PANT_ALTO - 60, 120, 30)
                Juego.draw_button(salir_button, 'Cerrar', fuente, Datos.BLACK, Datos.WHITE, Datos.GREEN, screen)

                # Mostrar información de cada jugador en la tabla
                for i, jugador in enumerate(jugadores_2):
                    Juego.draw_text(f'Jugador {jugador.indice + 1}', fuente, 250, 170 + i * 60, Datos.BLACK, screen)
                    Juego.draw_text(str(jugador.kills), fuente, 400, 170 + i * 60, Datos.BLACK, screen)
                    Juego.draw_text(str(jugador.muertes), fuente, 550, 170 + i * 60, Datos.BLACK, screen)
                    Juego.draw_text(str(jugador.suicidios), fuente, 700, 170 + i * 60, Datos.BLACK, screen)

                    # Muestra la imagen del tanque asociado al jugador
                    for i, jugador in enumerate(jugadores_2):
                        if i < len(jugadores_2):
                            #screen.blit(imagenes.Tanque_HUDs[aux[i].color], (50, 150 + i * 60))
                            screen.blit(Imagenes.Tanque_HUDs[jugadores_2[i].color_tanque], (50, 150 + i * 60))
                
        
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        tabla_abierta = False

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if salir_button.collidepoint(event.pos):
                            tabla_abierta = False

                    if event.type == pygame.KEYDOWN and event.key == pygame.K_TAB:
                        tabla_abierta = False
                        tab_presionada = True

                pygame.display.flip()

    def shop(screen): # Función que maneja la pestaña de la tienda del juego
        tienda_abierta = True
        #guardamos la cantidad de balas y el dinero del tanque en variables auxiliares
        cantBala105mm = Jugador.jugadores[Datos.turnos].cantBala105mm
        cantBala80mm = Jugador.jugadores[Datos.turnos].cantBala80mm
        cantBala60mm = Jugador.jugadores[Datos.turnos].cantBala60mm
        creditos = Jugador.jugadores[Datos.turnos].creditos
        while tienda_abierta:
            Pantalla.pantalla.fondoblanco(screen)
            fuente = pygame.font.Font(None, 36)
            # Botón de devolver compras
            devolver_button = pygame.Rect(200, Datos.PANT_ALTO - 60, 120, 30)
            Juego.draw_button(devolver_button, 'Devolver', fuente, Datos.BLACK, Datos.WHITE, Datos.GREEN, screen)

            # Botón de Tienda (título)
            Juego.draw_text('Tienda', fuente, Datos.PANT_ANCHO / 2 - 200, Datos.PANT_ALTO / 2 - 150, Datos.BLACK, screen)

            # Subtítulo y botones para tipos de bala
            Juego.draw_text('Tipos de Bala', fuente, Datos.PANT_ANCHO / 2 - 200, Datos.PANT_ALTO / 2 - 50, Datos.BLACK, screen)

            # Mostrar creditos
            Juego.draw_text(f"creditos: {Jugador.jugadores[Datos.turnos].creditos}", fuente, Datos.PANT_ANCHO / 2 - 200, Datos.PANT_ALTO / 2 - 100, Datos.BLACK, screen)

            bala1_button = pygame.Rect(Datos.PANT_ANCHO / 2 - 250, Datos.PANT_ALTO / 2, 100, 50)
            Juego.draw_button(bala1_button, 'Bala 1', fuente, Datos.BLACK, Datos.WHITE, Datos.GREEN, screen)

            bala2_button = pygame.Rect(Datos.PANT_ANCHO / 2 - 250, Datos.PANT_ALTO / 2 + 60, 100, 50)
            Juego.draw_button(bala2_button, 'Bala 2', fuente, Datos.BLACK, Datos.WHITE, Datos.GREEN, screen)

            bala3_button = pygame.Rect(Datos.PANT_ANCHO / 2 - 250, Datos.PANT_ALTO / 2 + 120, 100, 50)
            Juego.draw_button(bala3_button, 'Bala 3', fuente, Datos.BLACK, Datos.WHITE, Datos.GREEN, screen)

            # Botón de Salir como una pestaña
            salir_button = pygame.Rect(40, Datos.PANT_ALTO - 60, 120, 30)
            Juego.draw_button(salir_button,'Siguiente', fuente, Datos.BLACK, Datos.WHITE, Datos.GREEN, screen)

            #mostrar el color del tanque
            screen.blit(Imagenes.Tanque_HUDs[Jugador.jugadores[Datos.turnos].color_tanque], (Datos.PANT_ANCHO / 2 - 50, Datos.PANT_ALTO / 2 + 50))

            #mostrar la cantidad de balas de 105mm, 80mm y 60mm con sus respectivas imagenes
            screen.blit(Imagenes.Bala105, (Datos.PANT_ANCHO / 2 + 100, Datos.PANT_ALTO / 2))
            Juego.draw_text(f"x{Jugador.jugadores[Datos.turnos].cantBala105mm}", fuente, Datos.PANT_ANCHO / 2 + 125, Datos.PANT_ALTO / 2 + 10, Datos.BLACK, screen)
            screen.blit(Imagenes.Bala80, (Datos.PANT_ANCHO / 2 + 100, Datos.PANT_ALTO / 2 + 60))
            Juego.draw_text(f"x{Jugador.jugadores[Datos.turnos].cantBala80mm}", fuente, Datos.PANT_ANCHO / 2 + 125, Datos.PANT_ALTO / 2 + 70, Datos.BLACK, screen)
            screen.blit(Imagenes.Bala60, (Datos.PANT_ANCHO / 2 + 100, Datos.PANT_ALTO / 2 + 120))
            Juego.draw_text(f"x{Jugador.jugadores[Datos.turnos].cantBala60mm}", fuente, Datos.PANT_ANCHO / 2 + 125, Datos.PANT_ALTO / 2 + 130, Datos.BLACK, screen)
            pygame.display.update()

            if Jugador.jugadores[Datos.turnos].IA == False:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        tienda_abierta = False

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if salir_button.collidepoint(event.pos):
                            tienda_abierta = False

                        elif bala1_button.collidepoint(event.pos):
                            Juego.verificar_creditos(1, fuente,screen)

                        elif bala2_button.collidepoint(event.pos):
                            Juego.verificar_creditos(2, fuente,screen)

                        elif bala3_button.collidepoint(event.pos):
                            Juego.verificar_creditos(3, fuente,screen)
                        
                        elif devolver_button.collidepoint(event.pos):
                            Jugador.jugadores[Datos.turnos].cantBala105mm = cantBala105mm
                            Jugador.jugadores[Datos.turnos].cantBala80mm = cantBala80mm
                            Jugador.jugadores[Datos.turnos].cantBala60mm = cantBala60mm
                            Jugador.jugadores[Datos.turnos].creditos = creditos
                            
            elif Jugador.jugadores[Datos.turnos].IA == True:
                if Jugador.jugadores[Datos.turnos].creditos >= 4000:
                    Jugador.jugadores[Datos.turnos].cantBala105mm += 1
                    Jugador.jugadores[Datos.turnos].creditos -= 4000
                    pygame.time.delay(1000)
                elif Jugador.jugadores[Datos.turnos].creditos >= 2500:
                    Jugador.jugadores[Datos.turnos].cantBala80mm += 1
                    Jugador.jugadores[Datos.turnos].creditos -= 2500
                    pygame.time.delay(1000)
                elif Jugador.jugadores[Datos.turnos].creditos >= 1000:
                    Jugador.jugadores[Datos.turnos].cantBala60mm += 1
                    Jugador.jugadores[Datos.turnos].creditos -= 1000
                    pygame.time.delay(1000)
                else:
                    pygame.time.delay(1000)
                    tienda_abierta = False

    def muestra_ganador(Ganador, screen, fuente, color): #Función para mostrar el ganador del juego
        
        Pantalla.pantalla.fondoblanco(screen)
        for indice, jugador in enumerate(Jugador.jugadores):
            if color == Jugador.jugadores[indice].color_tanque:
                Jugador.jugadores[indice].partidas_ganadas += 1
                winner = Jugador.jugadores[indice].color_tanque
        
        texto_ganador = fuente.render(f"Ganador ronda: Jugador {winner}", True, Datos.BLACK) 
        screen.blit(texto_ganador, (Datos.PANT_ANCHO / 2 - texto_ganador.get_width() / 2, Datos.PANT_ALTO / 2 - texto_ganador.get_height() / 2))
        screen.blit(Imagenes.Tanque_HUDs[color], (Datos.PANT_ANCHO / 2 - 50, Datos.PANT_ALTO / 2 + 50))

        Datos.partida_actual += 1
        pygame.display.flip() 
        pygame.time.delay(3000)
        if Datos.partida_actual > Datos.num_partidas:
            Juego.muestra_ganador_final(screen, fuente)

    def muestra_ganador_final(screen, fuente): #Función para mostrar el ganador final del juego
        Pantalla.pantalla.fondoblanco(screen)
        jugador_ganador = None
        jugador_auxiliar = None
        empate = 0
        #verificamos cual jugador tiene la cantidad de victorias más alta, si es un empate, se muestra un mensaje de empate entre los jugadores empatados
        for indice, jugador in enumerate(Jugador.jugadores):
            jugador_auxiliar = Jugador.jugadores[indice]
            if indice == 0:
                jugador_ganador = jugador_auxiliar
            elif jugador_auxiliar.ktotales > jugador_ganador.ktotales:
                jugador_ganador = jugador_auxiliar
                empate = 0
            elif jugador_auxiliar.ktotales == jugador_ganador.ktotales:
                empate = 1
        if empate == 1:
            texto_ganador = fuente.render("Empate entre 2 o más jugadores", True, Datos.BLACK)
            screen.blit(texto_ganador, (Datos.PANT_ANCHO / 2 - texto_ganador.get_width() / 2, Datos.PANT_ALTO / 2 - texto_ganador.get_height() / 2))
        else:
            texto_ganador = fuente.render(f"Ganador: Jugador {jugador_ganador.color_tanque}", True, Datos.BLACK)
            screen.blit(texto_ganador, (Datos.PANT_ANCHO / 2 - texto_ganador.get_width() / 2, Datos.PANT_ALTO / 2 - texto_ganador.get_height() / 2))
            screen.blit(Imagenes.Tanque_HUDs[jugador_ganador.color_tanque], (Datos.PANT_ANCHO / 2 - 50, Datos.PANT_ALTO / 2 + 50))
        pygame.display.flip()
        pygame.time.delay(3000)
        sys.exit()
        
    def sin_balas(screen, fuente): #Función para mostrar el mensaje de que todos los jugadores se quedaron sin balas
        Pantalla.pantalla.fondoblanco(screen)
        texto_ganador = fuente.render("Todos se quedaron sin balas", True, Datos.BLACK)
        screen.blit(texto_ganador, (Datos.PANT_ANCHO / 2 - texto_ganador.get_width() / 2, Datos.PANT_ALTO / 2 - texto_ganador.get_height() / 2))
        pygame.display.flip()
        pygame.time.delay(3000)
        Datos.partida_actual += 1
        for indice, tanque in enumerate(Tanque.tanques):
            Tanque.tanques[indice].sin_balas = False
        if Datos.partida_actual > Datos.num_partidas:
            Juego.muestra_ganador_final(screen, fuente)

    def seleccion(screen, fuente): #Función de selección de jugadores
        clock = pygame.time.Clock()

        key_repeat_delay = 200  # Milisegundos
        key_repeat_interval = 50  # Milisegundos

        key_repeat_timer = 0
        while True:
            Jugador.jugadores.clear()
            salir = False


            Pantalla.pantalla.fondoseleccion(screen)
            Pantalla.pantalla.muestra_seleccion(screen, fuente) 

            j1 = pygame.draw.rect(screen, Datos.PURPLE, (Datos.PANT_ANCHO / 10, Datos.PANT_ALTO / 3.5, 100, 20))
            j2 = pygame.draw.rect(screen, Datos.PURPLE, (Datos.PANT_ANCHO / 3, Datos.PANT_ALTO / 3.5, 100, 20))
            j3 = pygame.draw.rect(screen, Datos.PURPLE, (Datos.PANT_ANCHO / 1.764, Datos.PANT_ALTO / 3.5, 100, 20))
            j4 = pygame.draw.rect(screen, Datos.PURPLE, (Datos.PANT_ANCHO / 10, Datos.PANT_ALTO / 1.457, 100, 20))
            j5 = pygame.draw.rect(screen, Datos.PURPLE, (Datos.PANT_ANCHO / 3, Datos.PANT_ALTO / 1.457, 100, 20))
            j6 = pygame.draw.rect(screen, Datos.PURPLE, (Datos.PANT_ANCHO / 1.764, Datos.PANT_ALTO / 1.457, 100, 20))

            num_partidas_texto = fuente.render(f"Numero de partidas: {Datos.num_partidas}", True, Datos.WHITE)
            aviso_texto = fuente.render(f"Usa las flechas para ajustar las partidas", True, Datos.WHITE)

            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                if pygame.time.get_ticks() - key_repeat_timer > key_repeat_delay:
                    key_repeat_timer = pygame.time.get_ticks()
                    if Datos.num_partidas == 20:
                        Datos.num_partidas = 1
                    else:
                        Datos.num_partidas += 1
            elif keys[pygame.K_DOWN]:
                if pygame.time.get_ticks() - key_repeat_timer > key_repeat_delay:
                    key_repeat_timer = pygame.time.get_ticks()
                    if Datos.num_partidas == 1:
                        Datos.num_partidas = 20
                    else:
                        Datos.num_partidas -= 1

            screen.blit(num_partidas_texto, (Datos.PANT_ANCHO / 1.5, Datos.PANT_ALTO / 1.2))
            screen.blit(aviso_texto, (Datos.PANT_ANCHO / 1.8, Datos.PANT_ALTO / 1.3))

            for indice,jugador in enumerate(Jugador.seleccionJugadores):
                if jugador == 0:
                        text = 'Jugador'
                elif jugador == 1:
                    text = 'IA'
                else:
                    text = 'No juega'

                if indice < 3:
                    Juego.draw_text(text, fuente, Datos.PANT_ANCHO / Datos.lista_cuadrar_jugadores_texto_x[indice], Datos.PANT_ALTO / Datos.lista_cuadrar_jugadores_texto_y[0], Datos.WHITE, screen)
                else:
                    Juego.draw_text(text, fuente, Datos.PANT_ANCHO / Datos.lista_cuadrar_jugadores_texto_x[indice-3], Datos.PANT_ALTO / Datos.lista_cuadrar_jugadores_texto_y[1], Datos.WHITE, screen)

            jugar = pygame.Rect(Datos.PANT_ANCHO / 1.2, Datos.PANT_ALTO / 10, 100, 50)
            volver = pygame.Rect(Datos.PANT_ANCHO / 1.2, Datos.PANT_ALTO / 1.53, 100, 50)
            controles = pygame.Rect(Datos.PANT_ANCHO / 1.2, Datos.PANT_ALTO / 2.65, 100, 50)
            Juego.draw_button(jugar, 'Jugar', fuente, Datos.WHITE, Datos.BLACK, Datos.GREEN, screen)
            Juego.draw_button(volver, 'Volver', fuente, Datos.WHITE, Datos.BLACK, Datos.GREEN, screen)
            Juego.draw_button(controles, 'Controles', fuente, Datos.WHITE, Datos.BLACK, Datos.GREEN, screen)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:  
                    if j1.collidepoint(event.pos):
                        if Jugador.seleccionJugadores[0]==2:
                            Jugador.seleccionJugadores[0] = 0
                        else:
                            Jugador.seleccionJugadores[0] += 1
                        pygame.display.update()
                    if j2.collidepoint(event.pos):
                            if Jugador.seleccionJugadores[1] == 2:
                                Jugador.seleccionJugadores[1] = 0
                            else:
                                Jugador.seleccionJugadores[1] += 1
                            pygame.display.update()
                    if j3.collidepoint(event.pos):
                            if Jugador.seleccionJugadores[2] == 2:
                                Jugador.seleccionJugadores[2] = 0
                            else:
                                Jugador.seleccionJugadores[2] += 1
                            pygame.display.update()
                    if j4.collidepoint(event.pos):
                            if Jugador.seleccionJugadores[3] == 2:
                                Jugador.seleccionJugadores[3] = 0
                            else:
                                Jugador.seleccionJugadores[3] += 1
                            pygame.display.update()
                    if j5.collidepoint(event.pos):
                            if Jugador.seleccionJugadores[4] == 2:
                                Jugador.seleccionJugadores[4] = 0
                            else:
                                Jugador.seleccionJugadores[4] += 1
                            pygame.display.update()
                    if j6.collidepoint(event.pos):
                            if Jugador.seleccionJugadores[5] == 2:
                                Jugador.seleccionJugadores[5] = 0
                            else:
                                Jugador.seleccionJugadores[5] += 1
                            pygame.display.update()  
                    if jugar.collidepoint(event.pos):
                        for indice,jugador in enumerate(Jugador.seleccionJugadores):
                            if jugador == 0:
                                Jugador.crearJugador(indice, False)
                            if jugador == 1:
                                Jugador.crearJugador(indice, True)
                        return True
                    if volver.collidepoint(event.pos):
                        return False
                    if controles.collidepoint(event.pos):
                        Juego.controles(screen)    
                keys = pygame.key.get_pressed()
                if keys[pygame.K_ESCAPE]:
                    salir = True       

    def mostrar_tooltip(tanque, screen, x, y): # Función tooltip (muestra la vida de cada tanque con el mouse)
        if x + 100 > Datos.PANT_ANCHO:
            x -= 100
        pygame.draw.rect(screen, Datos.WHITE, (x, y, 100, 75))
        screen.blit(Imagenes.Tanque_Tooltip[tanque.color], (x + 20, y + 10))
        fuente = pygame.font.Font(None, 30)
        Juego.draw_text(f"Vida: {tanque.vida}", fuente, x + 10, y + 50, Datos.BLACK, screen)
        pygame.display.update()

    def cambiar_sin_balas():
        for indice, tanque in enumerate(Tanque.tanques):
            if Tanque.tanques[indice].sin_balas == False and Datos.bala_tanque is None:
                    if Tanque.tanques[indice].cantBala105mm == 0 and Tanque.tanques[indice].cantBala80mm == 0 and Tanque.tanques[indice].cantBala60mm == 0:
                        Tanque.tanques[indice].sin_balas = True
    
    def comprobar_sin_balas():
        if Tanque.tanques[Datos.turnos].sin_balas == True and Datos.bala_tanque is None:
                Datos.comprobar_viento = False
                if Datos.turnos < len(Tanque.tanques)-1:
                    Datos.turnos += 1
                else:
                    Datos.turnos = 0
                    Datos.rondas += 1
                Datos.anima_quedan_balas = True
                Datos.tecla_espacio_presionada = False
                Datos.tiempo_transcurrido = 0

    def juego(screen, fuente): # Función que maneja el juego en sí
        #Compra de cada partida
        for indice, jugador in enumerate(Jugador.jugadores):
            Juego.shop(screen)
            Datos.turnos += 1
        Datos.turnos = 0
        primera_iteracion = True
        #Creacion clases (Terreno y tanques)
        salirJuego = False
        terreno = Terreno(Datos.PANT_ANCHO, Datos.PANT_ALTO)
        Tanque.tanques.clear()
        Tanque.creaTanques(Jugador.jugadores)
        Tanque.spawnTanques(terreno)
        
        #una vez creado los tanques ahora se crean los cañones
        for indice, tanque in enumerate(Tanque.tanques):
            Canon(Tanque.tanques[indice])

        #Inicio de variables 
        Datos.reiniciar_datos()

        Clock = pygame.time.Clock()
        #ajuste de pivotes de los tanques
        for indice, tanque in enumerate(Tanque.tanques):
            Tanque.tanques[indice].pivote = [Tanque.tanques[indice].x+21, Tanque.tanques[indice].y-5]

        #ubicacion de los extremos de los cañones
        for indice, tanque in enumerate(Tanque.tanques):
            Tanque.tanques[indice].extremo_canonx, Tanque.tanques[indice].extremo_canony = Pantalla.pantalla.prerotate(screen, Tanque.tanques[indice].color, Datos.ang_tank[0], Tanque.tanques[indice].pivote)

        incremento = 0.035

        salir = screen.blit(Imagenes.Exit, (Datos.PANT_ANCHO / 2.5, 10)) 
        reset = screen.blit(Imagenes.Restart, (Datos.PANT_ANCHO / 2, 10)) 
        #antes de comenzar el juego se baraja el orden de los jugadores haciendo shuffle al arraylist de tanques
        
        listas_combinadas = list(zip(Tanque.tanques, Jugador.jugadores))

        # Desordena la lista combinada
        random.shuffle(listas_combinadas)

        # Descomprime las listas nuevamente
        Tanque.tanques, Jugador.jugadores = map(list, zip(*listas_combinadas))
        
        #random.shuffle(Tanque.tanques)
        Tanque.tanques[Datos.turnos].mostrar_datos = True
        #Para mostrar correctamente los datos de la primera iteración se crea un nuevo booleando
        

        
        tab_presionada = False
        mostrando_tabla = False

        while True:
            if primera_iteracion is False:
                Juego.cambiar_sin_balas()
                Juego.comprobar_sin_balas()
            for indice, tanque in enumerate(Tanque.tanques):
                if Tanque.tanques[indice].sin_balas == True:
                    Datos.tanque_sin_balas += 1
                elif Tanque.tanques[indice].sin_balas == False:
                    Datos.tanque_sin_balas -= 1
                if Datos.tanque_sin_balas == len(Tanque.tanques):
                    Juego.sin_balas(screen, fuente)
                    salirJuego = True
                    Datos.reiniciar = True  
            Datos.tanque_sin_balas = 0    

            Clock.tick(Datos.FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if reset.collidepoint(pygame.mouse.get_pos()):
                        salirJuego = True
                        Datos.reiniciar = True  # Reiniciar el juego
                        for indice, jugador in enumerate(Jugador.jugadores):
                            Jugador.jugadores[indice].partidas_ganadas = 0
                            Jugador.jugadores[indice].kills = 0
                            Jugador.jugadores[indice].muertes = 0
                            Jugador.jugadores[indice].suicidios = 0
                            Jugador.jugadores[indice].cantBala60mm = 0
                            Jugador.jugadores[indice].cantBala80mm = 0
                            Jugador.jugadores[indice].cantBala105mm = 0
                            Jugador.jugadores[indice].creditos = 10000
                    if salir.collidepoint(pygame.mouse.get_pos()):
                        salirJuego = True  # Volver al menú principal
                        
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_TAB:
                        Juego.mostrar_tabla_jugadores(screen, fuente, Jugador.jugadores, False)
                        tab_presionada = True

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_TAB:
                        tab_presionada = False

            keys = pygame.key.get_pressed()

            if Tanque.tanques[Datos.turnos].esIA == False:
                if keys[pygame.K_ESCAPE]:
                    salirJuego = True

                if keys[pygame.K_SPACE]:
                    Datos.tecla_espacio_presionada = True

                #Controles para el jugador Tanque.tanques[Datos.turnos]
                Juego.manejar_controles(keys)
            elif Tanque.tanques[Datos.turnos].esIA == True and Datos.bala_tanque is None:
                Tanque.tanques[Datos.turnos].angulo, Tanque.tanques[Datos.turnos].velocidad, Tanque.tanques[Datos.turnos].tipo_bala = Tanque.ia(Tanque.tanques[Datos.turnos])
                Datos.tecla_espacio_presionada = True
                pygame.time.delay(4000)

            #Dibuja el terreno y aplica imagenes de fondo y hud
            Pantalla.pantalla.background(screen)
            terreno.dibujar(screen)
            Pantalla.pantalla.hud(screen)

            #DIBUJAR HITBOXES
            for indice, tanque in enumerate(Tanque.tanques):
                Tanque.tanques[indice].dibujar(screen)

            #PASAR DATOS DE KILLS, MUERTES Y SUICIDIOS DE TANQUE A JUGADOR CON EL COLOR DEL TANQUE
            for indice, tanque in enumerate(Tanque.tanques):
                for indice2, jugador in enumerate(Jugador.jugadores):
                    if Tanque.tanques[indice].color == Jugador.jugadores[indice2].color_tanque:
                        Jugador.jugadores[indice2].kills = Tanque.tanques[indice].kills
                        Jugador.jugadores[indice2].muertes = Tanque.tanques[indice].muertes
                        Jugador.jugadores[indice2].suicidios = Tanque.tanques[indice].suicidios


            #VERIFICA LA VIDA 
            colorTanque = Tanque.tanques[Datos.turnos].color
            for indice, tanque in enumerate(Tanque.tanques):
                #KILL Y SUICIDIO
                if Tanque.tanques[indice].vida <= 0:
                    Tanque.tanques[indice].muertes += 1                    
                    for indice2, jugador in enumerate(Jugador.jugadores):
                        if Tanque.tanques[indice].color == Jugador.jugadores[indice2].color_tanque:
                            Jugador.jugadores[indice2].muertes += Tanque.tanques[indice].muertes
                            Jugador.jugadores[indice2].cantBala105mm = Tanque.tanques[indice].cantBala105mm
                            Jugador.jugadores[indice2].cantBala80mm = Tanque.tanques[indice].cantBala80mm
                            Jugador.jugadores[indice2].cantBala60mm = Tanque.tanques[indice].cantBala60mm
                    if Tanque.tanques[indice].color == colorTanque:
                        if Datos.turnos+1 >= len(Tanque.tanques):
                            colorTanque = Tanque.tanques[0].color
                        else:
                            colorTanque = Tanque.tanques[Datos.turnos+1].color
                    del Tanque.tanques[indice]
                        
                if len(Tanque.tanques) == 1:
                    for indice2, jugador in enumerate(Jugador.jugadores):
                        if Tanque.tanques[0].color == Jugador.jugadores[indice2].color_tanque:
                            Jugador.jugadores[indice2].cantBala105mm = Tanque.tanques[0].cantBala105mm
                            Jugador.jugadores[indice2].cantBala80mm = Tanque.tanques[0].cantBala80mm
                            Jugador.jugadores[indice2].cantBala60mm = Tanque.tanques[0].cantBala60mm
                    
                    Juego.mostrar_tabla_jugadores(screen, fuente, Jugador.jugadores, True)
                    Juego.muestra_ganador(Tanque.tanques[0].num, screen, fuente, Tanque.tanques[0].color)
                    salirJuego = True
                    Datos.reiniciar = True
                    
            while True:
                if Datos.turnos >= len(Tanque.tanques):
                    Datos.turnos = 0
                if Tanque.tanques[Datos.turnos].color == colorTanque:
                    break
                Datos.turnos += 1
            if Datos.tecla_espacio_presionada:
                if Datos.bala_tanque is None:
                    Datos.mostrar_altura = Tanque.tanques[Datos.turnos].indice
                    if Tanque.tanques[Datos.turnos].tipo_bala == 1 and Tanque.tanques[Datos.turnos].cantBala105mm == 0:
                        Datos.anima_quedan_balas = True
                        Datos.tecla_espacio_presionada = False
                        Datos.tiempo_transcurrido = 0
                    elif Tanque.tanques[Datos.turnos].tipo_bala == 2 and Tanque.tanques[Datos.turnos].cantBala80mm == 0:
                        Datos.anima_quedan_balas = True
                        Datos.tecla_espacio_presionada = False
                        Datos.tiempo_transcurrido = 0
                    elif Tanque.tanques[Datos.turnos].tipo_bala == 3 and Tanque.tanques[Datos.turnos].cantBala60mm == 0:
                        Datos.anima_quedan_balas = True
                        Datos.tecla_espacio_presionada = False
                        Datos.tiempo_transcurrido = 0
                    else:
                        #si pasa las comprobaciones se dispara la bala
                        if primera_iteracion:
                            primera_iteracion=False
                        else:
                            if Datos.turnos==0:
                                Tanque.tanques[len(Tanque.tanques)-1].mostrar_datos = False
                                Tanque.tanques[Datos.turnos].mostrar_datos = True
                            else:
                                Tanque.tanques[Datos.turnos-1].mostrar_datos = False
                                Tanque.tanques[Datos.turnos].mostrar_datos = True
                        Datos.bala_tanque = Tanque.tanques[Datos.turnos].disparar( 
                            Tanque.tanques[Datos.turnos].extremo_canonx, 
                            Tanque.tanques[Datos.turnos].extremo_canony, 
                            Datos.ang_tank[Tanque.tanques[Datos.turnos].angulo], 
                            Tanque.tanques[Datos.turnos].velocidad, 
                            Datos.tiempo_transcurrido, 
                            screen, 
                            Datos.BLACK, 
                            Tanque.tanques[Datos.turnos].tipo_bala 
                        )   
                        
                else:
                    Datos.altura_maxima = Datos.bala_tanque.punto_maximo(Datos.altura_maxima)
                    Datos.bala_tanque.verificacion(Datos.tiempo_transcurrido, screen, Datos.BLACK)
                    Datos.distancia_maxima = Datos.bala_tanque.distancia_maxima(Tanque.tanques[Datos.turnos].x, Datos.distancia_maxima)
                    for indice, tanque in enumerate(Tanque.tanques):
                        if Datos.bala_tanque.verificar_impacto_ancho(Datos.PANT_ANCHO):
                            Datos.bala_tanque = None
                            Datos.tecla_espacio_presionada = False
                            Datos.tiempo_transcurrido = 0
                            Datos.comprobar_viento = False
                            if Datos.turnos < len(Tanque.tanques)-1:
                                Datos.turnos += 1
                            else:
                                Datos.turnos = 0
                                Datos.rondas += 1
                                
                            break
                        elif terreno.verificar_colision(Datos.bala_tanque):
                            Datos.tecla_espacio_presionada = False
                            Datos.tiempo_transcurrido = 0
                            terreno.modificar_terreno(terreno, Tanque.tanques[Datos.turnos])
                            puntosExplosionX, puntosExplosionY = terreno.obtener_puntos_circulo(Tanque.tanques[Datos.turnos].radioExplosion, terreno.calcular_centro_explosion() )
                            #dibujamos los puntosExplosionx y puntosExplosionY para ver si estan bien
                            for i in range(len(puntosExplosionX)):
                                pygame.draw.circle(screen, Datos.BLACK, (puntosExplosionX[i], puntosExplosionY[i]), 2)
                            pygame.display.flip()
                            for indice, tanque in enumerate(Tanque.tanques):
                                if Datos.bala_tanque.verificar_impacto_tanque_explosion(Tanque.tanques[indice], puntosExplosionX, puntosExplosionY):
                                    if Tanque.tanques[Datos.turnos].tipo_bala == 1:
                                        Tanque.tanques[indice].vida -= Tanque.tanques[Datos.turnos].Bala105mm
                                    elif Tanque.tanques[Datos.turnos].tipo_bala == 2:
                                        Tanque.tanques[indice].vida -= Tanque.tanques[Datos.turnos].Bala80mm
                                    elif Tanque.tanques[Datos.turnos].tipo_bala == 3:
                                        Tanque.tanques[indice].vida -= Tanque.tanques[Datos.turnos].Bala60mm
                                    Tanque.acomodarTanque(screen, terreno, primera_iteracion) 
                                    #KILL Y SUICIDIO
                                    if Tanque.tanques[indice].vida <= 0:
                                        print("vida del tanque " + Datos.color_tanque[Tanque.tanques[indice].color] + " llegó a 0 por daño de explosion al terreno")
                                        if Datos.turnos == indice:
                                            Tanque.tanques[Datos.turnos].suicidios += 1
                                            print("suicidio del tanque " + Datos.color_tanque[Tanque.tanques[Datos.turnos].color])
                                        else:
                                            Tanque.tanques[Datos.turnos].kills += 1
                                            print("Tanque " + Datos.color_tanque[Tanque.tanques[Datos.turnos].color] + " mató a tanque " + Datos.color_tanque[Tanque.tanques[indice].color])
                                            
                            Datos.bala_tanque = None
                            Datos.comprobar_viento = False
                            if Datos.turnos < len(Tanque.tanques)-1:
                                Datos.turnos += 1
                            else:
                                Datos.turnos = 0
                                Datos.rondas += 1
                            break
                        elif Datos.bala_tanque.verificar_impacto_tanque(Tanque.tanques[indice]):
                            if Tanque.tanques[Datos.turnos].tipo_bala == 1:
                                Tanque.tanques[indice].vida -= Tanque.tanques[Datos.turnos].Bala105mm
                                Datos.impacto_tanque = Tanque.tanques[indice].color
                            elif Tanque.tanques[Datos.turnos].tipo_bala == 2:
                                Tanque.tanques[indice].vida -= Tanque.tanques[Datos.turnos].Bala80mm
                                Datos.impacto_tanque = Tanque.tanques[indice].color
                            elif Tanque.tanques[Datos.turnos].tipo_bala == 3:
                                Tanque.tanques[indice].vida -= Tanque.tanques[Datos.turnos].Bala60mm
                                Datos.impacto_tanque = Tanque.tanques[indice].color
                                

                                
                            Datos.tecla_espacio_presionada = False
                            Datos.tiempo_transcurrido = 0
                            terreno.modificar_terreno(terreno, Tanque.tanques[Datos.turnos])
                            puntosExplosionX, puntosExplosionY = terreno.calcular_puntos_explosion(terreno.calcular_centro_explosion(), Tanque.tanques[Datos.turnos])
                            if Datos.bala_tanque.verificar_impacto_tanque_explosion(Tanque.tanques[indice], puntosExplosionX, puntosExplosionY):
                                #KILL Y SUICIDIO
                                if Datos.impacto_tanque != Tanque.tanques[indice].color:
                                    if Tanque.tanques[Datos.turnos].tipo_bala == 1:
                                        Tanque.tanques[indice].vida -= Tanque.tanques[Datos.turnos].Bala105mm
                                    elif Tanque.tanques[Datos.turnos].tipo_bala == 2:
                                        Tanque.tanques[indice].vida -= Tanque.tanques[Datos.turnos].Bala80mm
                                    elif Tanque.tanques[Datos.turnos].tipo_bala == 3:
                                        Tanque.tanques[indice].vida -= Tanque.tanques[Datos.turnos].Bala60mm
                                Tanque.acomodarTanque(screen, terreno, primera_iteracion) 
                            if Tanque.tanques[indice].vida <= 0:
                                print("vida del tanque " + Datos.color_tanque[Tanque.tanques[indice].color] + " llegó a 0 por daño de explosion al tanque o impacto directo")
                                if Datos.turnos == indice:
                                    Tanque.tanques[Datos.turnos].suicidios += 1
                                    print("suicidio del tanque " + Datos.color_tanque[Tanque.tanques[Datos.turnos].color])
                                else:
                                    Tanque.tanques[Datos.turnos].kills += 1
                                    print("Tanque " + Datos.color_tanque[Tanque.tanques[Datos.turnos].color] + " mató a tanque " + Datos.color_tanque[Tanque.tanques[indice].color])
                            Datos.impacto_tanque = 0
                            Datos.bala_tanque = None
                            Datos.comprobar_viento = False
                            if Datos.turnos < len(Tanque.tanques)-1:
                                Datos.turnos += 1
                            else:
                                Datos.turnos = 0
                                Datos.rondas += 1
                            break
              
                Datos.tiempo_transcurrido += incremento

            Tanque.acomodarTanque(screen, terreno, primera_iteracion) 

            # Representacion gráfica de los Datos
            Pantalla.pantalla.muestra_texto(screen, fuente ,Tanque.tanques[Datos.turnos], Datos.ang_tank[Tanque.tanques[Datos.turnos].angulo-30],Datos.bala_tanque)
            #linea que muestra los tanques
            Pantalla.pantalla.muestra_imagen(screen, Tanque.tanques, Datos.turnos)
            Pantalla.pantalla.muestra_datos(screen, fuente, Datos.altura_maxima, Datos.distancia_maxima, Tanque.tanques)
            if Datos.bala_tanque is not None and Datos.bala_tanque.visualizar():
                Pantalla.pantalla.muestra_bala(screen, Tanque.tanques[Datos.turnos].tipo_bala, Datos.bala_tanque.xactual())
            for indice, tanque in enumerate(Tanque.tanques):
                Tanque.tanques[indice].extremo_canonx, Tanque.tanques[indice].extremo_canony = Pantalla.pantalla.prerotate(screen, Tanque.tanques[indice].color, -(Datos.ang_tank[Tanque.tanques[indice].angulo]-90), Tanque.tanques[indice].pivote)
            #Mostrar tooltip para la vida y el color del tanque
            #Detectar la posicion del mause
            posMause_x, posMause_y = pygame.mouse.get_pos()

            #mostrar el tooltip si el mause esta sobre el tanque
            for indice, tanque in enumerate(Tanque.tanques):
                if Tanque.tanques[indice].x < posMause_x < Tanque.tanques[indice].x + 42 and Tanque.tanques[indice].y < posMause_y < Tanque.tanques[indice].y + 42:
                    Juego.mostrar_tooltip(Tanque.tanques[indice], screen, posMause_x, posMause_y)
            #mostrar si no quedan balas
            if Datos.anima_quedan_balas:
                Pantalla.pantalla.muestra_no_balas(screen, fuente, Tanque.tanques[Datos.turnos])
            if Datos.viento_habilitado and Datos.tecla_espacio_presionada == False and Datos.comprobar_viento == False:
                Datos.comprobar_viento = True
                Bala.actualizar_direccion_viento()
            pygame.display.flip()
            if salirJuego:
                break