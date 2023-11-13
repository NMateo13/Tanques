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

            j1 = pygame.draw.rect(screen, Datos.BLACK, (Datos.PANT_ANCHO / 10, Datos.PANT_ALTO / 3.5, 100, 20))
            j2 = pygame.draw.rect(screen, Datos.BLACK, (Datos.PANT_ANCHO / 3, Datos.PANT_ALTO / 3.5, 100, 20))
            j3 = pygame.draw.rect(screen, Datos.BLACK, (Datos.PANT_ANCHO / 1.764, Datos.PANT_ALTO / 3.5, 100, 20))
            j4 = pygame.draw.rect(screen, Datos.BLACK, (Datos.PANT_ANCHO / 10, Datos.PANT_ALTO / 1.457, 100, 20))
            j5 = pygame.draw.rect(screen, Datos.BLACK, (Datos.PANT_ANCHO / 3, Datos.PANT_ALTO / 1.457, 100, 20))
            j6 = pygame.draw.rect(screen, Datos.BLACK, (Datos.PANT_ANCHO / 1.764, Datos.PANT_ALTO / 1.457, 100, 20))

            for indice,jugador in enumerate(Jugador.jugadores):
                if jugador == 0:
                        text = 'Jugador'
                elif jugador == 1:
                    text = 'IA'
                else:
                    text = 'No juega'

                if indice < 3:
                    texto = Juego.draw_text(text, fuente, Datos.PANT_ANCHO / Datos.lista_cuadrar_jugadores_texto_x[indice], Datos.PANT_ALTO / Datos.lista_cuadrar_jugadores_texto_y[0], Datos.WHITE, screen)
                else:
                    texto = Juego.draw_text(text, fuente, Datos.PANT_ANCHO / Datos.lista_cuadrar_jugadores_texto_x[indice-3], Datos.PANT_ALTO / Datos.lista_cuadrar_jugadores_texto_y[1], Datos.WHITE, screen)


            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:  
                    if j1.collidepoint(event.pos):
                        if Jugador.jugadores[0]==2:
                            Jugador.jugadores[0] = 0
                        else:
                            Jugador.jugadores[0] += 1
                        pygame.display.update()
                    if j2.collidepoint(event.pos):
                            if Jugador.jugadores[1] == 2:
                                Jugador.jugadores[1] = 0
                            else:
                                Jugador.jugadores[1] += 1
                            pygame.display.update()
                    if j3.collidepoint(event.pos):
                            if Jugador.jugadores[2] == 2:
                                Jugador.jugadores[2] = 0
                            else:
                                Jugador.jugadores[2] += 1
                            pygame.display.update()
                    if j4.collidepoint(event.pos):
                            if Jugador.jugadores[3] == 2:
                                Jugador.jugadores[3] = 0
                            else:
                                Jugador.jugadores[3] += 1
                            pygame.display.update()
                    if j5.collidepoint(event.pos):
                            if Jugador.jugadores[4] == 2:
                                Jugador.jugadores[4] = 0
                            else:
                                Jugador.jugadores[4] += 1
                            pygame.display.update()
                    if j6.collidepoint(event.pos):
                            if Jugador.jugadores[5] == 2:
                                Jugador.jugadores[5] = 0
                            else:
                                Jugador.jugadores[5] += 1
                            pygame.display.update()  
                    if jugar.collidepoint(event.pos):
                        pass
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
        tanque1 = Tanque.crearTanques(terreno, Datos.bandera_tanque)
        tanque2 = Tanque.crearTanques(terreno, Datos.bandera_tanque)

        canon1 = Canon(tanque1)
        canon2 = Canon(tanque2)

        #Inicio de variables 
        Datos.reiniciar_datos()

        Clock = pygame.time.Clock()

        tanque1.pivote = [tanque1.x+21, tanque1.y-5]
        tanque2.pivote = [tanque2.x+21, tanque2.y-5]

        Datos.exremo_canonx_1, Datos.exremo_canony_1 = Pantalla.pantalla.prerotate(screen, 1, Datos.ang_tank[Datos.angulo_jugador1], tanque1.pivote)
        Datos.extremo_canonx_2, Datos.extremo_canony_2 =Pantalla.pantalla.prerotate(screen, 2, Datos.ang_tank[Datos.angulo_jugador2]-90, tanque2.pivote)

        incremento = 0.035

        salir = screen.blit(imagenes.Exit, (Pantalla.pantalla.ancho - imagenes.Exit.get_width() - 650, 10))
        reset = screen.blit(imagenes.Restart, (Pantalla.pantalla.ancho - imagenes.Restart.get_width() - 550, 10))

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

            # Juego.controles del jugador 1
            if Datos.turno1:
                if keys[pygame.K_w]:
                    if Datos.angulo_jugador1 == 66:
                        Datos.angulo_jugador1 = 0
                    else:
                        Datos.angulo_jugador1 += 1
                elif keys[pygame.K_s]:
                    if Datos.angulo_jugador1 == 0:
                        Datos.angulo_jugador1 = 66
                    else:
                        Datos.angulo_jugador1 -= 1

                elif keys[pygame.K_a]:
                    Datos.velocidad_jugador1 -= 5
                    Datos.velocidad_jugador1 = max(0, Datos.velocidad_jugador1)
                elif keys[pygame.K_d]:
                    Datos.velocidad_jugador1 += 5
                    Datos.velocidad_jugador1 = min(300, Datos.velocidad_jugador1)

                # Cambio de bala J1
                elif keys[pygame.K_1]:
                    Datos.tipo_bala1 = 1
                    Datos.radioExplosion = 75
                elif keys[pygame.K_2]:
                    Datos.tipo_bala1 = 2
                    Datos.radioExplosion = 50
                elif keys[pygame.K_3]:
                    Datos.tipo_bala1 = 3
                    Datos.radioExplosion = 25

            # Juego.controles del jugador 2
            if Datos.turno2:
                if keys[pygame.K_UP]:
                    if Datos.angulo_jugador2 == 66:
                        Datos.angulo_jugador2 = 0
                    else:
                        Datos.angulo_jugador2 += 1
                elif keys[pygame.K_DOWN]:
                    if Datos.angulo_jugador2 == 0:
                        Datos.angulo_jugador2 = 66
                    else:
                        Datos.angulo_jugador2 -= 1
                elif keys[pygame.K_LEFT]:
                    Datos.velocidad_jugador2 -= 5
                    Datos.velocidad_jugador2 = max(0, Datos.velocidad_jugador2)
                elif keys[pygame.K_RIGHT]:
                    Datos.velocidad_jugador2 += 5
                    Datos.velocidad_jugador2 = min(300, Datos.velocidad_jugador2)

                # Cambio de bala J2
                elif keys[pygame.K_1]:
                    Datos.tipo_bala2 = 1
                    Datos.radioExplosion = 75
                elif keys[pygame.K_2]:
                    Datos.tipo_bala2 = 2
                    Datos.radioExplosion = 50
                elif keys[pygame.K_3]:
                    Datos.tipo_bala2 = 3
                    Datos.radioExplosion = 25

            screen.blit(imagenes.Background, (0, 0))
            terreno.dibujar(screen)
            screen.blit(imagenes.HUD, (0, Datos.PANT_ALTO - 120))
            tanque1.dibujar(screen)  #DIBUJAN HITBOX
            tanque2.dibujar(screen)  #DIBUJAN HITBOX

            if tanque1.vida <= 0: # Si la vida del tanque 1 es menor o igual a 0, el ganador es el tanque 2
                Ganador = 2
                Juego.muestra_ganador(Ganador, screen, fuente)

            if tanque2.vida <= 0: # Si la vida del tanque 2 es menor o igual a 0, el ganador es el tanque 1
                Ganador = 1
                Juego.muestra_ganador(Ganador, screen, fuente)

            if Datos.tecla_espacio_presionada and Datos.turno1:
                if Datos.bala_tanque1 is None:
                    Datos.mostrar_altura1 = True
                    Datos.mostrar_altura2 = False
                    if Datos.tipo_bala1 == 1 and tanque1.cantBala105mm == 0:
                        print("No quedan balas")
                        Datos.tecla_espacio_presionada = False
                        Datos.tiempo_transcurrido = 0
                    elif Datos.tipo_bala1 == 2 and tanque1.cantBala80mm == 0:
                        print("No quedan balas")
                        Datos.tecla_espacio_presionada = False
                        Datos.tiempo_transcurrido = 0
                    elif Datos.tipo_bala1 == 3 and tanque1.cantBala60mm == 0:
                        print("No quedan balas")
                        Datos.tecla_espacio_presionada = False
                        Datos.tiempo_transcurrido = 0
                    else:
                        Datos.bala_tanque1 = tanque1.disparar(Datos.exremo_canonx_1, Datos.exremo_canony_1, Datos.ang_tank[Datos.angulo_jugador1], Datos.velocidad_jugador1, Datos.tiempo_transcurrido, screen, Datos.BLACK, Datos.tipo_bala1)
                else:
                    Datos.altura_maxima = Datos.bala_tanque1.punto_maximo(Datos.altura_maxima)
                    Datos.distancia_maxima = Datos.bala_tanque1.distancia_maxima(tanque1.x, Datos.distancia_maxima)
                    Datos.bala_tanque1.verificacion(Datos.tiempo_transcurrido, screen, Datos.BLACK)
                    impacto_tanque = Datos.bala_tanque1.verificar_impacto_tanque(tanque2)
                    impacto_tanque_igual = Datos.bala_tanque1.verificar_impacto_tanque(tanque1)
                    impacto_terreno = terreno.verificar_colision(Datos.bala_tanque1)
                    impacto_borde = Datos.bala_tanque1.verificar_impacto_ancho(Datos.PANT_ANCHO)
                            
                    if impacto_tanque:
                        if Datos.tipo_bala1 == 1:
                            tanque2.vida -= tanque1.Bala105mm
                            Datos.bala_tanque1 = None
                            Datos.tecla_espacio_presionada = False
                            Datos.turno1 = False
                            Datos.turno2 = True
                            Datos.tiempo_transcurrido = 0
                        
                        elif Datos.tipo_bala1 == 2:
                            tanque2.vida -= tanque1.Bala80mm
                            Datos.bala_tanque1 = None
                            Datos.tecla_espacio_presionada = False
                            Datos.turno1 = False
                            Datos.turno2 = True
                            Datos.tiempo_transcurrido = 0

                        elif Datos.tipo_bala1 == 3:
                            tanque2.vida -= tanque1.Bala60mm
                            Datos.bala_tanque1 = None
                            Datos.tecla_espacio_presionada = False
                            Datos.turno1 = False
                            Datos.turno2 = True
                            Datos.tiempo_transcurrido = 0
                    elif impacto_tanque_igual:
                        if Datos.tipo_bala1 == 1:
                            tanque1.vida -= tanque1.Bala105mm
                            Datos.bala_tanque1 = None
                            Datos.tecla_espacio_presionada = False
                            Datos.turno1 = False
                            Datos.turno2 = True
                            Datos.tiempo_transcurrido = 0
                        
                        elif Datos.tipo_bala1 == 2:
                            tanque1.vida -= tanque1.Bala80mm
                            Datos.bala_tanque1 = None
                            Datos.tecla_espacio_presionada = False
                            Datos.turno1 = False
                            Datos.turno2 = True
                            Datos.tiempo_transcurrido = 0

                        elif Datos.tipo_bala1 == 3:
                            tanque1.vida -= tanque1.Bala60mm
                            Datos.bala_tanque1 = None
                            Datos.tecla_espacio_presionada = False
                            Datos.turno1 = False
                            Datos.turno2 = True
                            Datos.tiempo_transcurrido = 0
                    elif impacto_borde:
                            Datos.bala_tanque1 = None
                            Datos.tecla_espacio_presionada = False
                            Datos.turno1 = False
                            Datos.turno2 = True
                            Datos.tiempo_transcurrido = 0

                    elif impacto_terreno:
                        for x, y in Datos.bala_tanque1.trayectoria:
                            Datos.centroExplosion.append(int(x))
                            Datos.centroExplosion.append(int(y))
                            for i in range(Datos.radioExplosion):
                                ancho= []
                                ancho.append(int(x)-Datos.radioExplosion+i)
                        Datos.bala_tanque1 = None
                        Datos.tecla_espacio_presionada = False
                        Datos.turno1 = False
                        Datos.turno2 = True
                        Datos.tiempo_transcurrido = 0
                        #calculamos los puntos de la circunferencia de la explosion
                        num_puntosExplosion = int(2 * math.pi * Datos.radioExplosion)
                        puntosExplosionX = []
                        puntosExplosionY = []
                        for i in range(num_puntosExplosion):
                            angle = (2 * math.pi / num_puntosExplosion) * i
                            x = int(Datos.centroExplosion[0] + Datos.radioExplosion * math.cos(angle))
                            y = int(Datos.centroExplosion[1] + Datos.radioExplosion * math.sin(angle))
                            puntosExplosionX.append(x)
                            puntosExplosionY.append(y)
                        #verificamos cada punto x de la circunferencia y verificamos el punto y mas bajo de la circunferencia
                        for i in range(len(puntosExplosionX)):
                            pygame.draw.circle(screen, Datos.BLACK, (puntosExplosionX[i], puntosExplosionY[i]), 1)
                        pygame.display.flip()
                        conjuntoPuntos = set(puntosExplosionX)
                        Datos.arrayaux = list(conjuntoPuntos)
                        Datos.arrayaux.sort()
                        bandera = 0
                        valory = 0
                        for i in range(len(Datos.arrayaux)):
                            valory = 0
                            for j in range(len(puntosExplosionX)):
                                if Datos.arrayaux[i] == puntosExplosionX[j]:
                                    if bandera == 0:
                                        valory = puntosExplosionY[j]
                                        bandera+=1
                                    else:
                                        if puntosExplosionY[j] > valory:
                                            valory = puntosExplosionY[j]
                            valory = Datos.PANT_ALTO - valory
                            if Datos.arrayaux[i] < Datos.PANT_ANCHO and Datos.arrayaux[i] > 0:
                                if terreno.terreno[Datos.arrayaux[i]] > valory:
                                    terreno.terreno[Datos.arrayaux[i]] = valory
                        Datos.centroExplosion.clear()
                        puntosExplosionX.clear()
                        puntosExplosionY.clear()
                        Datos.arrayaux.clear()
                        conjuntoPuntos.clear()

                Datos.tiempo_transcurrido += incremento

            if Datos.tecla_espacio_presionada and Datos.turno2:
                if Datos.bala_tanque2 is None:
                    Datos.mostrar_altura1 = False
                    Datos.altura_maximamostrar_altura2 = True
                    if Datos.tipo_bala2 == 1 and tanque2.cantBala105mm == 0:
                        print("No quedan balas")
                        Datos.tecla_espacio_presionada = False
                        Datos.tiempo_transcurrido = 0
                    elif Datos.tipo_bala2 == 2 and tanque2.cantBala80mm == 0:
                        print("No quedan balas")
                        Datos.tecla_espacio_presionada = False
                        Datos.tiempo_transcurrido = 0
                    elif Datos.tipo_bala2 == 3 and tanque2.cantBala60mm == 0:
                        print("No quedan balas")
                        Datos.tecla_espacio_presionada = False
                        Datos.tiempo_transcurrido = 0
                    else:
                        Datos.bala_tanque2 = tanque2.disparar(Datos.extremo_canonx_2, Datos.extremo_canony_2, Datos.ang_tank[Datos.angulo_jugador2], Datos.velocidad_jugador2, Datos.tiempo_transcurrido, screen, Datos.BLACK, Datos.tipo_bala2)
                else:
                    Datos.altura_maxima = Datos.bala_tanque2.punto_maximo(Datos.altura_maxima)
                    Datos.distancia_maxima = Datos.bala_tanque2.distancia_maxima(tanque2.x, Datos.distancia_maxima)
                    Datos.bala_tanque2.verificacion(Datos.tiempo_transcurrido, screen, Datos.BLACK)
                    impacto_tanque = Datos.bala_tanque2.verificar_impacto_tanque(tanque1)
                    impacto_tanque_igual = Datos.bala_tanque2.verificar_impacto_tanque(tanque2)
                    impacto_terreno = terreno.verificar_colision(Datos.bala_tanque2)
                    impacto_borde = Datos.bala_tanque2.verificar_impacto_ancho(Datos.PANT_ANCHO)
                    if impacto_tanque:
                        if Datos.tipo_bala2 == 1:
                            tanque1.vida -= tanque2.Bala105mm
                            Datos.bala_tanque2 = None
                            Datos.tecla_espacio_presionada = False
                            Datos.turno2 = False
                            Datos.turno1 = True
                            Datos.tiempo_transcurrido = 0
                        
                        elif Datos.tipo_bala2 == 2:
                            tanque1.vida -= tanque2.Bala80mm
                            Datos.bala_tanque2 = None
                            Datos.tecla_espacio_presionada = False
                            Datos.turno2 = False
                            Datos.turno1 = True
                            Datos.tiempo_transcurrido = 0

                        elif Datos.tipo_bala2 == 3:
                            tanque1.vida -= tanque2.Bala60mm
                            Datos.bala_tanque2 = None
                            Datos.tecla_espacio_presionada = False
                            Datos.turno2 = False
                            Datos.turno1 = True
                            Datos.tiempo_transcurrido = 0
                    elif impacto_tanque_igual:
                        if Datos.tipo_bala2 == 1:
                            tanque2.vida -= tanque2.Bala105mm
                            Datos.nTurnos += 1
                            Datos.bala_tanque2 = None
                            Datos.tecla_espacio_presionada = False
                            Datos.turno2 = False
                            Datos.turno1 = True
                            Datos.tiempo_transcurrido = 0
                        
                        elif Datos.tipo_bala2 == 2:
                            tanque2.vida -= tanque2.Bala80mm
                            Datos.bala_tanque2 = None
                            Datos.tecla_espacio_presionada = False
                            Datos.turno2 = False
                            Datos.turno1 = True
                            Datos.tiempo_transcurrido = 0

                        elif Datos.tipo_bala2 == 3:
                            tanque2.vida -= tanque2.Bala60mm
                            Datos.bala_tanque2 = None
                            Datos.tecla_espacio_presionada = False
                            Datos.turno2 = False
                            Datos.turno1 = True
                            Datos.tiempo_transcurrido = 0
                    elif impacto_borde:
                        Datos.bala_tanque2 = None
                        Datos.tecla_espacio_presionada = False
                        Datos.turno2 = False
                        Datos.turno1 = True
                        Datos.tiempo_transcurrido = 0

                    elif impacto_terreno:
                        for x, y in Datos.bala_tanque2.trayectoria:
                            Datos.centroExplosion.append(int(x))
                            Datos.centroExplosion.append(int(y))
                        Datos.bala_tanque2 = None
                        Datos.tecla_espacio_presionada = False
                        Datos.turno2 = False
                        Datos.turno1 = True
                        Datos.tiempo_transcurrido = 0
                        #calculamos los puntos de la circunferencia de la explosion
                        num_puntosExplosion = int(2 * math.pi * Datos.radioExplosion)
                        puntosExplosionX = []
                        puntosExplosionY = []
                        for i in range(num_puntosExplosion):
                            angle = (2 * math.pi / num_puntosExplosion) * i
                            x = int(Datos.centroExplosion[0] + Datos.radioExplosion * math.cos(angle))
                            y = int(Datos.centroExplosion[1] + Datos.radioExplosion * math.sin(angle))
                            puntosExplosionX.append(x)
                            puntosExplosionY.append(y)
                        #verificamos cada punto x de la circunferencia y verificamos el punto y mas bajo de la circunferencia
                        for i in range(len(puntosExplosionX)):
                            pygame.draw.circle(screen, Datos.BLACK, (puntosExplosionX[i], puntosExplosionY[i]), 1)
                        pygame.display.flip()
                        conjuntoPuntos = set(puntosExplosionX)
                        Datos.arrayaux = list(conjuntoPuntos)
                        Datos.arrayaux.sort()
                        bandera = 0
                        valory = 0
                        for i in range(len(Datos.arrayaux)):
                            valory = 0
                            for j in range(len(puntosExplosionX)):
                                if Datos.arrayaux[i] == puntosExplosionX[j]:
                                    if bandera == 0:
                                        valory = puntosExplosionY[j]
                                        bandera+=1
                                    else:
                                        if puntosExplosionY[j] > valory:
                                            valory = puntosExplosionY[j]
                            valory = Datos.PANT_ALTO - valory
                            if Datos.arrayaux[i] < Datos.PANT_ANCHO and Datos.arrayaux[i] > 0:
                                if terreno.terreno[Datos.arrayaux[i]] > valory:
                                    terreno.terreno[Datos.arrayaux[i]] = valory
                        Datos.centroExplosion.clear()
                        puntosExplosionX.clear()
                        puntosExplosionY.clear()
                        Datos.arrayaux.clear()
                        conjuntoPuntos.clear()

                        
                Datos.tiempo_transcurrido += incremento
            if tanque1.y != (terreno.alto - terreno.terreno[tanque1.indice] - 16):
                tanque1.y = terreno.alto - terreno.terreno[tanque1.indice] - 16
                tanque1.pivote = [tanque1.x+21, tanque1.y-5]
                Datos.extremo_canonx_1, Datos.extremo_canony_1 = Pantalla.pantalla.prerotate(screen, 1, Datos.ang_tank[Datos.angulo_jugador1], tanque1.pivote)

            elif tanque2.y != (terreno.alto -  terreno.terreno[tanque2.indice] - 14):
                tanque2.y = terreno.alto -  terreno.terreno[tanque2.indice] - 14
                tanque2.pivote = [tanque2.x+21, tanque2.y-5]
                Datos.extremo_canonx_2, Datos.extremo_canony_2 =Pantalla.pantalla.prerotate(screen, 2, Datos.ang_tank[Datos.angulo_jugador2]-90, tanque2.pivote)


            # Descuento de balas        
            if Datos.tipo_bala1 == 1:
                Datos.cantidad_balas1 = tanque1.cantBala105mm
            elif Datos.tipo_bala1 == 2:
                Datos.cantidad_balas1 = tanque1.cantBala80mm
            elif Datos.tipo_bala1 == 3:
                Datos.cantidad_balas1 = tanque1.cantBala60mm
                        
            if Datos.tipo_bala2 == 1:
                Datos.cantidad_balas2 = tanque2.cantBala105mm
            elif Datos.tipo_bala2 == 2:
                Datos.cantidad_balas2 = tanque2.cantBala80mm
            elif Datos.tipo_bala2 == 3:
                Datos.cantidad_balas2 = tanque2.cantBala60mm

            # Representacion gráfica de los Datos
            Pantalla.pantalla.muestra_salud(screen, fuente,tanque1.vida, tanque2.vida)
            Pantalla.pantalla.muestra_potencia(screen, fuente,Datos.velocidad_jugador1,Datos.velocidad_jugador2)
            Pantalla.pantalla.muestra_angulo(screen, fuente,Datos.ang_tank[Datos.angulo_jugador1-30],Datos.ang_tank[Datos.angulo_jugador2-30])    
            Pantalla.pantalla.muestra_texto(screen, fuente ,Datos.turno1,Datos.cantidad_balas1,Datos.cantidad_balas2)
            Pantalla.pantalla.muestra_imagen(screen, Datos.tipo_bala1, Datos.tipo_bala2, tanque1.x, tanque1.y, tanque2.x, tanque2.y)
            Pantalla.pantalla.muestra_altura(screen, fuente, Datos.altura_maxima, Datos.mostrar_altura1, Datos.mostrar_altura2)
            Pantalla.pantalla.muestra_distancia(screen, fuente, Datos.distancia_maxima, Datos.mostrar_altura1, Datos.mostrar_altura2)
            if Datos.bala_tanque1 is not None and Datos.bala_tanque1.visualizar():
                Pantalla.pantalla.muestra_bala(screen, Datos.tipo_bala1, Datos.bala_tanque1.xactual())
            elif Datos.bala_tanque2 is not None and Datos.bala_tanque2.visualizar():
                Pantalla.pantalla.muestra_bala(screen, Datos.tipo_bala2, Datos.bala_tanque2.xactual())

            Datos.extremo_canonx_1, Datos.extremo_canony_1 = Pantalla.pantalla.prerotate(screen, 1, -(Datos.ang_tank[Datos.angulo_jugador1]-90), tanque1.pivote)
            Datos.extremo_canonx_2, Datos.extremo_canony_2 = Pantalla.pantalla.prerotate(screen, 2, -(Datos.ang_tank[Datos.angulo_jugador2]-90), tanque2.pivote)
            pygame.display.flip()
            if salirJuego:
                break