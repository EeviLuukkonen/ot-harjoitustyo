import unittest
from kassapaate import Kassapaate

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()

    def test_kassapaatteen_rahamaara_oikein(self):
        self.assertNotEqual(self.kassapaate.kassassa_rahaa, 1000)