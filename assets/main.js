/* EFÍMERA CÓRDOBA · v3 — interacción (ES/EN) */
(function () {
  document.documentElement.classList.add('js');
  const $ = (s, c = document) => c.querySelector(s);
  const $$ = (s, c = document) => [...c.querySelectorAll(s)];
  const reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const EN = () => (document.documentElement.lang || '').startsWith('en');
  const tx = (es, en) => (EN() ? en : es);
  const live = els => els.find(e => !e.closest('[hidden]')) || els[0];

  /* Cabecera: pasa a blanco al bajar */
  const headers = $$('.header');
  const stick = () => headers.forEach(h => h.classList.toggle('is-stuck', window.scrollY > 40));
  stick(); window.addEventListener('scroll', stick, { passive: true });

  /* Menú móvil */
  const closeNav = () => { $$('.mobile-nav').forEach(m => m.classList.remove('open')); document.body.style.overflow = ''; };
  $$('[data-menu-open]').forEach(b => b.addEventListener('click', () => {
    const m = (b.closest('[data-chrome]') || document).querySelector('.mobile-nav');
    m.classList.add('open'); document.body.style.overflow = 'hidden'; }));
  $$('[data-menu-close], .mobile-nav nav a, .mobile-nav .lang a').forEach(b => b.addEventListener('click', closeNav));
  document.addEventListener('keydown', e => { if (e.key === 'Escape') closeNav(); });

  /* Revelado */
  const io = new IntersectionObserver(es => es.forEach(en => { if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); } }), { rootMargin: '0px 0px -8% 0px', threshold: .06 });
  $$('.rv, .rv-blur').forEach(el => io.observe(el));

  /* Marquesinas */
  $$('.marquee__track').forEach(t => { t.innerHTML += t.innerHTML; });

  /* Frases que se encienden palabra a palabra */
  const statements = $$('[data-words]');
  statements.forEach(el => { el.innerHTML = el.textContent.trim().split(/\s+/).map(w => `<span class="w">${w}</span>`).join(' '); });
  const paint = () => statements.forEach(el => {
    if (!el.offsetParent) return;
    const r = el.getBoundingClientRect(), vh = window.innerHeight;
    let p = (vh * .9 - r.top) / (vh * .55 + r.height * .6);
    p = reduce ? 1 : Math.max(0, Math.min(1, p));
    const ws = el.querySelectorAll('.w'), n = Math.round(p * ws.length);
    ws.forEach((w, i) => w.classList.toggle('on', i < n));
  });

  /* Zoom suave del medio de portada */
  const zooms = $$('[data-zoom]');
  const zoom = () => zooms.forEach(z => {
    if (reduce || !z.offsetParent) return;
    const r = z.parentElement.getBoundingClientRect();
    z.style.transform = `scale(${1 + Math.max(0, Math.min(1, -r.top / r.height)) * .12})`;
  });
  let tick = false;
  const onScroll = () => { if (tick) return; tick = true; requestAnimationFrame(() => { paint(); zoom(); tick = false; }); };
  window.addEventListener('scroll', onScroll, { passive: true });
  window.addEventListener('resize', onScroll);
  paint(); zoom();

  /* Vídeo */
  $$('[data-sound]').forEach(b => { const v = document.getElementById(b.dataset.sound); if (!v) return;
    b.addEventListener('click', () => { v.muted = !v.muted; if (!v.muted) v.play().catch(() => {});
      b.textContent = v.muted ? tx('Activar sonido', 'Sound on') : tx('Silenciar', 'Mute'); b.setAttribute('aria-pressed', String(!v.muted)); }); });
  $$('[data-play]').forEach(b => { const v = document.getElementById(b.dataset.play); if (!v) return;
    b.addEventListener('click', () => { if (v.paused) { v.play(); b.textContent = tx('Pausa', 'Pause'); } else { v.pause(); b.textContent = tx('Reproducir', 'Play'); } }); });
  if (reduce) $$('video[autoplay]').forEach(v => v.pause());

  /* Carruseles */
  $$('[data-rail]').forEach(w => {
    const rail = $('.rail', w), bar = $('.rail-progress span', w);
    const upd = () => { const max = rail.scrollWidth - rail.clientWidth, vis = rail.clientWidth / (rail.scrollWidth || 1);
      bar.style.width = (vis * 100) + '%'; bar.style.left = (max > 0 ? rail.scrollLeft / max * (100 - vis * 100) : 0) + '%'; };
    rail.addEventListener('scroll', upd, { passive: true }); window.addEventListener('resize', upd); upd();
    const step = () => ($('.card', rail)?.getBoundingClientRect().width || 300) + 20;
    $$('[data-prev]', w).forEach(b => b.addEventListener('click', () => rail.scrollBy({ left: -step(), behavior: 'smooth' })));
    $$('[data-next]', w).forEach(b => b.addEventListener('click', () => rail.scrollBy({ left: step(), behavior: 'smooth' })));
  });

  /* Visor de imágenes: cada [data-gallery] es una serie */
  const lbs = $$('.lightbox');
  if (lbs.length) {
    let lb = lbs[0], items = [], i = 0, last = null;
    const show = k => { i = (k + items.length) % items.length; const it = items[i];
      $('img', lb).src = it.dataset.full; $('img', lb).alt = it.dataset.alt; $('figcaption', lb).textContent = it.dataset.alt;
      $('.lb-count', lb).textContent = `${String(i + 1).padStart(2, '0')} / ${String(items.length).padStart(2, '0')}`; };
    $$('[data-gallery] button[data-full]').forEach(it => it.addEventListener('click', () => {
      lb = live(lbs); items = $$('button[data-full]', it.closest('[data-gallery]')); last = it; show(items.indexOf(it));
      lb.classList.add('open'); document.body.style.overflow = 'hidden'; $('.lb-close', lb).focus(); }));
    const close = () => { lb.classList.remove('open'); document.body.style.overflow = ''; last && last.focus(); };
    lbs.forEach(l => {
      $('.lb-close', l).addEventListener('click', close);
      $('.lb-prev', l).addEventListener('click', () => show(i - 1));
      $('.lb-next', l).addEventListener('click', () => show(i + 1));
      l.addEventListener('click', e => { if (e.target === l) close(); });
    });
    document.addEventListener('keydown', e => { if (!lb.classList.contains('open')) return;
      if (e.key === 'Escape') close(); if (e.key === 'ArrowLeft') show(i - 1); if (e.key === 'ArrowRight') show(i + 1); });
  }

  /* Mapas: los puntos viajan en data-map */
  if (window.L) $$('[data-map]').forEach(el => {
    const pts = JSON.parse(el.dataset.map);
    const map = L.map(el, { scrollWheelZoom: false });
    L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', { maxZoom: 19, attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>' }).addTo(map);
    const mk = {};
    pts.forEach(p => {
      const icon = L.divIcon({ className: "", html: `<div class="pin" style="background:${p.color};color:${p.txt || "#fff"}">${p.n}</div>`, iconSize: [34, 34], iconAnchor: [17, 17] });
      mk[p.n] = L.marker(p.coords, { icon, title: p.title }).addTo(map).bindPopup(`<strong>${p.n} · ${p.title}</strong>${p.place}<br><a href="${p.url}">${p.more}</a>`);
    });
    el._efmB = L.latLngBounds(pts.map(p => p.coords)).pad(.2); el._efm = map; map.fitBounds(el._efmB);
    const stops = $$('.stops a', el.parentElement);
    stops.forEach(a => a.addEventListener('mouseenter', () => { stops.forEach(x => x.classList.remove('active')); a.classList.add('active'); mk[a.dataset.n].openPopup(); }));
  });

  /* Pestañas (convocatoria de empresas): una sección a la vez para acortar la página */
  $$('[data-tabbed]').forEach(box => {
    const tabs = $$('[data-tab]', box), panels = $$('[data-panel]', box);
    const headerH = () => (live($$('.header'))?.offsetHeight || 0);
    const activate = (id, scroll) => {
      panels.forEach(p => p.classList.toggle('on', p.id === id));
      tabs.forEach(t => { const on = t.dataset.tab === id; t.setAttribute('aria-selected', String(on));
        if (on) { const bar = t.parentElement; bar.scrollLeft = t.offsetLeft - (bar.clientWidth - t.offsetWidth) / 2; } });
      if (scroll) window.scrollTo({ top: box.getBoundingClientRect().top + window.scrollY - headerH(), behavior: reduce ? 'auto' : 'smooth' });
    };
    tabs.forEach(t => t.addEventListener('click', e => { e.preventDefault(); activate(t.dataset.tab, true); }));
    const fromHash = () => {
      const id = decodeURIComponent(location.hash.slice(1)); if (!id) return false;
      const el = document.getElementById(id); const p = el && el.closest('[data-panel]');
      if (!p || !box.contains(p)) return false;
      activate(p.id, false); requestAnimationFrame(() => el.scrollIntoView()); return true;
    };
    if (!fromHash()) activate(panels[0].id, false);
    window.addEventListener('hashchange', fromHash);
    $$('a[href^="#"]').forEach(a => { if (!a.dataset.tab) a.addEventListener('click', () => setTimeout(fromHash, 0)); });
  });

  /* Formularios (v3: sin servidor conectado) */
  $$('form[data-form]').forEach(f => {
    const msg = $('.form-msg', f);
    f.addEventListener('submit', e => {
      e.preventDefault();
      if ($('.hp input', f)?.value) return;
      if (!f.checkValidity()) { f.reportValidity(); return; }
      msg.textContent = f.dataset.ok; msg.classList.add('show');
      $$('input:not([type=checkbox]), textarea', f).forEach(x => { if (!x.closest('.hp')) x.value = ''; });
    });
  });

  /* Cookies (una sola elección para los dos idiomas) */
  const cks = $$('.cookies'), KEY = 'efm_consent';
  let saved = null; try { saved = JSON.parse(localStorage.getItem(KEY)); } catch (e) {}
  const hideAll = () => cks.forEach(c => c.classList.remove('show'));
  const store = v => { try { localStorage.setItem(KEY, JSON.stringify(Object.assign({ v: 1, t: Date.now() }, v))); } catch (e) {} hideAll(); };
  cks.forEach(ck => {
    if (!saved) ck.classList.add('show');
    $('[data-ck-all]', ck).addEventListener('click', () => store({ analitica: true, publicidad: true }));
    $('[data-ck-none]', ck).addEventListener('click', () => store({ analitica: false, publicidad: false }));
    $('[data-ck-cfg]', ck).addEventListener('click', () => $('.cfg', ck).classList.toggle('show'));
    $('[data-ck-save]', ck).addEventListener('click', () => store({ analitica: $('[data-ck-an]', ck).checked, publicidad: $('[data-ck-pub]', ck).checked }));
  });
  $$('[data-cookies-open]').forEach(b => b.addEventListener('click', () => cks.forEach(ck => { ck.classList.add('show'); $('.cfg', ck).classList.add('show'); })));
})();
