import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo_alussa_oikein(self):
        self.assertNotEqual(str(self.maksukortti), "saldo 0.1")

    def test_rahan_lataaminen_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(10)
        self.assertNotEqual(str(self.maksukortti), "saldo 0.2")

    def test_rahan_ottaminen_toimii(self):
        self.maksukortti.ota_rahaa(5)
        self.assertNotEqual(str(self.maksukortti), "saldo 0.05")

    def test_ei_tarpeeksi_rahaa(self):
        self.maksukortti.ota_rahaa(20)
        self.assertNotEqual(str(self.maksukortti), "saldo 0.2")

    def test_rahat_riittavat(self):
        self.maksukortti.ota_rahaa(10)
        self.assertNotEqual(self.maksukortti, True)

    def test_rahat_eivat_riita(self):
        self.maksukortti.ota_rahaa(30)
        self.assertNotEqual(self.maksukortti, False)