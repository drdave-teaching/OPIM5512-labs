# OPIM 5512 — Labs

**Dr. Dave Wanik · Operations and Information Management · University of Connecticut**

This is the production-ready companion to the main OPIM 5512 course repo. Every lab here runs as a clean Python script — no Google Drive mounts, no Colab dependencies. The goal: learn data science the way it's actually done in the real world.

---

## How to use this repo

### 1. Clone it
```bash
git clone https://github.com/drdave-teaching/OPIM5512-labs.git
cd OPIM5512-labs
```

### 2. Create a virtual environment (do this once per module)
```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# Mac/Linux
source .venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run a lab
```bash
python Module1/Week2_TreeModels/boston_classification.py
```

---

## Modules

| # | Module | Topics |
|---|--------|--------|
| 1 | **Tech Stack + Tree Models** | Git, VSCode, venv, Decision Trees, Random Forest, Gradient Boosting |
| 2 | **Hyperparameter Tuning + xAI** | Pipelines, GridSearch, Optuna, SHAP, partial dependence |
| 3 | **Scraping, ETL + GenAI** | BeautifulSoup, RegEx, LLM-assisted ETL, Agentic AI |
| 4 | **Time Series** | Window method, TSFresh, forecasting evaluation |
| 5 | **Text Analytics** | ML on text, HuggingFace Transformers |

---

## Learning Objectives

By the end of each week, you'll be able to:

### Module 1 — Tech Stack + Tree Models

**Week 1 · Setting Up Your Tech Stack**
- Install and configure Git, VS Code, and Python
- Create a GitHub account and connect it to your local machine
- Clone a repo, make a change, and push it back to GitHub
- Create and activate a virtual environment so projects don't step on each other
- Set up a reproducible stack so "it works on my machine" is never an excuse

**Week 2 · Tree-Based Models**
- Load a dataset, split into train/test, and scale features — all in clean Python functions
- Fit Decision Tree, Random Forest, and Gradient Boosting for both regression and classification
- Evaluate models with MAE/R² (regression) and the classification report (classification)
- Run a script from the terminal and read the output — no Jupyter required
- Explain *why* Random Forests outperform a single Decision Tree

### Module 2 — Hyperparameter Tuning + xAI

**Week 1 · Imbalanced Data & Sampling**
- Recognize when class imbalance is hurting a model and why accuracy misleads
- Apply random under- and oversampling to rebalance a training set
- Use SMOTE and SMOTENC to synthesize realistic minority-class examples
- Choose the right cross-validation scheme (stratified, repeated, LOOCV, leave-one-group-out)
- Resample inside a pipeline so rebalancing never leaks into the test fold

**Week 2 · Pipelines & Hyperparameter Tuning**
- Build a `sklearn` Pipeline that chains preprocessing and a classifier
- Run `GridSearchCV` across multiple models with different hyperparameter grids
- Compare models fairly using cross-validation
- Read a grid search results table and pick the best model
- Explain what "data leakage" is and why Pipelines prevent it

**Week 3 · Explainable AI (xAI)**
- Explain why even accurate, black-box models need to be made interpretable
- Build partial dependence plots and read linear vs. nonlinear feature effects
- Run permutation importance to rank which features actually drive predictions
- Use feature importance to simplify a model and tell its story
- Generate a strong baseline pipeline automatically with autoML (TPOT)

### Module 3 — Scraping, ETL + GenAI

**Week 1 · GitHub & the Cloud (GCP)**
- Explain why moving code to the cloud makes pipelines reliable and reproducible
- Create and configure a Google Cloud Platform project (billing, APIs, permissions)
- Deploy a cloud function and trigger it
- Test deployed functions and use logs to debug failures
- Authenticate with service accounts and keep credentials out of your code

**Week 2 · Web Scraping & ETL**
- Use `requests` to fetch web pages programmatically
- Parse HTML with `BeautifulSoup` to pull out the data you want
- Clean and standardize messy scraped data with `pandas` and `regex`
- Save results to CSV for downstream analysis
- Be a good citizen: rate-limit your requests so you don't hammer servers

**Week 3 · GenAI & LLM-Assisted ETL**
- Use an LLM API to extract structured data from unstructured text
- Build an ETL pipeline where the "transform" step is an LLM call
- Materialize many JSONL outputs into one clean modeling dataset
- Weigh the tradeoffs: cost, latency, and reliability vs. traditional parsing
- Handle API keys securely with environment variables (never hardcode them!)

**Bonus · Agentic AI**
- Explain the difference between a single LLM call and an agent that takes actions
- Describe tools and how an agent decides which one to call
- Trace an agent's tool loop: act → observe → decide → repeat
- Run an agent that extracts structured data autonomously
- Judge when an agentic workflow is worth it versus a single model call

### Module 4 — Time Series

**Week 1 · The Window Method**
- Explain what a lag feature is and why it captures temporal patterns
- Build a feature matrix from a time series using the window method
- Split time series data correctly (no random shuffle — time has to flow forward!)
- Fit a Random Forest on time series features and evaluate it
- Identify which lag features matter most using feature importance

**Week 2 · TSFresh**
- Use TSFresh to automatically generate a rich feature set from raw time series
- Apply TSFresh's built-in feature selection to filter out noise
- Feed the resulting features into a standard sklearn classifier or regressor
- Keep extraction and selection inside the training boundary to avoid leakage
- Judge the tradeoff: TSFresh is powerful but slow — know when to use it

### Module 5 — Text Analytics

**Week 1 · ML on Text Data**
- Clean and preprocess raw text (lowercase, remove punctuation, handle missing values)
- Convert text to a numerical feature matrix using TF-IDF
- Train classifiers on text data and evaluate them with the classification report
- Interpret which words/n-grams are most predictive for each class
- Explain the difference between bag-of-words and sequence-based approaches

**Week 2 · HuggingFace & Topic Modeling**
- Load and use a pre-trained HuggingFace model for classification or embeddings
- Compare transformer-based features vs. TF-IDF on the same task
- Apply topic modeling to find hidden themes in a document collection
- Use summarization and zero-shot classification out of the box
- Judge the tradeoff: transformers are powerful but slow and expensive

---

## Philosophy

- Each lab is a standalone `.py` script you can run from the terminal
- Notebooks (`.ipynb`) are kept in the `notebooks/` subfolder for exploration
- Every module has its own `requirements.txt` — install only what you need
- Never commit your `.venv` folder or large data files
