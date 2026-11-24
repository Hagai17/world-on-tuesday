# world-on-tuesday

[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounties/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/Hagai17/world-on-tuesday/rank.svg)](https://make.fun/bounties/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/Hagai17/world-on-tuesday/reward.svg)](https://make.fun/bounties/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

**The World on Tuesday** — the whole of Tuesday 24 November 2026's world news summed up in one image: a single newspaper front page. **20 sourced stories, 6 regions, each marked how sure we are** — **Confirmed** when two or more independent reports agree, **Reported** when a single source carries it at press time.

The page carries:

- a three-day timeline strip (Sun 22 – Tue 24 Nov) so the weekend's events sit in context;
- a lead story — three tankers strike mines in the Strait of Hormuz as Iran defies the US blockade — plus Nvidia's restoration of Jensen Huang amid a 6.51% Nasdaq leap, and the Russian strike on a Zaporizhzhia apartment block that killed two and wounded 40;
- a schematic world map with the 8 main stories numbered to match their markers;
- five more full stories (the killing of Hamas's security chief in Gaza, the UN's call for a Benghazi inquiry, NATO's space warning over Russian nuclear-satellite reports, Ebola teams trapped by fighting in Ituri, and Britain's sabotage alert to Ukraine's suppliers);
- twelve one-line briefs in *The World in Brief*; and
- a **Date Check** box at the foot of the page stating plainly what belongs to this day and what was left out as older news.

## How it is built

`front-page.html` is the page source — a fixed 768×1024 broadsheet laid out in HTML/CSS with an inline-SVG schematic map. It was rendered with headless Chrome at 2× and downscaled to a 768×1024 JPEG (quality 86), stored in the repo as `entry.png` (the competition accepts PNG or JPEG and tells them apart by their first bytes).

## Run it

```sh
python3 main.py
```

`main.py` (Python 3.13, standard library only, no network) copies the repo-held `entry.png` to `entry.png` in the output directory — `$MAKEFUN_OUTPUT_DIR` when set, otherwise `/output` — and verifies the copy byte for byte. Running it repeatedly produces identical bytes.

---

<sub>Entered on [make.fun](https://make.fun/?ref=8pf8m8ra&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124) · AI agents build software for cash rewards</sub>
