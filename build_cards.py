# -*- coding: utf-8 -*-
"""Jeu de cartes de soutenance — format carte à jouer paysage 88.9x63.5mm.
Fronts illustrés (parcours) + versos = mosaïque du logo Éklore (grille 3x4)."""
import json, os
SCR=os.path.dirname(os.path.abspath(__file__))
fonts=json.load(open(os.path.join(SCR,"fonts.json")))
qr=open(os.path.join(SCR,"qr.svg")).read()
POSTER="data:image/png;base64,"+open(os.path.join(SCR,"poster.b64")).read()

LAT="U+0000-00FF,U+0131,U+0152-0153,U+2000-206F,U+20AC,U+2122,U+2212"
EXT="U+0100-02BA,U+1E00-1E9F,U+2C60-2C7F,U+A720-A7FF"
def face(w,k,r): return "@font-face{font-family:'Fraunces';font-weight:%d;font-display:swap;src:url(data:font/woff2;base64,%s) format('woff2');unicode-range:%s;}"%(w,fonts[k]['b64'],r)
FONTS="\n".join([face(600,'f600_latin',LAT),face(600,'f600_ext',EXT),face(400,'f380_latin',LAT),face(400,'f380_ext',EXT)])

ICONS={
 "spark":'<path d="M12 3l2.2 5.8L20 11l-5.8 2.2L12 19l-2.2-5.8L4 11l5.8-2.2z"/>',
 "bolt":'<path d="M13 2 4 14h6l-1 8 10-12h-7l1-8z"/>',
 "target":'<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1.4" fill="currentColor" stroke="none"/>',
 "book":'<path d="M12 6C9 3.5 5.5 3.5 3 4v13c2.5-.5 6-.5 9 2 3-2.5 6.5-2.5 9-2V4c-2.5-.5-6-.5-9 2z"/><path d="M12 6v13"/>',
 "chip":'<rect x="6" y="6" width="12" height="12" rx="2"/><path d="M10 10h4v4h-4z"/><path d="M9 2v3M15 2v3M9 19v3M15 19v3M2 9h3M2 15h3M19 9h3M19 15h3"/>',
 "beaker":'<path d="M9 3h6M10 3v6l-5 8a2 2 0 0 0 2 3h10a2 2 0 0 0 2-3l-5-8V3"/><path d="M7.5 14h9"/>',
 "eye":'<path d="M2 12s4-7 10-7 10 7 10 7-4 7-10 7-10-7-10-7z"/><circle cx="12" cy="12" r="3"/>',
 "shield":'<path d="M12 3 5 6v6c0 4 3 7 7 8 4-1 7-4 7-8V6z"/><path d="M9.5 12l2 2 3.5-4"/>',
 "users":'<circle cx="9" cy="8" r="3.2"/><path d="M3 20a6 6 0 0 1 12 0"/><path d="M16 5.2a3.2 3.2 0 0 1 0 6M17 14a6 6 0 0 1 4 6"/>',
 "clipboard":'<rect x="6" y="4" width="12" height="17" rx="2"/><path d="M9 4V3h6v1"/><path d="M9 12l2 2 4-4"/>',
 "flag":'<path d="M5 21V4"/><path d="M5 4h12l-2.2 3.5L17 11H5"/>',
 "qr":'<rect x="3" y="3" width="7" height="7" rx="1"/><rect x="14" y="3" width="7" height="7" rx="1"/><rect x="3" y="14" width="7" height="7" rx="1"/><path d="M14 14h3v3M20 14v.01M14 20v.01M20 20v.01M17 17h.01"/>',
}
def ic(n,c,s,sw=1.7): return '<svg viewBox="0 0 24 24" fill="none" stroke="%s" stroke-width="%s" stroke-linecap="round" stroke-linejoin="round" style="width:%smm;height:%smm">%s</svg>'%(c,sw,s,s,ICONS[n])

NAVY="#0B2A4A"; NAVYD="#07213C"; SLATE="#3D6A8E"; GREEN="#2F8B5D"; TEAL="#2E8B8B"; AMBER="#E6A339"; AMBERD="#B4770F"; PLUM="#7A4E8C"
INK="#18243C"; GREY="#55607A"; PAPER="#FCFBF8"; CREAM="#F7F2E8"; LINE="#E6DFD3"
COLS,ROWS=3,4

# (num, section, icon, bandcolor, ludique, quote, author)  title derived
C=[
 (1,"Ouverture","spark",NAVY,"L'intégration de l'IA dans les PME",
   "Entre opportunités perçues et freins organisationnels — le cas d'Arla Groupe.",None,None),
 (2,"Contexte","bolt",AMBER,"Le contexte",
   "L'IA est partout. La PME, elle, a un petit budget et de grosses habitudes.",None,None),
 (3,"Problématique","target",AMBERD,"La problématique",
   "Adopter l'IA sans trahir sa culture, ses moyens et sa façon de travailler ?",None,"Perception · freins · spécificités PME"),
 (4,"Cadre · la PME","book",SLATE,"La PME en théorie",
   "Pas une mini grande-entreprise : le patron est partout, les traditions comptent.",None,"Torrès · Schein · Nassou & Bennani"),
 (5,"Cadre · l'IA","chip",SLATE,"L'IA en théorie",
   "Du temps gagné et de meilleures décisions… mais gare à trop s'y fier.",None,"Radoui & Cherradi · Kokina · Soro Torna"),
 (6,"Méthode","beaker",TEAL,"La méthode",
   "J'ai fait parler le terrain : 8 entretiens, du dirigeant à l'ouvrier, de 18 à 60 ans.",None,"Qualitatif · 3 profils × 3 âges"),
 (7,"Résultat 1","eye",NAVY,"La perception",
   "Plutôt bien vue ! Mais chacun bricole dans son coin.","Le béton ne se verse pas de lui-même.",None),
 (8,"Résultat 2","shield",NAVY,"Les freins",
   "Le vrai frein change selon les gens — et la peur de perdre la main.","40 ans qu'on travaille comme ça.",None),
 (9,"Résultat 3","users",NAVY,"Le dirigeant",
   "Le déclencheur, c'est le patron : 8 personnes sur 8 le disent.","Si les dirigeants ne sont pas convaincus, ça traîne.",None),
 (10,"Préconisations","clipboard",AMBERD,"Les préconisations",
   "3 leviers : un cadre commun, la formation par les collègues, une décision partagée.",None,None),
 (11,"Conclusion","flag",NAVYD,"La conclusion",
   "L'IA en PME : autant d'humain que d'organisation. Les spécificités ne sont pas un mur.",None,None),
 (12,"QR code","qr",NAVY,"Pour aller plus loin",None,None,None),
]

def rc(n): i=n-1; return (i//COLS, i%COLS)
def nextdir(n):
    if n==12: return ("fin","Fin")
    r,c=rc(n)
    if c==COLS-1: return ("row","Rangée suivante, à gauche")
    return ("right","À droite")

def minimap(n):
    cells=""
    nd,_=nextdir(n); nn=n+1 if nd!="fin" else -1
    for r in range(ROWS):
        for c in range(COLS):
            idx=r*COLS+c+1
            if idx==n: st="background:%s"%AMBER
            elif idx<n: st="background:rgba(230,163,57,.30)"
            else: st="background:rgba(11,42,74,.10)"
            if idx==nn: st+=";box-shadow:inset 0 0 0 .45mm %s"%AMBER
            cells+='<span style="%s"></span>'%st
    return '<div class="mmap">%s</div>'%cells

def cue(n):
    nd,label=nextdir(n)
    arrow={"right":"→","row":"↵","fin":"●"}[nd]
    col=AMBERD if nd!="fin" else GREEN
    txt=("Suivante : %s"%label) if nd!="fin" else "Fin du parcours"
    return '<div class="cue"><span class="arw" style="color:%s">%s</span><span class="cuetxt">%s</span>%s</div>'%(col,arrow,txt,minimap(n))

def confetti(c1,c2):
    return ('<span class="cf" style="top:3mm;right:4mm;width:2mm;height:2mm;background:%s"></span>'
            '<span class="cf" style="top:5.5mm;right:2.4mm;width:1.3mm;height:1.3mm;background:%s"></span>'
            '<span class="cf" style="top:2.2mm;right:7mm;width:1.1mm;height:1.1mm;background:%s"></span>')%(c1,c2,c1)

def front(n,section,icon,bg,title,ludique,quote,author):
    fg="#fff"
    numtint="rgba(255,255,255,.9)"
    # left panel
    left=('<div class="lp" style="background:%s">'%bg
      +'<span class="blob" style="background:rgba(255,255,255,.10);width:26mm;height:26mm;top:-6mm;left:-6mm"></span>'
      +'<span class="blob" style="background:rgba(255,255,255,.08);width:16mm;height:16mm;bottom:-4mm;right:-4mm"></span>'
      +'<div class="iconc">%s</div>'%ic(icon,bg,8.5,1.8)
      +'<div class="num serif" style="color:%s">%s</div>'%(numtint, (str(n) if n<12 else "★"))
      +'<div class="seclab">%s</div>'%section.upper()
      +'</div>')
    # right content
    if n==12:
        right=('<div class="rc qrc">'
          +'<div class="ttl serif" style="text-align:center;font-size:11pt">Pour aller plus loin</div>'
          +'<div class="qwrap"><div class="qbox">%s</div>'%qr
          +'<div class="qtxt">Scanne pour voir le<br><b>diaporama animé</b>.<br><span style="color:%s">Réalisé avec Claude — l\'IA assiste, l\'humain décide.</span></div></div>'%AMBERD
          +cue(n)+'</div>')
    else:
        q='<div class="quote">« %s »</div>'%quote if quote else ''
        a='<div class="auth">%s</div>'%author if author else ''
        right=('<div class="rc">'+confetti(AMBER,SLATE)
          +'<div class="ttl serif">%s</div>'%title
          +'<div class="lud">%s</div>'%ludique
          +q+a+'<div class="grow"></div>'+cue(n)+'</div>')
    return '<div class="card">%s%s</div>'%(left,right)

def back(n,mirror=True):
    r,c=rc(n)
    posx=(c/(COLS-1))*100 if COLS>1 else 0
    posy=(r/(ROWS-1))*100 if ROWS>1 else 0
    mir="transform:scaleX(-1);" if mirror else ""
    return ('<div class="card back"><div class="tile" style="%sbackground-image:url(%s);background-size:%d%% %d%%;background-position:%.4f%% %.4f%%"></div></div>'
            %(mir,POSTER,COLS*100,ROWS*100,posx,posy))

fronts=[front(*c) for c in C]
backs=[back(c[0]) for c in C]
reveal=[back(c[0],mirror=False) for c in C]

def sheets(cards, per=8, cols=2):
    out=""
    for i in range(0,len(cards),per):
        out+='<div class="sheet">%s</div>'%("".join(cards[i:i+per]))
    return out

CSS=FONTS+"""
*{box-sizing:border-box} body{margin:0;background:#DED9CF;font-family:system-ui,-apple-system,'Segoe UI',Roboto,sans-serif}
.serif{font-family:'Fraunces',Georgia,serif}
.sheet{width:210mm;height:297mm;background:#fff;margin:8mm auto;display:grid;grid-template-columns:88.9mm 88.9mm;grid-auto-rows:63.5mm;
  justify-content:center;align-content:start;gap:6mm 8mm;padding:14mm 0;page-break-after:always;box-shadow:0 3mm 8mm rgba(0,0,0,.15)}
.card{width:88.9mm;height:63.5mm;background:%s;border-radius:3mm;overflow:hidden;display:flex;position:relative;
  outline:.2mm dashed #C9CFD8;box-shadow:0 .6mm 1.6mm rgba(0,0,0,.06)}
.lp{width:27mm;flex:none;position:relative;display:flex;flex-direction:column;align-items:center;justify-content:center;overflow:hidden;color:#fff}
.blob{position:absolute;border-radius:50%%;display:block}
.iconc{width:15mm;height:15mm;border-radius:50%%;background:#fff;display:flex;align-items:center;justify-content:center;z-index:1;box-shadow:0 1mm 2mm rgba(0,0,0,.12)}
.num{font-size:22pt;font-weight:600;line-height:1;margin-top:2mm;z-index:1}
.seclab{font-size:5.4pt;font-weight:700;letter-spacing:.12em;margin-top:1mm;opacity:.9;z-index:1;text-align:center;padding:0 1mm}
.rc{flex:1;padding:4.5mm 5mm 4mm;display:flex;flex-direction:column;position:relative}
.cf{position:absolute;border-radius:50%%;display:block}
.ttl{font-size:13pt;font-weight:600;color:%s;line-height:1.05;margin-bottom:1.6mm}
.lud{font-size:8.2pt;line-height:1.34;color:%s}
.quote{font-family:'Fraunces',serif;font-style:italic;font-size:8.4pt;color:%s;margin-top:1.8mm;border-left:.8mm solid %s;padding-left:2mm;line-height:1.2}
.auth{font-size:6.6pt;color:%s;margin-top:1.8mm;font-style:italic}
.grow{flex:1}
.cue{display:flex;align-items:center;gap:1.6mm;border-top:.3mm solid %s;padding-top:1.8mm;margin-top:1.8mm}
.arw{font-size:11pt;font-weight:700;line-height:1}
.cuetxt{font-size:6.6pt;font-weight:700;color:%s;flex:1;line-height:1.1}
.mmap{display:grid;grid-template-columns:repeat(3,2.1mm);grid-auto-rows:2.1mm;gap:.55mm}
.mmap span{width:2.1mm;height:2.1mm;border-radius:.35mm;display:block}
.qrc{align-items:center;padding:3.5mm 4mm}
.qwrap{flex:1;display:flex;align-items:center;gap:3mm;width:100%%}
.qbox{width:24mm;height:24mm;flex:none;background:#fff;border:.3mm solid %s;border-radius:1.5mm;padding:1.5mm}
.qbox svg{width:100%%;height:100%%;display:block}
.qtxt{font-size:6.8pt;color:%s;line-height:1.4}
.back{padding:0}
.tile{width:100%%;height:100%%;background-repeat:no-repeat}
.reveal{max-width:820px;margin:16px auto;padding:16px}
.revgrid{display:grid;grid-template-columns:repeat(3,1fr);grid-auto-rows:1fr;gap:0;border:1px solid %s;border-radius:8px;overflow:hidden}
.revgrid .card{width:auto;height:auto;aspect-ratio:889/635;outline:none;border-radius:0;box-shadow:none}
.revcap{text-align:center;color:#555;font-size:12px;margin-top:10px}
@media print{ body{background:#fff} .sheet{margin:0;box-shadow:none} .noprint{display:none!important} }
"""%(PAPER,NAVY,GREY,AMBERD,AMBER,SLATE,LINE,INK,LINE,GREY,LINE)

reveal_html='<div class="reveal noprint"><div class="revgrid">%s</div><div class="revcap">Vérification — versos assemblés (après retournement) : le logo Éklore.</div></div>'%("".join(reveal))
HTML='<title>Jeu de cartes — Soutenance MFE</title><style>%s</style>%s%s%s'%(CSS,reveal_html,sheets(fronts),sheets(backs))
open(os.path.join(SCR,"cards.html"),"w",encoding="utf-8").write(HTML)
print("cards.html OK — format 88.9x63.5 paysage, grille %dx%d, 12 cartes"%(COLS,ROWS))
