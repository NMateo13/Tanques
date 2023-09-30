import pygame, sys, Terreno, Pantalla
from Bala import Bala
from Tanque import Tanque
from Terreno import Terreno
from Canon import Canon

pygame.init()
pygame.display.set_caption("Juego de Tanques") 
pygame.display.set_icon(Pantalla.pantalla.IMG_Explosion) 

font = pygame.font.Font(None, 36)
size = (Pantalla.pantalla.ancho, Pantalla.pantalla.alto)
screen = pygame.display.set_mode(size)
FPS = 60
terreno = Terreno(Pantalla.pantalla.ancho, Pantalla.pantalla.alto)

# Crear dos hitboxes
tank1 = Pantalla.pantalla.tank1
tank2 = Pantalla.pantalla.tank2
tanque1 = Tanque(Pantalla.pantalla.posX_Tanque1, Pantalla.pantalla.posY_Tanque1 + 10, Pantalla.pantalla.RED, tank1)
tanque2 = Tanque(Pantalla.pantalla.ancho - Pantalla.pantalla.Tanque2.get_width() - Pantalla.pantalla.posX_Tanque2, Pantalla.pantalla.posY_Tanque2 + 10, Pantalla.pantalla.RED, tank2)

bala_tanque1 = None
bala_tanque2 = None
#arraylist hasta 150
ang_tank = [210,215,220,225,230,235,240,245,250,255,260,265,270,275,280,285,290,295,300,305,310,315,320,325,330,335,340,345,350,355,0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100,105,110,115,120,125,130,135,140,145,150,155,160,165,170,175,180]
#0 = 30
#61 en total
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
pivote2 = [Pantalla.pantalla.ancho - Pantalla.pantalla.IMG_Canon2.get_width() - Pantalla.pantalla.posX_Tanque2 - 15, Pantalla.pantalla.posY_Tanque2+5]
        
angulo_jugador1 = 30 # Ángulo inicial
extremo_canonx_1, extremo_canony_1 = Pantalla.pantalla.prerotate(screen, 1, ang_tank[angulo_jugador1], pivote1)
velocidad_jugador1 = 50  # Velocidad inicial

angulo_jugador2 = 30  # Ángulo inicial
extremo_canonx_1, extremo_canony_1 =Pantalla.pantalla.prerotate(screen, 2, ang_tank[angulo_jugador2]-90, pivote2)
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
            if turno1:
                if event.key == pygame.K_w:
                    if angulo_jugador1  == 66:
                        angulo_jugador1 = 0
                    else:
                        angulo_jugador1 += 1
                elif event.key == pygame.K_s:
                    if angulo_jugador1 == 0:
                        angulo_jugador1 = 66
                    else:
                        angulo_jugador1 -= 1
                elif event.key == pygame.K_a:
                    velocidad_jugador1 -= 5
                    velocidad_jugador1 = max(0, velocidad_jugador1)
                elif event.key == pygame.K_d:
                    velocidad_jugador1 += 5
                    velocidad_jugador1 = min(150, velocidad_jugador1)
                #cambio de bala J1
                elif event.key == pygame.K_1:
                    tipo_bala1 = 1
                elif event.key == pygame.K_2:
                    tipo_bala1 = 2
                elif event.key == pygame.K_3:
                    tipo_bala1 = 3

            #Controles jugador 2 
            if turno2:   
                if event.key == pygame.K_UP:
                    if angulo_jugador2 == 66:
                        angulo_jugador2 = 0
                    else:
                        angulo_jugador2 += 1
                elif event.key == pygame.K_DOWN:
                    if angulo_jugador2 == 0:
                        angulo_jugador2 = 66
                    else:
                        angulo_jugador2 -= 1
                elif event.key == pygame.K_LEFT:
                    velocidad_jugador2 -= 5
                    velocidad_jugador2 = max(0, velocidad_jugador2)
                elif event.key == pygame.K_RIGHT:
                    velocidad_jugador2 += 5
                    velocidad_jugador2 = min(150, velocidad_jugador2)
                #cambio de bala J2
                elif event.key == pygame.K_1:
                    tipo_bala2 = 1
                elif event.key == pygame.K_2:
                    tipo_bala2 = 2
                elif event.key == pygame.K_3:
                    tipo_bala2 = 3

    screen.fill(Pantalla.pantalla.WHITE)
    screen.blit(Pantalla.pantalla.Background, (0, 0))
    terreno.dibujar(screen)
    screen.blit(Pantalla.pantalla.HUD, (0, 540))
    tanque1.dibujar(screen)
    tanque2.dibujar(screen)

    if tecla_espacio_presionada and turno1:
        if bala_tanque1 is None:
            mostrar_altura1 = True
            mostrar_altura2 = False
            altura_maxima = 0
            bala_tanque1 = tanque1.disparar(extremo_canonx_1, extremo_canony_1, ang_tank[angulo_jugador1], velocidad_jugador1, tiempo_transcurrido, screen, Pantalla.pantalla.BLACK, tipo_bala1)
        else:
            altura_maxima = bala_tanque1.punto_maximo(altura_maxima)
            bala_tanque1.verificacion(tiempo_transcurrido, screen, Pantalla.pantalla.BLACK)
            impacto_tanque = bala_tanque1.verificar_impacto_tanque(tanque2)
            impacto_terreno = terreno.verificar_colision(bala_tanque1)
            impacto_borde = bala_tanque1.verificar_impacto_ancho(Pantalla.pantalla.ancho)
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
            bala_tanque2 = tanque1.disparar(extremo_canonx_2, extremo_canony_2, ang_tank[angulo_jugador2], velocidad_jugador2, tiempo_transcurrido, screen, Pantalla.pantalla.BLACK, tipo_bala2)
        else:
            altura_maxima = bala_tanque2.punto_maximo(altura_maxima)
            bala_tanque2.verificacion(tiempo_transcurrido, screen, Pantalla.pantalla.BLACK)
            impacto_tanque = bala_tanque2.verificar_impacto_tanque(tanque1)
            impacto_terreno = terreno.verificar_colision(bala_tanque2)
            impacto_borde = bala_tanque2.verificar_impacto_ancho(Pantalla.pantalla.ancho)
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
    Pantalla.pantalla.muestra_angulo(screen, font,ang_tank[angulo_jugador1-30],ang_tank[angulo_jugador2-30])
    Pantalla.pantalla.muestra_texto(screen, font)
    Pantalla.pantalla.muestra_imagen(screen, tipo_bala1, tipo_bala2)
    Pantalla.pantalla.muestra_altura(screen, font, altura_maxima, mostrar_altura1, mostrar_altura2)
    extremo_canonx_1, extremo_canony_1 = Pantalla.pantalla.prerotate(screen, 1, -(ang_tank[angulo_jugador1]-90), pivote1)
    extremo_canonx_2, extremo_canony_2 = Pantalla.pantalla.prerotate(screen, 2, -(ang_tank[angulo_jugador2]-90), pivote2)
    pygame.display.flip()
