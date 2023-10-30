import pygame, datos, os, random, imagenes


class Pantalla:
    offset = pygame.math.Vector2(0, -10)

    #Seleccion aleatoria de los tanques
    tank1 = random.randint(1, 4)
    tank2 = random.randint(1, 4)
    while tank1 == tank2:
        tank2 = random.randint(1, 4)

    #Imagenes
    if tank1 == 1:
        imagenes.IMG_Tanque1
    elif tank1 == 2:
        imagenes.IMG_Tanque2
    elif tank1 == 3:
        imagenes.IMG_Tanque3
    elif tank1 == 4:
        imagenes.IMG_Tanque4

    if tank2 == 1:
        imagenes.IMG_Tanque1
    elif tank2 == 2:
        imagenes.IMG_Tanque2
    elif tank2 == 3:
        imagenes.IMG_Tanque3
    elif tank2 == 4:
        imagenes.IMG_Tanque4

    if tank1 == 1:
        imagenes.IMG_Canon1
    elif tank1 == 2:
        imagenes.IMG_Canon2
    elif tank1 == 3:
        imagenes.IMG_Canon3
    elif tank1 == 4:
        imagenes.IMG_Canon4

    if tank2 == 1:
        imagenes.IMG_Canon1
    elif tank2 == 2:
        imagenes.IMG_Canon2
    elif tank2 == 3:
        imagenes.IMG_Canon3
    elif tank2 == 4:
        imagenes.IMG_Canon4
        
    def __init__(self, ancho, alto):
        
        self.ancho = ancho
        self.alto = alto

    def crearMatriz(self, alto, ancho):

        Pantalla.matriz = [[0] * ancho for _ in range(alto - datos.medidaHUD)]

    def dibujar(self, screen):
        
        for filas in range(0, (datos.PANT_ALTO - datos.medidaHUD)):
            for columnas in range (0, pantalla.ancho):
                if pantalla.matriz[filas][columnas] == 1:
                    pygame.draw.rect(screen, pantalla.GREEN, (columnas, filas, 6, 6))
    
    #Funciones para mostrar información en la pantalla
    def muestra_texto(self, screen, font, turno,balas1, balas2):
        balas1_texo = str(balas1)
        balas2_texo = str(balas2)

        jugador_texto1 = font.render("Jugador 1", True, datos.WHITE)
        screen.blit(jugador_texto1, (460, datos.PANT_ALTO - 110))

        jugador_texto2 = font.render("Jugador 2", True, datos.WHITE)
        screen.blit(jugador_texto2, (pantalla.ancho - jugador_texto2.get_width() - 460, datos.PANT_ALTO - 110))

        stats = font.render("STATS", True, datos.RED)
        screen.blit(stats, (300, datos.PANT_ALTO - 110))
        screen.blit(stats, (pantalla.ancho - stats.get_width() - 300, datos.PANT_ALTO - 110))

        bala = font.render("TIPO DE BALA", True, datos.RED)
        screen.blit(bala, (25, datos.PANT_ALTO - 110))
        screen.blit(bala, (pantalla.ancho - bala.get_width() - 25, datos.PANT_ALTO - 110))
        #tanque 1
        cant_balas = font.render(balas1_texo, True, datos.WHITE)
        screen.blit(cant_balas, (pantalla.ancho - cant_balas.get_width() - 1080, datos.PANT_ALTO - 30))

        #tanque 2
        cant_balas = font.render(balas2_texo, True, datos.WHITE)
        screen.blit(cant_balas, (pantalla.ancho - cant_balas.get_width() - 110 , datos.PANT_ALTO - 30))
        
        #Indica el turno del jugador
        if turno:
            turno_texto = font.render("J1", True, datos.WHITE)
        else:
            turno_texto = font.render("J2", True, datos.WHITE)
        
        screen.blit(turno_texto, (pantalla.ancho // 2 - turno_texto.get_width() // 2, datos.PANT_ALTO - 140))
        nTurno_texto = font.render(f"Turno: {datos.nTurnos}", True, datos.WHITE)
        screen.blit(nTurno_texto, (pantalla.ancho // 2 - nTurno_texto.get_width() // 2, datos.PANT_ALTO - 170))

    def muestra_salud(self, screen, font, vida_tanque1, vida_tanque2): #falta agregar las variables de vida de los tanques
        salud_texto1 = font.render(f"Vida: {vida_tanque1}%", True, datos.WHITE)
        screen.blit(salud_texto1, (250, datos.PANT_ALTO - 85))

        salud_texto2 = font.render(f"Vida: {vida_tanque2}%", True, datos.WHITE) 
        screen.blit(salud_texto2, (pantalla.ancho - salud_texto2.get_width() - 300, datos.PANT_ALTO - 85))

    def muestra_potencia(self, screen, font,velocidad_jugador1, velocidad_jugador2): 
        potencia_texto1 = font.render(f"Potencia: {velocidad_jugador1}", True, datos.WHITE)
        screen.blit(potencia_texto1, (250, datos.PANT_ALTO - 57))

        potencia_texto2 = font.render(f"Potencia: {velocidad_jugador2}", True, datos.WHITE)
        screen.blit(potencia_texto2, (pantalla.ancho - potencia_texto2.get_width() - 280, datos.PANT_ALTO - 57))

    def muestra_angulo(self, screen, font,angulo_jugador1, angulo_jugador2): 
        angulo_texto1 = font.render(f"Ángulo: {angulo_jugador1}°", True, datos.WHITE)
        screen.blit(angulo_texto1, (250, datos.PANT_ALTO - 30))

        angulo_texto2 = font.render(f"Ángulo: {angulo_jugador2}°", True, datos.WHITE)
        screen.blit(angulo_texto2, (pantalla.ancho - angulo_texto2.get_width() - 280, datos.PANT_ALTO - 30))

    def muestra_imagen(self, screen, tipo1, tipo2, posX1, posX2, posY1, posY2):
        screen.blit(imagenes.Tanque1, (posX1 - 10, posY1)) 
        screen.blit(imagenes.Tanque2, (pantalla.ancho - imagenes.Tanque2.get_width() - posX2+20, posY2)) 
        screen.blit(imagenes.Exit, (pantalla.ancho - imagenes.Exit.get_width() - 650, 10))
        screen.blit(imagenes.Restart, (pantalla.ancho - imagenes.Restart.get_width() - 550, 10))

        #NO TOCAR SON ESTÁTICOS 

        screen.blit(imagenes.Tanque1_HUD, (450, 525)) 
        screen.blit(imagenes.Tanque2_HUD, (pantalla.ancho - imagenes.Tanque2_HUD.get_width() - 450, 525)) 
        if tipo1 == 1:
            #cambiar imagen a bala 105mm
            screen.blit(imagenes.Bala105, (50, datos.PANT_ALTO - 75))
        elif tipo1 == 2:
            #cambiar imagen a bala 80mm
            screen.blit(imagenes.Bala80, (60, datos.PANT_ALTO - 75))
        elif tipo1 == 3:
            #cambiar imagen a bala 60mm
            screen.blit(imagenes.Bala60, (70, datos.PANT_ALTO - 75))
        
        if tipo2 == 1:
            #cambiar imagen a bala 105mm
            screen.blit(imagenes.Bala105, (pantalla.ancho - imagenes.Bala105.get_width() - 50, datos.PANT_ALTO - 75))
        elif tipo2 == 2:
            #cambiar imagen a bala 80mm
            screen.blit(imagenes.Bala80, (pantalla.ancho - imagenes.Bala80.get_width() - 60, datos.PANT_ALTO - 75))
        elif tipo2 == 3:
            #cambiar imagen a bala 60mm
            screen.blit(imagenes.Bala60, (pantalla.ancho - imagenes.Bala60.get_width() - 70, datos.PANT_ALTO - 75))

        #NO TOCAR SON ESTÁTICOS

    #ahora se iniciará una función para calcular la altura maxima de la bala y la distancia recorrida por la bala y se mostrará en pantalla
    def muestra_altura(self, screen, font, altura_maxima, mostrar1, mostrar2):
        if mostrar1:
            altura_texto1 = font.render(f"Altura máxima J1: {altura_maxima}", True, datos.WHITE)
            screen.blit(altura_texto1, (10, datos.PANT_ALTO - 180))
        elif mostrar2:
            altura_texto2 = font.render(f"Altura máxima J2: {altura_maxima}", True, datos.WHITE)
            screen.blit(altura_texto2, (10, datos.PANT_ALTO - 180))

    def prerotate(self, screen, num, angle, pivote):
        if num==1:
            img, rect, x, y = Pantalla.rotate(imagenes.Canon1, angle, pivote)
        elif num==2:
            img, rect, x, y = Pantalla.rotate(imagenes.Canon2, angle, pivote)
        screen.blit(img, rect)
        return x, y
    
    def rotate(surface, angle, pivot):
        rotated_image = pygame.transform.rotozoom(surface, -angle, 1)
        # Rota el vector de desplazamiento
        rotated_offset = Pantalla.offset.rotate(angle)
        # Agrega el vector de desplazamiento al punto pivote para desplazar el rectangulo.
        rect = rotated_image.get_rect(center=pivot+rotated_offset)
        # Devuelve la imagen rotada y el rectangulo desplazado
        x = rect.x
        y = rect.y
        return rotated_image, rect, x, y
    
    def prueba(self, surface, x, y):
        pygame.draw.circle(surface, datos.BLACK, (x, y), 2)

    def muestra_distancia(self, screen, font, distancia_maxima, mostrar1, mostrar2):
        if mostrar1:
            distancia_texto1 = font.render(f"Distancia máxima J1: {distancia_maxima}", True, datos.WHITE)
            screen.blit(distancia_texto1, (10, datos.PANT_ALTO - 150))
        elif mostrar2:
            distancia_texto2 = font.render(f"Distancia máxima J2: {distancia_maxima}", True, datos.WHITE)
            screen.blit(distancia_texto2, (10, datos.PANT_ALTO - 150))

    def muestra_bala(self, screen, tipo_bala, pos_x):
        if tipo_bala == 1:
            screen.blit(imagenes.Prebala105, (pos_x, 0))
        elif tipo_bala == 2:
            screen.blit(imagenes.Prebala80, (pos_x, 0))
        elif tipo_bala == 3:
            screen.blit(imagenes.Prebala60, (pos_x, 0))

pantalla = Pantalla(datos.PANT_ANCHO, datos.PANT_ALTO)
matriz = []