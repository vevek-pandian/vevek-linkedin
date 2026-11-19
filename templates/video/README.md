# Jagged Intelligence video template

Standard format for Vevek Pandian's LinkedIn videos.

- 1080 x 1920 (vertical), 30 fps, H.264 + AAC, 25–35 seconds
- 6 scenes: Hook → Big number → Bar comparison → Bar comparison / supporting stat → Quote (light) → 3 ✅ moves + "Follow Vevek Pandian" pill
- Persistent: "Jagged Intelligence" kicker with zigzag, thin blue progress bar, photo footer ("Vevek Pandian · AI Engineering Leader · UAE") and source line
- Colours and fonts: see the project design language (blue #5AA9FF on dark #0D1117, #1D5FBF on light #F4F2EC; Space Grotesk + Inter; green ticks #16A34A)
- Audio: original synthesised bed (music.py): soft pad + pulse, whoosh at scene changes, ticks on number reveals, low hit on hook and quote. No voiceover.

How to make a new one:
1. Copy video-template.html, change only the scene text and numbers (and the scene timings in `S` if needed).
2. `python3 render.py stills` to check key frames, then `python3 render.py full` (one MP4 per scene).
3. Update cue times in music.py to the new scene starts and number reveals, run it.
4. Join the scene files with the ffmpeg concat demuxer (`-c copy`) and mux the soundtrack (`-c:v copy -c:a aac`).
