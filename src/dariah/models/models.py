from enum import Enum
from functools import partial

from dariah.models.__call_dariah_model_service import __call_dariah_model_service


class Endpoints(Enum):
    dating: str = "https://diachronia.csi.wmi.amu.edu.pl/api/challenge/solve/datowanie"
    diachronic_normalizer: str = "https://diachronia.csi.wmi.amu.edu.pl/api/challenge/solve/normalizator-diachroniczny"
    synonyms: str = "https://diachronia.csi.wmi.amu.edu.pl/api/challenge/solve/synonimy"
    disambiguation: str = "https://diachronia.csi.wmi.amu.edu.pl/api/challenge/solve/ujednoznacznianie"


def create_function(name: str):
    func = partial(__call_dariah_model_service, str(Endpoints[name].value))
    func.__doc__ = f"Call DARIAH model service for {name}"
    return func


globals().update({name: create_function(name) for name in Endpoints.__members__})
