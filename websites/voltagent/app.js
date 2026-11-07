// Mobile nav toggle
const navBar = document.getElementById('nav-bar');
const navToggle = document.getElementById('nav-toggle');
const navLinks = document.getElementById('nav-links');

navToggle.addEventListener('click', () => {
  const open = navBar.classList.toggle('open');
  navToggle.setAttribute('aria-expanded', String(open));
});

navLinks.querySelectorAll('a').forEach((link) => {
  link.addEventListener('click', () => {
    navBar.classList.remove('open');
    navToggle.setAttribute('aria-expanded', 'false');
  });
});

// Copy-to-clipboard for the quickstart code block
const copyBtn = document.getElementById('copy-btn');
const codeBlock = document.querySelector('.code-body code');

copyBtn.addEventListener('click', async () => {
  const text = codeBlock.innerText;
  try {
    if (navigator.clipboard && window.isSecureContext) {
      await navigator.clipboard.writeText(text);
    } else {
      const textarea = document.createElement('textarea');
      textarea.value = text;
      textarea.style.position = 'fixed';
      textarea.style.opacity = '0';
      document.body.appendChild(textarea);
      textarea.select();
      document.execCommand('copy');
      document.body.removeChild(textarea);
    }
    copyBtn.textContent = 'copied';
    copyBtn.classList.add('copied');
  } catch (err) {
    copyBtn.textContent = 'error';
  }
  setTimeout(() => {
    copyBtn.textContent = 'copy';
    copyBtn.classList.remove('copied');
  }, 1800);
});

// Hero trace: flip the last step from "running" to "done" once, for a live feel.
// Content is already fully present in the DOM either way.
const traceState = document.getElementById('trace-state');
if (traceState) {
  setTimeout(() => {
    traceState.textContent = 'done';
    traceState.classList.add('done');
  }, 1400);
}
