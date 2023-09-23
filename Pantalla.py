import pygame, os


class Pantalla:
    
    #Colores
    WHITE = (225, 225, 225)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 153, 0)
    GRAY = (128, 139, 150)

    #Imagenes
    IMG_Tanque1 = pygame.image.load(os.path.join("Assets", "Tanque1.png"))
    IMG_Tanque2 = pygame.image.load(os.path.join("Assets", "Tanque2.png"))
    IMG_Background = pygame.image.load(os.path.join("Assets", "Background.png"))
    IMG_HUD = pygame.image.load(os.path.join("Assets", "hud_bg.png"))
    IMG_Explosion = pygame.image.load(os.path.join("Assets", "boom.png"))
    IMG_BalaCanyon = pygame.image.load(os.path.join("Assets", "bala_canon.png"))
    
    #Reescalado de imagenes
    Tanque1 = pygame.transform.scale(IMG_Tanque1, (IMG_Tanque1.get_width() // 4, IMG_Tanque1.get_height() // 4))
    Tanque2 = pygame.transform.scale(IMG_Tanque2, (IMG_Tanque2.get_width() // 4, IMG_Tanque2.get_height() // 4))
    Tanque1_HUD = pygame.transform.scale(IMG_Tanque1, (IMG_Tanque1.get_width() // 2, IMG_Tanque1.get_height() // 2))
    Tanque2_HUD = pygame.transform.scale(IMG_Tanque2, (IMG_Tanque2.get_width() // 2, IMG_Tanque2.get_height() // 2))
    BalaCanyon = pygame.transform.scale(IMG_BalaCanyon, (IMG_BalaCanyon.get_width() // 2, IMG_BalaCanyon.get_height() // 2))
    Background = pygame.transform.scale(IMG_Background, (1200, 540))
    HUD = pygame.transform.scale(IMG_HUD, (1200, 120))

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

    def muestra_potencia(self, screen, font): #falta agregar las variables de potencia de la bala
        potencia_texto1 = font.render(f"Potencia: 20", True, pantalla.WHITE)
        screen.blit(potencia_texto1, (250, pantalla.alto - 57))

        potencia_texto2 = font.render(f"Potencia: 40", True, pantalla.WHITE)
        screen.blit(potencia_texto2, (pantalla.ancho - potencia_texto2.get_width() - 280, pantalla.alto - 57))

    def muestra_angulo(self, screen, font): #falta agregar las variables de angulo de la bala
        angulo_texto1 = font.render(f"Angulo: 45°", True, pantalla.WHITE)
        screen.blit(angulo_texto1, (250, pantalla.alto - 30))

        angulo_texto2 = font.render(f"Angulo: 80°", True, pantalla.WHITE)
        screen.blit(angulo_texto2, (pantalla.ancho - angulo_texto2.get_width() - 280, pantalla.alto - 30))

    def muestra_imagen(self, screen):
        screen.blit(pantalla.Tanque1, (250, 280))
        screen.blit(pantalla.Tanque2, (pantalla.ancho - pantalla.Tanque2.get_width() - 250, 280))

        screen.blit(pantalla.Tanque1_HUD, (390, 460))
        screen.blit(pantalla.Tanque2_HUD, (pantalla.ancho - pantalla.Tanque2_HUD.get_width() - 370, 460))

        screen.blit(pantalla.BalaCanyon, (65, pantalla.alto - 90))
        screen.blit(pantalla.BalaCanyon, (pantalla.ancho - pantalla.BalaCanyon.get_width() - 65, pantalla.alto - 90))
        
pantalla = Pantalla(1200, 660)
matriz = []

    
