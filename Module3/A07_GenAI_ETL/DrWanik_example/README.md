# Dr. Wanik's A07, start to finish (Oct 14, 2026)

Same steps as the [A07 sheet](../A07_CLOUD_SHELL_COMMANDS.md), done on Dr. Wanik's own fork. Use it as your model.

**The changes (click Files changed):**
- [Part 1: Gemini extracts 10 new fields](https://github.com/drdww/myscrapers-f26-v2/pull/2/files): one file, three edits (schema, rules, `out_record`)
- [Part 2: materialize-llm](https://github.com/drdww/myscrapers-f26-v2/pull/3/files): three new files

**The two master tables it produced (same 467 Hartford cars):**

| File | Columns | Built by |
|---|---|---|
| [DrWanik_listings_master_REGEX_2026-10-14.csv](DrWanik_listings_master_REGEX_2026-10-14.csv) | 9: price, year, make, model, mileage + ids | `materialize-master` from the regex extractor |
| [DrWanik_listings_master_GEMINI_2026-10-14.csv](DrWanik_listings_master_GEMINI_2026-10-14.csv) | 19: the same 9 + trim, body_type, drivetrain, transmission, fuel_type, exterior_color, title_status, condition, leather_seats, city | `materialize-llm` from Gemini |

**The code, as deployed:**
- [extractor_llm_GEMINI_10_fields_main.py](extractor_llm_GEMINI_10_fields_main.py): `cloud_function/extractor-llm-poc/main.py` after Part 1
- [materialize_llm_GEMINI_main.py](materialize_llm_GEMINI_main.py): `cloud_function/materialize-llm/main.py` (Part 2)
- [materialize_master_REGEX_main.py](materialize_master_REGEX_main.py): the regex version it was copied from, for comparison

**What Gemini found in 467 cars:** 43 manual transmissions, 200 four-wheel drive, 15 rebuilt titles, 53 cars with
leather seats, and the town for 358 of them. Re-reading all 153 old batches took 16 minutes with 0 errors.
