__author__ = 'Giovanni'

import math

class DPoint(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def distanceTo(self, punto):
        quadrati = (self.x - punto.x) ** 2 + (self.y - punto.y) ** 2 + (self.z - punto.z) ** 2
        return math.sqrt(quadrati)

    def clone(self):
        clonato = DPoint(self.x, self.y, self.z)
        return clonato

    def shift(self, movx=0, movy=0, movz=0):
        self.x += movx
        self.y += movy
        self.z += movz


