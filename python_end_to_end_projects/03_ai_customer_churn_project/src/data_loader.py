from pathlib import Path
import pandas as pd

def load_data(file_path="data/customer_churn.csv"):
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"Dataset not found: {path}")
    return pd.read_csv(path)
