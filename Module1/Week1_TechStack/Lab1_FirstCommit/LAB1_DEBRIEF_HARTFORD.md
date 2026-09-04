# Lab 1 — Debrief & Skills Check

**OPIM 5512 · Module 1 · Hartford section, Wed Sep 2 2026**
Pulled from the class recording. Watch it here: **[Lab 1 (Hartford) recording](https://kaltura.uconn.edu/media/t/1_b192yazq)**.

> **The headline:** tonight the deliverable was a *repo, not a notebook.* Two people each owned half
> of the same problem — weather and electricity demand — and the only way to the answer was to merge
> the work together. That's the workflow you'll reuse every week this semester.

---

## Did I learn it? — Git & collaboration

Tick the ones you could do again without help. If you can't, that's the thing to practice.

- [ ] Create a repo, add a **collaborator**, and accept the invite
- [ ] Turn on **branch protection** (a ruleset on `main`: require a pull request + 1 approval; block force pushes)
- [ ] **Clone once** in GitHub Desktop, then **Fetch origin**; use **Show in Explorer** to find the files on disk
- [ ] Make **one branch per task** (`dev-weather` / `dev-demand`) and **Publish** it
- [ ] Move a notebook Colab → GitHub with **File → Save** (plain Save; not Ctrl+S), on the right branch
- [ ] Get an output file into the repo: **download → drag into the folder → Commit (real message) → Push**
- [ ] Open a **pull request**, request your partner as reviewer
- [ ] **Review** a partner's PR — read the diff — and choose **Approve / Comment / Request changes**
- [ ] **Merge**, then **delete the branch** (short-lived branches; restorable ~30 days if you need it back)
- [ ] Read the **network graph** (Insights → Network) as the record of who did what, when

## Did I learn it? — Data science (pandas)

- [ ] Recognize "dirty-ish" real data and two series moving at the same hourly **heartbeat**
- [ ] Weather (METAR): readings at **:51 past the hour**, `M` = missing, `T` = trace
- [ ] Demand (ISO-NE): **Hour Ending 1–24** → subtract 1 to get the hour that *begins*
- [ ] Convert a string to a datetime with `pd.to_datetime`, make an `hour` column, set it as the index
- [ ] **Resample/aggregate** to hourly (mean / max / min) and name columns *with units*
- [ ] Make a **line plot** and a **histogram**; save with `plt.savefig`; plot against **time, not row number**
- [ ] Know the window is **744 hours**, and that **one hour is genuinely missing** (a real CT outage)

---

## What actually happened (the honest debrief)

- **The stack held.** Everyone had GitHub, GitHub Desktop, and Colab working; the mechanics landed and both halves merged — the network graph showed the loop going both ways.
- **The data cleaning ate the clock.** Getting the two datasets tidy took long enough that we **ran out of time before the merge conflict and the written report.** That's fine for a first run — the point tonight was the muscle memory of working together.
- **File paths got messy.** As said on the recording near the end: *"we weren't able to be so elegant with our file paths."* Downloads with `(1)`/`(2)` suffixes and files landing in the repo root were the main friction.
- **Solo / online works too.** You can run both roles with two GitHub accounts, switching between them — exactly how it was demoed.

## What changes for next time (Stamford, Sep 9)

- The data comes **pre-cleaned** in a template repo — you spend the night on the *workflow*, not on `M` vs `T`.
- You still write **one plot yourself** (a histogram), so the pull request reviews real code.
- The **report is the finish line**, with the image links pre-wired; the **merge conflict** becomes an explicit "if you're ahead" bonus.

> If you missed anything above, the recording walks all of it end to end, and the extended edition of the lab lets you redo the data-cleaning part on your own.
