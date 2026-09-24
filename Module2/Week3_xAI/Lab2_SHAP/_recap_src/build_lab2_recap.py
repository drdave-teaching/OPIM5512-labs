# -*- coding: utf-8 -*-
"""Lab 2 (SHAP) recap video — Dave's real audio from the Stamford session (9/23) over rendered
code mock-ups for the theory beats, and real (cropped) screen footage only where the screen IS the
point (the tree lighting up, the beeswarm). Same pipeline as the OPIM 5641 Studio 2 recap.
No student webcams (cropped out) and no client material (the war story uses a mock-up)."""
import os
import subprocess
import tempfile
from PIL import Image, ImageDraw, ImageFont
import render_recap_cards

SRC = r"C:\Users\dww05002\Downloads\Dave Wanik's Personal Room-20260924 0202-1.mp4"
OUT = r"C:\Users\dww05002\Documents\DS_Fall2026_GeneralMaterials\OPIM5512_Lab2_SHAP_Recap.mp4"
HERE = os.path.dirname(os.path.abspath(__file__))
WORK = os.path.join(tempfile.gettempdir(), "l2recap")
os.makedirs(WORK, exist_ok=True)

W, H, FPS = 1280, 720, 30
CROP = "crop=1624:872:148:168"   # drops the webcam strip (top) and the taskbar (bottom)
NAVY = (10, 31, 68)
GOLD = (242, 169, 0)
WHITE = (245, 245, 247)
SOFT = (199, 208, 222)


def font(name, size, fallback):
    p = os.path.join(r"C:\Windows\Fonts", name)
    if not os.path.exists(p):
        p = os.path.join(r"C:\Windows\Fonts", fallback)
    return ImageFont.truetype(p, size)


T1 = font("segoeuib.ttf", 54, "arialbd.ttf")
T2 = font("segoeuib.ttf", 28, "arialbd.ttf")
T3 = font("segoeui.ttf", 28, "arial.ttf")

# (start_sec, dur_sec, chapter title, subtitle, card key — or None for real footage)
SEGMENTS = [
    (575.0, 62.0, "1 \u00b7 Permutation importance", "Shuffle a column, watch R\u00b2 drop \u2014 what matters?", "pi"),
    (836.45, 71.55, "2 \u00b7 Partial dependence", "Freeze a row, sweep one feature \u2014 how does it behave?", "pdp"),
    (1435.3, 86.0, "3 \u00b7 Why SHAP is fair", "Split the Kaggle prize by each player's contribution", "prize"),
    (1956.6, 64.0, "4 \u00b7 Play the game on a tree", "Known features use this house; unknown ones use the baseline", None),
    (4347.3, 74.3, "5 \u00b7 So what IS a SHAP value?", "One feature's push on one prediction, over the baseline",
     [("define", 0.50), ("receipt", 0.50)]),
    (2590.0, 71.0, "6 \u00b7 The global view", "Every dot is one hour \u2014 the beeswarm", None),
    (2787.38, 38.77, "7 \u00b7 Use all three", "PI ranks \u00b7 PDP shapes \u00b7 SHAP itemizes", "three"),
    (4767.9, 91.45, "8 \u00b7 SHAP in the wild", "1,000 sensors, one broken KPI \u2014 where do you look?", "forensic"),
]
# boundaries are word-aligned (faster-whisper word timestamps on the source) -> clean sentence starts/ends


def card(path, big, small, eyebrow="OPIM 5512 \u00b7 Lab 2 recap"):
    img = Image.new("RGB", (W, H), NAVY)
    d = ImageDraw.Draw(img)
    d.rectangle([60, 84, 220, 92], fill=GOLD)
    d.text((60, 108), eyebrow, font=T2, fill=GOLD)
    y = 250
    for line in big:
        d.text((60, y), line, font=T1, fill=WHITE)
        y += 76
    y += 14
    for line in small:
        d.text((60, y), line, font=T3, fill=SOFT)
        y += 42
    d.rectangle([0, H - 10, W, H], fill=GOLD)
    img.save(path)


def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        raise SystemExit("FFMPEG FAILED\n" + " ".join(str(c) for c in cmd[:12]) + "\n" + r.stderr[-1500:])


def afilter(dur):
    fade_out = max(dur - 0.25, 0)
    return f"loudnorm=I=-18:TP=-2:LRA=11,afade=t=in:d=0.12,afade=t=out:st={fade_out:.2f}:d=0.25"


def staged_cards_over_audio(stages, start, dur, out, tag):
    """Several rendered cards in sequence (each for its fraction of the chapter) over one audio run."""
    parts = []
    for k, (png, frac) in enumerate(stages):
        p = os.path.join(WORK, f"{tag}_s{k}.mp4")
        run(["ffmpeg", "-loglevel", "error", "-y", "-loop", "1", "-framerate", str(FPS), "-i", png,
             "-t", f"{dur * frac:.3f}", "-r", str(FPS),
             "-c:v", "libx264", "-crf", "20", "-preset", "veryfast", "-tune", "stillimage",
             "-pix_fmt", "yuv420p", "-an", p])
        parts.append(p)
    lst = os.path.join(WORK, f"{tag}_list.txt")
    with open(lst, "w", encoding="utf-8") as f:
        for p in parts:
            f.write("file '" + p.replace("\\", "/") + "'\n")
    vid = os.path.join(WORK, f"{tag}_v.mp4")
    run(["ffmpeg", "-loglevel", "error", "-y", "-f", "concat", "-safe", "0", "-i", lst, "-c", "copy", vid])
    run(["ffmpeg", "-loglevel", "error", "-y", "-i", vid, "-ss", f"{start:.3f}", "-t", f"{dur:.3f}", "-i", SRC,
         "-map", "0:v", "-map", "1:a", "-filter:a", afilter(dur), "-t", f"{dur:.3f}",
         "-c:v", "copy", "-c:a", "aac", "-b:a", "128k", "-ar", "48000", "-ac", "2", out])


def silent_card(png, seconds, out):
    run(["ffmpeg", "-loglevel", "error", "-y", "-loop", "1", "-framerate", str(FPS), "-i", png,
         "-f", "lavfi", "-i", "anullsrc=channel_layout=stereo:sample_rate=48000",
         "-t", f"{seconds:.3f}", "-r", str(FPS),
         "-c:v", "libx264", "-crf", "20", "-preset", "veryfast", "-tune", "stillimage", "-pix_fmt", "yuv420p",
         "-c:a", "aac", "-b:a", "128k", "-ar", "48000", "-ac", "2", "-shortest", out])


def card_over_audio(png, start, dur, out):
    """Dave's audio from the real session, played over a rendered card."""
    run(["ffmpeg", "-loglevel", "error", "-y", "-loop", "1", "-framerate", str(FPS), "-i", png,
         "-ss", f"{start:.3f}", "-t", f"{dur:.3f}", "-i", SRC,
         "-map", "0:v", "-map", "1:a", "-filter:a", afilter(dur),
         "-t", f"{dur:.3f}", "-r", str(FPS),
         "-c:v", "libx264", "-crf", "20", "-preset", "veryfast", "-tune", "stillimage", "-pix_fmt", "yuv420p",
         "-c:a", "aac", "-b:a", "128k", "-ar", "48000", "-ac", "2", out])


def real_clip(start, dur, out):
    vf = (f"{CROP},scale={W}:{H}:force_original_aspect_ratio=decrease,"
          f"pad={W}:{H}:(ow-iw)/2:(oh-ih)/2:color=0x0A1F44,setsar=1,fps={FPS}")
    run(["ffmpeg", "-loglevel", "error", "-y", "-ss", f"{start:.3f}", "-t", f"{dur:.3f}", "-i", SRC,
         "-filter:v", vf, "-filter:a", afilter(dur),
         "-c:v", "libx264", "-crf", "20", "-preset", "veryfast", "-pix_fmt", "yuv420p",
         "-c:a", "aac", "-b:a", "128k", "-ar", "48000", "-ac", "2", out])


def main():
    print("rendering code mock-ups...")
    cards = render_recap_cards.build(os.path.join(HERE, "cards"))

    parts = []
    title_png = os.path.join(WORK, "title.png")
    card(title_png,
         ["Lab 2 recap", "Explaining a model with SHAP"],
         ["Permutation importance \u00b7 partial dependence \u00b7 SHAP",
          "In Dave's own words, from the Stamford session."])
    p = os.path.join(WORK, "p000.mp4")
    silent_card(title_png, 6, p)
    parts.append(p)

    total = 6.0
    for i, (start, dur, title, sub, key) in enumerate(SEGMENTS, 1):
        png = os.path.join(WORK, f"sec{i:02d}.png")
        card(png, [title], [sub])
        c = os.path.join(WORK, f"p{i:03d}a.mp4")
        silent_card(png, 2.4, c)
        parts.append(c)

        v = os.path.join(WORK, f"p{i:03d}b.mp4")
        if isinstance(key, list):
            staged_cards_over_audio([(cards[k], f) for k, f in key], start, dur, v, f"st{i:02d}")
            kind = "cards: " + " -> ".join(k for k, _ in key)
        elif key:
            card_over_audio(cards[key], start, dur, v)
            kind = f"card: {key}"
        else:
            real_clip(start, dur, v)
            kind = "real footage"
        parts.append(v)
        total += 2.4 + dur
        print(f"  ch {i}: {title:<34} {dur:6.1f}s  {kind}")

    end_png = os.path.join(WORK, "end.png")
    card(end_png,
         ["That's SHAP."],
         ["\u2022 Finish the lab: two plots + branch \u2192 PR \u2192 review \u2192 merge",
          "\u2022 Submit: a screenshot of Insights \u2192 Network (the two-way loop)",
          "\u2022 Recap, instructions, 20 steps: HuskyCT \u2192 In-Class Labs \u2192 Lab 2"])
    p = os.path.join(WORK, "p999.mp4")
    silent_card(end_png, 9, p)
    parts.append(p)
    total += 9

    listfile = os.path.join(WORK, "list.txt")
    with open(listfile, "w", encoding="utf-8") as f:
        for p in parts:
            f.write("file '" + p.replace("\\", "/") + "'\n")
    run(["ffmpeg", "-loglevel", "error", "-y", "-f", "concat", "-safe", "0", "-i", listfile,
         "-c", "copy", "-movflags", "+faststart", OUT])
    print(f"DONE -> {OUT}  (~{total / 60:.1f} min)")


if __name__ == "__main__":
    main()
