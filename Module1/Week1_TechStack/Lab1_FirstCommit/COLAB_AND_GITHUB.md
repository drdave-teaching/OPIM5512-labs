# Colab ↔ GitHub — moving work in both directions

**OPIM 5512 · Module 1**

We develop in **Colab** because it works: no installs, no "it runs on my machine," a free GPU
when you need one. We keep the work in **GitHub** because Colab has no memory of your team and
no way to say *"this version is the good one."*

So you need to move things between them. Here's every path you'll actually use.

---

## The map

```
   github.com  ────────►  Colab          "open the starter"
   (the truth)            (the editor)

   Colab       ────────►  a branch       "Save a copy in GitHub"
                          on github.com

   github.com  ────────►  your laptop    GitHub Desktop: Fetch / Pull
                          (GitHub Desktop = the map: branches, diffs, merges)
```

**Colab edits. Desktop reviews and merges. GitHub decides.**

---

## 1. Open a notebook *from* GitHub in Colab

**The easy way** — click the badge in the repo:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/drdave-teaching/OPIM5512-labs/blob/main/Module1/Week1_TechStack/Lab1_FirstCommit/notebooks/Lab1_Starter.ipynb)

**The menu way** — in Colab: **File → Open notebook → GitHub** tab → paste the repo URL →
pick the branch → pick the notebook.

**The URL way** — worth knowing, because it works for *any* notebook on GitHub. Take the
github.com URL and put `colab.research.google.com/github/` in front of the owner:

```
https://github.com/OWNER/REPO/blob/BRANCH/path/nb.ipynb
https://colab.research.google.com/github/OWNER/REPO/blob/BRANCH/path/nb.ipynb
```

> ⚠️ **Watch the branch in the URL.** Opening `/blob/main/...` gives you `main`'s version, not
> your branch's. If your edits "disappeared," this is why 90% of the time.

---

## 2. Read the data *from* GitHub, in Colab

Don't upload CSVs by hand every session. Read them straight from the repo:

```python
import pandas as pd

RAW = "https://raw.githubusercontent.com/drdave-teaching/OPIM5512-labs/main/Module1/Week1_TechStack/Lab1_FirstCommit/data"

demand_raw = pd.read_csv(f"{RAW}/isone_demand_hourly_raw.csv", header=None, names=["tag","date","he","load_mw"])
```

`raw.githubusercontent.com` is the "give me the file, not the web page" host. Get the URL by
opening the file on github.com and clicking **Raw**.

> ⚠️ **This only works for public repos.** If your pair repo is private, raw URLs 404 for
> everyone including you. Make the lab repo **public** — there's nothing secret in it.

---

## 3. Save your notebook *to* GitHub — the important one

In Colab: **File → Save a copy in GitHub.**

The dialog asks for four things. All four matter:

| Field | What to put |
|---|---|
| **Repository** | your pair repo |
| **Branch** | ⚠️ **your dev branch** — `dev-weather` or `dev-demand`. **Never `main`.** You can *type a new branch name here* and Colab will create it. |
| **File path** | `notebooks/weather_eda.ipynb` — the path inside the repo |
| **Commit message** | a real sentence. "Updated" is not a real sentence. |

The first time, a GitHub authorization popup appears. **Allow popups** for
`colab.research.google.com` or nothing happens and there's no error message.

Tick **"Include a link to Colab"** and it adds the Open-in-Colab badge to the top of the
notebook automatically.

### Three things that surprise everyone

**It commits straight to the branch.** There's no staging, no diff, no "are you sure." What
you have in the browser becomes a commit. This is exactly why we protect `main` — so that a
half-finished 6:40pm notebook physically cannot become the team's truth.

**If you pick a protected branch, it fails.** Colab reports it badly — you'll get a vague
error, not "branch protection blocked this." If saving mysteriously fails, check that you
weren't aiming at `main`.

**Outputs get committed too.** Your plots, your `df.head()` tables, everything — as base64
inside the JSON. Your partner's PR review will show a wall of unreadable diff. That's normal
and it's the reason for the next rule.

> ### 🚨 The rule that saves the semester
> **One notebook per person.** Never two people editing the same `.ipynb` on two branches.
> Notebooks are JSON with pictures inside; git cannot merge them and neither can you.
> Partition the work by *file*. Details in [BRANCHING_MENTAL_MODEL.md](BRANCHING_MENTAL_MODEL.md).

---

## 4. Get a *data file* out of Colab and into the repo

Colab's disk is temporary — when the runtime disconnects, your `weather_hourly.csv` is gone.
"Save a copy in GitHub" only saves the **notebook**, not the files it wrote.

For Week 1, the honest path — and it's two minutes:

```python
df.to_csv("weather_hourly.csv", index=False)

from google.colab import files
files.download("weather_hourly.csv")     # lands in your Downloads folder
```

Then: drag it into your repo folder on disk → **GitHub Desktop** shows it as a new file →
write a commit message → **Commit to `dev-weather`** → **Push**.

That round trip is worth doing by hand once. It's the moment GitHub Desktop stops being
mysterious: you can *see* the file arrive, see the diff, and choose whether it goes in.

> In Module 3 we replace this whole dance with a scheduled job on GCP that writes to cloud
> storage, and nobody ever downloads a CSV again. Feel the friction first — it's the reason
> that lesson lands.

---

## 5. Pull your partner's work back down

After both PRs merge, in **GitHub Desktop**: switch to `main` → **Fetch origin** → **Pull**.
Now both cleaned CSVs are on your laptop.

To run the joint notebook in Colab against the *merged* data, either re-open it from the `main`
branch (§1) or point `RAW` at `main` (§2). Both partners should see the same numbers. If you
don't, one of you is reading a stale branch — check the URL.

---

## Cheat sheet

| I want to… | Do this |
|---|---|
| Start from the class starter | Click the Colab badge in the repo |
| Save my work | File → Save a copy in GitHub → **dev branch** |
| Get my data file into the repo | `files.download()` → drag into repo folder → commit in Desktop |
| See what actually changed | GitHub Desktop, **Changes** tab |
| Get my partner's work | Desktop → `main` → Fetch → Pull |
| Propose my work becomes the team's | github.com → Compare & pull request |
| Undo something scary | Don't. Ask. Then Desktop → History → right-click → Revert |
