# Lab 1 — First Commit · Tonight in 20 Steps

**OPIM 5512 · Module 1** — same lab, run once per campus; come to YOUR campus's night

> **The one-sentence version: tonight the deliverable is a *repo*, not a notebook.**
> Two people each analyze a different half of the same problem, and the only way to the
> answer is to merge your work together.

---

## Before we start (stack check)

- [ ] **GitHub account** + **GitHub Desktop** installed and **signed in**
- [ ] **Google Colab** opens
- [ ] You know your **campus station**: Hartford = `KBDL`, Stamford = `KBDR`
- [ ] **No AI tonight** — no Claude / ChatGPT / Copilot / Colab autocomplete. Type it yourself.
      (Module 3 is an entire unit on using them. Not never — not yet.)

---

## The 20 steps, in order

### Set up (steps 1–6)
1. **Pair up.** Decide who's **Partner A (weather)** / **Partner B (demand)**. *(Solo/online? Two accounts, or pair over Teams.)*
2. **Partner A:** create a new **public** repo for the pair.
3. **Partner A:** add Partner B as a **collaborator** → **Partner B accepts** the invite.
4. **Partner A:** turn on **branch protection** for `main` (require a PR + 1 approval).
5. **Both:** **clone** the repo **once** in GitHub Desktop.
6. **Each:** make your branch (`dev-weather` / `dev-demand`) → **Publish** it.

### Grab data & build your half (steps 7–13)
7. **Each:** open your **starter** in Colab (new tab) → **run the first cell, look at your raw data.**
8. **Together:** write the **data dictionary** (your contract) in `README.md` — names, units, what one timestamp means.
9. **Each:** clean your half in Colab → **File → Save** to your branch *(drop a `#TEST` to prove it saved).*
10. **Each:** save your **CSV** and your **plot**; download both.
11. **Each:** GitHub Desktop → **Show in Explorer** → drag CSV → `data/clean/`, plot → `images/`.
12. **Each:** **commit** (real message) → **push**.
13. **Each:** open **one pull request** (your branch → `main`): notebook + contract + CSV + plot.

### Review & merge (steps 14–17)
14. **Each:** request your **partner** as reviewer.
15. **Each:** **review your partner's PR** — read the diff, then **Approve**.
16. **Merge** both PRs → **delete** the branches. *(Whoever merges the README **second** resolves the **merge conflict** — keep both halves.)*
17. **Both:** switch to `main` → **Fetch → Pull.** Now you each have **both** files.

### Join & report (steps 18–20)
18. **Together (one screen):** open the **joint EDA** notebook → run the **join** → find **three things**, one surprising.
19. **Write `REPORT.md`** (from the template) + save **figures** → branch → PR → partner reviews → merge.
20. **Read-out:** one figure on screen, one sentence — and check your **network graph** shows the loop both ways.

---

## Don't panic

- **Commit early.** Once something's committed, it's essentially impossible to lose.
- **Fetch and Pull can't hurt you.** Fetch = peek, Pull = download. Neither overwrites your work. The scary buttons are the *Discard* ones.
- **Save to the same path every time** — a different path makes a *second* notebook, not an update.
- **Restart & run all → Clear all outputs** before a notebook goes in — your partner has to read that diff.
- **`main` rejecting your push is the protection working, not a bug** — you're on `main` when you should be on your branch.

---

## Online / solo students

- **Pair over Teams** if two of you can — each on your own account, one owns the repo and adds the other. Real review, real contract.
- **Otherwise two accounts** (needs a second email): play both A and B yourself — you'll hit every step, including approving as the other account and resolving the conflict.
- **Simplest solo:** one account with **Required approvals = 0** — branch → PR → merge yourself (skips the approval gate).

---

## Definition of done — what's in the repo at 7:30

- [ ] Both partners are collaborators; **branch protection** on `main`
- [ ] `README.md` with a data dictionary for **both** files
- [ ] `data/clean/weather_hourly.csv` **and** `data/clean/demand_hourly.csv`
- [ ] Both cleaning notebooks + the joint EDA notebook
- [ ] **`REPORT.md`** — three findings (one surprising), figures, honest caveats, plain English
- [ ] **≥3 merged pull requests**, branches deleted, both of you authoring **and** reviewing
- [ ] A **network graph** showing the loop going both ways
