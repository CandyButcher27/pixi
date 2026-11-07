// Together AI — brand rebuild
// Nav surface swap, mobile drawer, platform tabs, pricing toggle, chat note.

(function () {
  const nav = document.getElementById('nav');
  const hero = document.getElementById('top');

  function syncNav() {
    const past = hero.getBoundingClientRect().bottom <= 72;
    nav.classList.toggle('is-light', past);
  }
  syncNav();
  window.addEventListener('scroll', syncNav, { passive: true });

  const burger = document.getElementById('burger');
  const drawer = document.getElementById('drawer');
  burger.addEventListener('click', () => {
    const open = drawer.classList.toggle('is-open');
    burger.setAttribute('aria-expanded', String(open));
  });
  drawer.querySelectorAll('a, button').forEach((el) => {
    el.addEventListener('click', () => {
      drawer.classList.remove('is-open');
      burger.setAttribute('aria-expanded', 'false');
    });
  });

  const tabButtons = document.querySelectorAll('.tab-pill');
  const tabPanels = document.querySelectorAll('.tab-panel');
  tabButtons.forEach((btn) => {
    btn.addEventListener('click', () => {
      tabButtons.forEach((b) => b.setAttribute('aria-selected', 'false'));
      btn.setAttribute('aria-selected', 'true');
      const target = btn.dataset.tab;
      tabPanels.forEach((p) => p.classList.toggle('is-active', p.dataset.panel === target));
    });
  });

  const pricingTabs = document.querySelectorAll('.pricing-tab');
  pricingTabs.forEach((btn) => {
    btn.addEventListener('click', () => {
      pricingTabs.forEach((b) => b.setAttribute('aria-selected', 'false'));
      btn.setAttribute('aria-selected', 'true');
    });
  });

  const planToggles = document.querySelectorAll('.toggle-pill');
  const priceCells = document.querySelectorAll('.price-table .mono-num');
  planToggles.forEach((btn) => {
    btn.addEventListener('click', () => {
      planToggles.forEach((b) => b.setAttribute('aria-pressed', 'false'));
      btn.setAttribute('aria-pressed', 'true');
      const plan = btn.dataset.plan;
      priceCells.forEach((cell) => {
        const val = cell.dataset[plan];
        if (!val) return;
        const suffix = cell.textContent.trim().replace(/^\S+/, '');
        cell.textContent = val + suffix;
      });
    });
  });

  const chatBtn = document.getElementById('chat-btn');
  const chatNote = document.getElementById('chat-note');
  chatBtn.addEventListener('click', () => chatNote.classList.toggle('is-open'));
})();
