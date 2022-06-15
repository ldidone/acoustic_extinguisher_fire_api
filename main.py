from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import pickle

app = FastAPI()
model = pickle.load(open('model\decision_tree_1.sav', 'rb'))
STATUS = {
    0: 'NON-EXTINCTION',
    1: 'EXTINTION',
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

    return {"prediction": result,
            "probability_percentage": f"{probability_percentage}%" }
