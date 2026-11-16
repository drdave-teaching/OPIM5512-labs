# Lab 6: Low, Expected and High (Forecast Uncertainty in Production) · **START HERE**

> Submit by **Fri Nov 20, 11:59 PM** (Hartford and Stamford).

**Solo · three notebooks (plus an optional fourth) · Colab · your Lab 5 energy project on Google Cloud.**
Your Lab 5 model gives one number per hour. Tonight it learns to say **how sure it is**: a low, an expected and a high
load for every hour, an honest **80% range**. Two things make a forecast uncertain, and you handle both:
the **weather forecast** is wrong sometimes (6A), and **your model** misses even with perfect weather (6B).
**The Lab 6 deliverable is simple: get a range on the leaderboard.** The easiest way is **6B Part 7**: ship the 6B
quantile forest directly, with the National Weather Service forecast, in about 5 minutes. That's enough for Lab 6.
**6C and 6D are optional.** They add the uncertainty from the weather forecasts (8 HRRR runs) to your range, then tune
it. They're correct and they're cool, but a bit complex as we wrap up the semester. Either way, your range is scored in
the final project window (Sunday night, Nov 29, to Fri Dec 4).

| | What | Link |
|---|---|---|
| 🌦️ | **6A · Your frozen model meets the HRRR** (NOAA's hourly 3 km weather model, through hefty and dynamical.org) | [Lab6A_Frozen_Model_Meets_HRRR.ipynb](https://colab.research.google.com/github/drdave-teaching/OPIM5512-notebooks/blob/main/Module4/Lab6A_Frozen_Model_Meets_HRRR.ipynb) |
| 🎯 | **6B · How sure is your model?** Random forest spread vs quantile forest, scored by CRPS; **Part 7 ships it** | [Lab6B_Model_Uncertainty_RF_vs_QRF.ipynb](https://colab.research.google.com/github/drdave-teaching/OPIM5512-notebooks/blob/main/Module4/Lab6B_Model_Uncertainty_RF_vs_QRF.ipynb) |
| 🚀 | **6C · Two kinds of uncertainty, one range, live** *(optional)* (pool the quantile forest over 8 HRRR runs, ship it) | [Lab6C_Combine_and_Ship.ipynb](https://colab.research.google.com/github/drdave-teaching/OPIM5512-notebooks/blob/main/Module4/Lab6C_Combine_and_Ship.ipynb) |
| 🧪 | **6D · Tune your range** *(optional)* (experiment with leaf size, features per split, HRRR runs and widen; validation CRPS; ship the winner) | [Lab6D_Tune_Your_Range.ipynb](https://colab.research.google.com/github/drdave-teaching/OPIM5512-notebooks/blob/main/Module4/Lab6D_Tune_Your_Range.ipynb) |
| 📊 | **The weather data** (every HRRR run at Bradley since 2023, as issued, + RTMA) | [data/README.md](https://github.com/drdave-teaching/OPIM5512-notebooks/blob/main/Module4/data/README.md) |
| 🧠 | **Your energy repo** (Sync fork once: 6B Part 7 or 6C Part 0) | [drdave-teaching/energy-forecasting](https://github.com/drdave-teaching/energy-forecasting) |
| 🏆 | **Class leaderboard** (Lab 6 table: ranges ranked by CRPS) | [opim5512-leaderboard-f26](https://storage.googleapis.com/opim5512-leaderboard-f26/index.html) |
| 🛠️ | **hefty** by Will Hobbs (open source; 6A Part 4 has an idea for your first contribution) | [github.com/williamhobbs/hefty](https://github.com/williamhobbs/hefty) |

## Before you start
- [ ] Your Lab 5 model is live: `forecast-24h` writes a forecast every hour and you're on the leaderboard
- [ ] You know your **energy project ID** and **bucket name**
- [ ] Do the notebooks **in order**: 6A, then 6B (ship it in Part 7), then 6C and 6D if you want to go further. Open each in Colab, then File → Save a copy in Drive.

## The notebooks

| Notebook | You do | You get |
|---|---|---|
| **6A** | Load your frozen model; pull tomorrow's HRRR forecast with **hefty**; compare it with the NWS forecast production uses; replay 2026 with the HRRR forecast you'd really have had 1, 12 and 24 hours ahead, graded with **RTMA** | How many MW weather error costs your model; 8 HRRR runs that disagree about tomorrow |
| **6B** | Learn the **CRPS**; build a range two ways: the spread of a random forest's trees vs a **quantile regression forest** at the 10th and 90th percentiles | An honest 80% range... with perfect weather only. **Part 7 (optional): ship it live** with the NWS forecast, a little wider |
| **6C** (optional) | **Sync fork**; rebuild the 8 runs for every hour of 2026; compare model-only, weather-only and **pooled**; upload `model_qrf.joblib`; run `forecast-24h` | Your range, live every hour, on the Lab 6 leaderboard |
| **6D** (optional) | Three periods (train 2023-24, tune on 2025, test 2026 once); run experiments with `try_setting()`: leaf size, `max_features`, a grid, HRRR runs and `range_widen`, seed noise, your own challenges; pick the winner by a rule; ship it | A tuned range live, plus an experiment log: your before and after for the final project report |

Heads up: 6A installs hefty, which needs a newer pandas, so **Colab restarts once** after the first cell. Wait for
"Connected", run the first cell again, and keep going.

## What changes in your energy project (6C, optional)
- Every hour at **:05**, Dr. Dave's class job saves the 8 newest HRRR runs at Bradley to one public file.
- At **:20** your `forecast-24h` (after Sync fork) reads it, runs your quantile forest on every run, pools the answers,
  and writes `predicted_low_mw`, `predicted_load_mw` and `predicted_high_mw`.
- Your Lab 5 `model.joblib` stays in the bucket as the backup. To go back to Lab 5 behavior, upload your old model card.

## Submit Lab 6 (HuskyCT text box)
The deliverable is simple: **your model is on the class leaderboard with a range** (a low and a high). Paste:
1. Your leaderboard **nickname**
2. The line your notebook printed when your range went live: **"6B range is live"** from 6B Part 7, **"Range is live"**
   from 6C, **"Tuned range is live"** from 6D Part 11, or **"Final model is live"** from the final project notebook

The questions at the end of each notebook (1-12 in 6A to 6C, 13-17 in 6D) are optional reflection prompts, not graded:
they're for deeper understanding, and good material for your final project report.
Leave your energy project running after you submit: the final project scores your live ranges from Sunday night, Nov 29 (after Thanksgiving), to Fri Dec 4, 11:59 PM.

## Stuck?
Paste the error and the cell into Claude. For `forecast-24h` problems, run the troubleshooting log cell in 6C Part 5b and
paste the newest log line.
