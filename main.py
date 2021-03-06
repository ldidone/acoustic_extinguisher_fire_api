from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pandas as pd
import pickle

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

with open('decision_tree_1.sav', 'rb') as f:
    model = pickle.load(f)

STATUS = {
    0: 'NON-EXTINCTION',
    1: 'EXTINCTION',
}

class request_body(BaseModel):
    size: int
    fuel: str
    distance: int
    desibel: int
    airflow: float
    frequency: int

def get_data(data):
    size = data.size
    fuel = data.fuel
    distance = data.distance
    desibel = data.desibel
    airflow = data.airflow
    frequency = data.frequency

    data_list = list([size, fuel, distance, desibel, airflow, frequency])
    cols = list(['size', 'fuel', 'distance', 'desibel', 'airflow', 'frequency'])    
    x = pd.Series(data_list, index=cols)

    return x.to_frame().T

@app.post('/predict')
async def predict(data : request_body):
    x = get_data(data)

    prediction = model.predict(x)
    result = STATUS.get(prediction[0], 0)
    prediction_proba = model.predict_proba(x)
    probability_percentage = prediction_proba[0][prediction[0]] * 100

    return {"prediction": str(prediction[0]),
            "prediction_status": result,
            "probability_percentage": f"{probability_percentage}%" }
