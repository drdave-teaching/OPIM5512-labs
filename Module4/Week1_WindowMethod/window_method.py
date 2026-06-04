import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score
import os

DATA_PATH = os.path.join(os.path.dirname(__file__), "data", "BDL_Jan2019.csv")
TARGET_COL = "load_MW"
N_LAGS = 24  # use the past 24 time steps as features


def create_lag_features(series, n_lags):
    df = pd.DataFrame({"target": series})
    for lag in range(1, n_lags + 1):
        df[f"lag_{lag}"] = df["target"].shift(lag)
    return df.dropna()


def train_test_split_ts(df, test_size=0.2):
    split = int(len(df) * (1 - test_size))
    train, test = df.iloc[:split], df.iloc[split:]
    X_train, y_train = train.drop("target", axis=1), train["target"]
    X_test, y_test = test.drop("target", axis=1), test["target"]
    return X_train, X_test, y_train, y_test


def main():
    df = pd.read_csv(DATA_PATH, parse_dates=True, index_col=0)
    series = df[TARGET_COL].dropna()

    lagged = create_lag_features(series, N_LAGS)
    X_train, X_test, y_train, y_test = train_test_split_ts(lagged)

    model = RandomForestRegressor(n_estimators=100, random_state=42, n_jobs=-1)
    model.fit(X_train, y_train)

    preds = model.predict(X_test)
    mae = mean_absolute_error(y_test, preds)
    r2 = r2_score(y_test, preds)

    print(f"Window Method — {N_LAGS} lags — Random Forest")
    print(f"  MAE : {mae:.3f}")
    print(f"  R²  : {r2:.3f}")

    importance = pd.Series(model.feature_importances_, index=X_train.columns)
    print("\nTop 5 most important lags:")
    print(importance.sort_values(ascending=False).head(5))


if __name__ == "__main__":
    main()
