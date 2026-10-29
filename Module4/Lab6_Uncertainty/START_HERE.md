# Lab 6: Low, Expected and High (Forecast Uncertainty in Production) · **START HERE**

> Submit by **Fri Nov 20, 11:59 PM** (Hartford and Stamford).

**Solo · three notebooks · Colab · your Lab 5 energy project on Google Cloud.**
Your Lab 5 model gives one number per hour. Tonight it learns to say **how sure it is**: a low, an expected and a high
load for every hour, an honest **80% range**. Two things make a forecast uncertain, and you handle both:
the **weather forecast** is wrong sometimes (6A), and **your model** misses even with perfect weather (6B). In 6C you
combine them, ship the range, and go on the Lab 6 leaderboard, ranked by **CRPS**.

| | What | Link |
|---|---|---|
| 🌦️ | **6A · Your frozen model meets the HRRR** (NOAA's hourly 3 km weather model, through hefty and dynamical.org) | [Lab6A_Frozen_Model_Meets_HRRR.ipynb](https://colab.research.google.com/github/drdave-teaching/OPIM5512-notebooks/blob/main/Module4/Lab6A_Frozen_Model_Meets_HRRR.ipynb) |
| 🎯 | **6B · How sure is your model?** Random forest spread vs quantile forest, scored by CRPS | [Lab6B_Model_Uncertainty_RF_vs_QRF.ipynb](https://colab.research.google.com/github/drdave-teaching/OPIM5512-notebooks/blob/main/Module4/Lab6B_Model_Uncertainty_RF_vs_QRF.ipynb) |
| 🚀 | **6C · Two kinds of uncertainty, one range, live** (pool the quantile forest over 8 HRRR runs, ship it) | [Lab6C_Combine_and_Ship.ipynb](https://colab.research.google.com/github/drdave-teaching/OPIM5512-notebooks/blob/main/Module4/Lab6C_Combine_and_Ship.ipynb) |
| 📊 | **The weather data** (every HRRR run at Bradley since 2023, as issued, + RTMA) | [data/README.md](https://github.com/drdave-teaching/OPIM5512-notebooks/blob/main/Module4/data/README.md) |
| 🧠 | **Your energy repo** (Sync fork in 6C Part 0) | [drdave-teaching/energy-forecasting](https://github.com/drdave-teaching/energy-forecasting) |
| 🏆 | **Class leaderboard** (Lab 6 table: ranges ranked by CRPS) | [opim5512-leaderboard-f26](https://storage.googleapis.com/opim5512-leaderboard-f26/index.html) |
| 🛠️ | **hefty** by Will Hobbs (open source; 6A Part 4 has an idea for your first contribution) | [github.com/williamhobbs/hefty](https://github.com/williamhobbs/hefty) |

## Before you start
- [ ] Your Lab 5 model is live: `forecast-24h` writes a forecast every hour and you're on the leaderboard
- [ ] You know your **energy project ID** and **bucket name**
- [ ] Do the notebooks **in order**: 6A, then 6B, then 6C. Open each in Colab, then File → Save a copy in Drive.

## The three notebooks

| Notebook | You do | You get |
|---|---|---|
| **6A** | Load your frozen model; pull tomorrow's HRRR forecast with **hefty**; compare it with the NWS forecast production uses; replay 2026 with the HRRR forecast you'd really have had 1, 12 and 24 hours ahead, graded with **RTMA** | How many MW weather error costs your model; 8 HRRR runs that disagree about tomorrow |
| **6B** | Learn the **CRPS**; build a range two ways: the spread of a random forest's trees vs a **quantile regression forest** at the 10th and 90th percentiles | An honest 80% range... with perfect weather only |
| **6C** | **Sync fork**; rebuild the 8 runs for every hour of 2026; compare model-only, weather-only and **pooled**; upload `model_qrf.joblib`; run `forecast-24h` | Your range, live every hour, on the Lab 6 leaderboard |

Heads up: 6A installs hefty, which needs a newer pandas, so **Colab restarts once** after the first cell. Wait for
"Connected", run the first cell again, and keep going.

## What changes in your energy project (6C)
- Every hour at **:05**, Dr. Dave's class job saves the 8 newest HRRR runs at Bradley to one public file.
- At **:20** your `forecast-24h` (after Sync fork) reads it, runs your quantile forest on every run, pools the answers,
  and writes `predicted_low_mw`, `predicted_load_mw` and `predicted_high_mw`.
- Your Lab 5 `model.joblib` stays in the bucket as the backup. To go back to Lab 5 behavior, upload your old model card.

## Submit Lab 6 (HuskyCT text box)
1. The **"Range is live"** line from 6C Part 5b
2. Your answers to questions **1 to 12** (1-4 in 6A, 5-8 in 6B, 9-12 in 6C), numbered, a sentence or two each

## Stuck?
Paste the error and the cell into Claude. For `forecast-24h` problems, run the troubleshooting log cell in 6C Part 5b and
paste the newest log line.
