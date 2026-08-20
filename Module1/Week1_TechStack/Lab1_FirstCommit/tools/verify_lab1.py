"""Run the reference solutions against the committed data and print the numbers
that FACILITATOR.md quotes. Instructor tool.

Run this after refresh_lab1_data.py, and once more the week before class.

    python verify_lab1.py
"""
import pathlib
import sys
import pandas as pd

HERE = pathlib.Path(__file__).resolve().parent.parent
DATA = HERE / "data"
sys.path.insert(0, str(HERE / "solutions"))

import clean_weather as cw          # noqa: E402
import clean_demand as cd           # noqa: E402

FAILURES = []


def check(label, ok, detail=""):
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}" + (f"  {detail}" if detail else ""))
    if not ok:
        FAILURES.append(label)


demand = cd.clean_demand((DATA / "isone_demand_hourly_raw.csv").as_uri())
print(f"\ndemand: {len(demand)} hours, "
      f"{demand.load_mw.min():,.0f} - {demand.load_mw.max():,.0f} MW")
check("demand row count is a whole number of days", len(demand) % 24 == 0, f"{len(demand)}")
check("demand hours are unique and gapless",
      demand.hour.is_monotonic_increasing and demand.hour.diff().dropna().nunique() == 1)
check("load is plausible for New England", 8000 < demand.load_mw.min() and demand.load_mw.max() < 29000)

for campus in ("hartford", "stamford"):
    station = cw.STATIONS[campus]
    url = (DATA / campus / f"airport_{station}_hourly_raw.csv").as_uri()
    wx = pd.read_csv(url, na_values=["M", "T"])
    wx["hour"] = pd.to_datetime(wx["valid"]).dt.floor("h")
    hourly = (wx.groupby("hour", as_index=False)
                .agg(temp_f=("tmpf", "mean"), dewpoint_f=("dwpf", "mean"),
                     humidity_pct=("relh", "mean"), wind_kt=("sknt", "mean")))

    print(f"\n{campus} ({station}): {len(hourly)} hours, "
          f"{hourly.temp_f.min():.0f} - {hourly.temp_f.max():.0f} F, "
          f"{hourly.temp_f.isna().sum()} missing temps")

    df = demand.merge(hourly, on="hour", how="inner")
    corr = df.temp_f.corr(df.load_mw)
    by_hour = df.assign(h=df.hour.dt.hour).groupby("h").load_mw.mean()
    hot = df.loc[df.temp_f.idxmax()]
    peak = df.loc[df.load_mw.idxmax()]

    check(f"{campus}: join covers >=98% of demand hours",
          len(df) >= 0.98 * len(demand), f"{len(df)}/{len(demand)}")
    check(f"{campus}: temp/load correlation is positive and material",
          corr > 0.3, f"r={corr:.3f}")
    check(f"{campus}: evening peak beats overnight trough",
          by_hour.idxmax() >= 16 and by_hour.idxmin() <= 6,
          f"peak hour {by_hour.idxmax()}:00, trough {by_hour.idxmin()}:00")

    # The teaching punchline. If this ever stops being true, the lab needs a new hook.
    check(f"{campus}: PUNCHLINE - hottest hour is not the peak-demand hour",
          hot.hour != peak.hour,
          f"hottest {hot.hour:%b %d %H:00} {hot.temp_f:.0f}F | "
          f"peak {peak.hour:%b %d %H:00} {peak.load_mw:,.0f} MW at {peak.temp_f:.0f}F")

print("\n" + ("ALL CHECKS PASSED" if not FAILURES
              else f"{len(FAILURES)} FAILED: " + "; ".join(FAILURES)))
sys.exit(1 if FAILURES else 0)
