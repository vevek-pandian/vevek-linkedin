NAME = "02-learn-the-stack-not-the-tool"
TAG = "For students"
SOURCE = "Lessons from AI<br>engineering leadership"
SEED = 2
# Bright piano, D major, I–V–vi–IV
MUSIC = {"bpm": 96, "chords": [[62, 66, 69, 74], [57, 61, 64, 69], [59, 62, 66, 71], [55, 59, 62, 67]],
         "voice": "piano", "pattern": [0, 2, 1, 3, 2, 1, 3, 2], "step": 0.5, "pad": 0.16, "bass": 0.09, "lead": 0.07, "hats": 0, "tick": 1320}

T = '<svg width="60" height="60" viewBox="0 0 52 52" style="flex-shrink:0"><circle cx="26" cy="26" r="26" fill="#16A34A"/><path d="M15 27l7 7 15-16" fill="none" stroke="#fff" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/></svg>'

def tile(n, t, d, at, hi=False, tag=""):
    tg = f'<span class="tag">{tag}</span>' if tag else ""
    return f'<div class="tile a{" hi" if hi else ""}" data-t="{at}"><span class="n">{n}</span><span>{tg}<span class="t">{t}</span><span class="d">{d}</span></span></div>'

SCENES = [
 {"dur": 5.0, "html": """
  <div class="kick a" data-t="0">For students</div>
  <h1 class="a" data-t="0.25">AI tools change every few months.</h1>
  <h1 class="a blue" data-t="1.1">The stack doesn't.</h1>
  <p class="body a" data-t="2.1">That's jagged intelligence for careers: tools spike and fade. Fundamentals compound.</p>"""},
 {"dur": 9.5, "html": '<h2 class="a" data-t="0.1">The AI engineering stack</h2>' + "".join([
    tile("06", "Deployment", "Docker, cloud, monitoring", 3.9),
    tile("05", "Evaluation", "Test sets, metrics, red-teaming", 3.2, hi=True, tag="MOST SKIPPED"),
    tile("04", "LLMs", "APIs, prompting, retrieval (RAG)", 2.5),
    tile("03", "Machine learning", "scikit-learn, PyTorch", 1.8),
    tile("02", "Data", "Cleaning, labelling, pipelines", 1.2),
    tile("01", "Python + SQL", "The language of data", 0.6)])},
 {"dur": 5.0, "light": True, "html": """
  <p class="q a" data-t="0.1">“</p>
  <h2 class="a" data-t="0.35" style="font-size:92px">Go deep on one layer. Understand <span class="blue">every layer</span> well enough to work with the people who own it.</h2>"""},
 {"dur": 5.5, "html": """
  <h2 class="a" data-t="0.1">Where students spend time vs <span class="blue">where it pays off</span></h2>
  <div class="cols a" data-t="0.9">
    <div class="col"><h3 style="color:#9AA3AF">Too much time</h3><p>Chasing the newest model</p><p>Prompt tricks</p><p>Tool tutorials</p></div>
    <div class="col" style="border:3px solid #5AA9FF;background:#12202F"><h3 class="blue">Too little time</h3><p>Data quality</p><p>Evaluation</p><p>Actually shipping</p></div>
  </div>"""},
 {"dur": 6.5, "html": f"""
  <h2 class="a" data-t="0.1">3 moves this semester</h2>
  <div class="tile a" data-t="0.7">{T}<span class="t">Build one project end to end</span></div>
  <div class="tile a" data-t="1.3">{T}<span class="t">Write your evals before your prompts</span></div>
  <div class="tile a" data-t="1.9">{T}<span class="t">Deploy it, even if 10 people use it</span></div>
  <div class="pill a" data-t="2.8">Follow Vevek Pandian</div>"""},
]
