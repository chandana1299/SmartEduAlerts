import joblib
import pandas as pd

model = joblib.load("ml_model.pkl")
encoder = joblib.load("fee_encoder.pkl")

def predict_alert(student):
    fee_encoded = encoder.transform([student["fee"]])[0]

    X = pd.DataFrame([[student["attendance"], fee_encoded]],
                     columns=["Attendance", "Fee"])

    return model.predict(X)[0]  # 1 or 0
