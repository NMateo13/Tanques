import pygame, Datos, os, random, imagenes, sys


class Pantalla:
    offset = pygame.math.Vector2(0, -10)

    tank1 = 1
    tank2 = 2
        
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
    def muestra_texto(self, screen, font, tanque, angulo):
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
        screen.blit(imagenes.Tanque_HUDs[tanque.color],  (Datos.PANT_ANCHO / 1.75, Datos.PANT_ALTO - imagenes.Tanque_HUDs[tanque.color].get_height() - 15))
        screen.blit(salud_texto, (Datos.PANT_ANCHO / 3.2, Datos.PANT_ALTO - 85))
        potencia_texto = font.render(f"Potencia: {int(tanque.velocidad/2)}", True, Datos.WHITE)
        screen.blit(potencia_texto, (Datos.PANT_ANCHO / 3.2, Datos.PANT_ALTO - 57))
        angulo_texto = font.render(f"Ángulo: {angulo}°", True, Datos.WHITE)
        screen.blit(angulo_texto, (Datos.PANT_ANCHO / 3.2, Datos.PANT_ALTO - 30))
        screen.blit(cant_balas, (110, Datos.PANT_ALTO - 30))
      
        turno_texto = font.render("Jugador Actual", True, Datos.WHITE)
        screen.blit(turno_texto, ((Datos.PANT_ANCHO / 1.8, Datos.PANT_ALTO - 110)))
        nTurno_texto = font.render(f"Turno: {Datos.nTurnos}", True, Datos.WHITE)
        screen.blit(nTurno_texto, (Datos.PANT_ANCHO // 2 - nTurno_texto.get_width() // 2, Datos.PANT_ALTO - 150))
    
    
    def muestra_imagen(self, screen, tanques, turno):
        for indice, tanque in enumerate(tanques):
            screen.blit(imagenes.Tanque[tanque.color], (tanque.x, tanque.y-10))
            
        screen.blit(imagenes.Exit, (Datos.PANT_ANCHO / 2.5, 10)) 
        screen.blit(imagenes.Restart, (Datos.PANT_ANCHO / 2, 10)) 
        screen.blit(imagenes.Tienda, (Datos.PANT_ANCHO / 1.2, Datos.PANT_ALTO - 100))
        
        if tanques[turno].tipo_bala == 1:
            #cambiar imagen a bala 105mm
            screen.blit(imagenes.Bala105, (50, Datos.PANT_ALTO - 75))
        elif tanques[turno].tipo_bala == 2:
            #cambiar imagen a bala 80mm
            screen.blit(imagenes.Bala80, (60, Datos.PANT_ALTO - 75))
        elif tanques[turno].tipo_bala == 3:
            #cambiar imagen a bala 60mm
            screen.blit(imagenes.Bala60, (70, Datos.PANT_ALTO - 75))

    def muestra_datos(self, screen, font, altura_maxima, distancia_maxima, tanques):
        for indice, tanque in enumerate(tanques):
            if tanques[indice].mostrar_datos:
                altura_texto = font.render(f"Altura máxima J{tanques[indice].num}: {altura_maxima}", True, Datos.WHITE)
                screen.blit(altura_texto, (10, Datos.PANT_ALTO - 175))
                distancia_texto = font.render(f"Distancia máxima J{tanques[indice].num}: {distancia_maxima}", True, Datos.WHITE)
                screen.blit(distancia_texto, (10, Datos.PANT_ALTO - 150))
            
    def prerotate(self, screen, num, angle, pivote):
        img, rect, x, y = Pantalla.rotate(imagenes.Canon[num], angle, pivote)
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

    def muestra_bala(self, screen, tipo_bala, pos_x):
        if tipo_bala == 1:
            screen.blit(imagenes.Prebala105, (pos_x, 0))
        elif tipo_bala == 2:
            screen.blit(imagenes.Prebala80, (pos_x, 0))
        elif tipo_bala == 3:
            screen.blit(imagenes.Prebala60, (pos_x, 0))

    #Las siguientes funciones consisten en cambiar el tamaño de las imagenes para que se adapten a la resolución de la pantalla
    def background(self, screen):
        if Datos.PANT_ALTO == 600: #Default 1200x600
            screen.blit(imagenes.Background, (0, 0))
        elif Datos.PANT_ALTO == 1080: #1920x1080
            screen.blit(imagenes.Background1080, (0, 0))
        elif Datos.PANT_ALTO == 800: #800x800
            screen.blit(imagenes.Background800, (0, 0))
        elif Datos.PANT_ALTO == 768: #1366x768
            screen.blit(imagenes.Background768, (0, 0))

    def hud(self, screen):
        if Datos.PANT_ALTO == 600: #Default 1200x600
            screen.blit(imagenes.HUD, (0, Datos.PANT_ALTO - 120))
        elif Datos.PANT_ALTO == 1080: #1920x1080
            screen.blit(imagenes.HUD1080, (0, Datos.PANT_ALTO - 120))
        elif Datos.PANT_ALTO == 800: #800x800
            screen.blit(imagenes.HUD800, (0, Datos.PANT_ALTO - 120))
        elif Datos.PANT_ALTO == 768: #1366x768
            screen.blit(imagenes.HUD768, (0, Datos.PANT_ALTO - 120))        

    def fondomenu(self, screen):
        if Datos.PANT_ALTO == 600: #Default 1200x600
            screen.blit(imagenes.FondoMenu, (0, 0))
        elif Datos.PANT_ALTO == 800: #800x800
            screen.blit(imagenes.FondoMenu800, (0, 0))
        elif Datos.PANT_ALTO == 1080: #1920x1080    
            screen.blit(imagenes.FondoMenu1080, (0, 0))
        elif Datos.PANT_ALTO == 768: #1366x768
            screen.blit(imagenes.FondoMenu768, (0, 0))

    def fondoseleccion(self, screen):
        if Datos.PANT_ALTO == 600: #Default 1200x600
            screen.blit(imagenes.FondoMenu_seleccion, (0, 0))
        elif Datos.PANT_ALTO == 800: #800x800
            screen.blit(imagenes.FondoMenu_seleccion800, (0, 0))
        elif Datos.PANT_ALTO == 1080: #1920x1080
            screen.blit(imagenes.FondoMenu_seleccion1080, (0, 0))
        elif Datos.PANT_ALTO == 768: #1366x768
            screen.blit(imagenes.FondoMenu_seleccion768, (0, 0))

    def fondocontroles(self, screen):
        if Datos.PANT_ALTO == 600: #Default 1200x600
            screen.blit(imagenes.FondoControles, (0, 0))
        elif Datos.PANT_ALTO == 800: #800x800
            screen.blit(imagenes.FondoControles800, (0, 0))
        elif Datos.PANT_ALTO == 1080: #1920x1080
            screen.blit(imagenes.FondoControles1080, (0, 0))
        elif Datos.PANT_ALTO == 768: #1366x768
            screen.blit(imagenes.FondoControles768, (0, 0))

    def muestra_seleccion(self, screen, fuente):
        #Cuadro 1
        screen.blit(imagenes.TanqueSeleccionVerde, (Datos.PANT_ANCHO / 9.5, Datos.PANT_ALTO / 6.5, 100, 100)) 
        #Cuadro 2
        screen.blit(imagenes.TanqueSeleccionRojo, (Datos.PANT_ANCHO / 2.95, Datos.PANT_ALTO / 6.5, 100, 100)) 
        #Cuadro 3
        screen.blit(imagenes.TanqueSeleccionAzul, (Datos.PANT_ANCHO / 1.75, Datos.PANT_ALTO / 6.5, 100, 100))
        #Cuadro 4
        screen.blit(imagenes.TanqueSeleccionAmarillo, (Datos.PANT_ANCHO / 9.5, Datos.PANT_ALTO / 1.8, 100, 100))
        #Cuadro 5
        screen.blit(imagenes.TanqueSeleccionRosa, (Datos.PANT_ANCHO / 2.95, Datos.PANT_ALTO / 1.8, 100, 100))
        #Cuadro 6
        screen.blit(imagenes.TanqueSeleccionCeleste, (Datos.PANT_ANCHO / 1.75, Datos.PANT_ALTO / 1.8, 100, 100))

        #Divisiones necesarias para cuadros separados independiente la resolución
        Pantalla.draw_text('1', fuente, Datos.PANT_ANCHO / 10, Datos.PANT_ALTO / 10, Datos.WHITE, screen)
        Pantalla.draw_text('2', fuente, Datos.PANT_ANCHO / 3, Datos.PANT_ALTO / 10, Datos.WHITE, screen)
        Pantalla.draw_text('3', fuente, Datos.PANT_ANCHO / 1.764, Datos.PANT_ALTO / 10, Datos.WHITE, screen)
        Pantalla.draw_text('4', fuente, Datos.PANT_ANCHO / 10, Datos.PANT_ALTO / 2, Datos.WHITE, screen)
        Pantalla.draw_text('5', fuente, Datos.PANT_ANCHO / 3, Datos.PANT_ALTO / 2, Datos.WHITE, screen)
        Pantalla.draw_text('6', fuente, Datos.PANT_ANCHO / 1.764, Datos.PANT_ALTO / 2, Datos.WHITE, screen)

        Pantalla.draw_text('Jugar', fuente, Datos.PANT_ANCHO / 1.2, Datos.PANT_ALTO / 10, Datos.WHITE, screen)
        Pantalla.draw_text('Volver', fuente, Datos.PANT_ANCHO / 1.2, Datos.PANT_ALTO / 1.53, Datos.WHITE, screen)
        Pantalla.draw_text('Controles', fuente, Datos.PANT_ANCHO / 1.2, Datos.PANT_ALTO / 2.65, Datos.WHITE, screen)


pantalla = Pantalla(Datos.PANT_ANCHO, Datos.PANT_ALTO)
matriz = []