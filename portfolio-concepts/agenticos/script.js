(() => {
  const canvas = document.getElementById("field");
  if (!canvas) return;
  const ctx = canvas.getContext("2d");
  const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  const glyphs = "01{}<>/\\|+-·:;=agenticos".split("");
  let particles = [];
  let w, h, dpr;

  function resize() {
    dpr = Math.min(window.devicePixelRatio || 1, 2);
    w = canvas.offsetWidth;
    h = canvas.offsetHeight;
    canvas.width = w * dpr;
    canvas.height = h * dpr;
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    const count = Math.round((w * h) / 14000);
    particles = Array.from({ length: count }, () => spawn());
  }

  function spawn() {
    return {
      x: Math.random() * w,
      y: Math.random() * h,
      speed: 0.12 + Math.random() * 0.28,
      char: glyphs[(Math.random() * glyphs.length) | 0],
      size: 11 + Math.random() * 10,
      alpha: 0.12 + Math.random() * 0.34,
      swap: 0.002 + Math.random() * 0.004,
    };
  }

  function draw() {
    ctx.clearRect(0, 0, w, h);
    ctx.font = "12px ui-monospace, monospace";
    ctx.textBaseline = "middle";
    for (const p of particles) {
      ctx.font = `${p.size}px ui-monospace, monospace`;
      ctx.fillStyle = `rgba(197, 73, 60, ${p.alpha})`;
      ctx.fillText(p.char, p.x, p.y);
      p.y -= p.speed;
      if (Math.random() < p.swap) p.char = glyphs[(Math.random() * glyphs.length) | 0];
      if (p.y < -20) {
        p.y = h + 20;
        p.x = Math.random() * w;
      }
    }
  }

  function frame() {
    draw();
    if (!reduceMotion) requestAnimationFrame(frame);
  }

  window.addEventListener("resize", resize);
  resize();
  if (reduceMotion) {
    draw();
  } else {
    requestAnimationFrame(frame);
  }
})();
