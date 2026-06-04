import pandas as pd
import numpy as np
from collections import Counter
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import classification_report
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
import os

DATA_PATH = os.path.join(os.path.dirname(__file__), "data", "breastcancer.csv")


def load_and_prepare(path):
    df = pd.read_csv(path)
    df.drop(columns=["id", "Unnamed: 32"], errors="ignore", inplace=True)
    le = LabelEncoder()
    df["diagnosis"] = le.fit_transform(df["diagnosis"])
    X = df.drop("diagnosis", axis=1)
    y = df["diagnosis"]
    return X, y


def build_grids():
    return [
        (
            "Logistic Regression",
            Pipeline([("scl", StandardScaler()), ("clf", LogisticRegression(max_iter=10000))]),
            [{"clf__penalty": ["l1", "l2"], "clf__C": [1, 10], "clf__solver": ["liblinear"]}],
        ),
        (
            "Decision Tree",
            Pipeline([("scl", StandardScaler()), ("clf", DecisionTreeClassifier())]),
            [{"clf__criterion": ["gini", "entropy"], "clf__max_depth": [3, 5, 10], "clf__min_samples_leaf": [5, 10]}],
        ),
        (
            "Random Forest",
            Pipeline([("scl", StandardScaler()), ("clf", RandomForestClassifier(random_state=42))]),
            [{"clf__n_estimators": [50, 100], "clf__max_depth": [5, 10], "clf__min_samples_leaf": [5, 10]}],
        ),
        (
            "Gradient Boosting",
            Pipeline([("scl", StandardScaler()), ("clf", GradientBoostingClassifier(random_state=42))]),
            [{"clf__n_estimators": [50, 100], "clf__learning_rate": [0.01, 0.1]}],
        ),
    ]


def main():
    X, y = load_and_prepare(DATA_PATH)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=123)

    print(f"Class distribution: {Counter(y)}\n")

    results = []
    for name, pipe, params in build_grids():
        gs = GridSearchCV(pipe, params, scoring="accuracy", cv=5, n_jobs=-1)
        gs.fit(X_train, y_train)
        score = gs.score(X_test, y_test)
        results.append((name, score, gs.best_params_))
        print(f"{name:<25} Test accuracy: {score:.4f}")
        print(f"  Best params: {gs.best_params_}\n")

    best = max(results, key=lambda x: x[1])
    print(f"\nBest model: {best[0]} ({best[1]:.4f})")


if __name__ == "__main__":
    main()
