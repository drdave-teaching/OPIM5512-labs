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
2. **Partner A:** open the [template repo](https://github.com/drdave-teaching/opim5512-lab1-template) → green **Use this template → Create a new repository** → owner = *you*, name `opim5512-lab1-<netidA>-<netidB>`, **Public** → Create.
3. **Partner A:** repo **Settings → Collaborators → Add people** → Partner B → **Partner B accepts** the invite (email or the bell icon).
4. **Partner A:** **Settings → Branches → Add branch ruleset** (or *Add rule*) for `main`: **require a pull request** + **1 approval**. *(Rehearsing solo? leave approvals at 0.)*
5. **Both:** GitHub Desktop → **File → Clone repository** → pick the repo → **Clone**. Once. Note the local path.
6. **Each:** **Current branch → New branch** → `dev-weather` (A) / `dev-demand` (B) → **Publish branch**.

### Plot & ship (steps 7–12)
7. **Each:** open *your* notebook in Colab: **colab.research.google.com → File → Open notebook → GitHub tab** → paste your repo URL → click `notebooks/Lab1_A_Weather.ipynb` (A) or `Lab1_B_Demand.ipynb` (B).
8. **Each:** A sets `CAMPUS`. **Runtime → Run all.** Look at the line plot that appears — it already saved a PNG.
9. **Each:** in the **TODO** cell, write your **histogram** (the shape is given right above it). Run it. Look at it. Fix the title/units if they don't read well.
10. **Each:** run the **download** cell → two PNGs land in your Downloads folder.
11. **Each:** **File → Save** the notebook → *your* repo · *your* `dev-` branch · keep the path `notebooks/…` · real commit message. *(Plain Save — not Ctrl+S.)*
12. **Each:** GitHub Desktop → **Repository → Show in Explorer** → drag both PNGs into **`images/`** *(rename first if the name has `(1)` in it)* → back in Desktop, top bar says your `dev-` branch → **Commit** → **Push**.

### Review & merge (steps 13–16)
13. **Each:** github.com → **Compare & pull request** → title → **Create** → **Reviewers** → your partner.
14. **Each:** open your **partner's** PR → **Files changed** → actually read their histogram cell and look at the PNGs → **Review changes → Approve**.
15. **Merge** both PRs → **Delete branch** on each.
16. **Both:** GitHub Desktop → **Current branch → main → Fetch → Pull**. Both partners' plots and notebooks are now on your laptop.

### Report & read-out (steps 17–20)
17. **One screen, two people:** on github.com open `REPORT.md` → ✏️ **Edit** → replace each **➜** line with one sentence (every number gets a unit). The four plots already show above the lines.
18. **Commit the report** to a new branch `report` → **Propose changes** → PR → the *other* partner approves → **Merge**. *(main is protected — that's the rule working, not a bug.)*
19. **If you're ahead:** run `notebooks/Lab1_Joint_Optional.ipynb` (both files joined) → drag `temp_vs_load.png` into `images/` → it drops into section 5 of the report.
20. **Read-out:** one plot on the screen, one sentence — and check **Insights → Network** shows the loop going both ways.

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
- [ ] Both notebooks saved back with a **histogram** in each
- [ ] **`REPORT.md`** — one real sentence under each plot, plus one honest "what this can't tell us"
- [ ] **≥3 merged pull requests** (one each + the report), branches deleted, both of you authoring **and** reviewing
- [ ] A **network graph** showing the loop going both ways

*Extra credit for the room that's flying: both partners add one line to `README.md → ## Findings` on separate branches, merge one, then the other — and resolve the **merge conflict** together.*
