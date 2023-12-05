import pygame, imagenes, Datos, sys, Pantalla, Tanque
from Juego import Juego


pygame.init()
pygame.display.set_icon(imagenes.IMG_Explosion) 
pygame.display.set_caption("PROYECTO TANQUE")
pygame.mixer.music.load('Assets/musica1.mp3')
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

while True:
    if Datos.reiniciar == True:
        Datos.reiniciar = False
        screen.fill(Datos.WHITE)
        texto_espera = fuente.render(f"Cargando...", True, Datos.BLACK)
        screen.blit(texto_espera, (Datos.PANT_ANCHO / 2 - texto_espera.get_width() / 2, Datos.PANT_ALTO / 2 - texto_espera.get_height() / 2))
        pygame.display.flip()
        pygame.time.delay(300)
        Datos.bandera_tanque = True
        Juego.juego(screen, fuente)
    screen.blit(imagenes.FondoMenu, (0, 0))

    play_button = pygame.Rect((Datos.PANT_ANCHO / 2) + 95, (Datos.PANT_ALTO / 2) - 98, 100, 50)
    control_button = pygame.Rect((Datos.PANT_ANCHO / 2) + 75, (Datos.PANT_ALTO / 2) - 5, 100, 50)
    quit_button = pygame.Rect((Datos.PANT_ANCHO / 2) + 100, (Datos.PANT_ALTO / 2) + 90, 100, 50)

    draw_text('Jugar', fuente, (Datos.PANT_ANCHO / 2) + 95, (Datos.PANT_ALTO / 2) - 98, Datos.WHITE)
    draw_text('Opciones', fuente, (Datos.PANT_ANCHO / 2) + 75, (Datos.PANT_ALTO / 2) - 5, Datos.WHITE)
    draw_text('Salir', fuente, (Datos.PANT_ANCHO / 2) + 100, (Datos.PANT_ALTO / 2) + 88, Datos.WHITE)


    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if play_button.collidepoint(event.pos):
                Juego.seleccion(screen, fuente)
                Juego.juego(screen, fuente)
            if control_button.collidepoint(event.pos):
                Juego.opciones(screen)
            if quit_button.collidepoint(event.pos):
                pygame.quit()
                sys.exit()
