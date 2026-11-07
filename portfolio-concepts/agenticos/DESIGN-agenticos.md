---
version: alpha
name: AgenticOS-landing
description: A dark, technical landing page for AgenticOS — a monorepo of independent agent-tooling modules routed through one shared model router. Near-black oxblood ink (#140f10) with a single tonal signal-red accent (#c5493c) carries every CTA, live-status dot, and diagram pulse — chosen specifically to avoid the amber/rust/gold/green/indigo fingerprints already claimed by the other builds in this repo's portfolio-concepts set. Display type is Gambarino (self-hosted, Fontshare), a distinctive high-character serif used only for headlines and section titles at large size with italic single-word accents; body, nav, and all UI chrome run on system-ui, a true neutral. The signature artifact is a real, labeled SVG diagram — five caller modules flowing through a central Token-router hub out to four real model providers — animated with a CSS dash-offset "current" rather than a generic hero graphic. Module cards use an invented chamfered-corner silhouette (clipped bottom-left notch) instead of a rounded rectangle, and the footer's oversized "AgenticOS" wordmark sits anchored flush to the bottom edge, above a fine module-grid texture, per the law's placement rule.

colors:
  ink: "#ece4e2"
  ink-dim: "#ab9c9a"
  ink-faint: "#756765"
  bg: "#140f10"
  bg-raised: "#1c1516"
  bg-raised-2: "#241b1c"
  accent: "#c5493c"
  accent-dim: "#833931"

typography:
  display:
    fontFamily: "Gambarino, Georgia, 'Iowan Old Style', serif"
    fontSize: "clamp(42px, 7vw, 76px)"
    fontWeight: 400
    lineHeight: 1.06
  body:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', sans-serif"
    fontSize: 16px
    lineHeight: 1.5
  label:
    fontFamily: "ui-monospace, 'Cascadia Code', Consolas, monospace"
    fontSize: 11px
    letterSpacing: 0.03em

spacing:
  section-y: 120px
  wrap-max: 1160px
  radius-nav: 999px
  radius-frame: 20px

components:
  nav: "floating centered pill, blurred glass, mono wordmark + bare glyph mark (no box)"
  hero: "full-bleed canvas glyph field (low-contrast drifting monospace characters) behind a two-line serif headline with one italic accent word; single glass CTA, no filled+outline pair"
  diagram: "static SVG node graph (5 callers → 1 hub → 4 providers), CSS dash-offset flow animation, gated globally by prefers-reduced-motion"
  modules-grid: "3-column grid of chamfered-corner cards, real project names/descriptions from README.md, honest status dot (active/planning/placeholder/reference)"
  footer: "oversized Gambarino wordmark anchored to bottom edge, above fine grid texture, real internal links only (no invented logos)"

notes: |
  Built to the anti-slop-design-law skill. Deliberately avoids: blue-purple gradients,
  glowy pill buttons, icon-in-tile, gradient-filled headline text, sun/moon toggle,
  filled+outline button pair, dot-under-nav-item, Google-default fonts (Inter,
  Space Grotesk, Sora, etc.). Font self-hosted via @font-face rather than a CDN/Google
  Fonts link. Content-bearing text is never gated behind an entrance animation — only
  the decorative canvas background and the diagram's flow-dash are motion-gated.
