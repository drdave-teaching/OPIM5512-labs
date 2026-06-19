# Module 2 — Week 3: Explainable AI (xAI)

**OPIM 5512 · Dr. Dave Wanik · University of Connecticut**

---

## Why does this matter?

A Random Forest or a gradient-boosted model can be very accurate and completely opaque — data goes in, a prediction comes out, and nobody can tell you *why*. In the real world that's not good enough. A manager, a regulator, or a customer will ask which factors drove the decision, and "the model said so" is not an answer.

Explainable AI gives you tools to open the black box: see how each feature moves the prediction, rank which features actually matter, and use that to both **tell the story** and **simplify the model**. A leaner model that scores the same is easier to defend, cheaper to run, and less likely to overfit.

---

## What you'll be able to do after this

- Explain why even accurate, black-box models need to be made interpretable
- Build partial dependence plots and read linear vs. nonlinear feature effects
- Run permutation importance to rank which features actually drive predictions
- Use feature importance to simplify a model and tell its story
- Generate a strong baseline pipeline automatically with autoML (TPOT)

---

## How to run it

```bash
# 1. Activate your virtual environment
.venv\Scripts\activate

# 2. Install dependencies
pip install scikit-learn pandas matplotlib
```

Two workhorse techniques, both model-agnostic and a few lines each:

```python
from sklearn.inspection import permutation_importance, PartialDependenceDisplay

# Which features actually matter? (measured on the test set)
r = permutation_importance(model, X_test, y_test, n_repeats=10, random_state=42)
print(sorted(zip(r.importances_mean, X.columns), reverse=True))

# How does a feature move the prediction?
PartialDependenceDisplay.from_estimator(model, X, features=['income', 'rooms'])
```

> Use the importance ranking to drop weak features, refit, and confirm the score holds — explanation becomes a leaner model.

See the slide deck in this folder (`M2_W3_Explainable_AI.pdf`) for the full walkthrough.
