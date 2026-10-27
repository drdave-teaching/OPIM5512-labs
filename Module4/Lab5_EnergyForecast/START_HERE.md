# Lab 5: Forecasting Connecticut's Electricity in Production · **START HERE**

> Hartford: **Wed Oct 28** · Stamford: **Wed Nov 4** · Submit by **Thu Nov 12, 11:59 PM** (both campuses).

**Solo · about 2 hours · Colab · Bradley weather + Connecticut load since 2023, then your own energy project on Google Cloud.**
Tonight you forecast **how much electricity Connecticut will use in each of the next 24 hours**: the problem ISO New
England solves every day. You tune a real time-series model, beat three honest baselines, and **deploy it**, so it makes a
new 24-hour forecast every hour from the live weather forecast and the live load. In Lab 6 and the final project, every
student's forecasts go on a class leaderboard.

| | What | Link |
|---|---|---|
| ☁️ | **Pre-lab: Energy Project Setup Guide** (do this BEFORE class, about 40 minutes) | [Energy_Project_Setup_F26.ipynb](https://colab.research.google.com/github/drdave-teaching/OPIM5512-notebooks/blob/main/Module4/Energy_Project_Setup_F26.ipynb) |
| 🚀 | **The lab notebook** (open in Colab, then File → Save a copy in Drive) | [Lab5_Energy_Forecast_In_Production.ipynb](https://colab.research.google.com/github/drdave-teaching/OPIM5512-notebooks/blob/main/Module4/Lab5_Energy_Forecast_In_Production.ipynb) |
| 🗺️ | **Tonight in 20 steps** (print it, or keep it on a second screen) | [OPIM5512_Lab5_20_Steps_PRINT.pdf](handouts/OPIM5512_Lab5_20_Steps_PRINT.pdf) |
| 🧹 | **How the training data was cleaned** (step by step, optional reading) | [Lab5_Building_the_Training_Data.ipynb](https://colab.research.google.com/github/drdave-teaching/OPIM5512-notebooks/blob/main/Module4/Lab5_Building_the_Training_Data.ipynb) |
| 🎁 | **Bonus (optional): more features, an ensemble, and a low/expected/high range for every hour** | [Lab5_Bonus_Features_Ensembles_Ranges.ipynb](https://colab.research.google.com/github/drdave-teaching/OPIM5512-notebooks/blob/main/Module4/Lab5_Bonus_Features_Ensembles_Ranges.ipynb) |
| 📊 | **The training data** (33,215 hours, Jan 2023 to Oct 15, 2026) + data dictionary | [data/README.md](https://github.com/drdave-teaching/OPIM5512-notebooks/blob/main/Module4/data/README.md) |
| 🧠 | **Your energy repo** (fork it in the pre-lab) | [drdave-teaching/energy-forecasting](https://github.com/drdave-teaching/energy-forecasting) |

## Before class (about 40 minutes, once)

Follow the **Energy Project Setup Guide** step by step. It's the same Cloud Shell routine as your Craigslist project, in a
**new** Google Cloud project, for a **new** repo. Your Craigslist project keeps running as it is.

**Two ways through it** (the prompts are at the top of the guide):
- **Path 1 (recommended): you do every step, Claude is your tutor.** You paste each block and click through GitHub
  yourself; Claude explains and fixes errors. This is the better path: Lab 6 and the final project build on this project.
- **Path 2 (if you are stuck or out of time): Claude does the setup while you watch.** Claude in Chrome or Claude Code
  runs the guide for you, one step at a time. You still sign in, approve the "Authorize" screens, and type your ISO
  Express secrets yourself, and you are still responsible for understanding what each step did.
- **Missed it or stuck either way?** Come at the start of class and we will fork and set it up together.

- [ ] A **new Google Cloud project** for energy, with a budget alert
- [ ] Your **fork of `drdave-teaching/energy-forecasting`**, with Actions **enabled** ("I understand my workflows...")
- [ ] Your **own free ISO Express account** at iso-ne.com, saved in your fork as two **repository secrets**: `ISO_NE_USERNAME`, `ISO_NE_PASSWORD`
- [ ] **Four green deploys** on your fork's Actions tab: scraper-weather-obs, scraper-weather-forecast, scraper-isone, forecast-24h
- [ ] **Deploy scraper-isone**'s last step says `"status": "ok"` (not `"skipped"`), and **Deploy forecast-24h** says `"no_model"` (correct until tonight)
- [ ] You know your **energy project ID** and **bucket name** (usually the same)

## Tonight in 9 parts

| Part | Minutes | You do |
|---|---|---|
| 0. Before you start | 5 | Check your four green deploys |
| 1. Load | 5 | 33,215 hours of Bradley weather + Connecticut load |
| 2. Look | 15 | The daily, weekly and yearly rhythm, the U-shape, and why yesterday predicts today |
| 3. Features | 10 | `make_features`: calendar + weather + the load at the same hour yesterday (**the same code runs in production**) |
| 4. Baselines | 10 | Split by **time** (train 2023-2025, test 2026), then three numbers to beat |
| 5. Tune | 25 | Tree, forest, gradient boosting with **time-series cross-validation**; your champion; its loss curve |
| 6. Misses | 15 | Real weeks, error by hour, permutation importance, the U-shape your model learned. **Your turn:** add last week's load |
| 7. Ship | 15 | Upload your model; run `forecast-24h` right from Colab |
| 8–9. Tomorrow + wrap up | 10 | Your first real 24-hour forecast next to ISO New England's; five short answers |

## What runs every hour in your energy project

| Minute | Function | Saves in `gs://YOUR-BUCKET/energy/` |
|---|---|---|
| :05 | `scraper-weather-obs` | `datasets/bdl_weather_obs_master.csv`: the weather that happened at Bradley |
| :05 | `scraper-weather-forecast` | `datasets/bdl_weather_forecast_master.csv`: the National Weather Service forecast, next 24 hours |
| :15 | `scraper-isone` | `datasets/ct_load_*_master.csv` and `isone_ct_forecast_master.csv`: Connecticut load + ISO New England's forecast |
| :20 | `forecast-24h` | `forecasts/latest.csv`: **your model's** next 24 hours (from tonight on) |

**Your model is frozen**: production never retrains it. Retraining = run the notebook again and upload; `forecast-24h`
switches to the new model at its next run, and `models/history/` keeps a copy of every model you ever shipped.

**Submit (tonight, in class):** HuskyCT → *Submit Lab 5* → in the text box, paste the line **Part 7e** prints
(`netid,bucket,nickname`), then your five Part 9 answers. No file upload. Final deadline **Thu Nov 12, 11:59 PM** (Hartford and Stamford).

**Leave everything running.** Your bucket collects weather and load every hour, and from tonight the class leaderboard
scores every forecast your model makes.

## Stuck?

Ask Claude: paste the cell, the **full** error, and what you expected. Most problems are one of these:

- **Pre-lab errors** (409, "concurrent policy changes", Actions off on your fork): see the **Troubleshooting** table at the bottom of the setup guide.
- **Wrong Google account** in the Colab pop-up (Part 7b): pick the Gmail you used for your **energy** project.
- **`"no_load_data"`** from `forecast-24h`: your ISO secrets are missing or misspelled; fix them, re-run **Deploy scraper-isone**, wait for its :15 run.
- **`"no_model"`**: your upload in 7c didn't run (check `PROJECT_ID` and `BUCKET_NAME` in Part 1b).
- **Part 8 says DEMO**: run 7d first (it starts `forecast-24h` and waits for it), then re-run Part 8.
