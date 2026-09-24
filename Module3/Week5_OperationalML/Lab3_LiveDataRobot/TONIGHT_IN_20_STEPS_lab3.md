# Lab 3 — Build a Live Data Robot · Tonight in 20 Steps

**OPIM 5512 · Module 3 — Operational ML**

> **The one-sentence version: tonight you build two tiny APIs and hand them to a robot that collects live energy + weather data every 5 minutes — forever, for free, while you sleep.**
> Partner A builds the **energy** API (ISO-NE), Partner B builds the **weather** API (National Weather Service),
> and you merge them through the same branch → PR → review → merge loop as Labs 1 and 2.

---

## Before we start

- [ ] **GitHub account** + **GitHub Desktop** signed in · **VS Code** opens with the **Python** and **Jupyter** extensions
- [ ] Laptop Python fighting you? Skip the fight: **Codespaces** (your repo → **Code → Codespaces → Create**) is VS Code in the browser with everything pre-installed. Same steps.
- [ ] Roles picked: **Partner A = energy** (`src/isone.py`), **Partner B = weather** (`src/nws.py`)
- [ ] Your job is **3 small TODOs** (A) or **2 small TODOs** (B). The robot and the tests are already written.

> ### ⚠️ The 3 things that trip everyone up (read this first)
> 1. **Partner B must ACCEPT the email invite before anything works.** Check inbox and spam the moment Partner A adds you.
> 2. **Make your `dev-` branch BEFORE you touch any file.** Already edited on `main` by accident? **New branch → "Bring my changes to the new branch" → yes.** Nothing lost.
> 3. **Your repo must be PUBLIC.** Public repos get unlimited free robot minutes. A private repo would burn through its free minutes in about a week.

> **Flying solo?** You are both A and B: set approvals to **0**, make **two branches** (`dev-energy`, `dev-weather`), build energy first, then weather.

---

## The 20 steps, in order

### Set up (steps 1–6)
1. **Pair up:** Partner A (energy) / Partner B (weather).
2. **Partner A:** open the [template repo](https://github.com/drdave-teaching/opim5512-lab3-template) → **Use this template → Create a new repository** → owner = *you*, name `opim5512-lab3-<netidA>-<netidB>`, **Public** → Create.
3. **Partner A:** **Settings → Collaborators → Add people** → Partner B. → **⛔ STOP: Partner B accepts the invite now.**
4. **Partner A:** **Settings → Rules** → ruleset on `main`: **require a pull request** + **1 approval**. *(Solo? approvals = 0.)*
5. **Both:** GitHub Desktop → **File → Clone repository** → pick the repo → **Clone.** Once.
6. **Each:** **Current branch → New branch** → `dev-energy` (A) / `dev-weather` (B) → **Publish branch** → **Fetch/Pull.**

### Build your API (steps 7–12)
7. **Each:** GitHub Desktop → **Repository → Open in Visual Studio Code.** Check the top bar still says your `dev-` branch.
8. **Each:** open **your** file — `src/isone.py` (A) or `src/nws.py` (B). Fill in the **TODOs** (the comments tell you exactly what goes there), then **delete the `raise NotImplementedError` line.** *(Stamford, Partner B: also change `STATION = "KBDL"` to `"KBDR"`.)*
9. **Each:** VS Code terminal → `pip install -r requirements.txt` → `python src/isone.py` (A) or `python src/nws.py` (B). **You should see real rows from right now.**
10. **Each:** GitHub Desktop → top bar = your `dev-` branch → Summary `build the energy API` / `build the weather API` → **Commit → Push.**
11. **Each:** github.com → **Compare & pull request** → **Create** → **Reviewers** → your partner. **Watch the check run:** ✓ green = your tests passed (your partner's show as *skipped* until they merge).
12. **Each:** open your **partner's** PR → **Files changed** → read their function + look for the green ✓ → **Approve.**

### Merge & wake the robot (steps 13–16)
13. **Merge** both PRs → **Delete branch** on each.
14. **Actions** tab → **collect** → **Run workflow** → Run. *(It also runs by itself every ~5 minutes — this just skips the wait.)*
15. When the run turns ✓, go to **Code** → switch the branch menu from `main` to **`data`** → open `isone_5min.csv` and `weather_obs.csv`. **That's your robot's work.**
16. **Both:** GitHub Desktop → **main → Fetch → Pull.** *(Your laptop gets the merged code; the data stays on the `data` branch.)*

### Watch it live (steps 17–20)
17. **VS Code** (on `main` now) → open `notebooks/Lab3_Watch_Your_Live_Data.ipynb` → **Select Kernel** (top right → your Python) → set `OWNER` and `REPO` → **Run All.**
18. **Look at the solar gap plot:** when is rooftop solar hiding the most demand from the grid?
19. **Wait an hour, run the notebook again — more rows.** Tomorrow — a lot more. The robot doesn't need you.
20. **Submit:** screenshot **Insights → Network** (the two-way loop) **and** the `data` branch's commit list (the robot's work). Read-out: one sentence each — what does your API hide, and what surprised you in the live data?

---

## Good Advice

- **`python` not found (Windows)?** Try `py` instead: `py src/isone.py`, `py -m pip install -r requirements.txt`. Still stuck after 5 minutes? **Switch to Codespaces** and keep going — don't burn the lab on setup.
- **Notebook asks for a kernel or says `ipykernel` is missing?** Run `pip install -r requirements.txt` in the VS Code terminal, then **Select Kernel** again.
- **Your PR shows a red ✗?** Click **Details** → scroll to the red `FAILED` line. It tells you which check failed and why (e.g., *"temp_f=16.0 but the API says 15 C = 59.0 F"* means you forgot `c_to_f`).
- **Your partner's tests say *skipped*?** That's normal until they merge. Skipped ≠ failed.
- **`NotImplementedError`?** You filled in the TODOs but didn't delete the `raise NotImplementedError` line.
- **Accidentally committed or dragged files onto `main`?** New branch → **"Bring my changes to the new branch"** → yes.
- **Robot run says "No new rows this run"?** That's correct, not broken. The feed hadn't published anything newer yet. It catches up next run.
- **Weather rows look ~20 minutes old?** Normal. The weather service reports every 5 minutes but publishes about 20 minutes late. ISO-NE is 1–4 minutes late.
- **Add your partner as Reviewer on every PR.** No reviewer = no approval = no loop.

---

## Definition of done — what's in the repo at 7:30

- [ ] Repo is **public**; both partners are collaborators; **branch protection** on `main`
- [ ] **2 merged pull requests** (one each), both with a green ✓, branches deleted
- [ ] The **`data` branch** exists with **both** `isone_5min.csv` and `weather_obs.csv`
- [ ] A **network graph** showing the loop going both ways
- [ ] *(optional bonus)* The notebook's solar-gap plot, with one sentence on what it shows

*You didn't just analyze data tonight. You built the thing that collects it.*
