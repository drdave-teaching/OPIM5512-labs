# -*- coding: utf-8 -*-
"""Builds notebooks/Lab3_Watch_Your_Live_Data.ipynb (run from the repo root)."""
import nbformat as nbf

nb = nbf.v4.new_notebook()
cells = []


def md(text):
    cells.append(nbf.v4.new_markdown_cell(text))


def code(text):
    cells.append(nbf.v4.new_code_cell(text))


md("""# Lab 3 - Watch your live data

Your robot (`.github/workflows/collect.yml`) runs every 5 minutes and writes to the **`data` branch** of your repo.
This notebook reads straight from that branch - so **re-run it later and there's more data**.

**In VS Code:** pick a kernel (top right -> **Select Kernel** -> your Python), set the two names below
to **YOUR** repo, then **Run All**.""")

code("""OWNER = "your-github-username"          # <- the account that owns the repo
REPO = "opim5512-lab3-netidA-netidB"     # <- your repo's name

BASE = f"https://raw.githubusercontent.com/{OWNER}/{REPO}/data/"
print(BASE)""")

code("""import pandas as pd
import matplotlib.pyplot as plt

load = pd.read_csv(BASE + "isone_5min.csv", parse_dates=["timestamp"])
weather = pd.read_csv(BASE + "weather_obs.csv", parse_dates=["timestamp"])

print("energy rows: ", len(load), " from", load["timestamp"].min(), "to", load["timestamp"].max())
print("weather rows:", len(weather), " from", weather["timestamp"].min(), "to", weather["timestamp"].max())""")

md("""## 1. How fresh is it?
The feeds publish every 5 minutes - but *publishing* and *arriving* aren't the same thing.
How old is the newest row of each?""")

code("""now = pd.Timestamp.now(tz="America/New_York").tz_localize(None)
energy_age = now - load["timestamp"].max()
weather_age = now - weather["timestamp"].max()
print("newest energy row is ", energy_age)
print("newest weather row is", weather_age)""")

md("""## 2. The hidden demand: rooftop solar
ISO-NE reports two loads. **Total Load** is what the grid actually delivered.
**Total Load With Estimated Solar** adds back the power rooftop panels made *behind the meter*.
The gap between them is solar the grid never sees.""")

code("""recent = load[load["timestamp"] >= load["timestamp"].max() - pd.Timedelta(hours=48)]

fig, ax = plt.subplots(figsize=(11, 4))
ax.plot(recent["timestamp"], recent["total_load_with_solar_mw"], label="with estimated solar (real demand)")
ax.plot(recent["timestamp"], recent["total_load_mw"], label="total load (what the grid delivered)")
ax.fill_between(recent["timestamp"], recent["total_load_mw"], recent["total_load_with_solar_mw"], alpha=0.25, label="rooftop solar")
ax.set_ylabel("MW")
ax.set_title("New England load, last 48 hours (5-minute data)")
ax.legend()
plt.show()""")

md("""**Look:** when is the gap biggest? What does a cloudy afternoon do to it?""")

md("""## 3. The weather at your airport""")

code("""recent_wx = weather[weather["timestamp"] >= weather["timestamp"].max() - pd.Timedelta(hours=48)]

fig, ax = plt.subplots(figsize=(11, 3))
ax.plot(recent_wx["timestamp"], recent_wx["temp_f"], label="temperature")
ax.plot(recent_wx["timestamp"], recent_wx["dewpoint_f"], label="dewpoint")
ax.set_ylabel("deg F")
ax.legend()
plt.show()""")

md("""## 4. Join them
Energy and weather don't share exact timestamps. `merge_asof` matches each 5-minute load row
to the most recent weather report at or before it (within 15 minutes).""")

code("""joined = pd.merge_asof(
    load.sort_values("timestamp"),
    weather.sort_values("timestamp"),
    on="timestamp",
    direction="backward",
    tolerance=pd.Timedelta(minutes=15),
)
joined = joined.dropna(subset=["temp_f"])
print(len(joined), "matched rows")

fig, ax = plt.subplots(figsize=(6, 5))
ax.scatter(joined["temp_f"], joined["total_load_with_solar_mw"], s=8, alpha=0.5)
ax.set_xlabel("temperature (F)")
ax.set_ylabel("load with solar (MW)")
plt.show()""")

md("""**Come back tomorrow and re-run this notebook.** The robot kept working while you slept.""")

nb["cells"] = cells
nb["metadata"]["kernelspec"] = {"name": "python3", "display_name": "Python 3"}
nbf.write(nb, "notebooks/Lab3_Watch_Your_Live_Data.ipynb")
print("wrote notebooks/Lab3_Watch_Your_Live_Data.ipynb")
