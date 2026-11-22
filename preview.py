# -*- coding: utf-8 -*-
"""
Empaqueta las páginas de build.py (ES y EN) en UN solo HTML autocontenido
(CSS y JS incrustados, navegación por #ancla) para verlo en cualquier visor.
  #obras        -> página en español
  #en/works     -> página en inglés
Uso:  python preview.py   ->   vista-previa-v6.html
"""
import base64, io, json, re
from PIL import Image
from pathlib import Path
import build

D = Path(__file__).parent
OUT = D / "vista-previa-v6.html"
KEYS = ["index", "festival", "obras"] + [o["slug"] for o in build.OBRAS] + ["lab", "patrocinio", "recorrido", "archivo", "2027", "contacto", "aviso-legal", "privacidad", "cookies"]
NAVKEY = {o["slug"]: "obras" for o in build.OBRAS}


def pid(lang, key):
    name = build.fname(key, lang)[:-5]
    if lang == "es":
        return "inicio" if name == "index" else name
    return "en" if name == "index" else "en/" + name


NAME2KEY = {lang: {build.fname(k, lang)[:-5]: k for k in KEYS} for lang in ("es", "en")}


def relink(h, lang):
    def rep(m):
        pre, name, anc = m.group(1) or "", m.group(2), m.group(3)
        tl = "en" if pre == "en/" else "es" if pre == "../" else lang
        if anc:
            return f'href="#{anc[1:] if tl == "es" else "en-" + anc[1:]}"'
        return f'href="#{pid(tl, NAME2KEY[tl][name])}"'
    h = re.sub(r'href="(en/|\.\./)?([a-z0-9-]+)\.html(#[^"]*)?"', rep, h)
    if lang == "en":   # ids únicos: en-…
        h = re.sub(r'\b(id|for|data-play|data-sound)="(?!contenido")([^"]+)"', r'\1="en-\2"', h)
        h = re.sub(r'href="#(?!en[-/]|en"|inicio"|contenido")([a-z][^"]*)"', lambda m: f'href="#{m.group(1)}"' if m.group(1) in ALL_PIDS else f'href="#en-{m.group(1)}"', h)
    return h.replace(" aria-current=page", "")


ALL_PIDS = set()


def main():
    build.build_all()
    for lang in ("es", "en"):
        for k in KEYS:
            ALL_PIDS.add(pid(lang, k))
    css = (D / "assets/styles.css").read_text(encoding="utf-8")
    js = (D / "assets/main.js").read_text(encoding="utf-8")
    first = (D / "index.html").read_text(encoding="utf-8")
    head = re.search(r"<head>(.*?)</head>", first, re.S).group(1)
    head = re.sub(r'<link rel="stylesheet" href="assets/styles\.css[^"]*">|<link rel="alternate"[^>]*>', "", head)
    tops, tails, pages, titles = [], [], [], {}
    for lang in ("es", "en"):
        d = D / ("en" if lang == "en" else "")
        idx = (d / "index.html").read_text(encoding="utf-8")
        hidden = "" if lang == "es" else " hidden"
        top = re.search(r"<body[^>]*>(.*?)<main id=\"contenido\">", idx, re.S).group(1)
        tail = re.search(r"</main>.*?(<footer.*?)<script src=\"(?:\.\./)?assets/main", idx, re.S).group(1)
        tops.append(f'<div data-chrome="{lang}"{hidden}>{relink(top, lang)}</div>')
        tails.append(f'<div data-chrome="{lang}"{hidden}>{relink(tail, lang)}</div>')
        for k in KEYS:
            h = (d / build.fname(k, lang)).read_text(encoding="utf-8")
            style = (re.search(r'<body(?: style="([^"]*)")?>', h).group(1) or "")
            main_ = re.search(r'<main id="contenido">(.*?)</main>', h, re.S).group(1)
            part = re.search(r"</main>\s*(<section class=\"partners\".*?</section>)", h, re.S)
            p = pid(lang, k)
            titles[p] = re.search(r"<title>(.*?)</title>", h).group(1)
            nav = NAVKEY.get(k, k)
            pages.append(f'<div data-page="{p}" data-lang="{lang}" data-nav="{pid(lang, nav)}" data-alt="{pid('en' if lang == 'es' else 'es', k)}" data-style="{style}" hidden>{relink(main_ + (part.group(1) if part else ""), lang)}</div>')
    router = """<script>
(function(){
  const pages=[...document.querySelectorAll('[data-page]')], T=%s; let cur=null;
  function show(pg){
    if(cur===pg) return; cur=pg;
    const lang=pg.dataset.lang;
    pages.forEach(p=>p.hidden=(p!==pg));
    document.querySelectorAll('[data-chrome]').forEach(c=>c.hidden=(c.dataset.chrome!==lang));
    document.documentElement.lang=lang;
    document.body.setAttribute('style', pg.dataset.style||'');
    document.querySelectorAll('.nav a').forEach(a=>a.getAttribute('href')==='#'+pg.dataset.nav?a.setAttribute('aria-current','page'):a.removeAttribute('aria-current'));
    document.title=T[pg.dataset.page]||document.title;
    document.querySelectorAll('[data-chrome] .lang a').forEach(a=>a.setAttribute('href','#'+pg.dataset.alt));
    requestAnimationFrame(()=>{ window.dispatchEvent(new Event('resize')); window.dispatchEvent(new Event('scroll'));
      pg.querySelectorAll('[data-map]').forEach(m=>{ if(m._efm){ m._efm.invalidateSize(); m._efm.fitBounds(m._efmB); } }); });
  }
  function route(){
    const h=decodeURIComponent(location.hash.slice(1))||'inicio';
    const pg=document.querySelector('[data-page="'+h+'"]');
    if(pg){ show(pg); window.scrollTo({top:0,behavior:'instant'}); return; }
    const el=document.getElementById(h);
    if(el){ const host=el.closest('[data-page]'); if(host) show(host); requestAnimationFrame(()=>el.scrollIntoView()); return; }
    show(pages[0]);
  }
  window.addEventListener('hashchange', route); route();
})();
</script>""" % json.dumps(titles, ensure_ascii=False)
    html = ("<!DOCTYPE html>\n<html lang=\"es\">\n<head>" + head + f"<style>{css}</style>\n"
            '<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" crossorigin="">\n</head>\n<body>\n'
            + "".join(tops) + '<main id="contenido">' + "\n".join(pages) + "</main>\n" + "".join(tails)
            + '\n<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js" crossorigin=""></script>\n'
            + f"<script>{js}</script>\n" + router + "\n</body>\n</html>")
    cache = {}

    def embed(m):   # fotos locales -> dentro del archivo, para abrirlo en cualquier sitio
        name = m.group(1)
        if name not in cache:
            im = Image.open(D / "assets/espacios" / (name + ".webp")); im.thumbnail((900, 900))
            buf = io.BytesIO(); im.save(buf, "WEBP", quality=68)
            cache[name] = "data:image/webp;base64," + base64.b64encode(buf.getvalue()).decode()
        return f'src="{cache[name]}"'
    html = re.sub(r'src="(?:\.\./)?assets/espacios/([a-z0-9-]+)\.webp"', embed, html)
    OUT.write_text(html, encoding="utf-8")
    print("✓", OUT.name, round(len(html) / 1024), "KB")


if __name__ == "__main__":
    main()
