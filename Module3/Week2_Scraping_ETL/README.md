# Module 3 — Week 2: Web Scraping & ETL

**OPIM 5512 · Dr. Dave Wanik · University of Connecticut**

---

## Why does this matter?

Not every dataset comes pre-packaged as a clean CSV. In the real world, you often have to *go get* the data — from websites, APIs, PDFs, emails, whatever. Web scraping is how data scientists build datasets that don't exist yet.

ETL (Extract, Transform, Load) is the process of pulling raw data, cleaning it, and putting it somewhere useful. This is a huge part of data engineering, and even as a data scientist you'll write ETL pipelines constantly. If you can scrape a website and turn it into a clean DataFrame, you can get data on anything.

---

## What you'll be able to do after this

- Use `requests` to fetch web pages programmatically
- Parse HTML with `BeautifulSoup` to pull out the data you want
- Clean and standardize messy scraped data with `pandas` and `regex`
- Save results to CSV for downstream analysis
- Be a good citizen: rate-limit your requests so you don't hammer servers

---

## How to run it

```bash
# 1. Activate your virtual environment
.venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Update the URL in scrape_cars.py to a real listings page
#    (check with Dr. Dave for the current target URL)

# 4. Run
python scrape_cars.py
```

The script will save a `scraped_cars.csv` in the current directory.

---

## The notebooks

- `M3_2_BeautifulSoup_ModelUpdates.ipynb` — original scraping walkthrough

A note on scraping: websites change. If the notebook throws errors, that's not a bug in the code — the site's HTML structure probably changed. Debugging that *is* the lesson.
