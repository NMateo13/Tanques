import pygame, sys, Terreno, Pantalla, imagenes, random, math, Datos
from Bala import Bala
from Tanque import Tanque
from Terreno import Terreno
from Canon import Canon
from Jugador import Jugador

class Juego:

    def draw_text(text, font, x, y, color, screen):
        textobj = font.render(text, 1, color)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        screen.blit(textobj, textrect)

    def opciones(screen):
        while True:
            salir = False

            boton_800 = pygame.Rect((Datos.PANT_ANCHO / 2) - 450, (Datos.PANT_ALTO / 2) - 140, 100, 50)
            boton_default = pygame.Rect((Datos.PANT_ANCHO / 2) - 450, (Datos.PANT_ALTO / 2) - 80, 100, 50)
            boton_1080 = pygame.Rect((Datos.PANT_ANCHO / 2) - 450, (Datos.PANT_ALTO / 2) - 20, 100, 50)
            boton_controles = pygame.Rect((Datos.PANT_ANCHO / 2) - 450, (Datos.PANT_ALTO / 2) + 190, 100, 50)
            boton_gravedad_baja = pygame.Rect((Datos.PANT_ANCHO / 2) + 350, (Datos.PANT_ALTO / 2) - 140, 100, 50)
            boton_gravedad_default = pygame.Rect((Datos.PANT_ANCHO / 2) + 350, (Datos.PANT_ALTO / 2) - 80, 100, 50)
            boton_gravedad_alta = pygame.Rect((Datos.PANT_ANCHO / 2) + 350, (Datos.PANT_ALTO / 2) - 20, 100, 50)
        
            screen.fill(Datos.WHITE)
            fuente = pygame.font.Font(None, 36)
            Juego.draw_text('Opciones', fuente, (Datos.PANT_ANCHO / 2) - 58, (Datos.PANT_ALTO / 2) - 250, Datos.BLACK, screen)
            Juego.draw_text('Resolucion', fuente, (Datos.PANT_ANCHO / 2) - 450, (Datos.PANT_ALTO / 2) - 200, Datos.BLACK, screen)
            Juego.draw_text('800x800', fuente, (Datos.PANT_ANCHO / 2) - 438, (Datos.PANT_ALTO / 2) - 137, Datos.BLACK, screen)
            Juego.draw_text('Default', fuente, (Datos.PANT_ANCHO / 2) - 436, (Datos.PANT_ALTO / 2) - 78, Datos.BLACK, screen)
            Juego.draw_text('1920x1080', fuente, (Datos.PANT_ANCHO / 2) - 442, (Datos.PANT_ALTO / 2) - 19, Datos.BLACK, screen)
            Juego.draw_text('Juego.controles', fuente, (Datos.PANT_ANCHO / 2) - 443, (Datos.PANT_ALTO / 2) + 191, Datos.BLACK, screen)
            Juego.draw_text('Menu: Escape', fuente, (Datos.PANT_ANCHO / 2) + 303, (Datos.PANT_ALTO / 2) + 191, Datos.BLACK, screen)
            Juego.draw_text('Gravedad', fuente, (Datos.PANT_ANCHO / 2) + 303, (Datos.PANT_ALTO / 2) - 200, Datos.BLACK, screen)
            Juego.draw_text('Gravedad Baja', fuente, (Datos.PANT_ANCHO / 2) + 303, (Datos.PANT_ALTO / 2) - 140, Datos.BLACK, screen)
            Juego.draw_text('Gravedad Default', fuente, (Datos.PANT_ANCHO / 2) + 303, (Datos.PANT_ALTO / 2) - 80, Datos.BLACK, screen)
            Juego.draw_text('Gravedad Alta', fuente, (Datos.PANT_ANCHO / 2) + 303, (Datos.PANT_ALTO / 2) - 20, Datos.BLACK, screen)

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
                        pygame.display.set_mode((Datos.PANT_ANCHO, Datos.PANT_ALTO))
                    if boton_default.collidepoint(event.pos):
                        Datos.PANT_ANCHO = 1200
                        Datos.PANT_ALTO = 600
                        pygame.display.set_mode((Datos.PANT_ANCHO, Datos.PANT_ALTO))
                    if boton_1080.collidepoint(event.pos):
                        Datos.PANT_ANCHO = 1920
                        Datos.PANT_ALTO = 1080
                        pygame.display.set_mode((Datos.PANT_ANCHO, Datos.PANT_ALTO))
                    if boton_controles.collidepoint(event.pos):
                        Juego.controles(screen)
                        salir = True
                    if boton_gravedad_baja.collidepoint(event.pos):
                        Datos.gravedad = 5
                    if boton_gravedad_default.collidepoint(event.pos):
                        Datos.gravedad = 9.8
                    if boton_gravedad_alta.collidepoint(event.pos):
                        Datos.gravedad = 20

            if salir:
                break

    def controles(screen):
        while True:
            salir = False
            screen.fill(Datos.WHITE)
            screen.blit(imagenes.FondoControles, (0, 0))
            fuente = pygame.font.Font(None, 36)
            Juego.draw_text('controles', fuente, (Datos.PANT_ANCHO / 2) - 58, (Datos.PANT_ALTO / 2) - 250, Datos.BLACK, screen) 
            Juego.draw_text('Jugador 1', fuente, (Datos.PANT_ANCHO / 2) - 418, (Datos.PANT_ALTO / 2) - 200, Datos.BLACK, screen) 
            Juego.draw_text('Jugador 2', fuente, (Datos.PANT_ANCHO / 2) + 303, (Datos.PANT_ALTO / 2) - 200, Datos.BLACK, screen) 
            fuente = pygame.font.Font(None, 23)
            Juego.draw_text('W: Más ángulo', fuente, (Datos.PANT_ANCHO / 2) - 438, (Datos.PANT_ALTO / 2) - 137, Datos.BLACK, screen)
            fuente = pygame.font.Font(None, 21)
            Juego.draw_text('Arriba: Más ángulo', fuente, (Datos.PANT_ANCHO / 2) + 277, (Datos.PANT_ALTO / 2) - 137, Datos.BLACK, screen)
            fuente = pygame.font.Font(None, 23)
            Juego.draw_text('S: Menos ángulo', fuente, (Datos.PANT_ANCHO / 2) - 436, (Datos.PANT_ALTO / 2) - 78, Datos.BLACK, screen)
            fuente = pygame.font.Font(None, 21)
            Juego.draw_text('Abajo: Menos ángulo', fuente, (Datos.PANT_ANCHO / 2) + 278, (Datos.PANT_ALTO / 2) - 78, Datos.BLACK, screen)
            fuente = pygame.font.Font(None, 23)
            Juego.draw_text('A: Menos potencia', fuente, (Datos.PANT_ANCHO / 2) - 442, (Datos.PANT_ALTO / 2) - 19, Datos.BLACK, screen)
            fuente = pygame.font.Font(None, 17)
            Juego.draw_text('Izquierda: Menos potencia', fuente, (Datos.PANT_ANCHO / 2) + 280, (Datos.PANT_ALTO / 2) - 17, Datos.BLACK, screen)
            fuente = pygame.font.Font(None, 23)
            Juego.draw_text('D: Más potencia', fuente, (Datos.PANT_ANCHO / 2) - 443, (Datos.PANT_ALTO / 2) + 39, Datos.BLACK, screen)
            fuente = pygame.font.Font(None, 17)
            Juego.draw_text('Derecha: Más potencia', fuente, (Datos.PANT_ANCHO / 2) + 283, (Datos.PANT_ALTO / 2) + 41, Datos.BLACK, screen)
            fuente = pygame.font.Font(None, 26)
            Juego.draw_text('1: Bala 105mm', fuente, (Datos.PANT_ANCHO / 2) - 425, (Datos.PANT_ALTO / 2) + 116, Datos.BLACK, screen)
            fuente = pygame.font.Font(None, 26)
            Juego.draw_text('2: Bala 80mm', fuente, (Datos.PANT_ANCHO / 2) - 57, (Datos.PANT_ALTO / 2) + 116, Datos.BLACK, screen)
            fuente = pygame.font.Font(None, 26)
            Juego.draw_text('3: Bala 60mm', fuente, (Datos.PANT_ANCHO / 2) + 307, (Datos.PANT_ALTO / 2) + 116, Datos.BLACK, screen)
            Juego.draw_text('Espacio: Disparar', fuente, (Datos.PANT_ANCHO / 2) - 75, (Datos.PANT_ALTO / 2) + 42, Datos.BLACK, screen)
            fuente = pygame.font.Font(None, 26)
            Juego.draw_text('Menu: Escape', fuente, (Datos.PANT_ANCHO / 2) - 59, (Datos.PANT_ALTO / 2) + 191, Datos.BLACK, screen)

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

    def muestra_ganador(Ganador, screen, fuente): #Función para mostrar el ganador del juego
        
        screen.fill(Datos.WHITE) 
        texto_ganador = fuente.render(f"Ganador: Jugador {Ganador}", True, Datos.BLACK) 
        screen.blit(texto_ganador, (Datos.PANT_ANCHO / 2 - texto_ganador.get_width() / 2, Datos.PANT_ALTO / 2 - texto_ganador.get_height() / 2)) 
        pygame.display.flip() 
        pygame.time.delay(3000) 
        sys.exit() 

    def seleccion(screen, fuente):
        
        while True:
            salir = False

            jugar = pygame.draw.rect(screen, Datos.BLACK, (Datos.PANT_ANCHO / 1.2, Datos.PANT_ALTO / 10, 100, 50))
            volver = pygame.draw.rect(screen, Datos.BLACK, (Datos.PANT_ANCHO / 1.2, Datos.PANT_ALTO / 1.53, 100, 50))
            controles = pygame.draw.rect(screen, Datos.BLACK, (Datos.PANT_ANCHO / 1.2, Datos.PANT_ALTO / 2.65, 100, 50))

            Pantalla.pantalla.muestra_seleccion(screen, fuente) 

            j1 = pygame.draw.rect(screen, Datos.PURPLE, (Datos.PANT_ANCHO / 10, Datos.PANT_ALTO / 3.5, 100, 20))
            j2 = pygame.draw.rect(screen, Datos.PURPLE, (Datos.PANT_ANCHO / 3, Datos.PANT_ALTO / 3.5, 100, 20))
            j3 = pygame.draw.rect(screen, Datos.PURPLE, (Datos.PANT_ANCHO / 1.764, Datos.PANT_ALTO / 3.5, 100, 20))
            j4 = pygame.draw.rect(screen, Datos.PURPLE, (Datos.PANT_ANCHO / 10, Datos.PANT_ALTO / 1.457, 100, 20))
            j5 = pygame.draw.rect(screen, Datos.PURPLE, (Datos.PANT_ANCHO / 3, Datos.PANT_ALTO / 1.457, 100, 20))
            j6 = pygame.draw.rect(screen, Datos.PURPLE, (Datos.PANT_ANCHO / 1.764, Datos.PANT_ALTO / 1.457, 100, 20))

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
                                Jugador.crearJugador(indice)
                        salir = True
                    if volver.collidepoint(event.pos):
                        salir = True
                    if controles.collidepoint(event.pos):
                        Juego.controles(screen)    
                keys = pygame.key.get_pressed()
                if keys[pygame.K_ESCAPE]:
                    salir = True       

            if salir:
                break

    def juego(screen, fuente):

        #Creacion clases (Terreno y tanques)
        salirJuego = False

        terreno = Terreno(Datos.PANT_ANCHO, Datos.PANT_ALTO)

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

        salir = screen.blit(imagenes.Exit, (Pantalla.pantalla.ancho - imagenes.Exit.get_width() - 650, 10))
        reset = screen.blit(imagenes.Restart, (Pantalla.pantalla.ancho - imagenes.Restart.get_width() - 550, 10))
        #antes de comenzar el juego se baraja el orden de los jugadores haciendo shuffle al arraylist de tanques
        random.shuffle(Tanque.tanques)
        #inicia el turno del jugador de Tanque.tanques[0] y se irá aumentando el indice para que jueguen todos los jugadores. iniciando en turno = 0
        turno = 0
        while True:
            Clock.tick(Datos.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if reset.collidepoint(pygame.mouse.get_pos()):
                        salirJuego = True
                        Datos.reiniciar = True  # Reiniciar el juego
                    if salir.collidepoint(pygame.mouse.get_pos()):
                        salirJuego = True  # Volver al menú principal
            
            keys = pygame.key.get_pressed()

            if keys[pygame.K_ESCAPE]:
                salirJuego = True
            
            if keys[pygame.K_SPACE]:
                Datos.tecla_espacio_presionada = True
            
            #Controles para el jugador Tanque.tanques[turno]
            if keys[pygame.K_w]:
                if Tanque.tanques[turno].angulo == 66:
                    Tanque.tanques[turno].angulo = 0
                else:
                    Tanque.tanques[turno].angulo += 1   
            elif keys[pygame.K_s]:
                if Tanque.tanques[turno].angulo == 0:
                    Tanque.tanques[turno].angulo = 66
                else:
                    Tanque.tanques[turno].angulo -= 1
            elif keys[pygame.K_a]:
                Tanque.tanques[turno].velocidad -= 5
                Tanque.tanques[turno].velocidad = max(0, Tanque.tanques[turno].velocidad)
            elif keys[pygame.K_d]:
                Tanque.tanques[turno].velocidad += 5
                Tanque.tanques[turno].velocidad = min(300, Tanque.tanques[turno].velocidad)
            elif keys[pygame.K_1]:
                Tanque.tanques[turno].tipo_bala = 1
                Tanque.tanques[turno].radioExplosion = 75
            elif keys[pygame.K_2]:
                Tanque.tanques[turno].tipo_bala = 2
                Tanque.tanques[turno].radioExplosion = 50
            elif keys[pygame.K_3]:
                Tanque.tanques[turno].tipo_bala = 3
                Tanque.tanques[turno].radioExplosion = 25

            screen.blit(imagenes.Background, (0, 0))
            terreno.dibujar(screen)
            screen.blit(imagenes.HUD, (0, Datos.PANT_ALTO - 120))

            #DIBUJAR HITBOXES
            for indice, tanque in enumerate(Tanque.tanques):
                Tanque.tanques[indice].dibujar(screen)

            #Verificar vida de los tanques, si la vida es menor o igual a 0, se elimina el tanque y si solo queda un tanque, se muestra el ganador
            for indice, tanque in enumerate(Tanque.tanques):
                if Tanque.tanques[indice].vida <=0:
                    del Tanque.tanques[indice]
                if len(Tanque.tanques) == 1:
                    Ganador = Tanque.tanques[0].indice
                    Juego.muestra_ganador(Ganador, screen, fuente)
            #comprobaciones de balas antes de disparar
            if Datos.tecla_espacio_presionada:
                if Datos.bala_tanque is None:
                    Datos.mostrar_altura = Tanque.tanques[turno].indice
                    if Tanque.tanques[turno].tipo_bala == 1 and Tanque.tanques[turno].cantBala105mm == 0:
                        print("No quedan balas")
                        Datos.tecla_espacio_presionada = False
                        Datos.tiempo_transcurrido = 0
                    elif Tanque.tanques[turno].tipo_bala == 2 and Tanque.tanques[turno].cantBala80mm == 0:
                        print("No quedan balas")
                        Datos.tecla_espacio_presionada = False
                        Datos.tiempo_transcurrido = 0
                    elif Tanque.tanques[turno].tipo_bala == 3 and Tanque.tanques[turno].cantBala60mm == 0:
                        print("No quedan balas")
                        Datos.tecla_espacio_presionada = False
                        Datos.tiempo_transcurrido = 0
                    else:
                        #si pasa las comprobaciones se dispara la bala
                        Datos.bala_tanque = Tanque.tanques[turno].disparar(Tanque.tanques[turno].extremo_canonx, Tanque.tanques[turno].extremo_canony, Datos.ang_tank[Tanque.tanques[turno].angulo], Tanque.tanques[turno].velocidad, Datos.tiempo_transcurrido, screen, Datos.BLACK, Tanque.tanques[turno].tipo_bala)
                else:
                    Datos.altura_maxima = Datos.bala_tanque.punto_maximo(Datos.altura_maxima)
                    Datos.distancia_maxima = Datos.bala_tanque.distancia_maxima(Tanque.tanques[turno].x, Datos.distancia_maxima)
                    for indice, tanque in enumerate(Tanque.tanques):
                        if Datos.bala_tanque.verificar_impacto_ancho(Datos.PANT_ANCHO):
                            Datos.bala_tanque = None
                            Datos.tecla_espacio_presionada = False
                            turno += 1
                            Datos.tiempo_transcurrido = 0
                            break
                        elif Terreno.verificar_colision(terreno, Datos.bala_tanque):
                            Datos.tecla_espacio_presionada = False
                            turno += 1
                            Datos.tiempo_transcurrido = 0
                            Terreno.modificar_terreno(terreno)
                            puntosExplosionX, puntosExplosionY = Terreno.calcular_puntos_explosion(Datos.bala_tanque, Tanque.tanques[turno].radioExplosion)
                            for indice, tanque in enumerate(Tanque.tanques):
                                if Datos.bala_tanque.verificar_impacto_tanque_explosion(Tanque.tanques[indice], puntosExplosionX, puntosExplosionY):
                                    if Tanque.tanques[turno].tipo_bala == 1:
                                        Tanque.tanques[indice].vida -= Tanque.tanques[turno].Bala105mm
                                    elif Tanque.tanques[turno].tipo_bala == 2:
                                        Tanque.tanques[indice].vida -= Tanque.tanques[turno].Bala80mm
                                    elif Tanque.tanques[turno].tipo_bala == 3:
                                        Tanque.tanques[indice].vida -= Tanque.tanques[turno].Bala60mm
                            Datos.bala_tanque = None
                            break
                        elif Datos.bala_tanque.verificar_impacto_tanque(Tanque.tanques[indice]):
                            if Tanque.tanques[turno].tipo_bala == 1:
                                Tanque.tanques[indice].vida -= Tanque.tanques[turno].Bala105mm
                            elif Tanque.tanques[turno].tipo_bala == 2:
                                Tanque.tanques[indice].vida -= Tanque.tanques[turno].Bala80mm
                            elif Tanque.tanques[turno].tipo_bala == 3:
                                Tanque.tanques[indice].vida -= Tanque.tanques[turno].Bala60mm
                            Datos.tecla_espacio_presionada = False
                            turno += 1
                            Datos.tiempo_transcurrido = 0
                            Terreno.modificar_terreno(terreno)
                            puntosExplosionX, puntosExplosionY = Terreno.calcular_puntos_explosion(Datos.bala_tanque, Tanque.tanques[turno].radioExplosion)
                            for indice, tanque in enumerate(Tanque.tanques):
                                if Datos.bala_tanque.verificar_impacto_tanque_explosion(Tanque.tanques[indice], puntosExplosionX, puntosExplosionY):
                                    if Tanque.tanques[turno].tipo_bala == 1:
                                        Tanque.tanques[indice].vida -= Tanque.tanques[turno].Bala105mm
                                    elif Tanque.tanques[turno].tipo_bala == 2:
                                        Tanque.tanques[indice].vida -= Tanque.tanques[turno].Bala80mm
                                    elif Tanque.tanques[turno].tipo_bala == 3:
                                        Tanque.tanques[indice].vida -= Tanque.tanques[turno].Bala60mm
                            Datos.bala_tanque = None
                            break
            

                        
            Datos.tiempo_transcurrido += incremento
            for indice, tanque in enumerate(Tanque.tanques):
                if Tanque.tanques[indice].y != (terreno.alto - terreno.terreno[Tanque.tanques[indice].indice] - 16):
                    Tanque.tanques[indice].y = terreno.alto - terreno.terreno[Tanque.tanques[indice].indice] - 16
                    Tanque.tanques[indice].pivote = [Tanque.tanques[indice].x+21, Tanque.tanques[indice].y-5]
                    Tanque.tanques[indice].extremo_canonx, Tanque.tanques[indice].extremo_canony = Pantalla.pantalla.prerotate(screen, Tanque.tanques[indice].color, Datos.ang_tank[0], Tanque.tanques[indice].pivote)


            # Descuento de balas        
            if Datos.tipo_bala1 == 1:
                Datos.cantidad_balas1 = Tanque.tanques[turno].cantBala105mm
            elif Datos.tipo_bala1 == 2:
                Datos.cantidad_balas1 = Tanque.tanques[turno].cantBala80mm
            elif Datos.tipo_bala1 == 3:
                Datos.cantidad_balas1 = Tanque.tanques[turno].cantBala60mm

            """# Representacion gráfica de los Datos
            Pantalla.pantalla.muestra_salud(screen, fuente,Tanque.tanques[indice].vida)
            Pantalla.pantalla.muestra_potencia(screen, fuente,Datos.velocidad_jugador1,Datos.velocidad_jugador2)
            Pantalla.pantalla.muestra_angulo(screen, fuente,Datos.ang_tank[Datos.angulo_jugador1-30],Datos.ang_tank[Datos.angulo_jugador2-30])    
            Pantalla.pantalla.muestra_texto(screen, fuente ,Datos.turno1,Datos.cantidad_balas1,Datos.cantidad_balas2)"""
            #linea que muestra los tanques
            Pantalla.pantalla.muestra_imagen(screen, Datos.tipo_bala1, Datos.tipo_bala2, Tanque.tanques)
            #Pantalla.pantalla.muestra_altura(screen, fuente, Datos.altura_maxima, Datos.mostrar_altura1, Datos.mostrar_altura2)
            #Pantalla.pantalla.muestra_distancia(screen, fuente, Datos.distancia_maxima, Datos.mostrar_altura1, Datos.mostrar_altura2)
            if Datos.bala_tanque is not None and Datos.bala_tanque.visualizar():
                Pantalla.pantalla.muestra_bala(screen, Datos.tipo_bala, Datos.bala_tanque.xactual())
            
            for indice, tanque in enumerate(Tanque.tanques):
                Tanque.tanques[indice].extremo_canonx, Tanque.tanques[indice].extremo_canony = Pantalla.pantalla.prerotate(screen, Tanque.tanques[indice].color, -(Datos.ang_tank[Tanque.tanques[indice].angulo]-90), Tanque.tanques[indice].pivote)
            pygame.display.flip()
            if salirJuego:
                break