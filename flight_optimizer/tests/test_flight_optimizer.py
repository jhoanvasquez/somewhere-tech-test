import pytest
import httpx
from flight_optimizer import get_best_flight

class MockResponse:
    def __init__(self, json_data, status_code=200):
        self._json = json_data
        self.status_code = status_code

    def raise_for_status(self):
        if self.status_code >= 400:
            raise httpx.HTTPStatusError("Error", request=None, response=None)

    def json(self):
        return self._json


def mock_get_city_code(city: str) -> str:
    """Fake IATA codes for tests."""
    codes = {"London": "LON", "Paris": "PAR", "Berlin": "BER"}
    return codes.get(city, "XXX")


def mock_httpx_get(url, headers=None, params=None):
    """Fake Kiwi API responses for tests."""
    if "locations/query" in url:
        # Fake locations API response
        return MockResponse({
            "locations": [{"code": params["term"].upper()}]
        })

    if "v2/search" in url:
        if params["fly_to"] == "PAR":
            return MockResponse({
                "data": [{"price": 100, "distance": 1000}]  # $0.1/km
            })
        elif params["fly_to"] == "BER":
            return MockResponse({
                "data": [{"price": 200, "distance": 1000}]  # $0.2/km
            })
        else:
            return MockResponse({"data": []})

    return MockResponse({}, 404)


def test_best_flight(monkeypatch):
    # Patch functions
    monkeypatch.setattr("flight_optimizer.get_city_code", mock_get_city_code)
    monkeypatch.setattr("httpx.get", mock_httpx_get)

    result = get_best_flight("London", ["Paris", "Berlin"])

    assert result["destination"] == "Paris"
    assert result["price"] == 100
    assert result["distance"] == 1000
    assert round(result["value"], 2) == 0.1


def test_no_flights(monkeypatch):
    monkeypatch.setattr("flight_optimizer.get_city_code", mock_get_city_code)
    def empty_response(url, headers=None, params=None):
        return MockResponse({"data": []})
    monkeypatch.setattr("httpx.get", empty_response)

    with pytest.raises(ValueError, match="No flights found"):
        get_best_flight("London", ["Paris"])
