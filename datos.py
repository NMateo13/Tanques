import os, pygame

# Imagenes
IMG_Tanque1 = pygame.image.load(os.path.join("Assets", "Tanque1.png"))
IMG_Tanque2 = pygame.image.load(os.path.join("Assets", "Tanque2.png"))
IMG_Tanque3 = pygame.image.load(os.path.join("Assets", "Tanque3.png"))
IMG_Tanque4 = pygame.image.load(os.path.join("Assets", "Tanque4.png"))
IMG_Canon1 = pygame.image.load(os.path.join("Assets", "canon1.png"))
IMG_Canon2 = pygame.image.load(os.path.join("Assets", "canon2.png"))
IMG_Canon3 = pygame.image.load(os.path.join("Assets", "canon3.png"))
IMG_Canon4 = pygame.image.load(os.path.join("Assets", "canon4.png"))
IMG_Background = pygame.image.load(os.path.join("Assets", "Background.png"))
IMG_HUD = pygame.image.load(os.path.join("Assets", "hud_bg.png"))
IMG_Explosion = pygame.image.load(os.path.join("Assets", "boom.png"))
IMG_Bala = pygame.image.load(os.path.join("Assets", "bala105.png"))
IMG_Bala60 = pygame.image.load(os.path.join("Assets", "bala60.png"))
IMG_Bala80 = pygame.image.load(os.path.join("Assets", "bala80.png"))
IMG_Bala105 = pygame.image.load(os.path.join("Assets", "bala105.png"))

#Reescalado de imagenes
Tanque1 = pygame.transform.scale(IMG_Tanque1, (IMG_Tanque1.get_width() // 4, IMG_Tanque1.get_height() // 4))
Tanque2 = pygame.transform.scale(IMG_Tanque2, (IMG_Tanque2.get_width() // 4, IMG_Tanque2.get_height() // 4))
Canon1 = pygame.transform.scale(IMG_Canon1, (IMG_Canon1.get_width() // 4, IMG_Canon1.get_height() // 4))
Canon2 = pygame.transform.scale(IMG_Canon2, (IMG_Canon2.get_width() // 4, IMG_Canon2.get_height() // 4))
Background = pygame.transform.scale(IMG_Background, (1200, 540))
HUD = pygame.transform.scale(IMG_HUD, (1200, 120))    
Tanque1_HUD = pygame.transform.scale(IMG_Tanque1, (IMG_Tanque1.get_width() // 2, IMG_Tanque1.get_height() // 2))
Tanque2_HUD = pygame.transform.scale(IMG_Tanque2, (IMG_Tanque2.get_width() // 2, IMG_Tanque2.get_height() // 2))
Bala105 = pygame.transform.scale(IMG_Bala105, (IMG_Bala105.get_width() // 1.5, IMG_Bala105.get_height() // 1.5))
Bala80 = pygame.transform.scale(IMG_Bala80, (IMG_Bala80.get_width() // 1.75, IMG_Bala80.get_height() // 1.75))
Bala60 = pygame.transform.scale(IMG_Bala60, (IMG_Bala60.get_width() // 2, IMG_Bala60.get_height() // 2))
Explosion = pygame.transform.scale(IMG_Explosion, (IMG_Explosion.get_width() // 4, IMG_Explosion.get_height() // 4))

# Variables y Constantes
FPS = 60
medidaHUD = 120
gravedad = 9.8

#arraylist hasta 150, 0 = 30, 61 en total
ang_tank = [210,215,220,225,230,235,240,245,250,255,260,265,270,275,280,285,290,295,300,305,310,315,320,325,330,335,340,345,350,355,0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100,105,110,115,120,125,130,135,140,145,150,155,160,165,170,175,180]


# Colores
WHITE = (225, 225, 225)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 153, 0)
BLUE = (0,0,255)
BROWN = (139, 69, 19)