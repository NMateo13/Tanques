

class Jugador:

    seleccionJugadores = [0, 0, 0, 0, 0, 0]
    jugadores= []
    color_jugadores = []

    def __init__(self):
        self.indice = None
        self.tanque = None
        self.color_tanque = None
        pass

    def crearJugador(indice):
        jugador = Jugador()
        jugador.indice = indice
        #el color del tanque depende del número de jugador siendo (0=verde, 1=rojo, 2=azul, 3=amarillo, 4=rosa, 5=celeste)
        jugador.color_tanque = indice+1
        Jugador.jugadores.append(jugador)

        

        



    