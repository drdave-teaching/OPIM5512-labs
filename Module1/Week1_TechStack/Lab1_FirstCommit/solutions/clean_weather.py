"""Reference solution - Partner A, the weather half.

Instructor copy. Turns the raw METAR observations for one campus airport into a tidy
hourly table.

    python clean_weather.py --campus hartford
"""
import argparse
import pandas as pd

STATIONS = {"hartford": "KBDL", "stamford": "KBDR"}
RAW = ("https://raw.githubusercontent.com/drdave-teaching/OPIM5512-labs/main/"
       "Module1/Week1_TechStack/Lab1_FirstCommit/data")


def clean_weather(campus="hartford"):
    station = STATIONS[campus]
    url = f"{RAW}/{campus}/airport_{station}_hourly_raw.csv"

    # "M" is missing and "T" is a trace of precipitation. Without na_values every
    # numeric column comes back as dtype object and nothing downstream works.
    wx = pd.read_csv(url, na_values=["M", "T"])

    # Observations land at :51 or :52. Floor, do not round - the 6:51 report
    # describes the 6 o'clock hour.
    wx["hour"] = pd.to_datetime(wx["valid"]).dt.floor("h")

    # A few hours carry a second "special" report, so collapse to one row per hour.
    hourly = (wx.groupby("hour", as_index=False)
                .agg(temp_f=("tmpf", "mean"),
                     dewpoint_f=("dwpf", "mean"),
                     humidity_pct=("relh", "mean"),
                     wind_kt=("sknt", "mean"))
                .round(2))
    return hourly


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--campus", default="hartford", choices=list(STATIONS))
    ap.add_argument("--out", default="weather_hourly.csv")
    args = ap.parse_args()

    hourly = clean_weather(args.campus)
    hourly.to_csv(args.out, index=False)

    print(f"{args.campus} ({STATIONS[args.campus]}): {len(hourly)} hours -> {args.out}")
    print(f"  temp range: {hourly.temp_f.min():.0f} - {hourly.temp_f.max():.0f} F")
    print(f"  missing temp: {hourly.temp_f.isna().sum()} hours")
