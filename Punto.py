import math
#classe che definisce metodi dei punti 
class Punto:
    #variabili statiche, quindi il loro valore è uguale per tutte le istanze della classe punto
    baricentrox = 1
    baricentroy = 1
    #costruttore
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def distanza(self):
        return math.sqrt((self.x-Punto.baricentrox)**2 + (self.y-Punto.baricentroy)**2)

    def angolo(self):
        if self.distanza() == 0:
            return 0
        angolo = math.acos((self.x-Punto.baricentrox)/self.distanza())
        if self.y-Punto.baricentroy < 0:
            angolo = math.pi*2 - angolo
        return angolo

    def __str__(self):
        return str(self.x) + " " + str(self.y)

    def __lt__(self, other):
        if self.angolo() == other.angolo():
            return self.distanza() < other.distanza()
        return self.angolo() < other.angolo()