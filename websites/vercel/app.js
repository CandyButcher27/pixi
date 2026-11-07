document.addEventListener('DOMContentLoaded', () => {
  const toggle = document.getElementById('navToggle');
  const mobileNav = document.getElementById('mobileNav');
  if (toggle && mobileNav) {
    toggle.addEventListener('click', () => {
      const open = mobileNav.classList.toggle('open');
      toggle.setAttribute('aria-expanded', String(open));
    });
    mobileNav.querySelectorAll('a').forEach((link) => {
      link.addEventListener('click', () => {
        mobileNav.classList.remove('open');
        toggle.setAttribute('aria-expanded', 'false');
      });
    });
  }

  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (reduceMotion) return;

  const counters = document.querySelectorAll('[data-count-to]');
  if (!counters.length || !('IntersectionObserver' in window)) return;

  const animateCount = (el) => {
    const target = parseInt(el.dataset.countTo, 10);
    const suffix = el.dataset.suffix || '';
    const duration = 900;
    const start = performance.now();
    const step = (now) => {
      const progress = Math.min((now - start) / duration, 1);
      const eased = 1 - Math.pow(1 - progress, 3);
      el.textContent = Math.round(target * eased) + suffix;
      if (progress < 1) requestAnimationFrame(step);
      else el.textContent = target + suffix;
    };
    requestAnimationFrame(step);
  };

  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        animateCount(entry.target);
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.5 });

  counters.forEach((el) => observer.observe(el));
});
