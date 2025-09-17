# Mock Normalizer (FastAPI)
# run: uvicorn app:app --reload --port 8080
from fastapi import FastAPI
from pydantic import BaseModel
import json, sqlite3, time

app = FastAPI()

class PriceChange(BaseModel):
    sku: str
    location: str
    new_price: float
    currency: str = "USD"

@app.post("/price-change")
async def price_change(evt: PriceChange):
    # Instead of Kafka, write to a local file as 'bus' (demo-safe)
    with open("/tmp/bus_price.jsonl", "a") as f:
        f.write(json.dumps({"type":"price.event","ts":time.time(), **evt.dict()})+"\n")
    return {"status":"published"}
