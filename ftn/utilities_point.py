__author__ = 'Giovanni'

import math

class FtnPoint(object):
    """
    La classe prende due liste di tre elementi ciascuno, ognuno rappresentante rispettivamente i 3 assi
    del punto e espone alcune proprieta' interessanti come (i valori sono tutti float) :

    distanza -> la distanza geometrica tra i due punti
    distanzaX, distanzaY, distanzaZ -> le distanze tra i due punti per singolo asse
    angoloXY -> l'angolo formato della retta che congiunge i due punti e una parallela all'asse delle x
                passante per il punto1

    """
    def __init__(self, punto1=[0,0,0], punto2=[0,0,0]):
        self.punto1 = punto1
        self.punto2 = punto2
        self.x1 = punto1[0]
        self.x2 = punto2[0]
        self.y1 = punto1[1]
        self.y2 = punto2[1]
        self.z1 = punto1[2]
        self.z2 = punto2[2]
        self.distanzaX = abs(punto2[0] - punto1[0])
        self.distanzaY = abs(punto2[1] - punto1[1])
        self.distanzaZ = abs(punto2[2] - punto1[2])
        self.distanza = math.sqrt(self.distanzaX ** 2 + self.distanzaY ** 2 + self.distanzaZ ** 2)
        if punto1 != punto2:
            self.angoloXY = self.calcolaAngoloXY()
        else:
            self.angoloXY = 0.0

    def calcolaAngoloXY(self):
        punto2Traslato = [self.x2 - self.x1, self.y2 - self.y1, self.z2 - self.z1]
        x2n = punto2Traslato[0] / self.distanza
        y2n = punto2Traslato[1] / self.distanza
        z2n = punto2Traslato[2] / self.distanza

        # casi di scuola

        if y2n == 0:
            if x2n > 0:
                return 0.0
            else:
                return 180.0
        if x2n == 0:
            if y2n > 0:
                return 90.0
            else:
                return 270.0

        # casi non di scuola

        if x2n > 0:
            if y2n > 0:
                return math.degrees(math.acos(x2n))
            else:
                return 360 - math.degrees(math.acos(x2n))
        else:
            if y2n > 0:
                return 180 - math.degrees(math.acos(-x2n))
            else:
                return 180 + math.degrees(math.acos(-x2n))
