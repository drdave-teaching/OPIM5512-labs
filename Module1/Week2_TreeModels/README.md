# Module 1 — Week 2: Tree-Based Models

**OPIM 5512 · Dr. Dave Wanik · University of Connecticut**

---

## Why does this matter?

Decision Trees, Random Forests, and Gradient Boosting are probably the most widely used models in applied data science. If you work in finance, healthcare, retail, logistics — you will use these. They're interpretable enough that you can explain them to a non-technical manager, and powerful enough to win Kaggle competitions.

The Boston Housing dataset is a classic. It's small enough to run fast, rich enough to be interesting, and has both a regression version (predict house price) and a classification version (predict above/below median). We use it here to build the same mental model twice — regression then classification — so the pattern becomes muscle memory.

---

## What you'll be able to do after this

- Load a dataset, split it into train/test, and scale features — all in clean Python functions
- Fit Decision Tree, Random Forest, and Gradient Boosting models for both regression and classification
- Evaluate models with MAE/R² (regression) and classification report (classification)
- Run a script from the terminal and read the output — no Jupyter required
- Explain *why* Random Forests outperform a single Decision Tree

---

## How to run it

```bash
# 1. Activate your virtual environment
.venv\Scripts\activate        # Windows
# source .venv/bin/activate   # Mac/Linux

# 2. Install dependencies
pip install -r requirements.txt

# 3. Drop the data file into the data/ folder
#    (BostonHousing.csv — get it from the course materials)

# 4. Run the scripts
python boston_regression.py
python boston_classification.py
```

You should see a table of MAE/R² scores for regression, and classification reports for each model.

---

## The notebooks

The `notebooks/` folder has the original exploratory versions:
- `DTR_RFR_GBR_BostonHousing.ipynb` — regression walkthrough
- `DTC_RFC_GBC_BostonHousing.ipynb` — classification walkthrough
- `Week2_1_NN_Regression.ipynb` — neural network bonus content
- `Week2_1_NN_Classification.ipynb` — neural network bonus content

The `.py` scripts are the cleaned-up, production versions of those notebooks. Compare them — notice how the scripts have functions, no `drive.mount()` calls, and can be run from anywhere.
