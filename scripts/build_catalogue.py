"""Render a pixi progression catalogue: one row per project, one column per pixi stage.

  uv run python scripts/build_catalogue.py <catalogue.json>

Paths in the JSON are relative to the folder above the JSON's folder (the projects root).
Writes index.html next to the JSON and lists any file the JSON names that does not exist.
"""

import json
import sys
from html import escape
from pathlib import Path

CSS = """
:root{--bg:#f3f2ee;--ink:#151515;--mute:#6b6b66;--line:#d6d4cc;--card:#fff;--acc:#1f5eff}
@media (prefers-color-scheme:dark){:root{--bg:#141414;--ink:#ecebe6;--mute:#9a9992;--line:#333;--card:#1d1d1d;--acc:#7da2ff}}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);font:15px/1.45 "Helvetica Neue",Helvetica,Arial,sans-serif}
a{color:inherit}.wrap{max-width:1600px;margin:0 auto;padding:28px 24px 60px}
h1{font-size:34px;letter-spacing:-.02em;margin:0 0 4px}.sub{color:var(--mute);margin:0 0 26px;max-width:820px}
.grid{display:grid;grid-template-columns:170px repeat(var(--n),minmax(230px,1fr));gap:14px;align-items:start}
.scroll{overflow-x:auto;padding-bottom:8px}
.stage{border-top:3px solid var(--ink);padding-top:8px}.stage b{display:block;font-size:17px}
.stage time{font:12px Menlo,Consolas,monospace;color:var(--mute)}.stage p{margin:6px 0 0;font-size:13px;color:var(--mute)}
.proj{border-top:1px solid var(--line);padding-top:10px}.proj b{display:block;font-size:19px}.proj small{color:var(--mute)}
.cell{background:var(--card);border:1px solid var(--line)}
.cell .th{display:block;height:300px;overflow:hidden;border-bottom:1px solid var(--line)}
.cell img{width:100%;height:100%;object-fit:cover;object-position:top;display:block}
.cell .meta{padding:9px 10px 11px;font-size:12.5px}
.cell .links{display:flex;gap:10px;flex-wrap:wrap;margin-bottom:4px}.cell .links a{color:var(--acc)}
.cell .k{font:11px Menlo,Consolas,monospace;color:var(--mute)}
.empty{border:1px dashed var(--line);height:300px;display:grid;place-items:center;color:var(--mute);font-size:13px}
.more{font:11px Menlo,Consolas,monospace;color:var(--mute)}
@media (max-width:700px){.grid{grid-template-columns:120px repeat(var(--n),240px)}}
"""


def cell(entry, root_rel):
    if not entry:
        return '<div class="empty">not built yet</div>'
    shots = entry.get("shots", [])
    th = (f'<a class="th" href="{root_rel}{escape(shots[0])}"><img loading="lazy" src="{root_rel}{escape(shots[0])}" alt=""></a>'
          if shots else '<div class="empty">no screenshot</div>')
    links = []
    if entry.get("page"):
        links.append(f'<a href="{root_rel}{escape(entry["page"])}">open page</a>')
    if entry.get("spec"):
        links.append(f'<a href="{root_rel}{escape(entry["spec"])}">spec.md</a>')
    links += [f'<a href="{root_rel}{escape(s)}">shot {i + 2}</a>' for i, s in enumerate(shots[1:])]
    keys = [k for k in (f"ref: {entry['ref']}" if entry.get("ref") else "",
                        f"house style {entry['score']}/7" if "score" in entry else "") if k]
    return (f'<div class="cell">{th}<div class="meta"><div class="links">{" · ".join(links)}</div>'
            f'{escape(entry.get("note", ""))}<div class="k">{" · ".join(keys)}</div></div></div>')


def main():
    src = Path(sys.argv[1]).resolve()
    root = src.parent.parent
    data = json.loads(src.read_text(encoding="utf-8"))
    stages = data["stages"]
    missing = [p for proj in data["projects"] for e in proj["entries"].values()
               for p in [e.get("page"), e.get("spec"), *e.get("shots", [])] if p and not (root / p).exists()]
    rows = ['<div></div>' + "".join(
        f'<div class="stage"><b>{i + 1}. {escape(s["name"])}</b><time>{escape(s["date"]) or "before pixi"}</time>'
        f'<p>{escape(s["what"])}</p></div>' for i, s in enumerate(stages))]
    for proj in data["projects"]:
        rows.append(f'<div class="proj"><b>{escape(proj["name"])}</b><small>{escape(proj["event"])}</small></div>'
                    + "".join(cell(proj["entries"].get(s["id"]), "../") for s in stages))
    html = f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1"><title>pixi catalogue</title><style>{CSS}</style></head>
<body><div class="wrap"><h1>pixi catalogue</h1>
<p class="sub">Each hackathon project through every pixi stage, oldest left. Static pages open from disk; React pages need the
projects folder served: <code>python -m http.server 8730</code> in {escape(root.name)}, then open
http://127.0.0.1:8730/catalogue/. House style counts the recurring Claude look (lower is better, 3 or less is good).</p>
<div class="scroll"><div class="grid" style="--n:{len(stages)}">{"".join(rows)}</div></div></div></body></html>"""
    (src.parent / "index.html").write_text(html, encoding="utf-8")
    print(f"wrote {src.parent / 'index.html'}: {len(data['projects'])} projects x {len(stages)} stages")
    for p in missing:
        print(f"missing: {p}")


if __name__ == "__main__":
    main()
