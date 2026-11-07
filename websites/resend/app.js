// Nav: scrolled state (hairline appears once the page moves)
const navBar = document.getElementById('navBar');
if (navBar) {
  const onScroll = () => navBar.classList.toggle('is-scrolled', window.scrollY > 8);
  onScroll();
  window.addEventListener('scroll', onScroll, { passive: true });
}

// Nav: mobile toggle
const navToggle = document.getElementById('navToggle');
const navMobile = document.getElementById('navMobile');
if (navToggle && navMobile) {
  navToggle.addEventListener('click', () => {
    const open = navToggle.getAttribute('aria-expanded') === 'true';
    navToggle.setAttribute('aria-expanded', String(!open));
    navMobile.classList.toggle('is-open', !open);
  });
}

// Code story: language tabs swap the snippet in the code window
const snippets = {
  node: {
    filename: 'send.js',
    html:
`<span class="tok-kw">import</span> { Resend } <span class="tok-kw">from</span> <span class="tok-str">'resend'</span>;

<span class="tok-kw">const</span> resend = <span class="tok-kw">new</span> Resend(<span class="tok-str">'re_123456789'</span>);

<span class="tok-kw">await</span> resend.emails.send({
  from: <span class="tok-str">'onboarding@resend.dev'</span>,
  to: <span class="tok-str">'user@example.com'</span>,
  subject: <span class="tok-str">'Welcome aboard'</span>,
  html: <span class="tok-str">'&lt;strong&gt;It just works.&lt;/strong&gt;'</span>,
});`
  },
  python: {
    filename: 'send.py',
    html:
`<span class="tok-kw">import</span> resend

resend.api_key = <span class="tok-str">"re_123456789"</span>

resend.Emails.send({
  <span class="tok-str">"from"</span>: <span class="tok-str">"onboarding@resend.dev"</span>,
  <span class="tok-str">"to"</span>: <span class="tok-str">"user@example.com"</span>,
  <span class="tok-str">"subject"</span>: <span class="tok-str">"Welcome aboard"</span>,
  <span class="tok-str">"html"</span>: <span class="tok-str">"&lt;strong&gt;It just works.&lt;/strong&gt;"</span>,
})`
  },
  ruby: {
    filename: 'send.rb',
    html:
`<span class="tok-kw">require</span> <span class="tok-str">"resend"</span>

Resend.api_key = <span class="tok-str">"re_123456789"</span>

Resend::Emails.send({
  <span class="tok-str">"from"</span>: <span class="tok-str">"onboarding@resend.dev"</span>,
  <span class="tok-str">"to"</span>: <span class="tok-str">"user@example.com"</span>,
  <span class="tok-str">"subject"</span>: <span class="tok-str">"Welcome aboard"</span>,
  <span class="tok-str">"html"</span>: <span class="tok-str">"&lt;strong&gt;It just works.&lt;/strong&gt;"</span>
})`
  },
  curl: {
    filename: 'send.sh',
    html:
`<span class="tok-kw">curl</span> -X POST <span class="tok-str">'https://api.resend.com/emails'</span> \\
  -H <span class="tok-str">'Authorization: Bearer re_123456789'</span> \\
  -H <span class="tok-str">'Content-Type: application/json'</span> \\
  -d <span class="tok-str">'{"from":"onboarding@resend.dev","to":"user@example.com","subject":"Welcome aboard","html":"&lt;strong&gt;It just works.&lt;/strong&gt;"}'</span>`
  }
};

const codeTabs = document.querySelectorAll('.code-tab');
const codeBody = document.getElementById('codeBody');
const codeFilename = document.getElementById('codeFilename');

codeTabs.forEach((tab) => {
  tab.addEventListener('click', () => {
    const lang = tab.getAttribute('data-lang');
    const snippet = snippets[lang];
    if (!snippet || !codeBody) return;

    codeTabs.forEach((t) => {
      t.classList.remove('is-active');
      t.setAttribute('aria-selected', 'false');
    });
    tab.classList.add('is-active');
    tab.setAttribute('aria-selected', 'true');

    codeBody.innerHTML = snippet.html;
    if (codeFilename) codeFilename.textContent = snippet.filename;
  });
});
