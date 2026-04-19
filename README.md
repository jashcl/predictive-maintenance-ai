# ⚙️ Predictive Maintenance AI System

![Python](https://img.shields.io/badge/Python-3.10-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-red)
![Machine Learning](https://img.shields.io/badge/ML-RandomForest-orange)
![Status](https://img.shields.io/badge/Status-Active-success)

---

## 🚀 Overview

A full-stack **AI-powered Predictive Maintenance System** that analyzes industrial sensor data to predict machine failure risk in real-time.

The system combines:
- Machine Learning for prediction
- FastAPI for scalable inference
- Streamlit for interactive visualization
- Feature engineering for industrial realism

---

## 🎯 Problem Statement

Industrial machines often fail without warning, causing:

- ⚠️ Downtime losses  
- 💰 High maintenance costs  
- ⏳ Production delays  

This system predicts failure **before it happens**, enabling proactive maintenance.

---

## 🧠 Key Features

- 🔮 Real-time failure risk prediction
- ⚙️ Feature engineering (Stress Index, Temperature Delta)
- 📊 Interactive dashboard (Sliders + Manual Input)
- 🧠 Model explainability (Feature importance)
- ⚡ REST API for ML inference
- 📉 Risk classification (Low / Medium / High)

---

## 🏗️ System Architecture


Sensor Data → Feature Engineering → ML Model → FastAPI → Streamlit Dashboard → User Insights


---

## 🧰 Tech Stack

### Backend
- FastAPI
- Uvicorn

### Machine Learning
- Scikit-learn
- Pandas
- NumPy
- Joblib

### Frontend
- Streamlit

---

## 📊 Model Inputs

- Machine Type (L / M / H)
- Air Temperature
- Process Temperature
- Rotational Speed
- Torque
- Tool Wear

---

## 🧪 Engineered Features

- Stress Index = Torque × Rotational Speed
- Temperature Difference = Process − Air

These features improve real-world industrial accuracy.

---

## 📤 API Response

```json
{
  "failure_risk": 0.73,
  "confidence": "73%",
  "status": "HIGH RISK",
  "recommendation": "Immediate inspection required"
}
🖥️ UI Features (Streamlit Dashboard)
🎛️ Input Modes
Slider-based simulation mode
Manual input mode
📊 Output
Risk score
Confidence percentage
Maintenance recommendation
📈 Explainability
Feature importance visualization
▶️ How to Run Locally
1. Install dependencies
pip install -r requirements.txt
2. Start backend
uvicorn app:app --reload
3. Start frontend
streamlit run dashboard.py
📁 Project Structure
predictive-maintenance/
│
├── app.py
├── dashboard.py
├── model.pkl
├── feature_importance.pkl
├── data.csv
├── requirements.txt
└── README.md
📌 What Makes This Project Strong

✔ End-to-end ML pipeline
✔ Production-style API design
✔ Interactive frontend dashboard
✔ Real-world industrial use case
✔ Feature engineering included
✔ Explainable AI output

🚀 Future Improvements
Deploy on cloud (Render + Streamlit Cloud)
Add real-time IoT sensor streaming
Database logging for machine history
Authentication system for users
Model upgrade with deep learning
👨‍💻 Author

Jash Shah

GitHub: https://github.com/jashcl
LinkedIn: https://www.linkedin.com/in/jash-shah-7076b91b3/
⭐ Summary

This project demonstrates an industry-grade predictive maintenance system combining machine learning, backend APIs, and interactive UI into a deployable product.
