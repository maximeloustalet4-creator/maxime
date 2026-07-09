# -*- coding: utf-8 -*-
"""Jeu de cartes de soutenance — fronts (parcours) + versos (mosaïque logo Éklore)."""
import json, os
SCR = os.path.dirname(os.path.abspath(__file__))
fonts = json.load(open(os.path.join(SCR,"fonts.json")))
qr = open(os.path.join(SCR,"qr.svg")).read()

LAT="U+0000-00FF,U+0131,U+0152-0153,U+2000-206F,U+20AC,U+2122,U+2212"
EXT="U+0100-02BA,U+1E00-1E9F,U+2C60-2C7F,U+A720-A7FF"
def face(w,k,r): return "@font-face{font-family:'Fraunces';font-weight:%d;font-display:swap;src:url(data:font/woff2;base64,%s) format('woff2');unicode-range:%s;}"%(w,fonts[k]['b64'],r)
FONTS="\n".join([face(600,'f600_latin',LAT),face(600,'f600_ext',EXT),face(400,'f380_latin',LAT),face(400,'f380_ext',EXT)])

ICONS={
 "spark":'<path d="M12 3l2.2 5.8L20 11l-5.8 2.2L12 19l-2.2-5.8L4 11l5.8-2.2z"/>',
 "bolt":'<path d="M13 2 4 14h6l-1 8 10-12h-7l1-8z"/>',
 "target":'<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1.3" fill="currentColor" stroke="none"/>',
 "book":'<path d="M5 4a2 2 0 0 1 2-2h11v18H7a2 2 0 0 0-2 2z"/><path d="M5 20a2 2 0 0 1 2-2h11"/>',
 "chip":'<rect x="6" y="6" width="12" height="12" rx="2"/><path d="M10 10h4v4h-4z"/><path d="M9 2v3M15 2v3M9 19v3M15 19v3M2 9h3M2 15h3M19 9h3M19 15h3"/>',
 "beaker":'<path d="M9 3h6M10 3v6l-5 8a2 2 0 0 0 2 3h10a2 2 0 0 0 2-3l-5-8V3"/><path d="M7.5 14h9"/>',
 "eye":'<path d="M2 12s4-7 10-7 10 7 10 7-4 7-10 7-10-7-10-7z"/><circle cx="12" cy="12" r="3"/>',
 "shield":'<path d="M12 3 5 6v6c0 4 3 7 7 8 4-1 7-4 7-8V6z"/><path d="M9.5 12l2 2 3.5-4"/>',
 "users":'<circle cx="9" cy="8" r="3.2"/><path d="M3 20a6 6 0 0 1 12 0"/><path d="M16 5.2a3.2 3.2 0 0 1 0 6M17 14a6 6 0 0 1 4 6"/>',
 "clipboard":'<rect x="6" y="4" width="12" height="17" rx="2"/><path d="M9 4V3h6v1"/><path d="M9 12l2 2 4-4"/>',
 "flag":'<path d="M5 21V4"/><path d="M5 4h12l-2.2 3.5L17 11H5"/>',
}
def ic(n,c,s,sw=1.7): return '<svg viewBox="0 0 24 24" fill="none" stroke="%s" stroke-width="%s" stroke-linecap="round" stroke-linejoin="round" style="width:%smm;height:%smm">%s</svg>'%(c,sw,s,s,ICONS[n])

NAVY="#0B2A4A"; NAVYD="#07213C"; SLATE="#3D6A8E"; GREEN="#2F8B5D"; AMBER="#E6A339"; AMBERD="#AF7112"
INK="#18243C"; GREY="#54607A"; PAPER="#FCFBF8"; CREAM="#F7F2E8"; LINE="#E6DFD3"
ORANGE="#F5A623"

COLS, ROWS = 4, 3

# ---- Logo Éklore recréé (fleur qui éclôt : tête + livre/pétales) sur toile 420x444
LOGO = ('<svg viewBox="0 0 420 444" xmlns="http://www.w3.org/2000/svg">'
 '<circle cx="210" cy="120" r="42" fill="%s"/>'
 # pétale gauche
 '<path fill="%s" d="M205 330 '
 'C150 326 96 300 72 244 '
 'C55 205 55 168 66 150 '
 'C74 137 88 138 104 150 '
 'C150 184 190 240 205 300 Z"/>'
 # pétale droite (miroir)
 '<path fill="%s" d="M215 330 '
 'C270 326 324 300 348 244 '
 'C365 205 365 168 354 150 '
 'C346 137 332 138 316 150 '
 'C270 184 230 240 215 300 Z"/>'
 '</svg>') % (ORANGE, ORANGE, ORANGE)
import base64
LOGO_B64 = base64.b64encode(LOGO.encode()).decode()
LOGO_URI = "data:image/svg+xml;base64,"+LOGO_B64

# ---- Contenu des cartes : (num, act, icon, band_bg, band_fg, numtint, title, ludique, note)
C=[
 (1,"Ouverture","spark",NAVY,"#fff","rgba(255,255,255,.20)",
   "L'intégration de l'intelligence artificielle dans les PME",
   "Entre opportunités perçues et freins organisationnels — le cas d'Arla Groupe.  Peut-on faire entrer une technologie de pointe dans une entreprise à taille humaine, sans casser ce qui fait sa force ?", None),
 (2,"Contexte","bolt",AMBER,NAVY,"rgba(11,42,74,.22)",
   "Le contexte",
   "L'IA débarque partout — jusqu'à 15 000 milliards de dollars d'ici 2030. Mais une PME avance avec un petit budget, un patron au four et au moulin, et des habitudes bien ancrées.", None),
 (3,"Problématique","target",AMBER,NAVY,"rgba(11,42,74,.22)",
   "La problématique",
   "La vraie question : comment adopter l'IA sans trahir sa culture, ses moyens et sa façon de travailler ?  Trois pistes : la perception, les freins, les spécificités de la PME.", None),
 (4,"Cadre · la PME","book",SLATE,"#fff","rgba(255,255,255,.26)",
   "La PME vue par la théorie",
   "Une PME n'est pas une mini grande-entreprise : le dirigeant est partout, tout le monde se connaît, et les traditions du métier comptent.", "Torrès · Schein · Nassou & Bennani · Blanchard & Albert-Cromarias"),
 (5,"Cadre · l'IA","chip",SLATE,"#fff","rgba(255,255,255,.26)",
   "L'IA vue par la théorie",
   "Deux visages : du temps gagné et de meilleures décisions d'un côté ; données, compétences et risque de trop s'y fier de l'autre.", "Radoui & Cherradi · Bennour & Oukassi · Kokina · Duarte · Soro Torna"),
 (6,"Méthode","beaker",GREEN,"#fff","rgba(255,255,255,.26)",
   "La méthodologie",
   "Pour comprendre le « pourquoi », j'ai fait parler le terrain : 8 entretiens, du dirigeant à l'ouvrier, de 18 à 60 ans.", "Étude qualitative · 3 profils × 3 âges"),
 (7,"Résultat · QR1","eye",NAVY,"#fff","rgba(255,255,255,.20)",
   "Résultat 1 — la perception",
   "Bonne surprise : l'IA est plutôt bien vue, surtout pour le temps gagné. Mais chacun bricole dans son coin. « Le béton ne se verse pas de lui-même. »", None),
 (8,"Résultat · QR2","shield",NAVY,"#fff","rgba(255,255,255,.20)",
   "Résultat 2 — les freins",
   "Le frein n°1 change selon les gens : formation, budget, peur de mal faire… et un frein inattendu : perdre la main. « 40 ans qu'on travaille comme ça. »", None),
 (9,"Résultat · QR3","users",NAVY,"#fff","rgba(255,255,255,.20)",
   "Résultat 3 — le dirigeant",
   "Le vrai déclencheur, c'est le patron : 8 personnes sur 8 le disent. La proximité aide… ou contamine. « Si les dirigeants ne sont pas convaincus, ça traîne. »", None),
 (10,"Préconisations","clipboard",AMBERD,"#fff","rgba(255,255,255,.26)",
   "Les préconisations",
   "Trois leviers concrets pour Arla : un cadre commun + un référent IA, une formation par petits gains et par les collègues, une décision co-construite.", None),
 (11,"Conclusion","flag",NAVYD,"#fff","rgba(255,255,255,.20)",
   "La conclusion",
   "La réponse : l'IA en PME, c'est autant d'humain que d'organisation. Les particularités de la PME ne sont pas un mur — c'est le terrain de jeu.", "Ouverture : une étude quantitative pour hiérarchiser"),
 (12,"Signature","spark",NAVY,"#fff","rgba(255,255,255,.20)",
   "Pour aller plus loin", None, None),  # carte QR (front spécial)
]

# position (row,col) 1-based, remplissage par rangées
def rc(n): i=n-1; return (i//COLS, i%COLS)  # 0-based (r,c)
def nextdir(n):
    if n==12: return ("fin", "Carte finale")
    r,c=rc(n)
    if c==COLS-1: return ("row", "Rangée du dessous, à gauche")
    return ("right","À droite")

def minimap(n):
    r0,c0=rc(n)
    cells=""
    for r in range(ROWS):
        for c in range(COLS):
            idx=r*COLS+c+1
            if idx==n: st="background:%s"%AMBER
            elif idx<n: st="background:rgba(230,163,57,.28)"
            else: st="background:rgba(0,0,0,.06)"
            # next cell outline
            nd,_=nextdir(n)
            nn = n+1 if nd!="fin" else -1
            if idx==nn: st+=";box-shadow:inset 0 0 0 .5mm %s"%AMBER
            cells+='<span style="%s"></span>'%st
    return '<div class="mmap">%s</div>'%cells

def placecue(n):
    nd,label=nextdir(n)
    arrow = {"right":"→","row":"↵","fin":"●"}[nd]
    col = AMBERD if nd!="fin" else GREEN
    txt = ("Carte suivante : %s"%label) if nd!="fin" else "Fin du parcours"
    return ('<div class="cue"><span class="arw" style="color:%s">%s</span>'
            '<span class="cuetxt">%s</span>%s</div>')%(col,arrow,txt,minimap(n))

def front(n,act,icon,bg,fg,numtint,title,ludique,note):
    if n==12:
        body=('<div class="qzone">'
          +'<div style="font-size:9pt;color:%s;text-align:center;margin-bottom:3mm">Le diaporama interactif de la soutenance :</div>'%GREY
          +'<div class="qbox">%s</div>'%qr
          +'<div style="font-size:7.4pt;color:%s;text-align:center;margin-top:3mm;line-height:1.45">Réalisé avec l\'appui de <b style="color:%s">Claude</b>, une intelligence artificielle.<br><b style="color:%s">L\'IA assiste, l\'humain décide.</b></div>'%(GREY,INK,AMBERD)
          +'</div>')
    else:
        note_html = '<div class="note">%s</div>'%note if note else ''
        body='<div class="ttl serif">%s</div><div class="lud">%s</div>%s'%(title,ludique,note_html)
    numlabel = str(n) if n<12 else "★"
    return ('<div class="card">'
      +'<div class="band" style="background:%s;color:%s"><div class="num serif" style="color:%s">%s</div>'%(bg,fg,numtint,numlabel)
      +'<div class="bandr"><span class="act">%s</span>%s</div></div>'%(act.upper(),ic(icon,fg,6))
      +'<div class="bodyc">%s<div class="spacer"></div>%s</div></div>')%(body,placecue(n))

def back(n, mirror=True):
    r,c=rc(n)
    posx = (c/(COLS-1))*100 if COLS>1 else 0
    posy = (r/(ROWS-1))*100 if ROWS>1 else 0
    mir = "transform:scaleX(-1);" if mirror else ""
    tile=('<div class="tile" style="%sbackground-image:url(%s);background-size:%d%% %d%%;background-position:%.4f%% %.4f%%;background-repeat:no-repeat"></div>'
          %(mir, LOGO_URI, COLS*100, ROWS*100, posx, posy))
    return '<div class="card back">%s</div>'%tile

def sheet(cards_html):
    return '<div class="sheet">%s</div>'%cards_html

# fronts sheets (3 x 4)
fronts=[front(*c) for c in C]
backs=[back(c[0]) for c in C]
reveal_tiles=[back(c[0], mirror=False) for c in C]  # pour vérif : logo reconstitué

sheets=""
for i in range(0,12,4): sheets+=sheet("".join(fronts[i:i+4]))
for i in range(0,12,4): sheets+=sheet("".join(backs[i:i+4]))

reveal='<div class="reveal noprint"><div class="revgrid">%s</div><div class="revcap">Vérification — dos assemblés (après retournement) : le logo Éklore doit apparaître.</div></div>'%("".join(reveal_tiles))

CSS=FONTS+"""
*{box-sizing:border-box} body{margin:0;background:#DED9CF;font-family:system-ui,-apple-system,'Segoe UI',Roboto,sans-serif}
.serif{font-family:'Fraunces',Georgia,serif}
.sheet{width:210mm;height:297mm;background:#fff;margin:8mm auto;display:grid;grid-template-columns:1fr 1fr;grid-template-rows:1fr 1fr;
  gap:0;padding:0;page-break-after:always;box-shadow:0 3mm 8mm rgba(0,0,0,.15)}
.card{width:105mm;height:148.5mm;background:%s;overflow:hidden;display:flex;flex-direction:column;position:relative;
  outline:.2mm dashed #C9CFD8;outline-offset:-.1mm}
.band{height:26mm;padding:5mm 6mm;display:flex;align-items:center;justify-content:space-between;flex:none}
.num{font-size:34pt;font-weight:600;line-height:1}
.bandr{display:flex;flex-direction:column;align-items:flex-end;gap:2mm}
.act{font-size:8pt;font-weight:700;letter-spacing:.13em}
.bodyc{flex:1;padding:6mm 6mm 5mm;display:flex;flex-direction:column}
.ttl{font-size:19pt;font-weight:600;color:%s;line-height:1.08;margin-bottom:3.5mm}
.lud{font-size:10.5pt;line-height:1.5;color:%s}
.note{font-size:7.6pt;color:%s;margin-top:3mm;font-style:italic;line-height:1.35}
.spacer{flex:1}
.cue{border-top:.3mm solid %s;padding-top:3mm;display:flex;align-items:center;gap:2.4mm}
.arw{font-size:15pt;font-weight:700;line-height:1}
.cuetxt{font-size:8.4pt;font-weight:700;color:%s;flex:1;line-height:1.15}
.mmap{display:grid;grid-template-columns:repeat(4,3mm);grid-template-rows:repeat(3,3mm);gap:.8mm}
.mmap span{width:3mm;height:3mm;border-radius:.5mm;display:block}
.qzone{flex:1;display:flex;flex-direction:column;align-items:center;justify-content:center}
.qbox{width:42mm;height:42mm;background:#fff;border:.3mm solid %s;border-radius:2mm;padding:2.5mm}
.qbox svg{width:100%%;height:100%%;display:block}
.back{background:%s;padding:0}
.tile{width:100%%;height:100%%}
/* reveal (écran seulement) */
.reveal{max-width:1000px;margin:20px auto;padding:20px}
.revgrid{display:grid;grid-template-columns:repeat(4,1fr);grid-template-rows:repeat(3,1fr);gap:0;background:%s;border:1px solid %s;border-radius:8px;overflow:hidden;aspect-ratio:%s}
.revgrid .card{width:auto;height:auto;aspect-ratio:105/148.5;outline:none}
.revcap{text-align:center;color:#555;font-size:13px;margin-top:12px}
@media print{ body{background:#fff} .sheet{margin:0;box-shadow:none} .noprint{display:none!important} }
"""%(PAPER,NAVY,INK,SLATE,LINE,INK,LINE,PAPER,PAPER,LINE, "%d/%d"%(COLS*105, ROWS*148))

HTML='<title>Jeu de cartes — Soutenance MFE</title><style>%s</style>%s%s'%(CSS,reveal,sheets)
open(os.path.join(SCR,"cards.html"),"w",encoding="utf-8").write(HTML)
print("cards.html OK — 12 fronts + 12 versos ; grille %dx%d"%(COLS,ROWS))
