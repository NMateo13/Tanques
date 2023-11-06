import pygame, sys, Terreno, Pantalla, datos, imagenes, random, math
from Bala import Bala
from Tanque import Tanque
from Terreno import Terreno
from Canon import Canon

def draw_text(text, font, x, y, color, screen):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    screen.blit(textobj, textrect)
    
def opciones(screen):
    while True:
        salir = False

        boton_800 = pygame.Rect((datos.PANT_ANCHO / 2) - 450, (datos.PANT_ALTO / 2) - 140, 100, 50)
        boton_default = pygame.Rect((datos.PANT_ANCHO / 2) - 450, (datos.PANT_ALTO / 2) - 80, 100, 50)
        boton_1080 = pygame.Rect((datos.PANT_ANCHO / 2) - 450, (datos.PANT_ALTO / 2) - 20, 100, 50)
        boton_aplicar = pygame.Rect((datos.PANT_ANCHO / 2) - 450, (datos.PANT_ALTO / 2) + 40, 100, 50)
    
        screen.fill(datos.WHITE)
        screen.blit(imagenes.FondoControles, (0, 0))
        fuente = pygame.font.Font(None, 36)
        draw_text('Opciones', fuente, (datos.PANT_ANCHO / 2) - 58, (datos.PANT_ALTO / 2) - 250, datos.BLACK, screen)
        draw_text('Resolucion', fuente, (datos.PANT_ANCHO / 2) - 418, (datos.PANT_ALTO / 2) - 200, datos.BLACK, screen)
        draw_text('Controles', fuente, (datos.PANT_ANCHO / 2) + 303, (datos.PANT_ALTO / 2) - 200, datos.BLACK, screen)
        fuente = pygame.font.Font(None, 23)
        draw_text('800x800', fuente, (datos.PANT_ANCHO / 2) - 438, (datos.PANT_ALTO / 2) - 137, datos.BLACK, screen)
        fuente = pygame.font.Font(None, 21)
        draw_text('W | Arriba: Más ángulo', fuente, (datos.PANT_ANCHO / 2) + 277, (datos.PANT_ALTO / 2) - 137, datos.BLACK, screen)
        fuente = pygame.font.Font(None, 23)
        draw_text('Default', fuente, (datos.PANT_ANCHO / 2) - 436, (datos.PANT_ALTO / 2) - 78, datos.BLACK, screen)
        fuente = pygame.font.Font(None, 21)
        draw_text('S | Abajo: Menos ángulo', fuente, (datos.PANT_ANCHO / 2) + 278, (datos.PANT_ALTO / 2) - 78, datos.BLACK, screen)
        fuente = pygame.font.Font(None, 23)
        draw_text('1920x1080', fuente, (datos.PANT_ANCHO / 2) - 442, (datos.PANT_ALTO / 2) - 19, datos.BLACK, screen)
        fuente = pygame.font.Font(None, 17)
        draw_text('A | Izquierda: Menos potencia', fuente, (datos.PANT_ANCHO / 2) + 280, (datos.PANT_ALTO / 2) - 17, datos.BLACK, screen)
        fuente = pygame.font.Font(None, 23)
        draw_text('Aplicar Resolución', fuente, (datos.PANT_ANCHO / 2) - 443, (datos.PANT_ALTO / 2) + 39, datos.BLACK, screen)
        fuente = pygame.font.Font(None, 17)
        draw_text('D | Derecha: Más potencia', fuente, (datos.PANT_ANCHO / 2) + 283, (datos.PANT_ALTO / 2) + 41, datos.BLACK, screen)
        fuente = pygame.font.Font(None, 26)
        draw_text('1: Bala 105mm', fuente, (datos.PANT_ANCHO / 2) - 425, (datos.PANT_ALTO / 2) + 116, datos.BLACK, screen)
        fuente = pygame.font.Font(None, 26)
        draw_text('2: Bala 80mm', fuente, (datos.PANT_ANCHO / 2) - 57, (datos.PANT_ALTO / 2) + 116, datos.BLACK, screen)
        fuente = pygame.font.Font(None, 26)
        draw_text('3: Bala 60mm', fuente, (datos.PANT_ANCHO / 2) + 307, (datos.PANT_ALTO / 2) + 116, datos.BLACK, screen)
        draw_text('Espacio: Disparar', fuente, (datos.PANT_ANCHO / 2) - 75, (datos.PANT_ALTO / 2) + 42, datos.BLACK, screen)
        fuente = pygame.font.Font(None, 26)
        draw_text('Menu: Escape', fuente, (datos.PANT_ANCHO / 2) - 59, (datos.PANT_ALTO / 2) + 191, datos.BLACK, screen)

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
                    datos.PANT_ANCHO = 800
                    datos.PANT_ALTO = 800
                    pygame.display.set_mode((datos.PANT_ANCHO, datos.PANT_ALTO))
                if boton_default.collidepoint(event.pos):
                    datos.PANT_ANCHO = 1200
                    datos.PANT_ALTO = 600
                    pygame.display.set_mode((datos.PANT_ANCHO, datos.PANT_ALTO))
                if boton_1080.collidepoint(event.pos):
                    datos.PANT_ANCHO = 1920
                    datos.PANT_ALTO = 1080
                    pygame.display.set_mode((datos.PANT_ANCHO, datos.PANT_ALTO))
                if boton_aplicar.collidepoint(event.pos):
                    pygame.display.update()
                    salir = True      

        if salir:
            break


def muestra_ganador(Ganador, screen, fuente): #Función para mostrar el ganador del juego
    screen.fill(datos.WHITE) 
    texto_ganador = fuente.render(f"Ganador: Jugador {Ganador}", True, datos.BLACK) 
    screen.blit(texto_ganador, (datos.PANT_ANCHO / 2 - texto_ganador.get_width() / 2, datos.PANT_ALTO / 2 - texto_ganador.get_height() / 2)) 
    pygame.display.flip() 
    pygame.time.delay(3000) 
    sys.exit() 

def juego(screen, fuente):
    salirJuego = False
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

    centroExplosion = []
    radioExplosion = 75
    arrayaux = []
    arrayaux2 = []

    aux_x=0
    aux_y=0

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

    Clock = pygame.time.Clock()
    tecla_espacio_presionada = False

    pivote1 = [posX_Tanque1 + 10, posY_Tanque1+5]
    pivote2 = [datos.PANT_ANCHO - imagenes.IMG_Canon2.get_width() - posX_Tanque2 + 5, posY_Tanque2+5]
            
    angulo_jugador1 = 30 # Ángulo inicial
    extremo_canonx_1, extremo_canony_1 = Pantalla.pantalla.prerotate(screen, 1, datos.ang_tank[angulo_jugador1], pivote1)
    velocidad_jugador1 = 50  # Velocidad inicial

    angulo_jugador2 = 30  # Ángulo inicial
    extremo_canonx_1, extremo_canony_1 =Pantalla.pantalla.prerotate(screen, 2, datos.ang_tank[angulo_jugador2]-90, pivote2)
    velocidad_jugador2 = 50  # Velocidad inicial

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
                    salirJuego = True
                    datos.reiniciar = True  # Reiniciar el juego
                if salir.collidepoint(pygame.mouse.get_pos()):
                    salirJuego = True  # Volver al menú principal
        
        keys = pygame.key.get_pressed()

        if keys[pygame.K_ESCAPE]:
            salirJuego = True
        
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
                radioExplosion = 75
            elif keys[pygame.K_2]:
                tipo_bala1 = 2
                radioExplosion = 50
            elif keys[pygame.K_3]:
                tipo_bala1 = 3
                radioExplosion = 25

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
                radioExplosion = 75
            elif keys[pygame.K_2]:
                tipo_bala2 = 2
                radioExplosion = 50
            elif keys[pygame.K_3]:
                tipo_bala2 = 3
                radioExplosion = 25

        screen.blit(imagenes.Background, (0, 0))
        terreno.dibujar(screen)
        screen.blit(imagenes.HUD, (0, datos.PANT_ALTO - 120))
        tanque1.dibujar(screen)
        tanque2.dibujar(screen)

        if tanque1.vida <= 0: # Si la vida del tanque 1 es menor o igual a 0, el ganador es el tanque 2
            Ganador = 2
            muestra_ganador(Ganador, screen, fuente)

        if tanque2.vida <= 0: # Si la vida del tanque 2 es menor o igual a 0, el ganador es el tanque 1
            Ganador = 1
            muestra_ganador(Ganador, screen, fuente)

        if tecla_espacio_presionada and turno1:
            if bala_tanque1 is None:
                mostrar_altura1 = True
                mostrar_altura2 = False
                if tipo_bala1 == 1 and tanque1.cantBala105mm == 0:
                    print("No quedan balas")
                    tecla_espacio_presionada = False
                    tiempo_transcurrido = 0
                elif tipo_bala1 == 2 and tanque1.cantBala80mm == 0:
                    print("No quedan balas")
                    tecla_espacio_presionada = False
                    tiempo_transcurrido = 0
                elif tipo_bala1 == 3 and tanque1.cantBala60mm == 0:
                    print("No quedan balas")
                    tecla_espacio_presionada = False
                    tiempo_transcurrido = 0
                else:
                    bala_tanque1 = tanque1.disparar(extremo_canonx_1, extremo_canony_1, datos.ang_tank[angulo_jugador1], velocidad_jugador1, tiempo_transcurrido, screen, datos.BLACK, tipo_bala1)
            else:
                datos.altura_maxima = bala_tanque1.punto_maximo(datos.altura_maxima)
                datos.distancia_maxima = bala_tanque1.distancia_maxima(tanque1.x, datos.distancia_maxima)
                bala_tanque1.verificacion(tiempo_transcurrido, screen, datos.BLACK)
                impacto_tanque = bala_tanque1.verificar_impacto_tanque(tanque2)
                impacto_tanque_igual = bala_tanque1.verificar_impacto_tanque(tanque1)
                impacto_terreno = terreno.verificar_colision(bala_tanque1)
                impacto_borde = bala_tanque1.verificar_impacto_ancho(datos.PANT_ANCHO)
                        
                if impacto_tanque:
                    if tipo_bala1 == 1:
                        tanque2.vida -= tanque1.Bala105mm
                        bala_tanque1 = None
                        tecla_espacio_presionada = False
                        turno1 = False
                        turno2 = True
                        tiempo_transcurrido = 0
                    
                    elif tipo_bala1 == 2:
                        tanque2.vida -= tanque1.Bala80mm
                        bala_tanque1 = None
                        tecla_espacio_presionada = False
                        turno1 = False
                        turno2 = True
                        tiempo_transcurrido = 0

                    elif tipo_bala1 == 3:
                        tanque2.vida -= tanque1.Bala60mm
                        bala_tanque1 = None
                        tecla_espacio_presionada = False
                        turno1 = False
                        turno2 = True
                        tiempo_transcurrido = 0
                elif impacto_tanque_igual:
                    if tipo_bala1 == 1:
                        tanque1.vida -= tanque1.Bala105mm
                        bala_tanque1 = None
                        tecla_espacio_presionada = False
                        turno1 = False
                        turno2 = True
                        tiempo_transcurrido = 0
                    
                    elif tipo_bala1 == 2:
                        tanque1.vida -= tanque1.Bala80mm
                        bala_tanque1 = None
                        tecla_espacio_presionada = False
                        turno1 = False
                        turno2 = True
                        tiempo_transcurrido = 0

                    elif tipo_bala1 == 3:
                        tanque1.vida -= tanque1.Bala60mm
                        bala_tanque1 = None
                        tecla_espacio_presionada = False
                        turno1 = False
                        turno2 = True
                        tiempo_transcurrido = 0
                elif impacto_borde:
                        bala_tanque1 = None
                        tecla_espacio_presionada = False
                        turno1 = False
                        turno2 = True
                        tiempo_transcurrido = 0

                elif impacto_terreno:
                    for x, y in bala_tanque1.trayectoria:
                        centroExplosion.append(int(x))
                        centroExplosion.append(int(y))
                        for i in range(radioExplosion):
                            ancho= []
                            ancho.append(int(x)-radioExplosion+i)
                    Pantalla.pantalla.prueba(screen, centroExplosion[0], centroExplosion[1])
                    pygame.display.flip()
                    bala_tanque1 = None
                    tecla_espacio_presionada = False
                    turno1 = False
                    turno2 = True
                    tiempo_transcurrido = 0
                    #calculamos los puntos de la circunferencia de la explosion
                    num_puntosExplosion = int(2 * math.pi * radioExplosion)
                    puntosExplosionX = []
                    puntosExplosionY = []
                    for i in range(num_puntosExplosion):
                        angle = (2 * math.pi / num_puntosExplosion) * i
                        x = int(centroExplosion[0] + radioExplosion * math.cos(angle))
                        y = int(centroExplosion[1] + radioExplosion * math.sin(angle))
                        puntosExplosionX.append(x)
                        puntosExplosionY.append(y)
                    #verificamos cada punto x de la circunferencia y verificamos el punto y mas bajo de la circunferencia
                    for i in range(len(puntosExplosionX)):
                        pygame.draw.circle(screen, datos.BLACK, (puntosExplosionX[i], puntosExplosionY[i]), 1)
                    pygame.display.flip()
                    conjuntoPuntos = set(puntosExplosionX)
                    arrayaux = list(conjuntoPuntos)
                    arrayaux.sort()
                    bandera = 0
                    valory = 0
                    for i in range(len(arrayaux)):
                        valory = 0
                        for j in range(len(puntosExplosionX)):
                            if arrayaux[i] == puntosExplosionX[j]:
                                if bandera == 0:
                                    valory = puntosExplosionY[j]
                                    bandera+=1
                                else:
                                    if puntosExplosionY[j] > valory:
                                        valory = puntosExplosionY[j]
                        valory = datos.PANT_ALTO - valory
                        if arrayaux[i] < 1200 and arrayaux[i] > 0:
                            if terreno.terreno[arrayaux[i]] > valory:
                                terreno.terreno[arrayaux[i]] = valory
                    centroExplosion.clear()
                    puntosExplosionX.clear()
                    puntosExplosionY.clear()
                    arrayaux.clear()
                    conjuntoPuntos.clear()

            tiempo_transcurrido += incremento

        if tecla_espacio_presionada and turno2:
            if bala_tanque2 is None:
                mostrar_altura1 = False
                mostrar_altura2 = True
                if tipo_bala2 == 1 and tanque2.cantBala105mm == 0:
                    print("No quedan balas")
                    tecla_espacio_presionada = False
                    tiempo_transcurrido = 0
                elif tipo_bala2 == 2 and tanque2.cantBala80mm == 0:
                    print("No quedan balas")
                    tecla_espacio_presionada = False
                    tiempo_transcurrido = 0
                elif tipo_bala2 == 3 and tanque2.cantBala60mm == 0:
                    print("No quedan balas")
                    tecla_espacio_presionada = False
                    tiempo_transcurrido = 0
                else:
                    bala_tanque2 = tanque2.disparar(extremo_canonx_2, extremo_canony_2, datos.ang_tank[angulo_jugador2], velocidad_jugador2, tiempo_transcurrido, screen, datos.BLACK, tipo_bala2)
            else:
                datos.altura_maxima = bala_tanque2.punto_maximo(datos.altura_maxima)
                datos.distancia_maxima = bala_tanque2.distancia_maxima(tanque2.x, datos.distancia_maxima)
                bala_tanque2.verificacion(tiempo_transcurrido, screen, datos.BLACK)
                impacto_tanque = bala_tanque2.verificar_impacto_tanque(tanque1)
                impacto_tanque_igual = bala_tanque2.verificar_impacto_tanque(tanque2)
                impacto_terreno = terreno.verificar_colision(bala_tanque2)
                impacto_borde = bala_tanque2.verificar_impacto_ancho(datos.PANT_ANCHO)
                if impacto_tanque:
                    if tipo_bala2 == 1:
                        tanque1.vida -= tanque2.Bala105mm
                        bala_tanque2 = None
                        tecla_espacio_presionada = False
                        turno2 = False
                        turno1 = True
                        tiempo_transcurrido = 0
                    
                    elif tipo_bala2 == 2:
                        tanque1.vida -= tanque2.Bala80mm
                        bala_tanque2 = None
                        tecla_espacio_presionada = False
                        turno2 = False
                        turno1 = True
                        tiempo_transcurrido = 0

                    elif tipo_bala2 == 3:
                        tanque1.vida -= tanque2.Bala60mm
                        bala_tanque2 = None
                        tecla_espacio_presionada = False
                        turno2 = False
                        turno1 = True
                        tiempo_transcurrido = 0
                elif impacto_tanque_igual:
                    if tipo_bala2 == 1:
                        tanque2.vida -= tanque2.Bala105mm
                        datos.nTurnos += 1
                        bala_tanque2 = None
                        tecla_espacio_presionada = False
                        turno2 = False
                        turno1 = True
                        tiempo_transcurrido = 0
                    
                    elif tipo_bala2 == 2:
                        tanque2.vida -= tanque2.Bala80mm
                        bala_tanque2 = None
                        tecla_espacio_presionada = False
                        turno2 = False
                        turno1 = True
                        tiempo_transcurrido = 0

                    elif tipo_bala2 == 3:
                        tanque2.vida -= tanque2.Bala60mm
                        bala_tanque2 = None
                        tecla_espacio_presionada = False
                        turno2 = False
                        turno1 = True
                        tiempo_transcurrido = 0
                elif impacto_borde:
                    bala_tanque2 = None
                    tecla_espacio_presionada = False
                    turno2 = False
                    turno1 = True
                    tiempo_transcurrido = 0

                elif impacto_terreno:
                    for x, y in bala_tanque2.trayectoria:
                        centroExplosion.append(int(x))
                        centroExplosion.append(int(y))
                    bala_tanque2 = None
                    tecla_espacio_presionada = False
                    turno2 = False
                    turno1 = True
                    tiempo_transcurrido = 0
                    #calculamos los puntos de la circunferencia de la explosion
                    num_puntosExplosion = int(2 * math.pi * radioExplosion)
                    puntosExplosionX = []
                    puntosExplosionY = []
                    for i in range(num_puntosExplosion):
                        angle = (2 * math.pi / num_puntosExplosion) * i
                        x = int(centroExplosion[0] + radioExplosion * math.cos(angle))
                        y = int(centroExplosion[1] + radioExplosion * math.sin(angle))
                        puntosExplosionX.append(x)
                        puntosExplosionY.append(y)
                    #verificamos cada punto x de la circunferencia y verificamos el punto y mas bajo de la circunferencia
                    for i in range(len(puntosExplosionX)):
                        pygame.draw.circle(screen, datos.BLACK, (puntosExplosionX[i], puntosExplosionY[i]), 1)
                    pygame.display.flip()
                    conjuntoPuntos = set(puntosExplosionX)
                    arrayaux = list(conjuntoPuntos)
                    arrayaux.sort()
                    bandera = 0
                    valory = 0
                    for i in range(len(arrayaux)):
                        valory = 0
                        for j in range(len(puntosExplosionX)):
                            if arrayaux[i] == puntosExplosionX[j]:
                                if bandera == 0:
                                    valory = puntosExplosionY[j]
                                    bandera+=1
                                else:
                                    if puntosExplosionY[j] > valory:
                                        valory = puntosExplosionY[j]
                        valory = datos.PANT_ALTO - valory
                        if arrayaux[i] < 1200 and arrayaux[i] > 0:
                            if terreno.terreno[arrayaux[i]] > valory:
                                terreno.terreno[arrayaux[i]] = valory
                    centroExplosion.clear()
                    puntosExplosionX.clear()
                    puntosExplosionY.clear()
                    arrayaux.clear()
                    conjuntoPuntos.clear()

                    
            tiempo_transcurrido += incremento
        if posY_Tanque1 != (terreno.alto - terreno.terreno[indice] - 26) or posY_Tanque2 != (600 -  terreno.terreno[indice2] - 24):
            
            posY_Tanque1 = terreno.alto - terreno.terreno[indice] - 26
            posY_Tanque2 = 600 -  terreno.terreno[indice2] - 24 

            tanque1.y = posY_Tanque1+10
            tanque2.y = posY_Tanque2+20

            pivote1 = [posX_Tanque1 + 10, posY_Tanque1]
            pivote2 = [datos.PANT_ANCHO - imagenes.IMG_Canon2.get_width() - posX_Tanque2 + 5, posY_Tanque2+5]

            extremo_canonx_1, extremo_canony_1 = Pantalla.pantalla.prerotate(screen, 1, datos.ang_tank[angulo_jugador1], pivote1)
            extremo_canonx_1, extremo_canony_1 =Pantalla.pantalla.prerotate(screen, 2, datos.ang_tank[angulo_jugador2]-90, pivote2)




        # Descuento de balas        
        if tipo_bala1 == 1:
            datos.cantidad_balas1 = tanque1.cantBala105mm
        elif tipo_bala1 == 2:
            datos.cantidad_balas1 = tanque1.cantBala80mm
        elif tipo_bala1 == 3:
            datos.cantidad_balas1 = tanque1.cantBala60mm
                    
        if tipo_bala2 == 1:
            datos.cantidad_balas2 = tanque2.cantBala105mm
        elif tipo_bala2 == 2:
            datos.cantidad_balas2 = tanque2.cantBala80mm
        elif tipo_bala2 == 3:
            datos.cantidad_balas2 = tanque2.cantBala60mm

        # Representacion gráfica de los datos
        Pantalla.pantalla.muestra_salud(screen, fuente,tanque1.vida, tanque2.vida)
        Pantalla.pantalla.muestra_potencia(screen, fuente,velocidad_jugador1,velocidad_jugador2)
        Pantalla.pantalla.muestra_angulo(screen, fuente,datos.ang_tank[angulo_jugador1-30],datos.ang_tank[angulo_jugador2-30])    
        Pantalla.pantalla.muestra_texto(screen, fuente ,turno1,datos.cantidad_balas1,datos.cantidad_balas2)
        Pantalla.pantalla.muestra_imagen(screen, tipo_bala1, tipo_bala2, posX_Tanque1, posX_Tanque2, posY_Tanque1, posY_Tanque2)
        Pantalla.pantalla.muestra_altura(screen, fuente, datos.altura_maxima, mostrar_altura1, mostrar_altura2)
        Pantalla.pantalla.muestra_distancia(screen, fuente, datos.distancia_maxima, mostrar_altura1, mostrar_altura2)
        if bala_tanque1 is not None and bala_tanque1.visualizar():
            Pantalla.pantalla.muestra_bala(screen, tipo_bala1, bala_tanque1.xactual())
        elif bala_tanque2 is not None and bala_tanque2.visualizar():
            Pantalla.pantalla.muestra_bala(screen, tipo_bala2, bala_tanque2.xactual())

        extremo_canonx_1, extremo_canony_1 = Pantalla.pantalla.prerotate(screen, 1, -(datos.ang_tank[angulo_jugador1]-90), pivote1)
        extremo_canonx_2, extremo_canony_2 = Pantalla.pantalla.prerotate(screen, 2, -(datos.ang_tank[angulo_jugador2]-90), pivote2)
        pygame.display.flip()
        if salirJuego:
            break