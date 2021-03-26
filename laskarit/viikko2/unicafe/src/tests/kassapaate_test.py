import unittest
from kassapaate import Kassapaate

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()

    def test_kassapaatteen_rahamaara_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_lounaita_myyty_oikein(self):
        self.assertEqual(self.kassapaate.edulliset + self.kassapaate.maukkaat, 0)

    def test_edullisen_kateisosto_toimii(self):
        self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)

    def test_edullisen_kateisoston_vaihtoraha_ok(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(300), 60)        

    def test_edullisen_kateisosto_toimii_ei_tarpeeksi_rahaa(self):
        self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)


        
