# Lab 1 — First Commit

**OPIM 5512 · Module 1 · Wed 5:30–7:30**
Hartford: **Sep 2** · Stamford: **Sep 9** — same lab, run twice.

---

## The one-sentence version

> **Tonight the deliverable is a repo, not a notebook.**

You and a partner will each analyze a *different half* of the same problem — one of you takes
the weather, one takes the electricity demand — and neither of you can answer the question
alone. The only way to get to the analysis is to **merge your work together**. Then you write
up what you found, for a manager who doesn't know what a p-value is. That's the lab.

## What you'll be able to do at 7:30 that you couldn't at 5:30

1. Share a repo with a partner without stepping on each other
2. Branch → commit → push → open a PR → **review a real person's work** → merge → delete branch
3. Agree on a data contract *before* anybody writes code — and find out at 7:00 whether it held
4. Resolve a merge conflict without panicking
5. Move a notebook between **Colab** and **GitHub** in both directions
6. Explore a dataset you've never seen and write up what you found for someone who isn't a data scientist

> There's no scraping tonight and no modeling tonight. Both are coming (Module 3 and
> Module 2). Week 1 is about the workflow you'll use for the rest of the semester.

---

## Before you show up

- Watch the Module 1 videos
- Have a **GitHub account** and **GitHub Desktop** installed and signed in
  → [setup_guide.md](../setup_guide.md)
- Skim [github_fundamentals.md](../github_fundamentals.md) §8–§12 (branches, PRs, conflicts)
- Have [Lab1_instructions_opim5512.md](Lab1_instructions_opim5512.md) open during the lab —
  it's every click you'll need tonight, in order
- Read [BRANCHING_MENTAL_MODEL.md](BRANCHING_MENTAL_MODEL.md) — 5 minutes, and it's the
  difference between the lab making sense and the lab being button-mashing

## Tools — and why we're using two of them

| Tool | What it's for tonight |
|---|---|
| **Google Colab** | Where you write and run code. No install, no environment problems. |
| **GitHub Desktop** | Where you see *what changed*, switch branches, and merge. |
| **github.com** | Where pull requests and reviews happen. |

📎 Click by click, in the order you'll need it:
[Lab1_instructions_opim5512.md](Lab1_instructions_opim5512.md)
📎 Moving notebooks and data between Colab and GitHub:
[COLAB_AND_GITHUB.md](COLAB_AND_GITHUB.md)

Colab is the *editor*. GitHub Desktop is the *map*. You need both because Colab can show you
your code but it can't show you your team.

---

## 🚫 No AI tonight

No Claude, no ChatGPT, no Copilot, no Colab autocomplete suggestions. Type it yourself.

This isn't because those tools are bad — **Module 3 is an entire unit on using them**, and
you'll lean on them hard for the rest of the semester. It's because of what tonight is:

- **Git is muscle memory.** Watching a model resolve a merge conflict teaches you nothing you
  can use at 11pm in November when a merge goes sideways and nobody's around.
- **You're going to approve your partner's pull request.** Approving code you didn't write and
  don't understand is the single habit that makes code review worthless. Tonight is where you
  learn to actually read a diff.

Not never. Not yet.

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
| **5:45–6:05** | **Grab data + the contract.** A creates the repo, adds B, turns on branch protection; both clone. Each makes a branch (`dev-weather` / `dev-demand`), opens their starter and *looks* at their raw data — then *together* you write the data dictionary in the README: column names, units, and above all **what one row's timestamp means**. Each writes their half on their own branch. |
| **6:05–6:40** | **Clean it — one PR each.** Clean your half in Colab, save the notebook + a tidy CSV to your branch, and open **one** pull request that carries your notebook, your contract, and your CSV. |
| **6:40–6:55** | **The ping-pong.** Both PRs open at once. Each of you reviews the *other's* diff on github.com and must actually choose Approve / Comment / Request changes. Merge. Delete branch. |
| **6:55–7:20** | **Joint EDA + the report.** Both pull `main`. Now — and only now — you both have both files. One screen, two people. Explore, then write `REPORT.md`. |
| **7:20–7:30** | **Read-outs.** Every pair puts one figure on the screen and says what it means in one sentence. |

### The collision (it's on purpose)

At some point you will both need to edit the **data dictionary** in `README.md`. Whoever merges
second gets a **merge conflict**. Good. Resolve it together — that conflict is the two of you
having independently named the same column two different things, which is exactly the
conversation you'd otherwise be having in November with a broken model.

---

## The last 25 minutes: you have a manager

Once your two files are merged, the lab stops being about git and starts being about the data.

> **From:** your manager
> **Subject:** weather and our load
>
> We keep hearing that hot weather drives up electricity demand. Before I take a position on
> it, I want to see it in our own data. Come back with a one-page summary. **I have about
> ninety seconds and I do not know what a correlation coefficient is.**

**Never two people in the report notebook at once** — a notebook is JSON and figures are binary,
so git can't merge them; simultaneous edits mean one of you overwrites the other. Two safe ways:

- **Same screen (in person):** one drives, one navigates, swap after ten minutes. Only the
  driver's laptop commits; the navigator reviews the PR. **Fastest in this 25-minute window.**
- **Relay (remote / online-only, if there's time):** A pulls `main` → adds plots → pushes →
  merges; **then** B pulls `main` (now has A's work) → adds plots → pushes → merges. Take turns,
  and **pull `main` at the start of every turn** or you'll wipe your partner's plots.

Same idea either way — **divide when files are separate, pair when they're not.** That's how real
analysis actually gets done.

**Find three things.** At least one has to surprise you. Then write it up:

- `REPORT.md` — copy the skeleton from [REPORT_TEMPLATE.md](REPORT_TEMPLATE.md)
- `figures/` — your best two or three, titled and labeled well enough for someone who's never
  seen this data

Then commit it on a branch, open a PR, and have your partner review it. Last loop of the night.

> 💡 A number your manager will understand: **"each degree above 75 °F adds roughly ___ MW"**
> lands far better than "r = 0.57". See if you can produce one sentence of that shape.

There's at least one genuinely surprising thing in this dataset. We're not going to tell you
what it is. If nobody finds it by 7:25, Dave will.

## Definition of done — what's in the repo at 7:30

- [ ] Both partners listed as collaborators; branch protection on `main` (PR + 1 approval)
- [ ] `README.md` with a data dictionary covering **both** cleaned files
- [ ] `data/clean/weather_hourly.csv` and `data/clean/demand_hourly.csv`
- [ ] `notebooks/` — two cleaning notebooks plus the joint EDA notebook
- [ ] **`REPORT.md`** — three findings, two or three figures, honest caveats, plain English
- [ ] `figures/` — the images the report points at
- [ ] **≥3 merged pull requests** (one each for your halves + the report), branches deleted, both of you authoring and reviewing
- [ ] A network graph showing the loop going both ways

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
