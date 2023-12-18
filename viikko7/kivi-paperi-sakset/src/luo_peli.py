from enum import Enum
from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly
from kps_parempi_tekoaly import KPSParempiTekoaly


class Peli(Enum):
    PELAAJA_VS_PELAAJA = "a"
    TEKOALY_VS_PELAAJA = "b"
    PAREMPI_TEKOALY_VS_PELAAJA = "c"

class LuoPeli:
    def luo_peli(self, peli):
        match peli:
            case Peli.PELAAJA_VS_PELAAJA.value:
                return KPSPelaajaVsPelaaja()
            case Peli.TEKOALY_VS_PELAAJA.value:
                return KPSTekoaly()
            case Peli.PAREMPI_TEKOALY_VS_PELAAJA.value:
                return KPSParempiTekoaly()
            case _:
                return None