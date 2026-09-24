# -*- coding: utf-8 -*-
"""Render the Lab 3 markdown handouts -> print-styled PDFs (same house style as Labs 1-2).
Run from anywhere:  python _template_src/build_print.py"""
import os
import subprocess

import markdown

CHROME = r"C:/Program Files/Google/Chrome/Application/chrome.exe"
LAB = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(LAB, "handouts")

DOCS = [
    ("TONIGHT_IN_20_STEPS_lab3.md", "OPIM5512_Lab3_20_Steps_PRINT.pdf", "Lab 3 — Tonight in 20 Steps"),
    ("Lab3_instructions.md", "OPIM5512_Lab3_Instructions_PRINT.pdf", "Lab 3 — Instructions"),
]

CSS = """
@page { size: letter; margin: 0.6in 0.62in; }
* { box-sizing: border-box; }
html { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
body { font-family: 'Segoe UI', Calibri, Arial, sans-serif; font-size: 10.5pt; line-height: 1.42; color:#1c1c1e; margin:0; }
h1 { font-size: 21pt; color:#0A1F44; border-bottom:3px solid #F2A900; padding-bottom:5px; margin:16px 0 10px; }
h1:first-of-type { margin-top:0; }
h2 { font-size: 15pt; color:#0A1F44; margin:18px 0 6px; border-bottom:1px solid #d0d5dd; padding-bottom:3px; page-break-after:avoid; }
h3 { font-size: 12.5pt; color:#0A1F44; margin:12px 0 4px; page-break-after:avoid; }
p, li { margin: 3px 0; }
ul, ol { margin:4px 0 8px; padding-left:22px; }
li { page-break-inside:avoid; }
code { font-family: Consolas, 'Courier New', monospace; background:#eef1f6; padding:1px 4px; border-radius:3px; font-size:9.3pt; }
pre { background:#0f1729; color:#e6edf3; padding:9px 12px; border-radius:6px; overflow:auto; font-size:8.8pt; line-height:1.35; page-break-inside:avoid; }
pre code { background:none; color:inherit; padding:0; font-size:8.8pt; }
blockquote { background:#f5f8fc; border-left:4px solid #9d4edd; margin:8px 0; padding:6px 12px; border-radius:0 4px 4px 0; page-break-inside:avoid; }
blockquote p { margin:3px 0; }
table { border-collapse:collapse; width:100%; margin:8px 0; font-size:9.4pt; page-break-inside:avoid; }
th, td { border:1px solid #cbd2dc; padding:4px 8px; text-align:left; vertical-align:top; }
th { background:#0A1F44; color:#ffffff; }
tr:nth-child(even) td { background:#f6f8fb; }
a { color:#0A55C8; text-decoration:none; }
hr { border:none; border-top:1px solid #d5dae2; margin:14px 0; }
strong { color:#111; }
"""

os.makedirs(OUT, exist_ok=True)
for src, pdf, title in DOCS:
    with open(os.path.join(LAB, src), encoding="utf-8") as f:
        body = markdown.markdown(f.read(), extensions=["tables", "fenced_code", "sane_lists"])
    html = ("<!doctype html><html><head><meta charset='utf-8'><title>" + title + "</title><style>"
            + CSS + "</style></head><body>" + body + "</body></html>")
    tmp = os.path.join(LAB, "_print_temp.html")
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(html)
    out_pdf = os.path.join(OUT, pdf)
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
                    "--run-all-compositor-stages-before-draw", "--virtual-time-budget=12000",
                    "--print-to-pdf=" + out_pdf, "file:///" + tmp.replace("\\", "/")], capture_output=True)
    os.remove(tmp)
    print(("OK " if os.path.exists(out_pdf) else "FAIL ") + out_pdf)
