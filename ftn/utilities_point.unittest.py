__author__ = 'Giovanni'

import unittest
from utilities_point import FtnPoint

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.punto = FtnPoint(punto1=[10,10,4], punto2=[20,-10,-3])
        self.puntoang000 = FtnPoint(punto2=[20, 0, 10])
        self.puntoang090 = FtnPoint(punto2=[0, 15.7, -2])
        self.puntoang180 = FtnPoint(punto2=[-15, 0, 11])
        self.puntoang270 = FtnPoint(punto1=[7, 3, -2], punto2=[7, -7, 5])
        self.puntocaso1 = FtnPoint(punto1=[7, 3, -2], punto2=[9, 5, 0])

    def test_distanzax(self):
        self.assertEqual(self.punto.distanzaX, 10)

    def test_distanzay(self):
        self.assertEqual(self.punto.distanzaY, 20)

    def test_distanzaz(self):
        self.assertEqual(self.punto.distanzaZ, 7)

    def test_distanzatotale(self):
        self.assertEqual(round(self.punto.distanza, 3), 23.431)

    def test_angolo000(self):
        self.assertEqual(self.puntoang000.angoloXY, 0.0)

    def test_angolo090(self):
        self.assertEqual(self.puntoang090.angoloXY, 90.0)

    def test_angolo180(self):
        self.assertEqual(self.puntoang180.angoloXY, 180.0)

    def test_angolo270(self):
        self.assertEqual(self.puntoang270.angoloXY, 270.0)

    def test_angoloCaso1(self):
        self.assertEqual(round(self.puntocaso1.angoloXY, 3), 54.736)

if __name__ == '__main__':
    unittest.main()
