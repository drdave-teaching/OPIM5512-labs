# Module 1 — Week 1: Setting Up Your Tech Stack

**OPIM 5512 · Dr. Dave Wanik · University of Connecticut**

---

## Why does this matter?

Before you can do any data science, you need a working environment. This sounds boring — it isn't. In your first job, you'll spend real time on this. Every team has a "stack" (the set of tools everyone agrees to use), and being able to set yours up from scratch — without asking for help — is a signal that you know what you're doing.

The tools we're setting up here (Git, VS Code, Python virtual environments) are used by data scientists at every major company. Learn them once, use them forever.

---

## What you'll be able to do after this

- Install and configure Git, VS Code, and Python
- Create a GitHub account and connect it to your local machine
- Clone a repo, make a change, and push it back to GitHub
- Create and activate a virtual environment so your projects don't step on each other
- Never again say "it works on my machine" — because everyone's machine will be set up the same way

---

## How to run it

This week is about setup, not running scripts. Follow the guide:

1. Open `setup_guide.md` in this folder — work through it top to bottom
2. When you're done, you should be able to run this in your terminal without errors:
   ```bash
   git --version
   python --version
   ```
3. Create your personal class repo (`opim5512-<your-netid>`) and make your first commit

**You'll know you're done when your "Hello World" commit shows up on GitHub.**

---

## 🧪 The live lab — [Lab 1: First Commit](Lab1_FirstCommit/)

**Hartford Wed Sep 2 · Stamford Wed Sep 9 · 5:30–7:30.** Same lab, run twice.

You and a partner each analyze *half* of one problem — one takes the airport weather, one
takes New England's electricity demand — and neither of you can reach the punchline alone.
The only way to see the final plot is to merge your work together.

| Read this | Why |
|---|---|
| [Lab1_FirstCommit/README.md](Lab1_FirstCommit/README.md) | the lab itself, run of show, what "done" means |
| [BRANCHING_MENTAL_MODEL.md](Lab1_FirstCommit/BRANCHING_MENTAL_MODEL.md) | **read before class** — how to think about branches and merging |
| [COLAB_AND_GITHUB.md](Lab1_FirstCommit/COLAB_AND_GITHUB.md) | moving notebooks and data between Colab and GitHub in both directions |
| [github_fundamentals.md](github_fundamentals.md) | the buttons — clone, commit, branch, PR, conflicts |

We develop in **Colab** and keep the work in **GitHub**, using **GitHub Desktop** to see what
changed and to merge. Colab is the editor; Desktop is the map.

---

## The notebooks

The `notebooks/` folder has the original class notebooks for reference:
- `SettingUpTechEnviro.ipynb` — the full walkthrough in notebook form
- `Shell_Bash_commands.ipynb` — useful terminal commands to know
- `DTC_RFC_GBC_BostonHousing.ipynb` — preview of where we're headed (classification)
- `DTR_RFR_GBR_BostonHousing.ipynb` — preview of where we're headed (regression)

Don't stress about the modeling notebooks yet — they're a taste of what's coming in Week 2.
