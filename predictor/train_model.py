import pandas as pd # type: ignore
from xgboost import XGBClassifier  # type: ignore # ✅ NEW
from sklearn.linear_model import LogisticRegression # type: ignore
from sklearn.model_selection import train_test_split # type: ignore
import joblib # type: ignore
import os

# Create model folder if not exists
os.makedirs("predictor/models", exist_ok=True)

# Load PIMA dataset
df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/diabetes.csv")

X = df.drop("Outcome", axis=1)
y = df["Outcome"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Primary model: XGBoost
primary_model = XGBClassifier(use_label_encoder=False, eval_metric='logloss')
primary_model.fit(X_train, y_train)

# Secondary validator: Logistic Regression
validator_model = LogisticRegression(max_iter=200)
validator_model.fit(X_train, y_train)

# Save both models
joblib.dump(primary_model, "predictor/models/primary_model.pkl")
joblib.dump(validator_model, "predictor/models/validator_model.pkl")

print("✅ Models (XGBoost + LogisticRegression) trained and saved successfully!")
