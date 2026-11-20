# Jagged Intelligence content run: RUNBOOK

This is the runbook for the scheduled task "Jagged Intelligence 9-day content run". It runs every 9 days. Each run researches the hottest AI news of the last 9 days, makes the next batch of LinkedIn content, queues it in Buffer, and updates the content log.

Everything a fresh session needs is in this repo:

| Path | What |
|---|---|
| `toolkit/DESIGN_LANGUAGE.md` | Visual rules (colours, fonts, layouts, video template). Follow it exactly. |
| `toolkit/assets/` | Vevek's headshot (`photo.jpg`) and fonts (Space Grotesk, Inter). |
| `toolkit/cards/make_cards.py` + `toolkit/cards/examples/` | Post image cards, 1080×1350 PNG. Copy the script, replace the `cards[...]` entries, run it. Output goes to `images/`. |
| `toolkit/carousel/example/1..6.html` + `render_carousel.py` | Carousel slides. Copy the example folder to `toolkit/carousel/<NN-topic>/`, edit the slides, then run `python3 toolkit/carousel/render_carousel.py <dir> carousels/<Carousel_N_Topic>.pdf`. |
| `templates/video/engine.py` + `templates/video/specs/` | Videos. Write a new spec next to the others (NAME, TAG, SOURCE, SEED, MUSIC, SCENES), then run `cd templates/video && python3 engine.py <spec> stills` and check the stills in `build/<NAME>/`. Then run `python3 engine.py <spec> full`. Output goes to `videos/<NAME>.mp4`. |
| `toolkit/log/build_log.py`, `add_row.py` | The content log. `python3 toolkit/log/add_row.py '<json list of 10 fields>'`, then `python3 toolkit/log/build_log.py`. This writes `logs/Vevek_LinkedIn_Content_Log.xlsx` and `logs/linkedin-content-log.md`. |

Python needs `playwright` (preinstalled with Chromium), `numpy`, `pypdf`, `openpyxl`, `pillow` and ffmpeg. Install whatever is missing with `pip install --break-system-packages`.

## Fixed facts

- **Person:** Vevek Pandian, AI Engineering Leader, UAE.
- **Brand:** "Jagged Intelligence": where AI is brilliant and where it quietly stumbles.
- **Buffer:** organisation "My Organization" `5b505238cd0a06925135162d`, LinkedIn channel `6aff2c55ece6dfde5f21aa24`, timezone Asia/Dubai (+04:00).
- **Posting slots (UAE time):** Mon 08:45, Tue 15:30, Wed 16:00, Thu 16:30, Fri 09:00. No weekends.
- **UAE public holidays:** skip 2–3 Dec (National Day) and 1 Jan, and check for any others in the window.
- **Free plan limit:** Buffer's free plan holds at most 10 scheduled posts at once. Count the scheduled posts first and never go over 10.
- **Public media hosting:** this repo. Use the commit-SHA raw URL `https://raw.githubusercontent.com/vevek-pandian/vevek-linkedin/<SHA>/<path>`, not `/main/`, because `/main/` can lag. Check each URL returns 200 before giving it to Buffer.
- **Git:** commit with `git -c user.name="Vevek Pandian" -c user.email="vevek-pandian@users.noreply.github.com" commit ...`, then push with `git -c push.negotiate=true push origin main`.

## Steps for each run

1. **Get the repo.** Attach `vevek-pandian/vevek-linkedin` with push access (add_repo, access "push"), then clone it.
2. **Read the log.** Open `logs/linkedin-content-log.md` and read every past title and topic key. Never repeat a topic, company angle or hook.
3. **Find the window.**
   - Use Buffer `list_posts` (status scheduled, sorted by dueAt) to find the latest scheduled post.
   - The window is the 9 days starting the day after that post. If nothing is scheduled, the window starts tomorrow.
   - Fill every weekday slot in the window that isn't a UAE holiday. That is usually 5–7 posts, capped so the total in Buffer stays at 10 or fewer.
4. **Research.**
   - Use web search to find the hottest AI news of the **last 9 days**. Look at model launches, big company moves, studies and surveys with real numbers, failures and incidents, regulation, and UAE/GCC AI news.
   - Confirm every fact and number from a primary or reputable source.
   - Quote people only with their exact words.
   - No photos of real people and no company logos.
5. **Plan the mix** across the window:
   - About half are **text + image card** posts.
   - One **carousel** (6 slides, PDF), on the Wednesday slot if there is one.
   - One or two **short videos** (25–35 s, vertical), on a Friday slot if possible.
   - At least one piece in each run is for **students / early-career**: lessons from AI engineering leadership on tools, best practices, design and architecture.
   - Alternate dark and light visuals.
6. **Write the posts** in the house style:
   - **Hook:** two short lines. A plain statement, then the punchline (for example, "AI tools change every few months. / The stack doesn't.").
   - **Body:** short paragraphs, framed through jagged intelligence, with 3–5 **✅ green-tick** points, a one-line key line, and practical steps.
   - **Close:** a specific question, never "Thoughts?".
   - **Length:** about 900–1,800 characters.
   - **Hashtags:** 5 at the end, CamelCase, starting with **#JaggedIntelligence**.
   - **Never include** an AI-disclosure line, the employer name (Greenfield) or past employers.
   - **Location:** always "UAE", never "Abu Dhabi".
   - **Call to action** on visuals: **"Follow Vevek Pandian"**.
7. **Make the visuals.**
   - Cards go in `images/NN-topic.png` (keep numbering from the highest existing number).
   - Carousels go in `carousels/Carousel_N_Topic.pdf`. Also save slide 1 as a PNG for the Buffer thumbnail.
   - Videos go in `videos/NN-topic.mp4`. Give each video its own original soundtrack: a different key, instrument voice (piano, rhodes, marimba or bell) and tempo from recent videos. Keep it pleasant and calm.
   - Look at every image and at least the video stills before using them. Fix any text overflow or bad line breaks.
8. **Push** to GitHub and check every raw SHA URL returns 200.
9. **Queue in Buffer** with `create_post`: `mode: customScheduled`, `dueAt` in +04:00, `schedulingType: automatic`.
   - Image posts: `{image:{url, metadata:{altText}}}`.
   - Videos: `{video:{url, metadata:{title}}}`.
   - Carousels: `{document:{url, title, thumbnailUrl}}`.
10. **Update the log.** Add one row per item:
    `[created, "YYYY-MM-DD HH:MM", format, hook, topic key, companies, pillar, key facts + source, "Scheduled in Buffer", "Buffer + <repo path>"]`
    - Rebuild with `build_log.py`, commit `logs/` and push.
    - If the Projects tool is available, write `logs/linkedin-content-log.md` to project doc `claude/linkedin-content-log.md` (project_write with local_path).
    - Send the xlsx to the user with SendUserFile.
11. **Keep the schedule going.**
    - Use list_triggers to check for upcoming runs of "Jagged Intelligence 9-day content run".
    - If fewer than 2 future runs exist, create the next one-shot runs at 11:23 Asia/Dubai, 9 days apart after the latest one. Use the same prompt.
12. **Report** with SendUserMessage: what was queued (date, format, hook), sources, the next run date, and anything that needs Vevek (for example, Buffer full or a holiday skipped).

If something blocks the run (Buffer or GitHub unreachable, the queue already full), don't guess. Do the research and drafts, save them under `drafts/<date>/` in the repo, push, and report what's waiting.
