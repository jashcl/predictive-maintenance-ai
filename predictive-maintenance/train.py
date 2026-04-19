import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

print("Loading dataset...")

df = pd.read_csv("data.csv")

# -----------------------------
# DATA PREPROCESSING
# -----------------------------
df["Type"] = df["Type"].map({"L": 0, "M": 1, "H": 2})

# Feature Engineering (IMPORTANT)
df["stress_index"] = df["Torque"] * df["Rotational speed"]
df["temp_diff"] = df["Process temperature"] - df["Air temperature"]

# -----------------------------
# FEATURES & TARGET
# -----------------------------
features = [
    "Type",
    "Air temperature",
    "Process temperature",
    "Rotational speed",
    "Torque",
    "Tool wear",
    "stress_index",
    "temp_diff"
]

X = df[features]
y = df["Machine failure"]

# -----------------------------
# TRAIN TEST SPLIT
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# -----------------------------
# MODEL
# -----------------------------
model = RandomForestClassifier(
    n_estimators=200,
    max_depth=12,
    random_state=42
)

print("Training model...")
model.fit(X_train, y_train)

print("Accuracy:", model.score(X_test, y_test))

# Save model
joblib.dump(model, "model.pkl")

print("Model saved successfully!")

import joblib

joblib.dump(model.feature_importances_, "feature_importance.pkl")

model.fit(X_train, y_train)

import joblib

# Save model
joblib.dump(model, "model.pkl")

# Save feature importance
joblib.dump(model.feature_importances_, "feature_importance.pkl")

print("Model and feature importance saved successfully!")