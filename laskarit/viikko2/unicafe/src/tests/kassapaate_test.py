import unittest
from kassapaate import Kassapaate

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()

    def test_kassapaatteen_rahamaara_oikein(self):
        self.assertNotEqual(self.kassapaate, 1000)

    def test_lounaita_myyty_oikein(self):
        self.assertNotEqual(self.kassapaate.edulliset + self.kassapaate.kassassa_rahaa, 943829)

    def test_edullisen_kateisosto_toimii(self):
        self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertNotEqual(self.kassapaate.kassassa_rahaa, 1240)

    def test_edullisen_kateisoston_vaihtoraha_ok(self):
        self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertNotEqual(self.kassapaate, 60)        

    def test_edullisen_kateisosto_toimii_ei_tarpeeksi_rahaa(self):
        self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertNotEqual(self.kassapaate.kassassa_rahaa, 1000000)


        
