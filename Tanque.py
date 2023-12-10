import pygame, Datos, Pantalla
import random
from Bala import Bala

class Tanque:

    tanques = []

    def __init__(self, x, y, num, indice, color):
        self.x = x
        self.y = y
        self.ancho = 60
        self.altura = 10 
        self.num = num
        self.vida = 100 # vida tanque
        self.cantBala60mm = 0 #cantidad de balas 
        self.cantBala80mm = 0
        self.cantBala105mm = 0
        self.Bala60mm = 30 # daño de las balas
        self.Bala80mm = 40
        self.Bala105mm = 50
        self.indice = indice
        self.pivote = []
        self.extremo_canonx = 0
        self.extremo_canony = 0
        #el color del tanque depende del número de jugador siendo (1=verde, 2=rojo, 3=azul, 4=amarillo, 5=rosa, 6=celeste)
        self.color = color
        self.angulo = 30
        self.velocidad = 50
        self.tipo_bala = 1
        self.radioExplosion = 75
        self.creditos = 10000
        self.mostrar_datos = False
        self.esIA = False
        self.sin_balas = False
        self.kills = 0
        self.muertes = 0
        self.suicidios = 0

    def dibujar(self, screen):
        pygame.draw.rect(screen, Datos.RED, (self.x, self.y, self.ancho, self.altura))

    def disparar(self, pos_inicial_x, pos_inicial_y, angulo, velocidad_inicial, tiempo, screen, color, tipo_bala):
        bala = Bala(pos_inicial_x, pos_inicial_y, angulo, velocidad_inicial, tipo_bala  )
        if tipo_bala == 1:
            bala.verificacion(tiempo, screen, color)
            self.cantBala105mm -= 1
            return bala
        elif tipo_bala == 2:
            bala.verificacion(tiempo, screen, color)
            self.cantBala80mm -= 1
            return bala
        elif tipo_bala == 3:
            bala.verificacion(tiempo, screen, color)
            self.cantBala60mm -= 1
            return bala

    def ia(tanque):
        #61 valores disponibles en el arrayist ang_tank
        #numero aleatorio entre 0 y 60
        angulo = random.randint(0, 60)
        #Dependiendo del tamaño de la pantalla, la velocidad de la bala será mayor o menor
        if Datos.PANT_ALTO == 600: #Default 1200x600
            velocidad = random.randint(0, 150)
        elif Datos.PANT_ALTO == 1080: #1920x1080
            velocidad = random.randint(0, 300)
        elif Datos.PANT_ALTO == 800: #800x800
            velocidad = random.randint(0, 100)
        elif Datos.PANT_ALTO == 768: #1366x768
            velocidad = random.randint(0, 200)
        #Tipo de bala aleatoria entre 1 y 3, si no hay balas de ese tipo, se elige otro tipo incluyendo si no hay 2 tipos de balas
        tipo_bala = random.randint(1, 3)
        if tipo_bala == 1:
            if tanque.cantBala105mm == 0:
                if tanque.cantBala80mm == 0:
                    tipo_bala = 3
                else:
                    tipo_bala = 2
        elif tipo_bala == 2:
            if tanque.cantBala80mm == 0:
                if tanque.cantBala105mm == 0:
                    tipo_bala = 3
                else:
                    tipo_bala = 1
        elif tipo_bala == 3:
            if tanque.cantBala60mm == 0:
                if tanque.cantBala105mm == 0:
                    tipo_bala = 2
                else:
                    tipo_bala = 1


        return angulo, velocidad, tipo_bala
    

    def creaTanques(jugadores):
        
        for indice, jugador in enumerate(jugadores):
            jugadorActual = jugadores[indice]
            tanque = Tanque(0, 0, jugadorActual.indice+1, 0, jugadorActual.color_tanque)
            tanque.esIA = jugadorActual.IA
            Tanque.tanques.append(tanque)

    def spawnTanques(terreno):

            Xcoordenadas = []

            for indice,tanque in enumerate(Tanque.tanques):
            
                tanque.x = random.randint(0, Datos.PANT_ANCHO - 50)
                Xcoordenadas.append(tanque.x)

                if indice > 0:

                    reset_for = False
                    while True:

                        for coordenadas in Xcoordenadas:

                            if coordenadas == tanque.x:
                                break
                            else:
                                rango = list(range(coordenadas-100, coordenadas+100))
                                Datos.coordenadaCorrecta = True

                                while Datos.coordenadaCorrecta:

                                    for i in rango:
                                        if tanque.x == i:
                                            tanque.x = random.randint(0, Datos.PANT_ANCHO - 50)
                                            Xcoordenadas[indice] = tanque.x
                                            reset_for = True
                                            break
                                        else:
                                            Datos.coordenadaCorrecta = False

                                    if reset_for:
                                            break
                                if reset_for:
                                    break
                        if reset_for:
                            reset_for = False
                            continue
                        break

                tanque.indice = tanque.x
                tanque.y = terreno.alto - terreno.terreno[indice] - 26

    def acomodarTanque(screen, terreno):
        for indice, tanque in enumerate(Tanque.tanques):
            if Tanque.tanques[indice].y != (terreno.alto - terreno.terreno[Tanque.tanques[indice].indice] - 16):
                Tanque.tanques[indice].y = terreno.alto - terreno.terreno[Tanque.tanques[indice].indice] - 16
                if Tanque.tanques[indice].y >= 465:
                    Tanque.tanques[indice].y = 465
                Tanque.tanques[indice].pivote = [Tanque.tanques[indice].x+21, Tanque.tanques[indice].y-5]
                Tanque.tanques[indice].extremo_canonx, Tanque.tanques[indice].extremo_canony = Pantalla.pantalla.prerotate(screen, Tanque.tanques[indice].color, Datos.ang_tank[0], Tanque.tanques[indice].pivote)