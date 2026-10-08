# A06 · Ship your regex

**OPIM 5512 · Module 3.2 · Update the ETL · Group discussion · Due Friday, October 16, 11:59 PM**

📺 **Watch first:** [A06 walkthrough video (6 min)](https://lms.uconn.edu/webapps/blackboard/execute/blti/launchLink?course_id=_200751_1&content_id=_14866015_1) (opens in HuskyCT; sign in first): Dr. Wanik does every step below on his own fork.

In Lab 3 you wrote a regular expression that pulls the right make and model, but only inside a notebook. Your pipeline
on Google Cloud is still using the old one. This week you **ship** it: change one line in your pipeline's code on a
branch, review it in a pull request, merge it, and watch GitHub redeploy your extractor by itself. That is CI/CD.

**Time:** about 30 minutes. **You change exactly one line.**

---

## Why a branch?
Only `main` deploys. The workflows run on `main`, and Google Cloud only trusts `main`. So a branch is a safe sandbox:
you can edit, commit, and look at your change **without touching the running pipeline**. The pull request is your
last look before it goes live.

## Step 0 · Save your "before" (2 minutes)
Before you change anything, count the makes your pipeline has extracted so far. Open **Cloud Shell** (the `>_` icon,
top right of the Google Cloud console), run **Step 4a** below to set your names, then run the tally from **Step 5a**.
Screenshot it. Expect a lot of `Contact` and town names like `East`, `West` and `Rocky`: that is the bug you are about to fix.

## Step 1 · Make the change on a branch (pick ONE way)

### Way A: the pencil (github.com)
1. Open **your fork** on github.com → `cloud_function/extractor-per-listing/main.py`.
2. Click the **pencil** (Edit this file).
3. Find line 41:
   ```python
   MAKE_MODEL_RE = re.compile(r"\b([A-Z][a-z]+)\s+([A-Z][A-Za-z0-9]+)")
   ```
   Replace it with **your Lab 3 regex** (the line Way 2 printed for you, `re.MULTILINE` included):
   ```python
   MAKE_MODEL_RE = re.compile(r"^(?:19|20)\d{2}\n([A-Za-z-]+)\s+([A-Za-z0-9-]+)", re.MULTILINE)
   ```
   Tip: click at the start of line 41, press **Shift+End** to select the whole line, then paste. If the blank line
   under it disappears, click at the end of line 41 and press **Enter** to put it back.
4. Click **Commit changes…** → choose **Create a new branch for this commit and start a pull request** → name it
   `dev-regex` → **Propose changes**. (If GitHub suggests a name like `yourname-patch-1`, that is fine too.)

### Way B: github.dev (VS Code in the browser)
1. On your fork's main page, press the **`.`** (period) key. VS Code opens in your browser.
2. Bottom-left branch name → **Create new branch…** → `dev-regex`.
3. Open `cloud_function/extractor-per-listing/main.py`, change line 41 as above.
4. **Source Control** (left bar) → type a message → **Commit & Push**. Back on github.com, click **Compare & pull request**.

## Step 2 · Review your own pull request
- **Files changed** tab: you should see **one red line and one green line**, nothing else.
- Anything else changed (an extra space on another line, a second file)? Fix it on the branch before merging.
- Write one sentence in the PR description: what the old regex grabbed, and what yours grabs.

## Step 3 · Merge and watch it deploy
1. **Merge pull request** → **Confirm merge** → **Delete branch**.
2. **Actions** tab: **Deploy Extractor** starts by itself. Wait for the **green check** (2 to 3 minutes).
   Stuck? The [walkthrough video](https://lms.uconn.edu/webapps/blackboard/execute/blti/launchLink?course_id=_200751_1&content_id=_14866015_1) shows every click.
   *(Red X? Click it, open the failed step, and ask Claude with the full error.)*

## Step 4 · Re-extract your cars with the new regex (Cloud Shell)
New cars get your regex automatically. Your **old** cars were extracted with the old one, so send them back through
once. Open **Cloud Shell** (the `>_` icon, top right of the Google Cloud console) and paste the blocks below **one at a time**.

**The worked example uses Dr. Wanik's names.** Change the two names in 4a to yours, or let Claude do it (see the prompt below).

**4a · Tell Cloud Shell which project and bucket are yours**
```bash
gcloud config set project myscrapers-dww05002-f26-510015
REGION="us-central1"
BUCKET_NAME="myscrapers-dww05002-f26-510015"
```

**4b · Wait until the NEW extractor is live**
GitHub's green check can come a few minutes **before** Google Cloud actually serves the new code. Run this and check
that the time is **after** you clicked Merge (times are in UTC: 4 PM Eastern = 20:00 UTC). If it is older, wait a
minute and run it again.
```bash
gcloud functions describe extractor-per-listing --region="${REGION}" --gen2 --format='value(updateTime)'
```

**4c · Re-run every old batch through the new extractor**
Each batch prints a line with `"ok":true`. It takes about a minute.
```bash
URL="$(gcloud functions describe extractor-per-listing --region="${REGION}" --gen2 --format='value(serviceConfig.uri)')"
for RUN in $(gcloud storage ls "gs://${BUCKET_NAME}/scrapes/" | awk -F/ '{print $(NF-1)}'); do
  curl -s -X POST -H "Authorization: Bearer $(gcloud auth print-identity-token)" -H "Content-Type: application/json" \
       -d "{\"run_id\":\"${RUN}\",\"overwrite\":true}" "${URL}"
  echo
done
```

**4d · Rebuild your master table** (the same as Force run on `materialize-master-hourly` in Cloud Scheduler)
```bash
gcloud scheduler jobs run materialize-master-hourly --location="${REGION}"
```
Wait about 20 seconds before Step 5. (Forget this step and your master table keeps the old values until the next
hourly run. That is the #1 "it didn't work!" in this assignment.)

> **Personalize it with Claude.** Paste this prompt, then all of Step 4:
> *"Here are Cloud Shell commands from my OPIM 5512 A06 instructions. My Google Cloud project ID is ____ and my bucket
> name is ____ (region us-central1). Rewrite the commands with my names, change nothing else, and tell me what each
> block does in one sentence."*
> Not sure of your names? They are the `PROJECT_ID` and `BUCKET_NAME` you used in the Final GCP Guide F26 (Step 1).

## Step 5 · Prove it worked
**5a · Count the makes in your master table** (the before-and-after in one line):
```bash
gcloud storage cat "gs://${BUCKET_NAME}/structured/datasets/listings_master.csv" | cut -d, -f6 | sort | uniq -c | sort -rn | head -12
```
Before your fix, the top "make" was `Contact` (plus town names like `East`, `West`, `Rocky`). After it, you should see
real brands: `honda`, `toyota`, `ford`... Still seeing `Contact`? Go back to 4b: the loop probably ran before the new
extractor was live. Run 4c and 4d again.

**5b · Peek at a few rows** (price, year, make, model, mileage):
```bash
gcloud storage cat "gs://${BUCKET_NAME}/structured/datasets/listings_master.csv" | cut -d, -f4-8 | head -10
```

**5c · Re-run your Lab 3 notebook on your own data** (untick `USE_BACKUP_DATA`). The **original extractor** column
is now **your regex, running in the cloud**, and it should match your Way 2 column from Lab 3.

## What to post in the A06 discussion
Due **Friday, October 16, 11:59 PM**. Post in your group's A06 thread:

1. A screenshot of your **merged pull request** (the one-line diff).
2. A screenshot of the **green Deploy Extractor** run.
3. Your **make tally before and after** (Step 0 and Step 5a screenshots).
4. One sentence: which ads does your regex still miss, and why?
5. Reply to at least one groupmate: did their tally change the same way yours did?

## Rules that keep your fork healthy
- Change **only** that one line. Keep your own analysis in separate files (notebooks).
  That way **Sync fork** keeps working when Dr. Wanik updates the course code.
- Made a mess? On the merged PR, click **Revert** → merge the revert PR. You are back where you started.

---
*Stretch (the original A06 idea): add a new field to `parse_listing` (for example `transmission` or `condition`,
both sit in the details block) and add it to `CSV_COLUMNS` in materialize-master. Same branch → PR → merge loop.*
