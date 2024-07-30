from enum import Enum


class Endpoints(Enum):
    dating: str = "https://diachronia.csi.wmi.amu.edu.pl/api/challenge/solve/datowanie"
    diachronic_normalizer: str = "https://diachronia.csi.wmi.amu.edu.pl/api/challenge/solve/normalizator-diachroniczny"
    synonyms: str = "https://diachronia.csi.wmi.amu.edu.pl/api/challenge/solve/synonimy"
    disambiguation: str = "https://diachronia.csi.wmi.amu.edu.pl/api/challenge/solve/ujednoznacznianie"
