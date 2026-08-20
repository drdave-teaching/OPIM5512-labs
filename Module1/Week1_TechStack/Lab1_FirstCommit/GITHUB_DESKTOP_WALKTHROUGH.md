# GitHub Desktop — the walkthrough for Lab 1

**OPIM 5512 · Module 1 · keep this open during the lab**

Every click you need tonight, in the order you'll need it. This is the *specific* path for this
lab — the general reference, with pictures, is
[github_fundamentals.md](../github_fundamentals.md).

> 🚫 **No AI tonight.** No Claude, no ChatGPT, no Copilot, no Colab autocomplete suggestions.
> Not because they're bad — Module 3 is an entire unit on using them — but because git is
> muscle memory, and you can't approve a partner's pull request you didn't actually read.
> Tonight is hands on keyboard. **Type it.**

---

## Before 5:30 — check these three things

1. **GitHub Desktop opens and you're signed in.**
   `File → Options → Accounts` (Windows) / `GitHub Desktop → Settings → Accounts` (Mac).
   You should see your username. If not, sign in now, not at 6:40.
2. **Git knows who you are.** Same Options window → **Git** tab. Name and email filled in.
   Use the email on your GitHub account or your commits won't link to you.
3. **colab.research.google.com opens** and you're signed into a Google account.

---

# Part 1 — Set up the repo (Partner A drives, 5:45)

Only **one** of you does this. Partner B watches over the shoulder — you'll need to know it
too, and there's no second repo to practice on.

### 1.1 Create it on github.com

Go to **github.com** → green **New** button (or the **+** at top right → New repository).

| Field | What to put |
|---|---|
| Repository name | `opim5512-lab1-<netidA>-<netidB>` |
| Description | "Weather and electricity demand — OPIM 5512 Lab 1" |
| **Public / Private** | ⚠️ **Public.** Colab reads your CSVs over a raw URL, and raw URLs don't work on private repos. There's nothing sensitive in here. |
| Add a README file | ✅ **check it** — you need at least one commit to exist before you can protect a branch |
| .gitignore template | **Python** |

Click **Create repository**.

### 1.2 Add your partner

**Settings** (tab across the top of the repo) → **Collaborators** in the left sidebar →
**Add people** → type their GitHub username → **Add to this repository**.

**Partner B: go check your email or your GitHub notifications and accept the invitation.**
Nothing works for you until you do. This trips up someone every single time.

### 1.3 Turn on branch protection

This is the rule that makes the whole night work: it means nobody — including you — can push
straight to `main`. Every change has to go through a pull request that the other person
approves.

**Settings** → **Rules → Rulesets** in the left sidebar → **New ruleset → New branch ruleset**.

- **Ruleset name:** `protect-main`
- **Enforcement status:** switch it to **Active** ← easy to miss, and it does nothing without this
- **Target branches:** **Add target → Include default branch**
- Under **Branch rules**, tick:
  - ✅ **Require a pull request before merging**
  - set **Required approvals** to **1**
  - ✅ **Block force pushes**

Click **Create**.

> ⚠️ **Target the default branch only.** If you protect `[All branches]` you'll block your own
> `dev-` branches and nothing will push. If that happens tonight: it's a two-click fix, and
> honestly it's worth seeing once.

### 1.4 Both of you: get it onto your laptop

In **GitHub Desktop**: `File → Clone repository` → **GitHub.com** tab → find the repo in the
list → note the **Local path** (remember where it is, you'll be dragging files there) →
**Clone**.

If you don't see it, click the refresh icon, and make sure Partner B accepted the invite.

---

# Part 2 — The contract (both, 5:45–6:05)

Before either of you writes code, agree on what your two output files look like and write it
down in the README. Column names, units, filenames, and — the one that bites — **what a
timestamp means.**

Each of you makes this a real pull request, so you've done the loop once before it matters.

Follow **Part 3** below for the mechanics; the only difference is you're editing `README.md`
instead of adding a CSV. Use branch names `contract-<yourname>`.

---

# Part 3 — The loop (each of you, on your own branch, 6:05–6:40)

This is the core cycle. You'll do it several times tonight and hundreds of times in your career.

### 3.1 Make your branch

In GitHub Desktop, look at the **top bar**. It has three boxes: current repository, **current
branch**, and the publish/push button. You'll be reading this bar constantly.

Click **Current branch** → **New branch** → name it:

- Partner A: `dev-weather`
- Partner B: `dev-demand`

→ **Create branch**. The top bar should now show your branch name, not `main`.

> 🔴 **The single most common mistake tonight is doing work while `main` is selected.**
> Check the top bar. Check it again before every commit.

Click **Publish branch** so it exists on GitHub too.

### 3.2 Do the work in Colab

Open your starter notebook, clean your half, produce your CSV, and download it — that's all in
[COLAB_AND_GITHUB.md](COLAB_AND_GITHUB.md). Come back here when the file is in your Downloads
folder.

### 3.3 Put the file in the repo

Open your repo folder on disk (the Local path from step 1.4). Make a folder called `data`, and
inside it one called `clean`. Drag your downloaded CSV in:

- Partner A → `data/clean/weather_hourly.csv`
- Partner B → `data/clean/demand_hourly.csv`

### 3.4 Commit

Switch to GitHub Desktop. It noticed. The **Changes** tab on the left now lists your file.

1. **Click the filename** and actually look at the diff on the right. For a new CSV you'll see
   green lines — your data. *Look at it.* This is the habit: never commit something you
   haven't looked at.
2. Bottom left, write a **Summary**. A real one:
   - ✅ `Add cleaned hourly weather for KBDL, Jul 20 - Aug 19`
   - ❌ `update`, `stuff`, `asdf`
3. Click **Commit to `dev-weather`** (it names your branch on the button — read it).
4. Click **Push origin** in the top bar.

### 3.5 Open the pull request

After pushing, Desktop shows a blue banner: **Create Pull Request**. Click it — it opens
github.com.

- Check the arrow at the top: it should say **base: main ← compare: dev-weather**
- Title: what you did
- Description: what your partner should look at. *"Check my column names against the contract"*
  is a great PR description.
- **Create pull request**

Now tell your partner. Out loud. They're sitting next to you.

---

# Part 4 — The ping-pong (6:40–6:55)

Both PRs are open at once. You review theirs, they review yours.

### 4.1 Review your partner's PR

On github.com, open **their** pull request → the **Files changed** tab.

Read it. Actually read it. Then click **Review changes** (top right) and pick one — you must
pick one:

| | When |
|---|---|
| **Comment** | you have a question but aren't blocking |
| **Approve** | you read it and it's good |
| **Request changes** | something's wrong — say specifically what |

Write a sentence. "Looks good" is not a review. Try *"column names match the contract, and I
like that you kept the missing hour instead of dropping it."*

→ **Submit review**

### 4.2 Merge

Once your partner has approved *your* PR, go to your PR → **Merge pull request** → **Confirm
merge** → **Delete branch** (the button appears right after; take it).

If the merge button is greyed out, you don't have an approval yet. That's branch protection
doing its job.

### 4.3 Both of you: come home to main

In GitHub Desktop:
1. **Current branch** → **main**
2. **Fetch origin**
3. **Pull origin**

Now look in `data/clean/`. **Both files are there.** Neither of you could have gotten here
alone — that's the point of the last hour.

---

# Part 5 — The merge conflict (it's on purpose)

You both edited the data dictionary in `README.md`. Whoever merges second gets this:

```
This branch has conflicts that must be resolved
```

**Don't panic and don't start over.** Here's the fix, in Desktop:

1. **Current branch → main**, then **Fetch** and **Pull** so you have your partner's version
2. **Current branch → your branch**
3. **Branch → Update from main**
4. Desktop says there's a conflict and offers **Open in editor** — do that

You'll see this in the file:

```
<<<<<<< HEAD
temp_f: hourly temperature at the airport, degrees Fahrenheit
=======
temperature: air temp (F) from the METAR observation
>>>>>>> main
```

Top block is yours. Bottom block is theirs. **Decide together what the line should say** — it
can be either one, or a third thing you write — then **delete all three marker lines**
(`<<<<<<<`, `=======`, `>>>>>>>`). Save.

Back in Desktop: the conflict warning clears → **Continue merge** → commit → **Push**. Your PR
updates itself and the merge button comes back.

> That conflict wasn't a git problem. It was the two of you naming the same column two
> different ways, and git refusing to guess which one was right. Fixing it took thirty seconds.
> Finding it in November, inside a broken model, would have taken an afternoon.

---

# Part 6 — The report (7:20ish)

Same loop one last time, together this time. Whoever's driving:

1. New branch: `report`
2. Add `REPORT.md` and your `figures/` folder to the repo on disk
3. Commit → Push → Create Pull Request
4. Your partner reviews it — and for a written report, "request changes" is a completely
   normal and useful thing to do
5. Merge, delete branch, pull `main`

---

## Show your work: the network graph

On github.com: **Insights** tab → **Network** in the sidebar.

You should see a picture of tonight: `main` running along, two branches peeling off and
rejoining, then another. **That graph is the deliverable.** It's proof that two people worked
in one repo without breaking each other, and it can't be faked by one person doing everything.

---

## When something goes wrong

| What you see | What it means | What to do |
|---|---|---|
| Push rejected, "protected branch" | you're on `main` | Check the top bar. Make a branch, commit there. |
| Merge button greyed out | no approval yet | Your partner has to approve. Ask them. |
| Partner can't see the repo | invite not accepted | Check GitHub notifications / email |
| `raw.githubusercontent.com` 404 in Colab | repo is private, or wrong branch in the URL | Make it public; check `main` vs your branch |
| Desktop shows 300 changed files | you committed `__pycache__` or `.ipynb_checkpoints` | Add them to `.gitignore`, then `Repository → Repository settings` |
| "Changes" is empty but you saved the file | you saved it outside the repo folder | Check the Local path from step 1.4 |
| You committed to the wrong branch | happens to everyone | **Don't** try to undo it. Ask Dave — it's a 20-second fix and worth watching once. |

> **The one thing not to do:** don't delete the folder and re-clone to escape a problem. You'll
> lose work, and the problem is almost always two clicks. Ask instead — that's what the room is
> for tonight.
