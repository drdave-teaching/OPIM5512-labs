# A08 Midterm: Regex Model vs Gemini Model, Run Like a Real Experiment

**OPIM 5512 · Module 3 · Solo · Due Friday, Oct 30, 11:59 PM · Builds on Lab 4 (your regex model) and A07 (your Gemini fields)**

> **The one-sentence version: does a price model built on your Gemini features beat your Lab 4 regex model, and why?**
> You answer it the way a data science team does at work: a fair test, a check that the result is real and not luck,
> plots that explain the winner, a deployed model, and a short memo for your manager.

**See it done first.** Dr. Wanik ran this exact experiment on his own cars:
[his notebook, every chart included](https://github.com/drdave-teaching/OPIM5512-notebooks/blob/main/Module3/A08_Midterm_WorkedExample_DrWanik.ipynb) and [his one-page memo](handouts/DrWanik_Bakeoff_Memo.pdf). His answer: on the newest cars and on 21 of 25 paired folds the Gemini model won,
about $150 better per car, and **all** of the gain came from the new A07 fields (Gemini reading the same 4 fields was
no better than regex). On his small training window alone it was a tie, which is why the "real or luck" check matters.
Your cars, your fields, your answer may differ. That is the point.

---

## Before you start (5 minutes)

- [ ] Your **A07 is done**: `listings_master_llm.csv` exists in your bucket with your new columns (A07 Proof 3)
- [ ] Your **Lab 4 model is still live**: `predict-shap` has been pricing new cars every hour since Lab 4
- [ ] Run the notebook **after Oct 28**, so the test window (Oct 21 to 28) is complete

---

## Part 1 · Run the experiment (40%)

Open the **[midterm starter notebook](https://colab.research.google.com/github/drdave-teaching/OPIM5512-notebooks/blob/main/Module3/A08_Midterm_Bakeoff_STARTER.ipynb)**
(**File → Save a copy in Drive**), type your project ID and bucket name in Part 0, and run it top to bottom (it reads
both tables straight from your bucket, like Lab 4). It is the same notebook as
Dr. Wanik's report, set up for your data: it finds your new Gemini columns by itself.

**The fair-test rules (already built in; do not change them):**

| Rule | What it means |
|---|---|
| Same cars | both tables joined on `post_id`; a car flagged in either table is dropped from both |
| Same target | the asking price |
| Same calendar | **train on cars scraped through Oct 20, test on cars scraped Oct 21 to Oct 28** (the same for everyone) |
| Same recipe | Lab 4's cleaning, flags, model families, grids, seed and 5-fold CV |
| One change | only the feature list: v1 = regex's 4, v1.5 = Gemini's 4, v2 = Gemini's 4 + your new fields |

**What the notebook gives you, and what you write under each ✍️ Your turn (2 to 3 sentences each):**

1. **Agreement:** how often regex and Gemini agree on price, year, make, model, mileage. Where do they disagree?
2. **Scoreboard:** `train_cv_mae` and `test_mae` for all 3 families × 3 versions. Which champion wins?
3. **Real or luck:** the 25 paired folds. On how many does v2 win, and what is the interval for the improvement?
4. **Ablation:** how much of the change came from **reading better** (v1 → v1.5) vs **new fields** (v1.5 → v2)?
5. **Actual vs predicted:** the two scatterplots. Where does each model miss?
6. **Permutation importance:** which inputs does each model lean on? Did any new field matter?
7. **SHAP:** bar + beeswarm for both models. Does mileage still dominate once Gemini adds your fields?
8. **Partial dependence:** year and mileage for both, and your new fields for v2. Do the shapes make sense for cars?
9. **Same car, scored twice:** pick 3 test cars (one v2 nails, one it misses, one you find interesting). **Read the ads.**
   Were the Gemini fields right?
10. **More data:** the MAE-vs-number-of-cars curves. Is either model still improving?

---

## Part 2 · Ship the winner (20%)

1. **Sync fork once** (GitHub → your myscrapers fork → **Sync fork → Update branch**). This updates `predict-shap` so it
   reads the feature list from your model card: **no code edits**.
2. Run the starter's **Part 2. Ship the winner** cell. It trains your winner on all your cars and uploads it with a model
   card that tells production which features it needs and which table to read (`listings_master_llm.csv`).
3. **Proof:** after the next :25, a screenshot of `preds_master.csv` showing your new `model_version` (and
   `shap_master.csv` with a `shap_` column for each of your new fields).

If v1 wins, ship v2 anyway (set `SHIP = V2`): production is your proof that a Gemini-feature model runs in the cloud.

---

## Part 3 · How did your Lab 4 model do in the real world? (15%)

Your frozen Lab 4 model has priced every new car since Lab 4 night. The starter's Part 3 section reads your
`preds_master.csv`, keeps the cars your model **never saw**, drops flagged asking prices, and gives you the
**production MAE** next to your **Lab 4 test MAE**. Close, or far apart? Plot the error by day: does it drift?

---

## Part 4 · Tell your manager (25%)

A **1 to 2 page memo** (like [Dr. Wanik's](handouts/DrWanik_Bakeoff_Memo.pdf)) **or** a **Looker Studio dashboard**
a manager or recruiter could read. Four short sections, with your numbers:
1. **The result:** which model won, by how much, on how many of the 25 folds.
2. **Why:** reading better vs new fields; which fields mattered (permutation importance, SHAP).
3. **The cost:** Gemini is about $2 per 1,000 cars and about 5 seconds per car; the regex is essentially free.
   Worth it?
4. **The call:** what is live now, and what you would test next.

---

## Submit (HuskyCT → A08 Midterm)

- Your notebook (**File → Download → .ipynb**), run top to bottom
- Your memo (PDF) or your dashboard link
- The Part 2 screenshot

## If you get stuck

| You see | Do this |
|---|---|
| "No new Gemini columns found" | Your A07 Edit 3 (`out_record`) is missing: A07 Step 2, then Step 4 to re-read old cars |
| Very few test cars (under 30) | Check your scraper is still running; tell Dr. Wanik (he will adjust your window) |
| `predict-shap` says "your model needs columns ..." | Your model card is missing `data_key`: re-run the starter's Part 2 cell |
| `predict-shap` ignores your new fields | You skipped Sync fork in Part 2, step 1 |
| Anything else | Paste the cell, the full error and what you expected into Claude |
