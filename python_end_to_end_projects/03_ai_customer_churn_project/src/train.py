from pathlib import Path
import json
import joblib

from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from data_loader import load_data

def train_model():
    data = load_data()

    X = data.drop(columns=["customer_id", "churn"])
    y = data["churn"]

    numerical_columns = ["age", "monthly_spend", "tenure_months", "support_calls"]
    categorical_columns = ["contract_type", "payment_method"]

    preprocessor = ColumnTransformer(
        transformers=[
            ("num", StandardScaler(), numerical_columns),
            ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_columns),
        ]
    )

    model = Pipeline(
        steps=[
            ("preprocessor", preprocessor),
            ("classifier", LogisticRegression(max_iter=1000)),
        ]
    )

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42, stratify=y
    )

    model.fit(X_train, y_train)
    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)
    report = classification_report(y_test, predictions, output_dict=True)

    Path("models").mkdir(exist_ok=True)
    Path("reports").mkdir(exist_ok=True)

    joblib.dump(model, "models/churn_model.pkl")

    metrics = {
        "accuracy": round(float(accuracy), 4),
        "classification_report": report,
    }
    Path("reports/metrics.json").write_text(
        json.dumps(metrics, indent=2), encoding="utf-8"
    )

    print(f"Model trained successfully. Accuracy: {accuracy:.2%}")
    print("Saved model: models/churn_model.pkl")
    print("Saved metrics: reports/metrics.json")

if __name__ == "__main__":
    train_model()
