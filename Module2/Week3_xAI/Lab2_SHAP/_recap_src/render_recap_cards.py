# -*- coding: utf-8 -*-
"""Rendered code mock-ups for the Lab 2 SHAP recap video — clean cards instead of screen grabs.
Reuses the run-of-show deck's CSS + content() so the video matches the slides (navy/gold)."""
import os
import re
import random
import subprocess

CHROME = r"C:/Program Files/Google/Chrome/Application/chrome.exe"
HERE = os.path.dirname(os.path.abspath(__file__))
DECK = os.path.join(HERE, "..", "_deck_src", "gen_ros_deck.py")

EXTRA_CSS = """
.pillrow{ display:flex; gap:0.28in; justify-content:center; margin-top:0.16in; }
.pill.dim{ background:#e8ecf2; color:#5d6f80; }
.split{ display:flex; gap:0.35in; align-items:center; margin-top:0.12in; }
.split .code{ flex:0 0 6.3in; font-size:13.5pt; }
.hm{ margin:0.12in auto 0; }
.hm .row{ display:flex; align-items:center; height:22px; }
.hm .lab{ width:1.25in; font-family:Consolas,monospace; font-size:11pt; color:#5d6f80; text-align:right; padding-right:10px; }
.hm .lab.hot{ color:#0A1F44; font-weight:800; }
.hm .lab.kpi{ color:#b3261e; font-weight:800; }
.hm .cell{ width:15px; height:18px; margin-right:1px; border-radius:2px; }
.defn{ display:flex; gap:0.3in; align-items:flex-start; margin-top:0.05in; }
.defn ol{ flex:1; margin:0; padding-left:0.28in; }
.defn li{ font-size:14.5pt; line-height:1.4; margin-bottom:0.09in; color:#1c2530; }
.defn li b{ color:#0A1F44; }
.defn .code{ flex:0 0 5.55in; font-size:12pt; margin-top:0.04in; }
"""

DEFINE_BODY = (
    '<div class="defn"><ol>'
    '<li><b>One number per feature, per prediction</b> &mdash; how far that feature pushed <i>this</i> '
    'prediction away from the <b>base value</b> (the average prediction). Same units as the target: MW.</li>'
    '<li><b>Signed.</b> + pushes the prediction up; &minus; pulls it down.</li>'
    '<li><b>Adds up exactly.</b> base value + all the SHAP values = the prediction.</li>'
    '<li><b>Fair.</b> It&rsquo;s the feature&rsquo;s <b>average bump</b> across every team of the other '
    'features it could join &mdash; the Kaggle-prize split. Features not on the team are filled in from '
    '<b>background rows</b>.</li></ol>'
    '<div class="code">sv = explainer(X_test)   <span class="c"># 149 rows x 6 features</span>\n\n'
    'sv.values[i, j]      <span class="c"># feature j\'s push, hour i (MW)</span>\n'
    'sv.base_values[i]    <span class="c"># the average prediction</span>\n\n'
    '<span class="c"># the receipt always balances:</span>\n'
    'sv.base_values[i] + sv.values[i].<span class="fn">sum</span>()\n'
    '    == model.<span class="fn">predict</span>(X_test)[i]   <span class="c"># True</span></div>'
    '</div>'
)


def load_deck():
    src = open(DECK, encoding="utf-8").read().split('html = "<!doctype')[0]
    ns = {"__file__": os.path.abspath(DECK), "__name__": "deck_cards"}
    exec(src, ns)
    return ns


def clean(slide_html, kick):
    s = re.sub(r'<div class="kick">.*?</div>', f'<div class="kick">{kick}</div>', slide_html, count=1)
    s = re.sub(r'<div class="foot">.*?</div>', "", s)
    return s


def render(css, slide_html, out_dir, name):
    page = ("<!doctype html><html><head><meta charset='utf-8'><style>" + css + EXTRA_CSS
            + "</style></head><body>" + slide_html + "</body></html>")
    hp = os.path.join(out_dir, name + ".html")
    open(hp, "w", encoding="utf-8").write(page)
    pp = os.path.join(out_dir, name + ".png")
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
                    "--force-device-scale-factor=1", "--window-size=1280,720",
                    f"--screenshot={pp}", "file:///" + hp.replace("\\", "/")], capture_output=True)
    return pp


def spaghetti_svg():
    random.seed(7)
    w, h = 400, 250
    x0, y0, x1, y1 = 40, 20, 385, 215
    parts = [f'<svg width="{w}" height="{h}" xmlns="http://www.w3.org/2000/svg">',
             f'<line x1="{x0}" y1="{y1}" x2="{x1}" y2="{y1}" stroke="#8a93a3" stroke-width="2"/>',
             f'<line x1="{x0}" y1="{y0}" x2="{x0}" y2="{y1}" stroke="#8a93a3" stroke-width="2"/>',
             f'<text x="{(x0 + x1) / 2}" y="{h - 2}" font-size="14" fill="#5d6f80" text-anchor="middle" font-family="Segoe UI">bedrooms (swept)</text>']
    curves = []
    for k in range(12):
        base = random.uniform(0.15, 0.55)
        slope = random.uniform(0.25, 0.55)
        bend = random.uniform(0.0, 0.25)
        pts = []
        for i in range(11):
            t = i / 10.0
            v = base + slope * t + bend * t * t
            pts.append(v)
        curves.append(pts)
    top = max(max(c) for c in curves)
    for c in curves:
        coords = " ".join(f"{x0 + (x1 - x0) * i / 10:.1f},{y1 - (y1 - y0) * v / top:.1f}" for i, v in enumerate(c))
        parts.append(f'<polyline points="{coords}" fill="none" stroke="#c8cfda" stroke-width="2"/>')
    avg = [sum(c[i] for c in curves) / len(curves) for i in range(11)]
    coords = " ".join(f"{x0 + (x1 - x0) * i / 10:.1f},{y1 - (y1 - y0) * v / top:.1f}" for i, v in enumerate(avg))
    parts.append(f'<polyline points="{coords}" fill="none" stroke="#F2A900" stroke-width="6" stroke-linecap="round"/>')
    parts.append(f'<text x="{x1 - 4}" y="{y0 + 14}" font-size="15" fill="#0A1F44" font-weight="800" text-anchor="end" font-family="Segoe UI">average = the PDP</text>')
    parts.append("</svg>")
    return "".join(parts)


def heatmap_html():
    random.seed(11)
    rows = ["sensor 008", "sensor 023", "sensor 044", "sensor 051", "sensor 087", "sensor 102",
            "sensor 140", "sensor 166", "sensor 213", "sensor 257", "sensor 309"]
    hot = {"sensor 044", "sensor 140", "sensor 257"}
    ncol, w0, w1 = 48, 24, 35
    out = ['<div class="hm">']
    for r in rows:
        cls = "lab hot" if r in hot else "lab"
        cells = []
        for c in range(ncol):
            if r in hot and w0 <= c <= w1:
                a = random.uniform(0.7, 1.0)
                col = f"rgba(179,38,30,{a:.2f})"
            else:
                a = random.uniform(0.04, 0.22) if random.random() < 0.8 else random.uniform(0.25, 0.4)
                col = f"rgba(179,38,30,{a:.2f})"
            cells.append(f'<div class="cell" style="background:{col}"></div>')
        out.append(f'<div class="row"><div class="{cls}">{r}</div>{"".join(cells)}</div>')
    kpi = []
    for c in range(ncol):
        col = "#d64545" if w0 <= c <= w1 + 1 else "#cfe8d4"
        kpi.append(f'<div class="cell" style="background:{col}"></div>')
    out.append(f'<div class="row" style="margin-top:6px"><div class="lab kpi">KPI</div>{"".join(kpi)}</div>')
    out.append('<div class="row"><div class="lab"></div><div style="font-size:11pt;color:#5d6f80;'
               'font-family:Segoe UI">July &rarr; (one column per retrain)</div></div>')
    out.append("</div>")
    return "".join(out)


def build(out_dir):
    os.makedirs(out_dir, exist_ok=True)
    ns = load_deck()
    css, slides, content = ns["CSS"], ns["slides_html"], ns["content"]
    cards = {}

    def by_title(fragment):
        hits = [s for s in slides if fragment in s]
        if len(hits) != 1:
            raise SystemExit(f"expected exactly one deck slide containing {fragment!r}, found {len(hits)}")
        return hits[0]

    # reuse deck slides by title (kicker swapped, footer dropped) — robust to slides being added
    cards["prize"] = render(css, clean(by_title("Why it's fair: split a prize"),
                                       "LAB 2 RECAP &middot; WHY SHAP IS FAIR"), out_dir, "prize")
    cards["receipt"] = render(css, clean(by_title("a receipt, not a ranking"),
                                         "LAB 2 RECAP &middot; WHAT SHAP IS"), out_dir, "receipt")
    cards["three"] = render(css, clean(by_title("Three tools, three boss-questions"),
                                       "LAB 2 RECAP &middot; USE ALL THREE"), out_dir, "three")

    pi_body = (
        '<div class="note">Freeze the trained model. <b>Shuffle one column</b> of X_test, predict again, '
        'and watch R&sup2; drop. Repeat ~30&times; for a box plot. A big drop means the model <b>leans on</b> '
        'that column &mdash; and it works on <b>any</b> model.</div>'
        '<div class="code" style="font-size:14.5pt;margin:0.22in 1.1in 0.1in">'
        '<span class="c"># corrupt one column, measure the damage</span>\n'
        '<span class="k">from</span> sklearn.inspection <span class="k">import</span> permutation_importance\n'
        'r = <span class="fn">permutation_importance</span>(model, X_test, y_test,\n'
        '                           n_repeats=30)</div>'
        '<div class="pillrow"><span class="pill">shuffle a key column &rarr; R&sup2; 0.90 &rarr; 0.80</span>'
        '<span class="pill dim">shuffle a useless one &rarr; R&sup2; stays &asymp; 0.90</span></div>'
    )
    pi = content("LAB 2 RECAP &middot; TOOL 1", "Permutation importance &mdash; &ldquo;what matters?&rdquo;",
                 pi_body, ("Tells you WHAT matters.", "Not how, and not for which row &mdash; that&rsquo;s the next two tools."), 0)
    cards["pi"] = render(css, clean(pi, "LAB 2 RECAP &middot; TOOL 1"), out_dir, "pi")

    pdp_body = (
        '<div class="note">Take <b>one row</b>. Freeze every feature <b>except one</b>. Sweep that feature '
        '(0, 1, 2, 3 bedrooms&hellip;) and plot the prediction. Every row &rarr; a plate of spaghetti &rarr; '
        '<b>average it</b> into one curve.</div>'
        '<div class="split"><div class="code">'
        '<span class="c"># sweep one feature, average the response</span>\n'
        '<span class="k">from</span> sklearn.inspection <span class="k">import</span> (\n'
        '    PartialDependenceDisplay)\n'
        'PartialDependenceDisplay.<span class="fn">from_estimator</span>(\n'
        '    model, X, [<span class="s">"bedrooms"</span>])</div>'
        + spaghetti_svg() + '</div>'
    )
    pdp = content("LAB 2 RECAP &middot; TOOL 2", "Partial dependence &mdash; &ldquo;how does it behave?&rdquo;",
                  pdp_body, ("Tells you HOW a feature moves the prediction.", "On average &mdash; which can hide the rows that behave differently."), 0)
    cards["pdp"] = render(css, clean(pdp, "LAB 2 RECAP &middot; TOOL 2"), out_dir, "pdp")

    define = content("LAB 2 RECAP &middot; READ THIS ONE", "So what IS a SHAP value?", DEFINE_BODY,
                     ("A SHAP value = one feature&rsquo;s fair share of one prediction.",
                      "Same shape as X: one number per row, per feature."), 0)
    cards["define"] = render(css, clean(define, "LAB 2 RECAP &middot; READ THIS ONE"), out_dir, "define")

    fx_body = (
        '<div class="note" style="font-size:14.5pt">A paper machine the size of a football field, ~1,000 sensors, '
        'a KPI that went bad in July. Retrain a random forest <b>every hour</b>, run SHAP on each new prediction, '
        'and plot each sensor&rsquo;s SHAP <b>over time</b>:</div>'
        + heatmap_html()
    )
    fx = content("LAB 2 RECAP &middot; IN THE WILD", "SHAP as a forensic tool", fx_body,
                 ("Three suspects light up together &mdash; one was the culprit.",
                  "SHAP didn&rsquo;t just predict the failure; it pointed at where to look."), 0)
    cards["forensic"] = render(css, clean(fx, "LAB 2 RECAP &middot; IN THE WILD"), out_dir, "forensic")
    return cards


if __name__ == "__main__":
    out = os.path.join(HERE, "cards")
    for k, v in build(out).items():
        print(k, os.path.exists(v), v)
