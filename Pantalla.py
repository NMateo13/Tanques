import pygame, Datos, os, random, Imagenes, sys

class Pantalla:
    offset = pygame.math.Vector2(0, -10)
        
    def __init__(self, ancho, alto):
        
        self.ancho = ancho
        self.alto = alto

    def dibujar(self, screen):
        
        for filas in range(0, (Datos.PANT_ALTO - Datos.medidaHUD)):
            for columnas in range (0, pantalla.ancho):
                if pantalla.matriz[filas][columnas] == 1:
                    pygame.draw.rect(screen, pantalla.GREEN, (columnas, filas, 6, 6))
    
    def draw_text(text, font, x, y, color, screen):
        textobj = font.render(text, 1, color)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        screen.blit(textobj, textrect)

    #Funciones para mostrar información en la pantalla
    def muestra_texto(self, screen, font, tanque, angulo): # Muestra textos en el juego
        if tanque.tipo_bala == 1:
            bala_texto = str(tanque.cantBala105mm)
        elif tanque.tipo_bala == 2:
            bala_texto = str(tanque.cantBala80mm)
        elif tanque.tipo_bala == 3:
            bala_texto = str(tanque.cantBala60mm)

        stats = font.render("STATS", True, Datos.RED)
        screen.blit(stats, (Datos.PANT_ANCHO / 2.9, Datos.PANT_ALTO - 110))

        bala = font.render("TIPO DE BALA", True, Datos.RED)
        screen.blit(bala, (25, Datos.PANT_ALTO - 110))
        
        cant_balas = font.render(bala_texto, True, Datos.WHITE)
        salud_texto = font.render(f"Vida: {tanque.vida}%", True, Datos.WHITE)
        #Funcion para dibujar el color del tanque que corresponda en el turno
        screen.blit(Imagenes.Tanque_HUDs[tanque.color],  (Datos.PANT_ANCHO / 1.75, Datos.PANT_ALTO - Imagenes.Tanque_HUDs[tanque.color].get_height() - 15))
        screen.blit(salud_texto, (Datos.PANT_ANCHO / 3.2, Datos.PANT_ALTO - 85))
        potencia_texto = font.render(f"Potencia: {int(tanque.velocidad/2)}", True, Datos.WHITE)
        screen.blit(potencia_texto, (Datos.PANT_ANCHO / 3.2, Datos.PANT_ALTO - 57))
        angulo_texto = font.render(f"Ángulo: {angulo}°", True, Datos.WHITE)
        screen.blit(angulo_texto, (Datos.PANT_ANCHO / 3.2, Datos.PANT_ALTO - 30))
        screen.blit(cant_balas, (110, Datos.PANT_ALTO - 30))
      
        turno_texto = font.render("Jugador Actual", True, Datos.WHITE)
        screen.blit(turno_texto, ((Datos.PANT_ANCHO / 1.8, Datos.PANT_ALTO - 110)))

        #mostrar el numero de rondas, partidas y turnos
        texto_turnos = font.render(f"Turnos: {Datos.turnos + 1}", True, Datos.WHITE)
        texto_rondas = font.render(f"Ronda: {Datos.rondas}", True, Datos.WHITE)
        texto_partidas = font.render(f"Partida: {Datos.partida_actual}", True, Datos.WHITE)

        screen.blit(texto_turnos, (Datos.PANT_ANCHO / 1.2, Datos.PANT_ALTO - 100))
        screen.blit(texto_rondas, (Datos.PANT_ANCHO / 1.2, Datos.PANT_ALTO - 75))
        screen.blit(texto_partidas, (Datos.PANT_ANCHO / 1.2, Datos.PANT_ALTO - 50))

    
    def muestra_imagen(self, screen, tanques, turno): # Muestra imagenes del juego
        for indice, tanque in enumerate(tanques):
            screen.blit(Imagenes.Tanque[tanque.color], (tanque.x, tanque.y-10))
            
        screen.blit(Imagenes.Exit, (Datos.PANT_ANCHO / 2.5, 10)) 
        screen.blit(Imagenes.Restart, (Datos.PANT_ANCHO / 2, 10)) 
        
        if tanques[turno].tipo_bala == 1:
            #cambiar imagen a bala 105mm
            screen.blit(Imagenes.Bala105, (50, Datos.PANT_ALTO - 75))
        elif tanques[turno].tipo_bala == 2:
            #cambiar imagen a bala 80mm
            screen.blit(Imagenes.Bala80, (60, Datos.PANT_ALTO - 75))
        elif tanques[turno].tipo_bala == 3:
            #cambiar imagen a bala 60mm
            screen.blit(Imagenes.Bala60, (70, Datos.PANT_ALTO - 75))

    def muestra_datos(self, screen, font, altura_maxima, distancia_maxima, tanques):
        for indice, tanque in enumerate(tanques):
            if tanques[indice].mostrar_datos:
                altura_texto = font.render(f"Altura máxima J{tanques[indice].num}: {altura_maxima}", True, Datos.WHITE)
                screen.blit(altura_texto, (10, Datos.PANT_ALTO - 175))
                distancia_texto = font.render(f"Distancia máxima J{tanques[indice].num}: {distancia_maxima}", True, Datos.WHITE)
                screen.blit(distancia_texto, (10, Datos.PANT_ALTO - 150))
            
    def prerotate(self, screen, num, angle, pivote):
        img, rect, x, y = Pantalla.rotate(Imagenes.Canon[num], angle, pivote)
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

    def muestra_bala(self, screen, tipo_bala, pos_x): # Muestra la bala en el juego
        if tipo_bala == 1:
            screen.blit(Imagenes.Prebala105, (pos_x, 0))
        elif tipo_bala == 2:
            screen.blit(Imagenes.Prebala80, (pos_x, 0))
        elif tipo_bala == 3:
            screen.blit(Imagenes.Prebala60, (pos_x, 0))

    #Las siguientes 5 funciones consisten en cambiar el tamaño de las imagenes para que se adapten a la resolución de la pantalla
    def background(self, screen):
        if Datos.PANT_ALTO == 600: #Default 1200x600
            screen.blit(Imagenes.Background, (0, 0))
        elif Datos.PANT_ALTO == 1080: #1920x1080
            screen.blit(Imagenes.Background1080, (0, 0))
        elif Datos.PANT_ALTO == 800: #800x800
            screen.blit(Imagenes.Background800, (0, 0))
        elif Datos.PANT_ALTO == 768: #1366x768
            screen.blit(Imagenes.Background768, (0, 0))

    def hud(self, screen):
        if Datos.PANT_ALTO == 600: #Default 1200x600
            screen.blit(Imagenes.HUD, (0, Datos.PANT_ALTO - 120))
        elif Datos.PANT_ALTO == 1080: #1920x1080
            screen.blit(Imagenes.HUD1080, (0, Datos.PANT_ALTO - 120))
        elif Datos.PANT_ALTO == 800: #800x800
            screen.blit(Imagenes.HUD800, (0, Datos.PANT_ALTO - 120))
        elif Datos.PANT_ALTO == 768: #1366x768
            screen.blit(Imagenes.HUD768, (0, Datos.PANT_ALTO - 120))        

    def fondomenu(self, screen):
        if Datos.PANT_ALTO == 600: #Default 1200x600
            screen.blit(Imagenes.FondoMenu, (0, 0))
        elif Datos.PANT_ALTO == 800: #800x800
            screen.blit(Imagenes.FondoMenu800, (0, 0))
        elif Datos.PANT_ALTO == 1080: #1920x1080    
            screen.blit(Imagenes.FondoMenu1080, (0, 0))
        elif Datos.PANT_ALTO == 768: #1366x768
            screen.blit(Imagenes.FondoMenu768, (0, 0))

    def fondoseleccion(self, screen):
        if Datos.PANT_ALTO == 600: #Default 1200x600
            screen.blit(Imagenes.FondoMenu_seleccion, (0, 0))
        elif Datos.PANT_ALTO == 800: #800x800
            screen.blit(Imagenes.FondoMenu_seleccion800, (0, 0))
        elif Datos.PANT_ALTO == 1080: #1920x1080
            screen.blit(Imagenes.FondoMenu_seleccion1080, (0, 0))
        elif Datos.PANT_ALTO == 768: #1366x768
            screen.blit(Imagenes.FondoMenu_seleccion768, (0, 0))

    def fondocontroles(self, screen):
        if Datos.PANT_ALTO == 600: #Default 1200x600
            screen.blit(Imagenes.FondoControles, (0, 0))
        elif Datos.PANT_ALTO == 800: #800x800
            screen.blit(Imagenes.FondoControles800, (0, 0))
        elif Datos.PANT_ALTO == 1080: #1920x1080
            screen.blit(Imagenes.FondoControles1080, (0, 0))
        elif Datos.PANT_ALTO == 768: #1366x768
            screen.blit(Imagenes.FondoControles768, (0, 0))

    def muestra_seleccion(self, screen, fuente): # Muestra la pantalla de seleccion de tanques
        for i in range (1,7):
            screen.blit(Imagenes.TanqueSeleccion[i], (Datos.PANT_ANCHO / Datos.Tanque_sele_ancho[i], Datos.PANT_ALTO / Datos.Tanque_sele_alto[i], 100, 100))

        #Divisiones necesarias para cuadros separados independiente la resolución
        Pantalla.draw_text('1', fuente, Datos.PANT_ANCHO / 10, Datos.PANT_ALTO / 10, Datos.WHITE, screen)
        Pantalla.draw_text('2', fuente, Datos.PANT_ANCHO / 3, Datos.PANT_ALTO / 10, Datos.WHITE, screen)
        Pantalla.draw_text('3', fuente, Datos.PANT_ANCHO / 1.764, Datos.PANT_ALTO / 10, Datos.WHITE, screen)
        Pantalla.draw_text('4', fuente, Datos.PANT_ANCHO / 10, Datos.PANT_ALTO / 2, Datos.WHITE, screen)
        Pantalla.draw_text('5', fuente, Datos.PANT_ANCHO / 3, Datos.PANT_ALTO / 2, Datos.WHITE, screen)
        Pantalla.draw_text('6', fuente, Datos.PANT_ANCHO / 1.764, Datos.PANT_ALTO / 2, Datos.WHITE, screen)

    def muestra_no_balas(self, screen, fuente, tanque): # Muestra el texto de no quedan balas
        #el texto ira subiendo y desapareciendo con cada iteración hasta que suba 100 pixeles y desaparezca
        texto = fuente.render("No quedan balas", True, Datos.BLACK)
        #ajustamos el tamaño del texto
        texto = pygame.transform.scale(texto, (texto.get_width() // 2, texto.get_height() // 2))
        texto.set_alpha(255 - Datos.sube_texto)
        screen.blit(texto, (tanque.x, tanque.y - Datos.sube_texto))
        Datos.sube_texto += 1
        pygame.display.update()
        if Datos.sube_texto == 255:
            Datos.sube_texto = 0
            Datos.anima_quedan_balas = False

pantalla = Pantalla(Datos.PANT_ANCHO, Datos.PANT_ALTO)
matriz = []