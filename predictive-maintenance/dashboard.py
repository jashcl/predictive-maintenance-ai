import streamlit as st
import requests
import joblib
import pandas as pd

st.set_page_config(page_title="Predictive Maintenance AI", layout="centered")

st.title("⚙️ Predictive Maintenance System")
st.write("Use sliders OR manual input to test machine failure risk")

# ---------------- MODE SELECT ----------------
mode = st.radio("Input Mode", ["Sliders", "Manual Input"])

# ---------------- INPUTS ----------------

machine_type = st.selectbox("Machine Type", ["L", "M", "H"])

if mode == "Sliders":

    air_temp = st.slider("Air Temperature", 290.0, 320.0, 300.0)
    process_temp = st.slider("Process Temperature", 300.0, 340.0, 310.0)
    speed = st.slider("Rotational Speed", 1000, 3000, 1500)
    torque = st.slider("Torque", 10, 100, 50)
    wear = st.slider("Tool Wear", 0, 300, 100)

else:

    air_temp = st.number_input("Air Temperature", value=300.0)
    process_temp = st.number_input("Process Temperature", value=310.0)
    speed = st.number_input("Rotational Speed", value=1500)
    torque = st.number_input("Torque", value=50)
    wear = st.number_input("Tool Wear", value=100)

# ---------------- PREDICT BUTTON ----------------

if st.button("Predict Failure Risk"):

    payload = {
        "type": machine_type,
        "air_temperature": air_temp,
        "process_temperature": process_temp,
        "rotational_speed": speed,
        "torque": torque,
        "tool_wear": wear
    }

    try:
        response = requests.post(
            "http://127.0.0.1:8000/predict",
            json=payload
        )

        result = response.json()

        st.markdown("---")
        st.subheader("📊 Prediction Result")

        st.metric("Failure Risk", result["failure_risk"])
        st.metric("Confidence", result["confidence"])
        st.write("Status:", result["status"])
        st.write("Recommendation:", result["recommendation"])

        # ---------------- FEATURE IMPORTANCE ----------------
        importance = joblib.load("feature_importance.pkl")

        features = [
    "Type",
    "Air Temperature",
    "Process Temperature",
    "Rotational Speed",
    "Torque",
    "Tool Wear",
    "Stress Index",
    "Temp Difference"
]

        df_imp = pd.DataFrame({
            "Feature": features,
            "Importance": importance
        })

        st.markdown("---")
        st.subheader("🔍 Feature Importance")

        st.bar_chart(df_imp.set_index("Feature"))

    except Exception as e:
        st.error(f"Error: {e}")