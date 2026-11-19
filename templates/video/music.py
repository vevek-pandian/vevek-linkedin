"""Original synthesized soundtrack: calm tech pad + soft pulse + subtle cues at scene changes and number reveals."""
import numpy as np, wave

SR = 48000
D = 32.0
t = np.arange(int(SR * D)) / SR
out = np.zeros((len(t), 2))

def note(f): return 440.0 * 2 ** ((f - 69) / 12)

def env_adsr(n, a, r):
    e = np.ones(n)
    na, nr = int(a * SR), int(r * SR)
    e[:na] = np.linspace(0, 1, na)
    e[-nr:] *= np.linspace(1, 0, nr)
    return e

def add(sig, start, gain=1.0, pan=0.0):
    i = int(start * SR)
    j = min(len(out), i + len(sig))
    sig = sig[: j - i] * gain
    out[i:j, 0] += sig * (1 - pan) * 0.5 * 2 ** 0.5
    out[i:j, 1] += sig * (1 + pan) * 0.5 * 2 ** 0.5

# Chord progression (Am9 - Fmaj7 - Cmaj7 - G6), 4 s per chord, loops
chords = [[57, 64, 67, 71, 74], [53, 60, 64, 69, 72], [48, 55, 59, 64, 67], [55, 59, 62, 64, 71]]
CH = 4.0
for k in range(int(D / CH) + 1):
    ch = chords[k % 4]
    n = int((CH + 1.5) * SR)
    tt = np.arange(n) / SR
    e = env_adsr(n, 1.2, 1.8)
    pad = np.zeros(n)
    for m in ch:
        f = note(m)
        for det in (-0.12, 0.0, 0.12):
            pad += np.sin(2 * np.pi * f * (1 + det / 100) * tt + np.random.rand() * 6.28)
    pad *= e / (len(ch) * 3)
    add(pad, k * CH, gain=0.22, pan=0.0)
    # Bass root
    fb = note(ch[0] - 12)
    bass = np.sin(2 * np.pi * fb * tt) * env_adsr(n, 0.4, 1.5)
    add(bass, k * CH, gain=0.10)

# Soft pulse (plucky arpeggio) every 0.5 s, starting after the hook line lands
for k in range(int(1.0 * 2), int((D - 1.5) * 2)):
    st = k * 0.5
    ch = chords[int(st // CH) % 4]
    m = ch[[1, 2, 3, 4, 3, 2][k % 6]] + 12
    n = int(0.45 * SR)
    tt = np.arange(n) / SR
    s = (np.sin(2 * np.pi * note(m) * tt) + 0.3 * np.sin(2 * np.pi * 2 * note(m) * tt)) * np.exp(-tt * 9)
    add(s, st, gain=0.045, pan=0.35 if k % 2 else -0.35)

# Scene-change whoosh (filtered noise swell)
def whoosh(length=0.7):
    n = int(length * SR)
    w = np.random.randn(n)
    k = np.ones(40) / 40
    w = np.convolve(w, k, mode="same")
    e = np.sin(np.linspace(0, np.pi, n)) ** 2
    return w * e
for s in [4.6, 10.4, 15.6, 21.4, 26.4]:
    add(whoosh(), s - 0.35, gain=0.12)

# Soft "tick" when numbers start counting / bars grow
def tick(f=1400):
    n = int(0.12 * SR)
    tt = np.arange(n) / SR
    return np.sin(2 * np.pi * f * tt) * np.exp(-tt * 40)
for s, f in [(5.2, 1320), (6.9, 990), (11.6, 1320), (12.5, 990), (16.8, 1320), (17.6, 990), (18.7, 1180),
             (27.1, 1180), (27.7, 1320), (28.3, 1480), (29.2, 1760)]:
    add(tick(f), s, gain=0.12)

# Low "impact" on the hook and the quote
def impact():
    n = int(1.2 * SR)
    tt = np.arange(n) / SR
    return np.sin(2 * np.pi * (55 + 30 * np.exp(-tt * 6)) * tt) * np.exp(-tt * 3.5)
for s in [0.25, 21.75]:
    add(impact(), s, gain=0.35)

# Master fade in/out, normalise to about -16 dBFS RMS with peak headroom
fade = np.ones(len(t))
fi, fo = int(0.6 * SR), int(2.0 * SR)
fade[:fi] = np.linspace(0, 1, fi)
fade[-fo:] = np.linspace(1, 0, fo)
out *= fade[:, None]
rms = np.sqrt(np.mean(out ** 2))
out *= (10 ** (-16 / 20)) / rms
peak = np.abs(out).max()
if peak > 0.89: out *= 0.89 / peak

pcm = (out * 32767).astype(np.int16)
with wave.open("/home/claude/video/out/soundtrack.wav", "wb") as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes(pcm.tobytes())
print("ok", round(20 * np.log10(np.abs(out).max()), 1), "dBFS peak")
