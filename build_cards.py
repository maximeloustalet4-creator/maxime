# -*- coding: utf-8 -*-
"""Jeu de cartes 88.9x63.5mm paysage. Les 12 fronts, posés en 3x4 (parcours serpent),
forment UNE infographie continue (fil conducteur + noeuds + flèches de liaison).
Versos = mosaïque du vrai logo Éklore."""
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
 "chev":'<path d="M8 4l8 8-8 8"/>',
}
def ic(n,c,s,sw=1.7): return '<svg viewBox="0 0 24 24" fill="none" stroke="%s" stroke-width="%s" stroke-linecap="round" stroke-linejoin="round" style="width:%smm;height:%smm">%s</svg>'%(c,sw,s,s,ICONS[n])
def chev(rot,c,s,sw=3): return '<svg viewBox="0 0 24 24" fill="none" stroke="%s" stroke-width="%s" stroke-linecap="round" stroke-linejoin="round" style="width:%smm;height:%smm;transform:rotate(%sdeg)">%s</svg>'%(c,sw,s,s,rot,ICONS["chev"])

NAVY="#0B2A4A"; NAVYD="#07213C"; SLATE="#3D6A8E"; GREEN="#2F8B5D"; TEAL="#2E8B8B"; AMBER="#E6A339"; AMBERD="#B4770F"
INK="#18243C"; GREY="#55607A"; PAPER="#FCFBF8"; LINE="#E6DFD3"
COLS,ROWS=3,4
POS=[(0,0),(0,1),(0,2),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2),(3,2),(3,1),(3,0)]  # parcours serpent

def outdir(n):
    if n>=12: return None
    (ra,ca),(rb,cb)=POS[n-1],POS[n]
    if rb==ra: return "R" if cb>ca else "L"
    return "D"
def in_from_top(n):
    if n<=1: return False
    (ra,ca),(rb,cb)=POS[n-2],POS[n-1]
    return rb==ra+1

# (num, section, icon, color, title, ludique, quote, author)
C=[
 (1,"Ouverture","spark",NAVY,"L'intégration de l'IA dans les PME","Entre opportunités perçues et freins — le cas d'Arla Groupe.",None,None),
 (2,"Contexte","bolt",AMBER,"Le contexte","L'IA est partout. La PME, elle, a un petit budget et de grosses habitudes.",None,None),
 (3,"Problématique","target",AMBERD,"La problématique","Adopter l'IA sans trahir sa culture, ses moyens et sa façon de travailler ?",None,"Perception · freins · spécificités"),
 (4,"Cadre · PME","book",SLATE,"La PME en théorie","Pas une mini grande-entreprise : le patron est partout.",None,"Torrès · Schein · Nassou & Bennani"),
 (5,"Cadre · IA","chip",SLATE,"L'IA en théorie","Du temps gagné… mais gare à trop s'y fier.",None,"Radoui & Cherradi · Kokina · Soro Torna"),
 (6,"Méthode","beaker",TEAL,"La méthode","8 entretiens, du dirigeant à l'ouvrier, de 18 à 60 ans.",None,"Qualitatif · 3 profils × 3 âges"),
 (7,"Résultat 1","eye",NAVY,"La perception","Plutôt bien vue ! Mais chacun bricole dans son coin.","Le béton ne se verse pas de lui-même.",None),
 (8,"Résultat 2","shield",NAVY,"Les freins","Le frein change selon les gens — et la peur de perdre la main.","40 ans qu'on travaille comme ça.",None),
 (9,"Résultat 3","users",NAVY,"Le dirigeant","Le déclencheur, c'est le patron : 8 sur 8 le disent.","Si les dirigeants ne sont pas convaincus, ça traîne.",None),
 (10,"Préconisations","clipboard",AMBERD,"Les préconisations","Cadre commun, formation par les collègues, décision partagée.",None,None),
 (11,"Conclusion","flag",NAVYD,"La conclusion","Autant d'humain que d'organisation. Les spécificités ne sont pas un mur.",None,None),
 (12,"QR code","qr",NAVY,"Pour aller plus loin",None,None,None),
]

def rail(n):
    """Bande de liaison en bas : ligne continue + noeud central + flèche vers la suivante."""
    od=outdir(n); topin=in_from_top(n)
    parts='<div class="line"></div>'
    # noeud central
    endc=GREEN if n==12 else AMBER
    parts+='<div class="node" style="background:%s"></div>'%endc
    # flèche de sortie
    if od=="R":
        parts+='<div class="ochev" style="right:1.6mm">%s</div>'%chev(0,AMBER,3.4)
    elif od=="L":
        parts+='<div class="ochev" style="left:1.6mm">%s</div>'%chev(180,AMBER,3.4)
    elif od=="D":
        parts+='<div class="drop"></div><div class="dchev">%s</div>'%chev(90,AMBER,3.4)
    if n==12:
        parts+='<div class="ochev" style="right:1.6mm">%s</div>'%chev(0,GREEN,3.4)
    # entrée par le haut (flèche descendante sur le bandeau)
    topmark='<div class="tdrop"></div><div class="tchev">%s</div>'%chev(90,"#fff",3) if topin else ''
    return '<div class="rail">%s</div>%s'%(parts,topmark)

def front(n,section,icon,col,title,ludique,quote,author):
    band=('<div class="band" style="background:%s">'%col
      +'<span class="blob"></span>'
      +'<div class="bnum serif">%s</div>'%(str(n) if n<12 else "★")
      +'<div class="bic">%s</div>'%ic(icon,col,5.4,1.9)
      +'<div class="bsec">%s</div></div>'%section.upper())
    if n==12:
        body=('<div class="body qbody">'
          +'<div class="qbox">%s</div>'%qr
          +'<div class="qtxt"><b class="serif" style="font-size:11pt;color:%s">Pour aller plus loin</b><br>Scanne pour le <b>diaporama animé</b>.<br><span style="color:%s">Réalisé avec Claude — l\'IA assiste, l\'humain décide.</span></div></div>'%(NAVY,AMBERD))
    else:
        q='<div class="quote">« %s »</div>'%quote if quote else ''
        a='<div class="auth">%s</div>'%author if author else ''
        wm='<div class="wm">%s</div>'%ic(icon,col,30,1.3)
        body=('<div class="body">'+wm+'<span class="cf cf1"></span><span class="cf cf2"></span>'
          +'<div class="ttl serif">%s</div><div class="lud">%s</div>%s%s</div>'%(title,ludique,q,a))
    return '<div class="card">%s%s%s</div>'%(band,body,rail(n))

def back(n,mirror=True):
    r,c=POS[n-1]
    posx=(c/(COLS-1))*100; posy=(r/(ROWS-1))*100
    mir="transform:scaleX(-1);" if mirror else ""
    return '<div class="card back"><div class="tile" style="%sbackground-image:url(%s);background-size:%d%% %d%%;background-position:%.4f%% %.4f%%"></div></div>'%(mir,POSTER,COLS*100,ROWS*100,posx,posy)

fronts=[front(*c) for c in C]; backs=[back(c[0]) for c in C]; reveal=[back(c[0],False) for c in C]
def sheets(cards):
    out="";
    for i in range(0,len(cards),8): out+='<div class="sheet">%s</div>'%("".join(cards[i:i+8]))
    return out

CSS=FONTS+"""
*{box-sizing:border-box} body{margin:0;background:#DED9CF;font-family:system-ui,-apple-system,'Segoe UI',Roboto,sans-serif}
.serif{font-family:'Fraunces',Georgia,serif}
.sheet{width:210mm;height:297mm;background:#fff;margin:8mm auto;display:grid;grid-template-columns:88.9mm 88.9mm;grid-auto-rows:63.5mm;justify-content:center;align-content:start;gap:6mm 8mm;padding:14mm 0;page-break-after:always;box-shadow:0 3mm 8mm rgba(0,0,0,.15)}
.card{width:88.9mm;height:63.5mm;background:%s;border-radius:3mm;overflow:hidden;display:flex;flex-direction:column;position:relative;outline:.2mm dashed #C9CFD8}
.band{height:14mm;flex:none;display:flex;align-items:center;gap:2.6mm;padding:0 5mm;color:#fff;position:relative;overflow:hidden}
.blob{position:absolute;width:20mm;height:20mm;border-radius:50%%;background:rgba(255,255,255,.10);right:-5mm;top:-6mm}
.bnum{font-size:19pt;font-weight:600;line-height:1;z-index:1}
.bic{width:8.4mm;height:8.4mm;border-radius:50%%;background:#fff;display:flex;align-items:center;justify-content:center;flex:none;z-index:1}
.bsec{margin-left:auto;font-size:6.2pt;font-weight:700;letter-spacing:.11em;text-align:right;z-index:1}
.body{flex:1;padding:3.4mm 5mm 1mm;position:relative;overflow:hidden}
.wm{position:absolute;right:-5mm;bottom:-7mm;opacity:.06;z-index:0}
.body>.ttl,.body>.lud,.body>.quote,.body>.auth{position:relative;z-index:1}
.cf{position:absolute;border-radius:50%%;display:block}
.cf1{width:2mm;height:2mm;background:%s;top:2.4mm;right:4mm}
.cf2{width:1.3mm;height:1.3mm;background:%s;top:4.6mm;right:2.2mm}
.ttl{font-size:12.5pt;font-weight:600;color:%s;line-height:1.06;margin-bottom:1.4mm}
.lud{font-size:8.2pt;line-height:1.32;color:%s}
.quote{font-family:'Fraunces',serif;font-style:italic;font-size:8.2pt;color:%s;border-left:.8mm solid %s;padding-left:2mm;margin-top:1.6mm;line-height:1.2}
.auth{font-size:6.6pt;color:%s;font-style:italic;margin-top:1.4mm}
/* rail de liaison */
.rail{height:8mm;flex:none;position:relative}
.line{position:absolute;left:0;right:0;top:3.9mm;height:.9mm;background:%s}
.node{position:absolute;left:calc(50%% - 3mm);top:1.3mm;width:6mm;height:6mm;border-radius:50%%;border:.8mm solid #fff;box-shadow:0 0 0 .3mm %s}
.ochev{position:absolute;top:1.7mm;display:flex}
.drop{position:absolute;left:calc(50%% - .45mm);top:3.9mm;width:.9mm;height:4.1mm;background:%s}
.dchev{position:absolute;left:calc(50%% - 1.7mm);top:4.8mm}
.tdrop{position:absolute;left:calc(50%% - .45mm);top:0;width:.9mm;height:3.4mm;background:%s;z-index:2}
.tchev{position:absolute;left:calc(50%% - 1.5mm);top:2.2mm;z-index:2}
.qbody{display:flex;align-items:center;gap:3mm;padding:2.6mm 5mm}
.qbox{width:22mm;height:22mm;flex:none;background:#fff;border:.3mm solid %s;border-radius:1.5mm;padding:1.4mm}
.qbox svg{width:100%%;height:100%%;display:block}
.qtxt{font-size:6.8pt;color:%s;line-height:1.42}
.back{padding:0}.tile{width:100%%;height:100%%;background-repeat:no-repeat}
.reveal{max-width:820px;margin:16px auto;padding:16px}
.revgrid{display:grid;grid-template-columns:repeat(3,1fr);grid-auto-rows:1fr;gap:0;border:1px solid %s;border-radius:8px;overflow:hidden}
.revgrid .card{width:auto;height:auto;aspect-ratio:889/635;outline:none;border-radius:0}
.revcap{text-align:center;color:#555;font-size:12px;margin-top:10px}
@media print{ body{background:#fff} .sheet{margin:0;box-shadow:none} .noprint{display:none!important} }
"""%(PAPER,AMBER,SLATE,NAVY,GREY,AMBERD,AMBER,GREY,AMBER,AMBER,AMBER,AMBER,LINE,GREY,LINE)

reveal_html='<div class="reveal noprint"><div class="revgrid">%s</div><div class="revcap">Versos assemblés (après retournement) : le logo Éklore.</div></div>'%("".join(reveal))
HTML='<title>Jeu de cartes — Soutenance MFE</title><style>%s</style>%s%s%s'%(CSS,reveal_html,sheets(fronts),sheets(backs))
open(os.path.join(SCR,"cards.html"),"w",encoding="utf-8").write(HTML)
print("cards.html OK — parcours serpent, fil conducteur continu")
