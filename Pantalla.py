import pygame, os

class Pantalla:

    WHITE = (225, 225, 225)
    BLACK = (0, 0, 0)
    GREEN = (0, 153, 0)
    GRAY = (128, 139, 150)

    IMG_Tanque1 = pygame.image.load(os.path.join("Assets", "Tanque1.png"))
    IMG_Tanque2 = pygame.image.load(os.path.join("Assets", "Tanque2.png"))
    Tanque1 = pygame.transform.scale(IMG_Tanque1, (IMG_Tanque1.get_width() // 2, IMG_Tanque1.get_height() // 2))
    Tanque2 = pygame.transform.scale(IMG_Tanque2, (IMG_Tanque2.get_width() // 2, IMG_Tanque2.get_height() // 2))

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
    def muestra_salud(self, screen, font): #falta agregar las variables de vida de los tanques
        salud_texto1 = font.render(f"Vida: 100%", True, pantalla.BLACK)
        screen.blit(salud_texto1, (10, pantalla.alto - 80))

        salud_texto2 = font.render(f"Vida: 100%", True, pantalla.BLACK) 
        screen.blit(salud_texto2, (pantalla.ancho - salud_texto2.get_width() - 10, pantalla.alto - 80))

    def muestra_potencia(self, screen, font): #falta agregar las variables de potencia de la bala
        potencia_texto1 = font.render(f"Potencia: 20", True, pantalla.BLACK)
        screen.blit(potencia_texto1, (10, pantalla.alto - 50))

        potencia_texto2 = font.render(f"Potencia: 40", True, pantalla.BLACK)
        screen.blit(potencia_texto2, (pantalla.ancho - potencia_texto2.get_width() - 10, pantalla.alto - 50))

    def muestra_angulo(self, screen, font): #falta agregar las variables de angulo de la bala
        angulo_texto1 = font.render(f"Angulo: 45°", True, pantalla.BLACK)
        screen.blit(angulo_texto1, (10, pantalla.alto - 25))

        angulo_texto2 = font.render(f"Angulo: 80°", True, pantalla.BLACK)
        screen.blit(angulo_texto2, (pantalla.ancho - angulo_texto2.get_width() - 10, pantalla.alto - 25))

    def muestra_jugador(self, screen, font):
        jugador_texto1 = font.render(f"Jugador 1", True, pantalla.BLACK)
        screen.blit(jugador_texto1, (10, pantalla.alto - 110))
        jugador_texto2 = font.render(f"Jugador 2", True, pantalla.BLACK)
        screen.blit(jugador_texto2, (pantalla.ancho - jugador_texto2.get_width() - 10, pantalla.alto - 110))
        screen.blit(pantalla.Tanque1, (250, 450))
        screen.blit(pantalla.Tanque2, (pantalla.ancho - pantalla.Tanque2.get_width() - 250, 450))    
        
pantalla = Pantalla(1200, 660)
matriz = []

    
