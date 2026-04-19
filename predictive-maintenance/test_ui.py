import requests

url = "http://127.0.0.1:8000/predict"

data = {
    "type": "H",
    "air_temperature": 320,
    "process_temperature": 340,
    "rotational_speed": 3000,
    "torque": 80,
    "tool_wear": 200
}

response = requests.post(url, json=data)

print("Prediction Result:")
print(response.json())