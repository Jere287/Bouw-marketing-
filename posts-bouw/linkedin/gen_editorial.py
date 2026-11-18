"""Línea editorial de BOUW para LinkedIn (serie E): estilo de consultora, no de plantilla.

Reglas de esta línea:
- Fotos reales de planta y capturas reales de los proyectos (sitio/imagenes/), nada de íconos ni maquetas dibujadas.
- Una sola idea por pieza; mucho aire; una sola familia para titulares (Archivo) y una para texto (IBM Plex Sans).
- Logo pequeño abajo, como firma. Sin brillos, sin degradados de colores, sin retícula, sin botones falsos.
- Colores de BOUW: azul noche, cian y naranja como acento, sobre papel claro o sobre la foto.

Uso: python3 gen_editorial.py && node shot_editorial.js  →  png/E*.png
"""
import base64, html, io, os
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, '..'))
IMGS = os.path.join(ROOT, 'sitio', 'imagenes')
FONTS = os.path.join(ROOT, 'fonts')
OUT = os.path.join(HERE, 'html_editorial')
os.makedirs(OUT, exist_ok=True)

W, H, M = 1080, 1350, 84
PAPER, INK, NAVY, CYAN, CYAN_D, ORANGE, MUTED = '#f3f1ec', '#0b1a2e', '#0d2947', '#4fd6e8', '#1a97b3', '#e8833a', '#5b6b7e'
LOGO_DARK = os.path.join(ROOT, 'sitio', 'dragon', 'capturas', 'dragon-oscuro-realidad-transparente.png')
LOGO_LIGHT = os.path.join(ROOT, 'sitio', 'dragon', 'capturas', 'dragon-claro-realidad-transparente.png')


def data(path, width, crop=None, quality=88):
    im = Image.open(path)
    if crop:
        im = im.crop(crop)
    if im.width > width * 2:
        im = im.resize((width * 2, round(im.height * width * 2 / im.width)), Image.LANCZOS)
    buf = io.BytesIO()
    if im.mode in ('RGBA', 'LA', 'P'):
        im.convert('RGBA').save(buf, 'PNG', optimize=True)
        return 'data:image/png;base64,' + base64.b64encode(buf.getvalue()).decode()
    im.convert('RGB').save(buf, 'JPEG', quality=quality)
    return 'data:image/jpeg;base64,' + base64.b64encode(buf.getvalue()).decode()


def site(name):
    return os.path.join(IMGS, name + '.png')


def e(s):
    return html.escape(s, quote=False)


CSS = f"""
@font-face{{font-family:"Archivo";src:url(file://{FONTS}/Archivo-100_900.woff2);font-weight:100 900;font-stretch:62% 125%}}
@font-face{{font-family:"Plex";src:url(file://{FONTS}/IBMPlexSans-400.woff2);font-weight:400}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{background:{PAPER}}}
.slide{{position:relative;overflow:hidden;width:{W}px;height:{H}px;font-family:"Plex",sans-serif}}
.abs{{position:absolute}}
.hl{{font-family:"Archivo";font-weight:650;letter-spacing:-0.025em;line-height:1.02}}
.tx{{font-family:"Plex";font-weight:400;line-height:1.45}}
.lab{{font-family:"Plex";font-weight:400;font-size:24px;line-height:32px}}
"""


def label(t, color, top=80, left=M):
    """Etiqueta superior: una línea corta de cian y el tema, sin mayúsculas forzadas."""
    return f'<div class="abs lab" style="left:{left}px;top:{top}px;width:800px;color:{color}">{e(t)}</div>'


def firma(dark=False, top=H - 120):
    """Pie: filete fino, logo pequeño a la izquierda y el sitio a la derecha."""
    logo = data(LOGO_DARK if dark else LOGO_LIGHT, 160)
    line = 'rgba(255,255,255,.22)' if dark else 'rgba(11,26,46,.14)'
    col = 'rgba(255,255,255,.72)' if dark else MUTED
    return (f'<div class="abs" style="left:{M}px;top:{top}px;width:{W - 2 * M}px;height:1px;background:{line}"></div>'
            f'<img class="abs" src="{logo}" style="left:{M - 4}px;top:{top + 22}px;width:150px;height:{round(150 / 1.905)}px">'
            f'<div class="abs tx" style="left:{W - M - 500}px;top:{top + 40}px;width:500px;text-align:right;font-size:21px;color:{col}">bouw-eight.vercel.app</div>')


def photo(path, x, y, w, h, pos='center', crop=None):
    return (f'<img class="abs" src="{data(path, w, crop)}" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;'
            f'object-fit:cover;object-position:{pos}">')


def shot(path, x, y, w, h, pos='top', radius=10):
    """Captura de pantalla de un proyecto, con sombra suave, como en un informe."""
    return (f'<img class="abs" src="{data(path, w)}" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;object-fit:cover;'
            f'object-position:{pos};border-radius:{radius}px;box-shadow:0 24px 60px rgba(11,26,46,.18),0 2px 6px rgba(11,26,46,.08)">')


def facts(rows, top, dark=False, num_color=None):
    """Tres datos en columnas, con un filete encima, como la tabla de un informe."""
    col_n = num_color or (CYAN if dark else NAVY)
    col_t = 'rgba(255,255,255,.75)' if dark else MUTED
    line = 'rgba(255,255,255,.22)' if dark else 'rgba(11,26,46,.14)'
    cw = (W - 2 * M) // len(rows)
    out = f'<div class="abs" style="left:{M}px;top:{top}px;width:{W - 2 * M}px;height:1px;background:{line}"></div>'
    for i, (n, t) in enumerate(rows):
        x = M + i * cw
        out += (f'<div class="abs hl" style="left:{x}px;top:{top + 28}px;width:{cw - 20}px;font-size:64px;color:{col_n}">{n}</div>'
                f'<div class="abs tx" style="left:{x}px;top:{top + 106}px;width:{cw - 30}px;font-size:22px;line-height:30px;color:{col_t}">{e(t)}</div>')
    return out


pieces = []


def add(name, bg, body):
    pieces.append((name, f'<section class="slide" style="background:{bg}">{body}</section>'))


# E01 · Presentación sobre la foto real de la línea de extrusión
add('E01-quienes-somos', INK,
    photo(site('mejora-linea-extrusion'), 0, 0, W, H, pos='center 35%')
    + f'<div class="abs" style="left:0;top:0;width:{W}px;height:{H}px;background:linear-gradient(180deg,rgba(6,16,31,.15) 0%,rgba(6,16,31,.35) 40%,rgba(6,16,31,.92) 72%,#06101f 100%)"></div>'
    + f'<div class="abs" style="left:0;top:0;width:{W}px;height:260px;background:linear-gradient(180deg,rgba(6,16,31,.75),rgba(6,16,31,0))"></div>'
    + label('Quito y Monterrey', '#ffffff', top=80)
    + f'<div class="abs hl" style="left:{M}px;top:760px;width:880px;font-size:76px;color:#fff">Ingeniería de procesos para empresas que fabrican.</div>'
    + f'<div class="abs tx" style="left:{M}px;top:1030px;width:820px;font-size:28px;color:rgba(255,255,255,.82)">Mejora de planta, calidad y automatización. Más de 7 años entre Ecuador y México.</div>'
    + firma(dark=True))

# E02 · Un dato grande del caso de mejora continua
add('E02-dato-reprocesos', PAPER,
    label('Caso real', CYAN_D)
    + f'<div class="abs hl" style="left:{M - 8}px;top:250px;width:1000px;font-size:300px;line-height:1;color:{NAVY};letter-spacing:-0.05em">−20 %</div>'
    + f'<div class="abs hl" style="left:{M}px;top:580px;width:900px;font-size:58px;color:{INK}">de reprocesos en la línea.</div>'
    + f'<div class="abs tx" style="left:{M}px;top:690px;width:820px;font-size:28px;color:{MUTED}">Sin comprar maquinaria nueva: ordenando el flujo y dejando un trabajo estándar que el equipo sí sigue.</div>'
    + photo(site('mejora-perfil-estudio'), M, 850, W - 2 * M, 250, pos='center 40%')
    + firma())

# E03 · Una idea (frase del sitio), sin adornos
add('E03-primero-medimos', NAVY,
    label('Cómo trabajamos', CYAN)
    + f'<div class="abs hl" style="left:{M}px;top:300px;width:200px;font-size:200px;line-height:1;color:{CYAN}">“</div>'
    + f'<div class="abs hl" style="left:{M}px;top:470px;width:900px;font-size:74px;line-height:1.1;color:#fff">Medimos tu proceso real antes de proponer nada.</div>'
    + f'<div class="abs tx" style="left:{M}px;top:760px;width:820px;font-size:32px;color:rgba(255,255,255,.78)">Si al final no hay proyecto, la medición se queda contigo igual.</div>'
    + f'<div class="abs tx" style="left:{M}px;top:1080px;width:820px;font-size:24px;color:rgba(255,255,255,.55)">El diagnóstico toma de una a dos semanas.</div>'
    + firma(dark=True))

# E04 · Foto de medición en piso + titular
add('E04-medimos-en-piso', PAPER,
    photo(site('mejora-termometro'), 0, 0, W, 760, pos='center 38%')
    + label('Mejora continua', CYAN_D, top=820)
    + f'<div class="abs hl" style="left:{M}px;top:880px;width:900px;font-size:62px;color:{INK}">Las mejoras se deciden en piso, no en una presentación.</div>'
    + f'<div class="abs tx" style="left:{M}px;top:1080px;width:880px;font-size:26px;color:{MUTED}">Tiempos, temperaturas, recorridos y reprocesos, medidos en la línea.</div>'
    + firma())

# E05 · Caso Programa contable
add('E05-caso-programa-contable', PAPER,
    label('Caso real', CYAN_D)
    + f'<div class="abs hl" style="left:{M}px;top:150px;width:900px;font-size:66px;color:{INK}">Un ERP completo dentro de un solo Excel.</div>'
    + f'<div class="abs tx" style="left:{M}px;top:310px;width:880px;font-size:27px;color:{MUTED}">Inventario, kits, ventas y caja en once hojas conectadas. El equipo siguió en la herramienta que ya sabía usar.</div>'
    + shot(site('contable-excel-es-poster'), M, 450, W - 2 * M, 520, pos='top')
    + facts([('11', 'hojas conectadas'), ('0', 'licencias nuevas'), ('1', 'archivo para todo')], 1020)
    + firma())

# E06 · Caso Charms Ecuador
ph = ''.join(shot(site(n), M + i * 312, 440, 288, 560, pos='top', radius=22)
             for i, n in enumerate(['charms-movil-inicio', 'charms-movil-cotizar', 'charms-movil-pedidos']))
add('E06-caso-charms-ecuador', NAVY,
    label('Caso real', CYAN)
    + f'<div class="abs hl" style="left:{M}px;top:150px;width:900px;font-size:66px;color:#fff">El pedido llega a WhatsApp ya escrito.</div>'
    + f'<div class="abs tx" style="left:{M}px;top:310px;width:880px;font-size:27px;color:rgba(255,255,255,.75)">Catálogo con fotos reales y un cotizador en cuatro pasos. El taller solo confirma.</div>'
    + ph
    + facts([('15', 'modelos con foto real'), ('4', 'pasos para cotizar'), ('$0', 'al mes en hosting')], 1030, dark=True)
    + firma(dark=True))

# E07 · Caso Anatris
add('E07-caso-anatris', PAPER,
    label('Producto propio', CYAN_D)
    + f'<div class="abs hl" style="left:{M}px;top:150px;width:900px;font-size:66px;color:{INK}">Un atlas 3D de anatomía que funciona en el navegador.</div>'
    + f'<div class="abs tx" style="left:{M}px;top:310px;width:880px;font-size:27px;color:{MUTED}">Para fisioterapia: cada músculo con su ficha y cada dato clínico con su fuente.</div>'
    + shot(site('anatris-cuerpo'), M, 450, W - 2 * M, 520, pos='center')
    + facts([('113', 'músculos con ficha'), ('79', 'tests clínicos'), ('6', 'regiones del cuerpo')], 1020)
    + firma())

# E08 · Cómo trabajamos: cuatro pasos, como una tabla de propuesta
steps = [('Diagnóstico', '1 a 2 semanas', 'Medimos el proceso real antes de proponer nada.'),
         ('Precio cerrado', '3 a 5 días', 'Alcance, entregables, plazo y precio por escrito.'),
         ('Entrega semanal', '4 a 10 semanas', 'Cada semana ves algo que ya funciona.'),
         ('Acompañamiento', '30 días', 'Seguimos contigo mientras el proceso se estabiliza.')]
rows = ''
for i, (t, p, d) in enumerate(steps):
    y = 430 + i * 165
    rows += (f'<div class="abs" style="left:{M}px;top:{y}px;width:{W - 2 * M}px;height:1px;background:rgba(11,26,46,.14)"></div>'
             f'<div class="abs hl" style="left:{M}px;top:{y + 30}px;width:80px;font-size:34px;color:{ORANGE}">0{i + 1}</div>'
             f'<div class="abs hl" style="left:{M + 90}px;top:{y + 30}px;width:500px;font-size:38px;color:{INK}">{e(t)}</div>'
             f'<div class="abs tx" style="left:{W - M - 300}px;top:{y + 36}px;width:300px;text-align:right;font-size:24px;color:{CYAN_D}">{e(p)}</div>'
             f'<div class="abs tx" style="left:{M + 90}px;top:{y + 88}px;width:760px;font-size:24px;color:{MUTED}">{e(d)}</div>')
add('E08-como-trabajamos', PAPER,
    label('Cómo trabajamos', CYAN_D)
    + f'<div class="abs hl" style="left:{M}px;top:150px;width:900px;font-size:66px;color:{INK}">Plazos y precio por escrito, antes de empezar.</div>'
    + rows
    + firma())

# E09 · Del diseño a la realidad: la pieza en la mano
add('E09-del-diseno-a-la-realidad', INK,
    photo(site('mejora-perfil-seccion'), 0, 0, W, H, pos='center')
    + f'<div class="abs" style="left:0;top:0;width:{W}px;height:{H}px;background:linear-gradient(180deg,rgba(6,16,31,0) 30%,rgba(6,16,31,.88) 70%,#06101f 100%)"></div>'
    + f'<div class="abs" style="left:0;top:0;width:{W}px;height:260px;background:linear-gradient(180deg,rgba(6,16,31,.75),rgba(6,16,31,0))"></div>'
    + label('Mejora continua', '#ffffff')
    + f'<div class="abs hl" style="left:{M}px;top:880px;width:900px;font-size:84px;color:#fff">Del diseño a la realidad.</div>'
    + f'<div class="abs tx" style="left:{M}px;top:1080px;width:880px;font-size:27px;color:rgba(255,255,255,.8)">Llevamos lo que se dibuja en papel a una línea que lo fabrica igual, todos los días.</div>'
    + firma(dark=True))

names = []
for name, sec in pieces:
    open(os.path.join(OUT, name + '.html'), 'w').write(
        f'<!doctype html><html lang="es"><head><meta charset="utf-8"><style>{CSS}</style></head><body>{sec}</body></html>')
    names.append(f'{name}:{W}x{H}')
open(os.path.join(OUT, 'list.txt'), 'w').write('\n'.join(names))
print(len(pieces), 'piezas')
