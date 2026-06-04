import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.metrics import mean_absolute_error, r2_score
import os

DATA_PATH = os.path.join(os.path.dirname(__file__), "data", "BostonHousing.csv")


def load_and_prepare(path):
    df = pd.read_csv(path)
    X = df.drop("medv", axis=1)
    y = df["medv"]
    return X, y


def split_and_scale(X, y):
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, shuffle=True, random_state=42
    )
    scaler = MinMaxScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)
    return X_train, X_test, y_train, y_test


def evaluate(name, model, X_train, X_test, y_train, y_test):
    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    mae = mean_absolute_error(y_test, preds)
    r2 = r2_score(y_test, preds)
    print(f"{name:<30} MAE: {mae:.3f}   R2: {r2:.3f}")


def main():
    X, y = load_and_prepare(DATA_PATH)
    X_train, X_test, y_train, y_test = split_and_scale(X, y)

    models = [
        ("Decision Tree", DecisionTreeRegressor()),
        ("Random Forest", RandomForestRegressor(n_estimators=100, random_state=42)),
        ("Gradient Boosting", GradientBoostingRegressor(n_estimators=100, random_state=42)),
    ]

    print(f"\n{'Model':<30} {'MAE':>8}   {'R2':>6}")
    print("-" * 50)
    for name, model in models:
        evaluate(name, model, X_train, X_test, y_train, y_test)


if __name__ == "__main__":
    main()
