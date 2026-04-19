from fastapi import FastAPI
import joblib
import numpy as np

app = FastAPI()

# Load model
model = joblib.load("model.pkl")

# Encoding
type_map = {"L": 0, "M": 1, "H": 2}

@app.get("/")
def home():
    return {"message": "Predictive Maintenance API is running"}

@app.post("/predict")
def predict(data: dict):

    # Encode input
    t = type_map[data["type"]]

    air = data["air_temperature"]
    process = data["process_temperature"]
    speed = data["rotational_speed"]
    torque = data["torque"]
    wear = data["tool_wear"]

    # Feature engineering (MUST match training)
    stress_index = torque * speed
    temp_diff = process - air

    features = np.array([[
        t,
        air,
        process,
        speed,
        torque,
        wear,
        stress_index,
        temp_diff
    ]])

    # Prediction
    risk = model.predict_proba(features)[0][1]

    # Logic
    if risk > 0.7:
        status = "HIGH RISK"
        recommendation = "Immediate inspection required"
    elif risk > 0.3:
        status = "MEDIUM RISK"
        recommendation = "Schedule maintenance"
    else:
        status = "LOW RISK"
        recommendation = "Machine operating normally"

    return {
        "failure_risk": round(float(risk), 3),
        "confidence": f"{round(risk * 100, 2)}%",
        "status": status,
        "recommendation": recommendation
    }