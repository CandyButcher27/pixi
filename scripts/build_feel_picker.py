"""Build a local page for tagging gallery screenshots by feel (luxurious, clean, animated, playful).

  uv run python scripts/build_feel_picker.py

Candidates are pre-sorted by the galleries' own tags. Writes research/harvest/galleries/picker.html;
the page saves the picks as feels.json to the browser's download folder.
"""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GAL = ROOT / "research/harvest/galleries"
PER_FEEL = 30

FEELS = {
    "luxurious": {"fashion", "serif", "photographic", "photography", "photo", "architecture", "property", "greyscale",
                  "architecture-and-industrial-design", "black", "slideshow", "fullscreen", "video"},
    "clean": {"clean", "minimal", "whitespace", "simple", "white", "light", "grid", "professional"},
    "animated": {"3d", "webgl", "gsap", "interactive", "interaction", "experimental", "motion", "microinteractions",
                 "parallax", "storytelling", "preloader", "cursor", "transitions", "scrolling-behaviour"},
    "playful": {"colorful", "colour", "illustration", "art & illustration", "design-and-illustration", "yellow", "red",
                "green", "blue", "brutalist", "music"},
}

SEEDS = [
    {"label": "NAVIK spec-first", "img": "file:///C:/Users/sriva/Desktop/Hackathons/SIH/pixi-v2/pixi-shot.png", "feels": ["clean"]},
    {"label": "NAVIK React + Astryx", "img": "file:///C:/Users/sriva/Desktop/Hackathons/SIH/pixi-react/dist/pixi-shot.png", "feels": ["clean"]},
    {"label": "CoFounders spec-first", "img": "file:///C:/Users/sriva/Desktop/Hackathons/Neurax-CoFounders/pixi-v2/pixi-shot.png", "feels": ["animated"]},
    {"label": "Foundry prompt rules", "img": "file:///C:/Users/sriva/Desktop/Hackathons/Foundry-BuildContext/pixi/pixi-shot.png", "feels": ["luxurious"]},
]


def host(url):
    return url.split("//", 1)[-1].split("/", 1)[0]


def main():
    shots = {p.stem: p.name for p in (GAL / "screens").glob("*.png")}
    sites = []
    for line in (GAL / "sites_merged.jsonl").read_text(encoding="utf-8").splitlines():
        r = json.loads(line)
        h = host(r["url"])
        shot = shots.get(h) or shots.get(h.removeprefix("www."))
        if not shot:
            continue
        tags = sorted({t.split(":", 1)[-1].lower() for t in r["tags"]})
        score = {f: len(set(tags) & ks) for f, ks in FEELS.items()}
        sites.append({"url": r["url"], "host": h, "shot": "screens/" + shot, "tags": tags, "score": score})
    used, groups = set(), {}
    for f in FEELS:
        ranked = sorted((s for s in sites if s["score"][f] >= 2 and s["host"] not in used),
                        key=lambda s: (-s["score"][f], s["host"]))[:PER_FEEL]
        used |= {s["host"] for s in ranked}
        groups[f] = ranked
    groups["other"] = sorted((s for s in sites if s["host"] not in used), key=lambda s: s["host"])
    data = {"feels": list(FEELS), "groups": groups, "seeds": SEEDS}
    tpl = (ROOT / "scripts/feel_picker.html").read_text(encoding="utf-8")
    (GAL / "picker.html").write_text(tpl.replace("/*DATA*/null", json.dumps(data)), encoding="utf-8")
    print({k: len(v) for k, v in groups.items()}, "->", GAL / "picker.html")


if __name__ == "__main__":
    main()
