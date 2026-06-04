# Module 5 — Week 2: HuggingFace Transformers & Topic Modeling

**OPIM 5512 · Dr. Dave Wanik · University of Connecticut**

---

## Why does this matter?

TF-IDF is great, but it doesn't understand language — it just counts words. Transformers (BERT, RoBERTa, and their cousins) actually *understand* context. "The bank was steep" and "the bank was closed" use the same word but mean totally different things. Transformers get that. TF-IDF doesn't.

HuggingFace has made state-of-the-art NLP models accessible to everyone. You don't need a PhD in deep learning — you can call a pre-trained model in a few lines of Python. This is genuinely one of the most powerful tools in the modern data scientist's toolkit.

Topic modeling is a different but complementary skill — it's unsupervised, so instead of predicting a label you're discovering hidden themes in a collection of documents. Great for exploring large text datasets before you decide what question to ask.

---

## What you'll be able to do after this

- Load and use a pre-trained HuggingFace model for text classification or embeddings
- Compare transformer-based features vs. TF-IDF on the same task
- Apply topic modeling to find hidden themes in a document collection
- Understand the tradeoff: transformers are powerful but slow and expensive — know when to use them vs. simpler methods

---

## How to run it

```bash
# 1. Activate your virtual environment
.venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt
# Note: transformers + torch are large downloads — be patient

# 3. Check the notebooks/ folder to run the examples
```

The first time you run a HuggingFace model it will download the weights — that's normal and only happens once.

---

## The notebooks

- `NLP_Pandas_HuggingFace.ipynb` — using HuggingFace models in a pandas workflow
- `TopicModeling.ipynb` — unsupervised topic discovery with LDA

If your laptop is slow on the transformer notebook, try running it in Google Colab — it's free and has a GPU.
