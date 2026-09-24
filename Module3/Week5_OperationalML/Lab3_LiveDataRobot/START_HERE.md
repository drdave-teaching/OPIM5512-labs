# Lab 3 — Build a Live Data Robot · **START HERE**

**Two tiny APIs, one robot, all in VS Code — with GitHub.** Same branch → pull request → review → merge
workflow as Labs 1 and 2. Tonight the code stops being something *you* run: you hand it to a robot that
runs it **every 5 minutes, in the cloud, for free, while you sleep.**

> New England's grid publishes electricity demand every 5 minutes. The weather station at your campus
> airport reports every 5 minutes too. You and your partner each write a small **API** for one feed,
> then GitHub Actions calls both on a schedule and saves every new row.

| | What | Link |
|---|---|---|
| 🧰 | **The template repo** — Partner A clicks **Use this template** (robot, tests, notebook already in it) | [opim5512-lab3-template](https://github.com/drdave-teaching/opim5512-lab3-template) |
| 📋 | **Instructions — every click, in order** (keep open beside VS Code) | [Lab3_instructions.md](Lab3_instructions.md) |
| 🗺️ | **Tonight in 20 steps** (the one-page map) | [TONIGHT_IN_20_STEPS_lab3.md](TONIGHT_IN_20_STEPS_lab3.md) |
| 🖨️ | **Printables** — 20 steps · instructions · slides | [handouts/](handouts/) |

## Before you start

- **GitHub account + GitHub Desktop** signed in · **VS Code** with the **Python** and **Jupyter** extensions
- You did **Labs 1 and 2** (branch → commit → push → PR → review → merge). Same moves tonight.
- Laptop Python fighting you? Use **Codespaces** (your repo → **Code → Codespaces → Create**): VS Code in the
  browser with everything already installed. Same steps.

## What each partner does

| | Partner A — **energy** | Partner B — **weather** |
|---|---|---|
| feed | ISO-NE five-minute system load | National Weather Service station observations |
| the mess you hide | a session cookie, a Referer header, and a file full of comment/header rows | nested JSON in Celsius and km/h |
| file | `src/isone.py` | `src/nws.py` |
| your clean function | `get_five_minute_load()` | `get_observations()` |
| branch | `dev-energy` | `dev-weather` |
| you write | **3 small TODOs** | **2 small TODOs** |

Then together: review each other's pull request (the green ✓ is the robot telling you the code works),
merge both, press **Run workflow** once, and watch the `data` branch fill up. Open the notebook to see the
live data — including how much electricity demand **rooftop solar hides from the grid** at midday.

---

*New to the workflow? The Lab 1 kit is the reference: [Lab1_FirstCommit](../../../Module1/Week1_TechStack/Lab1_FirstCommit/START_HERE.md).*
