print("=== TRAIN MODEL SCRIPT STARTED ===")

import pandas as pd
import joblib
import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

print("Imports successful")

# project root
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print("Base dir:", base_dir)

data_path = os.path.join(
    base_dir, "data", "processed", "cleaned_data.csv"
)
print("Data path:", data_path)

model_dir = os.path.join(base_dir, "models")
model_path = os.path.join(model_dir, "risk_model.pkl")

print("Model dir:", model_dir)
print("Model path:", model_path)

os.makedirs(model_dir, exist_ok=True)
print("Models directory ensured")

# load data
df = pd.read_csv(data_path)
print("Data loaded. Shape:", df.shape)
print(df.head())

X = df.drop("risk_level", axis=1)
y = df["risk_level"]

print("Starting train-test split")

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("Training model now...")

model = RandomForestClassifier(
    n_estimators=100, random_state=42
)
model.fit(X_train, y_train)

print("Model training completed")

joblib.dump(model, model_path)
print("Model saved successfully at:", model_path)

print("=== TRAIN MODEL SCRIPT FINISHED ===")
