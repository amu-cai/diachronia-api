import logging
from typing import Any

import requests
from requests.adapters import HTTPAdapter
from requests.exceptions import HTTPError
from urllib3.util.retry import Retry


def __call_dariah_model_service(input_text: str, url: str, respone_parser: Any) -> Any:

    session = requests.Session()

    retries = Retry(
        total=5,
        backoff_factor=0.3,
        status_forcelist=[500, 502, 503, 504],
    )
    adapter = HTTPAdapter(max_retries=retries)
    session.mount("http://", adapter)
    session.mount("https://", adapter)
    try:
        response = session.post(url, json={"text": input_text})

        return response.json(cls=respone_parser)
    except HTTPError as e:
        logging.error(f"HTTP error occurred: {e}")
    except requests.exceptions.RequestException as e:
        logging.error(f"Request error occurred: {e}")

    logging.error(f"Failed to call DARIAH model service after {retries.total} attempts")
    return
