# A07 · Commands and steps: GenAI for ETL

**OPIM 5512 · Module 3.3 · Part 1: new Gemini fields · Part 2: your own `materialize-llm` function**

Your pipeline already asks Gemini to read every ad (the `extractor-llm-poc` function, every hour at :12). In A07 you
(1) teach it to return **new fields** (choose different or more fields than your A06 regex: transmission, body type,
fuel, color, title status, condition, location...), and (2) deploy a **new** Cloud Function, `materialize-llm`, that
collects Gemini's output into its own growing CSV, while your regex pipeline keeps running untouched. Then you compare
the two.

Cloud Shell blocks: open **Cloud Shell** (the `>_` icon, top right of the Google Cloud console) and paste them **one at a time**.

**The worked example uses Dr. Wanik's names.** Change the names in Step 0 to yours, or let Claude do it:

> **Personalize it with Claude.** Paste this prompt, then this whole page:
> *"Here are Cloud Shell commands from my OPIM 5512 A07 instructions. My Google Cloud project ID is ____ and my bucket
> name is ____ (region us-central1). The new fields I am adding are ____. Rewrite the commands with my names and
> fields, change nothing else, and tell me what each block does in one sentence."*

---

## Step 0 · Tell Cloud Shell which project and bucket are yours
```bash
gcloud config set project myscrapers-dww05002-f26-510015
REGION="us-central1"
BUCKET_NAME="myscrapers-dww05002-f26-510015"
```

## Step 1 · Is Gemini keeping up?
Two counts: ads extracted by your regex, and ads read by Gemini. They should match (Gemini runs 2 minutes after the
regex extractor). If Gemini is behind, force run it:
```bash
gcloud storage ls "gs://${BUCKET_NAME}/structured/**/jsonl/*.jsonl" | wc -l
gcloud storage ls "gs://${BUCKET_NAME}/structured/**/jsonl_llm/*.jsonl" | wc -l
```
```bash
gcloud scheduler jobs run extractor-llm-poc-hourly --location="${REGION}"
```
See what Gemini wrote for your newest car:
```bash
gcloud storage cat "$(gcloud storage ls "gs://${BUCKET_NAME}/structured/**/jsonl_llm/*.jsonl" | tail -1)"
```

---

# Part 1 · Add new fields to Gemini's schema

## Step 2 · Edit the schema (on a branch, exactly like A06)
In **your fork**, open `cloud_function/extractor-llm-poc/main.py` and find the `schema` inside `_vertex_extract_fields()`
(around line 181). Add one line per new field inside `"properties"`, for example:
```python
            "transmission": {"type": "string", "nullable": True},
            "title_status": {"type": "string", "nullable": True},
```
Leave new fields **out** of `"required"` (forcing them invites made-up answers). Want Gemini to stick to a fixed list,
like `automatic` / `manual`? Say so in the `sys_instr` text a few lines below.
Then: **Commit changes… → Create a new branch → pull request → check Files changed → Merge**. GitHub Actions runs
**Deploy LLM Extractor** by itself.

## Step 3 · Wait until the NEW Gemini extractor is live
The time printed must be **after** you clicked Merge (UTC: 4 PM Eastern = 20:00).
```bash
gcloud functions describe extractor-llm-poc --region="${REGION}" --gen2 --format='value(updateTime)'
```

## Step 4 · Re-read your old cars with the new schema
New cars get your new fields automatically. This sends every old batch back through Gemini: about one call per car
(a few cents for a few hundred cars). Each batch prints a line with `"ok":true`.
```bash
URL="$(gcloud functions describe extractor-llm-poc --region="${REGION}" --gen2 --format='value(serviceConfig.uri)')"
for RUN in $(gcloud storage ls "gs://${BUCKET_NAME}/structured/" | grep "run_id=" | awk -F'run_id=' '{print $2}' | tr -d '/'); do
  curl -s -X POST -H "Authorization: Bearer $(gcloud auth print-identity-token)" -H "Content-Type: application/json" \
       -d "{\"run_id\":\"${RUN}\",\"overwrite\":true}" "${URL}"
  echo
done
```

## Step 5 · Proof 1: Gemini is extracting your new field
Counts every value Gemini returned for `transmission` across all your cars (swap in each field you added).
**Screenshot this for your post.**
```bash
gcloud storage cat "gs://${BUCKET_NAME}/structured/**/jsonl_llm/*.jsonl" | grep -o '"transmission": *"[^"]*"' | sort | uniq -c | sort -rn
```
Nothing printed? Back to Step 3: Gemini probably re-read the cars before the new code was live. Run Step 4 again.

---

# Part 2 · Deploy your own `materialize-llm` function

`materialize-master` turns your **regex** JSON into `listings_master.csv`. You make a copy that turns your **Gemini**
JSON into `listings_master_llm.csv`. Everything is a **new file**, so your regex pipeline keeps running and Sync fork
keeps working. Do all of Part 2 on **one branch** (for example `dev-materialize-llm`).

## Step 6 · Copy the function code
1. In your fork, open `cloud_function/materialize-master/main.py` → click **Raw** → copy everything.
2. Back on your fork's main page: **Add file → Create new file**. Name it `cloud_function/materialize-llm/main.py`
   (typing the `/` makes the folders) and paste.
3. Make **3 edits** in the new file:

| Find | Change it to | Why |
|---|---|---|
| `prefix = f"{structured_prefix}/run_id={run_id}/jsonl/"` | `.../jsonl_llm/"` | read Gemini's output, not the regex output |
| `final_key = f"{base}/listings_master.csv"` | `listings_master_llm.csv` | write a separate CSV, so the regex one is untouched |
| `CSV_COLUMNS = [` ... `]` | add your new fields, e.g. `"transmission", "title_status",` | only listed columns are written to the CSV |

4. **Commit changes… → Create a new branch** `dev-materialize-llm` (stay on this branch for the next two files).
5. Do the same for `cloud_function/materialize-master/requirements.txt` → new file `cloud_function/materialize-llm/requirements.txt` (no edits).

## Step 7 · Copy the deploy workflow
Copy `.github/workflows/deploy-materialize-master.yml` into a new file `.github/workflows/deploy-materialize-llm.yml`
on the same branch, with **4 edits**:

| Find | Change it to |
|---|---|
| `name: Deploy materialize-master (CF Gen2 + Cloud Scheduler)` | `name: Deploy materialize-llm (CF Gen2 + Cloud Scheduler)` |
| `- 'cloud_function/materialize-master/**'` and `- '.github/workflows/deploy-materialize-master.yml'` | `- 'cloud_function/materialize-llm/**'` and `- '.github/workflows/deploy-materialize-llm.yml'` |
| `FUNCTION_NAME: materialize-master` and `FUNCTION_DIR: cloud_function/materialize-master` | `FUNCTION_NAME: materialize-llm` and `FUNCTION_DIR: cloud_function/materialize-llm` |
| `CRON_EXPR: "15 * * * *"   # :15 each hour` | `CRON_EXPR: "17 * * * *"   # :17, after Gemini at :12` |

## Step 8 · Pull request, merge, watch it deploy
Open the pull request for `dev-materialize-llm`. **Files changed** should show **3 new files** and nothing else.
Merge it. In **Actions**, a new workflow, **Deploy materialize-llm**, runs by itself. Wait for the green check.

## Step 9 · Proof 2: materialize-llm runs
Is the new function there, with its hourly job? Then run it now instead of waiting for :17.
```bash
gcloud functions describe materialize-llm --region="${REGION}" --gen2 --format='value(state,updateTime)'
gcloud scheduler jobs run materialize-llm-hourly --location="${REGION}"
```
Wait about 20 seconds. **Screenshot this for your post** (the output CSV and its size):
```bash
gcloud storage ls -l "gs://${BUCKET_NAME}/structured/datasets/"
```

## Step 10 · Proof 3: the new CSV has your fields
The header and first rows of `listings_master_llm.csv`:
```bash
gcloud storage cat "gs://${BUCKET_NAME}/structured/datasets/listings_master_llm.csv" | head -6
```
A tally of one new column, straight from the CSV (swap in your field name):
```bash
gcloud storage cat "gs://${BUCKET_NAME}/structured/datasets/listings_master_llm.csv" | python3 -c "import csv, sys, collections; print(collections.Counter(row.get('transmission') for row in csv.DictReader(sys.stdin)).most_common())"
```
Something failed? Read the function's log and paste it into Claude:
```bash
gcloud functions logs read materialize-llm --region="${REGION}" --gen2 --limit=20
```

---

## Step 11 · Compare Gemini and your regex
Open the [A07 notebook in Colab](https://colab.research.google.com/github/drdave-teaching/OPIM5512-notebooks/blob/main/Module3/M3_3_GenAI_ETL.ipynb)
and run **"Grade Gemini on your Lab 3 truth table"**: Gemini scored on the same 5 cars you graded the regex on in Lab 3.
Then look at `make` and `model` in the two CSVs side by side. How much better do they look?

---

**For your A07 post (all or nothing: customize it and deploy it):**
1. Your schema change (the pull request's Files changed) and **Proof 1**, the tally for each new field
2. **Proof 2**: `materialize-llm` ran and wrote `listings_master_llm.csv`
3. **Proof 3**: the CSV with your new columns
4. Why you chose your fields, what Gemini was good at extracting, and where it beat (or struggled against) your regex
