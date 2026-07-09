# -*- coding: utf-8 -*-
"""Génère la version 2 (plus esthétique) du diaporama en HTML autonome."""
import json, os

SCR = os.path.dirname(os.path.abspath(__file__))
fonts = json.load(open(os.path.join(SCR, "fonts.json")))

LAT = "U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+0304,U+0308,U+0329,U+2000-206F,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD"
EXT = "U+0100-02BA,U+02BD-02C5,U+02C7-02CC,U+02CE-02D7,U+02DD-02FF,U+0304,U+0308,U+0329,U+1D00-1DBF,U+1E00-1E9F,U+1EF2-1EFF,U+2020,U+20A0-20AB,U+20AD-20C0,U+2113,U+2C60-2C7F,U+A720-A7FF"

def face(weight, slice_key, rng):
    d = fonts[slice_key]["b64"]
    return ("@font-face{font-family:'Fraunces';font-style:normal;font-weight:%d;font-display:swap;"
            "src:url(data:font/woff2;base64,%s) format('woff2');unicode-range:%s;}" % (weight, d, rng))

FONTS_CSS = "\n".join([
    face(600, "f600_latin", LAT), face(600, "f600_ext", EXT),
    face(400, "f380_latin", LAT), face(400, "f380_ext", EXT),
])

# ---------------------------------------------------------------- ICONS (line, 24x24)
ICONS = {
 "bolt":'<path d="M13 2 4 14h6l-1 8 10-12h-7l1-8z"/>',
 "building":'<path d="M4 21V6l8-3 8 3v15"/><path d="M9 21v-5h6v5"/><path d="M8 8h.01M12 8h.01M16 8h.01M8 12h.01M12 12h.01M16 12h.01"/>',
 "target":'<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1.3" fill="currentColor" stroke="none"/>',
 "book":'<path d="M5 4a2 2 0 0 1 2-2h11v18H7a2 2 0 0 0-2 2z"/><path d="M5 20a2 2 0 0 1 2-2h11"/>',
 "chip":'<rect x="6" y="6" width="12" height="12" rx="2"/><path d="M10 10h4v4h-4z"/><path d="M9 2v3M15 2v3M9 19v3M15 19v3M2 9h3M2 15h3M19 9h3M19 15h3"/>',
 "layers":'<path d="M12 3 3 8l9 5 9-5-9-5z"/><path d="M3 13l9 5 9-5"/>',
 "beaker":'<path d="M9 3h6M10 3v6l-5 8a2 2 0 0 0 2 3h10a2 2 0 0 0 2-3l-5-8V3"/><path d="M7.5 14h9"/>',
 "eye":'<path d="M2 12s4-7 10-7 10 7 10 7-4 7-10 7-10-7-10-7z"/><circle cx="12" cy="12" r="3"/>',
 "shield":'<path d="M12 3 5 6v6c0 4 3 7 7 8 4-1 7-4 7-8V6z"/><path d="M9.5 12l2 2 3.5-4"/>',
 "users":'<circle cx="9" cy="8" r="3.2"/><path d="M3 20a6 6 0 0 1 12 0"/><path d="M16 5.2a3.2 3.2 0 0 1 0 6M17 14a6 6 0 0 1 4 6"/>',
 "spark":'<path d="M12 3l2.2 5.8L20 11l-5.8 2.2L12 19l-2.2-5.8L4 11l5.8-2.2z"/>',
 "clipboard":'<rect x="6" y="4" width="12" height="17" rx="2"/><path d="M9 4V3h6v1"/><path d="M9 12l2 2 4-4"/>',
 "briefcase":'<rect x="3" y="7" width="18" height="13" rx="2"/><path d="M8 7V5a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"/><path d="M3 12h18"/>',
 "flag":'<path d="M5 21V4"/><path d="M5 4h12l-2.2 3.5L17 11H5"/>',
 "up":'<path d="M12 19V6M6 12l6-6 6 6"/>',
 "alert":'<path d="M12 3 2 20h20z"/><path d="M12 10v4M12 17h.01"/>',
 "compass":'<circle cx="12" cy="12" r="9"/><path d="M15.5 8.5 13 13l-4.5 2.5L11 11z"/>',
 "scale":'<path d="M12 3v18M7 21h10M5 7h14M5 7 3 13h4zM19 7l-2 6h4z"/><path d="M8 4l8-1"/>',
}
def ic(name, color, size, sw=1.7):
    return ('<svg viewBox="0 0 24 24" fill="none" stroke="%s" stroke-width="%s" '
            'stroke-linecap="round" stroke-linejoin="round" style="width:%scqw;height:%scqw;flex:none">%s</svg>'
            % (color, sw, size, size, ICONS[name]))

# ---------------------------------------------------------------- CSS
CSS = """
:root{
  --navy:#0B2A4A; --navy2:#123A61; --navy-deep:#07213C; --ink:#18243C;
  --amber:#E6A339; --amber-deep:#AF7112; --slate:#3D6A8E; --slate-deep:#2B5175;
  --grey:#5A footer; --muted:#5C6辞;
  --paper:#FCFBF8; --card:#FFFFFF; --border:#ECE7DC; --border2:#E4DED2;
  --cream:#F7F2E8; --mist:#EDF2F6; --sage:#EAF3EC; --blush:#F8EDE6;
  --green:#2F8B5D; --green-d:#246B48; --rust:#C15A3C; --rust-d:#A2452C;
  --bg:#E7E4DD; --bg2:#DED9CF; --chrome-ink:#2A3242; --chrome-sub:#6C7686; --chrome-line:#CBc;
}
""".replace("--grey:#5A footer;","--grey:#54607A;").replace("--muted:#5C6辞;","--muted:#5C667B;").replace("--chrome-line:#CBc;","--chrome-line:#C8CBD1;") + """
:root{ --grey:#54607A; --muted:#5C667B; }
@media (prefers-color-scheme:dark){
  :root{ --bg:#091320; --bg2:#0C1A2A; --chrome-ink:#DDE4EE; --chrome-sub:#8395AB; --chrome-line:#1D2F45; }
}
:root[data-theme="light"]{ --bg:#E7E4DD; --bg2:#DED9CF; --chrome-ink:#2A3242; --chrome-sub:#6C7686; --chrome-line:#C8CBD1; }
:root[data-theme="dark"]{ --bg:#091320; --bg2:#0C1A2A; --chrome-ink:#DDE4EE; --chrome-sub:#8395AB; --chrome-line:#1D2F45; }

*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;background:linear-gradient(180deg,var(--bg),var(--bg2));
  font-family:system-ui,-apple-system,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;color:var(--chrome-ink);-webkit-font-smoothing:antialiased;}
.serif{font-family:'Fraunces',Georgia,'Times New Roman',serif;}
.wrap{max-width:1200px;margin:0 auto;padding:26px 18px 96px;}
.topbar{display:flex;align-items:center;justify-content:space-between;gap:16px;flex-wrap:wrap;margin-bottom:22px;}
.topbar h1{font-family:'Fraunces',Georgia,serif;font-size:clamp(18px,2.4vw,24px);font-weight:600;margin:0;letter-spacing:.2px;}
.topbar .sub{font-size:12.5px;color:var(--chrome-sub);margin-top:4px;}
.hint{font-size:12px;color:var(--chrome-sub);border:1px solid var(--chrome-line);border-radius:999px;padding:7px 14px;white-space:nowrap;}
.hint b{color:var(--amber-deep)}
@media (prefers-color-scheme:dark){.hint b{color:var(--amber)}}
:root[data-theme="dark"] .hint b{color:var(--amber)}

.deck{display:flex;flex-direction:column;gap:28px;}
.slide{position:relative;width:100%;aspect-ratio:16/9;border-radius:16px;overflow:hidden;container-type:size;
  background:var(--paper);box-shadow:0 1px 2px rgba(10,20,35,.10),0 18px 44px rgba(10,20,35,.20);scroll-margin-top:16px;}
.pad{position:absolute;inset:0;padding:4.8cqw 5.4cqw 3.9cqw;display:flex;flex-direction:column;}

/* header */
.eyebrow{display:flex;align-items:center;gap:1cqw;font-size:1.42cqw;font-weight:600;letter-spacing:.19em;text-transform:uppercase;color:var(--slate);}
.eyebrow .ix{color:var(--amber-deep);font-family:'Fraunces',serif;font-weight:600;letter-spacing:0;}
.eyebrow .ic{display:inline-flex;color:var(--amber-deep)}
.h1{font-family:'Fraunces',Georgia,serif;font-weight:600;font-size:3.28cqw;line-height:1.05;color:var(--navy);margin:.6cqw 0 0;letter-spacing:.1px;text-wrap:balance;}
.rule{display:flex;align-items:center;gap:.7cqw;margin-top:1.5cqw;}
.rule i{display:block;width:5.4cqw;height:.34cqw;background:linear-gradient(90deg,var(--amber),#F2C879);border-radius:2px;}
.rule b{width:.7cqw;height:.7cqw;background:var(--amber);border-radius:50%;transform:rotate(45deg);}
.body{flex:1;display:flex;flex-direction:column;justify-content:center;margin-top:1.5cqw;}

/* footer */
.foot{position:absolute;left:5.6cqw;right:5.6cqw;bottom:2.15cqw;display:flex;justify-content:space-between;align-items:center;
  font-size:1.04cqw;color:#9AA3B2;border-top:1px solid var(--border);padding-top:1.1cqw;}
.foot .pg{font-family:'Fraunces',serif;font-weight:600;color:var(--amber-deep);}
.tabL{position:absolute;left:0;top:5.6cqw;width:.55cqw;height:9.5cqw;background:var(--amber);border-radius:0 3px 3px 0;}

/* cards */
.grid{display:grid;gap:2cqw;}
.card{background:var(--card);border:1px solid var(--border);border-radius:1.9cqw;padding:2.5cqw 2.4cqw;
  box-shadow:0 1px 2px rgba(10,20,35,.05),0 10px 24px rgba(10,20,35,.05);}
.chead{display:flex;align-items:center;gap:1cqw;font-size:1.5cqw;font-weight:700;letter-spacing:.07em;text-transform:uppercase;}
.chead .cic{width:2.9cqw;height:2.9cqw;border-radius:.9cqw;display:flex;align-items:center;justify-content:center;flex:none;}
ul.b{list-style:none;margin:1.5cqw 0 0;padding:0;display:flex;flex-direction:column;gap:1.15cqw;}
ul.b li{font-size:1.72cqw;line-height:1.32;color:var(--grey);padding-left:2.5cqw;position:relative;}
ul.b li::before{content:"";position:absolute;left:0;top:.62cqw;width:.85cqw;height:.85cqw;background:var(--amber);border-radius:.18cqw;transform:rotate(45deg);}
ul.b li b{color:var(--ink);font-weight:700;}
.dense ul.b{gap:.7cqw}
.dense ul.b li{font-size:1.5cqw;line-height:1.26}
.dense .card{padding:2.0cqw 2.1cqw}
.dense .chead{font-size:1.4cqw}
.dense .tint{padding:1.5cqw 1.8cqw}

/* stat tile */
.stat{display:flex;flex-direction:column;gap:.2cqw;}
.stat .n{font-family:'Fraunces',serif;font-weight:600;font-size:3.5cqw;line-height:.95;color:var(--navy);letter-spacing:-.5px;}
.stat .n.am{color:var(--amber-deep)}
.stat .c{font-size:1.28cqw;color:var(--muted);line-height:1.25;}

/* title slide */
.slide.title{background:radial-gradient(120% 130% at 82% 12%,#164575 0%,var(--navy) 42%,var(--navy-deep) 100%);}
.slide.section{background:radial-gradient(120% 130% at 80% 15%,#164575 0%,var(--navy) 45%,var(--navy-deep) 100%);}
.bandtop{position:absolute;left:0;top:0;height:.9cqw;width:100%;background:linear-gradient(90deg,var(--amber),#F2C879 60%,var(--amber));}
.tkick{display:flex;align-items:center;gap:1.1cqw;font-size:1.55cqw;font-weight:600;letter-spacing:.2em;text-transform:uppercase;color:var(--amber);}
.ttitle{font-family:'Fraunces',Georgia,serif;font-weight:600;font-size:5.2cqw;line-height:1.03;color:#fff;margin:2.1cqw 0 0;letter-spacing:.2px;}
.tsub{font-family:'Fraunces',serif;font-style:italic;font-weight:400;font-size:2.5cqw;color:#D8E2EE;margin-top:2.2cqw;}
.tsub2{font-size:1.6cqw;color:#93A6BD;margin-top:1cqw;max-width:74%;line-height:1.4;}
.tmeta{position:absolute;left:5.6cqw;right:5.6cqw;bottom:3.4cqw;display:flex;gap:3.4cqw;font-size:1.42cqw;color:#C6D3E2;border-top:1px solid rgba(255,255,255,.14);padding-top:1.5cqw;}
.tmeta b{color:#fff;font-weight:600}
.tmeta .lab{color:var(--amber);font-weight:600;letter-spacing:.08em;text-transform:uppercase;font-size:1.12cqw;display:block;margin-bottom:.3cqw}
.deco{position:absolute;right:5cqw;top:8cqw;width:26cqw;height:26cqw;opacity:.5;pointer-events:none}

/* section divider */
.snum{font-family:'Fraunces',serif;font-weight:600;font-size:15cqw;line-height:.82;color:transparent;-webkit-text-stroke:.16cqw #2C517A;letter-spacing:-1px;}
.sec-wrap{position:absolute;inset:0;display:flex;flex-direction:column;justify-content:center;padding:0 6cqw;}
.skick{display:flex;align-items:center;gap:1.1cqw;font-size:1.5cqw;font-weight:600;letter-spacing:.2em;text-transform:uppercase;color:var(--amber);margin-bottom:1.4cqw}
.stitle{font-family:'Fraunces',Georgia,serif;font-weight:600;font-size:4.7cqw;color:#fff;margin-top:1.6cqw;line-height:1.03}
.ssub{font-size:1.75cqw;color:#AFC0D4;margin-top:1.3cqw;max-width:70%;line-height:1.4}
.sdots{position:absolute;right:6cqw;bottom:6cqw;display:grid;grid-template-columns:repeat(3,1fr);gap:1.1cqw}
.sdots span{width:1cqw;height:1cqw;border-radius:50%;background:#26476C}
.sdots span.on{background:var(--amber)}

/* result slide */
.kbadge{display:flex;align-items:center;gap:1.4cqw;background:linear-gradient(100deg,var(--navy),var(--navy2));border-radius:1.3cqw;
  padding:1.3cqw 1.8cqw;position:relative;overflow:hidden;box-shadow:0 8px 20px rgba(11,42,74,.18)}
.kbadge::before{content:"";position:absolute;left:0;top:0;bottom:0;width:.6cqw;background:var(--amber)}
.kbadge .ci{width:3.4cqw;height:3.4cqw;border-radius:.9cqw;background:rgba(230,163,57,.16);display:flex;align-items:center;justify-content:center;flex:none;margin-left:.5cqw}
.kbadge .kt{font-size:1.58cqw;color:#EAF1F8;line-height:1.26}
.kbadge .kt b{color:var(--amber);font-weight:700}
.litt{display:flex;align-items:flex-start;gap:1.1cqw;background:var(--cream);border:1px solid var(--border2);border-radius:1cqw;padding:1.05cqw 1.5cqw;}
.litt .q{font-family:'Fraunces',serif;font-size:2.8cqw;line-height:.7;color:var(--amber);margin-top:.6cqw}
.litt .lt{font-size:1.3cqw;color:var(--ink);line-height:1.3}
.litt .lt b{color:var(--slate-deep);font-weight:700}

/* mini viz */
.viz8{display:flex;gap:.7cqw}
.viz8 span{width:1.7cqw;height:1.7cqw;border-radius:50%;background:var(--amber);box-shadow:0 1px 2px rgba(0,0,0,.12)}
.matrix{display:grid;grid-template-columns:auto repeat(3,1fr);gap:.55cqw;align-items:center}
.matrix .mh{font-size:1.12cqw;color:var(--muted);text-align:center;font-weight:600}
.matrix .rl{font-size:1.18cqw;color:var(--ink);font-weight:700;padding-right:.8cqw;white-space:nowrap}
.matrix .cell{height:2.7cqw;border-radius:.55cqw;background:var(--mist);border:1px solid var(--border2);display:flex;align-items:center;justify-content:center}
.matrix .cell b{width:1.1cqw;height:1.1cqw;border-radius:50%;background:var(--amber)}
.matrix .cell.e{background:#fff}

/* pills / chips */
.qchip{display:inline-flex;align-items:center;justify-content:center;background:var(--slate);color:#fff;font-weight:700;border-radius:.7cqw;font-size:1.5cqw;font-family:'Fraunces',serif;padding:.2cqw 0}
.numbig{font-family:'Fraunces',serif;font-weight:600;color:#E9EDF2;font-size:4.6cqw;line-height:.9}
.tint{border-radius:1.6cqw;padding:1.9cqw 2cqw}

/* rail */
.rail{position:fixed;right:15px;top:50%;transform:translateY(-50%);display:flex;flex-direction:column;gap:8px;z-index:20}
.rail a{width:9px;height:9px;border-radius:50%;background:var(--chrome-line);transition:.2s}
.rail a:hover,.rail a.on{background:var(--amber);transform:scale(1.3)}
@media (max-width:820px){.rail{display:none}}
.fnote{margin-top:36px;text-align:center;font-size:12px;color:var(--chrome-sub)}
a{color:inherit}
"""

FOOT = '<div class="foot"><span>Maxime LOUSTALET&nbsp;&nbsp;·&nbsp;&nbsp;Soutenance de mémoire&nbsp;&nbsp;·&nbsp;&nbsp;Eklore-ed School of Management&nbsp;&nbsp;·&nbsp;&nbsp;2025–2026</span><span class="pg">%s</span></div>'

def eyebrow(ix, icon, text):
    return ('<div class="eyebrow"><span class="ic">%s</span><span class="ix">%s</span>&nbsp;·&nbsp;%s</div>'
            % (ic(icon, "var(--amber-deep)", 2.0), ix, text))

def header(ix, icon, kick, title):
    return ('<div class="tabL"></div>'
            + eyebrow(ix, icon, kick)
            + '<div class="h1 serif">%s</div><div class="rule"><i></i><b></b></div>' % title)

def cic(color, bg):
    return 'style="background:%s;color:%s"' % (bg, color)

def slide(cls, inner):
    return '<section class="slide %s">%s</section>' % (cls, inner)

def content(page, ix, icon, kick, title, body, dense=False):
    d = " dense" if dense else ""
    return slide("content"+d, '<div class="pad">'+header(ix,icon,kick,title)
                 +'<div class="body">'+body+'</div></div>'+(FOOT%page))

def bullets(items):
    lis = "".join("<li>%s</li>" % it for it in items)
    return '<ul class="b">%s</ul>' % lis

def card(chead_html, inner, extra=""):
    return '<div class="card" style="%s">%s%s</div>' % (extra, chead_html, inner)

def chead(icon, color, bg, label, labcolor=None):
    lc = labcolor or "var(--navy)"
    return ('<div class="chead" style="color:%s"><span class="cic" %s>%s</span>%s</div>'
            % (lc, cic(color,bg), ic(icon,color,1.7), label))

SLIDES = []

# ---- 1 TITLE
deco = ('<svg class="deco" viewBox="0 0 200 200" fill="none" stroke="#E6A339" stroke-width="1">'
        '<circle cx="100" cy="100" r="88" opacity=".35"/><circle cx="100" cy="100" r="66" opacity=".5"/>'
        '<circle cx="100" cy="100" r="44" opacity=".7"/><circle cx="100" cy="100" r="22"/>'
        '<line x1="100" y1="2" x2="100" y2="198" opacity=".25"/><line x1="2" y1="100" x2="198" y2="100" opacity=".25"/></svg>')
SLIDES.append(slide("title", '<div class="bandtop"></div>'+deco
  +'<div class="pad" style="justify-content:center">'
  +'<div class="tkick">'+ic("spark","var(--amber)",1.9)+'&nbsp;Soutenance de mémoire de fin d\'études · Master 2</div>'
  +'<div class="ttitle serif">L\'intégration de l\'intelligence<br>artificielle dans les PME</div>'
  +'<div class="tsub serif">Entre opportunités perçues et freins organisationnels</div>'
  +'<div class="tsub2">Le cas de l\'intégration de nouveaux outils numériques au sein d\'Arla Groupe, PME du bâtiment</div>'
  +'</div>'
  +'<div class="tmeta"><div><span class="lab">Auteur</span><b>Maxime LOUSTALET</b></div>'
  +'<div><span class="lab">Directeur de recherche</span><b>Victor COMBES</b></div>'
  +'<div><span class="lab">Établissement</span><b>Eklore-ed School of Management</b></div></div>'))

# ---- 2 PLAN
plan = [("01","Contexte & problématique","Un enjeu d'actualité, un terrain, une question","target"),
        ("02","Cadre théorique & propositions","PME, culture, IA : ce que dit la littérature","book"),
        ("03","Méthodologie empirique","Étude qualitative — 8 entretiens semi-directifs","beaker"),
        ("04","Résultats & analyse","Trois questions de recherche sur le terrain","eye"),
        ("05","Apports & préconisations","Contributions et recommandations managériales","clipboard"),
        ("06","Conclusion & limites","Réponse, apport professionnel, perspectives","flag")]
cards = ""
for n,t,d,icn in plan:
    am = n in ("01","02","03")
    col = "var(--amber-deep)" if am else "var(--slate-deep)"
    bg = "var(--cream)" if am else "var(--mist)"
    cards += ('<div class="card" style="padding:1.7cqw 1.8cqw;display:flex;align-items:center;gap:1.4cqw">'
      +'<span class="cic" style="width:3.3cqw;height:3.3cqw;border-radius:1cqw;background:%s;color:%s">%s</span>' % (bg,col,ic(icn,col,1.9))
      +'<div><div style="display:flex;align-items:baseline;gap:.8cqw"><span class="serif" style="font-size:1.7cqw;font-weight:600;color:%s">%s</span>' % (col,n)
      +'<span class="serif" style="font-size:1.72cqw;font-weight:600;color:var(--navy)">%s</span></div>' % t
      +'<div style="font-size:1.24cqw;color:var(--muted);margin-top:.15cqw">%s</div></div></div>' % d)
body = '<div class="grid" style="grid-template-columns:1fr 1fr;gap:1.5cqw">%s</div>' % cards
SLIDES.append(content("2","—","layers","Fil conducteur de la présentation","Plan de la soutenance", body))

# ---- section divider helper
def divider(num, kick, title, sub, page, oncount):
    dots = ""
    for i in range(9):
        dots += '<span class="%s"></span>' % ("on" if i < oncount else "")
    return slide("section",
      '<div class="tabL" style="background:var(--amber);top:0;height:100%%;width:.5cqw"></div>'
      +'<div class="sec-wrap"><div class="snum serif">%s</div>' % num
      +'<div class="skick">%s&nbsp;%s</div>' % (ic("compass","var(--amber)",1.9), kick)
      +'<div class="stitle serif">%s</div><div class="ssub">%s</div></div>' % (title, sub)
      +'<div class="sdots">%s</div>' % dots
      +(FOOT%page).replace("var(--amber-deep)","#7C8CA3").replace("#9AA3B2","#6E7E96").replace("var(--border)","rgba(255,255,255,.12)"))

# ---- 3 DIV 01
SLIDES.append(divider("01","Première partie","Contexte & problématique","Un enjeu d'actualité majeur, un terrain concret, une question de recherche","3",1))

# ---- 4 CONTEXTE
left = card(chead("bolt","var(--amber-deep)","var(--cream)","Une vague inédite","var(--amber-deep)"),
  bullets(["<b>ChatGPT, Copilot, Gamma…</b> l'IA générative entre dans le travail quotidien.",
           "<b>Industrie 4.0</b> : automatisation, données, IA (Rouas &amp; Al Meriouh, 2025).",
           "<b>Un levier stratégique</b> de productivité et de compétitivité."])
  +'<div style="display:flex;gap:2.4cqw;margin-top:1.1cqw;padding-top:1.1cqw;border-top:1px solid var(--border)">'
  +'<div class="stat"><div class="n am serif">≈14%</div><div class="c">du PIB mondial porté par l\'IA d\'ici 2030 (≈ 15 000 Md$)</div></div></div>',
  extra="flex:1")
right = card(chead("building","var(--slate-deep)","var(--mist)","La PME, un cas à part","var(--slate-deep)"),
  bullets(["<b>Ressources limitées</b> : financières, humaines, technologiques.",
           "<b>Dirigeant central</b> et structure souple (Nassou &amp; Bennani, 2024).",
           "<b>Poids des traditions</b> et de la culture (Schein, 2015 ; Torrès, 1999)."])
  +'<div style="display:flex;gap:2.4cqw;margin-top:1.1cqw;padding-top:1.1cqw;border-top:1px solid var(--border)">'
  +'<div class="stat"><div class="n serif">≈90%</div><div class="c">des entreprises mondiales sont des PME (Farsad, 2021)</div></div></div>',
  extra="flex:1")
body = ('<div style="font-size:1.52cqw;color:var(--grey);margin-bottom:1.4cqw;max-width:96%">'
        'Une <b style="color:var(--ink)">bascule technologique</b> traverse toutes les organisations — mais la PME l\'aborde dans des conditions singulières. De ce contraste naît la <b style="color:var(--ink)">tension</b> au cœur de ce travail.</div>'
        +'<div class="grid" style="grid-template-columns:1fr 1fr">%s%s</div>' % (left,right))
SLIDES.append(content("4","01","bolt","Contexte & actualité","Une bascule technologique, un angle mort : la PME", body, dense=True))

# ---- 5 TERRAIN + PROBLEMATIQUE
terrain = card(chead("building","var(--slate-deep)","var(--mist)","Le terrain — Arla Groupe","var(--slate-deep)"),
  bullets(["<b>PME du bâtiment</b> : maçonnerie, construction métallique, bureau d'études.",
           "<b>Métiers variés</b> : dirigeants, métreurs, conducteurs de travaux, commerciaux, RH, terrain.",
           "<b>Déjà des usages IA</b> : ChatGPT, Copilot, Gamma au quotidien.",
           "<b>Le constat</b> : un usage individuel, spontané, non encadré."]), extra="flex:1")
prob = ('<div class="tint" style="background:linear-gradient(120deg,var(--navy),var(--navy2));position:relative;overflow:hidden">'
  +'<div style="position:absolute;right:-3cqw;top:-3cqw;opacity:.12">'+ic("target","#E6A339",22,1.2)+'</div>'
  +'<div style="display:flex;align-items:center;gap:.9cqw;color:var(--amber);font-weight:700;letter-spacing:.1em;font-size:1.4cqw;text-transform:uppercase">'+ic("target","var(--amber)",1.9)+'Problématique</div>'
  +'<div class="serif" style="color:#fff;font-style:italic;font-weight:400;font-size:1.98cqw;line-height:1.26;margin-top:1cqw">'
  +'« Comment les PME peuvent-elles intégrer l\'IA et les technologies numériques tout en tenant compte de leurs ressources limitées, de leur structure organisationnelle et de leur culture d\'entreprise ? »</div></div>')
qrs = ""
for a,b in [("QR1","Comment les salariés perçoivent-ils l'IA ?"),
            ("QR2","Quels freins organisationnels, humains, culturels ?"),
            ("QR3","En quoi les spécificités PME influencent l'adoption ?")]:
    qrs += ('<div style="display:flex;align-items:center;gap:1.1cqw;margin-top:.85cqw">'
      +'<span class="qchip" style="width:6cqw;height:2.5cqw">%s</span>' % a
      +'<span style="font-size:1.42cqw;color:var(--ink)">%s</span></div>' % b)
body = '<div class="grid" style="grid-template-columns:.92fr 1.08fr;align-items:start">%s<div>%s<div style="margin-top:.6cqw">%s</div></div></div>' % (terrain, prob, qrs)
SLIDES.append(content("5","01","compass","Terrain & problématique","Arla Groupe : un usage réel de l'IA, mais non encadré", body))

# ---- 6 DIV 02
SLIDES.append(divider("02","Deuxième partie","Cadre théorique & propositions","Ce que la littérature nous apprend sur les PME et sur l'IA","6",2))

# ---- 7 CADRE 1 PME
def theo(icon, color, bg, title, items):
    return ('<div class="card" style="padding:0;overflow:hidden">'
      +'<div style="display:flex;align-items:center;gap:.9cqw;padding:1.3cqw 1.5cqw;background:%s;color:%s;font-weight:700;letter-spacing:.05em;text-transform:uppercase;font-size:1.32cqw">%s%s</div>' % (bg,color,ic(icon,color,1.7),title)
      +'<div style="padding:1.4cqw 1.5cqw">'+bullets(items).replace('gap:1.15cqw','gap:.95cqw').replace('font-size:1.72cqw','font-size:1.4cqw')+'</div></div>')
c1 = theo("scale","var(--slate-deep)","var(--mist)","Définition",
     ["<b>Critères UE</b> : &lt; 250 salariés, CA &lt; 50 M€ (Oriot &amp; Misiaszek, 2012).",
      "<b>Structure simple</b> et peu formalisée (Nassou &amp; Bennani, 2024)."])
c2 = theo("users","var(--amber-deep)","var(--cream)","Proximité",
     ["<b>Dirigeant impliqué</b> au quotidien, décisions rapides.",
      "<b>« Proximité organisationnelle »</b> : atout relationnel clé (Torrès, 1999)."])
c3 = theo("book","var(--navy)","#E7EDF3","Culture &amp; traditions",
     ["<b>Culture = valeurs partagées</b> qui guident les décisions (Schein, 2015).",
      "<b>Traditions de métier</b> : artisan de métier vs entrepreneurial (Blanchard &amp; Albert-Cromarias, 2022)."])
prop = ('<div style="display:flex;align-items:center;gap:1.6cqw;margin-top:1.3cqw;background:var(--cream);border-left:.55cqw solid var(--amber);border-radius:.5cqw 1cqw 1cqw .5cqw;padding:1.2cqw 1.8cqw">'
  +'<span class="serif" style="font-size:1.5cqw;font-weight:600;color:var(--amber-deep);white-space:nowrap;letter-spacing:.04em">Proposition 1</span>'
  +'<span style="font-size:1.5cqw;color:var(--ink);line-height:1.3">Les caractéristiques structurelles et culturelles de la PME (dirigeant, proximité, traditions) <b>façonnent la manière dont elle accueille — ou freine — l\'IA</b>.</span></div>')
body = '<div class="grid" style="grid-template-columns:1fr 1fr 1fr;gap:1.5cqw">%s%s%s</div>%s' % (c1,c2,c3,prop)
SLIDES.append(content("7","02","book","Cadre théorique · 1/2","La PME : un objet organisationnel spécifique", body))

# ---- 8 CADRE 2 IA
opp = card(chead("up","var(--green-d)","var(--sage)","Opportunités","var(--green-d)"),
  bullets(["<b>Transformation digitale → performance</b> organisationnelle (Radoui &amp; Cherradi, 2025).",
           "<b>Analyse prédictive &amp; agilité</b> (Bennour &amp; Oukassi, 2025).",
           "<b>Automatisation</b> des tâches répétitives à faible valeur."]), extra="flex:1")
men = card(chead("alert","var(--rust-d)","var(--blush)","Freins & menaces","var(--rust-d)"),
  bullets(["<b>Données, compétences, intégration</b> au SI (Kokina et al., 2025 ; Duarte, 2025).",
           "<b>Enjeux éthiques</b> : biais, opacité, confidentialité.",
           "<b>Dépendance cognitive</b> : l'IA amplifie les vulnérabilités humaines (Soro Torna, 2024)."]), extra="flex:1")
prop = ('<div style="display:flex;align-items:center;gap:1.6cqw;margin-top:1.15cqw;background:var(--cream);border-left:.55cqw solid var(--amber);border-radius:.5cqw 1cqw 1cqw .5cqw;padding:1.15cqw 1.8cqw">'
  +'<span class="serif" style="font-size:1.5cqw;font-weight:600;color:var(--amber-deep);white-space:nowrap;letter-spacing:.04em">Proposition 2</span>'
  +'<span style="font-size:1.5cqw;color:var(--ink);line-height:1.3">L\'adoption de l\'IA ne dépend pas que de la technologie : elle se joue <b>autant sur des facteurs humains, organisationnels et culturels</b> que techniques.</span></div>')
body = '<div class="grid" style="grid-template-columns:1fr 1fr">%s%s</div>%s' % (opp,men,prop)
SLIDES.append(content("8","02","chip","Cadre théorique · 2/2","L'IA : un levier de performance et un défi organisationnel", body, dense=True))

# ---- 9 SYNTHESE
lev = '<div class="tint" style="background:var(--sage)"><div style="display:flex;align-items:center;gap:.8cqw;color:var(--green-d);font-weight:700;text-transform:uppercase;letter-spacing:.06em;font-size:1.4cqw">%s Leviers</div><div style="font-size:1.6cqw;color:var(--ink);margin-top:.7cqw;line-height:1.35">Flexibilité · proximité relationnelle · réactivité · dirigeant moteur</div></div>' % ic("up","var(--green-d)",1.7)
fre = '<div class="tint" style="background:var(--blush)"><div style="display:flex;align-items:center;gap:.8cqw;color:var(--rust-d);font-weight:700;text-transform:uppercase;letter-spacing:.06em;font-size:1.4cqw">%s Freins</div><div style="font-size:1.6cqw;color:var(--ink);margin-top:.7cqw;line-height:1.35">Ressources limitées · compétences · traditions · absence de cadre commun</div></div>' % ic("alert","var(--rust-d)",1.7)
props = ""
for a,b in [("QR1","La perception de l'IA dépend surtout du métier et de l'usage réel — pas seulement de l'âge."),
            ("QR2","Les freins sont pluriels (humains, financiers, organisationnels) et varient selon les profils."),
            ("QR3","Les spécificités PME (dirigeant, proximité, traditions) conditionnent l'adoption de l'IA.")]:
    props += ('<div style="display:flex;gap:1.2cqw;align-items:stretch;margin-top:.8cqw">'
      +'<span class="qchip" style="width:6cqw;font-size:1.55cqw;display:flex;align-items:center;justify-content:center">%s</span>' % a
      +'<span style="flex:1;background:var(--paper);border:1px solid var(--border);border-radius:.9cqw;padding:.85cqw 1.4cqw;font-size:1.46cqw;color:var(--ink);display:flex;align-items:center">%s</span></div>' % b)
body = ('<div class="grid" style="grid-template-columns:1fr 1fr;gap:1.6cqw;margin-bottom:1.7cqw">%s%s</div>' % (lev,fre)
  +'<div class="serif" style="font-size:1.72cqw;font-weight:600;color:var(--navy);margin-bottom:.4cqw">Trois propositions confrontées au terrain</div>%s' % props)
SLIDES.append(content("9","02","layers","Synthèse","De la théorie aux propositions de recherche", body))

# ---- 10 DIV 03
SLIDES.append(divider("03","Troisième partie","Méthodologie empirique","Une étude qualitative exploratoire fondée sur 8 entretiens semi-directifs","10",3))

# ---- 11 METHODO (with matrix viz)
why = card(chead("beaker","var(--slate-deep)","var(--mist)","Pourquoi le qualitatif ?","var(--slate-deep)"),
  bullets(["<b>Explorer le « pourquoi » et le « comment »</b> des comportements (Jando, 2024).",
           "<b>8 entretiens semi-directifs</b> · 10 questions ouvertes · enregistrés.",
           "<b>Analyse thématique</b> : ≈ 5 h de transcription + verbatims (Annexes 2 &amp; 3)."]), extra="flex:1")
# matrix 3 profils x 3 ages, 8 filled (one empty bottom-right)
cells = ""
mh = ["", "18–29", "30–44", "45 +"]
rows = ["Dirigeants","Bureau","Terrain"]
cells += "".join('<div class="mh">%s</div>' % h for h in mh)
grid = [[1,1,1],[1,1,1],[1,1,0]]
for ri,r in enumerate(rows):
    cells += '<div class="rl">%s</div>' % r
    for c in grid[ri]:
        cells += '<div class="cell%s">%s</div>' % ("" if c else " e", "<b></b>" if c else "")
matrix = card(chead("users","var(--amber-deep)","var(--cream)","Échantillonnage raisonné","var(--amber-deep)"),
  '<div class="matrix" style="margin-top:1.4cqw">%s</div>' % cells
  +'<div style="font-size:1.22cqw;color:var(--muted);margin-top:1.2cqw;line-height:1.35">3 familles de profils × 3 tranches d\'âge — <b style="color:var(--ink)">8 entretiens</b> couvrant l\'ensemble des situations.</div>', extra="flex:1")
body = '<div class="grid" style="grid-template-columns:1fr 1fr">%s%s</div>' % (why, matrix)
SLIDES.append(content("11","03","beaker","Démarche empirique","Une étude qualitative exploratoire assumée", body))

# ---- 12 DIV 04
SLIDES.append(divider("04","Quatrième partie","Résultats & analyse","Trois questions de recherche confrontées aux 8 entretiens","12",4))

# ---- result slide builder
def result(page, ix, icon, kick, title, keyicon, key, items, litt, viz=None):
    kb = ('<div class="kbadge"><div class="ci">%s</div><div class="kt"><b>Résultat clé — </b>%s</div></div>'
          % (ic(keyicon,"var(--amber)",2.0), key))
    lb = '<div class="litt"><span class="q serif">”</span><div class="lt"><b>Lien littérature — </b>%s</div></div>' % litt
    mid = bullets(items)
    if viz:
        mid = '<div style="display:flex;gap:2.2cqw;align-items:center">%s%s</div>' % (bullets(items), viz)
    body = kb + '<div style="margin:1.5cqw 0">'+mid+'</div>' + lb
    return content(page, ix, icon, kick, title, body, dense=True)

# ---- 13 QR1
SLIDES.append(result("13","04","eye","Question de recherche 1","Comment les salariés perçoivent-ils l'IA ?","eye",
  "une perception globalement positive, mais un usage isolé et non concerté.",
  ["<b>Le gain de temps, unanime :</b> se recentrer sur les tâches à valeur ajoutée ; « arrêter la bureautique basique ».",
   "<b>Les non-utilisateurs ne rejettent pas :</b> l'ouvrier (57 ans) et le dirigeant (63 ans) invoquent un « manque d'utilité », pas un refus.",
   "<b>Une lecture par le métier :</b> bureau automatisable vs terrain — « le béton ne se verse pas de lui-même ».",
   "<b>L'âge ne suffit pas :</b> « certains jeunes restent très attachés à leurs habitudes ».",
   "<b>Un usage individuel :</b> « c'est une affaire personnelle », sans savoir « jusqu'où on a le droit »."],
  "valide Bennour &amp; Oukassi (2025) sur la productivité ; illustre le défaut de structure collective (Kokina et al., 2025)."))

# ---- 14 QR2
SLIDES.append(result("14","04","shield","Question de recherche 2","Quels sont les freins à l'adoption de l'IA ?","shield",
  "des freins pluriels ; le frein prioritaire n'est pas le même selon les profils.",
  ["<b>Deux freins partagés :</b> la formation / l'accompagnement (unanime) et la contrainte financière.",
   "<b>Un frein propre à chaque profil :</b> appréhension psychologique (RH), esprit critique (achat), confidentialité chantier (conducteur).",
   "<b>Un frein émergent, absent de la littérature :</b> la peur d'une perte de compétences par sur-délégation (métreur).",
   "<b>La résistance = ancrage des habitudes :</b> « 40 ans qu'on travaille ainsi » — vigilance professionnelle, pas rejet idéologique.",
   "<b>Un frein structurel, le plus facile à lever :</b> l'absence de politique commune."],
  "confirme Kokina et al. (2025) &amp; Duarte (2025) ; l'ancrage renvoie à Schein (2015) et Blanchard &amp; Albert-Cromarias (2022)."))

# ---- 15 QR3 (with 8/8 viz)
viz8 = ('<div style="flex:none;text-align:center"><div class="serif" style="font-size:4.4cqw;font-weight:600;color:var(--navy);line-height:1">8<span style="color:var(--muted);font-size:2.4cqw">/8</span></div>'
  +'<div class="viz8" style="margin-top:.9cqw;max-width:9cqw;flex-wrap:wrap">'+''.join('<span></span>' for _ in range(8))+'</div>'
  +'<div style="font-size:1.14cqw;color:var(--muted);margin-top:.9cqw;max-width:9cqw;line-height:1.25">entretiens citent le rôle du dirigeant</div></div>')
SLIDES.append(result("15","04","users","Question de recherche 3","En quoi les spécificités PME influencent-elles l'adoption ?","users",
  "le dirigeant est décisif (8/8) ; proximité et traditions sont un cadre, pas un mur.",
  ["<b>Rôle du dirigeant — convergence totale :</b> « si les dirigeants ne sont pas convaincus, le changement sera plus lent ».",
   "<b>La proximité, levier ET risque :</b> elle diffuse les bonnes pratiques mais peut propager les résistances (Torrès, 1999).",
   "<b>La contrainte financière, différenciée :</b> gérable en grand public, bloquante sur le sur-mesure ; + un enjeu concurrentiel inédit.",
   "<b>Top-down vs participatif :</b> la direction impulse, mais le terrain aspire à co-décider — « c'est un référendum ».",
   "<b>Les traditions = adoption sélective :</b> personne ne rejette l'IA au nom du métier."],
  "valide Nassou &amp; Bennani (2024) et Torrès (1999) ; complète Blanchard &amp; Albert-Cromarias (2022) par l'« adoption sélective ».",
  viz=viz8))

# ---- 16 APPORTS
ap = [("bolt","Vigilance ≠ refus","La distance des non-utilisateurs est une vigilance professionnelle temporaire, pas un rejet."),
      ("users","Un seul dirigeant moteur suffit","Inutile de convaincre tout l'encadrement pour enclencher la dynamique."),
      ("alert","Le risque de perte de compétences","La sur-délégation à l'IA fait craindre une érosion du savoir-faire — peu documenté."),
      ("scale","La dimension concurrentielle","Ne pas investir dans l'IA devient un désavantage compétitif pour la PME."),
      ("book","L'« adoption sélective »","La tradition n'est pas un frein : elle est le cadre de l'adoption, métier par métier.")]
def apcard(i, icon, t, d, wide=False):
    return ('<div class="card" style="padding:0;overflow:hidden;display:flex;align-items:stretch;%s">' % ("grid-column:1 / -1;" if wide else "")
      +'<div style="background:linear-gradient(160deg,var(--navy),var(--navy2));width:6cqw;flex:none;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:.5cqw">'
      +'<span class="serif" style="font-size:2.7cqw;font-weight:600;color:var(--amber)">%d</span>%s</div>' % (i, ic(icon,"rgba(255,255,255,.55)",1.7))
      +'<div style="padding:1.3cqw 1.7cqw;display:flex;flex-direction:column;justify-content:center">'
      +'<div class="serif" style="font-size:1.78cqw;font-weight:600;color:var(--navy)">%s</div>' % t
      +'<div style="font-size:1.4cqw;color:var(--grey);margin-top:.35cqw;line-height:1.3">%s</div></div></div>' % d)
cards = "".join(apcard(i+1,*ap[i]) for i in range(4)) + apcard(5,*ap[4],wide=True)
body = '<div class="grid" style="grid-template-columns:1fr 1fr;gap:1.4cqw">%s</div>' % cards
SLIDES.append(content("16","04","spark","Apports scientifiques","Cinq résultats non anticipés par le modèle théorique", body))

# ---- 17 DIV 05
SLIDES.append(divider("05","Cinquième partie","Apports & préconisations","Trois recommandations opérationnelles pour Arla Groupe","17",5))

# ---- 18 PRECONISATIONS
prec = [("01","Structurer une politique commune","pilotée par un référent IA interne",
         ["1–2 outils communs à tous","Un coordinateur IA (informaticien recruté)","Des règles claires de confidentialité"],
         "Frein visé : absence de cadre commun","clipboard"),
        ("02","Déployer une formation différenciée","par les gains rapides et le compagnonnage",
         ["Cibler les « quick wins » métier","Former des ambassadeurs internes","Tutorat plutôt que théorie externe"],
         "Frein visé : formation & compétences","users"),
        ("03","Adopter une démarche participative","portée par la direction, co-construite",
         ["Vision claire portée par le dirigeant","Espace de dialogue avec les équipes","Respect des identités métier"],
         "Frein visé : tension top-down / adhésion","compass")]
cards = ""
for n,t,s,li,fr,icn in prec:
    lis = "".join('<li style="font-size:1.38cqw">%s</li>' % x for x in li)
    cards += ('<div class="card" style="padding:0;overflow:hidden;display:flex;flex-direction:column">'
      +'<div style="background:linear-gradient(140deg,var(--navy),var(--navy2));padding:1.4cqw 1.5cqw;display:flex;align-items:center;gap:1cqw">'
      +'<span class="serif" style="font-size:2.8cqw;font-weight:600;color:var(--amber)">%s</span>' % n
      +'<span style="color:#fff;font-weight:600;font-size:1.5cqw;line-height:1.15">%s</span>'
        '<span style="margin-left:auto;color:rgba(255,255,255,.5)">%s</span></div>' % (t, ic(icn,"rgba(255,255,255,.5)",2.1))
      +'<div style="padding:1.4cqw 1.5cqw;flex:1">'
      +'<div style="color:var(--slate-deep);font-style:italic;font-size:1.36cqw;margin-bottom:.6cqw">%s</div>' % s
      +'<ul class="b" style="gap:.75cqw">%s</ul></div>' % lis
      +'<div style="background:var(--cream);padding:.9cqw 1.5cqw;color:var(--amber-deep);font-weight:600;font-size:1.24cqw;display:flex;align-items:center;gap:.7cqw">%s%s</div></div>' % (ic("target","var(--amber-deep)",1.5), fr))
body = '<div class="grid" style="grid-template-columns:1fr 1fr 1fr;gap:1.5cqw">%s</div>' % cards
SLIDES.append(content("18","05","clipboard","Préconisations managériales","Trois leviers pour une intégration durable de l'IA", body))

# ---- 19 APPORT PRO
pro = [("compass","var(--amber-deep)","var(--cream)","Une posture de conduite du changement","Une technologie ne s'impose pas : elle s'accompagne, s'explique et se co-construit."),
       ("clipboard","var(--slate-deep)","var(--mist)","Un livrable directement actionnable","Un plan en 3 préconisations que je porte concrètement chez Arla Groupe, mon entreprise d'alternance."),
       ("eye","var(--amber-deep)","var(--cream)","Des compétences d'analyse","Mener des entretiens, écouter, structurer des verbatims, relier théorie et terrain."),
       ("briefcase","var(--slate-deep)","var(--mist)","Une vision stratégique du numérique","Un atout pour mon projet : accompagner la transformation digitale des organisations.")]
cards = ""
for icn,col,bg,t,d in pro:
    cards += card(chead(icn,col,bg,t,"var(--navy)").replace('font-size:1.5cqw','font-size:1.62cqw').replace('text-transform:uppercase;','').replace('letter-spacing:.07em;',''),
      '<div style="font-size:1.46cqw;color:var(--grey);margin-top:.9cqw;line-height:1.36">%s</div>' % d,
      extra="border-left:.5cqw solid %s" % col)
body = '<div class="grid" style="grid-template-columns:1fr 1fr;gap:1.5cqw">%s</div>' % cards
SLIDES.append(content("19","05","briefcase","Apport dans ma vie professionnelle","Ce que ce mémoire m'apporte, et apporte à l'entreprise", body))

# ---- 20 CONCLUSION
rep = ('<div class="tint" style="background:linear-gradient(120deg,var(--navy),var(--navy2));position:relative;overflow:hidden">'
  +'<div style="display:flex;align-items:center;gap:.9cqw;color:var(--amber);font-weight:700;letter-spacing:.08em;text-transform:uppercase;font-size:1.34cqw">'+ic("flag","var(--amber)",1.7)+'La réponse</div>'
  +'<div style="color:#fff;font-size:1.72cqw;line-height:1.32;margin-top:.7cqw">L\'adoption de l\'IA en PME dépend autant de facteurs <b>humains</b> qu\'<b>organisationnels</b>. Les spécificités de la PME ne sont pas un frein insurmontable, mais <b style="color:var(--amber)">le cadre à prendre en compte</b> pour réussir l\'intégration.</div></div>')
fk = '<div class="card" style="background:var(--mist);border:none"><div style="display:flex;align-items:center;gap:.8cqw;color:var(--navy);font-weight:700;text-transform:uppercase;font-size:1.3cqw;letter-spacing:.05em">%s Facteurs clés</div>%s</div>' % (ic("users","var(--navy)",1.6), bullets(["Rôle du dirigeant","Proximité entre salariés","Contraintes financières","Identités professionnelles"]).replace('font-size:1.72cqw','font-size:1.4cqw').replace('gap:1.15cqw','gap:.5cqw').replace('margin:1.5cqw','margin:.9cqw'))
lm = '<div class="card" style="background:var(--blush);border:none"><div style="display:flex;align-items:center;gap:.8cqw;color:var(--rust-d);font-weight:700;text-transform:uppercase;font-size:1.3cqw;letter-spacing:.05em">%s Limites</div>%s</div>' % (ic("alert","var(--rust-d)",1.6), bullets(["8 entretiens, une seule PME","Résultats non généralisables","Part de subjectivité","Instantané dans le temps"]).replace('font-size:1.72cqw','font-size:1.4cqw').replace('gap:1.15cqw','gap:.5cqw').replace('margin:1.5cqw','margin:.9cqw').replace('background:var(--amber)','background:var(--rust)'))
ov = '<div class="card" style="background:var(--sage);border:none"><div style="display:flex;align-items:center;gap:.8cqw;color:var(--green-d);font-weight:700;text-transform:uppercase;font-size:1.3cqw;letter-spacing:.05em">%s Ouverture</div><div style="font-size:1.42cqw;color:var(--ink);margin-top:.9cqw;line-height:1.36">Prolonger par une étude <b>quantitative</b> auprès de tous les salariés, pour hiérarchiser les freins et prioriser les préconisations.</div></div>' % ic("up","var(--green-d)",1.6)
body = rep + '<div class="grid" style="grid-template-columns:1fr 1fr 1fr;gap:1.4cqw;margin-top:1.3cqw">%s%s%s</div>' % (fk,lm,ov)
SLIDES.append(content("20","06","flag","Conclusion & perspectives","Ce qu'il faut retenir", body, dense=True))

# ---- 21 MERCI
SLIDES.append(slide("title", '<div class="bandtop"></div>'
  +'<div style="position:absolute;left:0;bottom:0;height:.9cqw;width:100%;background:linear-gradient(90deg,var(--amber),#F2C879 60%,var(--amber))"></div>'
  + deco.replace('class="deco"','class="deco" style="right:5cqw;top:7cqw;width:26cqw;height:26cqw;opacity:.4"')
  +'<div class="pad" style="justify-content:center">'
  +'<div class="tkick">'+ic("spark","var(--amber)",1.9)+'&nbsp;Merci</div>'
  +'<div class="ttitle serif" style="font-size:5.4cqw">Merci de votre attention</div>'
  +'<div class="rule" style="margin-top:1.8cqw"><i style="width:6cqw"></i><b></b></div>'
  +'<div class="tsub serif" style="font-size:2.1cqw">Je suis à votre disposition pour échanger et répondre à vos questions.</div>'
  +'<div style="margin-top:3.4cqw;font-size:1.6cqw;color:#fff;font-weight:600">Maxime LOUSTALET <span style="color:#93A6BD;font-weight:400">· L\'intégration de l\'IA dans les PME — le cas d\'Arla Groupe</span></div>'
  +'<div style="font-size:1.28cqw;color:#7C8FA8;margin-top:.5cqw">Directeur de recherche : Victor COMBES · Eklore-ed School of Management · 2025–2026</div>'
  +'</div>'))

# ---- 22 SIGNATURE / MISE EN ABYME
ai_deco = ('<svg class="deco" style="right:6cqw;top:9cqw;width:22cqw;height:22cqw;opacity:.42" viewBox="0 0 200 200" fill="none" stroke="#E6A339" stroke-width="1">'
  '<circle cx="100" cy="100" r="86" opacity=".3"/><circle cx="100" cy="100" r="62" opacity=".45"/>'
  '<circle cx="100" cy="100" r="38" opacity=".65"/>'
  '<path d="M100 66l7 20 20 7-20 7-7 20-7-20-20-7 20-7z" fill="#E6A339" stroke="none" opacity=".9"/></svg>')
SLIDES.append(slide("title",
  '<div class="bandtop"></div>'
  +'<div style="position:absolute;left:0;bottom:0;height:.9cqw;width:100%;background:linear-gradient(90deg,var(--amber),#F2C879 60%,var(--amber))"></div>'
  + ai_deco
  +'<div class="pad" style="justify-content:center">'
  +'<div class="tkick">'+ic("spark","var(--amber)",1.9)+'&nbsp;Mise en abyme · clin d\'œil final</div>'
  +'<div class="ttitle serif" style="font-size:4.7cqw;max-width:80%">Réalisé avec Claude,<br>une intelligence artificielle</div>'
  +'<div class="rule" style="margin-top:1.9cqw"><i style="width:6cqw"></i><b></b></div>'
  +'<div class="tsub serif" style="font-size:2.05cqw;max-width:82%">Le sujet de ce mémoire — l\'intégration de l\'IA — mis en pratique jusque dans sa soutenance.</div>'
  +'<div class="tsub2" style="max-width:80%;margin-top:1.3cqw">L\'intelligence artificielle y a servi d\'outil d\'appui — recherche documentaire, structuration et mise en forme — au service d\'un travail pensé, piloté, relu et assumé par son auteur.</div>'
  +'</div>'
  +'<div class="tmeta"><div><span class="lab">Auteur</span><b>Maxime LOUSTALET</b></div>'
  +'<div><span class="lab">Outil d\'appui</span><b>Claude — Anthropic</b></div>'
  +'<div><span class="lab">Principe</span><b>L\'IA assiste, l\'humain décide</b></div></div>'))

# ---------------------------------------------------------------- ASSEMBLE
SCRIPT = """
<nav class="rail" id="rail"></nav>
<script>
var slides=[].slice.call(document.querySelectorAll('.slide'));
var rail=document.getElementById('rail');
slides.forEach(function(s,i){s.id=s.id||('s'+(i+1));var a=document.createElement('a');a.href='#'+s.id;a.title='Diapo '+(i+1);rail.appendChild(a);});
var dots=[].slice.call(rail.children);
var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){var i=slides.indexOf(e.target);dots.forEach(function(d,j){d.classList.toggle('on',j===i);});}});},{threshold:.55});
slides.forEach(function(s){io.observe(s);});
function cur(){var b=0,bd=1e9;slides.forEach(function(s,i){var d=Math.abs(s.getBoundingClientRect().top-16);if(d<bd){bd=d;b=i;}});return b;}
window.addEventListener('keydown',function(e){
 if(e.key==='ArrowDown'||e.key==='PageDown'||e.key===' '){e.preventDefault();slides[Math.min(slides.length-1,cur()+1)].scrollIntoView({behavior:'smooth'});}
 if(e.key==='ArrowUp'||e.key==='PageUp'){e.preventDefault();slides[Math.max(0,cur()-1)].scrollIntoView({behavior:'smooth'});}
});
</script>
"""

HTML = ('<title>Soutenance MFE — Maxime LOUSTALET — Diaporama</title>\n<style>'
  + FONTS_CSS + "\n" + CSS + '</style>\n'
  + '<div class="wrap"><div class="topbar"><div>'
  + '<h1>Soutenance de mémoire — Diaporama</h1>'
  + '<div class="sub">Maxime LOUSTALET · L\'intégration de l\'IA dans les PME — le cas d\'Arla Groupe · 2025–2026</div></div>'
  + '<div class="hint">Navigation : <b>↑ ↓</b> ou molette · 22 diapositives</div></div>'
  + '<div class="deck" id="deck">' + "\n".join(SLIDES) + '</div>'
  + '<div class="fnote">Aperçu web du diaporama — le fichier PowerPoint (.pptx) éditable reprend les mêmes diapositives et les notes du présentateur.</div>'
  + '</div>' + SCRIPT)

open(os.path.join("/home/user/maxime","apercu-diaporama.html"),"w",encoding="utf-8").write(HTML)
print("written apercu-diaporama.html ;", len(HTML), "chars ;", len(SLIDES), "slides")
