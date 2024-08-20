import json
import logging
from enum import Enum
from functools import partial

from dariah.models.__call_dariah_model_service import __call_dariah_model_service


class Endpoints(Enum):
    dating: str = "https://diachronia.csi.wmi.amu.edu.pl/api/challenge/solve/datowanie"
    diachronic_normalizer: str = "https://diachronia.csi.wmi.amu.edu.pl/api/challenge/solve/normalizator-diachroniczny"
    synonyms: str = "https://diachronia.csi.wmi.amu.edu.pl/api/challenge/solve/synonimy"
    disambiguation: str = "https://diachronia.csi.wmi.amu.edu.pl/api/challenge/solve/ujednoznacznianie"


def create_function(name: str):
    func = partial(
        __call_dariah_model_service, url=str(Endpoints[name].value), respone_parser=get_response_parser(name)
    )
    func.__doc__ = f"Call DARIAH model service for {name}"
    return func


class SynonymsDariahJSONDecoder(json.JSONDecoder):
    def decode(self, data, **kwargs):
        try:
            data = data.strip().split("\t")
            data = [result.split("\n") for result in data]
            data = [{result[0]: result[1:][0].split(", ")} for result in data]
            return data
        except json.JSONDecodeError as e:
            logging.error(f"Invalid JSON received {e}")
            return


class UniversalDariahJSONDecoder(json.JSONDecoder):
    def decode(self, data, **kwargs):
        try:
            data = str(data).replace("/", r"\/")
            return data
        except json.JSONDecodeError as e:
            logging.error(f"Invalid JSON received {e}")
            return


def get_response_parser(name: str):
    match name:
        case "dating":
            return
        case "synonyms":
            return SynonymsDariahJSONDecoder
        case _:
            return UniversalDariahJSONDecoder


globals().update({name: create_function(name) for name in Endpoints.__members__})
