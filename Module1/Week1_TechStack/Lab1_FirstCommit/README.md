# Lab 1 — First Commit

**OPIM 5512 · Module 1 · Wed 5:30–7:30**
Hartford: **Sep 2** · Stamford: **Sep 9** — same lab, run twice.

---

## The one-sentence version

> **Tonight the deliverable is a repo, not a notebook.**

You and a partner will each analyze a *different half* of the same problem — one of you takes
the weather, one takes the electricity demand — and neither of you can finish the punchline
alone. The only way to see the final plot is to **merge your work together**. That's the lab.

## What you'll be able to do at 7:30 that you couldn't at 5:30

1. Share a repo with a partner without stepping on each other
2. Branch → commit → push → open a PR → **review a real person's work** → merge → delete branch
3. Agree on a data contract *before* anybody writes code
4. Resolve a merge conflict without panicking
5. Move a notebook between **Colab** and **GitHub** in both directions

> There's no scraping tonight and no modeling tonight. Both are coming (Module 3 and
> Module 2). Week 1 is about the workflow you'll use for the rest of the semester.

---

## Before you show up

- Watch the Module 1 videos
- Have a **GitHub account** and **GitHub Desktop** installed and signed in
  → [setup_guide.md](../setup_guide.md)
- Skim [github_fundamentals.md](../github_fundamentals.md) §8–§12 (branches, PRs, conflicts)
- Read [BRANCHING_MENTAL_MODEL.md](BRANCHING_MENTAL_MODEL.md) — 5 minutes, and it's the
  difference between the lab making sense and the lab being button-mashing

## Tools — and why we're using two of them

| Tool | What it's for tonight |
|---|---|
| **Google Colab** | Where you write and run code. No install, no environment problems. |
| **GitHub Desktop** | Where you see *what changed*, switch branches, and merge. |
| **github.com** | Where pull requests and reviews happen. |

Colab is the *editor*. GitHub Desktop is the *map*. You need both because Colab can show you
your code but it can't show you your team.

📎 The mechanics of moving files between them: [COLAB_AND_GITHUB.md](COLAB_AND_GITHUB.md)

---

## The data

Two CSVs, already in this folder. Real, and real enough to be annoying.

**`data/isone_demand_hourly_raw.csv`** — actual hourly electricity demand for **all of New
England**, straight off ISO-NE, 744 hours (Jul 20 – Aug 19, 2026).
It's a row-prefixed CSV: lines start with `"C"` (comment), `"H"` (header — there are *two*),
or `"D"` (data). `pd.read_csv` on it directly gives you garbage. Filter on `"D"`.

**`data/<your campus>/airport_<STATION>_hourly_raw.csv`** — hourly weather observations from
your campus's airport, same 744 hours.

| Campus | Station | Airport |
|---|---|---|
| **Hartford** | `KBDL` | Bradley International, Windsor Locks |
| **Stamford** | `KBDR` | Sikorsky Memorial, Bridgeport |

Missing values arrive as the letter **`M`**, trace precipitation as **`T`**. Observations are
taken at **:51 or :52 past the hour**, not on the hour — you'll have to deal with that to join
them. That's not a mistake in the file; that's what a METAR looks like.

> 🔷 The grid is shared, the weather is local. Both campuses analyze the *same* demand series
> against a *different* airport. Notice which parts of your answer change and which don't.

---

## Teams

**Pairs.** Odd person out pairs with Dave.

- **Partner A — weather.** You own `src/clean_weather.py` and `notebooks/weather_eda.ipynb`.
- **Partner B — demand.** You own `src/clean_demand.py` and `notebooks/demand_eda.ipynb`.

Neither of you can produce the other's output. That's deliberate — it's the reason the merge
has to actually work.

---

## Run of show

| Time | What happens |
|---|---|
| **5:30–5:45** | Pair up. Stack check: GitHub Desktop signed in, Colab opens. |
| **5:45–6:10** | **The contract.** A creates the repo from the template, adds B, turns on branch protection. Then *together* you write the data dictionary in the README — column names, units, timestamps, filenames. |
| **6:10–6:45** | **Split and work.** A on branch `dev-weather`, B on branch `dev-demand`. Separate files, no overlap. Clean your half, save a tidy CSV, make one plot. |
| **6:45–7:05** | **The ping-pong.** Two PRs open at once. Each of you reviews the *other's* diff on github.com and must actually choose Approve / Comment / Request changes. Merge. Delete branch. |
| **7:05–7:20** | **The join.** Both pull `main`. Now — and only now — you both have both files. Run `notebooks/join_and_plot.ipynb` together and find the punchline. |
| **7:20–7:30** | **Rounds.** Two or three network graphs on screen. Each pair says their one insight out loud. |

### The collision (it's on purpose)

At some point you will both need to edit the **data dictionary** in `README.md`. Whoever merges
second gets a **merge conflict**. Good. Resolve it together — that conflict is the two of you
having independently named the same column two different things, which is exactly the
conversation you'd otherwise be having in November with a broken model.

---

## The punchline you're hunting

Once the two files are joined, plot **demand against temperature**, and separately plot demand
by **hour of day**.

There is something in there that surprises most people the first time: **the hottest hour of the
month is not the highest-demand hour of the month** — and it isn't even the same day. Find both.
Then argue about why.

That's your "one real insight." It's worth more than a pretty chart.

---

## Definition of done — what's in the repo at 7:30

- [ ] Both partners listed as collaborators; branch protection on `main` (PR + 1 approval)
- [ ] `README.md` with a data dictionary covering **both** cleaned files
- [ ] `src/clean_weather.py` and `src/clean_demand.py`
- [ ] `data/clean/weather_hourly.csv` and `data/clean/demand_hourly.csv`
- [ ] `notebooks/` — two EDA notebooks plus the joint join-and-plot notebook
- [ ] **≥4 merged pull requests** (2 each), branches deleted
- [ ] A network graph showing the loop going both ways
- [ ] One sentence in the README: *"The thing we found was ___."*

---

## Explicitly out of scope tonight

Scraping · APIs · GCP · scheduling · modeling · backfilling history. All of it is coming.
Week 1 is small on purpose — Module 3's whole story is *"now make it run without you,"* and
that story needs a laptop to start from.

## The one rule

> **Code goes in the repo. Data doesn't.**

Tonight we break it once, deliberately: the cleaned CSVs get committed, because *the CSV is
what your partner reviews in the pull request.* Say out loud that it's an exception. Module 3
is where it gets fixed properly.
