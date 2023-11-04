import pygame, imagenes, datos, Juego, sys

pygame.init()
pygame.display.set_icon(imagenes.IMG_Explosion) 
pygame.display.set_caption("PROYECTO TANQUE")
pygame.mixer.music.load('Assets/musica1.mp3')
pygame.mixer.music.set_volume(datos.volumen)
pygame.mixer.music.play(-1)
fuente = pygame.font.Font(None, 36)
size = (datos.PANT_ANCHO, datos.PANT_ALTO)
screen = pygame.display.set_mode(size)
reset = 0

def draw_text(text, font, x, y, color):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    screen.blit(textobj, textrect)


while True:
    if datos.reiniciar == True:
        datos.reiniciar = False
        screen.fill(datos.WHITE)
        texto_espera = fuente.render(f"Cargando...", True, datos.BLACK)
        screen.blit(texto_espera, (datos.PANT_ANCHO / 2 - texto_espera.get_width() / 2, datos.PANT_ALTO / 2 - texto_espera.get_height() / 2))
        pygame.display.flip() 
        pygame.time.delay(300)
        Juego.juego(screen, fuente)
    screen.blit(imagenes.FondoMenu, (0, 0))

    play_button = pygame.Rect((datos.PANT_ANCHO / 2) + 155, (datos.PANT_ALTO / 2) - 98, 100, 50)
    control_button = pygame.Rect((datos.PANT_ANCHO / 2) + 90, (datos.PANT_ALTO / 2) - 5, 100, 50)
    quit_button = pygame.Rect((datos.PANT_ANCHO / 2) + 118, (datos.PANT_ALTO / 2) + 90, 100, 50)

    draw_text('Jugar', fuente, (datos.PANT_ANCHO / 2) + 155, (datos.PANT_ALTO / 2) - 98, datos.BLACK)
    draw_text('Opciones', fuente, (datos.PANT_ANCHO / 2) + 130, (datos.PANT_ALTO / 2) - 5, datos.BLACK)
    draw_text('Salir', fuente, (datos.PANT_ANCHO / 2) + 160, (datos.PANT_ALTO / 2) + 88, datos.BLACK)

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if play_button.collidepoint(event.pos):
                Juego.juego(screen, fuente)
            if control_button.collidepoint(event.pos):
                Juego.opciones(screen)
            if quit_button.collidepoint(event.pos):
                pygame.quit()
                sys.exit()