import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import joblib

df = pd.read_csv("training_data_full.csv")

le = LabelEncoder()
df["Fee"] = le.fit_transform(df["Fee"])

X = df[["Attendance", "Fee"]]
y = df["Alert"]

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

joblib.dump(model, "ml_model.pkl")
joblib.dump(le, "fee_encoder.pkl")

print("ML model trained using full student dataset")
