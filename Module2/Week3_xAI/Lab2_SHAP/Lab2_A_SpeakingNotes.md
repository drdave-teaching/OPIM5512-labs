# Lab 2A — instructor speaking notes (global SHAP)

*Talk-to-it notes that follow the Partner A notebook cell by cell. Say the bold lines; the sub-bullets are the depth for curious students.*

---

## Setup cell — the model + the (time-series) split
- **"We reuse the Lab 1 energy data — one row per hour — and fit a random forest to predict New England demand."**
- **"Notice the split: `shuffle=False`. This is a time series, so we do NOT shuffle — the test set is the most recent 20% of hours. Shuffling would let the model peek at the future."**
  - R² lands around **0.83**, not 0.90 — a chronological split is a *tougher, more honest* test than a shuffled one. That drop is a feature, not a bug (and it's the door into Module 4, time series).

## SHAP setup — `explainer` vs `shap_values` (a "noun vs verb" beat)
- **"`explainer` is the *tool* — print it and you just get `<...TreeExplainer at 0x...>`, no results. It knows *how* to explain but hasn't yet."**
- **"`shap_values = explainer(Xte)` is us *running* it on the held-out hours — now we have the numbers."** Same as `model` vs `model.predict(X)`.
- **We explain `Xte` (the test set), not all the data** — you explain the model on data it has never seen. Shape is `(149, 6)` = test hours × features.
- The result is an **Explanation object** with two attributes that matter:
  - **`.base_values`** = the **average prediction** (~**14,900 MW**), one number repeated per row.
  - **`.values`** = the SHAP contributions, `(149 × 6)` — six numbers per hour, each a push in **MW**.
  - Also `.data` = the feature values. The honest identity: **base + a row's 6 pushes = that row's prediction, exactly.**
- If a student asks "is that mean just `y.mean()`?": **no — it's the mean of the model's *predictions*** (path-dependent, over the training coverage ≈ `model.predict(Xtr).mean()`). For a good RF it's *close* to `y_train.mean()`, but conceptually it's average *prediction*, not average actual.

## Built-in importances — say what it ISN'T
- **"This bar chart is the random forest's *built-in* importance — impurity (Gini) importance. Two tells: it sums to 1.0, and it's magnitude-only, no direction."**
  - It's computed from the *training* tree structure and is biased toward high-cardinality/continuous features. Fast, but shallow — "which features it split on a lot," not "how much they move real predictions."
- **Three kinds of importance worth contrasting** (students love this):
  1. **RF impurity** (`model.feature_importances_`) — training structure, biased, sums to 1, no direction.
  2. **Permutation importance** (`sklearn.inspection.permutation_importance`, on the test set) — shuffle one feature, measure how much the score drops. Model-agnostic; measures *real predictive reliance* on held-out data. (The one to prefer over RF's.)
  3. **SHAP** `mean|SHAP|` (`np.abs(shap_values.values).mean(0)`) — average push per feature, in **MW**, and the beeswarm adds **direction**.
  - They often rank alike — but not always, and *that's* the lesson.

## The beeswarm — how to read it out loud
- **"Each dot is one test hour. Color = the feature's value (red high, blue low). Left of center = it pushed demand *down*; right = *up*."**
- Worked example to say: **`weekend` — the red dots (weekend = 1) sit on the LEFT, so weekends lower predicted demand"** (less commercial/industrial load). Red-on-the-left = "high values lower the prediction."
- Workflow note for students: **view it first, then save it** — run `shap.plots.beeswarm(shap_values)` to look, then a second call with `show=False` + `savefig`.

## "Under the hood" knobs (for the curious)
- **`feature_perturbation`**: `tree_path_dependent` (default, no background) vs `interventional` (needs `data=background`). The background is a *choice* and it sets the base value. ⚠️ shap's `Independent` masker caps the background at **100 rows** by default.
- Other explainers: `Exact`, `Permutation`, `Kernel` (model-agnostic, slower). `explainer.shap_interaction_values(X)` gives feature×feature interactions. `check_additivity`, `approximate=` are tuning flags. Beeswarm options: `max_display`, `order`, `color`.
- And the model's own hyperparameters change *what* gets explained — SHAP explains whatever model you hand it.

## Partial dependence (a global view, from the same table)
- **"SHAP gives you a partial-dependence view too, and you don't need sklearn for the basic one."**
  - **`shap.plots.scatter(shap_values[:, "temp_f"], color=shap_values)`** — the SHAP *dependence scatter*: x = feature value, y = SHAP push; color auto-picks the strongest interacting feature (vertical spread = interactions).
  - **`shap.partial_dependence_plot("temp_f", model.predict, X, ...)`** — the *actual* PDP curve.
  - **How to say the difference:** a PDP *averages the model's predictions* as you slide one feature across its range; the SHAP scatter shows the same shape but keeps every hour as a dot and centers it on the contribution — so you also catch when the effect is inconsistent (interactions).
  - Reach for **sklearn** (`PartialDependenceDisplay`) only for **ICE curves** or **2-D interaction PDPs**.

## Optional extensions (if there's time)
- **Remake the beeswarm as a boxplot and a violin** from `shap_values.values` — `pd.DataFrame(shap_values.values, columns=FEATURES).plot.box(vert=False)`; `shap.plots.violin(shap_values)` / `summary_plot(..., plot_type="layered_violin")`. Ask: what does each view show that the others hide? (box/violin = shape/spread; beeswarm = direction via color.)
- **`temp_f` as a SHAP scatter vs a real PDP** — where do they agree/differ, and why?

## The report + the merge-conflict beat
- The report is soft-coded: it embeds the plots by **relative path**, so it displays whatever PNGs get pushed — and only fully renders once **both** partners merge.
- **The `Authors:` line is a deliberate, isolated merge conflict:** both partners edit that one line with their name → the second PR conflicts *only there* → resolve by keeping both names. Everything else lives in separate sections, so it merges cleanly. One merge shows both lessons: *most of a shared file merges itself; the line you both touched makes you decide.*

---
*Companion to `SHAP_LECTURE.md` and the run-of-show deck. Partner B mirrors this on the local/waterfall side.*
