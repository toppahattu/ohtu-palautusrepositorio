import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
from viitegeneraattori import Viitegeneraattori
from varasto import Varasto
from tuote import Tuote

class TestKauppa(unittest.TestCase):
    def setUp(self):
        varasto_mock = Mock()

        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10
            elif tuote_id == 2:
                return 15
            return 0

        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "mehu", 5)
            elif tuote_id == 2:
                return Tuote(2, "limppari", 6)
            elif tuote_id == 3:
                return Tuote(3, "vesi", 3)
            return None

        varasto_mock.saldo.side_effect = varasto_saldo
        varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        self.pankki_mock = Mock()
        self.viitegeneraattori_mock = Mock(wraps=Viitegeneraattori())
        self.viitegeneraattori_mock.uusi.return_value = 13

        self.kauppa = Kauppa(varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)

    def test_ostoksen_paatyttya_pankkia_kutsutaan_oikeilla_parametreilla(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("teppo", "1234-5678")
        self.pankki_mock.tilisiirto.assert_called_with("teppo", 13, "1234-5678", "33333-44455", 5)

    def test_kaksi_eri_tuotetta_ostoksena_pankkia_kutsutaan_oikeilla_parametreilla(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("teppo", "1234-5678")
        self.pankki_mock.tilisiirto.assert_called_with("teppo", 13, "1234-5678", "33333-44455", 11)

    def test_kaksi_samaa_tuotetta_ostoksena_pankkia_kutsutaan_oikeilla_parametreilla(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("teppo", "1234-5678")
        self.pankki_mock.tilisiirto.assert_called_with("teppo", 13, "1234-5678", "33333-44455", 10)

    def test_kaksi_tuotetta_ostoksena_joista_toinen_loppu_pankkia_kutsutaan_oikeilla_parametreilla(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(3)
        self.kauppa.tilimaksu("teppo", "1234-5678")
        self.pankki_mock.tilisiirto.assert_called_with("teppo", 13, "1234-5678", "33333-44455", 5)

    def test_jokainen_asiointi_kaupassa_aloitetaan_tyhjalla_ostoskorilla(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("teppo", "1234-5678")
        self.pankki_mock.tilisiirto.assert_called_with(ANY, ANY, ANY, ANY, 5)

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("teppo", "1234-5678")
        self.pankki_mock.tilisiirto.assert_called_with(ANY, ANY, ANY, ANY, 6)

    def test_jokainen_ostos_saa_oman_viitenumeron(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("teppo", "1234-5678")
        self.assertEqual(self.viitegeneraattori_mock.uusi.call_count, 1)

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("teppo", "1234-5678")
        self.assertEqual(self.viitegeneraattori_mock.uusi.call_count, 2)

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("teppo", "1234-5678")
        self.assertEqual(self.viitegeneraattori_mock.uusi.call_count, 3)

    def test_tuotteen_ostoskorista_poistamisen_jalkeen_pankkia_kutsutaan_oikeilla_parametreilla(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.poista_korista(2)
        self.kauppa.tilimaksu("teppo", "1234-5678")
        self.pankki_mock.tilisiirto.assert_called_with("teppo", 13, "1234-5678", "33333-44455", 5)
