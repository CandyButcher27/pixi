document.querySelectorAll('.mockup-tab').forEach(function (tab) {
  tab.addEventListener('click', function () {
    var wrap = tab.closest('.mockup');
    wrap.querySelectorAll('.mockup-tab').forEach(function (t) { t.classList.remove('active'); });
    wrap.querySelectorAll('.mockup-body').forEach(function (b) { b.classList.remove('active'); });
    tab.classList.add('active');
    wrap.querySelector('[data-body="' + tab.dataset.tab + '"]').classList.add('active');
  });
});

var navToggle = document.getElementById('navToggle');
if (navToggle) {
  navToggle.addEventListener('click', function () {
    document.querySelector('.nav-links').classList.toggle('open');
  });
}
