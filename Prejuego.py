import pygame, Imagenes, Datos, sys, Pantalla
from Juego import Juego

# Se inicializa pygame
pygame.init()
pygame.display.set_icon(Imagenes.IMG_Explosion) 
pygame.display.set_caption("PROYECTO TANQUE")
pygame.mixer.music.load('Assets/musica.mp3')
pygame.mixer.music.set_volume(Datos.volumen)
#pygame.mixer.music.play(-1)
fuente = pygame.font.Font(None, 36)
size = (Datos.PANT_ANCHO, Datos.PANT_ALTO)
screen = pygame.display.set_mode(size)
reset = 0

def draw_text(text, font, x, y, color):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    screen.blit(textobj, textrect)
    
def draw_button(rect, text, font, text_color, button_color, hover_color, screen):
    pygame.draw.rect(screen, hover_color if rect.collidepoint(pygame.mouse.get_pos()) else button_color, rect)
    text_surface = font.render(text, True, text_color)
    text_rect = text_surface.get_rect(center=rect.center)
    screen.blit(text_surface, text_rect)

while True:
    if Datos.reiniciar == True:   
        Datos.reiniciar = False
        Pantalla.pantalla.fondoblanco(screen)
        texto_espera = fuente.render("Cargando...", True, Datos.BLACK)
        screen.blit(texto_espera, (Datos.PANT_ANCHO / 2 - texto_espera.get_width() / 2, Datos.PANT_ALTO / 2 - texto_espera.get_height() / 2))
        pygame.display.flip()
        pygame.time.delay(300)
        Datos.bandera_tanque = True
        Juego.juego(screen, fuente)

    # Se llama a funcion que muestra la imagen de fondo del menu
    Pantalla.pantalla.fondomenu(screen)
    
    # Se crean los botones del menu
    play_button = pygame.Rect((Datos.PANT_ANCHO / 1.72), (Datos.PANT_ALTO / 3), 100, 50)
    settings_button = pygame.Rect((Datos.PANT_ANCHO / 1.72), (Datos.PANT_ALTO / 2.2), 100, 50)
    quit_button = pygame.Rect((Datos.PANT_ANCHO / 1.72), (Datos.PANT_ALTO / 1.75), 100, 50)
    # Se dibujan los botones del menu
    draw_button(play_button, 'Jugar', fuente, Datos.WHITE, Datos.BLACK, Datos.GREEN, screen)
    draw_button(settings_button, 'Opciones', fuente, Datos.WHITE, Datos.BLACK, Datos.GREEN, screen)
    draw_button(quit_button, 'Salir', fuente, Datos.WHITE, Datos.BLACK, Datos.GREEN, screen)

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if play_button.collidepoint(event.pos):
                jugar = Juego.seleccion(screen, fuente)
                if jugar == True:
                    Juego.juego(screen, fuente)
            if settings_button.collidepoint(event.pos):
                Juego.opciones(screen)
            if quit_button.collidepoint(event.pos):
                pygame.quit()
                sys.exit()
