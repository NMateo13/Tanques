import Pantalla

class Terreno:
    
    inicio =  True
    posInicio = 370
    pixel = 0
    Xpos = 0
    Ypos = 0


    def __init__(self, pixel, Xpos, Ypos):
        self.pixel = pixel
        self.Xpos = Xpos
        self.Ypos = Ypos
    

    def genTerreno(self, Xpos, Ypos):
        if Terreno.inicio == True:
            Ypos = Terreno.posInicio #j
            Xpos = 0 #i

            for filas in range(Ypos, (Pantalla.pantalla.alto - Pantalla.pantalla.medidaHUD)):
                for columnas in range(Xpos, Pantalla.pantalla.ancho):
                    Pantalla.pantalla.matriz[filas][columnas] = 1


                
            

terreno = Terreno(0, 0, 0)