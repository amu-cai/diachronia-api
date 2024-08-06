import logging

import requests
from requests.adapters import HTTPAdapter
from requests.exceptions import HTTPError
from urllib3.util.retry import Retry


def __call_dariah_model_service(url: str, input_text: str) -> dict | None:
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
        response = session.post(f"{url}", json={"text": input_text})
        return response.json()
    except HTTPError as e:
        logging.error(f"HTTP error occurred: {e}")
    except requests.exceptions.RequestException as e:
        logging.error(f"Request error occurred: {e}")

    logging.error(f"Failed to call DARIAH model service after {retries.total} attempts")
    return
