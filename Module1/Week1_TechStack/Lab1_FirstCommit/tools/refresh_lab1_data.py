"""Re-pull the Lab 1 datasets. Instructor tool.

Run this in late August so the "last month" framing stays true, then re-run
verify_lab1.py to confirm the punchline still holds.

    python refresh_lab1_data.py                    # last full 31 days
    python refresh_lab1_data.py --start 20260720 --end 20260819

What it pulls
-------------
demand   ISO-NE hourly system demand, one request for the whole range.
         The report page must be hit first in the same Session to pick up an
         isox_token cookie. No account needed.
         The working report page is  .../-/tree/dmnd-five-minute-sys
         The old  .../-/tree/five-minute-system-load  now returns 500.

weather  IEM ASOS archive, report_type=3 (routine hourly METAR).
         Rate limits hard on rapid repeat requests - the sleep is deliberate.
"""
import argparse
import datetime as dt
import io
import pathlib
import time
import requests
import pandas as pd

HERE = pathlib.Path(__file__).resolve().parent.parent
DATA = HERE / "data"
STATIONS = {"hartford": "KBDL", "stamford": "KBDR"}

UA = {"User-Agent": ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                     "(KHTML, like Gecko) Chrome/128.0 Safari/537.36")}
ISONE_REPORT = ("https://www.iso-ne.com/isoexpress/web/reports/load-and-demand/"
                "-/tree/dmnd-five-minute-sys")


def pull_demand(start, end):
    s = requests.Session()
    s.headers.update(UA)
    s.get(ISONE_REPORT, timeout=45)          # sets isox_token
    if "isox_token" not in s.cookies:
        raise RuntimeError("no isox_token cookie - the report page URL has probably moved")

    r = s.get(f"https://www.iso-ne.com/transform/csv/hourlysystemdemand?start={start}&end={end}",
              timeout=180, headers={"Referer": ISONE_REPORT})
    r.raise_for_status()

    n = sum(1 for line in r.text.splitlines() if line.startswith('"D"'))
    if n == 0:
        raise RuntimeError(f"200 OK but zero data rows - check the date range ({start}-{end})")

    out = DATA / "isone_demand_hourly_raw.csv"
    out.write_text(r.text, encoding="utf-8")
    print(f"demand: {n} hourly rows -> {out.relative_to(HERE)}")
    return n


def pull_weather(campus, station, start, end):
    s, e = dt.datetime.strptime(start, "%Y%m%d"), dt.datetime.strptime(end, "%Y%m%d")
    e = e + dt.timedelta(days=1)             # IEM end date is exclusive
    url = ("https://mesonet.agron.iastate.edu/cgi-bin/request/asos.py?"
           f"station={station}&data=tmpf&data=dwpf&data=relh&data=sknt&data=drct"
           "&data=p01i&data=vsby&data=skyc1"
           f"&year1={s.year}&month1={s.month}&day1={s.day}"
           f"&year2={e.year}&month2={e.month}&day2={e.day}"
           "&tz=America%2FNew_York&format=onlycomma&latlon=no&elev=no"
           "&missing=M&trace=T&direct=no&report_type=3")

    for attempt in range(4):
        r = requests.get(url, headers=UA, timeout=600)
        if r.status_code == 200 and len(r.text) > 1000:
            df = pd.read_csv(io.StringIO(r.text))
            d = DATA / campus
            d.mkdir(parents=True, exist_ok=True)
            out = d / f"airport_{station}_hourly_raw.csv"
            df.to_csv(out, index=False)
            print(f"{campus} ({station}): {len(df)} obs -> {out.relative_to(HERE)}")
            return len(df)
        print(f"  {station} attempt {attempt + 1}: status={r.status_code} len={len(r.text)}")
        time.sleep(30)
    raise RuntimeError(f"IEM would not serve {station} - try again later")


if __name__ == "__main__":
    today = dt.date.today()
    ap = argparse.ArgumentParser()
    ap.add_argument("--start", default=(today - dt.timedelta(days=31)).strftime("%Y%m%d"))
    ap.add_argument("--end", default=(today - dt.timedelta(days=1)).strftime("%Y%m%d"))
    args = ap.parse_args()

    print(f"window: {args.start} -> {args.end}\n")
    pull_demand(args.start, args.end)
    for campus, station in STATIONS.items():
        pull_weather(campus, station, args.start, args.end)
        time.sleep(20)

    print("\nDone. Now run tools/verify_lab1.py and update the numbers in FACILITATOR.md.")
