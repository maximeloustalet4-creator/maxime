# -*- coding: utf-8 -*-
"""Jeu de cartes 88.9x63.5mm — style INFOGRAPHIE "chiffres clés" :
tuiles pleine couleur, gros pictogramme, gros chiffre, légende courte, badge numéro.
Assemblées en 3x4 (ordre ligne par ligne) = une infographie. Versos = logo Éklore."""
import json, os, base64
SCR=os.path.dirname(os.path.abspath(__file__))
fonts=json.load(open(os.path.join(SCR,"fonts.json")))
qr=open(os.path.join(SCR,"qr.svg")).read()
POSTER="data:image/png;base64,"+open(os.path.join(SCR,"poster.b64")).read()
LOGO="data:image/png;base64,"+open(os.path.join(SCR,"logo_small.b64")).read()

LAT="U+0000-00FF,U+0131,U+0152-0153,U+2000-206F,U+20AC,U+2122,U+2212"
EXT="U+0100-02BA,U+1E00-1E9F,U+2C60-2C7F,U+A720-A7FF"
def face(w,k,r): return "@font-face{font-family:'Fraunces';font-weight:%d;font-display:swap;src:url(data:font/woff2;base64,%s) format('woff2');unicode-range:%s;}"%(w,fonts[k]['b64'],r)
FONTS="\n".join([face(600,'f600_latin',LAT),face(600,'f600_ext',EXT),face(400,'f380_latin',LAT),face(400,'f380_ext',EXT)])

ICONS={
 "bolt":'<path d="M13 2 4 14h6l-1 8 10-12h-7l1-8z"/>',
 "target":'<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1.5" fill="currentColor" stroke="none"/>',
 "book":'<path d="M12 6C9 3.5 5.5 3.5 3 4v13c2.5-.5 6-.5 9 2 3-2.5 6.5-2.5 9-2V4c-2.5-.5-6-.5-9 2z"/><path d="M12 6v13"/>',
 "chip":'<rect x="6" y="6" width="12" height="12" rx="2"/><path d="M10 10h4v4h-4z"/><path d="M9 2v3M15 2v3M9 19v3M15 19v3M2 9h3M2 15h3M19 9h3M19 15h3"/>',
 "beaker":'<path d="M9 3h6M10 3v6l-5 8a2 2 0 0 0 2 3h10a2 2 0 0 0 2-3l-5-8V3"/><path d="M7.5 14h9"/>',
 "eye":'<path d="M2 12s4-7 10-7 10 7 10 7-4 7-10 7-10-7-10-7z"/><circle cx="12" cy="12" r="3"/>',
 "shield":'<path d="M12 3 5 6v6c0 4 3 7 7 8 4-1 7-4 7-8V6z"/><path d="M9.2 12l2 2 3.6-4"/>',
 "users":'<circle cx="9" cy="8" r="3.4"/><path d="M2.5 20a6.5 6.5 0 0 1 13 0"/><path d="M16 5a3.4 3.4 0 0 1 0 6.4M17.5 14a6 6 0 0 1 4 6"/>',
 "clipboard":'<rect x="6" y="4" width="12" height="17" rx="2"/><path d="M9 4V3h6v1"/><path d="M9.5 12l1.8 1.8L15 10"/>',
 "flag":'<path d="M5 21V4"/><path d="M5 4h13l-2.4 3.8L18 12H5"/>',
 "qr":'<rect x="3" y="3" width="7" height="7" rx="1"/><rect x="14" y="3" width="7" height="7" rx="1"/><rect x="3" y="14" width="7" height="7" rx="1"/><path d="M14 14h3v3M20.5 14v.01M14 20.5v.01M20.5 20.5v.01M17.5 17.5h.01"/>',
}
def ic(n,c,s,sw=2.0): return '<svg viewBox="0 0 24 24" fill="none" stroke="%s" stroke-width="%s" stroke-linecap="round" stroke-linejoin="round" style="width:%smm;height:%smm">%s</svg>'%(c,sw,s,s,ICONS[n])

NAVY="#0B2A4A"; BLUE="#1466A6"; SLATE="#3D6A8E"; TEAL="#178F8F"; GREEN="#2F8B5D"; AMBER="#E6A339"; INK="#0B2A4A"
COLS,ROWS=3,4
def pos(n): return ((n-1)//COLS,(n-1)%COLS)   # ligne par ligne

# (num, section, icon, tile, focal, caption, quote)
C=[
 (1,"Mémoire · Soutenance",None,NAVY,None,None,None),  # carte-titre
 (2,"Contexte","bolt",BLUE,"≈14%","du PIB mondial capté par l'IA d'ici 2030 — mais la PME a peu de moyens.",None),
 (3,"Problématique","target",TEAL,"?","Adopter l'IA sans trahir sa culture, ses moyens et sa façon de travailler.",None),
 (4,"Cadre · la PME","book",AMBER,"< 250","salariés : le seuil d'une PME. Le patron partout, les traditions comptent.",None),
 (5,"Cadre · l'IA","chip",SLATE,"2","visages de l'IA : un atout ET un risque (trop s'y fier).",None),
 (6,"Méthode","users",BLUE,"8","entretiens, du dirigeant à l'ouvrier, de 18 à 60 ans.",None),
 (7,"Résultat 1 · Perception","eye",TEAL,"6/8","utilisent déjà l'IA — mais chacun dans son coin.","« Le béton ne se verse pas de lui-même. »"),
 (8,"Résultat 2 · Freins","shield",NAVY,"≠","Le frein n°1 change selon les gens — et la peur de perdre la main.","« 40 ans qu'on travaille comme ça. »"),
 (9,"Résultat 3 · Dirigeant","users",AMBER,"8/8","citent le dirigeant comme le facteur décisif de l'adoption.","« S'ils ne sont pas convaincus, ça traîne. »"),
 (10,"Préconisations","clipboard",SLATE,"3","leviers : cadre commun, formation par les pairs, décision partagée.",None),
 (11,"Conclusion","flag",TEAL,"↔","Autant d'humain que d'organisation : les spécificités de la PME ne sont pas un mur, mais le cadre.",None),
 (12,"Pour aller plus loin","qr",NAVY,None,None,None),
]

def contrast(tile): return NAVY if tile==AMBER else "#fff"

def badge(n,tile):
    fg=contrast(tile)
    return '<div class="badge" style="color:%s"><span class="serif">%s</span></div>'%(tile, str(n))

def focal_size(f):
    L=len(f)
    return 40 if L<=1 else (37 if L<=2 else (26 if L<=4 else 20))

def tile(n,section,icon,col,focal,caption,quote):
    fg=contrast(col)
    dim="rgba(11,42,74,.14)" if col==AMBER else "rgba(255,255,255,.13)"
    deco='<span class="blob" style="background:%s"></span>'%dim
    top='<div class="top"><div class="badge" style="color:%s"><span class="serif">%s</span></div><div class="sec" style="color:%s">%s</div></div>'%(col,n,fg,section.upper())
    if n==1:
        body=('<div class="tbody">'
          +'<div class="tkick" style="color:%s">Les cartes clés de ma démonstration</div>'%(AMBER)
          +'<div class="ttitle serif">L\'intégration de l\'intelligence artificielle dans les PME</div>'
          +'<div class="tsub">Entre opportunités et freins — le cas d\'Arla Groupe</div>'
          +'<img class="tlogo" src="%s" alt="Éklore"/></div>'%LOGO)
        return '<div class="card" style="background:%s;color:%s">%s%s%s</div>'%(col,fg,deco,top,body)
    if n==12:
        body=('<div class="qmain"><div class="qbox">%s</div>'%qr
          +'<div class="qtxt">Scanne pour le <b>diaporama animé</b> de la soutenance.<br><span style="color:%s">Réalisé avec Claude — l\'IA assiste, l\'humain décide.</span></div></div>'%(AMBER))
        return '<div class="card" style="background:%s;color:%s">%s%s%s</div>'%(col,fg,deco,top,body)
    picto='<div class="pic" style="background:%s">%s</div>'%(dim, ic(icon,fg,15,2.1))
    fsz=focal_size(focal)
    q='<div class="q">%s</div>'%quote if quote else ''
    main=('<div class="main"><div class="txt">'
      +'<div class="focal serif" style="font-size:%spt;color:%s">%s</div>'%(fsz,fg,focal)
      +'<div class="cap">%s</div>%s</div>%s</div>'%(caption,q,picto))
    return '<div class="card" style="background:%s;color:%s">%s%s%s</div>'%(col,fg,deco,top,main)

def back(n,mirror=True):
    r,c=pos(n)
    posx=(c/(COLS-1))*100; posy=(r/(ROWS-1))*100
    mir="transform:scaleX(-1);" if mirror else ""
    return '<div class="card back"><div class="tile" style="%sbackground-image:url(%s);background-size:%d%% %d%%;background-position:%.4f%% %.4f%%"></div></div>'%(mir,POSTER,COLS*100,ROWS*100,posx,posy)

fronts=[tile(*c) for c in C]; backs=[back(c[0]) for c in C]; reveal=[back(c[0],False) for c in C]
def sheets(cards):
    out=""
    for i in range(0,len(cards),8): out+='<div class="sheet">%s</div>'%("".join(cards[i:i+8]))
    return out

CSS=FONTS+"""
*{box-sizing:border-box} body{margin:0;background:#DED9CF;font-family:system-ui,-apple-system,'Segoe UI',Roboto,sans-serif}
.serif{font-family:'Fraunces',Georgia,serif}
.sheet{width:210mm;height:297mm;background:#fff;margin:8mm auto;display:grid;grid-template-columns:88.9mm 88.9mm;grid-auto-rows:63.5mm;justify-content:center;align-content:start;gap:6mm 8mm;padding:14mm 0;page-break-after:always;box-shadow:0 3mm 8mm rgba(0,0,0,.15)}
.card{width:88.9mm;height:63.5mm;border-radius:3mm;overflow:hidden;position:relative;padding:4.5mm 5mm}
.blob{position:absolute;width:34mm;height:34mm;border-radius:50%;right:-9mm;bottom:-11mm}
.top{display:flex;align-items:center;gap:2.6mm;position:relative;z-index:2}
.badge{width:8mm;height:8mm;border-radius:50%;background:#fff;display:flex;align-items:center;justify-content:center;flex:none}
.badge .serif{font-size:13pt;font-weight:600;line-height:1}
.sec{font-size:6.6pt;font-weight:700;letter-spacing:.1em;text-transform:uppercase;opacity:.95}
.main{display:flex;align-items:center;gap:3mm;height:calc(100% - 9mm);position:relative;z-index:2}
.txt{flex:1;min-width:0}
.focal{font-weight:600;line-height:.98;letter-spacing:-.5px}
.cap{font-size:8.2pt;line-height:1.28;margin-top:1.4mm;opacity:.96}
.q{font-family:'Fraunces',serif;font-style:italic;font-size:7.6pt;margin-top:1.6mm;opacity:.9}
.pic{width:24mm;height:24mm;border-radius:50%;flex:none;display:flex;align-items:center;justify-content:center}
/* title card */
.tbody{height:calc(100% - 9mm);display:flex;flex-direction:column;justify-content:center;position:relative;z-index:2}
.tkick{font-size:7pt;font-weight:700;letter-spacing:.14em;text-transform:uppercase;margin-bottom:1.6mm}
.ttitle{font-size:16pt;font-weight:600;line-height:1.08}
.tsub{font-size:8.4pt;margin-top:2mm;opacity:.9}
.tlogo{position:absolute;right:0;bottom:0;width:15mm;height:auto}
/* qr card */
.qmain{display:flex;align-items:center;gap:3.5mm;height:calc(100% - 9mm);position:relative;z-index:2}
.qbox{width:24mm;height:24mm;flex:none;background:#fff;border-radius:2mm;padding:1.6mm}
.qbox svg{width:100%;height:100%;display:block}
.qtxt{font-size:7.6pt;line-height:1.45}
.back{padding:0;border-radius:3mm}.tile{width:100%;height:100%;background-repeat:no-repeat}
.reveal{max-width:820px;margin:16px auto;padding:16px}
.revgrid{display:grid;grid-template-columns:repeat(3,1fr);grid-auto-rows:1fr;gap:0;border:1px solid #E6DFD3;border-radius:8px;overflow:hidden}
.revgrid .card{width:auto;height:auto;aspect-ratio:889/635;padding:0;border-radius:0}
.revcap{text-align:center;color:#555;font-size:12px;margin-top:10px}
@media print{ body{background:#fff} .sheet{margin:0;box-shadow:none} .noprint{display:none!important} }
"""

reveal_html='<div class="reveal noprint"><div class="revgrid">%s</div><div class="revcap">Versos assemblés (après retournement) : le logo Éklore.</div></div>'%("".join(reveal))
HTML='<title>Jeu de cartes — Soutenance MFE</title><style>%s</style>%s%s%s'%(CSS,reveal_html,sheets(fronts),sheets(backs))
open(os.path.join(SCR,"cards.html"),"w",encoding="utf-8").write(HTML)
print("cards.html OK — style infographie chiffres clés")
