"""Measure a rendered page's composition grammar from computed styles and geometry.

Used in both directions: to describe an existing catalogue entry during ingestion,
and to check a freshly built page during verification. No model in the loop.
"""
from __future__ import annotations

from pathlib import Path

from playwright.sync_api import sync_playwright

VIEWPORT = {"width": 1440, "height": 900}

PROBE = r"""
() => {
  const vw = window.innerWidth;
  const pageH = document.documentElement.scrollHeight;
  const num = v => parseFloat(v) || 0;
  const rectOf = el => {
    const r = el.getBoundingClientRect();
    return {x: r.left, y: r.top + window.scrollY, w: r.width, h: r.height};
  };
  const shown = el => {
    const s = getComputedStyle(el);
    const r = el.getBoundingClientRect();
    return r.width > 1 && r.height > 1 && s.visibility !== 'hidden' && s.display !== 'none' && num(s.opacity) > 0.05;
  };
  const all = Array.from(document.body.querySelectorAll('*')).filter(shown);
  const opaque = c => c && c !== 'transparent' && !/rgba\(\s*0,\s*0,\s*0,\s*0\s*\)/.test(c);

  const bodyStyle = getComputedStyle(document.body);
  const bodySize = num(bodyStyle.fontSize) || 16;

  // typography
  const families = new Set();
  let maxType = 0, maxTypeWeight = 400, maxTypeFamily = '';
  for (const el of all) {
    const s = getComputedStyle(el);
    if ((el.textContent || '').trim().length > 1) families.add(s.fontFamily);
    const size = num(s.fontSize);
    if (size > maxType && (el.textContent || '').trim().length > 2) {
      maxType = size; maxTypeWeight = num(s.fontWeight) || 400; maxTypeFamily = s.fontFamily;
    }
  }

  // gradients
  const gradients = all.filter(el => /gradient\(/.test(getComputedStyle(el).backgroundImage)).length;

  // control geometry: buttons and button-like links
  const controls = all.filter(el => {
    if (el.tagName === 'BUTTON') return true;
    if (el.tagName === 'INPUT' && /submit|button/i.test(el.type || '')) return true;
    const cls = (el.className && el.className.baseVal !== undefined ? el.className.baseVal : el.className) || '';
    if (el.tagName === 'A' && /\b(btn|button|cta)\b/i.test(String(cls))) return true;
    return false;
  });
  let pillControls = 0, maxControlRadius = 0;
  for (const el of controls) {
    const r = rectOf(el);
    const rad = num(getComputedStyle(el).borderTopLeftRadius);
    maxControlRadius = Math.max(maxControlRadius, rad);
    if (r.h > 0 && rad >= r.h / 2 - 1) pillControls++;
  }

  // surface geometry: radius of large panels
  let maxPanelRadius = 0;
  let glassPanels = 0;
  for (const el of all) {
    const r = rectOf(el);
    if (r.w * r.h < 8000) continue;
    const s = getComputedStyle(el);
    if (opaque(s.backgroundColor) || s.borderTopWidth !== '0px') {
      maxPanelRadius = Math.max(maxPanelRadius, num(s.borderTopLeftRadius));
    }
    if (/blur\(/.test(s.backdropFilter || '') || /blur\(/.test(s.webkitBackdropFilter || '')) glassPanels++;
  }

  // full-bleed sections
  const fullBleed = all.filter(el => {
    const r = rectOf(el);
    if (r.w < vw * 0.98 || r.h < 200) return false;  // 0.98 so a scrollbar does not hide a full-bleed section
    const s = getComputedStyle(el);
    return opaque(s.backgroundColor) || s.backgroundImage !== 'none' || el.querySelector('img, video, canvas, svg');
  }).length;

  // equal-width sibling rows (the card grid tell)
  const cardRows = [];
  for (const el of all) {
    const kids = Array.from(el.children).filter(shown);
    if (kids.length < 2) continue;
    const rs = kids.map(rectOf);
    const w0 = rs[0].w, y0 = rs[0].y;
    const equal = rs.every(r => Math.abs(r.w - w0) <= 3 && Math.abs(r.y - y0) <= 6);
    if (!equal || w0 < 120 || rs[0].h < 60) continue;
    const boxed = kids.filter(k => {
      const s = getComputedStyle(k);
      return opaque(s.backgroundColor) || s.borderTopWidth !== '0px' || num(s.borderTopLeftRadius) > 0;
    }).length;
    cardRows.push({count: kids.length, boxed: boxed, width: Math.round(w0)});
  }

  // horizontal centre of mass of text, per element subtree
  const textCentroid = root => {
    let wsum = 0, xsum = 0;
    const walk = document.createTreeWalker(root, NodeFilter.SHOW_TEXT);
    let n;
    while ((n = walk.nextNode())) {
      const t = (n.textContent || '').trim();
      if (t.length < 2) continue;
      const range = document.createRange();
      range.selectNodeContents(n);
      const r = range.getBoundingClientRect();
      if (r.width < 1 || r.height < 1) continue;
      const weight = t.length * Math.sqrt(r.height);
      // clamp: text parked outside the viewport (marquees, overflow tracks, off-screen
      // slides) otherwise drags the centre of mass past the page edge and the alignment
      // it implies is meaningless
      const centre = Math.min(Math.max(r.left + r.width / 2, 0), vw);
      wsum += weight;
      xsum += weight * centre;
    }
    return wsum ? Math.min(Math.max(xsum / wsum / vw, 0), 1) : null;
  };

  // hero: first substantial block that is not the nav
  const topLevel = Array.from(document.body.children).filter(shown)
    .flatMap(el => (el.tagName === 'MAIN' || el.tagName === 'DIV' && el.children.length > 2)
      ? Array.from(el.children).filter(shown) : [el]);
  const sections = topLevel.filter(el => rectOf(el).h >= 180 && el.tagName !== 'NAV' && el.tagName !== 'HEADER');
  const hero = sections[0] || null;

  const sectionCentroids = sections.map(textCentroid).filter(v => v !== null);
  let flips = 0;
  for (let i = 1; i < sectionCentroids.length; i++) {
    const a = sectionCentroids[i - 1] - 0.5, b = sectionCentroids[i] - 0.5;
    if (Math.abs(a) > 0.04 && Math.abs(b) > 0.04 && Math.sign(a) !== Math.sign(b)) flips++;
  }

  // imagery share of the page
  let mediaArea = 0;
  for (const el of all) {
    const s = getComputedStyle(el);
    const isMedia = ['IMG', 'VIDEO', 'CANVAS', 'PICTURE'].includes(el.tagName) || /url\(/.test(s.backgroundImage);
    if (!isMedia) continue;
    const r = rectOf(el);
    mediaArea += r.w * r.h;
  }

  // palette
  const bgCounts = {};
  for (const el of all) {
    const r = rectOf(el);
    if (r.w * r.h < 20000) continue;
    const c = getComputedStyle(el).backgroundColor;
    if (!opaque(c)) continue;
    bgCounts[c] = (bgCounts[c] || 0) + r.w * r.h;
  }
  const backgrounds = Object.entries(bgCounts).sort((a, b) => b[1] - a[1]).slice(0, 6).map(e => e[0]);

  const textChars = (document.body.innerText || '').replace(/\s+/g, ' ').length;

  return {
    viewport_width: vw,
    page_height: Math.round(pageH),
    element_count: all.length,
    body_font_size: bodySize,
    body_font_family: bodyStyle.fontFamily,
    display_font_size: Math.round(maxType),
    display_font_weight: maxTypeWeight,
    display_font_family: maxTypeFamily,
    font_families: Array.from(families).slice(0, 8),
    gradient_elements: gradients,
    glass_panels: glassPanels,
    control_count: controls.length,
    pill_controls: pillControls,
    max_control_radius: Math.round(maxControlRadius),
    max_panel_radius: Math.round(maxPanelRadius),
    full_bleed_sections: fullBleed,
    card_rows: cardRows,
    section_count: sections.length,
    section_centroids: sectionCentroids.map(v => Math.round(v * 1000) / 1000),
    centroid_flips: flips,
    hero_centroid: hero ? textCentroid(hero) : null,
    hero_height: hero ? Math.round(rectOf(hero).h) : 0,
    hero_text_align: hero ? getComputedStyle(hero).textAlign : null,
    media_area_ratio: Math.round(mediaArea / (vw * pageH) * 1000) / 1000,
    backgrounds: backgrounds,
    text_chars: textChars,
  };
}
"""

GENERIC_FAMILIES = ("inter", "system-ui", "-apple-system", "segoe ui", "roboto", "helvetica neue", "arial")


def measure(page_path: str | Path) -> dict:
    """Render one local HTML page and return its raw composition metrics."""
    url = Path(page_path).resolve().as_uri()
    with sync_playwright() as pw:
        browser = pw.chromium.launch()
        page = browser.new_page(viewport=VIEWPORT)
        page.goto(url, wait_until="networkidle")
        page.wait_for_timeout(400)
        metrics = page.evaluate(PROBE)
        browser.close()
    return metrics


def measure_many(page_paths: list[Path]) -> dict[str, dict]:
    """One browser, many pages. Keyed by the page's parent directory name."""
    out: dict[str, dict] = {}
    with sync_playwright() as pw:
        browser = pw.chromium.launch()
        page = browser.new_page(viewport=VIEWPORT)
        for p in page_paths:
            try:
                page.goto(Path(p).resolve().as_uri(), wait_until="networkidle", timeout=30000)
                page.wait_for_timeout(300)
                out[Path(p).parent.name] = page.evaluate(PROBE)
            except Exception as exc:
                out[Path(p).parent.name] = {"error": f"{type(exc).__name__}: {exc}"}
        browser.close()
    return out


def grammar(m: dict) -> dict:
    """Turn raw metrics into the categorical composition grammar used for retrieval."""
    if "error" in m:
        return {"error": m["error"]}

    centroid = m.get("hero_centroid")
    if centroid is None:
        hero_alignment = "unknown"
    elif centroid < 0.42:
        hero_alignment = "left"
    elif centroid > 0.58:
        hero_alignment = "right"
    else:
        hero_alignment = "centered"

    widest_row = max((r for r in m["card_rows"] if r["boxed"] >= r["count"] - 1),
                     key=lambda r: r["count"], default=None)
    card_reliance = "none"
    if widest_row:
        card_reliance = "high" if widest_row["count"] >= 3 else "low"

    display_ratio = m["display_font_size"] / max(m["body_font_size"], 1)
    per_1k = m["element_count"] / max(m["page_height"] / 1000, 1)
    chars_per_1k = m["text_chars"] / max(m["page_height"] / 1000, 1)

    radius = max(m["max_control_radius"], m["max_panel_radius"])
    if m["pill_controls"]:
        geometry = "pill"
    elif radius >= 20:
        geometry = "rounded"
    elif radius >= 6:
        geometry = "soft"
    else:
        geometry = "sharp"

    fam = (m.get("display_font_family") or "").lower()
    return {
        "hero_alignment": hero_alignment,
        "hero_weight_split": round(centroid, 3) if centroid is not None else None,
        "section_rhythm": "alternating" if m["centroid_flips"] >= 2 else "uniform",
        "full_bleed_sections": m["full_bleed_sections"],
        "card_reliance": card_reliance,
        "largest_card_row": widest_row["count"] if widest_row else 0,
        "geometry": geometry,
        "max_radius": radius,
        "display_dominance": round(display_ratio, 2),
        "display_weight": m["display_font_weight"],
        "generic_display_font": any(g in fam for g in GENERIC_FAMILIES),
        "imagery": ("dominant" if m["media_area_ratio"] >= 0.30
                    else "present" if m["media_area_ratio"] >= 0.06 else "absent"),
        "imagery_ratio": m["media_area_ratio"],
        "density": ("high" if per_1k >= 55 else "medium" if per_1k >= 28 else "low"),
        "text_density": ("high" if chars_per_1k >= 900 else "medium" if chars_per_1k >= 350 else "low"),
        "gradients": m["gradient_elements"],
        "glass_panels": m["glass_panels"],
        "palette_size": len(m["backgrounds"]),
        "sections": m["section_count"],
        "page_height": m["page_height"],
    }
