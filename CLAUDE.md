# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this project is

"Build with Claude for Gym Owners" — a free, static HTML course site teaching non-technical gym owners to use Claude AI for operational tasks. No build step, no framework, no dependencies. Open any HTML file directly in a browser.

**Local preview:**
```bash
python3 -m http.server 8080
# then open http://localhost:8080
```

## Architecture

Pure static site — 6 HTML files, one CSS file, one JS file. No bundler, no npm, no templates.

Each module is a self-contained HTML file sharing `style.css` and `script.js`. The nav and mobile menu are duplicated in every file (no server-side includes or JS templating).

**Module numbering:** `module-1.html` through `module-5.html`. The bonus module is `module-5.html`.

## Design system

Anthropic color palette defined as CSS variables in `:root` at the top of `style.css`:
- `--bg` / `--surface` / `--surface-2` — warm cream backgrounds
- `--accent` / `--accent-hover` — terracotta orange (`#D97B54`)
- `--code-bg` — dark background for prompt blocks only
- `--text` / `--text-muted` — warm dark brown tones

**Key CSS classes:**
- `.prompt-block` — wraps `<pre>` prompt text; `script.js` auto-injects a copy button
- `.example-output` — shows example Claude output with left accent border
- `.callout.accent` — callout box with left orange border
- `.steps` — numbered step list using CSS counters
- `.custom-note` — inline code-style highlight for placeholder text like `[GYM NAME]`
- `.module-nav` — prev/next navigation at the bottom of each module
- `.course-byline` — small uppercase link back to homepage, shown at top of `<main>` on module pages

## Nav structure

Two elements per page — desktop (`.nav-links` inside `.nav-inner`) and mobile (`.mobile-menu`):
- Desktop: short labels (`1 · Start`, `2 · Intake`, `3 · Conversations`, `4 · Comms`, `★ Bonus`)
- Mobile: full names (`Module 1 — Start Here`, `Module 2 — Member Intake Assistant`, etc.)
- Active page gets `class="active"` on its `<a>` tag in both menus
- Nav brand shows `Vladimir Brusov` linking to `index.html`

When adding or renaming a module, update the nav block in **all 6 HTML files**.

## Content conventions

- All prompt templates use `[PASTE YOUR GYM PROFILE HERE]` as the first field — this refers to the Gym Profile Block built in Module 1
- Placeholder text uses `[ALL CAPS IN BRACKETS]` style
- Fictional example gym: **Iron Standard** · fictional coach: **Coach John** / `john@ironstandard.com`
- No real people, no real gyms, no direct quotes from external sources
- Prose style: direct, no corporate filler, no excessive explanation — matches the course voice

## Git

Single `main` branch. Remote is `github.com/vladimirbrusov83-hub/Gym_owners`.
