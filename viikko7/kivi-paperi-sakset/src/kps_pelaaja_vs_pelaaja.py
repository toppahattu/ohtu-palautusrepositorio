from kivi_paperi_sakset import KiviPaperiSakset


class KPSPelaajaVsPelaaja(KiviPaperiSakset):    
    def _toisen_siirto(self, _):
        return input("Toisen pelaajan siirto: ")