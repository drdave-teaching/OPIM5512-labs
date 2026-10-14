# Memo: Regex model vs Gemini model for used-car pricing

**To:** Pricing team · **From:** Dave Wanik · **Date:** October 14, 2026<br>
**Data:** 467 Hartford-area Craigslist listings, Sep 28 to Oct 14 (461 after removing junk prices and placeholder mileage)

## Bottom line
The model built on Gemini's features is **about $150 more accurate per car** than the regex model, and the result is
not luck: it won **21 of 25** paired cross-validation folds (95% interval for the gain: **$66 to $234**). **Recommend
shipping the Gemini model.** The extra cost is about $2 per 1,000 listings.

## Results

| Test | Regex model (4 fields) | Gemini model (14 fields) | Difference |
|---|---|---|---|
| Newest cars (Oct 8 to 14, 87 cars), MAE | $2,394 | $2,246 | Gemini better by $148 (6%) |
| 25 paired folds, all cars, average MAE | $3,074 | $2,923 | Gemini better by $150, wins 21 of 25 |
| Older cars only (training window), CV MAE | $3,217 | $3,253 | Tie |

Both champions are random forests, tuned with the same grids, seed and data. Guessing the median price misses by $3,812.

## Why the Gemini model wins
- **All of the gain comes from the 10 new fields, not from better reading.** Gemini's version of the same four fields
  scored *worse* than regex ($3,174 vs $3,074): its longer model names ("f-150 supercrew", "ram 1500") split cars into
  rarer groups.
- **What the model uses:** mileage, year and make still lead. Among the new fields, **drivetrain, body type, city and
  condition** matter. Transmission, leather seats and title status add almost nothing yet.
- **The patterns make sense:** with everything else held the same, trucks price about $1,250 above sedans, and
  front-wheel drive about $1,300 below four-wheel and rear-wheel drive.

## Would more data help?
Yes, for both models. Retrained on 92 to 368 cars, both error curves are still falling. The Gemini model is ahead at
every size, by roughly $170 to $250 once there are 200 or more cars. More data mainly helps rare categories: with only
15 rebuilt titles, the model cannot yet learn the discount a rebuilt title should carry.

## Cost
| | Regex | Gemini |
|---|---|---|
| Per 1,000 listings | essentially $0 | about $2 |
| Time per listing | milliseconds | about 5 seconds |
| One-time re-read of all 467 old listings | none | about $1, 16 minutes |

## Recommendation and next steps
1. **Ship the Gemini model** to production (`predict-shap` reads its features from the model card; no code changes).
2. **Re-run this comparison at about 1,000 listings** to confirm the gap holds as both models improve.
3. **Clean Gemini's model names** (for example, "f-150 supercrew" to "f-150") to recover the reading loss above.
4. **Watch rebuilt and salvage titles** as they accumulate; that discount should become learnable.
