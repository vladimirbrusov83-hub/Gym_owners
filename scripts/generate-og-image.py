#!/usr/bin/env python3
"""
Generates og-image.png (1200×630) for course.brusovcoach.org.
Run from project root: python3 scripts/generate-og-image.py
"""

from PIL import Image, ImageDraw, ImageFont
import os

WIDTH, HEIGHT = 1200, 630
OUTPUT = os.path.join(os.path.dirname(__file__), "..", "og-image.png")

# Palette (matches style.css)
CREAM       = "#FAF9F5"
ACCENT      = "#D97B54"  # terracotta orange
TEXT_DARK   = "#1C1813"
TEXT_MUTED  = "#6B6257"

GEORGIA_BOLD    = "/System/Library/Fonts/Supplemental/Georgia Bold.ttf"
GEORGIA_REGULAR = "/System/Library/Fonts/Supplemental/Georgia.ttf"
SANS            = "/System/Library/Fonts/SFNS.ttf"

MARGIN_LEFT  = 80
MARGIN_RIGHT = 60

def load(path, size):
    return ImageFont.truetype(path, size)

def fit_font(path, text, max_width, max_size, min_size=40):
    for size in range(max_size, min_size - 1, -1):
        if load(path, size).getlength(text) <= max_width:
            return load(path, size)
    return load(path, min_size)

img  = Image.new("RGB", (WIDTH, HEIGHT), CREAM)
draw = ImageDraw.Draw(img)

# ── Top accent line ──────────────────────────────────────────────────────────
draw.rectangle([0, 0, WIDTH, 6], fill=ACCENT)

# ── Fonts ────────────────────────────────────────────────────────────────────
title_max_w = WIDTH - MARGIN_LEFT - MARGIN_RIGHT - 20
f_title    = fit_font(GEORGIA_BOLD, "Build with Claude for Gym Owners", title_max_w, 76)
f_subtitle = load(SANS, 34)
f_tagline  = load(SANS, 24)
f_byline   = load(SANS, 20)

# ── Layout ───────────────────────────────────────────────────────────────────
TOP_START = 6 + 80

# Title
title_text = "Build with Claude for Gym Owners"
draw.text((MARGIN_LEFT, TOP_START), title_text, font=f_title, fill=TEXT_DARK)
title_bbox   = draw.textbbox((MARGIN_LEFT, TOP_START), title_text, font=f_title)
title_bottom = title_bbox[3]

# Subtitle
subtitle_text = "A free practical course — no coding required"
subtitle_y = title_bottom + 22
draw.text((MARGIN_LEFT, subtitle_y), subtitle_text, font=f_subtitle, fill=TEXT_MUTED)
subtitle_bbox   = draw.textbbox((MARGIN_LEFT, subtitle_y), subtitle_text, font=f_subtitle)
subtitle_bottom = subtitle_bbox[3]

# Tagline — two lines
tagline_line1 = "Member intake · Difficult conversations · Communication scripts"
tagline_line2 = "Hiring & staff tools — built in a weekend, used every day"
tagline_y = subtitle_bottom + 28
draw.text((MARGIN_LEFT, tagline_y), tagline_line1, font=f_tagline, fill=TEXT_MUTED)
bbox1 = draw.textbbox((MARGIN_LEFT, tagline_y), tagline_line1, font=f_tagline)
draw.text((MARGIN_LEFT, bbox1[3] + 6), tagline_line2, font=f_tagline, fill=TEXT_MUTED)

# Bottom-left: by Vladimir Brusov
byline_y = HEIGHT - 50 - 20
draw.text((MARGIN_RIGHT, byline_y), "by Vladimir Brusov", font=f_byline, fill=TEXT_MUTED)

# Bottom-right: site URL (right-aligned, accent color)
url_text = "course.brusovcoach.org"
url_w    = load(SANS, 20).getlength(url_text)
url_x    = WIDTH - MARGIN_RIGHT - url_w
draw.text((url_x, byline_y), url_text, font=f_byline, fill=ACCENT)

# ── Save ─────────────────────────────────────────────────────────────────────
img.save(OUTPUT, "PNG", optimize=True)
print(f"Saved: {os.path.abspath(OUTPUT)}")
print(f"Size:  {os.path.getsize(OUTPUT):,} bytes")
