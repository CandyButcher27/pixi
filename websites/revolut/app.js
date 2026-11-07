// Approximate FX rates, USD base (illustrative — not live data).
const RATES = { USD: 1, EUR: 0.9241, GBP: 0.7912, JPY: 157.32, INR: 83.41 };

function toNumber(str) {
  return parseFloat(String(str).replace(/,/g, '')) || 0;
}
function formatAmount(n) {
  return n.toLocaleString('en-US', { maximumFractionDigits: 2 });
}

const amountFrom = document.getElementById('amountFrom');
const amountTo = document.getElementById('amountTo');
const currencyFrom = document.getElementById('currencyFrom');
const currencyTo = document.getElementById('currencyTo');
const rateText = document.getElementById('rateText');
const swapBtn = document.getElementById('swapBtn');

function convert() {
  const from = currencyFrom.value;
  const to = currencyTo.value;
  const amount = toNumber(amountFrom.value);
  const rate = RATES[to] / RATES[from];
  amountTo.value = formatAmount(amount * rate);
  rateText.textContent = `1 ${from} = ${rate.toFixed(4)} ${to}`;
}

if (amountFrom) {
  amountFrom.addEventListener('input', convert);
  currencyFrom.addEventListener('change', convert);
  currencyTo.addEventListener('change', convert);

  swapBtn.addEventListener('click', () => {
    const f = currencyFrom.value;
    currencyFrom.value = currencyTo.value;
    currencyTo.value = f;
    swapBtn.classList.toggle('spun');
    convert();
  });

  convert();
}

// Rate ticker — build once, duplicate for a seamless scroll loop.
const tickerTrack = document.getElementById('tickerTrack');
if (tickerTrack) {
  const pairs = [
    ['USD', 'EUR', true], ['USD', 'GBP', false], ['USD', 'JPY', true],
    ['EUR', 'GBP', false], ['USD', 'INR', true], ['GBP', 'JPY', true],
  ];
  const items = pairs.map(([a, b, up]) => {
    const rate = (RATES[b] / RATES[a]).toFixed(4);
    return `<span class="ticker-item">${a}/${b} <b>${rate}</b> <span class="${up ? 'up' : 'down'}">${up ? '▲' : '▼'}</span></span>`;
  }).join('');
  tickerTrack.innerHTML = items + items;
}

// Mobile nav toggle.
const navToggle = document.getElementById('navToggle');
const mobileNav = document.getElementById('mobileNav');
if (navToggle) {
  navToggle.addEventListener('click', () => {
    const open = navToggle.getAttribute('aria-expanded') === 'true';
    navToggle.setAttribute('aria-expanded', String(!open));
    mobileNav.hidden = open;
  });
}
