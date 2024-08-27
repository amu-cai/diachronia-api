from unittest.mock import MagicMock, patch

from requests.exceptions import Timeout

from dariah.models.__call_dariah_model_service import __call_dariah_model_service


def test_call_dariah_model_service_timeout():
    mock_response = MagicMock()
    mock_response.json.return_value = {"result": "success"}
    mock_response.status_code = 200

    with patch("dariah.models.__call_dariah_model_service.requests.post") as mock_post:
        mock_post.side_effect = Timeout

        result = __call_dariah_model_service("", "http://example.com/api/model", None)

        assert isinstance(result, type(None))


@patch("dariah.models.__call_dariah_model_service.requests.Session.post")
def test_call_dariah_model_service(mock_post):
    mock_post.return_value.json.return_value = {"result": "success"}

    result = __call_dariah_model_service("example text", "http://mock-endpoint.com", None)

    assert result == {"result": "success"}
