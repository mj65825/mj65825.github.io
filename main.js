(function () {
  var root = document.documentElement;
  function get(k) { try { return localStorage.getItem(k); } catch (e) { return null; } }
  function set(k, v) { try { localStorage.setItem(k, v); } catch (e) {} }

  root.dataset.theme = get('theme') || 'dark';
  root.dataset.color = get('color') || 'gold';

  var sidebar = document.getElementById('sidebar');
  var menu = document.getElementById('menuToggle');
  menu.addEventListener('click', function () { sidebar.classList.toggle('open'); });
  document.addEventListener('click', function (e) {
    if (sidebar.classList.contains('open') && !sidebar.contains(e.target) && !menu.contains(e.target)) sidebar.classList.remove('open');
  });

  document.getElementById('themeToggle').addEventListener('click', function () {
    var next = root.dataset.theme === 'dark' ? 'light' : 'dark';
    root.dataset.theme = next; set('theme', next);
  });

  var picker = document.getElementById('colorPicker');
  document.getElementById('paletteToggle').addEventListener('click', function () { picker.classList.toggle('open'); });
  function setSwatches() {
    picker.querySelectorAll('.swatch').forEach(function (s) { s.classList.toggle('is-active', s.dataset.color === root.dataset.color); });
  }
  picker.querySelectorAll('.swatch').forEach(function (s) {
    function pick() { root.dataset.color = s.dataset.color; set('color', s.dataset.color); setSwatches(); }
    s.addEventListener('click', pick);
    s.addEventListener('keydown', function (e) { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); pick(); } });
  });
  setSwatches();

  var io = 'IntersectionObserver' in window ? new IntersectionObserver(function (es) {
    es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } });
  }, { threshold: 0.08 }) : null;
  document.querySelectorAll('.reveal').forEach(function (el) { io ? io.observe(el) : el.classList.add('in'); });

  var btns = document.querySelectorAll('.filter__btn');
  btns.forEach(function (b) {
    b.addEventListener('click', function () {
      btns.forEach(function (x) { x.classList.remove('is-active'); x.setAttribute('aria-selected', 'false'); });
      b.classList.add('is-active'); b.setAttribute('aria-selected', 'true');
      var f = b.dataset.filter;
      document.querySelectorAll('#proj-grid .card').forEach(function (c) {
        c.classList.toggle('hide', f !== 'all' && c.dataset.tags.split(' ').indexOf(f) === -1);
      });
    });
  });

  var typed = document.getElementById('typed');
  if (typed) {
    var txt = typed.dataset.text.replace('&rarr;', '\u2192'), i = 0;
    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) { typed.textContent = txt; }
    else (function tick() { typed.textContent = txt.slice(0, ++i); if (i < txt.length) setTimeout(tick, 70); })();
  }

  var top = document.getElementById('toTop');
  window.addEventListener('scroll', function () { top.classList.toggle('show', window.scrollY > 500); });
  top.addEventListener('click', function () { window.scrollTo({ top: 0, behavior: 'smooth' }); });
})();
