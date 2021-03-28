import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(400)

    def test_kassapaatteen_rahamaara_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_lounaita_myyty_oikein(self):
        self.assertEqual(self.kassapaate.edulliset + self.kassapaate.maukkaat, 0)

    def test_edullisen_kateisosto_toimii_myydyt_ok(self):
        self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)

    def test_edullisen_kateisoston_vaihtoraha_ok(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(300), 60)        

    def test_edullisen_kateisosto_toimii_ei_tarpeeksi_rahaa(self):
        self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_edullisen_kateisosto_toimii_ei_tarpeeksi_rahaa_vaihtorahat_ok(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(200), 200)

    def test_edullisen_kateisosto_toimii_ei_tarpeeksi_rahaa_myydyt_ok(self):
        self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassapaate.edulliset + self.kassapaate.maukkaat, 0)

    def test_maukkaan_kateisosto_toimii_myydyt_ok(self):
        self.kassapaate.syo_maukkaasti_kateisella(450)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)

    def test_maukkaan_kateisoston_vaihtoraha_ok(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(400), 0)        

    def test_maukkaan_kateisosto_toimii_ei_tarpeeksi_rahaa(self):
        self.kassapaate.syo_maukkaasti_kateisella(200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_maukkaan_kateisosto_toimii_ei_tarpeeksi_rahaa_vaihtorahat_ok(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(200), 200)

    def test_maukkaan_kateisosto_toimii_ei_tarpeeksi_rahaa_myydyt_ok(self):
        self.kassapaate.syo_maukkaasti_kateisella(200)
        self.assertEqual(self.kassapaate.edulliset + self.kassapaate.maukkaat, 0)

    def test_edullinen_korttiosto_toimii(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti), True)

    def test_edullinen_korttiosto_toimii(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(str(self.maksukortti), "saldo: 1.6")

    def test_korttiosto_myydyt_ok(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset + self.kassapaate.maukkaat, 1)

    def test_korttiosto_ei_tarpeeksi_rahaa_myydyt_ok(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset + self.kassapaate.maukkaat, 1)

    def test_korttiosto_ei_tarpeeksi_rahaa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti), False)

    def test_korttiosto_ei_tarpeeksi_rahaa_kortti_ok(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)        
        self.assertEqual(str(self.maksukortti), "saldo: 1.6")

    def test_kassan_rahamaara_korttiostossa_ok(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)      
##########
    def test_maukas_korttiosto_toimii(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti), True)

    def test_maukas_korttiosto_toimii(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(str(self.maksukortti), "saldo: 0.0")

    def test_maukas_korttiosto_myydyt_ok(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset + self.kassapaate.maukkaat, 1)

    def test_maukas_korttiosto_ei_tarpeeksi_rahaa_myydyt_ok(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset + self.kassapaate.maukkaat, 1)

    def test_korttiosto_ei_tarpeeksi_rahaa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti), False)

    def test_maukas_korttiosto_ei_tarpeeksi_rahaa_kortti_ok(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)      
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)        
        self.assertEqual(str(self.maksukortti), "saldo: 0.0")

    def test_kassan_rahamaara_maukkaassa_korttiostossa_ok(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)  
########        
    def test_rahan_lataus_kortille_ok(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 10)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100010)

    def test_rahan_lataus_kortille_ok(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 10)
        self.assertEqual(self.maksukortti.saldo, 410)

    def test_rahan_lataus_kortille_negatiivinen_summa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -10)
        self.assertEqual(self.maksukortti.saldo, 400)

    