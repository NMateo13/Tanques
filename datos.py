bala_tanque1 = None
bala_tanque2 = None
centroExplosion = []
radioExplosion = 75
arrayaux = []
arrayaux2 = []
aux_x=0
aux_y=0
tipo_bala1 = 1
tipo_bala2 = 1
turno1 = True
turno2 = False
extremo_canonx_1 = 0
extremo_canony_1 = 0
extremo_canonx_2 = 0
extremo_canony_2 = 0
mostrar_altura1 = False
mostrar_altura2 = False    

# Variables y Constantes
FPS = 60
medidaHUD = 120
gravedad = 9.8
PANT_ANCHO = 1200
PANT_ALTO = 600
cantidad_balas1 = 0
cantidad_balas2 = 0
altura_maxima = 0
distancia_maxima = 0
volumen = 0.25
nTurnos = 1
reiniciar = False
bandera_tanque = True
bala_tanque1 = None
bala_tanque2 = None

#arraylist hasta 150, 0 = 30, 61 en total
ang_tank = [210,215,220,225,230,235,240,245,250,255,260,265,270,275,280,285,290,295,300,305,310,315,320,325,330,335,340,345,350,355,0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100,105,110,115,120,125,130,135,140,145,150,155,160,165,170,175,180,185,190,195,200,205]

# Colores
WHITE = (225, 225, 225)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 153, 0)
BLUE = (0,0,255)
BROWN = (139, 69, 19)


def reiniciar_datos():
    global bala_tanque1, bala_tanque2
    global centroExplosion, radioExplosion
    global arrayaux ,arrayaux2 ,aux_x ,aux_y
    global tipo_bala1,tipo_bala2, turno1,turno2
    global extremo_canonx_1, extremo_canony_1, extremo_canonx_2,extremo_canony_2
    global mostrar_altura1, mostrar_altura2
    bala_tanque1 = None
    bala_tanque2 = None
    centroExplosion = []
    radioExplosion = 75
    arrayaux = []
    arrayaux2 = []
    aux_x=0
    aux_y=0
    tipo_bala1 = 1
    tipo_bala2 = 1
    turno1 = True
    turno2 = False
    extremo_canonx_1 = 0
    extremo_canony_1 = 0
    extremo_canonx_2 = 0
    extremo_canony_2 = 0
    mostrar_altura1 = False
    mostrar_altura2 = False
    



    