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

## Philosophy

- Each lab is a standalone `.py` script you can run from the terminal
- Notebooks (`.ipynb`) are kept in the `notebooks/` subfolder for exploration
- Every module has its own `requirements.txt` — install only what you need
- Never commit your `.venv` folder or large data files
