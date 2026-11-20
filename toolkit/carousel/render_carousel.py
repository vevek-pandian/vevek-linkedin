"""Render a carousel folder of slide HTML files (1.html, 2.html, ...) at 1080x1350 into one PDF.
Usage: python3 render_carousel.py <slides_dir> <out.pdf>
Slides reference fonts and photo relative to toolkit/ (see example/)."""
import sys, os, glob, asyncio
from playwright.async_api import async_playwright
from pypdf import PdfWriter, PdfReader
src, out = sys.argv[1], sys.argv[2]
files = sorted(glob.glob(os.path.join(src, "*.html")), key=lambda f: int(os.path.basename(f).split(".")[0]))
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(); pg = await b.new_page(viewport={"width": 1080, "height": 1350})
        w = PdfWriter()
        for f in files:
            await pg.goto("file://" + os.path.abspath(f)); await pg.evaluate("document.fonts.ready"); await pg.wait_for_timeout(300)
            tmp = f[:-5] + ".pdf"
            await pg.pdf(path=tmp, width="1080px", height="1350px", print_background=True, margin={"top": "0", "bottom": "0", "left": "0", "right": "0"})
            await pg.screenshot(path=f[:-5] + ".png"); w.add_page(PdfReader(tmp).pages[0])
        w.write(out); await b.close()
asyncio.run(main())
print("pages", len(files), "->", out)
