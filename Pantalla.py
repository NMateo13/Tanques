import pygame, os, random


class Pantalla:
    
    #Colores
    WHITE = (225, 225, 225)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 153, 0)
    GRAY = (128, 139, 150)
    BLUE = (0,0,255)

    offset = pygame.math.Vector2(0, -10)
    #Seleccion aleatoria de los tanques
    tank1 = random.randint(1, 4)
    tank2 = random.randint(1, 4)
    while tank1 == tank2:
        tank2 = random.randint(1, 4)

    #Imagenes
    if tank1 == 1:
        IMG_Tanque1 = pygame.image.load(os.path.join("Assets", "Tanque1.png"))
    elif tank1 == 2:
        IMG_Tanque1 = pygame.image.load(os.path.join("Assets", "Tanque2.png"))
    elif tank1 == 3:
        IMG_Tanque1 = pygame.image.load(os.path.join("Assets", "Tanque3.png"))
    elif tank1 == 4:
        IMG_Tanque1 = pygame.image.load(os.path.join("Assets", "Tanque4.png"))  
    if tank2 == 1:
        IMG_Tanque2 = pygame.image.load(os.path.join("Assets", "Tanque1.png"))
    elif tank2 == 2:
        IMG_Tanque2 = pygame.image.load(os.path.join("Assets", "Tanque2.png"))
    elif tank2 == 3:
        IMG_Tanque2 = pygame.image.load(os.path.join("Assets", "Tanque3.png"))
    elif tank2 == 4:
        IMG_Tanque2 = pygame.image.load(os.path.join("Assets", "Tanque4.png"))
    if tank1 == 1:
        IMG_Canon1 = pygame.image.load(os.path.join("Assets", "canon1.png"))
    elif tank1 == 2:
        IMG_Canon1 = pygame.image.load(os.path.join("Assets", "canon2.png"))
    elif tank1 == 3:
        IMG_Canon1 = pygame.image.load(os.path.join("Assets", "canon3.png"))
    elif tank1 == 4:
        IMG_Canon1 = pygame.image.load(os.path.join("Assets", "canon4.png"))
    if tank2 == 1:
        IMG_Canon2 = pygame.image.load(os.path.join("Assets", "canon1.png"))
    elif tank2 == 2:
        IMG_Canon2 = pygame.image.load(os.path.join("Assets", "canon2.png"))
    elif tank2 == 3:
        IMG_Canon2 = pygame.image.load(os.path.join("Assets", "canon3.png"))
    elif tank2 == 4:
        IMG_Canon2 = pygame.image.load(os.path.join("Assets", "canon4.png"))
    IMG_Background = pygame.image.load(os.path.join("Assets", "Background.png"))
    IMG_HUD = pygame.image.load(os.path.join("Assets", "hud_bg.png"))
    IMG_Explosion = pygame.image.load(os.path.join("Assets", "boom.png"))
    IMG_BalaCanyon = pygame.image.load(os.path.join("Assets", "bala_canon.png"))
    
    #Reescalado de imagenes
    Tanque1 = pygame.transform.scale(IMG_Tanque1, (IMG_Tanque1.get_width() // 4, IMG_Tanque1.get_height() // 4))
    Tanque2 = pygame.transform.scale(IMG_Tanque2, (IMG_Tanque2.get_width() // 4, IMG_Tanque2.get_height() // 4))
    Canon1 = pygame.transform.scale(IMG_Canon1, (IMG_Canon1.get_width() // 4, IMG_Canon1.get_height() // 4))
    Canon2 = pygame.transform.scale(IMG_Canon2, (IMG_Canon2.get_width() // 4, IMG_Canon2.get_height() // 4))
    Tanque1_HUD = pygame.transform.scale(IMG_Tanque1, (IMG_Tanque1.get_width() // 2, IMG_Tanque1.get_height() // 2))
    Tanque2_HUD = pygame.transform.scale(IMG_Tanque2, (IMG_Tanque2.get_width() // 2, IMG_Tanque2.get_height() // 2))
    BalaCanyon = pygame.transform.scale(IMG_BalaCanyon, (IMG_BalaCanyon.get_width() // 2, IMG_BalaCanyon.get_height() // 2))
    Background = pygame.transform.scale(IMG_Background, (1200, 540))
    HUD = pygame.transform.scale(IMG_HUD, (1200, 120))

    
    """
    J1_1 = (69, 266)
    J1_2 = (156, 230)
    J1_3 = (320, 335)
    J1_4 = (467, 429)

    J2_1 = (661, 297)
    J2_2 = (786, 230)
    J2_3 = (947, 335)
    J2_4 = (1100, 430)
    """
    J1X = [24, 140, 260, 365]
    J1Y = [250, 210, 270, 370]
    J2X = [10, 105, 205, 390]
    J2Y = [390, 390, 300, 210]

    #Posiciones de los tanques 

    posTanque1 = random.randint(0, 3)
    posTanque2 = random.randint(0, 3)

    posX_Tanque1 = J1X[posTanque1]
    posY_Tanque1 = J1Y[posTanque1]

    posX_Tanque2 = J2X[posTanque2]
    posY_Tanque2 = J2Y[posTanque2]

    medidaHUD = 120    

    def __init__(self, ancho, alto):
        
        self.ancho = ancho
        self.alto = alto

    def crearMatriz(self, alto, ancho):

        Pantalla.matriz = [[0] * ancho for _ in range(alto - Pantalla.medidaHUD)]

    def dibujar(self, screen):
        
        for filas in range(0, (pantalla.alto - pantalla.medidaHUD)):
            for columnas in range (0, pantalla.ancho):
                if pantalla.matriz[filas][columnas] == 1:
                    pygame.draw.rect(screen, pantalla.GREEN, (columnas, filas, 6, 6))
    
    #Funciones para mostrar información en la pantalla
    def muestra_texto(self, screen, font): 
        jugador_texto1 = font.render(f"Jugador 1", True, pantalla.WHITE)
        screen.blit(jugador_texto1, (460, pantalla.alto - 110))

        jugador_texto2 = font.render(f"Jugador 2", True, pantalla.WHITE)
        screen.blit(jugador_texto2, (pantalla.ancho - jugador_texto2.get_width() - 460, pantalla.alto - 110))

        stats = font.render(f"STATS", True, pantalla.RED)
        screen.blit(stats, (300, pantalla.alto - 110))
        screen.blit(stats, (pantalla.ancho - stats.get_width() - 300, pantalla.alto - 110))

        bala = font.render(f"TIPO DE BALA", True, pantalla.RED)
        screen.blit(bala, (25, pantalla.alto - 110))
        screen.blit(bala, (pantalla.ancho - bala.get_width() - 25, pantalla.alto - 110))

    def muestra_salud(self, screen, font): #falta agregar las variables de vida de los tanques
        salud_texto1 = font.render(f"Vida: 100%", True, pantalla.WHITE)
        screen.blit(salud_texto1, (250, pantalla.alto - 85))

        salud_texto2 = font.render(f"Vida: 100%", True, pantalla.WHITE) 
        screen.blit(salud_texto2, (pantalla.ancho - salud_texto2.get_width() - 300, pantalla.alto - 85))

    def muestra_potencia(self, screen, font,velocidad_jugador1, velocidad_jugador2): 
        potencia_texto1 = font.render(f"Potencia: {velocidad_jugador1}", True, pantalla.WHITE)
        screen.blit(potencia_texto1, (250, pantalla.alto - 57))

        potencia_texto2 = font.render(f"Potencia: {velocidad_jugador2}", True, pantalla.WHITE)
        screen.blit(potencia_texto2, (pantalla.ancho - potencia_texto2.get_width() - 280, pantalla.alto - 57))

    def muestra_angulo(self, screen, font,angulo_jugador1, angulo_jugador2): 
        angulo_texto1 = font.render(f"Ángulo: {angulo_jugador1}°", True, pantalla.WHITE)
        screen.blit(angulo_texto1, (250, pantalla.alto - 30))

        angulo_texto2 = font.render(f"Ángulo: {angulo_jugador2}°", True, pantalla.WHITE)
        screen.blit(angulo_texto2, (pantalla.ancho - angulo_texto2.get_width() - 280, pantalla.alto - 30))

    def muestra_imagen(self, screen, tipo1, tipo2):
        screen.blit(pantalla.Tanque1, (self.posX_Tanque1, self.posY_Tanque1)) 
        screen.blit(pantalla.Tanque2, (pantalla.ancho - pantalla.Tanque2.get_width() - self.posX_Tanque2, self.posY_Tanque2)) 

        #NO TOCAR SON ESTÁTICOS 
        screen.blit(pantalla.Tanque1_HUD, (450, 600)) 
        screen.blit(pantalla.Tanque2_HUD, (pantalla.ancho - pantalla.Tanque2_HUD.get_width() - 450, 600)) 
        if tipo1 == 1:
            screen.blit(pantalla.BalaCanyon, (65, pantalla.alto - 90))
        elif tipo1 == 2:
            #cambiar imagen a bala tipo 2
            print()
        elif tipo1 == 3:
            #cambiar imagen a bala tipo 3
            print()
        
        if tipo2 == 1:
            screen.blit(pantalla.BalaCanyon, (pantalla.ancho - pantalla.BalaCanyon.get_width() - 65, pantalla.alto - 90))
        elif tipo2 == 2:
            #cambiar imagen a bala tipo 2
            print()
        elif tipo2 == 3:
            #cambiar imagen a bala tipo 3
            print()
        #los print son para que no tire error

        #NO TOCAR SON ESTÁTICOS
    #ahora se iniciará una función para calcular la altura maxima de la bala y la distancia recorrida por la bala y se mostrará en pantalla
    def muestra_altura(self, screen, font, altura_maxima, mostrar1, mostrar2):
        if mostrar1:
            altura_texto1 = font.render(f"Altura máxima J1: {altura_maxima}", True, pantalla.WHITE)
            screen.blit(altura_texto1, (10, pantalla.alto - 150))
        elif mostrar2:
            altura_texto2 = font.render(f"Altura máxima J2: {altura_maxima}", True, pantalla.WHITE)
            screen.blit(altura_texto2, (10, pantalla.alto - 150))
    
    

    def prerotate(self, screen, num, angle, pivote):
        if num==1:
            img, rect, x, y = Pantalla.rotate(pantalla.Canon1, angle, pivote)
        elif num==2:
            img, rect, x, y = Pantalla.rotate(pantalla.Canon2, angle, pivote)
        screen.blit(img, rect)
        return x, y

    
    def rotate(surface, angle, pivot):
        rotated_image = pygame.transform.rotozoom(surface, -angle, 1)
        #rota el vector de desplazamiento
        rotated_offset = Pantalla.offset.rotate(angle)
        # Agregua el vector de desplazamiento al punto pivote para desplazar el rectangulo.
        rect = rotated_image.get_rect(center=pivot+rotated_offset)
        # Devuelve la imagen rotada y el rectangulo desplazado
        x = rect.x
        y = rect.y
        return rotated_image, rect, x, y
pantalla = Pantalla(1200, 660)
matriz = []