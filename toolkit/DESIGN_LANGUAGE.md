# Vevek Pandian · LinkedIn design language

Use this for every LinkedIn visual: single-image post cards, carousels, newsletter covers and banners. The brand name on visuals is **Jagged Intelligence**. Standard theme: **blue**.

---

## 1. Formats and sizes

| Use | Size (px) | Notes |
|---|---|---|
| Post image (default) | 1080 × 1350 (4:5 portrait) | Takes the most feed space on mobile |
| Carousel slide | 1080 × 1350 | Export as one PDF, 6–7 slides (max 10) |
| Square fallback | 1080 × 1080 | Only if a layout needs it |
| Newsletter cover | 1200 × 627 | No photos of real public figures |

- Safe padding: **88 px top, 96 px sides, 80 px bottom.**
- Layout: three zones stacked with `space-between`: **top bar → main content → footer.**
- One message per image. Text must read on a phone.

---

## 2. Colour

### Backgrounds
| Token | Hex | Use |
|---|---|---|
| Ink (dark ground) | `#0D1117` | Dark slides and cards |
| Paper (light ground) | `#F4F2EC` | Light slides and cards |
| Dark panel | `#161C25` | Tiles/boxes on dark, with border `#252D39` (2 px) |
| Light panel | `#FFFFFF` | Tiles/boxes on light, with border `#E3DFD3` (2 px) |
| Highlight panel (dark) | `#12202F` | The one emphasised tile on a dark slide |

### Text
| Token | Hex | Use |
|---|---|---|
| Text on dark | `#F3F1EA` | Headlines, body |
| Muted on dark | `#C9CED6` / `#B4BBC6` | Body / secondary |
| Faint on dark | `#9AA3AF` | Slide numbers, sources |
| Text on light | `#0D1117` | Headlines |
| Body on light | `#2B323C` / `#3E4652` | Body / tile descriptions |
| Faint on light | `#5B6370` | Slide numbers, sources |

### Accent (blue theme, the standard)
| Token | Hex | Use |
|---|---|---|
| Blue on dark | `#5AA9FF` | Kicker, accent headline line, big numbers, buttons, photo ring, highlighted tile border |
| Blue on light | `#1D5FBF` | Same roles on light backgrounds (darker for contrast) |
| Button text on blue | `#0D1117` | Text on the blue "Swipe"/"Follow" pill |
| Tick green | `#16A34A` | ✅ check circles only. The green tick stays green on every theme |

Other accents exist in the template's colour picker (green `#34D27B`, amber `#F5A524`), but **blue is the standard for all carousels and post images.**

### Lines
- Footer divider: 2 px, `#252D39` on dark, `#D9D5CA` on light.

---

## 3. Typography

| Role | Font | Weight | Size (px, at 1080 wide) |
|---|---|---|---|
| Cover headline | Space Grotesk | 700 | 104–150, line-height 1.0, letter-spacing −0.03em |
| Slide headline | Space Grotesk | 700 | 78–96, line-height 1.02–1.05 |
| Accent second line | Space Grotesk | 600 | 72–76, in blue |
| Big number | Space Grotesk | 700 | 260–340, letter-spacing −0.05em, in blue |
| Kicker (top-left) | Space Grotesk | 600 | 26, UPPERCASE, letter-spacing 0.14em, blue |
| Tile title | Space Grotesk | 700 | 48–50 |
| Tile label (STEP 1 / ZONE 3) | Space Grotesk | 600 | 22–24, letter-spacing 0.12em |
| Body | Inter | 400 | 34–40, line-height 1.4–1.45 |
| Tile description | Inter | 400 | 27–28, line-height 1.4 |
| Slide number / source | Inter | 500 | 21–26 |

- Fonts: Google Fonts (Space Grotesk 500/600/700, Inter 400/500/600).
- Sentence case for headlines. No emoji except ✅ in post text (on visuals, draw the tick as a green circle).

---

## 4. Signature elements

- **Zigzag mark:** a small jagged polyline (44 × 22 px, 3.5 px stroke, rounded joins) before the kicker, in blue. It stands for "jagged intelligence". A wider faint zigzag (`#2A313C`) can sit above the cover footer.
- **Kicker + slide number** on every slide: kicker top-left, `01 / 06` top-right (or "Jagged Intelligence" on single post cards).
- **Photo footer** on every slide and card: round headshot (72 px on inner slides, 84 px on post cards, 96 px on covers, 140 px on the last slide), object-position 50% 22%, 3 px ring in the slide's blue. Next to it: **Vevek Pandian** (Space Grotesk 600) and **AI Engineering Leader · UAE** (Inter, 75% opacity). Source line on the right.
- **Location wording:** always "UAE", never "Abu Dhabi".
- **No employer:** never show Greenfield on visuals.

---

## 5. Components

- **Tick list:** white tiles (light slide) with a 52 px green circle tick, a 38 px Space Grotesk title and a 28 px Inter description. 4 rows max.
- **2 × 2 framework grid:** four tiles, one highlighted (blue 3 px border, highlight panel, label in blue, e.g. "ZONE 3 · WHERE IT'S WON").
- **Stat slide:** one giant blue number, one-line caption (56 px), two mini stat tiles below, source in footer.
- **Quote / key line:** large quote mark in blue, 84–124 px headline. A full blue background is allowed for one quote slide per carousel (dark text on blue).
- **Pills/buttons:** fully rounded (999 px radius). Primary = blue fill, ink text. Secondary = 2 px border `#3A4351`.
- **Bar comparison:** 64 px tracks in dark panel colour, grey bar `#3A4351` for the baseline, blue bar for the headline value, widths proportional to the real numbers.
- Corner radius: tiles 22–24 px, profile card 28 px.

---

## 6. Carousel structure (6–7 slides)

1. **Cover (dark):** kicker, headline + blue punchline, one-line promise, photo + name, blue "Swipe →" pill.
2. **Context (light):** what happened, 3 short paragraphs, blue rule.
3. **Big number (dark):** stat slide.
4. **Tick list (light):** 4 lessons or signs.
5. **Framework (dark):** 2 × 2 grid with one highlighted tile, "Save this…" in the footer.
6. **Key line (blue background), optional.**
7. **Question + follow (dark):** the comment question, profile card with Follow / Repost / Save pills, newsletter line in the footer.

Alternate dark and light. Number slides `01 / 06`. Cite sources in the footer of any slide with numbers.

---

## 7. Post image cards (single image)

One card per text post, same palette and footer. Pick one layout:
- **Key line:** a 2-line headline, second line in blue.
- **Big number:** a giant blue figure plus caption.
- **Framework:** 3 rows or a 2 × 2 grid of the post's ✅ points.
- **Comparison:** two bars or before/after.

Top-right label reads "Jagged Intelligence". Alternate dark/light across the week.

---

## 8. Video template (standard)

- **Format:** 1080 × 1920 vertical, 30 fps, H.264 + AAC, 25–35 seconds. All text on screen (works muted).
- **Framing:** always through Jagged Intelligence: where AI (or its rollout) is brilliant vs where it quietly stumbles.
- **Persistent elements:** zigzag "Jagged Intelligence" kicker top-left, small context tag top-right (e.g. "New study · Nov 2026"), thin blue progress bar under it, photo footer (104 px photo, name, "AI Engineering Leader · UAE") with the source on the right.
- **6 scenes:**
  1. Hook (dark): white line + blue punchline + one jagged-intelligence sentence
  2. Big number (dark): counts up in blue, the comparison number in grey `#4A5563`
  3. Bar comparison (dark): blue bar vs grey bar, growing to the real values
  4. Supporting stat (dark): second comparison plus one "yet…" line
  5. Quote (light background, blue quote mark, exact wording only)
  6. Close (dark): "3 ways to smooth the jagged edge" with 3 ✅ tiles and a blue **"Follow Vevek Pandian"** pill
- **Motion:** elements slide up 40 px and fade in (ease-out cubic, ~0.55 s); 0.3 s fades between scenes.
- **Audio:** original synthesised bed (soft pad + light pulse), whoosh on each scene change, soft ticks on number reveals and ticks, low hit on hook and quote. Peak about −1 dBFS, fade in and out. No voiceover and no voice imitating Vevek.
- **Files:** template, render script and music script are in the GitHub repo under `templates/video/`; finished videos go in `videos/`.

## 9. Call to action (all formats)

- The follow call to action is **"Follow Vevek Pandian"** (brand-first), on videos, carousel last slides and any post card that has a call to action.

## 10. Assets and where things live

- **Headshot:** Vevek's photo (navy jacket, grey background). On the design canvas it is uploaded asset `/_blob/931c17d9267fe910e2a8f4ae0d7c4d00`.
- **Design canvas (editable template + all carousels):** Claude artifact "Jagged Intelligence Carousel Template" (claude.ai/artifact/1WZBzK4BuYKMQTEED1ANGQ). Pages: Template, Carousel 1–4.
- **Public image hosting for Buffer:** GitHub repo `vevek-pandian/vevek-linkedin`, folder `images/`. Use the commit-SHA raw URL (`raw.githubusercontent.com/vevek-pandian/vevek-linkedin/<commit>/images/<file>.png`); the `/main/` URL can lag behind a new push.
- **File naming:** `NN-short-topic.png` for post cards; `Carousel_N_Topic.pdf` for carousels.
- **Alt text:** add a one-sentence description to every image attached in Buffer.

---

## 11. Don'ts

- No stock photos, no photos of real public figures, no company logos (company names as text are fine).
- No gradients, glows or emoji on visuals.
- No more than one highlighted tile per slide.
- No text below 20 px.
- Don't change the ✅ tick colour from green.
