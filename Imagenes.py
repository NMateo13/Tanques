import Datos, os, pygame

# Imagenes
IMG_Tanque1 = pygame.image.load(os.path.join("Assets", "Tanque1.png"))
IMG_Tanque2 = pygame.image.load(os.path.join("Assets", "Tanque2.png"))
IMG_Tanque3 = pygame.image.load(os.path.join("Assets", "Tanque3.png"))
IMG_Tanque4 = pygame.image.load(os.path.join("Assets", "Tanque4.png"))
IMG_Tanque5 = pygame.image.load(os.path.join("Assets", "Tanque5.png"))
IMG_Tanque6 = pygame.image.load(os.path.join("Assets", "Tanque6.png"))
IMG_Canon1 = pygame.image.load(os.path.join("Assets", "canon1.png"))
IMG_Canon2 = pygame.image.load(os.path.join("Assets", "canon2.png"))
IMG_Canon3 = pygame.image.load(os.path.join("Assets", "canon3.png"))
IMG_Canon4 = pygame.image.load(os.path.join("Assets", "canon4.png"))
IMG_Canon5 = pygame.image.load(os.path.join("Assets", "canon5.png"))
IMG_Canon6 = pygame.image.load(os.path.join("Assets", "canon6.png"))
IMG_Background = pygame.image.load(os.path.join("Assets", "background.png"))
IMG_HUD = pygame.image.load(os.path.join("Assets", "hud_bg.png"))
IMG_Explosion = pygame.image.load(os.path.join("Assets", "boom.png"))
IMG_Bala60 = pygame.image.load(os.path.join("Assets", "bala60.png"))
IMG_Bala80 = pygame.image.load(os.path.join("Assets", "bala80.png"))
IMG_Bala105 = pygame.image.load(os.path.join("Assets", "bala105.png"))
IMG_Exit = pygame.image.load(os.path.join("Assets", "exit.png"))
IMG_Restart = pygame.image.load(os.path.join("Assets", "reset.png"))
IMG_FondoMenu = pygame.image.load(os.path.join("Assets", "menu.png"))
IMG_fondo_controles = pygame.image.load(os.path.join("Assets", "fondo_controles.png"))
IMG_Prebala_105 = pygame.image.load(os.path.join("Assets", "prebala105.png"))
IMG_Prebala_80 = pygame.image.load(os.path.join("Assets", "prebala80.png"))
IMG_Prebala_60 = pygame.image.load(os.path.join("Assets", "prebala60.png"))
IMG_Background_seleccion = pygame.image.load(os.path.join("Assets", "fondo_menu.png"))
IMG_FondoBlanco = pygame.image.load(os.path.join("Assets", "fondoblanco.jpg"))

#Reescalado de imagenes
TanqueSeleccion = {
    1: pygame.transform.scale(IMG_Tanque1, (IMG_Tanque1.get_width() // 3, IMG_Tanque1.get_height() // 3)),
    2: pygame.transform.scale(IMG_Tanque2, (IMG_Tanque2.get_width() // 3, IMG_Tanque2.get_height() // 3)),
    3: pygame.transform.scale(IMG_Tanque3, (IMG_Tanque3.get_width() // 3, IMG_Tanque3.get_height() // 3)),
    4: pygame.transform.scale(IMG_Tanque4, (IMG_Tanque4.get_width() // 3, IMG_Tanque4.get_height() // 3)),
    5: pygame.transform.scale(IMG_Tanque5, (IMG_Tanque5.get_width() // 3, IMG_Tanque5.get_height() // 3)),
    6: pygame.transform.scale(IMG_Tanque6, (IMG_Tanque6.get_width() // 3, IMG_Tanque6.get_height() // 3))
}

Tanque = {
    1: pygame.transform.scale(IMG_Tanque1, (IMG_Tanque1.get_width() // 4, IMG_Tanque1.get_height() // 4)),
    2: pygame.transform.scale(IMG_Tanque2, (IMG_Tanque2.get_width() // 4, IMG_Tanque2.get_height() // 4)),
    3: pygame.transform.scale(IMG_Tanque3, (IMG_Tanque3.get_width() // 4, IMG_Tanque3.get_height() // 4)),
    4: pygame.transform.scale(IMG_Tanque4, (IMG_Tanque4.get_width() // 4, IMG_Tanque4.get_height() // 4)),
    5: pygame.transform.scale(IMG_Tanque5, (IMG_Tanque5.get_width() // 4, IMG_Tanque5.get_height() // 4)),
    6: pygame.transform.scale(IMG_Tanque6, (IMG_Tanque6.get_width() // 4, IMG_Tanque6.get_height() // 4))
}
Canon = {
    1: pygame.transform.scale(IMG_Canon1, (IMG_Canon1.get_width() // 4, IMG_Canon1.get_height() // 4)),
    2: pygame.transform.scale(IMG_Canon2, (IMG_Canon2.get_width() // 4, IMG_Canon2.get_height() // 4)),
    3: pygame.transform.scale(IMG_Canon3, (IMG_Canon3.get_width() // 4, IMG_Canon3.get_height() // 4)),
    4: pygame.transform.scale(IMG_Canon4, (IMG_Canon4.get_width() // 4, IMG_Canon4.get_height() // 4)),
    5: pygame.transform.scale(IMG_Canon5, (IMG_Canon5.get_width() // 4, IMG_Canon5.get_height() // 4)),
    6: pygame.transform.scale(IMG_Canon6, (IMG_Canon6.get_width() // 4, IMG_Canon6.get_height() // 4))
}

Background = pygame.transform.scale(IMG_Background, (Datos.PANT_ANCHO, Datos.PANT_ALTO))
HUD = pygame.transform.scale(IMG_HUD, (Datos.PANT_ANCHO, 120))    
Tanque_HUDs = {
    1: pygame.transform.scale(IMG_Tanque1, (IMG_Tanque1.get_width() // 2, IMG_Tanque1.get_height() // 2)),
    2: pygame.transform.scale(IMG_Tanque2, (IMG_Tanque2.get_width() // 2, IMG_Tanque2.get_height() // 2)),
    3: pygame.transform.scale(IMG_Tanque3, (IMG_Tanque3.get_width() // 2, IMG_Tanque3.get_height() // 2)),
    4: pygame.transform.scale(IMG_Tanque4, (IMG_Tanque4.get_width() // 2, IMG_Tanque4.get_height() // 2)),
    5: pygame.transform.scale(IMG_Tanque5, (IMG_Tanque5.get_width() // 2, IMG_Tanque5.get_height() // 2)),
    6: pygame.transform.scale(IMG_Tanque6, (IMG_Tanque6.get_width() // 2, IMG_Tanque6.get_height() // 2))
}
Tanque_Tooltip = {
    1: pygame.transform.scale(IMG_Tanque1, (IMG_Tanque1.get_width() // 4, IMG_Tanque1.get_height() // 4)),
    2: pygame.transform.scale(IMG_Tanque2, (IMG_Tanque2.get_width() // 4, IMG_Tanque2.get_height() // 4)),
    3: pygame.transform.scale(IMG_Tanque3, (IMG_Tanque3.get_width() // 4, IMG_Tanque3.get_height() // 4)),
    4: pygame.transform.scale(IMG_Tanque4, (IMG_Tanque4.get_width() // 4, IMG_Tanque4.get_height() // 4)),
    5: pygame.transform.scale(IMG_Tanque5, (IMG_Tanque5.get_width() // 4, IMG_Tanque5.get_height() // 4)),
    6: pygame.transform.scale(IMG_Tanque6, (IMG_Tanque6.get_width() // 4, IMG_Tanque6.get_height() // 4))
}
Bala105 = pygame.transform.scale(IMG_Bala105, (IMG_Bala105.get_width() // 1.5, IMG_Bala105.get_height() // 1.5))
Bala80 = pygame.transform.scale(IMG_Bala80, (IMG_Bala80.get_width() // 1.75, IMG_Bala80.get_height() // 1.75))
Bala60 = pygame.transform.scale(IMG_Bala60, (IMG_Bala60.get_width() // 2, IMG_Bala60.get_height() // 2))
Explosion = pygame.transform.scale(IMG_Explosion, (IMG_Explosion.get_width() // 4, IMG_Explosion.get_height() // 4))
Exit = pygame.transform.scale(IMG_Exit, (IMG_Exit.get_width() // 1.5, IMG_Exit.get_height() // 1.5))
Restart = pygame.transform.scale(IMG_Restart, (IMG_Restart.get_width() // 1.5, IMG_Restart.get_height() // 1.5))
Prebala105 = pygame.transform.scale(IMG_Prebala_105, (IMG_Prebala_105.get_width() // 6, IMG_Prebala_105.get_height() // 6))
Prebala80 = pygame.transform.scale(IMG_Prebala_80, (IMG_Prebala_80.get_width() // 6, IMG_Prebala_80.get_height() // 6))
Prebala60 = pygame.transform.scale(IMG_Prebala_60, (IMG_Prebala_60.get_width() // 6, IMG_Prebala_60.get_height() // 6))
FondoMenu = pygame.transform.scale(IMG_FondoMenu, (Datos.PANT_ANCHO, Datos.PANT_ALTO))
FondoControles = pygame.transform.scale(IMG_fondo_controles, (Datos.PANT_ANCHO, Datos.PANT_ALTO))
FondoMenu_seleccion = pygame.transform.scale(IMG_Background_seleccion, (Datos.PANT_ANCHO, Datos.PANT_ALTO))

#Reescalado de imagenes de fondo para diferentes resoluciones 
Background800 = pygame.transform.scale(IMG_Background, (800, 800)) 
Background1080 = pygame.transform.scale(IMG_Background, (1920, 1080)) 
Background768 = pygame.transform.scale(IMG_Background, (1366, 768)) 
HUD800 = pygame.transform.scale(IMG_HUD, (800, 120)) 
HUD1080 = pygame.transform.scale(IMG_HUD, (1920, 120)) 
HUD768 = pygame.transform.scale(IMG_HUD, (1366, 120)) 
FondoMenu800 = pygame.transform.scale(IMG_FondoMenu, (800, 800)) 
FondoMenu1080 = pygame.transform.scale(IMG_FondoMenu, (1920, 1080)) 
FondoMenu768 = pygame.transform.scale(IMG_FondoMenu, (1366, 768)) 
FondoControles800 = pygame.transform.scale(IMG_fondo_controles, (800, 800)) 
FondoControles1080 = pygame.transform.scale(IMG_fondo_controles, (1920, 1080)) 
FondoControles768 = pygame.transform.scale(IMG_fondo_controles, (1366, 768)) 
FondoMenu_seleccion800 = pygame.transform.scale(IMG_Background_seleccion, (800, 800)) 
FondoMenu_seleccion1080 = pygame.transform.scale(IMG_Background_seleccion, (1920, 1080)) 
FondoMenu_seleccion768 = pygame.transform.scale(IMG_Background_seleccion, (1366, 768)) 
FondoBlanco = pygame.transform.scale(IMG_FondoBlanco, (Datos.PANT_ANCHO, Datos.PANT_ALTO))
FondoBlanco800 = pygame.transform.scale(IMG_FondoBlanco, (800, 800))
FondoBlanco1080 = pygame.transform.scale(IMG_FondoBlanco, (1920, 1080))
FondoBlanco768 = pygame.transform.scale(IMG_FondoBlanco, (1366, 768))