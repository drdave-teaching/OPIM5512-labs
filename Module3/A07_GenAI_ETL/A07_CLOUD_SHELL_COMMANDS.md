# A07 · Cloud Shell commands: Gemini as your extractor

**OPIM 5512 · Module 3.3 · Copy, paste, read the answer**

Your pipeline already asks Gemini to read every ad (the `extractor-llm-poc` function, every hour at :12). In A07 you
teach it to return **new fields** (transmission, color, condition, ...), ship the change the same way as A06, and check
the results. Open **Cloud Shell** (the `>_` icon, top right of the Google Cloud console) and paste the blocks **one at a time**.

**The worked example uses Dr. Wanik's names.** Change the names in Step 0 to yours, or let Claude do it:

> **Personalize it with Claude.** Paste this prompt, then this whole page:
> *"Here are Cloud Shell commands from my OPIM 5512 A07 instructions. My Google Cloud project ID is ____ and my bucket
> name is ____ (region us-central1). Rewrite the commands with my names, change nothing else, and tell me what each
> block does in one sentence."*

---

## Step 0 · Tell Cloud Shell which project and bucket are yours
```bash
gcloud config set project myscrapers-dww05002-f26-510015
REGION="us-central1"
BUCKET_NAME="myscrapers-dww05002-f26-510015"
```

## Step 1 · Is Gemini keeping up?
Two counts: ads extracted by your regex, and ads read by Gemini. They should match (Gemini runs 2 minutes after the
regex extractor). If Gemini is behind, run Step 2.
```bash
gcloud storage ls "gs://${BUCKET_NAME}/structured/**/jsonl/*.jsonl" | wc -l
gcloud storage ls "gs://${BUCKET_NAME}/structured/**/jsonl_llm/*.jsonl" | wc -l
```

## Step 2 · Force run Gemini (catches up on every batch it has not read yet)
```bash
gcloud scheduler jobs run extractor-llm-poc-hourly --location="${REGION}"
```

## Step 3 · What did Gemini write for one car?
Prints the newest Gemini record: `price`, `year`, `make`, `model`, `mileage`, plus which model answered.
```bash
gcloud storage cat "$(gcloud storage ls "gs://${BUCKET_NAME}/structured/**/jsonl_llm/*.jsonl" | tail -1)"
```

## Step 4 · Add your new fields (on a branch, exactly like A06)
In **your fork**, open `cloud_function/extractor-llm-poc/main.py` and find the `schema` (around line 181). Add one line
per new field inside `"properties"`, for example:
```python
            "transmission": {"type": "string", "nullable": True},
            "paint_color": {"type": "string", "nullable": True},
```
Then: **Commit changes… → Create a new branch → pull request → check Files changed → Merge**. GitHub Actions runs
**Deploy LLM Extractor** by itself. (Want Gemini to stick to a fixed list, like `automatic` / `manual`? Say so in the
`sys_instr` text a few lines below the schema.)

## Step 5 · Wait until the NEW Gemini extractor is live
The time printed must be **after** you clicked Merge (UTC: 4 PM Eastern = 20:00).
```bash
gcloud functions describe extractor-llm-poc --region="${REGION}" --gen2 --format='value(updateTime)'
```

## Step 6 · Re-read your old cars with the new schema
New cars get your new fields automatically. This sends every old batch back through Gemini. It makes about one
Gemini call per car (a few cents for a few hundred cars), and each batch prints a line with `"ok":true`.
```bash
URL="$(gcloud functions describe extractor-llm-poc --region="${REGION}" --gen2 --format='value(serviceConfig.uri)')"
for RUN in $(gcloud storage ls "gs://${BUCKET_NAME}/structured/" | grep "run_id=" | awk -F'run_id=' '{print $2}' | tr -d '/'); do
  curl -s -X POST -H "Authorization: Bearer $(gcloud auth print-identity-token)" -H "Content-Type: application/json" \
       -d "{\"run_id\":\"${RUN}\",\"overwrite\":true}" "${URL}"
  echo
done
```

## Step 7 · Did it work? Tally your new field
Counts every value Gemini returned for `transmission` across all your cars. Swap in any field you added.
```bash
gcloud storage cat "gs://${BUCKET_NAME}/structured/**/jsonl_llm/*.jsonl" | grep -o '"transmission": *"[^"]*"' | sort | uniq -c | sort -rn
```
Expect something like `180 "transmission": "automatic"` and `31 "transmission": "manual"`. Nothing printed? Go back to
Step 5: Gemini probably re-read the cars before the new code was live. Run Step 6 again.

## Step 8 · Grade Gemini on your Lab 3 truth table
Open the [A07 notebook in Colab](https://colab.research.google.com/github/drdave-teaching/OPIM5512-notebooks/blob/main/Module3/M3_3_GenAI_ETL.ipynb)
and run the section **"Grade Gemini on your Lab 3 truth table"**. It scores Gemini on the same 5 cars you graded the regex
on in Lab 3. Where is the LLM smarter? Where is the regex faster, cheaper, and just as right?

---

**For your A07 post:** your schema change (the pull request's Files changed), the Step 7 tally for each new field, and
your Step 8 scores.
