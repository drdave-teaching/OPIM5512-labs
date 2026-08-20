# How to think about branches and merging

**OPIM 5512 · Module 1 · read before Lab 1**

You already know how to collaborate on a Google Doc: everybody types into the same live
document, the last person to type wins, and there is no moment where a human says *"yes,
this change is good."* That works fine for prose. It is a catastrophe for code, because
code either runs or it doesn't, and "last write wins" is how a working model turns into a
broken one at 11pm the night before a deadline.

Git is the opposite arrangement. **Everyone works on their own copy, and someone has to
say yes before it becomes the team's copy.** Branches are how you get your own copy.
Merging is the "say yes."

That's the whole idea. The rest is vocabulary.

---

## The four sentences that matter

**1. `main` is what the team agrees is true right now.**
Not "the newest code." Not "Dave's code." The version you'd be comfortable with a
stranger cloning and running. If `main` is broken, the team is broken.

**2. A branch is a proposal.**
It is a string of commits that nobody else has to trust yet. You are saying *"here is a
version of the world where I added the lag features"* — and until it merges, no one else
is affected by it. You can abandon it and lose nothing.

**3. Branches are cheap. Make one for every question you're asking.**
A branch is not a copy of your files. It's a bookmark pointing at a commit. Creating one
costs nothing and takes two seconds. The right number of branches is *one per idea*, not
one per week.

**4. Merging is a decision, not a file operation.**
Git can splice two histories together automatically **when the two branches touched
different lines**. When they touched the *same* lines, git refuses to guess whose version
is right and hands it to you. That's a **merge conflict** — and it is git being careful,
not git being broken. A conflict is a question: *"you two disagree about this line, which
one do you want?"*

---

## The picture

```
                  o---o---o   dev-weather   (your proposal)
                 /         \
main  o---o---o------------(M)---o          (the team's truth)
                 \         /
                  o---o---o   dev-demand    (your partner's proposal)
```

Everything below `main` is a conversation. `main` itself is the conclusion.

The `(M)` is the merge — and in this class, the merge only happens after a human has
looked at the diff and clicked **Approve**. That human review is the entire reason we use
pull requests instead of just pushing to `main`.

---

## Rules that keep you out of trouble

**Name the branch after the question, not the file.**
`try-24h-lag-features` tells your partner what you're attempting. `dave-edits` tells them
nothing and ages badly. You'll have five branches by October and you'll need to know which
one was the good idea.

**One branch = one idea = one pull request.**
If you can't describe the branch in a single sentence, it's two branches. This is the
single highest-leverage habit in this list, because a PR that does one thing can actually
be reviewed, and a PR that does six things gets rubber-stamped.

**⚠️ Notebooks do not merge. Plan around it.**
A `.ipynb` file is JSON — it stores your code, *and* your outputs, *and* execution counts,
*and* cell IDs. Two people editing the same notebook on two branches produces a conflict
full of base64 image data that no human being wants to read. There is no clever fix; there
is only prevention:

> **One notebook per person.** Partition the work by *file*, not by *section*.

This is exactly why Lab 1 gives Partner A and Partner B different files to create. It's
not busywork — it's the professional workaround for a real limitation of the tool.
(Shared `.py` files and `.md` files merge fine, because they're plain lines of text. That's
also a quiet argument for moving finished code *out* of notebooks and into `src/`.)

**Merge `main` into your branch often.**
The size of a merge conflict is proportional to how long the branch has been alive. A
branch that's three days old and two commits behind `main` merges silently. A branch
that's three weeks old is a conflict with a countdown timer on it. In GitHub Desktop:
**Branch → Update from main**.

**Delete the branch after it merges.**
Its commits live on inside `main` forever. Keeping the branch around just clutters the
dropdown and tempts someone to commit to it six weeks later.

---

## When should I make a branch?

> **When you're about to do something you might want to throw away.**

That's it. Trying a new model? Branch. Rewriting the cleaning step? Branch. Fixing a typo
in the README? Honestly, also branch — because in this class `main` is protected and you
*can't* commit to it directly, which is deliberate. The protection is there so that the
review step isn't optional on the night you're in a hurry.

---

## What a conflict actually looks like

```
<<<<<<< HEAD
temperature_f: hourly temperature at the airport, degrees Fahrenheit
=======
temp_f: air temp (F) from the METAR observation
>>>>>>> dev-weather
```

Top block = what's on the branch you're merging **into**. Bottom block = what's coming
**in**. Your job is to decide what the line should say — which might be either version, or
a third thing you write yourself — and then **delete all three marker lines**. Save,
commit, done.

The reason you got this conflict is that you and your partner independently wrote a
definition for the same column. That's not a git problem. That's a *team* problem that git
surfaced. Which brings us to the last idea:

---

## The real lesson

Git doesn't prevent disagreements. It **makes them visible at merge time instead of at
demo time.** Every conflict you resolve in Lab 1 is a conversation you would otherwise
have had in November, with a broken model and a deadline.

Agree on the data contract *first* — column names, units, filenames, timestamps — and most
conflicts never happen. That's why Lab 1 makes you write the data dictionary together
before either of you writes a line of code.

---

📎 Mechanics — the buttons to click — are in
[github_fundamentals.md](../github_fundamentals.md) §8–§12.
