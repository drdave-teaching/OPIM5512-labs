# The lecture — SHAP in plain English

*Read this before the hands-on, or follow along while Dave walks it. ~10 minutes.*

---

## 1. A good score is not the finish line

In Lab 1 you built the data. In Module 2 you trained models and tuned them. Say you land a random
forest that predicts New England electricity demand and it scores **R² ≈ 0.90** — nine-tenths of the
hour-to-hour swing explained. Nice. Now the grid operator asks the only question that matters in the room:

> *"Okay — but **why** does it say 23,000 MW at 6 PM tomorrow?"*

"The forest said so" is not an answer. A model you can't explain is a model nobody will act on. That's
what tonight is about: making the model **show its work**.

## 2. The one idea: give every feature a number, in the units you care about

**SHAP** (SHapley Additive exPlanations) takes a single prediction and splits it into one number per
feature. Each number says how many **megawatts** that feature pushed *this* prediction **up (+)** or
**down (−)**, compared to the model's **average** prediction.

Start from the average prediction (SHAP calls it the *base value*). Add up every feature's push and you
land **exactly** on the model's answer for that row:

```
average prediction  +  (all the feature pushes)  =  this row's prediction
   14,952 MW         +      + 8,130 MW            =    23,082 MW
```

That "adds up exactly" property is the whole point — it's **additive and honest**. No feature's
contribution is hand-waved; the pushes always reconcile to the real number. (That's the "Additive" in the
name, and it comes from a fair-division idea in game theory — every "player" gets credit for exactly what
it contributed.)

## 3. Two zoom levels: local and global

**Local — one prediction, one story.** Pick a single hour. The **waterfall plot** stacks that hour's
pushes: start at the average, `hour_of_day = 18` adds +3,000 MW, `dewpoint_f = 73` adds +2,350, and so on
until you reach the actual prediction. *This* is the answer you hand a stakeholder: "demand is high this
hour **because** it's 6 PM, it's muggy, and it's hot."

**Global — every prediction at once.** Now stack the local explanations for **all** the rows. The
**beeswarm plot** shows, for each feature, a dot per row: position left/right = the push in MW, color =
whether the feature's value was high or low. Read it top to bottom and you see which features the model
leans on overall — and *in which direction*. (For our model: `hour_of_day`, `dewpoint_f`, and `temp_f`
do the heavy lifting; high values push demand up.)

> **Global tells you what the model relies on. Local tells you the story of one decision.**
> Tonight, one partner builds each — then you merge them into one report.

## 4. The three plots you'll meet tonight

| plot | scope | one-line read |
|---|---|---|
| **beeswarm** (`shap.plots.beeswarm`) | global | features ranked by impact; color = feature value |
| **waterfall** (`shap.plots.waterfall`) | local | average → this prediction, one bar per feature |
| **dependence scatter** (`shap.plots.scatter`, *optional joint*) | global | how one feature's push changes across its range |

## 5. The three lines of code behind all of it

You do **not** write these tonight (the setup cell runs them for you) — but this is the whole engine:

```python
import shap
explainer   = shap.TreeExplainer(model)   # reads the trained forest
shap_values = explainer(X)                 # one push per feature, per row
```

`shap_values` is now a table the same shape as your data (743 rows × 6 features), where every cell is a
**push in MW**. Every plot tonight is just a different view of that one table:

- **beeswarm** → `shap.plots.beeswarm(shap_values)`  *(Partner A's one line)*
- **waterfall** → `shap.plots.waterfall(shap_values[i])`  *(Partner B's one line, for row `i`)*

That's it. The model already exists; SHAP just makes it talk.

---

### The five-sentence version (if you remember nothing else)

1. A good model isn't the finish line — you have to be able to say **how it decided**.
2. **SHAP** gives every feature, for every prediction, a number: **MW pushed up (+) or down (−)** from the average.
3. Add a row's pushes to the average and you get that exact prediction — **additive and honest**.
4. **Global** (beeswarm) = which features matter overall, and in which direction.
5. **Local** (waterfall) = one row, one prediction, one story — the answer you give a stakeholder.
