# Module 4 — Week 1: The Window Method for Time Series

**OPIM 5512 · Dr. Dave Wanik · University of Connecticut**

---

## Why does this matter?

Time series data is everywhere — stock prices, energy demand, website traffic, sales forecasts, weather. Most of the data science world runs on time-indexed data, and yet most intro courses skip it entirely.

The Window Method is the key insight that unlocks time series for traditional ML: instead of treating each row as independent, you create *lag features* — "what was the value 1 hour ago? 6 hours ago? 24 hours ago?" — and suddenly you can use any model you already know (Random Forest, Gradient Boosting, etc.) on time series data. No special time series library needed.

---

## What you'll be able to do after this

- Explain what a lag feature is and why it captures temporal patterns
- Build a feature matrix from a time series using the window method
- Split time series data correctly (no random shuffle — time has to flow forward!)
- Fit a Random Forest on time series features and evaluate it
- Identify which lag features matter most using feature importance

---

## How to run it

```bash
# 1. Activate your virtual environment
.venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Drop BDL_Jan2019.csv into the data/ folder

# 4. Run
python window_method.py
```

---

## The notebooks

- `TheWindowMethod_Lags.ipynb` — the original walkthrough, building intuition step by step
- `EDA_TimeSeries_Financial.ipynb` — exploratory analysis on financial time series
- `Missing_Data_Weather.ipynb` — handling gaps in time series data (super common in practice)

Start with `TheWindowMethod_Lags.ipynb` to build the mental model, then look at how `window_method.py` cleans it up.
