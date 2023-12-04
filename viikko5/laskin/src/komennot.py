class Summa:
    def __init__(self, sovelluslogiikka, io):
        self._sovelluslogiikka = sovelluslogiikka
        self._io = io
        self._edellinen_arvo = 0
        
    def suorita(self):
        syote = int(self._io())
        self._edellinen_arvo = self._sovelluslogiikka.arvo()
        self._sovelluslogiikka.plus(syote)

    def kumoa(self):
        self._sovelluslogiikka.aseta_arvo(self._edellinen_arvo)

class Erotus:
    def __init__(self, sovelluslogiikka, io):
        self._sovelluslogiikka = sovelluslogiikka
        self._io = io
        self._edellinen_arvo = 0
        
    def suorita(self):        
        syote = int(self._io())
        self._edellinen_arvo = self._sovelluslogiikka.arvo()
        self._sovelluslogiikka.miinus(syote)        

    def kumoa(self):
        self._sovelluslogiikka.aseta_arvo(self._edellinen_arvo)

class Nollaus:
    def __init__(self, sovelluslogiikka):
        self._sovelluslogiikka = sovelluslogiikka
        self._edellinen_arvo = 0        
        
    def suorita(self):
        self._edellinen_arvo = self._sovelluslogiikka.arvo()
        self._sovelluslogiikka.nollaa()        

    def kumoa(self):
        self._sovelluslogiikka.aseta_arvo(self._edellinen_arvo)

class Kumoa:
        
    def suorita(self, komento):
        komento.kumoa()