# -*- coding: utf-8 -*-
"""
Dosier de la convocatoria de empresas 2027 (PDF, A4 apaisado) con la estética de la web.
Reutiliza los datos y textos de build.py. Genera ES y EN.
Uso:  python dosier.py   ->   assets/dosier/*.pdf
Necesita Google Chrome instalado (lo usa en modo invisible para imprimir a PDF).
"""
import subprocess, sys
from html import escape
from pathlib import Path
import build
from build import (t, T, C, SPACES, STATS_2026, SHIMA, DEZEEN, AKT, GETS, DEADLINE, SHOWCASE, WAYS, GUESTS, AWARD, INCLUDES,
                   COLABORAN, MAIL, MARK, MARK_LINE, OBRAS, DOSIER, img)

D = Path(__file__).parent
OUTDIR = D / "assets" / "dosier"
CHROME = [r"C:\Program Files\Google\Chrome\Application\chrome.exe", r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"]

CSS = """
@page { size: 297mm 210mm; margin: 0; }
* { box-sizing: border-box; margin: 0; padding: 0; }
:root { --arcilla:#C98C6C; --arcilla-osc:#8E5138; --arena:#D8C4A2; --arena-osc:#B49A74; --crema:#F4EDE2; --cal:#EADFCC; --tinta:#141210; --gris:#6F675C;
  --d:"Unbounded","Arial Black",sans-serif; --s:"Instrument Serif",Georgia,serif; --b:"DM Sans",Arial,sans-serif; }
html { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
body { font-family: var(--b); color: var(--tinta); font-size: 10.5pt; line-height: 1.5; }
.slide { width: 297mm; height: 210mm; position: relative; overflow: hidden; page-break-after: always; background: var(--crema); padding: 16mm 18mm; }
.slide:last-child { page-break-after: auto; }
.arcilla { background: var(--arcilla); } .tinta { background: var(--tinta); color: #fff; } .arena { background: var(--arena); } .cal { background: var(--cal); }
.mark { display: inline-flex; flex-direction: column; align-items: flex-start; gap: .3em; font-family: var(--d); font-weight: 500; letter-spacing: -.04em; line-height: 1; text-transform: uppercase; white-space: nowrap; }
.mark > span { display: block; } .mark.line { flex-direction: row; align-items: baseline; gap: .32em; }
.mark .acc { position: relative; display: inline-block; }
.mark .acc::before { content: ""; position: absolute; left: -.06em; right: -.06em; top: -.15em; height: .09em; background: currentColor; }
.label { font-size: 7.5pt; font-weight: 700; letter-spacing: .16em; text-transform: uppercase; }
.d { font-family: var(--d); font-weight: 400; letter-spacing: -.03em; line-height: 1.04; }
.it { font-family: var(--s); font-style: italic; letter-spacing: 0; }
.foot { position: absolute; left: 18mm; right: 18mm; bottom: 9mm; display: flex; justify-content: space-between; align-items: baseline; font-size: 7pt; font-weight: 700; letter-spacing: .12em; text-transform: uppercase; opacity: .7; }
.half ~ .foot, .stack ~ .foot { right: calc(50% + 10mm); }
.foot .mark { font-size: 8pt; }
.lead { font-size: 13pt; line-height: 1.45; }
.half { position: absolute; top: 0; bottom: 0; right: 0; width: 50%; }
.half img { width: 100%; height: 100%; object-fit: cover; display: block; }
.textcol { width: 46%; height: 100%; display: flex; flex-direction: column; }
/* portada */
.cover { display: flex; flex-direction: column; justify-content: space-between; }
.cover .big { font-size: 62pt; }
.cover .sub { font-family: var(--s); font-style: italic; font-size: 34pt; line-height: 1; }
.cover .row { display: flex; justify-content: space-between; align-items: flex-end; gap: 10mm; }
/* pasos */
.steps { display: grid; grid-template-columns: repeat(4, 1fr); border-top: 1.5pt solid var(--tinta); margin-top: 14mm; }
.steps > div { padding: 7mm 6mm 0 0; } .steps > div + div { padding-left: 6mm; border-left: .6pt solid rgba(20,18,16,.3); }
.steps .k { font-family: var(--s); font-style: italic; font-size: 38pt; line-height: 1; color: var(--arcilla-osc); display: block; margin-bottom: 5mm; }
.steps h3 { font-family: var(--d); font-weight: 400; font-size: 13pt; letter-spacing: -.02em; line-height: 1.15; margin-bottom: 3mm; }
/* cifras */
.stats { display: grid; grid-template-columns: repeat(4, 1fr); border-top: .6pt solid rgba(255,255,255,.3); }
.stats > div { padding: 6mm 5mm 6mm 0; border-bottom: .6pt solid rgba(255,255,255,.3); }
.stats b { display: block; font-family: var(--d); font-weight: 400; font-size: 30pt; letter-spacing: -.05em; line-height: 1; color: var(--arena); }
.stats span { display: block; margin-top: 2.5mm; font-weight: 700; font-size: 9pt; }
.strip { display: grid; grid-template-columns: repeat(5, 1fr); gap: 4mm; margin-top: 8mm; }
.strip img { width: 100%; aspect-ratio: 4/3; object-fit: cover; display: block; }
.strip small { display: block; margin-top: 1.5mm; font-size: 7.5pt; opacity: .7; }
/* mapa */
.mapwrap { display: grid; grid-template-columns: 128mm 1fr; gap: 12mm; height: 100%; align-items: center; }
.mapwrap svg { height: 172mm; width: auto; display: block; }
.mlist { list-style: none; border-top: .6pt solid rgba(20,18,16,.25); }
.mlist li { display: grid; grid-template-columns: 11mm 1fr; gap: 4mm; align-items: center; padding: 2.4mm 0; border-bottom: .6pt solid rgba(20,18,16,.25); }
.mlist .n { width: 9mm; height: 9mm; border-radius: 50%; background: var(--tinta); color: var(--crema); display: grid; place-items: center; font: 400 8pt var(--d); }
.mlist strong { display: block; font-family: var(--d); font-weight: 400; font-size: 11pt; letter-spacing: -.02em; line-height: 1.2; }
.mlist small { color: var(--gris); font-size: 8pt; }
/* espacio */
.space .num { font-family: var(--s); font-style: italic; font-size: 64pt; line-height: .9; color: var(--arcilla-osc); }
.space h2 { font-size: 24pt; margin: 4mm 0 6mm; }
.space .meta { margin-top: auto; border-top: .6pt solid rgba(20,18,16,.3); padding-top: 4mm; font-size: 8.5pt; display: grid; gap: 1.5mm; margin-bottom: 8mm; }
.space .meta b { font-weight: 700; }
/* condiciones */
.price { display: grid; grid-template-columns: auto 1fr; gap: 12mm; align-items: center; background: var(--tinta); color: #fff; padding: 9mm 10mm; margin-top: 8mm; }
.price b { font-family: var(--d); font-weight: 400; font-size: 52pt; letter-spacing: -.05em; line-height: .9; color: var(--arena); }
.price b small { display: block; font-family: var(--b); font-size: 8pt; letter-spacing: .14em; text-transform: uppercase; color: #fff; opacity: .7; margin-bottom: 2mm; font-weight: 700; }
.price ul { padding-left: 4mm; display: grid; gap: 1.5mm; font-size: 10.5pt; }
.calendar { list-style: none; margin-top: 8mm; border-top: .6pt solid rgba(20,18,16,.3); }
.calendar li { display: grid; grid-template-columns: 78mm 1fr; gap: 6mm; padding: 3.5mm 0; border-bottom: .6pt solid rgba(20,18,16,.3); align-items: baseline; }
.calendar .when { font-family: var(--d); font-size: 13pt; letter-spacing: -.02em; color: var(--arcilla-osc); }
.calendar h3 { font-family: var(--d); font-weight: 400; font-size: 11pt; letter-spacing: -.02em; }
/* equipo */
.two { display: grid; grid-template-columns: 1fr 1fr; gap: 14mm; }
.box { border: .6pt solid rgba(20,18,16,.3); background: #fff; padding: 8mm; }
.logos { display: flex; gap: 10mm; align-items: center; margin: 4mm 0 6mm; }
.logos img { height: 13mm; width: auto; }
.logos { flex-wrap: nowrap; gap: 5mm; }
.logos > img { height: 10.5mm !important; }
.aa-logo { display: inline-flex; align-items: center; gap: 2.5mm; font-size: 6.5pt; font-weight: 700; line-height: 1.2; letter-spacing: .02em; }
.aa-logo img { height: 8.5mm !important; }
.aa-logo { font-size: 6pt; gap: 1.8mm; white-space: nowrap; }
.names { display: flex; flex-wrap: wrap; gap: 2mm; margin-top: 3mm; }
.names span { border: .6pt solid rgba(20,18,16,.35); border-radius: 99px; padding: 1mm 3mm; font-size: 8pt; font-weight: 700; }
/* contacto */
.contact { display: flex; flex-direction: column; justify-content: space-between; }
.contact .big { font-size: 80pt; }
.contact .cols a { color: inherit; text-decoration: underline; text-underline-offset: 1mm; }
.contact .cols { display: grid; grid-template-columns: 1.5fr 1.2fr .8fr 1fr; gap: 10mm; font-size: 10.5pt; border-top: .6pt solid rgba(255,255,255,.3); padding-top: 6mm; }
.contact .cols .label { opacity: .6; display: block; margin-bottom: 2mm; }
"""


CSS += """
/* v6 */
.cover .mark.big { font-size: 50pt; }
.emblem-cover { display: block; height: 30mm; width: auto; margin-bottom: 7mm; }
.brandline { display: inline-flex; align-items: center; gap: 2.5mm; }
.brandline img { height: 5.5mm; width: auto; }
.brandline.big { font-size: 16pt; gap: 5mm; }
.brandline.big img { height: 16mm; }
.cover .promise { margin-top: 7mm; font-family: var(--d); font-weight: 500; font-size: 13pt; letter-spacing: -.02em; }
.cover .promise span { display: block; padding: 1.6mm 0; border-top: .6pt solid rgba(20,18,16,.35); }
.deadline { display: flex; flex-wrap: wrap; gap: 2mm 3mm; align-items: center; font-weight: 700; font-size: 10pt; }
.deadline span { white-space: nowrap; }
.deadline span { background: var(--tinta); color: var(--crema); border-radius: 99px; padding: 1.2mm 3.5mm; font-size: 7pt; letter-spacing: .14em; text-transform: uppercase; }
.confirmed { margin-top: auto; margin-bottom: 14mm; border-top: .6pt solid rgba(20,18,16,.3); padding-top: 4mm; display: flex; gap: 5mm; align-items: baseline; }
.confirmed b { font-family: var(--d); font-weight: 400; font-size: 15pt; letter-spacing: -.02em; }
.grid4 { display: grid; grid-template-columns: repeat(4, 1fr); border-top: 1.5pt solid var(--tinta); margin-top: 12mm; }
.grid4 > div { padding: 6mm 5mm 0 0; } .grid4 > div + div { padding-left: 5mm; border-left: .6pt solid rgba(20,18,16,.3); }
.grid4 .k { font-family: var(--s); font-style: italic; font-size: 30pt; line-height: 1; display: block; margin-bottom: 4mm; }
.prod { display: grid; grid-template-columns: 1fr 1.2fr; gap: 14mm; align-items: center; padding-bottom: 24mm; }
.prod .intro h1 { font-size: 30pt; line-height: 1.05; margin: 6mm 0 7mm; }
.prod .intro .lead { font-size: 11pt; }
.cards2 { display: grid; grid-template-columns: 1fr 1fr; gap: 4mm; }
.cards2 > div { background: var(--crema); padding: 7mm 7mm 8mm; min-height: 58mm; }
.cards2 .k { font-family: var(--s); font-style: italic; font-size: 34pt; line-height: 1; color: var(--arcilla-osc); display: block; margin-bottom: 5mm; }
.cards2 h3 { font-family: var(--d); font-weight: 500; font-size: 14pt; letter-spacing: -.02em; margin-bottom: 2.5mm; }
.cards2 p { font-size: 9.5pt; line-height: 1.45; }
.grid4 h3 { font-family: var(--d); font-weight: 400; font-size: 13pt; letter-spacing: -.02em; margin-bottom: 2.5mm; }
.stack { position: absolute; top: 0; bottom: 0; right: 0; width: 50%; display: grid; grid-template-rows: 1.25fr 1fr; gap: 3mm; }
.stack img { width: 100%; height: 100%; object-fit: cover; display: block; min-height: 0; }
.ways { list-style: none; margin-top: 7mm; border-top: .6pt solid rgba(20,18,16,.3); }
.ways li { padding: 3.2mm 0; border-bottom: .6pt solid rgba(20,18,16,.3); }
.ways b { font-family: var(--d); font-weight: 400; font-size: 11.5pt; letter-spacing: -.02em; display: block; margin-bottom: 1mm; }
.glist { list-style: none; border-top: .6pt solid rgba(20,18,16,.3); margin-top: 7mm; }
.glist li { font-family: var(--d); font-size: 17pt; letter-spacing: -.03em; padding: 3mm 0; border-bottom: .6pt solid rgba(20,18,16,.3); }
.glist li::before { content: ""; display: inline-block; width: 2mm; height: 2mm; border-radius: 50%; background: var(--arcilla-osc); margin-right: 2.5mm; vertical-align: .6mm; }
.award { background: var(--tinta); color: #fff; padding: 9mm; display: flex; flex-direction: column; gap: 4mm; }
.award h3 { font-family: var(--d); font-weight: 400; font-size: 11pt; color: var(--arena); margin-bottom: 1mm; }
.incl { list-style: none; border-top: .6pt solid rgba(20,18,16,.3); }
.incl li { position: relative; padding: 2.6mm 0 2.6mm 6mm; border-bottom: .6pt solid rgba(20,18,16,.3); font-size: 10pt; }
.incl li::before { content: "✦"; position: absolute; left: 0; color: var(--arcilla-osc); }
.fee { background: var(--tinta); color: #fff; padding: 9mm; }
.fee b { display: block; font-family: var(--d); font-weight: 400; font-size: 30pt; letter-spacing: -.04em; line-height: .95; white-space: nowrap; color: var(--arena); margin: 2mm 0 5mm; }
.fee ul { padding-left: 4mm; display: grid; gap: 1.5mm; font-size: 9.5pt; }
"""


# IMÁGENES DEL DOSIER: pon la ruta de la foto en su hueco (None = hueco vacío reservado)
IMAGENES = {
    "portada": ("assets/dosier/fotos/portada-globos-sol.jpg", ("Foto de portada", "Cover photo")),
    "pausa-1": ("assets/dosier/fotos/globos-muro.jpg", ("Foto a página completa", "Full-page photo")),
    "render-1": ("assets/dosier/fotos/sagrado-florecer-dorado.jpg", ("Render de una instalación grande", "Render of a large installation")),
    "render-2": ("assets/dosier/fotos/lo-que-permanece-circulos.jpg", ("Render de una instalación grande", "Render of a large installation")),
    "pausa-2": ("assets/dosier/fotos/globos-capuchinos.jpg", ("Foto o render a página completa", "Full-page photo or render")),
    "pausa-3": ("assets/dosier/fotos/globos-c3a.jpg", ("Foto o render a página completa", "Full-page photo or render")),
}


def pic(key):
    path, hint = IMAGENES[key]
    if path:
        return f'<img src="{path}" alt="">'
    n = list(IMAGENES).index(key) + 1
    return f'<div class="ph"><div><span class="label">{t("Espacio para imagen", "Image placeholder")} {n:02d}</span><p>{T(hint)}</p></div></div>'


def full(key):
    return f'<section class="slide full">{pic(key)}</section>'


CSS += """
.full { padding: 0; }
.full > img, .full > .ph { position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; }
.ph { background: var(--cal); display: grid; place-items: center; text-align: center; padding: 8mm; min-height: 0; height: 100%; }
.ph > div { border: .8pt dashed rgba(20,18,16,.45); width: 100%; height: 100%; display: grid; place-content: center; gap: 2mm; color: rgba(20,18,16,.7); }
.ph p { font-family: var(--s); font-style: italic; font-size: 14pt; }
.arcilla .ph { background: var(--arena); }
"""


CSS += """
.lc { text-transform: none; }
.partners3 .box { padding: 5mm 6mm; }
.partners3 .box p { font-size: 8.5pt !important; line-height: 1.4; }
/* sin bloques negros: paleta con texto negro */
.arena-osc { background: var(--arena-osc); color: var(--tinta); }
.stats, .stats > div { border-color: rgba(20,18,16,.3) !important; }
.stats b { color: var(--tinta); }
.contact .cols { border-top-color: rgba(20,18,16,.35); }
.award { background: var(--arena); color: var(--tinta); }
.award h3 { color: var(--arcilla-osc); }
.fee { background: var(--arcilla); color: var(--tinta); }
.fee b { color: var(--tinta); }
.deadline span { background: var(--crema); color: var(--tinta); }
"""


def foot(n):
    return f'<div class="foot"><span class="brandline"><img src="{img('assets/logos/emblema-mini.svg')}" alt="">{MARK_LINE}</span><span>{t("Convocatoria de empresas · 2027", "Brand open call · 2027")}</span><span>{n:02d}</span></div>'


def deck():
    sl = []
    L = lambda: len(sl) + 1
    dl = f'<p class="deadline"><span>{t("Candidaturas abiertas", "Applications open")}</span>{t("hasta el", "until")} {T(DEADLINE)} · {t("15 plazas", "15 places")}</p>'
    # portada
    sl.append(f'''<section class="slide arcilla cover" style="padding-right:calc(50% + 14mm)">
  <div class="row"><span class="label">{t("Segunda edición · septiembre 2027 · Córdoba", "Second edition · September 2027 · Córdoba")}<br>{t("Festival internacional de arquitectura efímera", "International festival of ephemeral architecture")}</span></div>
  <div><img class="emblem-cover" src="{img('assets/logos/emblema.svg')}" alt="">{MARK.replace('class="mark"', 'class="mark big"')}<p class="sub" style="margin-top:9mm">{t("Convocatoria de empresas&nbsp;2027", "2027 brand open&nbsp;call")}</p>
    <p class="promise"><span>{t("15 plazas para empresas", "15 places for companies")}</span><span>{t("6 espacios patrimoniales y el C3A", "6 heritage venues and the C3A")}</span></p></div>
  <div>{dl}<p class="label" style="margin-top:6mm">Fundación Artdecor · MuDD Architects · AA School London</p></div>
  <div class="half">{pic("portada")}</div>
</section>''')
    # la propuesta
    sl.append(f'''<section class="slide">
  <div class="textcol"><span class="label" style="color:var(--arcilla-osc)">{t("La convocatoria", "The open call")}</span>
    <h1 class="d" style="font-size:30pt;margin:6mm 0 7mm">{t('Tu marca, un artista, <span class="it">un patio</span>.', 'Your brand, an artist, <span class="it">a patio</span>.')}</h1>
    <p class="lead">{t("Para la segunda edición de EFÍMERA CÓRDOBA seleccionaremos 15 empresas. Cada una crea una instalación en un espacio del festival: con un artista de su elección, con uno que le proponemos o in-house, con su propio equipo.", "For the second edition of EFÍMERA CÓRDOBA we will select 15 companies. Each one creates an installation in a festival venue: with an artist of its choice, with one we suggest, or in-house with its own team.")}</p>
    <p style="margin-top:5mm">{t("Durante todo septiembre de 2027, la obra se abre al público con entrada libre en el casco histórico de Córdoba, Patrimonio Mundial. Tu marca no solo pone un logo: forma parte de la obra.", "Throughout September 2027, the work is open to the public free of charge in Córdoba's World Heritage historic centre. Your brand doesn't just add a logo: it becomes part of the work.")}</p>
    <div class="confirmed"><span class="label" style="color:var(--arcilla-osc)">{t("Ya confirmada", "Already confirmed")}</span><img src="{img('assets/logos/keyter.png')}" alt="Keyter Group" style="height:5.5mm;display:block;margin-top:1.5mm"></div>
  </div>
  <div class="half"><img src="{img('assets/dosier/fotos/palmera-red.jpg')}" alt=""></div>{foot(L())}
</section>''')
    # cómo funciona
    steps = [(t("Presenta tu candidatura", "Apply"), t("Quiénes sois, qué espacio os interesa y qué queréis enseñar. Hasta el 28 de febrero de 2027.", "Who you are, which venue interests you and what you want to show. Until 28 February 2027.")),
             (t("Selección", "Selection"), t("La dirección artística estudia cada propuesta y elige a las empresas participantes.", "The artistic direction reviews every proposal and chooses the participating companies.")),
             (t("Creáis la instalación", "Create the installation"), t("Con un artista de vuestra elección, con uno que os proponemos o in-house. Un asistente de producción os acompaña, sin coste.", "With an artist of your choice, one we suggest, or in-house. A production assistant supports you, free of charge.")),
             (t("Septiembre, abierta a todos", "September, open to&nbsp;all"), t("Del 1 al 30 de septiembre de 2027, con entrada libre. Se desmonta el día 30.", "From 1 to 30 September 2027, free entry. It comes down on the 30th."))]
    st = "".join(f'<div><span class="k">{i + 1:02d}</span><h3>{h}</h3><p>{p}</p></div>' for i, (h, p) in enumerate(steps))
    sl.append(f'''<section class="slide cal">
  <span class="label" style="color:var(--arcilla-osc)">{t("Cómo funciona", "How it works")}</span>
  <h1 class="d" style="font-size:34pt;margin-top:6mm;max-width:220mm">{t('De la candidatura a <span class="it">un mes</span> de&nbsp;ciudad.', 'From application to <span class="it">a month</span> in the&nbsp;city.')}</h1>
  <div class="steps">{st}</div>{foot(L())}
</section>''')
    # foto a página completa entre «Cómo funciona» y «Tu producto»
    sl.append(full("pausa-1"))
    # producto dentro de la obra: titular a la izquierda, cuatro tarjetas a la derecha
    sh = "".join(f'<div><span class="k">{i + 1:02d}</span><h3>{T(h)}</h3><p>{T(p)}</p></div>' for i, (h, p) in enumerate(SHOWCASE))
    sl.append(f'''<section class="slide arcilla prod">
  <div class="intro"><span class="label">{t("Tu producto, dentro de la obra", "Your product, inside the work")}</span>
    <h1 class="d">{t('Aquí tu producto no se&nbsp;mira:&nbsp;<span class="it">se&nbsp;vive</span>.', "Here your product isn't looked&nbsp;at:&nbsp;<span class='it'>it's experienced</span>.")}</h1>
    <p class="lead">{t("Las instalaciones pueden ser interactivas: quien entra toca el material, activa la tecnología, recorre la pieza por dentro. Es la mejor forma de enseñar de qué es capaz lo que fabricáis.", "Installations can be interactive: visitors touch the material, trigger the technology, walk through the piece. It's the best way to show what your products can do.")}</p></div>
  <div class="cards2">{sh}</div>{foot(L())}
</section>''')
    # piensa en grande (RENDERS PROVISIONALES: sustituir cuando lleguen)
    wy = "".join(f'<li><b>{T(h)}</b>{T(p)}</li>' for h, p in WAYS)
    sl.append(f'''<section class="slide">
  <div class="textcol"><span class="label" style="color:var(--arcilla-osc)">{t("Piensa en grande", "Think big")}</span>
    <h1 class="d" style="font-size:28pt;margin:6mm 0 5mm">{t('Un patio entero <span class="it">para tu&nbsp;idea</span>.', 'A whole patio <span class="it">for your&nbsp;idea</span>.')}</h1>
    <p>{t("Instalaciones que ocupan un patio entero, cubren una capilla o se recorren por dentro. Tres maneras de crearlas:", "Installations that fill an entire patio, cover a chapel or can be walked through. Three ways to create them:")}</p>
    <ul class="ways">{wy}</ul></div>
  <div class="stack">{pic("render-1")}{pic("render-2")}</div>{foot(L())}
</section>''')
    # 2026 en cifras
    real = [("5", t("obras en espacios patrimoniales", "works in heritage venues")), ("30", t("días de festival", "festival days")),
            ("15", t("ponentes en el Lab", "Lab speakers")), (str(len(COLABORAN)), t("entidades colaboradoras", "supporting organisations"))]
    stats = "".join(f'<div><b>{T(n)}</b><span>{T(l)}</span></div>' for n, l in STATS_2026) + "".join(f'<div><b>{n}</b><span>{l}</span></div>' for n, l in real)
    strip = "".join(f'<div><img src="{img(o["card"])}" alt=""><small>{o["n"]} · {o["title"]}</small></div>' for o in OBRAS if o["card"])
    sl.append(f'''<section class="slide arena-osc">
  <span class="label" style="opacity:.6">{t("Primera edición · septiembre 2026", "First edition · September 2026")}</span>
  <h1 class="d" style="font-size:30pt;margin:5mm 0 7mm">{t('2026 en <span class="it">cifras</span>', '2026 in <span class="it">numbers</span>')}</h1>
  <div class="stats">{stats}</div>
  <div class="strip">{strip}</div>{foot(L())}
</section>''')
    # mapa
    ml = "".join(f'<li><span class="n">{x["n"]}</span><div><strong>{x["name"]}</strong><small>{x["addr"] or "Córdoba"}</small></div></li>' for x in SPACES)
    sl.append(f'''<section class="slide" style="padding-top:12mm;padding-bottom:12mm">
  <div class="mapwrap"><div>{build.mapa_svg()}</div>
    <div><span class="label" style="color:var(--arcilla-osc)">{t("Los espacios", "The venues")}</span>
      <h1 class="d" style="font-size:28pt;margin:5mm 0 3mm">{t('La ciudad como <span class="it">museo</span>.', 'The city as a <span class="it">museum</span>.')}</h1>
      <p style="margin-bottom:6mm">{t("Seis paradas a pie por el casco histórico, el C3A al otro lado del río y 15 instalaciones en total.", "Six stops on foot through the historic centre, the C3A across the river, and 15 installations in total.")}</p>
      <ol class="mlist">{ml}</ol></div></div>
</section>''')
    # espacios
    for x in SPACES:
        sl.append(f'''<section class="slide space">
  <div class="textcol"><span class="label" style="color:var(--arcilla-osc)">{t("Espacio", "Venue")} {x["n"]} / {len(SPACES):02d}</span>
    <span class="num" style="margin-top:6mm">{x["n"]}</span>
    <h2 class="d">{x["name"]}</h2>
    <p class="lead">{T(x["desc"])}</p>
    <div class="meta"><span><b>{t("Dirección", "Address")}:</b> {x["addr"] or "Córdoba"}</span><span>{T(x["was"])}</span><span><b>{t("Disponible", "Available")}:</b> {t("1–30 septiembre 2027 · varias instalaciones por espacio", "1–30 September 2027 · several installations per venue")}</span>{('<span style="opacity:.6">' + T(x["credit"]) + '</span>') if x.get("credit") else ""}</div>
  </div>
  <div class="half"><img src="assets/espacios/{x["img"]}.webp" alt=""></div>{foot(L())}
</section>''')
    sl.append(full("pausa-2"))
    # agenda profesional + premio
    gl = "".join(f"<li>{T(g)}</li>" for g in GUESTS)
    aw = "".join(f"<div><h3>{T(h)}</h3><p>{T(p)}</p></div>" for h, p in AWARD)
    sl.append(f'''<section class="slide">
  <div class="two" style="align-items:start">
    <div><span class="label" style="color:var(--arcilla-osc)">{t("Agenda profesional", "Professional programme")}</span>
      <h1 class="d" style="font-size:24pt;margin:5mm 0 5mm">{t('Tu instalación, ante quien&nbsp;<span class="it">decide</span>.', 'Your installation, in front of those who&nbsp;<span class="it">decide</span>.')}</h1>
      <p>{t("Durante septiembre, EFÍMERA invita a Córdoba a una lista de interioristas, arquitectos, propietarios de hoteles e invitados de negocio. Las empresas seleccionadas pueden quedar con ellos y enseñarles su instalación en persona.", "During September, EFÍMERA invites a list of interior designers, architects, hotel owners and business guests to Córdoba. Selected companies can meet them and show them their installation in person.")}</p>
      </div>
    <div class="award"><span class="label" style="opacity:.6">{t("Premio EFÍMERA 2027", "EFÍMERA Award 2027")}</span>
      <h2 class="d" style="font-size:22pt">{t('Premio a la mejor <span class="it">instalación</span>.', 'Award for the best <span class="it">installation</span>.')}</h2>
      <p>{t("Un jurado elige la instalación que mejor ha unido marca, arte y lugar. La entrega de premios es en la clausura, a finales de septiembre.", "A jury chooses the installation that best brings together brand, art and place. The award ceremony takes place at the closing, at the end of September.")}</p>
      {aw}</div>
  </div>{foot(L())}
</section>''')
    # qué te llevas
    gt = "".join(f'<div><span class="k">{i + 1:02d}</span><h3>{T(h)}</h3><p>{T(p)}</p></div>' for i, (h, p) in enumerate(GETS))
    sl.append(f'''<section class="slide arcilla">
  <span class="label">{t("Qué te llevas", "What you take away")}</span>
  <h1 class="d" style="font-size:36pt;margin-top:6mm;max-width:230mm">{t('Tu marca, contada <span class="it">por&nbsp;otros</span>.', 'Your brand, told <span class="it">by&nbsp;others</span>.')}</h1>
  <p class="lead" style="margin-top:6mm;max-width:200mm">{t("La instalación dura un mes; lo que se cuenta de ella, mucho más. Además de la obra, os lleváis material y visibilidad para seguir contándola.", "The installation lasts a month; what is said about it lasts much longer. Beyond the work, you take away material and visibility to keep telling its story.")}</p>
  <div class="grid4">{gt}</div>{foot(L())}
</section>''')
    # participar y condiciones
    inc = "".join(f"<li>{T(x)}</li>" for x in INCLUDES)
    sl.append(f'''<section class="slide arena">
  <span class="label" style="color:var(--arcilla-osc)">{t("Participar", "Taking part")}</span>
  <h1 class="d" style="font-size:28pt;margin:5mm 0 3mm">{t('No alquilas un espacio: <span class="it">firmas una obra</span>.', "You don't rent a venue: <span class='it'>you sign a work</span>.")}</h1>
  <p style="max-width:230mm;margin-bottom:7mm">{t("Lo que paga una empresa seleccionada no es un alquiler: es la oportunidad de crear, con un artista o con su equipo, una instalación en un espacio patrimonial y de presentar su marca ante miles de visitantes y una lista de invitados profesionales.", "What a selected company pays is not rent: it's the opportunity to create, with an artist or its own team, an installation in a heritage venue, and to present its brand to thousands of visitors and a list of professional guests.")}</p>
  <div class="two" style="gap:10mm">
    <div class="fee"><span class="label" style="opacity:.7">{t("Cuota de participación", "Participation fee")}</span><b>{t("Desde 3.000 €", "From €3,000")}</b>
      <ul><li>{t("Según el espacio y la escala de la instalación. Para todo septiembre de 2027.", "Depending on the venue and the scale of the installation. For all of September 2027.")}</li>
        <li>{t("Aparte, la empresa asume los honorarios de su artista, si trabaja con uno.", "In addition, the company covers its artist's fee, if it works with one.")}</li>
        <li>{t("Y la producción, el montaje y el desmontaje de la instalación (30 de septiembre).", "And the production, installation and dismantling of the piece (30 September).")}</li></ul></div>
    <div><span class="label">{t("Qué incluye", "What's included")}</span><ul class="incl" style="margin-top:3mm">{inc}</ul></div>
  </div>{foot(L())}
</section>''')
    # calendario
    cl = "".join(f'<li><span class="when">{w} 2027</span><div><h3>{h}</h3><p>{d}</p></div></li>' for w, h, d in [
        (t("Hasta el 28 febrero", "Until 28 February"), t("Candidaturas de empresas", "Company applications"), t("Cierre de la convocatoria: 15 plazas.", "The open call closes: 15 places.")),
        (t("Marzo", "March"), t("Selección", "Selection"), t("Comunicamos la resolución a todas las empresas candidatas.", "We let every applicant company know the outcome.")),
        (t("20–31 agosto", "20–31 August"), "Efímera Lab", t("Taller con estudiantes de la AA School de Londres.", "Workshop with students from London's AA School.")),
        (t("1–30 septiembre", "1–30 September"), t("Instalaciones abiertas al público", "Installations open to the public"), t("En los siete espacios, con la agenda profesional en paralelo.", "In all seven venues, with the professional programme alongside.")),
        (t("Finales de septiembre", "Late September"), t("Premio EFÍMERA", "EFÍMERA Award"), t("Entrega de premios en la clausura.", "Award ceremony at the closing.")),
        (t("30 septiembre", "30 September"), t("Desmontaje", "Dismantling"), t("Cada patio vuelve a ser patio.", "Each patio is a patio again."))])
    sl.append(f'''<section class="slide cal">
  <span class="label" style="color:var(--arcilla-osc)">{t("Calendario", "Calendar")}</span>
  <h1 class="d" style="font-size:30pt;margin-top:5mm">{t('2027, <span class="it">paso a paso</span>.', '2027, <span class="it">step by step</span>.')}</h1>
  <ol class="calendar">{cl}</ol>{foot(L())}
</section>''')
    # quién está detrás
    names = "".join(f"<span>{n}</span>" for n, _ in COLABORAN)
    sl.append(f'''<section class="slide">
  <span class="label" style="color:var(--arcilla-osc)">{t("Quién está detrás", "Who is behind it")}</span>
  <h1 class="d" style="font-size:28pt;margin:5mm 0 8mm">{t('Una red de <span class="it">oficio</span>, técnica y prensa.', 'A network of <span class="it">craft</span>, technique and press.')}</h1>
  <div class="two">
    <div class="partners3" style="display:grid;gap:3.5mm">
      <div class="box"><span class="label" style="color:var(--arcilla-osc)">{t("Partner técnico", "Technical partner")}</span><h2 style="margin:2.5mm 0 3mm"><img src="{img('assets/logos/shima-seiki.png')}" alt="Shima Seiki" style="height:4.2mm;display:block"></h2><p style="font-size:9pt">{T(SHIMA)}</p></div>
      <div class="box"><span class="label" style="color:var(--arcilla-osc)">{t("Socio de prensa", "Media partner")}</span><h2 style="margin:2mm 0 2.5mm"><img src="{img('assets/logos/dezeen.svg')}" alt="Dezeen" style="height:5.5mm;display:block"></h2><p style="font-size:9pt">{T(DEZEEN)}</p></div>
      <div class="box"><span class="label" style="color:var(--arcilla-osc)">{t("Empresa socia · ingeniería", "Partner company · engineering")}</span><h2 style="margin:2mm 0 2.5mm"><img src="{img('assets/logos/tyrens-akt.png')}" alt="Tyréns AKT" style="height:6.5mm;display:block"></h2><p style="font-size:9pt">{T(AKT)}</p></div></div>
    <div><span class="label">{t("Organizan, con la AA School", "Organised by, with the AA School")}</span>
      <div class="logos"><img src="{img('img/logos/artdecor.ae34de74.png')}" alt="Fundación Artdecor"><img src="{img('img/logos/mudd.6f8b5b97.png')}" alt="MuDD Architects"><span class="aa-logo"><img src="assets/logos/aa.svg" alt="Architectural Association"><span>Architectural Association<br>School of Architecture</span></span></div>
      <p>{t("Con la Architectural Association School of Architecture de Londres. Comisariado de Nina Chaltiel y Fernando Vacas.", "With the Architectural Association School of Architecture, London. Curated by Nina Chaltiel and Fernando Vacas.")}</p>
      <p class="label" style="margin-top:6mm">{t("Ya confirmados para 2027", "Already confirmed for 2027")}</p><div class="names"><span>Keyter Group</span><span>{t("Tyréns AKT (antes AKT II) · empresa socia", "Tyréns AKT (formerly AKT II) · partner company")}</span><span>{t("C3A · colaborador y espacio de intervención", "C3A · partner and installation venue")}</span></div>
      <p class="label" style="margin-top:6mm">{t("Colaboraron en 2026", "2026 supporters")}</p><div class="names">{names}</div></div>
  </div>{foot(L())}
</section>''')
    sl.append(full("pausa-3"))
    # contacto
    web = build.SITE + ("en/" + build.fname("patrocinio", "en") if build.LANG == "en" else build.fname("patrocinio", "es")) + "#candidatura"
    sl.append(f'''<section class="slide arcilla contact">
  <span class="label" style="opacity:.6">{t("Candidaturas hasta el", "Applications until")} {T(DEADLINE)}</span>
  <div><p class="d big" style="font-size:66pt">{t('Presenta tu <span class="it">candidatura</span>.', 'Submit your <span class="it">application</span>.')}</p>
    <p class="lead" style="margin-top:6mm;max-width:190mm">{t("Cuéntanos quiénes sois, qué queréis destacar y qué espacio os interesa. 15 plazas: revisamos cada propuesta.", "Tell us who you are, what you want to highlight and which venue interests you. 15 places: we review every proposal.")}</p></div>
  <div class="cols"><div><span class="label">{t("Candidatura online", "Apply online")}</span><a href="{web}">{t("Presenta la candidatura en la web →", "Apply on the website →")}</a></div>
    <div><span class="label">Email</span><a href="mailto:{MAIL}">{MAIL}</a></div><div><span class="label">Instagram</span><a href="{build.IG}">@efimera_fest</a></div>
    <div><span class="label">Fundación Artdecor</span>C/ Juramento, 1 · 14002 Córdoba</div></div>
  <div class="brandline big"><img src="{img('assets/logos/emblema.svg')}" alt="">{MARK_LINE}</div>
</section>''')
    fonts = '<link href="https://fonts.googleapis.com/css2?family=Unbounded:wght@400;500;700&family=Instrument+Serif:ital@0;1&family=DM+Sans:opsz,wght@9..40,400;9..40,700&display=block" rel="stylesheet">'
    return f'<!DOCTYPE html><html lang="{build.LANG}"><head><meta charset="utf-8"><title>EFÍMERA CÓRDOBA · {t("Convocatoria de empresas 2027", "2027 brand open call")}</title>{fonts}<style>{CSS}</style></head><body>{"".join(sl)}</body></html>'


def main():
    chrome = next((c for c in CHROME if Path(c).exists()), None)
    OUTDIR.mkdir(parents=True, exist_ok=True)
    prof = Path(sys.argv[1]) if len(sys.argv) > 1 else D / ".chrome-pdf"
    for lang in ("es", "en"):
        build.LANG = lang
        html = D / f"_dosier-{lang}.html"
        html.write_text(build.keep_mudd(deck()).replace('src="../assets/', 'src="assets/'), encoding="utf-8")
        out = OUTDIR / DOSIER[lang]
        subprocess.run([chrome, "--headless=new", "--disable-gpu", "--no-pdf-header-footer", f"--user-data-dir={prof}",
                        "--virtual-time-budget=20000", f"--print-to-pdf={out}", html.resolve().as_uri()], check=True, capture_output=True, timeout=180)
        import pymupdf, os
        doc = pymupdf.open(out)
        doc.rewrite_images(dpi_threshold=400, dpi_target=300, quality=92)
        doc.save(str(out) + ".tmp", garbage=4, deflate=True); n = len(doc); doc.close(); os.replace(str(out) + ".tmp", out)
        html.unlink()
        print("✓", out.name, n, "páginas", round(out.stat().st_size / 1024), "KB")


if __name__ == "__main__":
    main()
