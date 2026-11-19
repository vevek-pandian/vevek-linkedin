NAME = "03-what-production-teaches-you"
TAG = "For students"
SOURCE = "Lessons from AI<br>engineering leadership"
SEED = 3
# Warm lo-fi Rhodes, F major jazz ii–V–I–vi with soft hats
MUSIC = {"bpm": 82, "chords": [[55, 58, 62, 65], [48, 52, 55, 58], [53, 57, 60, 64], [50, 53, 57, 60]],
         "voice": "rhodes", "pattern": [0, None, 2, 1, None, 3, 2, None], "step": 0.5, "pad": 0.15, "bass": 0.11, "lead": 0.09, "hats": 0.035, "tick": 990}

T = '<svg width="60" height="60" viewBox="0 0 52 52" style="flex-shrink:0"><circle cx="26" cy="26" r="26" fill="#16A34A"/><path d="M15 27l7 7 15-16" fill="none" stroke="#fff" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/></svg>'

def tile(n, t, d, at, hi=False):
    return f'<div class="tile a{" hi" if hi else ""}" data-t="{at}"><span class="n">{n}</span><span><span class="t">{t}</span><span class="d">{d}</span></span></div>'

SCENES = [
 {"dur": 5.0, "html": """
  <div class="kick a" data-t="0">For students</div>
  <h1 class="a" data-t="0.25">In tutorials, AI works first time.</h1>
  <h1 class="a blue" data-t="1.1">In production, it fails quietly.</h1>
  <p class="body a" data-t="2.1">That gap is jagged intelligence. Here's what production teaches you that tutorials don't.</p>"""},
 {"dur": 7.0, "html": '<h2 class="a" data-t="0.1">Lessons 1–3</h2>' + "".join([
    tile("01", "Data drifts", "The world changes. Your model doesn't, unless you retrain it.", 0.7),
    tile("02", "Demos hide edge cases", "The weird 5% of inputs decide whether people trust it.", 1.7),
    tile("03", "Every request costs money", "Latency and cost are features, not afterthoughts.", 2.7)])},
 {"dur": 5.5, "html": '<h2 class="a" data-t="0.1">Lessons 4–5</h2>' + "".join([
    tile("04", "Silent failures hurt most", "Monitor what the model says, not just whether it's up.", 0.7, hi=True),
    tile("05", "People need a handoff", "Design the moment the AI says “I'm not sure”.", 1.7)])},
 {"dur": 5.0, "light": True, "html": """
  <p class="q a" data-t="0.1">“</p>
  <h2 class="a" data-t="0.35" style="font-size:100px">Accuracy gets you the demo. <span class="blue">Reliability</span> gets you the job.</h2>"""},
 {"dur": 6.5, "html": f"""
  <h2 class="a" data-t="0.1">Practise this now</h2>
  <div class="tile a" data-t="0.7">{T}<span class="t">Add a “bad inputs” test set to every project</span></div>
  <div class="tile a" data-t="1.3">{T}<span class="t">Log every prediction and review the misses</span></div>
  <div class="tile a" data-t="1.9">{T}<span class="t">Track cost and latency per request</span></div>
  <div class="pill a" data-t="2.8">Follow Vevek Pandian</div>"""},
]
