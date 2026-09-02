# Lab 1 — facilitator notes

**Dave only.** Hartford **Wed Sep 2** · Stamford **Wed Sep 9**. Same lab, run twice.

---

## What this lab is actually teaching

Not pandas. Not energy. **The collaboration loop**, using energy data as the vehicle because
it's the spine of the whole semester.

The design constraint that makes it work: **Partner A and Partner B each hold half the answer.**
The final plot is physically unreachable until both pull requests merge. Nobody has to be told
that merging matters — they hit the wall themselves at 7:05.

If you only have time to say one thing, say this: *"tonight the deliverable is a repo, not a
notebook."*

---

## Room setup (before 5:30)

- Class repo open on the projector, on the `Lab1_FirstCommit` folder
- A pair repo of your own, pre-made, so you can demo the loop cold
- The **network graph** view bookmarked (`Insights → Network` on any repo) — you'll want it
  three times tonight
- Have `solutions/` open in a second window but **do not share the link**
- Know your line on AI: **no Claude, no ChatGPT, no Copilot tonight.** Reason below.

## Timing

| Time | Segment | Watch for |
|---|---|---|
| 5:30–5:45 | Pair up, stack check | Anyone not signed into GitHub Desktop — fix now, not at 6:40 |
| 5:45–6:05 | **Grab data + the contract** | They open their starter and *look* first, then write the contract. Don't let them skip the contract. |
| 6:05–6:40 | Clean it — one PR each | Quiet room. Circulate. |
| 6:40–6:55 | **The ping-pong** | Both PRs open at once (one each). Force a real Approve click. |
| 6:55–7:20 | **Joint EDA + report** | The heart of the night. Hands off — let them explore. |
| 7:20–7:30 | Read-outs | One figure per pair, one sentence. |

Running long is normal. **Protect the joint EDA — it's 25 minutes and it needs all 25.** If
you're behind, take it out of the contract segment or the ping-pong, never out of 6:55–7:20. A
pair that merges but never explores did a git tutorial, not a data science lab.

**One branch, one PR per partner.** Each person's single `dev-` branch carries their starter
notebook, their half of the README contract, *and* their CSV — so they open **one** pull request
that covers all three (the README half is what collides in Part 5). Two PRs total (one each),
plus the report PR at the end = three merged PRs. Earlier drafts split the contract into its own
PR; that was two branches per person and confused even the instructor — collapsed to one on
purpose. Fewer, cleaner loops beat more, confusing ones.

---

## Grab data + the contract segment (5:45–6:05) — don't shorten this

First have each partner make their branch, open their starter in Colab, and **run the first cell
to actually look at their raw data** — they can't name columns they haven't seen. Then, before
any cleaning code, they agree the contract.

Make them write, in the README (on their own branch), before any cleaning:
- exact **column names** for both cleaned files
- **units** for every column
- the **timestamp convention** — this is the one that bites (ISO-NE Hour Ending → subtract 1)
- the **filenames** and where they live

> Say out loud: *"the merge conflict you get at 7:05 is a disagreement you're having right now
> and haven't noticed yet."*

The contract goes on each partner's `dev-` branch — **not a separate PR.** It rides out with
their notebook and CSV in the one PR at the end of Part 3, and the two halves collide when the
second PR merges (Part 5).

---

## The no-AI rule (say it at 5:35, don't apologize for it)

Tonight is hands-on-keyboard. No Claude, no ChatGPT, no Copilot, no Colab AI autocomplete.

The honest reason, and it's worth giving them: **git is muscle memory and review judgment,
neither of which transfers by watching.** A student who has Claude generate the merge-conflict
resolution has learned nothing they can use at 11pm in November when a merge goes sideways and
they're alone. Worse, they'll be approving a partner's pull request they didn't actually read
— which is the one habit that makes code review worthless.

Frame it as **"not yet," not "never."** Module 3 is an entire unit on LLM-assisted ETL and
they'll use it hard. Say that when you set the rule, or it reads as arbitrary.

Practical enforcement is light: Colab's AI suggestions are off unless they turn them on, and
you'll see it in the room. If somebody's clearly generating, the useful intervention is to ask
them to explain their own diff in the PR review — which is the actual skill being dodged.

---

## Running the joint EDA (6:55–7:20) — hands off

This is the segment where you have to resist yourself. They will flounder for the first three
minutes. **Let them.** That's what open-ended looks like from the inside, and it's the first
time all night they haven't been following instructions.

Set it up in 60 seconds and then get out of the way:

> *"You've got 744 hours of weather and demand in one table. Your manager wants a page. Three
> findings, one of them surprising, and be honest about what the data can't tell you. One
> screen, two people, swap the keyboard at 7:05."*

**Circulate silently.** When a pair is stuck, ask a question instead of giving a plot:
*"what's the biggest number in the load column, and when did it happen?"* — that alone gets
most pairs moving.

**Push on figure quality**, not on quantity. The single most useful correction you can make all
night is *"that title names your columns; make it state your finding."* Two good figures beat
six mediocre ones.

**The caveats section is the real assessment.** A pair that writes "we only have one month and
it's summer, so this says nothing about winter heating" has understood something most
first-semester students haven't. Call it out loud when you see it.

### The read-outs (7:20–7:30)
One figure per pair on the projector, one sentence of interpretation. Not a presentation —
seven pairs at ninety seconds each. Then close the loop yourself:

**If nobody has found it, reveal the hottest-hour / peak-hour split at 7:25** (numbers below).
It works far better as your closing move than as an assignment, and it hands you the Module 4
teaser for free.

---

## The engineered collision

Both partners must edit the data dictionary section of `README.md`. Second to merge gets the
conflict. This is deliberate — do not let them avoid it by "you go first."

Resolve it on the projector once if more than two pairs hit it at the same time.

**Conflicts on `.md` are fine. Conflicts on `.ipynb` are a nightmare.** If you have five spare
minutes, deliberately show them a notebook conflict — open the raw JSON diff, let them see the
base64 image data, then close it. Thirty seconds of that sells "one notebook per person"
better than any lecture. Full argument in `BRANCHING_MENTAL_MODEL.md`.

---

## The punchline — your closing reveal

Joined, the data says (verified 2026-08-20 by `tools/verify_lab1.py`):

| | Hartford / KBDL | Stamford / KBDR |
|---|---|---|
| matched hours | 743 of 744 | 743 of 744 |
| correlation(temp, load) | **0.566** | **0.655** |
| daily trough | 3am, ~13,100 MW | 3am |
| daily peak | 6pm, ~18,500 MW | 6pm |
| **hottest hour** | **Aug 6, 2pm — 91 °F** | **Aug 9, 3pm — 91 °F** |
| **peak-demand hour** | **Aug 7, 6pm — 23,677 MW at 88 °F** | same (shared grid) |

Mean load by temperature band: ~11,700 MW at 50–60 °F, ~15,600 at 70–80, ~21,200 above 90.

**The peak-demand hour is not the hottest hour, and it isn't even the same day.** That's the
insight to fish for. Three reasons worth landing:

1. **Thermal mass** — buildings absorb heat all day; the AC load peaks after the air does.
2. **Human schedule** — people get home at 6pm and turn things on. Demand is behavioral, not
   just physical.
3. **Cumulative heat** — Aug 7 was the second hot day running. Buildings that never cooled
   overnight start the day already warm. This is why forecasters use *lagged* temperature, and
   it's the reason Module 4's window method exists.

> 🔷 **Cross-campus nugget worth 30 seconds:** Bridgeport correlates *better* with New England
> demand (0.655) than Bradley does (0.566), even though Bradley is closer to the population
> centroid of the region. Coastal vs. inland, and the fact that ISO-NE load is dominated by
> the Boston–Providence–Hartford corridor. Neither cohort can see this alone — you can, and
> it's a nice thing to mention in week 2.

If a pair finds this on their own, **have them present it instead of you.** It's a better
ending than anything you'd say. If nobody does, it's your 7:25 close.

**For a pair that's way ahead:** ask whether the relationship is really a straight line. It
isn't — it's a U, and they can't see the heating side in a July–August sample. If they work
that out from first principles and write it into their caveats, that's an A-grade instinct.

**Other things pairs reliably find** (so you can react well): the weekday/weekend gap, the
morning shoulder around 7am, and the fact that dew point tracks load about as well as
temperature does. All three are correct and worth affirming.

---

## What will actually break

| Symptom | Cause | Fix |
|---|---|---|
| "Where's *Save a copy in GitHub*?" | there is no such item — the notebook was opened *from* GitHub | use plain **File → Save**; it pops the Copy-to-GitHub dialog |
| Colab **File → Save** does nothing | popup blocked | allow popups for `colab.research.google.com` |
| "I saved but GitHub didn't change" | they hit Ctrl+S (autosaves to Drive only) | GitHub save is a deliberate snapshot — **File → Save**, and re-save after each edit |
| Can't type their branch in the Colab save dialog | branch field is existing-only | make the branch in GitHub Desktop first, then pick it from the dropdown |
| Save to GitHub fails with a vague error | they aimed at protected `main` | save to the dev branch |
| `raw.githubusercontent.com` 404s | pair repo is **private** | make it public — nothing in it is sensitive |
| Temperature column is a string | didn't set `na_values=["M"]` | that's the lesson; let them find it |
| Join returns 0 rows | hour-ending convention mismatch | **do not fix it for them** — make them diff the two columns |
| Join returns ~740 not 744 | missing METAR hours | real; goes in the data dictionary |
| Somebody protects **all** branches | branch protection rule set too wide | happens on your own A02 video — let it happen, fix it together |
| A pair commits the raw CSVs too | nobody said not to | fine tonight; flag it as Module 3's problem |
| GitHub Desktop shows 200 changed files | committed a `.ipynb_checkpoints` or venv | add `.gitignore`, teach it live |

**Pairs finish at wildly different speeds.** Fast pairs help slow pairs — that's the fastest
route to a working room, and it's worth saying explicitly at 6:15.

---

## Two campuses, one lab

**Between Sep 2 and Sep 9, fix bugs only — not content.**

If Hartford hits a broken URL or a genuinely wrong instruction, fix it. If Hartford found a
segment *easy*, leave it alone — otherwise the two cohorts didn't take the same lab and you
can't compare anything.

Keep a running note below. It's your Stamford prep, and next year's redesign.

### What broke in Hartford (fill in Sep 2)

```
timing:      contract segment ran ___ min
stuck point:
surprise:
fix before Stamford:
```

**Campus difference by design:** Hartford analyzes **KBDL** (Bradley), Stamford analyzes
**KBDR** (Sikorsky, Bridgeport). Same demand series, different airport. If anyone asks why:
the grid is shared, the weather is local. The two correlations are *not* identical (see the
cross-campus nugget above), which is itself worth 30 seconds.

> ⚠️ **Scheduling catch:** 11/11 (Veterans) and 11/25 (Thanksgiving) both fall on **Hartford**
> weeks. If UConn cancels, Hartford loses two in-person labs that Stamford keeps. Decide the
> fix before the schedule decides it for you.

---

## Data provenance

Everything in `data/` was pulled **2026-08-20** and covers **Jul 20 – Aug 19, 2026** (744 hours).

- **Demand** — ISO-NE `hourlysystemdemand` report, unmodified.
  ⚠️ The report page URL changed: the working referer is
  `.../load-and-demand/-/tree/dmnd-five-minute-sys`. The old one now 500s.
- **Weather** — IEM ASOS archive, `report_type=3` (routine hourly METAR), unmodified.

Refresh both with `tools/refresh_lab1_data.py`. Do it once in late August so the "current
month" framing stays true, and re-run the solution notebook afterward to confirm the punchline
still holds.

---

## Tooling progression — why Colab now, VS Code soon (design rationale)

**Week 1 / Lab 1 uses Colab on purpose.** The real subject of Lab 1 is the GitHub
collaboration loop, not Python setup. Colab hands all ~30 students an identical, zero-install
environment in the browser, so nobody is stuck at 5:40 with a broken `pip`/kernel while the
rest do git. The one-line principle:

> **Colab GUARANTEES the environment. VS Code ASSUMES it.** Week 1 you can't assume it yet.

You *could* run the whole lab in VS Code (edit notebook, run, clean, commit, push — one tool,
all local, and it dodges Colab's cross-repo save quirks). The cost is that it requires VS Code
+ Python + pandas/matplotlib + the Jupyter extension + the right kernel on every laptop. That
assumption is what eats the first hour of a mixed Windows/Mac room.

**The planned hand-off (Dave, Sep 1):**
- **A02 (Ping Pong)** → **VS Code, run locally.** The A02 notebook already carries the
  virtual-environment + `requirements.txt` + Windows/Mac/Linux "run the code" sections — it is
  built to move students off Colab and onto their own machine.
- **Lab 2** → **VS Code** as well.

So the sequence is Colab (Lab 1) → local/VS Code (A02, Lab 2) → cloud (Module 3, GCP). Each
step is "now make it run somewhere less forgiving," and that escalation is itself the
curriculum. Don't quietly flip Lab 1 to VS Code to "simplify" — the browser start is load-
bearing.
