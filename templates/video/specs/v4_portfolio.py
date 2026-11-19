NAME = "04-ai-project-recruiters-remember"
TAG = "For students"
SOURCE = "Lessons from AI<br>engineering leadership"
SEED = 4
# Bright marimba, G major I–vi–IV–V
MUSIC = {"bpm": 108, "chords": [[55, 59, 62, 67], [52, 55, 59, 64], [48, 52, 55, 60], [50, 54, 57, 62]],
         "voice": "marimba", "pattern": [0, 2, 3, 2, 1, 2, 3, None], "step": 0.5, "pad": 0.12, "bass": 0.10, "lead": 0.08, "hats": 0.02, "tick": 1480}

T = '<svg width="60" height="60" viewBox="0 0 52 52" style="flex-shrink:0"><circle cx="26" cy="26" r="26" fill="#16A34A"/><path d="M15 27l7 7 15-16" fill="none" stroke="#fff" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/></svg>'

def tile(n, t, d, at, hi=False, tag=""):
    tg = f'<span class="tag">{tag}</span>' if tag else ""
    return f'<div class="tile a{" hi" if hi else ""}" data-t="{at}"><span class="n">{n}</span><span>{tg}<span class="t">{t}</span><span class="d">{d}</span></span></div>'

SCENES = [
 {"dur": 5.0, "html": """
  <div class="kick a" data-t="0">For students</div>
  <h1 class="a" data-t="0.25">Most AI portfolios look the same.</h1>
  <h1 class="a blue" data-t="1.1">Here's how to stand out.</h1>
  <p class="body a" data-t="2.1">Another chatbot demo won't do it. Proof that you understand where your AI is strong and where it breaks will.</p>"""},
 {"dur": 9.0, "html": '<h2 class="a" data-t="0.1">5 steps to a project that gets remembered</h2>' + "".join([
    tile("01", "Solve a real problem", "For a real person, even if it's one person", 0.7),
    tile("02", "Measure a baseline", "What happens today without AI?", 1.6),
    tile("03", "Ship the simplest version", "Then improve it with evidence", 2.5),
    tile("04", "Show the numbers", "Accuracy, latency, cost per request", 3.4),
    tile("05", "Show where it fails", "Your examples of it breaking, and why", 4.3, hi=True, tag="RARELY DONE")])},
 {"dur": 5.0, "light": True, "html": """
  <p class="q a" data-t="0.1">“</p>
  <h2 class="a" data-t="0.35" style="font-size:100px">Showing where your AI fails proves you <span class="blue">understand it</span>.</h2>"""},
 {"dur": 5.5, "html": """
  <h2 class="a" data-t="0.1">What I usually see vs <span class="blue">what I look for</span></h2>
  <div class="cols a" data-t="0.9">
    <div class="col"><h3 style="color:#9AA3AF">Usually see</h3><p>A tutorial, renamed</p><p>Only the happy path</p><p>No numbers</p></div>
    <div class="col" style="border:3px solid #5AA9FF;background:#12202F"><h3 class="blue">Look for</h3><p>A real user</p><p>A baseline to beat</p><p>Honest failure cases</p></div>
  </div>"""},
 {"dur": 6.5, "html": f"""
  <h2 class="a" data-t="0.1">Your README checklist</h2>
  <div class="tile a" data-t="0.7">{T}<span class="t">The problem and who has it</span></div>
  <div class="tile a" data-t="1.3">{T}<span class="t">Results against a baseline</span></div>
  <div class="tile a" data-t="1.9">{T}<span class="t">Known limits and what you'd do next</span></div>
  <div class="pill a" data-t="2.8">Follow Vevek Pandian</div>"""},
]
