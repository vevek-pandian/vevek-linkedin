NAME = "05-how-a-production-llm-app-is-built"
TAG = "For students"
SOURCE = "Lessons from AI<br>engineering leadership"
SEED = 5
# Calm ambient bell, E minor i–VI–III–VII
MUSIC = {"bpm": 72, "chords": [[52, 55, 59, 64], [48, 52, 55, 60], [55, 59, 62, 67], [50, 54, 57, 62]],
         "voice": "bell", "pattern": [0, None, 2, None, 3, None, 1, None], "step": 0.5, "pad": 0.18, "bass": 0.08, "lead": 0.07, "hats": 0, "tick": 880}

T = '<svg width="60" height="60" viewBox="0 0 52 52" style="flex-shrink:0"><circle cx="26" cy="26" r="26" fill="#16A34A"/><path d="M15 27l7 7 15-16" fill="none" stroke="#fff" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/></svg>'

def node(n, t, d, at, hi=False):
    tg = '<span class="tag">CATCHES FAILURES</span>' if hi else ""
    return (f'<div class="tile a" data-t="{at}" style="padding:12px 28px;margin:0 0 10px 0"><span class="n">{n}</span>'
            f'<span>{tg}<span class="t" style="font-size:36px">{t}</span><span class="d" style="font-size:26px">{d}</span></span></div>')

SCENES = [
 {"dur": 5.0, "html": """
  <div class="kick a" data-t="0">For students</div>
  <h1 class="a" data-t="0.25">Your LLM demo is 1 box.</h1>
  <h1 class="a blue" data-t="1.1">Production is 7.</h1>
  <p class="body a" data-t="2.1">The model is the brilliant part. The boxes around it decide whether it quietly stumbles.</p>"""},
 {"dur": 10.0, "html": '<h2 class="a" data-t="0.1" style="font-size:68px">Inside a production LLM app</h2>' + "".join([
    node("1", "App / API", "Where the request comes in", 0.6),
    node("2", "Input guardrails", "Block unsafe or off-topic requests", 1.4, hi=True),
    node("3", "Retrieval", "Fetch your own data (vector database)", 2.2),
    node("4", "The LLM", "Generate the answer", 3.0),
    node("5", "Output checks", "Format, facts, policy", 3.8, hi=True),
    node("6", "Logging + evaluation", "Every answer scored and stored", 4.6, hi=True),
    node("7", "Human fallback", "Hand over when confidence is low", 5.4, hi=True)])},
 {"dur": 5.0, "light": True, "html": """
  <p class="q a" data-t="0.1">“</p>
  <h2 class="a" data-t="0.35" style="font-size:110px">The model is one box. <span class="blue">The system</span> is the product.</h2>"""},
 {"dur": 5.5, "html": """
  <h2 class="a" data-t="0.1">Demo thinking vs <span class="blue">system thinking</span></h2>
  <div class="cols a" data-t="0.9">
    <div class="col"><h3 style="color:#9AA3AF">Demo</h3><p>Pick the best model</p><p>Tune the prompt</p><p>It worked once</p></div>
    <div class="col" style="border:3px solid #5AA9FF;background:#12202F"><h3 class="blue">System</h3><p>Design the checks</p><p>Measure every answer</p><p>Plan for failure</p></div>
  </div>"""},
 {"dur": 6.5, "html": f"""
  <h2 class="a" data-t="0.1">Add to your next project</h2>
  <div class="tile a" data-t="0.7">{T}<span class="t">One input guardrail</span></div>
  <div class="tile a" data-t="1.3">{T}<span class="t">One automatic output check</span></div>
  <div class="tile a" data-t="1.9">{T}<span class="t">A log you actually review</span></div>
  <div class="pill a" data-t="2.8">Follow Vevek Pandian</div>"""},
]
