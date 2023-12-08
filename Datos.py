#Variables de juego
bala_tanque = None
mostrar_altura = 0
tecla_espacio_presionada = False
tiempo_transcurrido = 0
numero_jugadores = 0
num_partidas = 1
partida_actual = 1
anima_quedan_balas = False
sube_texto = 0
turnos = 0
rondas = 1
tanque_sin_balas = 0

# Variables y Constantes
FPS = 60
medidaHUD = 120
gravedad = 9.8
PANT_ANCHO = 1200
PANT_ALTO = 600
altura_maxima = 0
distancia_maxima = 0
volumen = 0.25
reiniciar = False
bandera_tanque = True
lista_cuadrar_jugadores_texto_x = [10, 3, 1.764]
lista_cuadrar_jugadores_texto_y = [3.5, 1.457]
Tanque_sele_ancho ={
    1: 9.5,
    2: 2.95,
    3: 1.75,
    4: 9.5,
    5: 2.95,
    6: 1.75
}
Tanque_sele_alto ={
    1: 6.5,
    2: 6.5,
    3: 6.5,
    4: 1.8,
    5: 1.8,
    6: 1.8
}

#arraylist hasta 150, 0 = 30, 61 en total
ang_tank = [210,215,220,225,230,235,240,245,250,255,260,265,270,275,280,285,290,295,300,305,310,315,320,325,330,335,340,345,350,355,0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100,105,110,115,120,125,130,135,140,145,150,155,160,165,170,175,180,185,190,195,200,205]

# Colores
WHITE = (225, 225, 225)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0,0,255)
BROWN = (139, 69, 19)
GREY = (128, 128, 128)
PURPLE = (40, 5, 107)


def reiniciar_datos():
    global mostrar_altura, tecla_espacio_presionada, tiempo_transcurrido, turnos, rondas, bala_tanque, tanque_sin_balas
    
    mostrar_altura = False
    tecla_espacio_presionada = False
    tiempo_transcurrido = 0
    turnos = 0
    rondas = 1
    bala_tanque = None
    tanque_sin_balas = 0



    
