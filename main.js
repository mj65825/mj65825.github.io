(function () {
  var root = document.documentElement;
  function get(k) { try { return localStorage.getItem(k); } catch (e) { return null; } }
  function set(k, v) { try { localStorage.setItem(k, v); } catch (e) {} }

  root.dataset.theme = get('theme') || 'dark';
  root.dataset.color = get('color') || 'gold';

  document.getElementById('themeToggle').addEventListener('click', function () {
    var next = root.dataset.theme === 'dark' ? 'light' : 'dark';
    root.dataset.theme = next; set('theme', next);
  });

  var picker = document.getElementById('colorPicker');
  document.getElementById('paletteToggle').addEventListener('click', function () { picker.classList.toggle('open'); });
  document.addEventListener('click', function (e) {
    if (!picker.contains(e.target) && !document.getElementById('paletteToggle').contains(e.target)) picker.classList.remove('open');
  });
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

  // spotlight glow that follows the cursor on tiles
  document.querySelectorAll('.tile').forEach(function (t) {
    t.addEventListener('pointermove', function (e) {
      var r = t.getBoundingClientRect();
      t.style.setProperty('--mx', (e.clientX - r.left) + 'px');
      t.style.setProperty('--my', (e.clientY - r.top) + 'px');
    });
  });

  // project filter
  var btns = document.querySelectorAll('.filter__btn');
  btns.forEach(function (b) {
    b.addEventListener('click', function () {
      btns.forEach(function (x) { x.classList.remove('is-active'); x.setAttribute('aria-selected', 'false'); });
      b.classList.add('is-active'); b.setAttribute('aria-selected', 'true');
      var f = b.dataset.filter;
      document.querySelectorAll('#proj-grid .pcard').forEach(function (c) {
        c.classList.toggle('hide', f !== 'all' && c.dataset.tags.split(' ').indexOf(f) === -1);
      });
    });
  });

  // highlight the nav link for the section in view
  var links = document.querySelectorAll('.nav__link[data-sec]');
  if (links.length && 'IntersectionObserver' in window) {
    var secs = [];
    links.forEach(function (l) { var s = document.getElementById(l.dataset.sec); if (s) secs.push(s); });
    var so = new IntersectionObserver(function (es) {
      es.forEach(function (e) {
        if (e.isIntersecting) links.forEach(function (l) { l.classList.toggle('is-active', l.dataset.sec === e.target.id); });
      });
    }, { rootMargin: '-45% 0px -50% 0px' });
    secs.forEach(function (s) { so.observe(s); });
  }

  var top = document.getElementById('toTop');
  window.addEventListener('scroll', function () { top.classList.toggle('show', window.scrollY > 700); });
  top.addEventListener('click', function () { window.scrollTo({ top: 0, behavior: 'smooth' }); });
})();
