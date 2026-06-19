# Module 2 — Week 1: Imbalanced Data & Sampling

**OPIM 5512 · Dr. Dave Wanik · University of Connecticut**

---

## Why does this matter?

Most of the problems worth solving are imbalanced. Fraud, equipment failure, disease, churn — the thing you care about is usually the rare class. If 95% of your rows are "no," a model that always predicts "no" is 95% accurate and completely useless.

This week you learn to fix that on two fronts: change the **data** (rebalance it with sampling) and change the **metric** (stop trusting accuracy, start watching recall and F1). And — just as important — you learn to do it *without leaking*, which is the single most common way these projects quietly go wrong.

---

## What you'll be able to do after this

- Recognize when class imbalance is hurting a model and why accuracy misleads
- Apply random under- and oversampling to rebalance a training set
- Use SMOTE and SMOTENC to synthesize realistic minority-class examples
- Choose the right cross-validation scheme (stratified, repeated, LOOCV, leave-one-group-out)
- Resample inside a pipeline so rebalancing never leaks into the test fold

---

## How to run it

```bash
# 1. Activate your virtual environment
.venv\Scripts\activate

# 2. Install dependencies
pip install scikit-learn imbalanced-learn pandas
```

The key idea in code — resample **inside** the pipeline so each CV fold is rebalanced on its own:

```python
from imblearn.pipeline import Pipeline
from imblearn.over_sampling import SMOTE
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import RepeatedStratifiedKFold, cross_val_score

cv = RepeatedStratifiedKFold(n_splits=5, n_repeats=3, random_state=42)
pipe = Pipeline([('smote', SMOTE(random_state=42)),
                 ('clf', RandomForestClassifier())])
scores = cross_val_score(pipe, X, y, cv=cv, scoring='f1')
```

> **Golden rule:** SMOTE goes *inside* the pipeline — resample per fold, score on untouched real data.

See the slide deck in this folder (`M2_W1_Imbalanced_Data_and_Sampling.pdf`) for the full walkthrough.
