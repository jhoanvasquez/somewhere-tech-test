from fastapi import FastAPI, Query
from flight_optimizer import get_best_flight

app = FastAPI(title="Flight Optimizer", version="1.0")


@app.get("/optimize-flight")
async def optimize_flight(
    origin: str,
    destinations: list[str] = Query(..., description="List of destination cities")
):
    try:
        best = get_best_flight(origin, destinations)
        return {
            "best_destination": best["destination"],
            "price": best["price"],
            "distance": best["distance"],
            "value_usd_per_km": round(best["value"], 2),
        }
    except Exception as e:
        return {"error": str(e)}
