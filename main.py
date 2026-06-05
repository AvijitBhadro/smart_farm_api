from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

data_store = {
    "temperature": 0.0,
    "humidity": 0.0,
    "soil": 0,
    "light": 0,
    "rain": 0,
    "soil_temp": 0.0
}


class SensorData(BaseModel):
    temperature: float
    humidity: float
    soil: int
    light: int
    rain: int
    soil_temp: float


@app.post("/data")
def receive_data(data: SensorData):

    data_store["temperature"] = data.temperature
    data_store["humidity"] = data.humidity
    data_store["soil"] = data.soil
    data_store["light"] = data.light
    data_store["rain"] = data.rain
    data_store["soil_temp"] = data.soil_temp

    return {"status": "ok"}


@app.get("/api")
def get_data():
    return data_store