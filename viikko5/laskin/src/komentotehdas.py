from komennot import Summa, Erotus, Nollaus, Kumoa

class Komentotehdas:
    def __init__(self, sovelluslogiikka, io):
        self._komennot = {
            1: Summa(sovelluslogiikka, io),
            2: Erotus(sovelluslogiikka, io),
            3: Nollaus(sovelluslogiikka),
            4: Kumoa()
        }
        

    def hae_komento(self, komento):
        if komento in self._komennot:
            return self._komennot[komento]
        return None