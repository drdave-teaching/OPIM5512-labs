"""Reference solution - Partner B, the demand half.

Instructor copy. Turns the raw ISO-NE hourly system demand report into a tidy
hourly table.

    python clean_demand.py
"""
import argparse
import io
import urllib.request
import pandas as pd

RAW = ("https://raw.githubusercontent.com/drdave-teaching/OPIM5512-labs/main/"
       "Module1/Week1_TechStack/Lab1_FirstCommit/data")


def clean_demand(url=f"{RAW}/isone_demand_hourly_raw.csv"):
    text = urllib.request.urlopen(url).read().decode("utf-8")

    # Every line is tagged: "C" comment, "H" header (there are two), "D" data.
    # Filter on the tag rather than skiprows - a new comment line would silently
    # break skiprows, and ISO-NE adds them.
    rows = [line for line in text.splitlines() if line.startswith('"D"')]

    demand = pd.read_csv(io.StringIO("\n".join(rows)), header=None,
                         names=["tag", "date", "hour_ending", "load_mw"])

    # Hour Ending runs 1-24. HE 01 is the hour that ran 00:00 -> 01:00, so the
    # hour it *starts* is HE minus one. Getting this backwards shifts the whole
    # series by an hour and only shows up as a bad correlation later.
    demand["hour"] = (pd.to_datetime(demand["date"])
                      + pd.to_timedelta(demand["hour_ending"].astype(int) - 1, unit="h"))

    return (demand[["hour", "load_mw"]]
            .sort_values("hour")
            .reset_index(drop=True))


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="demand_hourly.csv")
    args = ap.parse_args()

    hourly = clean_demand()
    hourly.to_csv(args.out, index=False)

    print(f"ISO-NE: {len(hourly)} hours -> {args.out}")
    print(f"  load range: {hourly.load_mw.min():,.0f} - {hourly.load_mw.max():,.0f} MW")
    print(f"  mean: {hourly.load_mw.mean():,.0f} MW")
