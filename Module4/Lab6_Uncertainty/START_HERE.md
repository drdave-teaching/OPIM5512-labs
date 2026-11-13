# Lab 6: Low, Expected and High (Forecast Uncertainty in Production) · **START HERE**

> Submit by **Fri Nov 20, 11:59 PM** (Hartford and Stamford).

**Solo · three notebooks (plus an optional fourth) · Colab · your Lab 5 energy project on Google Cloud.**
Your Lab 5 model gives one number per hour. Tonight it learns to say **how sure it is**: a low, an expected and a high
load for every hour, an honest **80% range**. Two things make a forecast uncertain, and you handle both:
the **weather forecast** is wrong sometimes (6A), and **your model** misses even with perfect weather (6B). In 6C you
combine them, ship the range, and go on the Lab 6 leaderboard, ranked by **CRPS**. That's the Lab 6 deliverable.
**6D is optional, and recommended for the final project:** you **tune** that range, experiment after experiment,
scored on 2025, one look at 2026, and the winner goes live. Its experiment log is a ready-made "one improvement" for
your final report, and a tuned range should score better in the final project window (Nov 21 to Dec 1).

| | What | Link |
|---|---|---|
| 🌦️ | **6A · Your frozen model meets the HRRR** (NOAA's hourly 3 km weather model, through hefty and dynamical.org) | [Lab6A_Frozen_Model_Meets_HRRR.ipynb](https://colab.research.google.com/github/drdave-teaching/OPIM5512-notebooks/blob/main/Module4/Lab6A_Frozen_Model_Meets_HRRR.ipynb) |
| 🎯 | **6B · How sure is your model?** Random forest spread vs quantile forest, scored by CRPS | [Lab6B_Model_Uncertainty_RF_vs_QRF.ipynb](https://colab.research.google.com/github/drdave-teaching/OPIM5512-notebooks/blob/main/Module4/Lab6B_Model_Uncertainty_RF_vs_QRF.ipynb) |
| 🚀 | **6C · Two kinds of uncertainty, one range, live** (pool the quantile forest over 8 HRRR runs, ship it) | [Lab6C_Combine_and_Ship.ipynb](https://colab.research.google.com/github/drdave-teaching/OPIM5512-notebooks/blob/main/Module4/Lab6C_Combine_and_Ship.ipynb) |
| 🧪 | **6D · Tune your range** *(optional, recommended for the final project)* (experiment with leaf size, features per split, HRRR runs and widen; validation CRPS; ship the winner) | [Lab6D_Tune_Your_Range.ipynb](https://colab.research.google.com/github/drdave-teaching/OPIM5512-notebooks/blob/main/Module4/Lab6D_Tune_Your_Range.ipynb) |
| 📊 | **The weather data** (every HRRR run at Bradley since 2023, as issued, + RTMA) | [data/README.md](https://github.com/drdave-teaching/OPIM5512-notebooks/blob/main/Module4/data/README.md) |
| 🧠 | **Your energy repo** (Sync fork in 6C Part 0) | [drdave-teaching/energy-forecasting](https://github.com/drdave-teaching/energy-forecasting) |
| 🏆 | **Class leaderboard** (Lab 6 table: ranges ranked by CRPS) | [opim5512-leaderboard-f26](https://storage.googleapis.com/opim5512-leaderboard-f26/index.html) |
| 🛠️ | **hefty** by Will Hobbs (open source; 6A Part 4 has an idea for your first contribution) | [github.com/williamhobbs/hefty](https://github.com/williamhobbs/hefty) |

## Before you start
- [ ] Your Lab 5 model is live: `forecast-24h` writes a forecast every hour and you're on the leaderboard
- [ ] You know your **energy project ID** and **bucket name**
- [ ] Do the notebooks **in order**: 6A, then 6B, then 6C (then 6D if you're doing it). Open each in Colab, then File → Save a copy in Drive.

## The notebooks

| Notebook | You do | You get |
|---|---|---|
| **6A** | Load your frozen model; pull tomorrow's HRRR forecast with **hefty**; compare it with the NWS forecast production uses; replay 2026 with the HRRR forecast you'd really have had 1, 12 and 24 hours ahead, graded with **RTMA** | How many MW weather error costs your model; 8 HRRR runs that disagree about tomorrow |
| **6B** | Learn the **CRPS**; build a range two ways: the spread of a random forest's trees vs a **quantile regression forest** at the 10th and 90th percentiles | An honest 80% range... with perfect weather only |
| **6C** | **Sync fork**; rebuild the 8 runs for every hour of 2026; compare model-only, weather-only and **pooled**; upload `model_qrf.joblib`; run `forecast-24h` | Your range, live every hour, on the Lab 6 leaderboard |
| **6D** (optional) | Three periods (train 2023-24, tune on 2025, test 2026 once); run experiments with `try_setting()`: leaf size, `max_features`, a grid, HRRR runs and `range_widen`, seed noise, your own challenges; pick the winner by a rule; ship it | A tuned range live, plus an experiment log: your before and after for the final project report |

Heads up: 6A installs hefty, which needs a newer pandas, so **Colab restarts once** after the first cell. Wait for
"Connected", run the first cell again, and keep going.

## What changes in your energy project (6C)
- Every hour at **:05**, Dr. Dave's class job saves the 8 newest HRRR runs at Bradley to one public file.
- At **:20** your `forecast-24h` (after Sync fork) reads it, runs your quantile forest on every run, pools the answers,
  and writes `predicted_low_mw`, `predicted_load_mw` and `predicted_high_mw`.
- Your Lab 5 `model.joblib` stays in the bucket as the backup. To go back to Lab 5 behavior, upload your old model card.

## Submit Lab 6 (HuskyCT text box)
The deliverable is simple: **your model is on the class leaderboard with a range** (a low and a high). Paste:
1. Your leaderboard **nickname**
2. The line your notebook printed when your range went live: **"Range is live"** from 6C, or **"Tuned range is live"**
   from 6D Part 11 if you did 6D

The notebook questions (1-12 in 6A to 6C, 13-17 in 6D) are for your final project report; they are not submitted here.
Leave your energy project running after you submit: the final project scores your live ranges from Sat Nov 21 to Tue Dec 1.

## Stuck?
Paste the error and the cell into Claude. For `forecast-24h` problems, run the troubleshooting log cell in 6C Part 5b and
paste the newest log line.
