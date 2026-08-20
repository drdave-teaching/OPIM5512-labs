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

## Timing

| Time | Segment | Watch for |
|---|---|---|
| 5:30–5:45 | Pair up, stack check | Anyone not signed into GitHub Desktop — fix now, not at 6:40 |
| 5:45–6:10 | **The contract** | This is the segment everyone wants to skip. Don't let them. |
| 6:10–6:45 | Split and work | Quiet room. Circulate. |
| 6:45–7:05 | **The ping-pong** | Two PRs open at once. Force a real Approve click. |
| 7:05–7:20 | **The join** | The payoff. Get a pair to put the scatter on the projector. |
| 7:20–7:30 | Rounds | Each pair says their one insight out loud. |

Running long is normal. **Protect the join.** If you're behind at 7:00, cut the second
ping-pong round, not the merge — a pair that never merges never learns the lesson.

---

## The contract segment (5:45–6:10) — don't shorten this

Pairs will want to start coding. The whole point is that they can't, yet, because they haven't
agreed on what the output looks like.

Make them write, in the README, before any code:
- exact **column names** for both cleaned files
- **units** for every column
- the **timestamp convention** — this is the one that bites
- the **filenames** and where they live

> Say out loud: *"the merge conflict you get at 7:05 is a disagreement you're having right now
> and haven't noticed yet."*

Then have each partner open a PR on the README. That's PR #1 and #2, done before the coding
even starts, which takes the fear out of the loop.

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

## The punchline

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

If a pair gets there on their own, have them present it. It's a better ending than anything
you'd say.

**Backup insight** if a pair is way ahead: ask them what the *lowest*-demand hours look like
and whether the relationship is really a straight line. (It isn't — it's a U, they just can't
see the heating side in a July–August sample. That's the Module 4 tease.)

---

## What will actually break

| Symptom | Cause | Fix |
|---|---|---|
| Colab "Save a copy in GitHub" does nothing | popup blocked | allow popups for `colab.research.google.com` |
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
