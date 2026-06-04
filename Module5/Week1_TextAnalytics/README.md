# Module 5 — Week 1: ML on Text Data

**OPIM 5512 · Dr. Dave Wanik · University of Connecticut**

---

## Why does this matter?

Most data in the world is unstructured text — emails, reviews, reports, social media posts, medical notes. Being able to turn raw text into something a machine learning model can learn from is one of the most valuable skills in applied data science.

TF-IDF (Term Frequency–Inverse Document Frequency) is the workhorse of classical text ML. It's not as flashy as transformers, but it's fast, interpretable, and still incredibly useful for many real problems. Understanding it gives you the foundation to understand why the fancier stuff works.

---

## What you'll be able to do after this

- Clean and preprocess raw text (lowercase, remove punctuation, handle missing values)
- Convert text to a numerical feature matrix using TF-IDF
- Train classifiers on text data and evaluate them with classification report
- Interpret which words/n-grams are most predictive for each class
- Explain the difference between bag-of-words and sequence-based approaches

---

## How to run it

```bash
# 1. Activate your virtual environment
.venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Drop StormEvents_2019.csv into the data/ folder

# 4. Run
python text_classification.py
```

---

## The notebooks

- `Text_Analytics_Storms_ML.ipynb` — full walkthrough using NOAA storm event narratives

The dataset is real NOAA data — storm event descriptions from 2019. The task: given the narrative text, predict the type of storm. It's a fun one.
