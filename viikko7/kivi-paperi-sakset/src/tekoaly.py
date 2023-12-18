class Tekoaly:
    def __init__(self):
        self._siirto = 0

    def anna_siirto(self):
        self._siirto += 1
        indeksi = self._siirto % 3

        siirrot = ["k", "p", "s"]
        return siirrot[indeksi]

    def aseta_siirto(self, siirto):
        # ei tehdä mitään
        pass
