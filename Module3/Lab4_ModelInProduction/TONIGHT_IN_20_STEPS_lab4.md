# Lab 4: Deploying Your Model to Production · Tonight in 20 Steps

**OPIM 5512 · Module 3 · Solo · Colab · Dr. Wanik's 453 Hartford cars, then your own Google Cloud bucket**

> **The one-sentence version: fit a really good model, deploy it to Google Cloud, and watch it price every new car.**
> You beat the baseline, tune three model families, check your champion with your own plots, ship it to your bucket,
> and see the prices (and the SHAP "why") production saves for brand-new cars.

---

## Before we start

- [ ] **`predict-shap` is deploying** (notebook Part 0): Sync fork → **Update branch** (A), or Actions → **Deploy predict-shap** → **Run workflow** (B), or the Cloud Shell block (C)
- [ ] **2-step verification is on** for your Google Cloud Gmail (Google Cloud may ask; click **Enable MFA**)
- [ ] You know your **project ID** and **bucket name** (usually the same)
- [ ] The notebook is open: HuskyCT → In-Class Labs → **Lab 4: Deploying Your Model to Production**

> ### ⚠️ The 3 things that trip everyone up (read this first)
> 1. **Save your work:** the notebook opens from GitHub, so first do **File → Save a copy in Drive**.
> 2. **The Google pop-up in 6b: pick the Gmail you used for Google Cloud.** Wrong account = "cannot see the bucket".
> 3. **Part 7 says exactly 500 cars?** You have more than 500 in your bucket. Production prices 500 per run; the rest
>    come at the next :25. Nothing is broken.

---

## The 20 steps, in order

### Part 0–1 · Start up and load (steps 1–4, 15 min)
1. Open the notebook from HuskyCT → **File → Save a copy in Drive** (work in the copy).
2. **Part 0:** find your case (A, B or C) and get `predict-shap` deploying. It takes about 3 minutes, so start it now.
3. **1a:** run the install cell (scikit-learn 1.6.1, shap 0.48.0). Asked to restart? Restart, then **Runtime → Run all** later.
4. **1b:** leave `USE_MY_OWN_DATA = False`, type your **PROJECT_ID** and **BUCKET_NAME** → run → **453 cars, 9 columns**.

### Part 2 · Clean (steps 5–6, 10 min)
5. **2a:** see the mess (`Ford` vs `ford`, `chevy` vs `chevrolet`), then run `clean_cars`: one name per brand.
6. **2b:** run the flags (odd price, placeholder miles, very old) → **6 flagged, 447 ready**. Read why each one was flagged.

### Part 3 · Baseline (steps 7–8, 10 min)
7. **3a–3b:** split (**357 training / 90 test**), then **peek inside the recipe**: 4 inputs become **98 columns**.
8. **3c–3d:** the numbers to beat: guess the median, then the plain tree (`train_cv_mae` **± std**, and `test_mae`).

### Part 4 · Tune (steps 9–11, 25 min)
9. Run the grid search (1–2 minutes): a decision tree, a random forest and KNN, each scored with 5-fold CV.
10. **Class challenge:** add values to any grid, re-run, and try for the lowest `train_cv_mae`. Post your best!
11. **Your champion** is picked for you (lowest `train_cv_mae`). Want another? Uncomment the second line.

### Your turn · You write the code (steps 12–13, 15 min)
12. Run the setup cell, then code **Task 1** (actual vs predicted scatter) and **Task 2** (error histogram), champion vs baseline.
13. Code **Task 3** (summary stats table). Talk it over: where does your champion beat the baseline?

### Part 5 · Explain (steps 14–15, 20 min)
14. Run the two helpers, then SHAP on your test cars: the **bar chart** and the **beeswarm** (the global picture).
15. **One car** (waterfall), then **5b: price a car you know**. Never-seen make? It says so (the "infrequent" bucket).

### Part 6 · Ship it (steps 16–18, 20 min)
16. **6a:** save `model.joblib` and `model_card.json` (the label production reads).
17. **6b:** sign in (pick your **Google Cloud Gmail**) → 3 checks: account, bucket, `predict-shap` ACTIVE. **6c:** upload.
18. **6d:** run `predict-shap` now → dots → **"Done: predict-shap wrote your predictions"** + your two file paths.

### Part 7 · Your model at work (step 19, 5 min)
19. **7a:** run it (plumbing). **7b:** the newest cars your model never saw, with its prices **and** SHAP values. Click the
    link and open `preds_master.csv` and `shap_master.csv` in Google Cloud.

### Part 8 · Wrap up (step 20, 5 min)
20. Answer the **five short questions** → **File → Download → .ipynb** → upload to **Submit Lab 4**
    (due **Thu Oct 22, 11:59 PM**, Hartford and Stamford).

---

## Your two production files (they grow every hour at :25)

| File | What is in it |
|---|---|
| `gs://YOUR-BUCKET/structured/preds_lab4/preds_master.csv` | every car, its asking price, your model's price, the error, the model version |
| `gs://YOUR-BUCKET/structured/preds_lab4/shap_master.csv` | the base value and the 4 SHAP values behind each price |

## If you get stuck

| You see | Do this |
|---|---|
| "Type your champion..." or a missing variable | Run every cell above it first (Runtime → Run before) |
| 6b: "cannot see the bucket" | Runtime → Disconnect and delete runtime, run again, pick your Google Cloud Gmail |
| 6b: "predict-shap is not ACTIVE" | Part 0: look for a red X in Actions (A/B), or re-run the Cloud Shell block (C) |
| 6d: "Nothing new after 4 minutes" | Run the optional log cell under 6d and paste the log into Claude |
| Part 7: "DEMO MODE" | Run 6d first, then re-run 7a |

**Leave `predict-shap` running.** Every hour it prices and explains your newest cars; that is your midterm data.
