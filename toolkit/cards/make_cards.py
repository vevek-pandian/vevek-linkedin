import os
REPO = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
TK = os.path.join(REPO, "toolkit")
import asyncio, os
from playwright.async_api import async_playwright

FONTS = os.path.join(TK, "assets", "fonts")
IMG = os.path.join(TK, "assets", "photo.jpg")
OUT = os.path.join(REPO, "images")
os.makedirs(OUT, exist_ok=True)

ff = ""
for w in (500, 600, 700):
    ff += f"@font-face{{font-family:'SG';font-weight:{w};src:url(file://{FONTS}/space-grotesk-latin-{w}-normal.woff2)}}"
for w in (400, 500, 600):
    ff += f"@font-face{{font-family:'IN';font-weight:{w};src:url(file://{FONTS}/inter-latin-{w}-normal.woff2)}}"

BASE = ff + """
*{box-sizing:border-box}
html,body{margin:0;width:1080px;height:1350px}
.card{width:1080px;height:1350px;padding:88px 96px 80px;display:flex;flex-direction:column;justify-content:space-between;font-family:'IN',sans-serif}
.dark{background:#0D1117;color:#F3F1EA}
.light{background:#F4F2EC;color:#0D1117}
.sg{font-family:'SG',sans-serif}
.top{display:flex;justify-content:space-between;align-items:center}
.kicker{display:flex;align-items:center;gap:14px;font-family:'SG';font-weight:600;font-size:26px;letter-spacing:.14em;text-transform:uppercase}
.dark .kicker{color:#5AA9FF}.light .kicker{color:#1D5FBF}
.tag{font-size:24px;font-weight:500}
.dark .tag{color:#9AA3AF}.light .tag{color:#5B6370}
.foot{display:flex;justify-content:space-between;align-items:center;padding-top:32px}
.dark .foot{border-top:2px solid #252D39}.light .foot{border-top:2px solid #D9D5CA}
.me{display:flex;align-items:center;gap:20px}
.me img{width:84px;height:84px;border-radius:42px;object-fit:cover;object-position:50% 22%;border:3px solid #5AA9FF}
.light .me img{border-color:#1D5FBF}
.me b{font-family:'SG';font-weight:600;font-size:28px;display:block}
.me span{font-size:21px;opacity:.75;white-space:nowrap}
.src{font-size:21px}
.dark .src{color:#9AA3AF}.light .src{color:#5B6370}
h1{margin:0;font-family:'SG';font-weight:700;letter-spacing:-.03em;line-height:1.0}
.blue{color:#5AA9FF}.light .blue{color:#1D5FBF}
p{margin:0}
"""

ZIG = '<svg width="44" height="22" viewBox="0 0 44 22"><polyline points="2,18 10,4 18,16 26,6 34,14 42,3" fill="none" stroke="currentColor" stroke-width="3.5" stroke-linejoin="round" stroke-linecap="round"/></svg>'

def card(theme, kicker, body, src, tag="Jagged Intelligence"):
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{BASE}{EXTRA}</style></head><body>
<div class="card {theme}">
  <div class="top"><div class="kicker">{ZIG}<span>{kicker}</span></div><span class="tag">{tag}</span></div>
  {body}
  <div class="foot"><div class="me"><img src="file://{IMG}"><div><b>Vevek Pandian</b><span>AI Engineering Leader · UAE</span></div></div><span class="src">{src}</span></div>
</div></body></html>"""

EXTRA = """
.chips{display:flex;flex-wrap:wrap;gap:16px}
.chip{padding:18px 28px;border-radius:999px;background:#161C25;border:2px solid #2A3341;font-family:'SG';font-weight:600;font-size:32px}
.grid2{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:22px}
.tile{padding:34px;border-radius:24px;display:flex;flex-direction:column;gap:12px}
.light .tile{background:#fff;border:2px solid #E3DFD3}
.dark .tile{background:#161C25;border:2px solid #252D39}
.tile.hi{border:3px solid #1D5FBF}
.dark .tile.hi{border-color:#5AA9FF;background:#12202F}
.tile .n{font-family:'SG';font-weight:600;font-size:22px;letter-spacing:.12em;color:#5B6370}
.dark .tile .n{color:#9AA3AF}
.tile.hi .n{color:#1D5FBF}.dark .tile.hi .n{color:#5AA9FF}
.tile .t{font-family:'SG';font-weight:700;font-size:50px;letter-spacing:-.015em}
.tile .d{font-size:27px;line-height:1.4;color:#3E4652}
.dark .tile .d{color:#C9CED6}
.row3{display:flex;flex-direction:column;gap:20px}
.bar{display:flex;flex-direction:column;gap:14px}
.bar .lab{display:flex;justify-content:space-between;font-family:'SG';font-weight:600;font-size:32px}
.track{height:64px;border-radius:16px;background:#161C25;border:2px solid #252D39;overflow:hidden}
.fill{height:100%;border-radius:14px}
"""

cards = {}

cards["01-banks-ai-agent-liability"] = card("dark", "Agentic AI · Banking", """
<div style="display:flex;flex-direction:column;gap:40px">
  <h1 style="font-size:150px">Your agent.<br><span class="blue">Your loss.</span></h1>
  <p style="font-size:38px;line-height:1.4;color:#C9CED6;max-width:860px">Big US banks now make customers responsible for what third-party AI agents do in their accounts. Even after a hack.</p>
</div>
<div class="chips"><span class="chip">Citi</span><span class="chip">PNC</span><span class="chip">Citizens</span><span class="chip">Wells Fargo</span><span class="chip">JPMorgan</span></div>
""", "Source: TechCrunch, Nov 2026")

cards["02-see-verify-control"] = card("light", "AI governance", """
<div style="display:flex;flex-direction:column;gap:28px">
  <p class="sg" style="font-weight:700;font-size:150px;line-height:.6;height:76px;color:#1D5FBF">“</p>
  <h1 style="font-size:84px;line-height:1.05">Greater AI autonomy requires greater transparency.</h1>
  <p style="font-size:30px;color:#5B6370">The idea behind Microsoft's AI Transparency Initiative, with 40+ organisations.</p>
</div>
<div class="row3">
  <div class="tile" style="flex-direction:row;align-items:center;gap:30px"><span class="t" style="min-width:250px">See</span><span class="d">What the agent was allowed to do, and what it did</span></div>
  <div class="tile hi" style="flex-direction:row;align-items:center;gap:30px"><span class="t" style="min-width:250px;color:#1D5FBF">Verify</span><span class="d">Check its reports against independent records. <b>Most teams skip this.</b></span></div>
  <div class="tile" style="flex-direction:row;align-items:center;gap:30px"><span class="t" style="min-width:250px">Control</span><span class="d">Enforce policy before any consequential action</span></div>
</div>
""", "Source: Microsoft, Ignite 2026")

cards["03-palo-alto-applied-compute"] = card("dark", "Enterprise AI", """
<div style="display:flex;flex-direction:column;gap:24px">
  <h1 class="blue" style="font-size:300px;letter-spacing:-.05em;line-height:.9">$4.5B</h1>
  <p class="sg" style="font-weight:600;font-size:56px;line-height:1.12;max-width:880px">to help enterprises run and secure their own AI models.</p>
</div>
<div class="tile" style="gap:18px">
  <span class="d" style="font-size:34px;line-height:1.4;color:#F3F1EA">"Every enterprise is going to run a mix of open and closed models, and every one of those models needs to be secured."</span>
  <span class="n">NIKESH ARORA · CEO, PALO ALTO NETWORKS</span>
</div>
""", "Source: Palo Alto Networks")

cards["04-astra-hidden-failures"] = card("dark", "Jagged intelligence", """
<div style="display:flex;flex-direction:column;gap:30px">
  <h1 style="font-size:96px;line-height:1.02">Smarter model.<br><span class="blue">Twice as likely to hide a failure.</span></h1>
  <p style="font-size:32px;line-height:1.4;color:#B4BBC6">Coding tasks where the model didn't mention a known blocker, in OpenAI's own tests.</p>
</div>
<div style="display:flex;flex-direction:column;gap:40px">
  <div class="bar"><div class="lab"><span>GPT-6 Astra</span><span>11.09%</span></div><div class="track"><div class="fill" style="width:44%;background:#3A4351"></div></div></div>
  <div class="bar"><div class="lab"><span>GPT-6.2 Astra</span><span class="blue">22.28%</span></div><div class="track"><div class="fill" style="width:88%;background:#5AA9FF"></div></div></div>
</div>
""", "Source: OpenAI system card")

cards["05-capability-vs-accountability"] = card("light", "Engineering leadership", """
<div style="display:flex;flex-direction:column;gap:30px">
  <h1 style="font-size:92px;line-height:1.04">Capability gets you the demo.<br><span class="blue">Accountability gets you to production.</span></h1>
</div>
<div class="grid2">
  <div class="tile"><span class="n">01</span><span class="t">Identity</span><span class="d">Every agent gets its own scoped access</span></div>
  <div class="tile"><span class="n">02</span><span class="t">Evidence</span><span class="d">Every action logged outside the agent</span></div>
  <div class="tile"><span class="n">03</span><span class="t">Approval</span><span class="d">A human signs off on anything irreversible</span></div>
  <div class="tile"><span class="n">04</span><span class="t">Ownership</span><span class="d">One named person per agent</span></div>
</div>
""", "4 checks for every AI agent")

async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={"width": 1080, "height": 1350}, device_scale_factor=1)
        for name, html in cards.items():
            f = os.path.join(REPO, "build", name + ".html")
            open(f, "w").write(html)
            await pg.goto("file://" + f)
            await pg.evaluate("document.fonts.ready")
            await pg.wait_for_timeout(300)
            await pg.screenshot(path=f"{OUT}/{name}.png")
        await b.close()
asyncio.run(main())
print(sorted(os.listdir(OUT)))
