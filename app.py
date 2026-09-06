from fastapi import FastAPI
from pydantic import BaseModel
import os

app = FastAPI()

APP_NAME = "student-ml-api"

def get_version():
    version_file = os.path.join(os.path.dirname(__file__), "VERSION")
    try:
        with open(version_file, "r") as f:
            return f.read().strip()
    except FileNotFoundError:
        return "0.0.0"

APP_VERSION = get_version()


class PredictRequest(BaseModel):
    value: float


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "application": APP_NAME,
        "version": APP_VERSION
    }


@app.post("/predict")
def predict(request: PredictRequest):
    prediction = request.value * 2
    return {
        "input": request.value,
        "prediction": prediction
    }