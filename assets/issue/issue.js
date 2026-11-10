/* Fynboe — Issue 01 · magazine edition
   Page turning by StPageFlip (MIT). Everything else: plain JS. */
(function () {
  const holder = document.getElementById('holder');
  const SNAPSHOT = document.getElementById('book').outerHTML;   // pages as written in index.html
  const whereEl = document.getElementById('where'), prevB = document.getElementById('prev'),
        nextB = document.getElementById('next'), prog = document.getElementById('progress');
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  let flip = null, portrait = false, cur = 0, P = [], N = 0;

  const idx = id => { if (!id) return null; const i = P.findIndex(p => p.dataset.id === id); return i < 0 ? null : i; };

  function make(start) {
    const vw = innerWidth, vh = innerHeight;
    portrait = !(vw >= 820 && vw / vh > 1.15);
    document.body.classList.toggle('portrait', portrait);
    let pw, ph;
    if (!portrait) { ph = Math.min(vh - 140, (vw - 120) / 2 / 0.75); pw = ph * 0.75; }
    else { pw = Math.min(vw - 20, (vh - 140) * 0.75); ph = pw / 0.75; }
    pw = Math.floor(pw); ph = Math.floor(ph);
    if (flip) { try { flip.destroy(); } catch (e) {} }
    holder.innerHTML = SNAPSHOT;
    const book = document.getElementById('book');
    P = [...book.querySelectorAll('.page')]; N = P.length;
    holder.style.width = (portrait ? pw : pw * 2) + 'px';
    holder.style.height = ph + 'px';
    flip = new St.PageFlip(book, {
      width: pw, height: ph, size: 'fixed', showCover: true, usePortrait: portrait,
      flippingTime: reduce ? 1 : 850, maxShadowOpacity: .45, drawShadow: true,
      mobileScrollSupport: false, showPageCorners: true, startPage: start || 0, swipeDistance: 25,
    });
    flip.loadFromHTML(P);
    flip.on('flip', e => { cur = e.data; update(); });
    cur = start || 0; update();
  }

  function visible() {
    if (portrait || cur === 0 || cur === N - 1) return [cur];
    const l = cur % 2 ? cur : cur - 1;
    return [l, l + 1];
  }

  /* films only load and play on the pages you are looking at */
  function films() {
    const vis = visible();
    P.forEach((p, i) => p.querySelectorAll('video').forEach(v => {
      if (vis.includes(i)) {
        if (!v.src) v.src = v.dataset.src;
        const pr = v.play(); if (pr) pr.catch(() => {});
      } else if (!v.paused) v.pause();
    }));
    // keep the two halves of a spread film in step
    const halves = vis.map(i => P[i] && P[i].querySelector('.spread video')).filter(Boolean);
    if (halves.length === 2) halves[1].currentTime = halves[0].currentTime;
  }

  function update() {
    const vis = visible();
    const first = P[vis[0]];
    let label = first.dataset.sec, num, id = '';
    if (vis.length === 2 && label === 'Advertisement') label = P[vis[1]].dataset.sec;
    if (cur === 0) num = 'No. 01 · Winter 2026';
    else if (vis.length === 2) num = `${String(vis[0] + 1).padStart(2, '0')}–${String(vis[1] + 1).padStart(2, '0')} / ${N}`;
    else num = `${String(cur + 1).padStart(2, '0')} / ${N}`;
    for (const i of vis) if (!id && P[i].dataset.id) id = P[i].dataset.id;
    for (let i = vis[0]; i >= 0 && !id; i--) id = P[i].dataset.id;
    whereEl.innerHTML = `<b>${label}</b><span>${num}</span>`;
    prevB.disabled = cur === 0; nextB.disabled = vis[vis.length - 1] >= N - 1;
    prog.style.width = (cur / (N - 1) * 100) + '%';
    if (id && location.hash.slice(1) !== id) { try { history.replaceState(null, '', '#' + id); } catch (e) {} }
    films();
  }

  function goId(id) { const i = idx(id); if (i === null || !flip || i === cur) return; flip.flip(i); }

  document.addEventListener('click', e => {
    const t = e.target.closest('[data-go]');
    if (t) { e.preventDefault(); e.stopPropagation(); goId(t.dataset.go); }
  }, true);
  prevB.onclick = () => flip.flipPrev();
  nextB.onclick = () => flip.flipNext();
  addEventListener('keydown', e => {
    if (e.target.closest('input,textarea')) return;
    if (['ArrowRight', 'PageDown', ' '].includes(e.key)) { e.preventDefault(); flip.flipNext(); }
    else if (['ArrowLeft', 'PageUp'].includes(e.key)) { e.preventDefault(); flip.flipPrev(); }
    else if (e.key === 'Home') flip.flip(0);
    else if (e.key === 'End') flip.flip(N - 1);
  });
  /* people scroll by reflex, so scrolling turns pages too */
  let lock = 0, acc = 0, accT;
  addEventListener('wheel', e => {
    if (portrait) return;
    e.preventDefault();
    if (Date.now() < lock) return;
    acc += Math.abs(e.deltaX) > Math.abs(e.deltaY) ? e.deltaX : e.deltaY;
    if (Math.abs(acc) > 60) { acc > 0 ? flip.flipNext() : flip.flipPrev(); acc = 0; lock = Date.now() + 900; }
    clearTimeout(accT); accT = setTimeout(() => acc = 0, 160);
  }, { passive: false });
  addEventListener('hashchange', () => goId(location.hash.slice(1)));
  let rt, lastW = innerWidth;
  addEventListener('resize', () => {
    clearTimeout(rt);
    rt = setTimeout(() => { if (Math.abs(innerWidth - lastW) < 2 && portrait) return; lastW = innerWidth; make(cur); }, 250);
  });

  document.documentElement.classList.add('js');
  P = [...document.querySelectorAll('#book .page')];
  make(idx(location.hash.slice(1)) || 0);
})();
