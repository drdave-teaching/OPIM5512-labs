import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import classification_report
import os

DATA_PATH = os.path.join(os.path.dirname(__file__), "data", "BostonHousing.csv")


def load_and_prepare(path):
    df = pd.read_csv(path)
    # create binary target: 1 if price above median, 0 otherwise
    df["medv"] = np.where(df["medv"] > df["medv"].median(), 1, 0)
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
    print(f"\n{'='*40}")
    print(f"Model: {name}")
    print(f"{'='*40}")
    print("-- Test Set --")
    print(classification_report(y_test, model.predict(X_test)))


def main():
    X, y = load_and_prepare(DATA_PATH)
    X_train, X_test, y_train, y_test = split_and_scale(X, y)

    models = [
        ("Logistic Regression", LogisticRegression()),
        ("Decision Tree", DecisionTreeClassifier()),
        ("Random Forest", RandomForestClassifier(n_estimators=100, random_state=42)),
        ("Gradient Boosting", GradientBoostingClassifier(n_estimators=100, random_state=42)),
    ]

    for name, model in models:
        evaluate(name, model, X_train, X_test, y_train, y_test)


if __name__ == "__main__":
    main()
