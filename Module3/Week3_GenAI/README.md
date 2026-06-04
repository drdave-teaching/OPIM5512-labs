# Module 3 — Week 3: GenAI & LLM-Assisted ETL

**OPIM 5512 · Dr. Dave Wanik · University of Connecticut**

---

## Why does this matter?

LLMs have fundamentally changed what's possible in data science. Tasks that used to require complex regex, custom parsers, or manual labeling can now be done by describing what you want in plain English and letting a model do the heavy lifting.

LLM-assisted ETL is already being used in production at real companies — pulling structured data out of unstructured documents, classifying text, generating synthetic training data, and more. This isn't the future. It's now.

---

## What you'll be able to do after this

- Use an LLM API to extract structured data from unstructured text
- Build a simple ETL pipeline where the "transform" step is an LLM call
- Understand the tradeoffs: cost, latency, and reliability vs. traditional parsing
- Handle API keys securely using environment variables (never hardcode them!)

---

## How to run it

```bash
# 1. Activate your virtual environment
.venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Create a .env file with your API key (NEVER commit this file)
echo ANTHROPIC_API_KEY=your_key_here > .env

# 4. Run the notebook or check the AgenticAI folder for the .py version
```

---

## The notebooks

- `M3_3_GenAI_ETL.ipynb` — full walkthrough of LLM-assisted data extraction

See also the `WeekN_AgenticAI/` folder — that's where we take this further with full agent loops.
