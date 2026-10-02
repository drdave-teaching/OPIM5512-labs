# A05 · Cloud Shell commands: is my pipeline healthy?

**OPIM 5512 · Module 3.1 · Copy, paste, read the answer**

Every check you would otherwise click through the Google Cloud console for, as one command each. Open **Cloud Shell**
(the `>_` icon, top right of the Google Cloud console) and paste the blocks **one at a time**.

**The worked example uses Dr. Wanik's names.** Change the names in Step 0 to yours, or let Claude do it:

> **Personalize it with Claude.** Paste this prompt, then this whole page:
> *"Here are Cloud Shell commands from my OPIM 5512 A05 instructions. My Google Cloud project ID is ____ and my bucket
> name is ____ (region us-central1). Rewrite the commands with my names, change nothing else, and tell me what each
> block does in one sentence."*
> Not sure of your names? They are the `PROJECT_ID` and `BUCKET_NAME` you used in the Final GCP Guide F26 (Step 1).

---

## Step 0 · Tell Cloud Shell which project and bucket are yours
Run this first, and again whenever Cloud Shell restarts.
```bash
gcloud config set project myscrapers-dww05002-f26-510015
REGION="us-central1"
BUCKET_NAME="myscrapers-dww05002-f26-510015"
```

## Step 1 · Are all 5 functions deployed? (your 5 green checks, seen from Google's side)
You should see 5 rows, all `ACTIVE`: `craigslist-scraper`, `extractor-per-listing`, `extractor-llm-poc`,
`materialize-master`, `train-dt`.
```bash
gcloud functions list --regions="${REGION}" --format="table(name.basename(),state,updateTime)"
```

## Step 2 · Are the 5 hourly jobs scheduled?
5 rows, all `ENABLED`, at minutes :00 (scraper), :10 (extractor), :12 (Gemini), :15 (materialize), :20 (train).
```bash
gcloud scheduler jobs list --location="${REGION}" --format="table(name.basename(),schedule,state,lastAttemptTime)"
```

## Step 3 · Force run the pipeline (instead of clicking Force run)
Run these **one at a time**, about a minute apart: each step needs the one before it to finish.
```bash
gcloud scheduler jobs run craigslist-scraper-hourly --location="${REGION}"
```
```bash
gcloud scheduler jobs run extractor-per-listing-hourly --location="${REGION}"
```
```bash
gcloud scheduler jobs run materialize-master-hourly --location="${REGION}"
```

## Step 4 · What is in my bucket?
Three counts: ads scraped, ads extracted, rows in your master table (the last number includes 1 header row).
```bash
gcloud storage ls "gs://${BUCKET_NAME}/scrapes/**.txt" | wc -l
gcloud storage ls "gs://${BUCKET_NAME}/structured/**/jsonl/*.jsonl" | wc -l
gcloud storage cat "gs://${BUCKET_NAME}/structured/datasets/listings_master.csv" | wc -l
```
The first two should match (or the second lags by one hour). It grows by up to 10 every hour.

## Step 5 · Peek at my data
The first 5 rows of your master table: price, year, make, model, mileage.
```bash
gcloud storage cat "gs://${BUCKET_NAME}/structured/datasets/listings_master.csv" | cut -d, -f4-8 | head -6
```
Your price predictions (they appear after a few hours of data):
```bash
gcloud storage cat "gs://${BUCKET_NAME}/structured/preds/preds_master.csv" | head -6
```

## Step 6 · Something looks wrong? Read the function's log
Swap in the function you are worried about (`craigslist-scraper`, `extractor-per-listing`, `materialize-master`, ...).
Paste the output into Claude with what you expected.
```bash
gcloud functions logs read craigslist-scraper --region="${REGION}" --gen2 --limit=20
```

---

**For your A05 post:** a screenshot of Step 1 (5 functions `ACTIVE`) and Step 4 (your counts) proves your pipeline is
alive, even better than the green checks alone.
