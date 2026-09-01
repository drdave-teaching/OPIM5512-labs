<!-- ↓↓↓ WORKING NOTE — delete this whole box before you submit ↓↓↓ -->

> 🛠 **How to build this report together (then delete this box).**
> A report notebook and its figures **can't be merged by git** — a notebook is JSON and figures
> are binary images, so if two people edit at once, one person's work overwrites the other's.
> The rule: **never two people in it at the same time.** Two safe ways to collaborate:
>
> - **Same screen (in person):** one *drives*, one *navigates*, swap every ~10 minutes. Only the
>   driver's laptop commits; the partner reviews the pull request. Fastest in the 25-minute window.
> - **Relay (remote / online-only, if there's time):** Partner A pulls `main` → adds a plot or two
>   → pushes → merges. **Then** Partner B pulls `main` (now B has A's work) → adds more → pushes →
>   merges. Take turns. ⚠️ **Pull `main` at the start of every turn** — skip that and you build on
>   an old copy and wipe your partner's plots.
>
> Underneath both: **divide when the files are separate, pair when they're not.** Column names in
> a text file → work apart and merge. A shared notebook full of plots → one person at a time.

<!-- ↑↑↑ delete everything above this line before submitting ↑↑↑ -->

# Weather and New England's electricity demand

**Prepared by:** _(both names)_
**Date:** _(today)_
**Data:** 744 hours, July 20 – August 19 2026. Demand: ISO-NE hourly system load (all of New
England). Weather: hourly observations from _(your airport — KBDL Bradley or KBDR Sikorsky)_.

---

## The short version

_Two or three sentences. If your manager reads nothing else, this is what they get. Lead with
the answer, not the method._

> _Example of the shape we're after — replace it, don't fill it in:_
> _"Yes, heat drives our load, and the effect is large: demand runs about X MW higher on hot
> afternoons than on mild ones. But the hottest hour isn't our peak hour — the peak comes
> later, which matters for how we plan."_

---

## What we found

**1.** _Finding, in plain English, with a number and a unit._

**2.** _Finding._

**3.** _Finding. At least one of your three should be something that surprised you._

---

## The evidence

### _Figure title that states the finding_

![](figures/your_figure.png)

_One or two sentences: what should the reader notice, and what does it mean? Don't describe
the chart — interpret it._

### _Second figure title_

![](figures/your_second_figure.png)

_Same again._

---

## What this data can't tell us

_Be honest and specific. Vague hedging is worse than none. Some real ones to consider:_

- _We have one month, and it's summer. Nothing here says anything about January._
- _We used one airport as a proxy for weather across all of New England._
- _We're describing a relationship, not proving a cause._
- _(How many hours were missing, and did that matter?)_

---

## What we'd do next

_One or two concrete things — the questions you'd chase if you had another week. This is the
section that gets you asked back._

---

<sub>Repo: _(link)_ · Analysis by _(A)_ (weather) and _(B)_ (demand) · Built for OPIM 5512 Lab 1</sub>
