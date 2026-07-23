from pathlib import Path
import joblib
import pandas as pd

def predict_customer():
    model_path = Path("models/churn_model.pkl")
    if not model_path.exists():
        raise FileNotFoundError("Run 'python src/train.py' before prediction.")

    model = joblib.load(model_path)

    new_customer = pd.DataFrame([{
        "age": 35,
        "monthly_spend": 4200,
        "tenure_months": 8,
        "support_calls": 4,
        "contract_type": "Monthly",
        "payment_method": "Credit Card",
    }])

    prediction = model.predict(new_customer)[0]
    probability = model.predict_proba(new_customer)[0][1]

    result = "Likely to churn" if prediction == 1 else "Likely to stay"
    print(f"Prediction: {result}")
    print(f"Churn probability: {probability:.2%}")

if __name__ == "__main__":
    predict_customer()
