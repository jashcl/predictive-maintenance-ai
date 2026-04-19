import requests

url = "http://127.0.0.1:8000/predict"

test_cases = [
    {"type": "L", "air_temperature": 298, "process_temperature": 308, "rotational_speed": 1500, "torque": 40, "tool_wear": 10},
    {"type": "M", "air_temperature": 310, "process_temperature": 320, "rotational_speed": 2000, "torque": 60, "tool_wear": 100},
    {"type": "H", "air_temperature": 330, "process_temperature": 350, "rotational_speed": 3000, "torque": 90, "tool_wear": 200}
]

for i, case in enumerate(test_cases):
    res = requests.post(url, json=case)
    print(f"\nTest Case {i+1}")
    print(res.json())