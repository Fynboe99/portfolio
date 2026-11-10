// Small interactions: videos only play when visible,
// a project preview that follows the cursor, and doodles that drift with the mouse.
(function () {
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var hover = window.matchMedia('(hover: hover) and (pointer: fine)').matches;

  // Image reveals, once, as they scroll into view
  var figs = document.querySelectorAll('.reveal-img');
  if (!('IntersectionObserver' in window) || reduce) {
    figs.forEach(function (f) { f.classList.add('in'); });
  } else {
    var fo = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add('in'); fo.unobserve(e.target); }
      });
    }, { rootMargin: '0px 0px -12% 0px', threshold: 0.01 });
    figs.forEach(function (f) { fo.observe(f); });
  }

  // The logo swirl turns with the page
  var mark = document.querySelector('.brand-mark');
  if (mark && !reduce) {
    var ticking = false;
    window.addEventListener('scroll', function () {
      if (ticking) return; ticking = true;
      requestAnimationFrame(function () { mark.style.setProperty('--spin', (Math.round(window.scrollY * 0.12 / 15) * 15) + 'deg'); ticking = false; });
    }, { passive: true });
  }

  // Videos
  var vids = document.querySelectorAll('video');
  if ('IntersectionObserver' in window) {
    var vo = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        var v = e.target;
        if (e.isIntersecting && !reduce) { var p = v.play(); if (p && p.catch) p.catch(function () {}); }
        else { v.pause(); }
      });
    }, { threshold: 0.15 });
    vids.forEach(function (v) { if (reduce) v.removeAttribute('autoplay'); vo.observe(v); });
  }

  if (reduce || !hover) return;

  // Cursor-following preview on the work index
  var preview = document.querySelector('.preview');
  var rows = document.querySelectorAll('.row[data-preview]');
  var mx = 0, my = 0, px = 0, py = 0, active = false, running = false;
  rows.forEach(function (r) { var i = new Image(); i.src = r.dataset.preview; });

  function loop() {
    px += (mx - px) * 0.16;
    py += (my - py) * 0.16;
    var tilt = Math.max(-6, Math.min(6, (mx - px) * 0.08));
    preview.style.transform = 'translate3d(' + (px + 28) + 'px,' + (py - 20) + 'px,0) translate(0,-50%) rotate(' + tilt + 'deg) scale(' + (active ? 1 : .85) + ')';
    if (active || Math.abs(mx - px) > .5) requestAnimationFrame(loop); else running = false;
  }
  function start() { if (!running) { running = true; requestAnimationFrame(loop); } }

  rows.forEach(function (r) {
    r.addEventListener('mouseenter', function (e) {
      preview.style.backgroundImage = 'url(' + r.dataset.preview + ')';
      preview.style.setProperty('--ratio', r.dataset.ratio || 1.333);
      if (!active) { px = e.clientX; py = e.clientY; }
      active = true; preview.classList.add('on'); start();
    });
    r.addEventListener('mouseleave', function () { active = false; preview.classList.remove('on'); });
  });
  window.addEventListener('mousemove', function (e) { mx = e.clientX; my = e.clientY; if (active) start(); }, { passive: true });

  // Doodles drift gently with the mouse
  var decos = document.querySelectorAll('.deco-drift');
  var tx = 0, ty = 0, cx = 0, cy = 0, drifting = false;
  function drift() {
    cx += (tx - cx) * 0.06; cy += (ty - cy) * 0.06;
    decos.forEach(function (d, i) {
      var depth = (i % 3 + 1) * 8;
      d.style.transform = 'translate3d(' + (cx * depth) + 'px,' + (cy * depth) + 'px,0)';
    });
    if (Math.abs(tx - cx) > .001 || Math.abs(ty - cy) > .001) requestAnimationFrame(drift); else drifting = false;
  }
  window.addEventListener('mousemove', function (e) {
    tx = (e.clientX / window.innerWidth - .5);
    ty = (e.clientY / window.innerHeight - .5);
    if (!drifting) { drifting = true; requestAnimationFrame(drift); }
  }, { passive: true });
})();
