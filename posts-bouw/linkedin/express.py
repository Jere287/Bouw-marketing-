"""Arma documentos para Adobe Express a partir de html/<pieza>.html (generados por gen_li.py).

Cada documento junta varias piezas como páginas (.slide), con:
- las letras por enlace (Typekit para IBM Plex y Google Fonts para Archivo e Instrument Serif), para que Express las reconozca;
- las imágenes incrustadas y reducidas al tamaño en que se ven, para que el archivo no pese de más.

Uso: python3 express.py  →  express/<documento>.html
"""
import base64, io, os, re
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, 'html')
OUT = os.path.join(HERE, 'express')
os.makedirs(OUT, exist_ok=True)

DOCS = {
    'bouw-li-casos': ['K01-caso-anatris', 'K02-caso-charms-ecuador', 'K03-caso-mejora-continua-planta',
                      'K04-caso-hoy-vs-bouw', 'K05-cierre-de-ano-la-cuenta'],
    'bouw-li-campana-1': ['L01-presentacion', 'L02-lean-ingenieria-de-planta', 'L03-cumplimiento-normativo-bpm',
                          'L04-programa-contable-excel', 'L05-simulacion-de-flujos'],
    'bouw-li-campana-2': ['L06-cual-te-suena', 'L07-en-que-condiciones', 'L08-la-cuenta',
                          'L09-donde-pierde-horas', 'L10-contacto'],
    'bouw-li-calidad': ['Q01-calidad-el-inspector', 'Q02-calidad-trazabilidad', 'Q03-calidad-informe-auditoria',
                        'Q04-calidad-capa-8d', 'Q05-calidad-lotes-retenidos'],
    'bouw-li-automatizacion': ['Z01-automatizacion-si-se-repite', 'Z02-automatizacion-copiar-datos',
                               'Z03-automatizacion-cierre-de-mes', 'Z04-automatizacion-tres-archivos',
                               'Z05-automatizacion-no-todo'],
    'bouw-li-carrusel': [f'C0{i}-carrusel-proyectos' for i in range(1, 8)],
}

FONTS = ('<link rel="stylesheet" href="https://use.typekit.net/dnh2wmm.css">'
         '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wght@600;700;800'
         '&amp;family=Instrument+Serif:ital@1&amp;display=swap">')
FAMILY = {'"Archivo"': '"Archivo",sans-serif', '"Plex",sans-serif': '"ibm-plex-sans",sans-serif',
          '"Plex"': '"ibm-plex-sans",sans-serif', '"PlexMono"': '"ibm-plex-mono",monospace',
          '"Instrument"': '"Instrument Serif",serif', 'font-family:Archivo': 'font-family:"Archivo",sans-serif'}

_cache = {}


def shrink(src, width):
    """Imagen reducida a ~1,5× el ancho en que se ve. PNG si tiene transparencia, JPEG si no."""
    key = (src[:200], len(src), width)
    if key in _cache:
        return _cache[key]
    if src.startswith('file://'):
        im = Image.open(src[7:])
    else:
        im = Image.open(io.BytesIO(base64.b64decode(src.split(',', 1)[1])))
    target = min(im.width, max(int(width * 1.5), 200))
    if im.width > target:
        im = im.resize((target, round(im.height * target / im.width)), Image.LANCZOS)
    buf = io.BytesIO()
    alpha = im.mode in ('RGBA', 'LA', 'P') and im.convert('RGBA').getextrema()[3][0] < 255
    if alpha:
        im.convert('RGBA').save(buf, 'PNG', optimize=True)
        out = 'data:image/png;base64,'
    else:
        im.convert('RGB').save(buf, 'JPEG', quality=86, optimize=True)
        out = 'data:image/jpeg;base64,'
    _cache[key] = out + base64.b64encode(buf.getvalue()).decode()
    return _cache[key]


def piece(name):
    doc = open(os.path.join(SRC, name + '.html')).read()
    css = re.search(r'<style>(.*?)</style>', doc, re.S).group(1)
    css = re.sub(r'@font-face\{.*?\}', '', css)
    m = re.search(r'(<section class="slide".*?</section>)', doc, re.S)
    sec = m.group(1)

    def img(mm):
        tag = mm.group(0)
        w = re.search(r'width:(\d+)px', tag)
        return tag.replace(mm.group(1), shrink(mm.group(1), int(w.group(1)) if w else 1080))
    sec = re.sub(r'<img[^>]*?src="([^"]+)"[^>]*>', img, sec)
    for a, b in FAMILY.items():
        css = css.replace(a, b)
        sec = sec.replace(a, b)
    w, h = re.search(r'width:(\d+)px;height:(\d+)px', sec).groups()
    sec = sec.replace('<section class="slide"', f'<section class="slide" data-canvas-width="{w}" data-canvas-height="{h}"', 1)
    return css, sec, w, h


for doc_name, names in DOCS.items():
    css, secs = None, []
    for n in names:
        c, s, w, h = piece(n)
        css = css or c
        secs.append(s)
    html = (f'<!doctype html><html lang="es"><head><meta charset="utf-8"><title>BOUW · {doc_name}</title>'
            f'<meta name="hz:slide-selector" content=".slide"><meta name="hz:canvas-width" content="{w}">'
            f'<meta name="hz:canvas-height" content="{h}">{FONTS}<style>{css}'
            f'.slide{{margin:0 0 40px 0}}</style></head><body>{"".join(secs)}</body></html>')
    p = os.path.join(OUT, doc_name + '.html')
    open(p, 'w').write(html)
    print(doc_name, len(names), 'páginas', round(len(html) / 1e6, 2), 'MB')
