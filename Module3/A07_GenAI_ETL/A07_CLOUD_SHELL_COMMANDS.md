# A07 · Commands and steps: GenAI for ETL

**OPIM 5512 · Module 3.3 · Part 1: new Gemini fields · Part 2: your own `materialize-llm` function**

Your pipeline already asks Gemini to read every ad (the `extractor-llm-poc` function, every hour at :12). In A07 you
(1) teach it to return **new fields** (choose different or more fields than your A06 regex: transmission, body type,
fuel, color, title status, condition, location...), and (2) deploy a **new** Cloud Function, `materialize-llm`, that
collects Gemini's output into its own growing CSV, while your regex pipeline keeps running untouched. Then you compare
the two.

> **See it done first: Dr. Wanik's A07 (same steps, his fork).** Open each pull request and click **Files changed**:
> - [Part 1: Gemini extracts 10 new fields](https://github.com/drdww/myscrapers-f26-v2/pull/2/files) (one file, three edits)
> - [Part 2: materialize-llm](https://github.com/drdww/myscrapers-f26-v2/pull/3/files) (three new files)
>
> His 10 fields: `trim`, `body_type` (convertible is one), `drivetrain`, `transmission`, `fuel_type`, `exterior_color`,
> `title_status`, `condition`, `leather_seats`, `city`. **You may use the same 10** (the blocks in Step 2 are ready to
> paste), or swap in your own ideas: `sunroof`, `num_owners`, `accident_history`, `seller_type` (dealer or private),
> `cylinders`, `backup_camera`, `needs_repair`... Every field you add becomes a new column for your midterm model.

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

## Step 2 · Three edits in ONE file (on a branch, exactly like A06)
In **your fork**, open `cloud_function/extractor-llm-poc/main.py` and click the pencil. You make **three edits**, all
in this file. Each block below is ready to paste (Dr. Wanik's 10 fields); delete or rename lines to make them yours,
but **use the same field names in all three places**.

**Edit 1 · The schema** (what Gemini must return). Find `"mileage": {"type": "integer", "nullable": True},` inside
`_vertex_extract_fields()` (around line 181) and paste this right **below** it. An `enum` is a fixed list of answers, so
your column comes out clean (`automatic`, never `Auto` or `AT`). Leave new fields **out** of `"required"`: forcing
them invites made-up answers.
```python
            # ---- A07: 10 new fields (left OUT of "required" so Gemini can say null instead of guessing) ----
            "trim": {"type": "string", "nullable": True},
            "body_type": {"type": "string", "nullable": True,
                          "enum": ["sedan", "suv", "truck", "coupe", "convertible", "hatchback", "wagon", "minivan", "van", "other"]},
            "drivetrain": {"type": "string", "nullable": True, "enum": ["fwd", "rwd", "awd", "4wd"]},
            "transmission": {"type": "string", "nullable": True, "enum": ["automatic", "manual"]},
            "fuel_type": {"type": "string", "nullable": True, "enum": ["gas", "diesel", "hybrid", "electric"]},
            "exterior_color": {"type": "string", "nullable": True,
                               "enum": ["black", "white", "silver", "gray", "blue", "red", "green", "brown", "beige", "gold", "yellow", "orange", "purple", "other"]},
            "title_status": {"type": "string", "nullable": True, "enum": ["clean", "rebuilt", "salvage", "lien", "missing", "parts only"]},
            "condition": {"type": "string", "nullable": True, "enum": ["new", "like new", "excellent", "good", "fair", "salvage"]},
            "leather_seats": {"type": "boolean", "nullable": True},
            "city": {"type": "string", "nullable": True},
```

**Edit 2 · The instructions** (how Gemini should decide). A few lines below, the `sys_instr` text ends with
`"do not infer values not explicitly present; do not add extra keys."`. Replace that **one line** with:
```python
        "do not infer values not explicitly present; do not add extra keys. "
        # ---- A07: rules for the new fields ----
        "trim: the trim level only (e.g. 'LX', 'Sport', 'Limited'), not the make or model. "
        "body_type: you MAY infer it from a well-known make and model (a Honda CR-V is an suv). "
        "drivetrain, transmission, fuel_type, exterior_color, title_status, condition: use the ad's own "
        "attribute lines (like 'drive: 4wd' or 'paint color: white') or clear statements in the text; a CVT counts as automatic. "
        "leather_seats: true only if the ad mentions leather seats or leather interior, false only if it says cloth seats, otherwise null. "
        "city: the town in parentheses after the price, e.g. '(Avon)' -> 'Avon'."
```

**Edit 3 · Save the answers** (everybody forgets this one). Gemini's answers are only saved if they are listed in
`out_record`. A field missing here never reaches your CSV. Find `"mileage": parsed.get("mileage"),` inside
`out_record = {` (around line 340) and paste this right **below** it:
```python
                    # ---- A07: write the new fields too (a field missing here never reaches your CSV) ----
                    "trim": parsed.get("trim"),
                    "body_type": parsed.get("body_type"),
                    "drivetrain": parsed.get("drivetrain"),
                    "transmission": parsed.get("transmission"),
                    "fuel_type": parsed.get("fuel_type"),
                    "exterior_color": parsed.get("exterior_color"),
                    "title_status": parsed.get("title_status"),
                    "condition": parsed.get("condition"),
                    "leather_seats": parsed.get("leather_seats"),
                    "city": parsed.get("city"),
```
Python is picky about spaces: keep each pasted line lined up with the line above it. Then **Commit changes… → Create
a new branch → pull request → Files changed** (compare with
[Dr. Wanik's](https://github.com/drdww/myscrapers-f26-v2/pull/2/files)) **→ Merge**. GitHub Actions runs
**Deploy LLM Extractor** by itself; wait for the green check (about 2 minutes). A red X? Open it, copy the error, and
paste it into Claude with your three edits.

## Step 3 · Wait until the NEW Gemini extractor is live
The time printed must be **after** you clicked Merge (UTC: 4 PM Eastern = 20:00).
```bash
gcloud functions describe extractor-llm-poc --region="${REGION}" --gen2 --format='value(updateTime)'
```

## Step 4 · Re-read your old cars with the new schema
New cars get your new fields automatically. This sends every old batch back through Gemini, 3 batches at a time
(your extractor runs at most 3 copies at once), with automatic retries. It costs about one Gemini call per car (a few
cents for a few hundred cars) and takes **about 15 to 25 minutes for 150 batches** (Dr. Wanik's 153 batches: 16 minutes, 0 errors). Each batch
prints one line that starts `{"errors":0,...,"ok":true`. Start it, keep the Cloud Shell tab open, and work on something
else; you are done when your prompt comes back.
```bash
URL="$(gcloud functions describe extractor-llm-poc --region="${REGION}" --gen2 --format='value(serviceConfig.uri)')"
reread() {
  curl -s --retry 3 --retry-delay 5 -X POST -w '\n' "${URL}" \
       -H "Authorization: Bearer $(gcloud auth print-identity-token)" -H "Content-Type: application/json" \
       -d "{\"run_id\":\"$1\",\"overwrite\":true}" | cut -c1-60
}
export URL
export -f reread
gcloud storage ls "gs://${BUCKET_NAME}/structured/" | grep "run_id=" | awk -F'run_id=' '{print $2}' | tr -d '/' \
  | xargs -P 3 -I{} bash -c 'reread {}'
```
Peek at one re-read car (your new fields should be in it, like `"transmission":"automatic"`):
```bash
gcloud storage cat "$(gcloud storage ls "gs://${BUCKET_NAME}/structured/**/jsonl_llm/*.jsonl" | head -1)"
```

## Step 5 · Proof 1: Gemini is extracting your new field
Run this **after Step 4 finishes**. It counts the answers Gemini gave for each new field across all your cars (put your own field names in `FIELDS`).
**Screenshot this for your post.**
```bash
gcloud storage cat "gs://${BUCKET_NAME}/structured/**/jsonl_llm/*.jsonl" | python3 -c "
import json, sys, collections
FIELDS = ['body_type', 'drivetrain', 'transmission', 'fuel_type', 'exterior_color', 'title_status', 'condition', 'leather_seats']
rows = [json.loads(line) for line in sys.stdin if line.strip()]
print(len(rows), 'cars read by Gemini')
for f in FIELDS:
    print(f, collections.Counter(r.get(f) for r in rows).most_common(6))
"
```
Every field shows only `None`? Back to Step 3: Gemini probably re-read the cars before the new code was live. Run Step 4 again.

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
| `"source_txt"` (the last name inside `CSV_COLUMNS = [ ... ]`) | `"source_txt",` then your field names: `"trim", "body_type", "drivetrain", "transmission", "fuel_type", "exterior_color", "title_status", "condition", "leather_seats", "city",` | only listed columns are written to the CSV |

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
Wait about a minute. **Screenshot this for your post** (the output CSV and its size):
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
