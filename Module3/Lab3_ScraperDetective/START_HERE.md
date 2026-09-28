# Lab 3 — Scraper Detective · **START HERE**

**Solo · about 2 hours · Colab · your own Google Cloud bucket.** Your Craigslist robot has been scraping cars
every hour. Tonight you check its work: **search** your data, open the **real ads** side by side, **grade** what the
regex extractor got right, then **fix the worst field with one regular expression.**

| | What | Link |
|---|---|---|
| 🕵️ | **The lab notebook** (open in Colab, run top to bottom) | [Lab3_Scraper_Detective.ipynb](https://colab.research.google.com/github/drdave-teaching/OPIM5512-notebooks/blob/main/Module3/Lab3_Scraper_Detective.ipynb) |
| ☁️ | **Final GCP Guide F26** (if your pipeline is not running yet) | [FINAL_GCP_Guide_F26.ipynb](https://colab.research.google.com/github/drdave-teaching/OPIM5512-notebooks/blob/main/Module3/FINAL_GCP_Guide_F26.ipynb) |
| 🗺️ | **Your BASE_SITE link** (your area on Craigslist) | HuskyCT → Module 3 → Week 3.1 → *Your BASE_SITE link* |
| 🎞️ | **Run-of-show slides** (tonight's plan + regex in 5 minutes) | [OPIM5512_Lab3_Detective_Deck.pdf](handouts/OPIM5512_Lab3_Detective_Deck.pdf) |
| 🔤 | **The regex you are grading** | [`extractor-per-listing/main.py`](https://github.com/drdave-teaching/myscrapers/blob/main/cloud_function/extractor-per-listing/main.py) |

## Before class (10 minutes, please)

- [ ] **5 green checks** in your fork's **Actions** tab (Final GCP Guide F26, Steps 0 to 10)
- [ ] In **Cloud Scheduler**, Force run the **scraper**, then the **extractor**, then **materialize-master** (one at a time)
- [ ] Your bucket has `scrapes/` and `structured/datasets/listings_master.csv`
- [ ] Bonus: let it run a few hours before class, so you have 20 to 30 cars instead of 10

Not there yet? That is Part 1 of the lab: we finish it together, and Claude helps you debug.

## Tonight in 5 parts

| Part | Time | You do |
|---|---|---|
| 1. Get it running | 30 min | Finish the guide: 5 green checks and one scrape |
| 2. Search and see | 25 min | Load your bucket into Colab, search your cars, open 3 live ads next to their raw text |
| 3. Grade the robot | 30 min | A truth table for 5 cars; accuracy for price, year, make, model, mileage |
| 4. Fix it with regex | 30 min | **One line:** a better make/model regex. Re-grade: before vs after |
| 5. Wrap up | 5 min | Three short answers; save and submit your notebook |

**Submit:** HuskyCT → *Submit Lab 3* (upload your `.ipynb`), due **Thu Oct 8, 11:59 PM** (Hartford and Stamford).

**The one thing you write:** `BETTER_MAKE_MODEL_RE = re.compile(r"...", re.MULTILINE)`.
Everything else is already in the notebook. We build it together live, and regex101.com (Python flavor) is great for testing.

## Want more? (stretch, and a preview of A06)

Put your regex into your fork's `cloud_function/extractor-per-listing/main.py` on a **`dev-regex` branch** and open a
pull request. Pushing to a branch deploys **nothing** (GitHub only deploys `main`, and Google only trusts `main`).
When you **merge to main**, GitHub redeploys your extractor automatically: that is CI/CD. Keep your own analysis in
separate files (notebooks) so **Sync fork** keeps working when Dr. Wanik updates the course code.

## Stuck?

Ask Claude: paste the cell, the **full** error, and what you expected. Most problems are one of these three:
- **Wrong Google account** in the Colab pop-up: pick the Gmail you used for Google Cloud.
- **`listings_master.csv` not found:** Force run the extractor, then materialize-master, and wait for **Success**.
- **Only 10 cars:** that is one scrape. It adds up to 10 new cars every hour.
