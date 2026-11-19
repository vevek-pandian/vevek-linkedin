import asyncio, subprocess, sys, os
from playwright.async_api import async_playwright

FPS = 30
SCENES = [x for x in [("s1", 0, 4.6), ("s2", 4.6, 10.4), ("s3", 10.4, 15.6), ("s4", 15.6, 21.4), ("s5", 21.4, 26.4), ("s6", 26.4, 32)] if (len(sys.argv)<3 or x[0] in sys.argv[2].split(","))]
OUT = "/home/claude/video/out"
os.makedirs(OUT, exist_ok=True)
mode = sys.argv[1] if len(sys.argv) > 1 else "full"

async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={"width": 1080, "height": 1920}, device_scale_factor=1)
        await pg.goto("file:///home/claude/video/video.html")
        await pg.evaluate("document.fonts.ready")
        await pg.wait_for_timeout(500)
        if mode == "stills":
            for t in [3.8, 8.6, 14.5, 20.8, 25.0, 31.0]:
                await pg.evaluate(f"render({t})")
                await pg.screenshot(path=f"{OUT}/still_{t}.jpg", type="jpeg", quality=85)
            await b.close(); return
        for name, a, z in SCENES:
            n = round((z - a) * FPS)
            tmp = f"{OUT}/{name}.tmp.mp4"
            ff = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "image2pipe", "-framerate", str(FPS), "-c:v", "mjpeg", "-i", "-",
                                   "-c:v", "libx264", "-preset", "veryfast", "-crf", "18", "-pix_fmt", "yuv420p", "-r", str(FPS), tmp], stdin=subprocess.PIPE)
            for i in range(n):
                await pg.evaluate(f"render({a + i / FPS})")
                ff.stdin.write(await pg.screenshot(type="jpeg", quality=92))
            ff.stdin.close()
            if ff.wait() == 0:
                os.replace(tmp, f"{OUT}/{name}.mp4")
            print(name, "done", flush=True)
        await b.close()

asyncio.run(main())
