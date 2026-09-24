# -*- coding: utf-8 -*-
"""Rebuild the Lab 2 run-of-show deck (navy/gold), with the prize ladder folded into the lecture.
   HTML -> Chrome --print-to-pdf (vector text). Images extracted from the old deck live in img/."""
import os, subprocess
HERE = os.path.dirname(os.path.abspath(__file__))
CHROME = r"C:/Program Files/Google/Chrome/Application/chrome.exe"
OUT_PDF = r"C:/Users/dww05002/OPIM5512-labs/Module2/Week3_xAI/Lab2_SHAP/handouts/OPIM5512_Lab2_SHAP_RunOfShow_Deck.pdf"

NAVY="#0A1F44"; GOLD="#F2A900"; PURPLE="#7b2fbe"; LAV="#f2effc"; INK="#1c2530"; GREY="#5d6f80"; GREYL="#c8cfda"

CSS = f"""
@page{{ size:13.333in 7.5in; margin:0; }}
*{{ box-sizing:border-box; }}
body{{ margin:0; font-family:'Segoe UI',Arial,Helvetica,sans-serif; color:{INK}; }}
.slide{{ position:relative; width:13.333in; height:7.5in; overflow:hidden; background:#fff; page-break-after:always; }}
.slide:last-child{{ page-break-after:auto; }}
.top{{ background:{NAVY}; border-bottom:6px solid {GOLD}; padding:0.34in 0.7in 0.26in; }}
.kick{{ color:{GOLD}; font-size:13pt; font-weight:800; letter-spacing:.12em; text-transform:uppercase; }}
.h{{ color:#fff; font-size:29pt; font-weight:800; margin-top:6px; line-height:1.1; }}
.body{{ padding:0.42in 0.7in; }}
ul.b{{ margin:0; padding-left:0.3in; }}
ul.b li{{ font-size:16.5pt; line-height:1.5; margin-bottom:0.11in; color:{INK}; }}
ul.b li b{{ color:{NAVY}; }}
.step{{ font-size:16.5pt; line-height:1.5; margin-bottom:0.10in; color:{INK}; }}
.step .n{{ color:{GOLD}; font-weight:800; }}
.callout{{ position:absolute; left:0.7in; right:0.7in; bottom:0.55in; background:{LAV};
           border-radius:8px; padding:0.16in 0.24in; }}
.callout .lead{{ color:{PURPLE}; font-weight:800; font-size:15pt; }}
.callout .rest{{ color:{GREY}; font-size:13.5pt; }}
.eq{{ background:{NAVY}; border-radius:8px; padding:0.26in 0.3in; margin:0.2in 0; text-align:center; }}
.eq .r1{{ color:#fff; font-size:19pt; font-weight:800; }}
.eq .r2{{ color:{GOLD}; font-size:19pt; font-weight:800; margin-top:8px; }}
.mono{{ font-family:Consolas,'Courier New',monospace; color:{PURPLE}; font-size:12.5pt; }}
table.p{{ border-collapse:collapse; font-size:15.5pt; margin:0.14in 0; }}
table.p th,table.p td{{ border:2px solid {GREYL}; padding:7px 15px; text-align:center; }}
table.p th{{ background:{NAVY}; color:#fff; }}
table.p td.win{{ background:{GOLD}; font-weight:800; }}
.pill{{ display:inline-block; background:{GOLD}; color:{NAVY}; font-weight:800; border-radius:9px;
        padding:6px 14px; margin:5px 8px 5px 0; font-size:15pt; }}
.two{{ display:flex; gap:0.4in; align-items:center; }}
.two .im{{ flex:0 0 7.1in; }}
.two .im img{{ width:100%; border:1px solid {GREYL}; border-radius:6px; }}
.two .tx li{{ font-size:15.5pt; line-height:1.45; margin-bottom:0.10in; }}
.foot{{ position:absolute; right:0.55in; bottom:0.24in; color:{GREY}; font-size:10.5pt; }}
.note{{ font-size:15.5pt; line-height:1.5; color:{INK}; margin:0.08in 0; }}
.note b{{ color:{NAVY}; }}
/* title slide */
.title{{ background:{NAVY}; width:13.333in; height:7.5in; position:relative; padding:1.0in 1.0in; }}
.title .eyebrow{{ color:#fff; font-size:16pt; font-weight:800; }}
.title .eyebrow span{{ color:{GOLD}; }}
.title h1{{ color:#fff; font-size:46pt; font-weight:800; margin:0.5in 0 0.22in; line-height:1.06; }}
.title .ul{{ width:2.4in; height:0.09in; background:{PURPLE}; border-radius:3px; margin:0.12in 0 0.3in; }}
.title .subg{{ color:{GOLD}; font-size:24pt; font-weight:800; }}
.title .meta{{ color:#c7d0de; font-size:15pt; margin-top:0.5in; }}
.title .tag{{ color:{GOLD}; font-size:16pt; font-weight:700; margin-top:8px; }}
/* code mock-ups (theory, not screen grabs) */
.cols3{{ display:flex; gap:0.26in; margin-top:0.08in; }}
.col{{ flex:1; background:#f6f8fb; border:1px solid {GREYL}; border-radius:10px; padding:0.14in 0.16in; }}
.col .tool{{ color:{NAVY}; font-weight:800; font-size:12.5pt; letter-spacing:.04em; text-transform:uppercase; }}
.col .q{{ color:{PURPLE}; font-weight:800; font-size:15.5pt; margin:3px 0 2px; }}
.code{{ background:#0f1729; border-radius:8px; padding:0.12in 0.14in; margin:0.09in 0;
        font-family:Consolas,'Courier New',monospace; font-size:11pt; line-height:1.45; color:#e6edf3; white-space:pre; }}
.code .c{{ color:#7d8ba6; }} .code .k{{ color:#7aa2f7; }} .code .fn{{ color:#e0af68; }} .code .s{{ color:#9ece6a; }}
.good{{ color:#1a7f37; font-size:12pt; margin-top:5px; font-weight:600; }}
.blind{{ color:#b04a3a; font-size:12pt; margin-top:2px; }}
.receipt{{ background:#0f1729; border-radius:10px; padding:0.2in 0.34in; margin:0.14in auto;
           font-family:Consolas,'Courier New',monospace; font-size:15.5pt; color:#e6edf3; width:9.3in; }}
.receipt .r{{ display:flex; justify-content:space-between; padding:2.5px 0; }}
.receipt .pos{{ color:#9ece6a; font-weight:700; }} .receipt .neg{{ color:#f7768e; font-weight:700; }}
.receipt .hr{{ border-top:1px dashed #3a4763; margin:7px 0; }}
.receipt .base span, .receipt .final span{{ color:#fff; font-weight:800; }}
.receipt .final .amt{{ color:{GOLD}; }}
.defn{{ display:flex; gap:0.3in; align-items:flex-start; margin-top:0.05in; }}
.defn ol{{ flex:1; margin:0; padding-left:0.28in; }}
.defn li{{ font-size:14.5pt; line-height:1.4; margin-bottom:0.09in; color:{INK}; }}
.defn li b{{ color:{NAVY}; }}
.defn .code{{ flex:0 0 5.55in; font-size:12pt; margin-top:0.04in; }}
"""

def foot(i): return f'<div class="foot">Lab 2 — Explaining a Model &nbsp;·&nbsp; {i}</div>'

def content(kick, h, body, callout=None, idx=0):
    c = ""
    if callout:
        c = f'<div class="callout"><span class="lead">{callout[0]}</span> <span class="rest">{callout[1]}</span></div>'
    return (f'<div class="slide"><div class="top"><div class="kick">{kick}</div><div class="h">{h}</div></div>'
            f'<div class="body">{body}</div>{c}{foot(idx)}</div>')

slides_html = []

# 1 title
slides_html.append(f'''<div class="slide"><div class="title">
<div class="eyebrow">UConn <span>· School of Business</span></div>
<h1>Lab 2 — Explaining a Model</h1><div class="ul"></div>
<div class="subg">SHAP · part lecture, part GitHub</div>
<div class="meta">OPIM 5512 · Module 2 · Explainable AI</div>
<div class="tag">A good score isn't the finish line — tonight the model explains itself.</div>
</div></div>''')

# 2 the deal
slides_html.append(content("WHY WE'RE HERE","The deal",
'''<ul class="b">
<li>You already have a model that predicts New England demand well (<b>R² ≈ 0.90</b>). Tonight you make it say <b>WHY</b>.</li>
<li>One partner builds the <b>GLOBAL</b> view (what drives the model overall), one builds the <b>LOCAL</b> view (why one hour).</li>
<li>Same GitHub loop as Lab 1: branch → commit → push → pull request → review → merge — then merge both views into one report.</li>
<li>First ~15 minutes are lecture (what SHAP is). Then it's hands-on.</li></ul>''',
("Your only code tonight is ONE SHAP line — type it.","You'll approve a partner's explanation of the same model. Approving what you didn't read is how review dies."),2))

# 3 prize 2-player (NEW)
slides_html.append(content("LECTURE · 1 of 8","Why it's fair: split a prize 🏆",
f'''<div class="note">Before the model: you + a friend win a <b>$10,000</b> Kaggle prize. A time machine lets each of you redo it <b>alone</b> — you place 2nd ($7,500), your friend 3rd ($5,000), nobody → $0.</div>
<table class="p"><tr><th>team</th><th>{{ }}</th><th>{{You}}</th><th>{{Friend}}</th><th>{{You, Friend}}</th></tr>
<tr><td>prize</td><td>$0</td><td>$7,500</td><td>$5,000</td><td class="win">$10,000</td></tr></table>
<div class="note"><b>2 players → 2! = 2 orderings → each contribution counts ½</b> (a plain average):</div>
<div class="note">You: +$7,500 and +$5,000 → <b>$6,250</b>. &nbsp; Friend: +$5,000 and +$2,500 → <b>$3,750</b>. &nbsp; Sum = <b>$10,000</b> ✓</div>''',
("Your fair share = your average contribution across the ways the team could form.","This is the Shapley value — a fair split from game theory (Lloyd Shapley, 1953)."),3))

# 4 prize 3-player + fixed weights (NEW)
slides_html.append(content("LECTURE · 2 of 8","Add a player → the weights are FIXED 🔒",
f'''<table class="p" style="font-size:13.5pt"><tr><th>team</th><th>{{ }}</th><th>P1</th><th>P2</th><th>P3</th><th>P1,P2</th><th>P1,P3</th><th>P2,P3</th><th>all</th></tr>
<tr><td>prize</td><td>$0</td><td>$5,000</td><td>$5,000</td><td>$0</td><td>$7,500</td><td>$7,500</td><td>$5,000</td><td class="win">$10,000</td></tr></table>
<div class="note"><b>3 players → 3! = 6 orderings → weights ⅓, ⅙, ⅙, ⅓.</b> &nbsp; Fair shares: P1 $5,000 · P2 $3,750 · P3 $1,250 → <b>$10,000</b> ✓</div>
<div style="margin:0.16in 0"><span class="pill">2 players → 2! = 2 → ½, ½</span><span class="pill">3 players → 3! = 6 → ⅓, ⅙, ⅙, ⅓</span></div>''',
("The weights are just 1/n! counting — 3 things → 6 ways to form the team → ⅓,⅙,⅙,⅓ for EVERY problem, every dataset.","Only the values (v(S)) change. That's why the weights on your worksheet never move."),4))

# 4a — SO WHAT IS A SHAP VALUE? (NEW, read-this-one definition + code mock-up)
slides_html.append(content("LECTURE · 3 of 8","So what IS a SHAP value?",
'''<div class="defn"><ol>
<li><b>One number per feature, per prediction</b> &mdash; how far that feature pushed <i>this</i> prediction away from the <b>base value</b> (the average prediction). Same units as the target: MW.</li>
<li><b>Signed.</b> + pushes the prediction up; &minus; pulls it down.</li>
<li><b>Adds up exactly.</b> base value + all the SHAP values = the prediction.</li>
<li><b>Fair.</b> It&rsquo;s the feature&rsquo;s <b>average bump</b> across every team of the other features it could join &mdash; the Kaggle-prize split. Features not on the team are filled in from <b>background rows</b>.</li></ol>
<div class="code">sv = explainer(X_test)   <span class="c"># 149 rows x 6 features</span>

sv.values[i, j]      <span class="c"># feature j's push, hour i (MW)</span>
sv.base_values[i]    <span class="c"># the average prediction</span>

<span class="c"># the receipt always balances:</span>
sv.base_values[i] + sv.values[i].<span class="fn">sum</span>()
    == model.<span class="fn">predict</span>(X_test)[i]   <span class="c"># True</span></div>
</div>''',
("A SHAP value = one feature&rsquo;s fair share of one prediction.","Same shape as X: one number per row, per feature."),5))

# 4b — WHAT SHAP IS: the receipt (NEW, code mock-up)
slides_html.append(content("LECTURE · 4 of 8","What SHAP is: a receipt, not a ranking",
'''<div class="note">Permutation importance and partial dependence describe the <b>model</b>. SHAP explains <b>one prediction</b> — an itemized, <b>signed</b> receipt whose line items <b>add up exactly</b> to the answer.</div>
<div class="receipt">
<div class="r base"><span>base value &mdash; the average prediction</span><span>14,952 MW</span></div>
<div class="hr"></div>
<div class="r"><span>hour_of_day = 17&nbsp;&nbsp;(5 PM)</span><span class="pos">+3,000</span></div>
<div class="r"><span>dewpoint_f = 71&nbsp;&nbsp;(humid)</span><span class="pos">+2,300</span></div>
<div class="r"><span>temp_f = 85&nbsp;&nbsp;(hot)</span><span class="pos">+2,200</span></div>
<div class="r"><span>weekend = 0&nbsp;&nbsp;(weekday)</span><span class="pos">+900</span></div>
<div class="r"><span>wind_kt = 12&nbsp;&nbsp;(some cooling)</span><span class="neg">&minus;270</span></div>
<div class="hr"></div>
<div class="r final"><span>this hour&rsquo;s prediction</span><span class="amt">23,082 MW</span></div>
</div>''',
("Every prediction gets its own receipt.","The line items sum to the answer &mdash; the guarantee PI and PDP can&rsquo;t give you."),5))

# 4c — THREE TOOLS (NEW, code mock-ups)
slides_html.append(content("LECTURE · 5 of 8","Three tools, three boss-questions &mdash; use all three",
'''<div class="cols3">
<div class="col"><div class="tool">Permutation importance</div><div class="q">&ldquo;What matters?&rdquo;</div>
<div class="code"><span class="c"># shuffle a column,</span>
<span class="c"># watch R&sup2; drop</span>
<span class="fn">permutation_importance</span>(
    model, X_test, y_test)</div>
<div class="good">&#10003; fast, model-agnostic ranking</div>
<div class="blind">&#10007; global only; correlated<br>&nbsp;&nbsp;&nbsp;features can fool it</div></div>

<div class="col"><div class="tool">Partial dependence</div><div class="q">&ldquo;How does it behave?&rdquo;</div>
<div class="code"><span class="c"># sweep one feature,</span>
<span class="c"># average the response</span>
<span class="fn">PartialDependenceDisplay</span>
 .<span class="fn">from_estimator</span>(model, X,
    [<span class="s">"hour_of_day"</span>])</div>
<div class="good">&#10003; shows the SHAPE (up/down/curvy)</div>
<div class="blind">&#10007; an average &mdash; hides<br>&nbsp;&nbsp;&nbsp;who&rsquo;s different</div></div>

<div class="col"><div class="tool">SHAP</div><div class="q">&ldquo;Why THIS one?&rdquo;</div>
<div class="code">sv = shap.<span class="fn">TreeExplainer</span>(model)(X)
shap.plots.<span class="fn">waterfall</span>(sv[i]) <span class="c"># 1 row</span>
shap.plots.<span class="fn">beeswarm</span>(sv)&nbsp;&nbsp;&nbsp;<span class="c"># all</span></div>
<div class="good">&#10003; per-row + signed + adds up;<br>&nbsp;&nbsp;&nbsp;rolls up to global for free</div>
<div class="blind">&#10007; costs more compute</div></div>
</div>''',
("PI ranks. PDP shapes. SHAP itemizes.","Only SHAP explains a SINGLE prediction &mdash; and gives you the global view on the way."),6))

# 5 SHAP in MW (existing lecture 1, now 5 of 7)
slides_html.append(content("LECTURE · 6 of 8","SHAP: give every feature a number — in MW",
f'''<div class="note">The model is that <b>same game</b>: the players are the <b>features</b>, the prize is the <b>prediction</b>.</div>
<div class="note">SHAP splits ONE prediction into one number per feature: how many <b>MW</b> it pushed the answer up (+) or down (−) from the average prediction. Add every push and you land <b>exactly</b> on the answer — additive and honest.</div>
<div class="eq"><div class="r1">average prediction &nbsp;+&nbsp; (all the feature pushes) &nbsp;=&nbsp; this hour's prediction</div>
<div class="r2">14,952 MW &nbsp;+&nbsp; +8,130 MW &nbsp;=&nbsp; 23,082 MW</div></div>
<div class="note">The engine is three lines you DON'T write — the setup cell runs them: <span class="mono">explainer = shap.TreeExplainer(model) · shap_values = explainer(X)</span></div>''',
None,5))

# 6 local waterfall (image)
slides_html.append(f'''<div class="slide"><div class="top"><div class="kick">LECTURE · 7 of 8</div><div class="h">Local: why THIS one prediction (waterfall)</div></div>
<div class="body"><div class="two"><div class="im"><img src="img/waterfall.png"></div>
<div class="tx"><ul class="b">
<li>One hour, one story.</li><li>Start at the average, <b>E[f(X)]</b>.</li>
<li>Each bar is a feature's push in <b>MW</b>.</li><li>Land on this hour's prediction, <b>f(x)</b>.</li>
<li>The peak hour is high <b>because</b> it's 6 PM, muggy, and hot.</li>
<li>This is the answer you give a stakeholder.</li></ul></div></div></div>{foot(6)}</div>''')

# 7 global beeswarm (image)
slides_html.append(f'''<div class="slide"><div class="top"><div class="kick">LECTURE · 8 of 8</div><div class="h">Global: what drives the model overall (beeswarm)</div></div>
<div class="body"><div class="two"><div class="im"><img src="img/beeswarm.png"></div>
<div class="tx"><ul class="b">
<li>Stack every hour's explanation.</li><li>One dot per hour; color = the feature's value (red high, blue low).</li>
<li>Left/right = push in MW.</li><li>Read top to bottom: <b>hour_of_day, dewpoint, temp</b> do the work.</li>
<li>High values (red) push demand <b>up</b>.</li><li>Global = what it leans on. Local = one story.</li></ul></div></div></div>{foot(7)}</div>''')

# 8 stack check
slides_html.append(content("BEFORE THE HANDS-ON","Stack check & roles",
'''<ul class="b">
<li><b>GitHub account</b> + GitHub Desktop installed and signed in</li>
<li><b>Google Colab</b> opens in your browser</li>
<li><b>You did Lab 1</b> — same branch → PR → review → merge loop tonight</li>
<li><b>Pick roles now</b> — Partner A = GLOBAL (beeswarm), Partner B = LOCAL (waterfall)</li>
<li><b>Have the instructions open</b> beside Colab — every click is in there, in order</li></ul>''',
("Odd one out pairs with Dave.","Online / solo? Two accounts, or pair over Teams."),8))

# 9 ACT 1
slides_html.append(content("ACT 1 · SET UP (steps 1–6)","Make the shared repo — from the template",
'''<div class="step"><span class="n">1 ·</span> Pair up — Partner A (global) / Partner B (local)</div>
<div class="step"><span class="n">2 ·</span> Partner A: template repo → Use this template → new PUBLIC repo, owner = you</div>
<div class="step"><span class="n">3 ·</span> Partner A: Settings → Collaborators → add B → <b>B ACCEPTS the invite now</b> (nothing works until B accepts — check spam)</div>
<div class="step"><span class="n">4 ·</span> Partner A: Settings → Rules → ruleset on main: require a PR + 1 approval</div>
<div class="step"><span class="n">5 ·</span> Both: clone the repo ONCE in GitHub Desktop</div>
<div class="step"><span class="n">6 ·</span> Each: New branch (dev-global / dev-local) → Publish branch → <b>Fetch/Pull</b></div>''',
("The template holds the data, both notebooks, images/, README (with the lecture) and REPORT.","You build nothing by hand."),9))

# 10 ACT 2
slides_html.append(content("ACT 2 · EXPLAIN (steps 7–12)","Run it, write one SHAP line, ship it",
'''<div class="step"><span class="n">7 ·</span> Colab → File → Open notebook → GitHub tab → your repo URL → open your notebook</div>
<div class="step"><span class="n">8 ·</span> Runtime → Run all. Setup installs SHAP, fits the model (note R²), builds shap_values + one free plot</div>
<div class="step"><span class="n">9 ·</span> In the TODO cell: A → beeswarm → shap_global.png ; B → waterfall for the peak hour → shap_local.png</div>
<div class="step"><span class="n">10 ·</span> Look at your plot. Run the download cell → two PNGs land in Downloads</div>
<div class="step"><span class="n">11 ·</span> File → Save the notebook → your repo · your dev- branch · same path (plain Save, not Ctrl+S)</div>
<div class="step"><span class="n">12 ·</span> Desktop → Show in Explorer → drag the PNGs into images/ → Commit → Push</div>''',
("One line:","shap.plots.beeswarm(shap_values) &nbsp;/&nbsp; shap.plots.waterfall(shap_values[i])"),10))

# 11 ACT 3
slides_html.append(content("ACT 3 · REVIEW & MERGE (steps 13–16)","The two-way loop",
'''<div class="step"><span class="n">13 ·</span> Compare & pull request → Create → Reviewers → your partner <i>(not listed? the invite wasn't accepted — Act 1, step 3)</i></div>
<div class="step"><span class="n">14 ·</span> Open your PARTNER's PR → Files changed → read their SHAP cell, look at the PNG → Approve</div>
<div class="step"><span class="n">15 ·</span> Merge both PRs → Delete branch</div>
<div class="step"><span class="n">16 ·</span> Both: Desktop → main → Fetch → Pull — four PNGs and both notebooks are now on your laptop</div>''',
("You can't approve your own PR — that's the gate.","Approve only the explanation you actually read. No loop in the network graph? Someone committed to main."),11))

# 12 ACT 4
slides_html.append(content("ACT 4 · REPORT & READ-OUT (optional — steps 17–20)","Do global and local agree?",
'''<div class="step"><span class="n">17 ·</span> One screen: REPORT.md → Edit → one sentence per ➜ line (every number gets a unit)</div>
<div class="step"><span class="n">18 ·</span> Commit to a new branch 'report' → PR → the other partner approves → Merge</div>
<div class="step"><span class="n">19 ·</span> Ahead? Run the joint notebook → shap_dependence.png → images/ → report section 5</div>
<div class="step"><span class="n">20 ·</span> Read-out: beeswarm + waterfall on screen — do they tell the SAME story? Check Insights → Network</div>''',
("Optional bonus — skip tonight if short on time.","The two plots + the branch → PR → review → merge loop are the win; the report is extra."),12))

# 13 good advice
slides_html.append(content("A FEW POINTERS","Good advice",
'''<ul class="b">
<li><b>No module named 'shap'?</b> The setup cell installs it — Runtime → Run all from the top.</li>
<li><b>SHAP plot errors on shap_values?</b> You skipped the setup cell that builds it. Run all from the top.</li>
<li><b>Reviewer / PR / branch not showing?</b> 9 times of 10 the invite wasn't accepted (Act 1). Otherwise GitHub is lagging — wait ~30s and refresh.</li>
<li><b>main rejecting your push is the protection working</b> — switch to your dev- branch.</li>
<li><b>Empty folder after a new branch?</b> Fetch origin → Pull in GitHub Desktop.</li></ul>''',
None,13))

# 14 online/solo
slides_html.append(content("CAN'T MAKE IT TO CAMPUS","Online / solo students",
'''<ul class="b">
<li><b>Pair over Teams if you can</b> — each on your own account, one owns the repo and adds the other.</li>
<li><b>Otherwise, two accounts</b> (needs a second email) — play both A and B, including approving as the other account.</li>
<li><b>Simplest solo</b> — one account with Required approvals = 0: branch → PR → merge yourself.</li>
<li><b>Either way</b> — join the live session on Teams; Friday office hours are highly recommended.</li></ul>''',
None,14))

# 15 definition of done
slides_html.append(content("AT 7:30","Definition of done",
'''<ul class="b" style="list-style:none;padding-left:0">
<li>☐ Both partners are collaborators; branch protection on main</li>
<li>☐ images/ has FOUR PNGs with the exact filenames (two per partner)</li>
<li>☐ Both notebooks saved back with one SHAP line each (beeswarm / waterfall)</li>
<li>☐ ≥2 merged pull requests (one each), branches deleted, both authoring AND reviewing</li>
<li>☐ A network graph showing the loop going both ways</li>
<li>☐ <i>(optional bonus)</i> REPORT.md — one real sentence under each plot, plus one 'what SHAP can't tell us'</li></ul>''',
None,15))

html = "<!doctype html><html><head><meta charset='utf-8'><style>"+CSS+"</style></head><body>"+"".join(slides_html)+"</body></html>"
hp = os.path.join(HERE, "_ros.html")
open(hp, "w", encoding="utf-8").write(html)
subprocess.run([CHROME,"--headless=new","--disable-gpu","--no-pdf-header-footer",
    "--run-all-compositor-stages-before-draw","--virtual-time-budget=20000",
    f"--print-to-pdf={OUT_PDF}","file:///"+hp.replace("\\","/")], capture_output=True)
print(("OK " if os.path.exists(OUT_PDF) else "FAIL ")+OUT_PDF, "|", len(slides_html), "slides")
