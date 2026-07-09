# -*- coding: utf-8 -*-
"""Jeu de cartes 88.9x63.5mm — tuiles couleur "chiffres clés" ENRICHIES :
chiffre + détails + auteurs/verbatim + repère de placement (mini-plan 3x4).
Assemblées 3x4 (ligne par ligne). Versos = mosaïque du logo Éklore."""
import os, json
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
 "eye":'<path d="M2 12s4-7 10-7 10 7 10 7-4 7-10 7-10-7-10-7z"/><circle cx="12" cy="12" r="3"/>',
 "shield":'<path d="M12 3 5 6v6c0 4 3 7 7 8 4-1 7-4 7-8V6z"/><path d="M9.2 12l2 2 3.6-4"/>',
 "users":'<circle cx="9" cy="8" r="3.4"/><path d="M2.5 20a6.5 6.5 0 0 1 13 0"/><path d="M16 5a3.4 3.4 0 0 1 0 6.4M17.5 14a6 6 0 0 1 4 6"/>',
 "clipboard":'<rect x="6" y="4" width="12" height="17" rx="2"/><path d="M9 4V3h6v1"/><path d="M9.5 12l1.8 1.8L15 10"/>',
 "flag":'<path d="M5 21V4"/><path d="M5 4h13l-2.4 3.8L18 12H5"/>',
 "qr":'<rect x="3" y="3" width="7" height="7" rx="1"/><rect x="14" y="3" width="7" height="7" rx="1"/><rect x="3" y="14" width="7" height="7" rx="1"/><path d="M14 14h3v3M20.5 14v.01M14 20.5v.01M20.5 20.5v.01M17.5 17.5h.01"/>',
}
def ic(n,c,s,sw=2.0): return '<svg viewBox="0 0 24 24" fill="none" stroke="%s" stroke-width="%s" stroke-linecap="round" stroke-linejoin="round" style="width:%smm;height:%smm">%s</svg>'%(c,sw,s,s,ICONS[n])

NAVY="#0B2A4A"; BLUE="#1466A6"; SLATE="#3D6A8E"; TEAL="#178F8F"; AMBER="#E6A339"
COLS,ROWS=3,4
def pos(n): return ((n-1)//COLS,(n-1)%COLS)
def contrast(t): return NAVY if t==AMBER else "#fff"

# (num, section, icon, tile, focal, lead, [infos], quote, authors)
C=[
 (1,"Mémoire · Soutenance",None,NAVY,None,None,[],None,None),
 (2,"Contexte","bolt",BLUE,"≈14%","du PIB mondial capté par l'IA d'ici 2030 (~15 000 Md$).",
   ["La PME : ressources limitées, dirigeant central, poids des traditions."],None,"Rouas & Al Meriouh, 2025 · Farsad, 2021"),
 (3,"Problématique","target",TEAL,"?","Intégrer l'IA sans trahir sa culture, ses moyens et sa façon de travailler.",
   ["3 sous-questions : perception · freins · spécificités PME."],None,None),
 (4,"Cadre · la PME","book",AMBER,"<250","salariés, CA < 50 M€ : le seuil d'une PME (UE).",
   ["Dirigeant impliqué, proximité organisationnelle.","Culture & traditions de métier."],None,"Oriot & Misiaszek · Torrès · Schein · Blanchard & A.-C."),
 (5,"Cadre · l'IA","chip",SLATE,"2","visages de l'IA.",
   ["Atout : performance & analyse prédictive.","Risque : données, compétences, dépendance cognitive."],None,"Radoui & Cherradi · Bennour & Oukassi · Kokina · Soro Torna"),
 (6,"Méthode","users",BLUE,"8","entretiens semi-directifs (qualitatif exploratoire).",
   ["Échantillon raisonné : 3 profils × 3 âges (18–60 ans).","~5 h de transcription + analyse par verbatims."],None,"Jando, 2024"),
 (7,"Résultat 1 · Perception","eye",TEAL,"6/8","utilisent déjà l'IA ; perception positive (gain de temps).",
   ["La lecture se fait par le métier, pas que par l'âge.","Usage encore individuel et non encadré."],"Le béton ne se verse pas de lui-même.","valide Bennour & Oukassi · Kokina"),
 (8,"Résultat 2 · Freins","shield",NAVY,"≠","Le frein n°1 change selon les profils.",
   ["Partagés : formation + budget.","Frein inédit : la peur de perdre la main."],"40 ans qu'on travaille comme ça.","Kokina · Duarte · Schein"),
 (9,"Résultat 3 · Dirigeant","users",AMBER,"8/8","citent le dirigeant comme le facteur décisif.",
   ["Un seul moteur suffit à lancer la dynamique.","Traditions = adoption sélective, pas un rejet."],"S'ils ne sont pas convaincus, ça traîne.","Torrès · Nassou & Bennani"),
 (10,"Préconisations","clipboard",SLATE,"3","leviers concrets pour Arla Groupe.",
   ["1 · Politique commune + référent IA.","2 · Formation par les pairs (quick wins).","3 · Démarche participative."],None,None),
 (11,"Conclusion","flag",TEAL,"↔","Autant d'humain que d'organisationnel.",
   ["Les spécificités PME = un cadre, pas un mur.","Ouverture : une étude quantitative pour hiérarchiser."],None,None),
 (12,"Pour aller plus loin","qr",NAVY,None,None,[],None,None),
]

def nextcue(n):
    if n==12: return ("Fin du parcours","●",-1)
    nn=n+1
    if (n-1)%COLS==COLS-1: return ("Rangée du dessous, à gauche","↵",nn)
    return ("À droite","→",nn)

def minimap(n,fg):
    label,arrow,nn=nextcue(n)
    cells=""
    for r in range(ROWS):
        for c in range(COLS):
            idx=r*COLS+c+1
            if idx==n: st="background:%s"%fg
            elif idx<n: st="background:%s"%("rgba(11,42,74,.45)" if fg==NAVY else "rgba(255,255,255,.5)")
            else: st="background:%s"%("rgba(11,42,74,.18)" if fg==NAVY else "rgba(255,255,255,.22)")
            if idx==nn: st+=";box-shadow:inset 0 0 0 .4mm %s"%fg
            cells+='<span style="%s"></span>'%st
    return '<div class="cue"><span class="cuel" style="color:%s"><b>%s</b> Carte suivante&nbsp;: %s</span><div class="mmap">%s</div></div>'%(fg,arrow,label,cells)

def fsz(f):
    L=len(f); return 30 if L<=1 else (26 if L<=2 else 20)

def tile(n,section,icon,col,focal,lead,infos,quote,authors):
    fg=contrast(col)
    dim="rgba(11,42,74,.13)" if col==AMBER else "rgba(255,255,255,.12)"
    deco='<span class="blob" style="background:%s"></span>'%dim
    top='<div class="top"><div class="badge" style="color:%s"><span class="serif">%s</span></div><div class="sec">%s</div></div>'%(col,n,section.upper())
    if n==1:
        body=('<div class="tbody"><div class="tkick" style="color:%s">Les cartes clés de ma démonstration</div>'%AMBER
          +'<div class="ttitle serif">L\'intégration de l\'IA dans les PME</div>'
          +'<div class="tsub">Entre opportunités et freins — le cas d\'Arla Groupe.</div>'
          +'<div class="tsub" style="opacity:.8;margin-top:1mm">Master 2 · Dir. V. Combes · Eklore-ed · 2025–2026</div>'
          +'<img class="tlogo" src="%s"/></div>'%LOGO)
        return '<div class="card" style="background:%s;color:%s">%s%s%s</div>'%(col,fg,deco,top,body)
    if n==12:
        body=('<div class="qmain"><div class="qbox">%s</div>'%qr
          +'<div class="qtxt"><b>Diaporama animé</b> de la soutenance — scanne le code.<br>Note MFE : 40 %% écrit · 60 %% oral.<br><span style="color:%s">Réalisé avec Claude — l\'IA assiste, l\'humain décide.</span></div></div>'%AMBER)
        return '<div class="card" style="background:%s;color:%s">%s%s%s</div>'%(col,fg,deco,top,body)
    wm='<div class="wm">%s</div>'%ic(icon,fg,26,2.0)
    infhtml="".join('<div class="info"><span class="dot" style="background:%s"></span>%s</div>'%(AMBER if col!=AMBER else NAVY, t) for t in infos)
    extra=''
    if quote: extra+='<div class="q">« %s »</div>'%quote
    if authors: extra+='<div class="au">%s</div>'%authors
    body=('<div class="body">%s'%wm
      +'<div class="statrow"><div class="focal serif" style="font-size:%spt">%s</div><div class="lead">%s</div></div>'%(fsz(focal),focal,lead)
      +'<div class="infos">%s</div>%s</div>'%(infhtml,extra)
      +minimap(n,fg))
    return '<div class="card" style="background:%s;color:%s">%s%s%s</div>'%(col,fg,deco,top,body)

def back(n,mirror=True):
    r,c=pos(n); posx=(c/(COLS-1))*100; posy=(r/(ROWS-1))*100
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
.card{width:88.9mm;height:63.5mm;border-radius:3mm;overflow:hidden;position:relative;padding:3.6mm 4.4mm 3mm;display:flex;flex-direction:column}
.blob{position:absolute;width:30mm;height:30mm;border-radius:50%;right:-8mm;top:-10mm}
.top{display:flex;align-items:center;gap:2.2mm;flex:none;position:relative;z-index:2}
.badge{width:6.8mm;height:6.8mm;border-radius:50%;background:#fff;display:flex;align-items:center;justify-content:center;flex:none}
.badge .serif{font-size:11pt;font-weight:600;line-height:1}
.sec{font-size:6.2pt;font-weight:700;letter-spacing:.09em;text-transform:uppercase;opacity:.95}
.body{flex:1;display:flex;flex-direction:column;position:relative;z-index:1;padding-top:2mm}
.wm{position:absolute;right:-3mm;bottom:-2mm;opacity:.1;z-index:0}
.statrow{display:flex;align-items:center;gap:2.6mm;z-index:1}
.focal{font-weight:600;line-height:.95;letter-spacing:-.5px;flex:none}
.lead{font-size:8.2pt;font-weight:700;line-height:1.14}
.infos{margin-top:1.6mm;display:flex;flex-direction:column;gap:.7mm;z-index:1}
.info{font-size:7.1pt;line-height:1.2;padding-left:2.4mm;position:relative;opacity:.97}
.dot{position:absolute;left:0;top:.9mm;width:1.2mm;height:1.2mm;border-radius:50%;display:block}
.q{font-family:'Fraunces',serif;font-style:italic;font-size:7pt;margin-top:1.5mm;opacity:.92;z-index:1}
.au{font-size:6pt;margin-top:1mm;opacity:.75;z-index:1}
.cue{margin-top:auto;display:flex;align-items:center;gap:2mm;padding-top:1.6mm;border-top:.25mm solid rgba(255,255,255,.22);z-index:2}
.cuel{font-size:6.4pt;font-weight:600;flex:1;line-height:1.1}
.cuel b{font-size:8pt}
.mmap{display:grid;grid-template-columns:repeat(3,1.9mm);grid-auto-rows:1.9mm;gap:.5mm;flex:none}
.mmap span{width:1.9mm;height:1.9mm;border-radius:.3mm;display:block}
.tbody{flex:1;display:flex;flex-direction:column;justify-content:center;position:relative;z-index:2}
.tkick{font-size:7pt;font-weight:700;letter-spacing:.13em;text-transform:uppercase;margin-bottom:1.6mm}
.ttitle{font-size:17pt;font-weight:600;line-height:1.06}
.tsub{font-size:8.2pt;margin-top:1.8mm;opacity:.92}
.tlogo{position:absolute;right:0;bottom:0;width:14mm;height:auto}
.qmain{flex:1;display:flex;align-items:center;gap:3.5mm;position:relative;z-index:2}
.qbox{width:24mm;height:24mm;flex:none;background:#fff;border-radius:2mm;padding:1.6mm}
.qbox svg{width:100%;height:100%;display:block}
.qtxt{font-size:7.4pt;line-height:1.45}
.back{padding:0;border-radius:3mm}.tile{width:100%;height:100%;background-repeat:no-repeat}
.reveal{max-width:820px;margin:16px auto;padding:16px}
.revgrid{display:grid;grid-template-columns:repeat(3,1fr);grid-auto-rows:1fr;gap:0;border:1px solid #E6DFD3;border-radius:8px;overflow:hidden}
.revgrid .card{width:auto;height:auto;aspect-ratio:889/635;padding:0;border-radius:0}
.revcap{text-align:center;color:#555;font-size:12px;margin-top:10px}
@media print{ body{background:#fff} .sheet{margin:0;box-shadow:none} .noprint{display:none!important} }
"""

reveal_html='<div class="reveal noprint"><div class="revgrid">%s</div><div class="revcap">Versos assemblés : le logo Éklore.</div></div>'%("".join(reveal))
HTML='<title>Jeu de cartes — Soutenance MFE</title><style>%s</style>%s%s%s'%(CSS,reveal_html,sheets(fronts),sheets(backs))
open(os.path.join(SCR,"cards.html"),"w",encoding="utf-8").write(HTML)
print("cards.html OK — tuiles enrichies + repère de placement")
