# AI Project: Customer Churn Prediction

This project demonstrates an end-to-end machine-learning workflow:

1. Load customer data.
2. Preprocess numerical and categorical columns.
3. Train a logistic-regression model.
4. Evaluate accuracy.
5. Save the trained model.
6. Load the model and make a new prediction.

## Setup

```bash
python -m venv venv
source venv/bin/activate       # macOS/Linux
venv\Scripts\activate        # Windows
pip install -r requirements.txt
python src/train.py
python src/predict.py
```

## Output

- Trained model: `models/churn_model.pkl`
- Evaluation results: `reports/metrics.json`

## Concepts Covered

- pandas
- scikit-learn pipeline
- preprocessing
- train/test split
- model evaluation
- model persistence using joblib
