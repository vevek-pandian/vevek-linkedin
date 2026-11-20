import os
REPO = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
TK = os.path.join(REPO, "toolkit")
"""Jagged Intelligence video engine: spec -> HTML -> scene MP4s -> soundtrack -> final MP4.
Usage: python3 engine.py <spec_module> [stills|full]"""
import asyncio, importlib, os, re, subprocess, sys, wave
import numpy as np
from playwright.async_api import async_playwright

FPS = 30
FONTS = os.path.join(TK, "assets", "fonts")
PHOTO = os.path.join(TK, "assets", "photo.jpg")
ZIG = '<svg width="56" height="28" viewBox="0 0 44 22"><polyline points="2,18 10,4 18,16 26,6 34,14 42,3" fill="none" stroke="currentColor" stroke-width="3.5" stroke-linejoin="round" stroke-linecap="round"/></svg>'
TICK = '<svg width="60" height="60" viewBox="0 0 52 52" style="flex-shrink:0"><circle cx="26" cy="26" r="26" fill="#16A34A"/><path d="M15 27l7 7 15-16" fill="none" stroke="#fff" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/></svg>'

CSS = """
*{box-sizing:border-box;margin:0}
html,body{width:1080px;height:1920px;overflow:hidden;background:#0D1117;font-family:IN,sans-serif;color:#F3F1EA}
#bgl{position:absolute;inset:0;background:#F4F2EC;opacity:0}
.scene{position:absolute;left:96px;right:96px;top:290px;bottom:320px;display:flex;flex-direction:column;justify-content:center;gap:40px;opacity:0}
.a{opacity:0}
.kick{font-family:SG;font-weight:600;font-size:34px;letter-spacing:.14em;text-transform:uppercase;color:#5AA9FF;display:flex;align-items:center;gap:16px}
h1{font-family:SG;font-weight:700;font-size:120px;line-height:1.0;letter-spacing:-.03em}
h2{font-family:SG;font-weight:700;font-size:88px;line-height:1.04;letter-spacing:-.025em}
.blue{color:#5AA9FF}
.light .blue{color:#1D5FBF}
.body{font-size:42px;line-height:1.4;color:#C9CED6}
.tile{display:flex;gap:28px;align-items:center;padding:30px 34px;border-radius:24px;background:#161C25;border:2px solid #252D39}
.tile .n{font-family:SG;font-weight:700;font-size:44px;color:#5AA9FF;min-width:64px}
.tile .t{font-family:SG;font-weight:600;font-size:42px;line-height:1.15;display:block}
.tile .d{font-size:30px;line-height:1.35;color:#B4BBC6;display:block;margin-top:6px}
.tile.hi{border:3px solid #5AA9FF;background:#12202F}
.tag{font-family:SG;font-weight:600;font-size:24px;letter-spacing:.12em;color:#5AA9FF;display:block;margin-bottom:6px}
.node{display:flex;align-items:center;gap:24px;padding:20px 30px;border-radius:20px;background:#161C25;border:2px solid #252D39}
.node .t{font-family:SG;font-weight:600;font-size:38px}
.node .d{font-size:27px;color:#9AA3AF;margin-left:auto;text-align:right}
.node.hi{border:3px solid #5AA9FF;background:#12202F}
.arrow{height:26px;display:flex;justify-content:center}
.cols{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:24px}
.col{padding:32px;border-radius:24px;background:#161C25;border:2px solid #252D39;display:flex;flex-direction:column;gap:20px}
.col h3{font-family:SG;font-weight:700;font-size:40px}
.col p{font-size:32px;line-height:1.35;color:#C9CED6}
.pill{display:flex;align-self:flex-start;padding:24px 40px;border-radius:999px;background:#5AA9FF;color:#0D1117;font-family:SG;font-weight:700;font-size:38px}
.light{color:#0D1117}
.light .body{color:#2B323C}
.q{font-family:SG;font-weight:700;font-size:240px;line-height:.5;height:120px;color:#1D5FBF}
#top{position:absolute;left:96px;right:96px;top:120px;display:flex;justify-content:space-between;align-items:center}
#prog{position:absolute;left:96px;top:205px;height:6px;width:0;background:#5AA9FF;border-radius:3px}
#progbg{position:absolute;left:96px;right:96px;top:205px;height:6px;background:#1F2630;border-radius:3px}
#foot{position:absolute;left:96px;right:96px;bottom:110px;display:flex;justify-content:space-between;align-items:center;padding-top:36px;border-top:2px solid #252D39}
#foot img{width:104px;height:104px;border-radius:52px;object-fit:cover;object-position:50% 22%;border:4px solid #5AA9FF}
.me{display:flex;align-items:center;gap:24px}
.me b{font-family:SG;font-weight:600;font-size:36px;display:block}
.me span{font-size:27px;opacity:.75;white-space:nowrap}
#src{font-size:24px;color:#9AA3AF;text-align:right;line-height:1.35}
"""

JS = """
const ease=x=>1-Math.pow(1-Math.min(Math.max(x,0),1),3);
const scenes=[...document.querySelectorAll('.scene')];
function render(t){
  document.getElementById('prog').style.width=(888*Math.min(t/D,1))+'px';
  let light=0;
  scenes.forEach((sc,i)=>{
    const a=+sc.dataset.a,b=+sc.dataset.b,lt=t-a;
    let o=0; if(t>=a&&t<b){o=Math.min(1,(b-t)/0.3); if(i>0)o=Math.min(o,lt/0.3);}
    sc.style.opacity=o; sc.style.display=o>0?'flex':'none';
    if(sc.classList.contains('light')&&o>0) light=o;
    if(o<=0) return;
    sc.querySelectorAll('[data-t]').forEach(e=>{const p=ease((lt-(+e.dataset.t))/0.55);e.style.opacity=p;e.style.transform=`translateY(${(1-p)*40}px)`;});
  });
  document.getElementById('bgl').style.opacity=light;
  const dk=light<0.5, c=(d,l)=>dk?d:l;
  const f=document.getElementById('foot');f.style.borderTopColor=c('#252D39','#D9D5CA');
  ['nm','ttl'].forEach(id=>document.getElementById(id).style.color=c('#F3F1EA','#0D1117'));
  document.getElementById('src').style.color=c('#9AA3AF','#5B6370');document.getElementById('tag').style.color=c('#9AA3AF','#5B6370');
  document.getElementById('kick').style.color=c('#5AA9FF','#1D5FBF');document.getElementById('prog').style.background=c('#5AA9FF','#1D5FBF');
  document.getElementById('progbg').style.background=c('#1F2630','#E3DFD3');f.querySelector('img').style.borderColor=c('#5AA9FF','#1D5FBF');
}
"""

def fonts():
    s = ""
    for w in (500, 600, 700): s += f"@font-face{{font-family:SG;font-weight:{w};src:url(file://{FONTS}/space-grotesk-latin-{w}-normal.woff2)}}"
    for w in (400, 500, 600): s += f"@font-face{{font-family:IN;font-weight:{w};src:url(file://{FONTS}/inter-latin-{w}-normal.woff2)}}"
    return s

def build_html(spec):
    t = 0.0; scenes = []
    for sc in spec.SCENES:
        a, b = t, t + sc["dur"]; t = b
        cls = "scene light" if sc.get("light") else "scene"
        scenes.append(f'<div class="{cls}" data-a="{a:.2f}" data-b="{b:.2f}">{sc["html"]}</div>')
    D = t
    html = f"""<!doctype html><html><head><meta charset="utf-8"><style>{fonts()}{CSS}</style></head><body>
<div id="bgl"></div>
<div id="top"><div class="kick" id="kick">{ZIG}<span>Jagged Intelligence</span></div><span id="tag" style="font-size:30px;font-weight:500">{spec.TAG}</span></div>
<div id="progbg"></div><div id="prog"></div>
{''.join(scenes)}
<div id="foot"><div class="me"><img src="file://{PHOTO}"><div><b id="nm">Vevek Pandian</b><span id="ttl">AI Engineering Leader · UAE</span></div></div><span id="src">{spec.SOURCE}</span></div>
<script>const D={D:.2f};{JS}window.render=render;</script></body></html>"""
    return html, D

def cues(spec):
    """Scene starts (whoosh) and element entries (ticks), absolute seconds."""
    t = 0.0; wh = []; tk = []
    for i, sc in enumerate(spec.SCENES):
        if i > 0: wh.append(t)
        for m in re.finditer(r'data-t="([\d.]+)"', sc["html"]):
            v = float(m.group(1))
            if v > 0.3: tk.append(t + v)
        t += sc["dur"]
    return wh, sorted(set(round(x, 2) for x in tk)), t

# ---------- music ----------
SR = 48000
def midi(m): return 440.0 * 2 ** ((m - 69) / 12)

def voice(kind, f, n):
    tt = np.arange(n) / SR
    if kind == "piano":
        s = sum(np.sin(2*np.pi*f*h*tt)/h**1.3 for h in (1, 2, 3, 4)) * np.exp(-tt*3.2)
    elif kind == "rhodes":
        s = (np.sin(2*np.pi*f*tt) + 0.25*np.sin(2*np.pi*f*2*tt)) * np.exp(-tt*2.2) * (1 + 0.25*np.sin(2*np.pi*4.5*tt))
    elif kind == "marimba":
        s = (np.sin(2*np.pi*f*tt) + 0.35*np.sin(2*np.pi*f*4*tt)*np.exp(-tt*18)) * np.exp(-tt*7)
    elif kind == "bell":
        s = (np.sin(2*np.pi*f*tt) + 0.4*np.sin(2*np.pi*f*2.76*tt)*np.exp(-tt*3) + 0.2*np.sin(2*np.pi*f*5.4*tt)*np.exp(-tt*6)) * np.exp(-tt*1.6)
    else:
        s = np.sin(2*np.pi*f*tt) * np.exp(-tt*4)
    a = int(0.004*SR); s[:a] *= np.linspace(0, 1, a)
    return s

def music(style, wh, tk, D, path, seed=1):
    rng = np.random.default_rng(seed)
    n = int(SR * D); out = np.zeros((n, 2))
    def add(sig, st, g=1.0, pan=0.0):
        i = int(st*SR); j = min(n, i+len(sig))
        if j <= i: return
        s = sig[:j-i]*g
        out[i:j, 0] += s*(1-pan)*0.707*1.414/2*2; out[i:j, 1] += s*(1+pan)*0.707*1.414/2*2
    beat = 60.0/style["bpm"]; bar = beat*4
    k = 0; st = 0.0
    while st < D:
        ch = style["chords"][k % len(style["chords"])]
        m = int((bar+2.0)*SR); tt = np.arange(m)/SR
        env = np.minimum(1, tt/0.9) * np.minimum(1, np.maximum(0, (bar+2.0-tt)/1.6))
        pad = sum(np.sin(2*np.pi*midi(x)*(1+d)*tt + rng.random()*6.28) for x in ch for d in (-0.0011, 0, 0.0011))
        add(pad*env/(len(ch)*3), st, style["pad"])
        add(np.sin(2*np.pi*midi(ch[0]-12)*tt)*env, st, style["bass"])
        # melodic pattern
        for bi, step in enumerate(style["pattern"]):
            if step is None: continue
            tn = st + bi*beat*style["step"]
            if tn >= D - 1.0 or tn >= st + bar: continue
            note = ch[step % len(ch)] + 12*(1 + step//len(ch))
            add(voice(style["voice"], midi(note), int(1.6*SR)), tn, style["lead"], pan=(0.3 if bi % 2 else -0.3))
        if style.get("hats"):
            for h in range(int(bar/(beat/2))):
                th = st + h*beat/2
                if th >= D: break
                hn = int(0.05*SR); hs = rng.standard_normal(hn)*np.exp(-np.arange(hn)/SR*90)
                add(np.diff(hs, prepend=0), th, style["hats"]*(1.0 if h % 2 else 0.6), pan=0.2)
        k += 1; st += bar
    for w in wh:
        m = int(0.7*SR); x = np.convolve(rng.standard_normal(m), np.ones(40)/40, mode="same")*np.sin(np.linspace(0, np.pi, m))**2
        add(x, w-0.35, 0.10)
    for t in tk:
        m = int(0.12*SR); tt = np.arange(m)/SR
        add(np.sin(2*np.pi*style["tick"]*tt)*np.exp(-tt*40), t, 0.08)
    m = int(1.2*SR); tt = np.arange(m)/SR
    add(np.sin(2*np.pi*(55+30*np.exp(-tt*6))*tt)*np.exp(-tt*3.5), 0.25, 0.3)
    fade = np.ones(n); fi, fo = int(0.6*SR), int(2.0*SR)
    fade[:fi] = np.linspace(0, 1, fi); fade[-fo:] = np.linspace(1, 0, fo)
    out *= fade[:, None]
    out *= (10**(-16/20))/np.sqrt(np.mean(out**2))
    pk = np.abs(out).max()
    if pk > 0.89: out *= 0.89/pk
    with wave.open(path, "wb") as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes((out*32767).astype(np.int16).tobytes())

async def render(spec, mode):
    work = os.path.join(REPO, "build", spec.NAME); os.makedirs(work, exist_ok=True)
    html, D = build_html(spec)
    open(f"{work}/video.html", "w").write(html)
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={"width": 1080, "height": 1920}, device_scale_factor=1)
        await pg.goto(f"file://{work}/video.html"); await pg.evaluate("document.fonts.ready"); await pg.wait_for_timeout(400)
        if mode == "stills":
            t = 0.0; shots = []
            for sc in spec.SCENES:
                t += sc["dur"]; shots.append(t - 0.45)
            for i, s in enumerate(shots):
                await pg.evaluate(f"render({s})"); await pg.screenshot(path=f"{work}/still_{i}.jpg", type="jpeg", quality=80)
            await b.close(); return D
        t = 0.0; files = []
        for i, sc in enumerate(spec.SCENES):
            a, z = t, t + sc["dur"]; t = z
            tmp, fin = f"{work}/s{i}.tmp.mp4", f"{work}/s{i}.mp4"
            ff = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "image2pipe", "-framerate", str(FPS), "-c:v", "mjpeg", "-i", "-",
                                   "-c:v", "libx264", "-preset", "veryfast", "-crf", "18", "-pix_fmt", "yuv420p", "-r", str(FPS), tmp], stdin=subprocess.PIPE)
            for k in range(round((z - a) * FPS)):
                await pg.evaluate(f"render({a + k / FPS})"); ff.stdin.write(await pg.screenshot(type="jpeg", quality=92))
            ff.stdin.close()
            if ff.wait() == 0: os.replace(tmp, fin)
            files.append(fin)
        await b.close()
    open(f"{work}/list.txt", "w").write("".join(f"file '{f}'\n" for f in files))
    wh, tk, D = cues(spec)
    music(spec.MUSIC, wh, tk, D, f"{work}/soundtrack.wav", seed=spec.SEED)
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", f"{work}/list.txt", "-c", "copy", f"{work}/joined.mp4"], check=True)
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", f"{work}/joined.mp4", "-i", f"{work}/soundtrack.wav", "-map", "0:v", "-map", "1:a",
                    "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-shortest", "-movflags", "+faststart", os.path.join(REPO, "videos", spec.NAME + ".mp4")], check=True)
    return D

if __name__ == "__main__":
    sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "specs"))
    spec = importlib.import_module(sys.argv[1])
    D = asyncio.run(render(spec, sys.argv[2] if len(sys.argv) > 2 else "full"))
    print("duration", round(D, 2))
