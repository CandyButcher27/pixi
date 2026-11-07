// mobile nav drawer
const burger = document.getElementById('navBurger');
const drawer = document.getElementById('mobileDrawer');

burger.addEventListener('click', () => {
  const open = burger.getAttribute('aria-expanded') === 'true';
  burger.setAttribute('aria-expanded', String(!open));
  drawer.classList.toggle('is-open', !open);
});

// product tab switcher (content for the default tab is already visible in markup)
const tabs = document.querySelectorAll('.product-tab');

tabs.forEach(tab => {
  tab.addEventListener('click', () => {
    tabs.forEach(t => t.setAttribute('aria-selected', 'false'));
    document.querySelectorAll('.product-panel').forEach(p => p.classList.remove('is-active'));

    tab.setAttribute('aria-selected', 'true');
    document.getElementById('panel-' + tab.dataset.panel).classList.add('is-active');
  });
});
