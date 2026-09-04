# Lab 2 — Explaining a Model (SHAP) · **START HERE**

**Half lecture, half hands-on — with GitHub.** Same branch → pull request → review → merge
workflow as Lab 1. Tonight you explain the **same model two ways** and merge the two views into one report.

> The model is already trained for you (a random forest that predicts New England electricity **demand**
> from weather and time). You don't tune it tonight — you make it **explain itself.**

| | What | Link |
|---|---|---|
| 📖 | **The lecture** — read this first, or follow along live (SHAP in plain English) | [SHAP_LECTURE.md](SHAP_LECTURE.md) |
| 🧰 | **The template repo** — Partner A clicks **Use this template** (data, notebooks, folders already in it) | [opim5512-lab2-template](https://github.com/drdave-teaching/opim5512-lab2-template) |
| 📋 | **Instructions — every click, in order** (keep open beside Colab) | [Lab2_instructions_shap.md](Lab2_instructions_shap.md) |
| 🗺️ | **Tonight in 20 steps** (the one-page map) | [TONIGHT_IN_20_STEPS_shap.md](TONIGHT_IN_20_STEPS_shap.md) |
| 🖨️ | **Printables** — 20 steps · instructions | [handouts/](handouts/) |

## Before you start

- **GitHub account + GitHub Desktop** installed and signed in · **Colab** opens
- You did **Lab 1** (branch → commit → push → PR → review → merge). Same moves tonight.
- The setup cell does `!pip install shap` and fits the model for you — **you write one SHAP line.**

## What each partner does

| | Partner A — **global** | Partner B — **local** |
|---|---|---|
| question | *Which features matter, overall?* | *Why THIS one prediction?* |
| notebook | `notebooks/Lab2_A_Global_SHAP.ipynb` | `notebooks/Lab2_B_Local_SHAP.ipynb` |
| branch | `dev-global` | `dev-local` |
| given | the built-in importances bar chart | the predicted-vs-actual scatter |
| you write | **one line** → a SHAP **beeswarm** | **one line** → a SHAP **waterfall** |
| you ship | notebook + `images/importances_builtin.png` + `images/shap_global.png` | notebook + `images/predicted_vs_actual.png` + `images/shap_local.png` |

Then together: review each other's pull request, merge both, fill in `REPORT.md` (image links already
wired), and put the two SHAP plots side by side for the read-out — **global says what the model leans on,
local tells the story of one hour.**

---

*New to the workflow? The Lab 1 kit is the reference: [Lab1_FirstCommit](../../../Module1/Week1_TechStack/Lab1_FirstCommit/START_HERE.md).*
