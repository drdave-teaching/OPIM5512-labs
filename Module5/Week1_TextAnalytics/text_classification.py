import pandas as pd
import numpy as np
import re
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import classification_report
import os

DATA_PATH = os.path.join(os.path.dirname(__file__), "data", "StormEvents_2019.csv")
TEXT_COL = "EVENT_NARRATIVE"
TARGET_COL = "EVENT_TYPE"
TOP_N_CLASSES = 5  # keep only the most common event types for a clean demo


def clean_text(text):
    if not isinstance(text, str):
        return ""
    text = text.lower()
    text = re.sub(r"[^a-z\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def load_and_prepare(path):
    df = pd.read_csv(path, encoding="latin-1", low_memory=False)
    df = df[[TEXT_COL, TARGET_COL]].dropna()

    # keep only the top N most frequent event types
    top_classes = df[TARGET_COL].value_counts().head(TOP_N_CLASSES).index
    df = df[df[TARGET_COL].isin(top_classes)].copy()

    df["text_clean"] = df[TEXT_COL].apply(clean_text)
    return df


def main():
    df = load_and_prepare(DATA_PATH)
    print(f"Dataset: {len(df)} records, {df[TARGET_COL].nunique()} classes")
    print(df[TARGET_COL].value_counts(), "\n")

    X_train, X_test, y_train, y_test = train_test_split(
        df["text_clean"], df[TARGET_COL], test_size=0.2, random_state=42, stratify=df[TARGET_COL]
    )

    tfidf = TfidfVectorizer(max_features=5000, ngram_range=(1, 2))
    X_train_vec = tfidf.fit_transform(X_train)
    X_test_vec = tfidf.transform(X_test)

    models = [
        ("Logistic Regression", LogisticRegression(max_iter=1000, random_state=42)),
        ("Random Forest", RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1)),
    ]

    for name, model in models:
        model.fit(X_train_vec, y_train)
        preds = model.predict(X_test_vec)
        print(f"\n{'='*40}\n{name}\n{'='*40}")
        print(classification_report(y_test, preds))


if __name__ == "__main__":
    main()
