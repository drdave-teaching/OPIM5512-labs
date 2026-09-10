# Lab 1 — First Commit · simple edition · Tonight in 20 Steps

**OPIM 5512 · Module 1** — same lab, run once per campus; come to YOUR campus's night

> **The one-sentence version: tonight the deliverable is a *repo*, not a notebook.**
> The data is already clean. You run a plot, write one histogram, and spend the night on the
> workflow you'll use all semester: branch → commit → push → pull request → review → merge.

---

## Before we start (stack check)

- [ ] **GitHub account** + **GitHub Desktop** installed and **signed in**
- [ ] **Google Colab** opens
- [ ] You know your campus word: `hartford` or `stamford`
- [ ] **No AI tonight** — the histogram is three lines. Type it.

---

## The 20 steps, in order

### Set up (steps 1–6)
1. **Pair up.** Decide who's **Partner A (weather)** / **Partner B (demand)**. *(Solo/online? Two accounts, or pair over Teams.)*
2. **Partner A:** github.com → **➕ → New repository** (build it — *don't* use a template) → owner = *you*, name `opim5512-lab1-<netidA>-<netidB>`, **Public**, ✅ Add a README + ✅ .gitignore = **Python** → **Create repository**.
3. **Partner A:** repo **Settings → Collaborators → Add people** → Partner B → **Partner B accepts** the invite (email or the bell icon).
4. **Partner A:** **Settings → Branches → Add branch ruleset** (or *Add rule*) for `main`: **require a pull request** + **1 approval**. *(Rehearsing solo? leave approvals at 0.)*
5. **Both:** GitHub Desktop → **File → Clone repository** → pick the repo → **Clone**. Once. Note the local path.
6. **Each:** **Current branch → New branch** → `dev-weather` (A) / `dev-demand` (B) → **Publish branch**.

### Plot & ship (steps 7–12)
7. **Each:** Colab → **File → Open notebook → GitHub tab** → paste `drdave-teaching/OPIM5512-labs` → open `Module1/Week1_TechStack/Lab1_FirstCommit/notebooks/Lab1_A_Weather.ipynb` (A) or `…/Lab1_B_Demand.ipynb` (B).
8. **Each:** A sets `CAMPUS`. **Runtime → Run all.** Look at the line plot that appears — it already saved a PNG.
9. **Each:** in the **TODO** cell, write your **histogram** (the shape is given right above it). Run it. Look at it. Fix the title/units if they don't read well.
10. **Each:** run the **download** cell → two PNGs land in Downloads. Then **File → Download → Download .ipynb** → your notebook lands there too.
11. *(We're **not** using Colab's Save-to-GitHub tonight — you'll drag the files in yourself so you see where they live.)*
12. **Each:** GitHub Desktop → **Repository → Show in Explorer** → make **`notebooks/`** + **`images/`** → drag your `.ipynb` into `notebooks/`, both PNGs into `images/` *(rename any `(1)` first)* → top bar says your `dev-` branch → **Commit** → **Push**.

### Review & merge (steps 13–16)
13. **Each:** github.com → **Compare & pull request** → title → **Create** → **Reviewers** → your partner.
14. **Each:** open your **partner's** PR → **Files changed** → actually read their histogram cell and look at the PNGs → **Review changes → Approve**.
15. **Merge** both PRs → **Delete branch** on each.
16. **Both:** GitHub Desktop → **Current branch → main → Fetch → Pull**. Both partners' plots and notebooks are now on your laptop.

### Deliverable & read-out (steps 17–20)
17. **Your deliverable:** on your repo → **Insights → Network** → **screenshot** the graph → post it to **Lab 1 participation** on HuskyCT. That graph is proof you both authored *and* reviewed.
18. **If you're ahead — a short report:** github.com → **Add file → Create new file** → `REPORT.md` → drop in your four plots (`![](images/weather_line.png)`) with **one sentence** each (units on every number).
19. **Ship the report through the loop:** commit it on a `report` branch → PR → the *other* partner approves → **Merge**. *(main is protected — the rule working.)*
20. **Really flying?** Run `Lab1_Joint_Optional.ipynb` (same GitHub tab, class repo) → `temp_vs_load.png` → `images/` → PR → merge. Chase the surprise: the hottest hour is **not** the peak-demand hour.

---

## Don't panic

- **Commit early.** Once something's committed, it's essentially impossible to lose.
- **Fetch and Pull can't hurt you.** Fetch = peek, Pull = download. The scary buttons are the *Discard* ones.
- **Same path every save** — a different path makes a *second* notebook, not an update.
- **`main` rejecting your push is the protection working** — you're on `main` when you should be on your branch.
- **PNG didn't download?** The download cell tells you which file is missing — run the cell that makes it, then re-run.

---

## Online / solo students

- **Pair over Teams** if two of you can — each on your own account; one owns the repo and adds the other.
- **Otherwise two accounts** (needs a second email): play both A and B yourself, including approving as the other account.
- **Simplest solo:** one account with **Required approvals = 0** — branch → PR → merge yourself.

---

## Definition of done — what's in the repo at 7:30

- [ ] Both partners are collaborators; **branch protection** on `main`
- [ ] `images/` has **four PNGs** (two per partner) with the exact filenames
- [ ] Both partners' **notebooks committed** (a histogram in each)
- [ ] **≥2 merged pull requests** (one each), branches deleted, both of you authoring **and** reviewing
- [ ] A **network-graph screenshot** posted to HuskyCT — **the deliverable**
- [ ] *(bonus)* a short `REPORT.md` merged through its own PR

*Extra credit for the room that's flying: both partners add one line to `README.md → ## Findings` on separate branches, merge one, then the other — and resolve the **merge conflict** together.*
