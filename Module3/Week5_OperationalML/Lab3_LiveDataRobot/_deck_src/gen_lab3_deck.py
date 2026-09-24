# -*- coding: utf-8 -*-
"""Lab 3 run-of-show deck (navy/gold, code mock-ups instead of screen grabs).
HTML -> Chrome --print-to-pdf. The one chart (img/solar_gap.png) is real 5-minute ISO-NE data."""
import os
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
CHROME = r"C:/Program Files/Google/Chrome/Application/chrome.exe"
OUT_PDF = os.path.join(os.path.dirname(HERE), "handouts", "OPIM5512_Lab3_RunOfShow_Deck.pdf")

NAVY = "#0A1F44"
GOLD = "#F2A900"
PURPLE = "#7b2fbe"
LAV = "#f2effc"
INK = "#1c2530"
GREY = "#5d6f80"
GREYL = "#c8cfda"

CSS = f"""
@page{{ size:13.333in 7.5in; margin:0; }}
*{{ box-sizing:border-box; }}
body{{ margin:0; font-family:'Segoe UI',Arial,Helvetica,sans-serif; color:{INK}; }}
.slide{{ position:relative; width:13.333in; height:7.5in; overflow:hidden; background:#fff; page-break-after:always; }}
.slide:last-child{{ page-break-after:auto; }}
.top{{ background:{NAVY}; border-bottom:6px solid {GOLD}; padding:0.34in 0.7in 0.26in; }}
.kick{{ color:{GOLD}; font-size:13pt; font-weight:800; letter-spacing:.12em; text-transform:uppercase; }}
.h{{ color:#fff; font-size:29pt; font-weight:800; margin-top:6px; line-height:1.1; }}
.body{{ padding:0.38in 0.7in; }}
ul.b{{ margin:0; padding-left:0.3in; }}
ul.b li{{ font-size:16.5pt; line-height:1.5; margin-bottom:0.11in; color:{INK}; }}
ul.b li b{{ color:{NAVY}; }}
.step{{ font-size:16pt; line-height:1.45; margin-bottom:0.09in; color:{INK}; }}
.step .n{{ color:{GOLD}; font-weight:800; }}
.callout{{ position:absolute; left:0.7in; right:0.7in; bottom:0.55in; background:{LAV}; border-radius:8px; padding:0.16in 0.24in; }}
.callout .lead{{ color:{PURPLE}; font-weight:800; font-size:15pt; }}
.callout .rest{{ color:{GREY}; font-size:13.5pt; }}
.note{{ font-size:15.5pt; line-height:1.5; color:{INK}; margin:0.06in 0; }}
.note b{{ color:{NAVY}; }}
.foot{{ position:absolute; right:0.55in; bottom:0.24in; color:{GREY}; font-size:10.5pt; }}
.code{{ background:#0f1729; border-radius:8px; padding:0.13in 0.16in; margin:0.08in 0;
        font-family:Consolas,'Courier New',monospace; font-size:12pt; line-height:1.45; color:#e6edf3; white-space:pre; }}
.code .c{{ color:#7d8ba6; }} .code .k{{ color:#7aa2f7; }} .code .fn{{ color:#e0af68; }} .code .s{{ color:#9ece6a; }}
.code .d{{ color:#9ece6a; }} .code .x{{ color:#f7768e; text-decoration:line-through; }}
.cols2{{ display:flex; gap:0.3in; align-items:stretch; }}
.cols2 > div{{ flex:1; }}
.lbl{{ font-weight:800; color:{NAVY}; font-size:13pt; letter-spacing:.04em; text-transform:uppercase; margin-bottom:2px; }}
.lbl.bad{{ color:#b04a3a; }} .lbl.good{{ color:#1a7f37; }}
.arrow{{ flex:0 0 0.5in !important; display:flex; align-items:center; justify-content:center; font-size:34pt; color:{GOLD}; font-weight:800; }}
table.t{{ border-collapse:collapse; font-size:14pt; margin:0.1in 0; width:100%; }}
table.t th, table.t td{{ border:1px solid {GREYL}; padding:6px 12px; text-align:left; }}
table.t th{{ background:{NAVY}; color:#fff; }}
table.t td.ok{{ color:#1a7f37; font-weight:700; }} table.t td.meh{{ color:#b36b00; font-weight:700; }}
.img{{ text-align:center; }}
.img img{{ width:9.2in; border:1px solid {GREYL}; border-radius:6px; }}
.big{{ font-size:40pt; font-weight:800; color:{NAVY}; }}
.pill{{ display:inline-block; background:{GOLD}; color:{NAVY}; font-weight:800; border-radius:9px; padding:6px 14px; margin:4px 8px 4px 0; font-size:14pt; }}
.title{{ background:{NAVY}; width:13.333in; height:7.5in; position:relative; padding:1.0in 1.0in; }}
.title .eyebrow{{ color:#fff; font-size:16pt; font-weight:800; }}
.title .eyebrow span{{ color:{GOLD}; }}
.title h1{{ color:#fff; font-size:46pt; font-weight:800; margin:0.5in 0 0.22in; line-height:1.06; }}
.title .ul{{ width:2.4in; height:0.09in; background:{PURPLE}; border-radius:3px; margin:0.12in 0 0.3in; }}
.title .subg{{ color:{GOLD}; font-size:24pt; font-weight:800; }}
.title .meta{{ color:#c7d0de; font-size:15pt; margin-top:0.5in; }}
.title .tag{{ color:{GOLD}; font-size:16pt; font-weight:700; margin-top:8px; }}
"""


def foot(i):
    return f'<div class="foot">Lab 3 &mdash; Build a Live Data Robot &nbsp;&middot;&nbsp; {i}</div>'


def content(kick, h, body, callout=None, idx=0):
    c = ""
    if callout:
        c = f'<div class="callout"><span class="lead">{callout[0]}</span> <span class="rest">{callout[1]}</span></div>'
    return (f'<div class="slide"><div class="top"><div class="kick">{kick}</div><div class="h">{h}</div></div>'
            f'<div class="body">{body}</div>{c}{foot(idx)}</div>')


slides = []

# 1 title
slides.append('''<div class="slide"><div class="title">
<div class="eyebrow">UConn <span>&middot; School of Business</span></div>
<h1>Lab 3 &mdash; Build a Live Data Robot</h1><div class="ul"></div>
<div class="subg">Two tiny APIs &middot; one robot &middot; all in VS Code</div>
<div class="meta">OPIM 5512 &middot; Module 3 &middot; Operational ML</div>
<div class="tag">Tonight your code stops needing you.</div>
</div></div>''')

# 2 the deal
slides.append(content("WHY WE'RE HERE", "The deal",
'''<ul class="b">
<li>New England's grid publishes electricity demand <b>every 5 minutes</b>. Your campus airport reports the weather <b>every 5 minutes</b> too.</li>
<li>Partner A writes a tiny <b>energy API</b> (ISO-NE). Partner B writes a tiny <b>weather API</b> (National Weather Service).</li>
<li>Same loop as Labs 1&ndash;2: branch &rarr; commit &rarr; push &rarr; pull request &rarr; review &rarr; merge.</li>
<li>Then a <b>robot</b> (GitHub Actions) calls both APIs every 5 minutes and saves every new row &mdash; <b>forever, free, while you sleep.</b></li></ul>''',
("First ~15 minutes: why APIs and robots. Then you build.", "Everything tonight happens in VS Code."), 2))

# 3 an API is a promise
slides.append(content("LECTURE &middot; 1 of 6", "An API is a promise: hide the mess",
'''<div class="cols2">
<div><div class="lbl bad">What ISO-NE actually sends</div><div class="code"><span class="c">"C","Real-Time Five-Minute System Load"</span>
<span class="c">"C","Report generated: 09/24/2026 10:59"</span>
<span class="c">"H","Date/Time","Total Load","Native..."</span>
<span class="c">"H","Date/Time","MW","MW","MW"</span>
<span class="d">"D","09/24/2026 10:50:00",8751.362,...</span>
<span class="d">"D","09/24/2026 10:55:00",8702.394,...</span>
<span class="c">"T","132 lines"</span>
<span class="c"># ...and only if you visited the report page</span>
<span class="c"># first for a cookie + sent it as the Referer</span></div></div>
<div class="arrow">&rarr;</div>
<div><div class="lbl good">What your API returns</div><div class="code">load = <span class="fn">get_five_minute_load</span>()
load.tail(2)

           timestamp  total_load_mw  ...
 2026-09-24 10:50:00        8751.36  ...
 2026-09-24 10:55:00        8702.39  ...</div></div>
</div>''',
("An API is a clean promise about what you get back.", "Nobody downstream should ever have to know about cookies, referers, or row codes."), 3))

# 4 two feeds two messes
slides.append(content("LECTURE &middot; 2 of 6", "Two feeds, two messes, two APIs",
'''<div class="cols2">
<div><div class="lbl">Partner A &mdash; energy &middot; <code>src/isone.py</code></div><div class="code">session = requests.<span class="fn">Session</span>()
<span class="c"># TODO 1: visit the page -> get a cookie</span>
session.<span class="fn">get</span>(REPORT_PAGE, timeout=30)
<span class="c"># TODO 2: ask for the CSV, say where you came from</span>
resp = session.<span class="fn">get</span>(url, headers={<span class="s">"Referer"</span>: REPORT_PAGE})
<span class="c"># TODO 3: keep only the '"D"' data rows</span>
<span class="k">for</span> line <span class="k">in</span> resp.text.<span class="fn">splitlines</span>():
    <span class="k">if</span> line.<span class="fn">startswith</span>(<span class="s">'"D"'</span>):
        data_rows.<span class="fn">append</span>(line)</div></div>
<div><div class="lbl">Partner B &mdash; weather &middot; <code>src/nws.py</code></div><div class="code"><span class="c"># TODO 1: identify yourself, get the JSON</span>
resp = requests.<span class="fn">get</span>(url, headers={
    <span class="s">"User-Agent"</span>: USER_AGENT}, timeout=30)

<span class="c"># TODO 2: metric -> the units we use</span>
<span class="s">"temp_f"</span>:   <span class="fn">c_to_f</span>(p[<span class="s">"temperature"</span>][<span class="s">"value"</span>]),
<span class="s">"wind_mph"</span>: <span class="fn">kmh_to_mph</span>(p[<span class="s">"windSpeed"</span>][<span class="s">"value"</span>]),
<span class="c"># ...dewpoint_f, humidity_pct</span></div></div>
</div>''',
("3 small TODOs for A, 2 for B.", "Then delete the raise NotImplementedError line and run it: real rows from right now."), 4))

# 5 the robot
slides.append(content("LECTURE &middot; 3 of 6", "The robot: GitHub Actions on a schedule",
'''<div class="cols2">
<div><div class="lbl">.github/workflows/collect.yml &nbsp;(given)</div><div class="code">on:
  schedule:
    - cron: <span class="s">"*/5 * * * *"</span>   <span class="c"># every 5 min</span>
  workflow_dispatch:          <span class="c"># + a Run button</span>

steps:
  - <span class="c"># check out the code (main)</span>
  - run: python src/collect.py
  - <span class="c"># commit new rows to the data branch</span></div></div>
<div><div class="lbl">Where things live</div>
<ul class="b" style="margin-top:0.1in">
<li><b>main</b> = the code. Protected. Changes arrive only through a reviewed PR.</li>
<li><b>data</b> = the data. The robot creates it on its first run and is the only one who commits there.</li>
<li>That's why 288 robot commits a day never clutter <b>your</b> network graph.</li></ul></div>
</div>''',
("The cloud runs your code now &mdash; not you.", "Public repos get unlimited free robot minutes. Keep your repo PUBLIC."), 5))

# 6 upsert
slides.append(content("LECTURE &middot; 4 of 6", "Why a late robot is still right",
'''<div class="note">GitHub's "every 5 minutes" is <b>roughly</b> every 5 minutes &mdash; runs start late, and sometimes get skipped when it's busy.
So the robot never asks <i>"what happened in the last 5 minutes?"</i> It pulls <b>the whole recent window</b> every time and <b>upserts</b>:</div>
<table class="t">
<tr><th>robot run</th><th>fetched</th><th>new rows kept</th><th>what happened</th></tr>
<tr><td>11:05 (on time)</td><td>422</td><td class="ok">+1</td><td>one fresh 5-minute row</td></tr>
<tr><td>11:10 &mdash; skipped</td><td>&mdash;</td><td>&mdash;</td><td>GitHub was busy</td></tr>
<tr><td>11:17 (late)</td><td>424</td><td class="ok">+2</td><td>caught up both missing rows</td></tr>
<tr><td>11:18 (ran twice)</td><td>424</td><td class="meh">+0</td><td>"No new rows this run." &mdash; correct</td></tr>
</table>''',
("New rows get added. Rows it has seen get refreshed. Nothing is ever lost or doubled.", "That's how real data pipelines survive an unreliable clock."), 6))

# 7 how live is live
slides.append(content("LECTURE &middot; 5 of 6", "How live is &ldquo;live&rdquo;? We measured it.",
'''<div class="note">Polled every minute for 30 minutes on Sept 24. The question isn't just <i>how often</i> &mdash; it's <i>how late</i> each reading arrives:</div>
<table class="t">
<tr><th>feed</th><th>a reading every&hellip;</th><th>it shows up&hellip;</th><th>so the robot sees new data&hellip;</th></tr>
<tr><td><b>ISO-NE</b> system load</td><td>5 minutes</td><td class="ok">1&ndash;3 minutes late</td><td class="ok">almost every run</td></tr>
<tr><td><b>Weather</b> KBDL / KBDR</td><td>5 minutes (+ the classic :51 hourly report)</td><td class="meh">in batches, 8&ndash;24 minutes late</td><td class="meh">most runs, a few at a time</td></tr>
</table>''',
("Published &ne; arrived.", "Live data always runs a little behind the clock. Your notebook measures exactly how far."), 7))

# 8 solar gap
slides.append(content("LECTURE &middot; 6 of 6", "The payoff: demand the grid never sees",
'''<div class="img"><img src="img/solar_gap.png"></div>''',
("Rooftop solar hides thousands of megawatts at midday.", "ISO-NE reports both loads every 5 minutes. Your notebook plots this gap from YOUR robot's data."), 8))

# 9 stack check
slides.append(content("BEFORE THE HANDS-ON", "Stack check & roles",
'''<ul class="b">
<li><b>GitHub Desktop</b> signed in &middot; <b>VS Code</b> with the <b>Python</b> + <b>Jupyter</b> extensions</li>
<li><b>Pick roles now</b> &mdash; Partner A = <b>energy</b> (<code>src/isone.py</code>), Partner B = <b>weather</b> (<code>src/nws.py</code>)</li>
<li><b>Stamford:</b> Partner B changes the station to <b>KBDR</b> (Sikorsky). The grid is shared; the weather is local.</li>
<li><b>Laptop Python fighting you?</b> Don't lose the lab to setup: <b>Code &rarr; Codespaces &rarr; Create</b> = VS Code in the browser, everything installed.</li></ul>''',
("Odd one out pairs with Dave.", "Online / solo? Be both A and B with two branches, approvals = 0."), 9))

# 10 ACT 1
slides.append(content("ACT 1 &middot; SET UP (steps 1&ndash;6)", "Make the shared repo &mdash; from the template",
'''<div class="step"><span class="n">1 &middot;</span> Pair up &mdash; Partner A (energy) / Partner B (weather)</div>
<div class="step"><span class="n">2 &middot;</span> Partner A: template repo &rarr; Use this template &rarr; new <b>PUBLIC</b> repo, owner = you</div>
<div class="step"><span class="n">3 &middot;</span> Partner A: Settings &rarr; Collaborators &rarr; add B &rarr; <b>B ACCEPTS the invite now</b></div>
<div class="step"><span class="n">4 &middot;</span> Partner A: Settings &rarr; Rules &rarr; ruleset on main: require a PR + 1 approval</div>
<div class="step"><span class="n">5 &middot;</span> Both: clone the repo ONCE in GitHub Desktop</div>
<div class="step"><span class="n">6 &middot;</span> Each: New branch (dev-energy / dev-weather) &rarr; Publish &rarr; Fetch &mdash; <b>before touching any file</b></div>''',
("The template already has the robot, the tests, and the notebook.", "You write the two APIs."), 10))

# 11 ACT 2
slides.append(content("ACT 2 &middot; BUILD YOUR API (steps 7&ndash;12)", "Fill the TODOs, run it, ship it",
'''<div class="step"><span class="n">7 &middot;</span> GitHub Desktop &rarr; Repository &rarr; Open in Visual Studio Code (check: your dev- branch)</div>
<div class="step"><span class="n">8 &middot;</span> Fill the TODOs in <b>your</b> file &rarr; delete the <code>raise NotImplementedError</code> line</div>
<div class="step"><span class="n">9 &middot;</span> Terminal: <code>pip install -r requirements.txt</code> &rarr; <code>python src/isone.py</code> / <code>python src/nws.py</code> &rarr; <b>live rows</b></div>
<div class="step"><span class="n">10 &middot;</span> GitHub Desktop: commit on your dev- branch &rarr; Push</div>
<div class="step"><span class="n">11 &middot;</span> Compare &amp; pull request &rarr; Reviewers &rarr; your partner &rarr; <b>watch the check run</b></div>
<div class="step"><span class="n">12 &middot;</span> Open your PARTNER's PR &rarr; read their function + look for the green &#10003; &rarr; Approve</div>''',
("Green &#10003; = your API passed. Your partner's tests say SKIPPED until they merge.", "Red &#10007;? Click Details &mdash; the FAILED line says what's wrong in plain English."), 11))

# 12 ACT 3
slides.append(content("ACT 3 &middot; MERGE &amp; WAKE THE ROBOT (steps 13&ndash;16)", "Hand your code to the cloud",
'''<div class="step"><span class="n">13 &middot;</span> Merge both PRs &rarr; Delete branch</div>
<div class="step"><span class="n">14 &middot;</span> <b>Actions</b> tab &rarr; <b>collect</b> &rarr; <b>Run workflow</b> (it also runs itself ~every 5 minutes &mdash; this skips the wait)</div>
<div class="step"><span class="n">15 &middot;</span> When it's &#10003;: Code &rarr; switch the branch menu to <b>data</b> &rarr; open both CSVs &mdash; <b>the robot's work</b></div>
<div class="step"><span class="n">16 &middot;</span> Both: GitHub Desktop &rarr; main &rarr; Fetch &rarr; Pull</div>''',
("Every commit on the data branch is by lab3-bot.", "Your main branch stayed clean &mdash; code and data live apart."), 12))

# 13 ACT 4
slides.append(content("ACT 4 &middot; WATCH IT LIVE (steps 17&ndash;20)", "Your data, growing",
'''<div class="step"><span class="n">17 &middot;</span> VS Code &rarr; <code>notebooks/Lab3_Watch_Your_Live_Data.ipynb</code> &rarr; Select Kernel &rarr; set OWNER + REPO &rarr; Run All</div>
<div class="step"><span class="n">18 &middot;</span> The solar-gap plot: when is rooftop solar hiding the most demand?</div>
<div class="step"><span class="n">19 &middot;</span> Wait an hour, Run All again &mdash; more rows. Tomorrow &mdash; a lot more.</div>
<div class="step"><span class="n">20 &middot;</span> Submit: screenshot <b>Insights &rarr; Network</b> + the <b>data</b> branch's commit list</div>''',
("You didn't just analyze data tonight.", "You built the thing that collects it."), 13))

# 14 good advice
slides.append(content("A FEW POINTERS", "Good advice",
'''<ul class="b">
<li><b>NotImplementedError?</b> You filled the TODOs but didn't delete the <code>raise</code> line.</li>
<li><b>Red &#10007; "temp_f=16.0 but the API says 15 C = 59.0 F"?</b> You stored Celsius &mdash; wrap it in <code>c_to_f(...)</code>.</li>
<li><b>Committed on main by accident?</b> New branch &rarr; "Bring my changes to the new branch" &rarr; yes.</li>
<li><b>"No new rows this run"</b> is correct, not broken &mdash; the feed hadn't published anything newer.</li>
<li><b>python not found (Windows)?</b> Use <code>py</code>. Still stuck after 5 minutes? Switch to <b>Codespaces</b>.</li></ul>''',
None, 14))

# 15 definition of done
slides.append(content("AT 7:30", "Definition of done",
'''<ul class="b" style="list-style:none;padding-left:0">
<li>&#9744; Repo is <b>public</b>; both partners are collaborators; branch protection on main</li>
<li>&#9744; <b>2 merged pull requests</b> (one each), both with a green &#10003;, branches deleted</li>
<li>&#9744; The <b>data</b> branch exists with <b>both</b> isone_5min.csv and weather_obs.csv</li>
<li>&#9744; A <b>network graph</b> showing the loop going both ways</li>
<li>&#9744; <i>(optional bonus)</i> the notebook's solar-gap plot + one sentence on what it shows</li></ul>''',
("Leave the robot running.", "Next module, you'll model the data it collects while you were away."), 15))

html = ("<!doctype html><html><head><meta charset='utf-8'><style>" + CSS + "</style></head><body>"
        + "".join(slides) + "</body></html>")
hp = os.path.join(HERE, "_lab3_deck.html")
with open(hp, "w", encoding="utf-8") as f:
    f.write(html)
os.makedirs(os.path.dirname(OUT_PDF), exist_ok=True)
subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
                "--run-all-compositor-stages-before-draw", "--virtual-time-budget=20000",
                "--print-to-pdf=" + OUT_PDF, "file:///" + hp.replace("\\", "/")], capture_output=True)
print(("OK " if os.path.exists(OUT_PDF) else "FAIL ") + OUT_PDF, "|", len(slides), "slides")
