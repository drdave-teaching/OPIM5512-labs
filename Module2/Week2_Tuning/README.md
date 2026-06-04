# Module 2 — Week 2: Pipelines & Hyperparameter Tuning

**OPIM 5512 · Dr. Dave Wanik · University of Connecticut**

---

## Why does this matter?

In the real world, nobody just fits a model with default settings and calls it a day. You tune it. Hyperparameter tuning is how you squeeze the last few percentage points of performance out of a model — and in some industries (credit scoring, fraud detection, medical diagnosis), those points matter a lot.

Pipelines are equally important. A Pipeline bundles your preprocessing and your model into one object — so you can't accidentally scale your test data using the training data's statistics (a classic mistake that leaks information and makes your model look better than it is). At work, pipelines also make your code way easier to hand off to someone else.

---

## What you'll be able to do after this

- Build a `sklearn` Pipeline that chains preprocessing and a classifier
- Run a `GridSearchCV` across multiple models with different hyperparameter grids
- Compare models fairly using cross-validation
- Read a grid search results table and pick the best model
- Explain what "data leakage" is and why Pipelines prevent it

---

## How to run it

```bash
# 1. Activate your virtual environment
.venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Drop breastcancer.csv into the data/ folder

# 4. Run
python grid_search_classification.py
```

Fair warning — grid search takes a few minutes. That's normal. In the real world you'd run this overnight or on a cloud machine.

---

## The notebooks

- `1_Regression_SpotCheck.ipynb` — spot-checking many regression models at once
- `1a_AdvancedPipelines_Regression.ipynb` — pipelines for regression
- `2_Classification_SpotCheck_and_Pipelines.ipynb` — spot-checking classifiers
- `2a_Pipelines_GridSearch_Classification.ipynb` — the full pipeline + grid search workflow
- `3_HyperparameterTuning_Widgets.ipynb` — interactive tuning with widgets

Start with `2a` — it's the closest to what the `.py` script does.
