# Module 4 — Week 2: TSFresh — Automated Time Series Feature Engineering

**OPIM 5512 · Dr. Dave Wanik · University of Connecticut**

---

## Why does this matter?

The window method from Week 1 is powerful but manual — you decide which lags to use. TSFresh takes a different approach: it automatically extracts hundreds of statistical features from your time series (mean, variance, entropy, autocorrelation, and many more) and then figures out which ones actually predict your target.

This is the kind of tool that data scientists use when they want to be thorough and let the data speak for itself. You'll see it in industrial IoT (predicting machine failures), finance (detecting anomalies), and healthcare (classifying patient outcomes from monitoring data).

---

## What you'll be able to do after this

- Use TSFresh to automatically generate a rich feature set from raw time series
- Apply TSFresh's built-in feature selection to filter out noise
- Feed the resulting features into a standard sklearn classifier or regressor
- Understand the tradeoff: TSFresh is powerful but slow — know when to use it

---

## How to run it

```bash
# 1. Activate your virtual environment
.venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt
# Note: tsfresh takes a minute to install — it has a lot of dependencies

# 3. Check the notebooks/ folder for the full walkthrough
```

---

## The notebooks

- `TSFresh_Example_BDLFiveYears.ipynb` — full TSFresh pipeline on 5 years of energy data

This one is compute-heavy. If it's slow on your laptop, that's normal — run it and go get coffee.
