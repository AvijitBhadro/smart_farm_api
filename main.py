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

# store latest sensor data
data_store = {
    "temperature": 0.0,
    "humidity": 0.0
    # "soil": 0,
    # "light": 0   # NEW
}

# data model
class SensorData(BaseModel):
    temperature: float
    humidity: float
    # soil: int
    # light: int   # NEW



@app.post("/data")
def receive_data(data: SensorData):
    data_store["temperature"] = data.temperature
    data_store["humidity"] = data.humidity
    # data_store["soil"] = data.soil
    # data_store["light"] = data.light  # NEW
    return {"status": "ok"}

@app.get("/")
def root():
    return {"message": "API is running"}

@app.get("/api")
def get_data():
    return data_store