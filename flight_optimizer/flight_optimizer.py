import argparse
import httpx
from datetime import datetime, timedelta
from haversine import haversine
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
API_KEY = os.getenv("KIWI_API_KEY")
BASE_URL = "https://tequila-api.kiwi.com"


def get_city_code(city: str) -> str:
    """Fetch IATA code for a given city name using Kiwi Locations API."""
    url = f"{BASE_URL}/locations/query"
    headers = {"apikey": API_KEY}
    params = {"term": city, "location_types": "city", "limit": 1}
    r = httpx.get(url, headers=headers, params=params)
    r.raise_for_status()
    data = r.json()
    if not data["locations"]:
        raise ValueError(f"City not found: {city}")
    return data["locations"][0]["code"]


def get_best_flight(origin: str, destinations: list[str]) -> dict:
    """Return best destination and $/km value from origin to destinations."""
    best = None
    today = datetime.utcnow()
    tomorrow = today + timedelta(days=1)

    for dest in destinations:
        try:
            origin_code = get_city_code(origin)
            dest_code = get_city_code(dest)

            url = f"{BASE_URL}/v2/search"
            headers = {"apikey": API_KEY}
            params = {
                "fly_from": origin_code,
                "fly_to": dest_code,
                "date_from": today.strftime("%d/%m/%Y"),
                "date_to": tomorrow.strftime("%d/%m/%Y"),
                "adults": 1,
                "curr": "USD",
                "limit": 1,
                "one_for_city": 1,
            }

            r = httpx.get(url, headers=headers, params=params)
            r.raise_for_status()
            data = r.json()

            if not data.get("data"):
                continue

            flight = data["data"][0]
            price = flight["price"]
            distance = flight["distance"]
            value = price / distance  # USD per km

            if best is None or value < best["value"]:
                best = {
                    "destination": dest,
                    "price": price,
                    "distance": distance,
                    "value": value,
                }
        except Exception as e:
            print(f"Error fetching flight for {dest}: {e}")

    if not best:
        raise ValueError("No flights found for given destinations.")
    return best


def cli():
    parser = argparse.ArgumentParser(description="Find cheapest flight per km")
    parser.add_argument("--from", dest="origin", required=True, help="Departure city")
    parser.add_argument("--to", dest="destinations", nargs="+", required=True, help="Destination cities")
    args = parser.parse_args()

    best = get_best_flight(args.origin, args.destinations)
    print(f"Best destination: {best['destination']}")
    print(f"Price: ${best['price']} for {best['distance']} km")
    print(f"Value: ${best['value']:.2f}/km")


if __name__ == "__main__":
    cli()