from joke_app import get_random_joke
import requests
from unittest.mock import patch

def test_get_random_joke_success():
    mock_response = {
        "setup": "Why don't scientists trust atoms?",
        "punchline": "Because they make up everything!"
    }

    with patch('requests.get') as mocked_get:
        mocked_get.return_value.status_code = 200
        mocked_get.return_value.json.return_value = mock_response

        joke = get_random_joke()
        assert "Why don't scientists trust atoms?" in joke
        assert "Because they make up everything!" in joke
