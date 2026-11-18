"""Piezas de LinkedIn de BOUW hechas con el logo y los textos de bouw-eight.vercel.app.

Logo: el dragón 3D del sitio (marca/dragon-3d/, renderizado de /dragon.glb) y el dragón sobre BOUW en 3D (sitio/dragon/capturas/)
(antes se usaba el PNG plano blanco; ya no).
Textos: sitio/TEXTOS-DEL-SITIO.md. Colores y letras: los del CSS del sitio (tema oscuro), con Archivo, IBM Plex Sans,
IBM Plex Mono e Instrument Serif.

Genera html/<pieza>.html y list.txt; shot.js las pasa a png/ y pdf.js arma el carrusel en PDF.
"""
import base64, html, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, '..'))
OUT = os.path.join(HERE, 'html')
os.makedirs(OUT, exist_ok=True)
FONTS = os.path.join(ROOT, 'fonts')
IMGS = os.path.join(ROOT, 'sitio', 'imagenes')


def b64(path):
    ext = path.rsplit('.', 1)[1].lower()
    mime = {'png': 'image/png', 'jpg': 'image/jpeg', 'jpeg': 'image/jpeg', 'webp': 'image/webp'}[ext]
    return f'data:{mime};base64,' + base64.b64encode(open(path, 'rb').read()).decode()


# El logo de verdad: el dragón 3D del sitio (modelo /dragon.glb) sobre las letras BOUW en 3D del encabezado.
LOGO = 'file://' + os.path.join(ROOT, 'sitio', 'dragon', 'capturas', 'dragon-oscuro-realidad-transparente.png')  # 2135×1121
DRAGON = 'file://' + os.path.join(ROOT, 'marca', 'dragon-3d', 'bouw-dragon-3d.png')                            # 2662×1980
LOGO_R = 2135 / 1121
DRAGON_R = 2662 / 1980


def glow(cx, cy, r, op=0.55, color='34,181,207'):
    """Halo cian detrás del dragón, como la luz de borde del sitio."""
    return (f'<div class="abs" style="left:{cx - r}px;top:{cy - r}px;width:{2 * r}px;height:{2 * r}px;border-radius:50%;'
            f'background:radial-gradient(circle,rgba({color},{op}) 0%,rgba({color},{op * 0.35}) 38%,rgba({color},0) 70%)"></div>')


def hero(x, y, w, halo=0.5):
    """El dragón 3D grande con su halo."""
    h = round(w / DRAGON_R)
    return glow(x + w // 2, y + h // 2, int(w * 0.62), halo) + dragon(x, y, w)


def logo(x, y, w):
    """Logo del sitio (BOUW + dragón). Se da el ancho; el alto sale de la proporción 720×304."""
    return f'<img class="abs" alt="BOUW" src="{LOGO}" style="left:{x}px;top:{y}px;width:{w}px;height:{round(w / LOGO_R)}px">'


def dragon(x, y, w, op=1):
    o = f';opacity:{op}' if op != 1 else ''
    return f'<img class="abs" alt="" src="{DRAGON}" style="left:{x}px;top:{y}px;width:{w}px;height:{round(w / DRAGON_R)}px;filter:drop-shadow(0 18px 40px rgba(0,0,0,.55)){o}">'


def photo(name, x, y, w, h, fit='cover', pos='center'):
    """Imagen del sitio (sitio/imagenes/). Si todavía no está, deja un recuadro."""
    for ext in ('webp', 'jpg', 'png'):
        p = os.path.join(IMGS, f'{name}.{ext}')
        if os.path.exists(p):
            return (f'<img class="abs" alt="" src="{b64(p)}" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;'
                    f'object-fit:{fit};object-position:{pos};border-radius:18px">')
    return f'<div class="abs" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;border-radius:18px;background:#0b2036"></div>'


CSS = f"""
@font-face{{font-family:"Archivo";src:url(file://{FONTS}/Archivo-100_900.woff2);font-weight:100 900;font-stretch:62% 125%}}
@font-face{{font-family:"Plex";src:url(file://{FONTS}/IBMPlexSans-400.woff2);font-weight:400}}
@font-face{{font-family:"PlexMono";src:url(file://{FONTS}/IBMPlexMono-500.woff2);font-weight:500}}
@font-face{{font-family:"Instrument";src:url(file://{FONTS}/InstrumentSerif-Italic.ttf);font-style:italic}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{background:#04101f}}
.slide{{position:relative;overflow:hidden;background:#04101f;color:#e8eef6;font-family:"Plex",sans-serif}}
.abs{{position:absolute}}
.h{{font-family:"Archivo";font-weight:700;letter-spacing:-0.028em;line-height:0.98;color:#e8eef6}}
.t{{font-family:"Archivo";font-weight:600;letter-spacing:-0.015em;line-height:1.15;color:#e8eef6}}
.dim{{color:#3d5a7a}}
.c{{color:#4fd6e8}}
.o{{color:#f79b4a}}
.serif{{font-family:"Instrument";font-style:italic;font-weight:400;letter-spacing:-0.01em;line-height:1.05;color:#e8eef6}}
.mono{{font-family:"PlexMono";font-weight:500;text-transform:uppercase;letter-spacing:0.2em;color:#8fa8c4}}
.k{{font-family:"PlexMono";font-weight:500;letter-spacing:0.06em;color:#4fd6e8}}
.p{{font-family:"Plex";font-weight:400;color:#c6d4e4;line-height:1.4}}
.rule{{position:absolute;height:2px;background:#15304d}}
.crule{{position:absolute;height:2px;background:#22b5cf}}
.panel{{position:absolute;background:#071a2f;border:2px solid #15304d;border-radius:18px}}
.chip{{position:absolute;border:2px solid #23415f;border-radius:40px;font-family:"PlexMono";font-weight:500;color:#c6d4e4;text-align:center}}
.btn{{position:absolute;background:#22b5cf;color:#04101f;font-family:"Archivo";font-weight:700;text-align:center;letter-spacing:-0.01em}}
"""


def e(s):
    return html.escape(s, quote=False)


def grad(text, a=(0x4f, 0xd6, 0xe8), b=(0xf7, 0x9b, 0x4a)):
    """Degradado cian → naranja letra por letra, como "se automatiza." en el sitio (se importa como texto editable)."""
    n = max(len(text) - 1, 1)
    out = ''
    for i, ch in enumerate(text):
        t = i / n
        c = '#%02x%02x%02x' % tuple(round(a[j] + (b[j] - a[j]) * t) for j in range(3))
        out += f'<span style="color:{c}">{e(ch)}</span>' if ch != ' ' else ' '
    return out


LEMA = 'Si se repite, ' + grad('se automatiza.')


def grid(w, h, step=60):
    d = ''.join(f'M{x} 0V{h}' for x in range(step, w, step)) + ''.join(f'M0 {y}H{w}' for y in range(step, h, step))
    return (f'<svg class="abs" style="left:0;top:0" width="{w}" height="{h}" viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg">'
            f'<path d="{d}" fill="none" stroke="#4fd6e8" stroke-opacity="0.04" stroke-width="2"/></svg>')


pieces = []  # (archivo, w, h, cuerpo)


def add(name, w, h, body, step=60):
    pieces.append((name, w, h, grid(w, h, step) + body))


def dash(x, y, w):
    return f'<div class="abs" style="left:{x}px;top:{y}px;width:{w}px;height:2px;background:#22b5cf;opacity:.6"></div>'


# Ayudas comunes de dibujo (series y visuales)
W, H, M = 1080, 1350, 84
IW = W - 2 * M
OR, CY, RED, YEL, GRN = '#f79b4a', '#4fd6e8', '#ff6b5e', '#f2c94c', '#5ad19a'


def serie(code, n, tema, color):
    return (logo(M, 50, 190)
            + f'<div class="abs" style="left:{W - M - 330}px;top:78px;width:330px;height:44px;border:2px solid {color};border-radius:22px"></div>'
            + f'<div class="abs mono" style="left:{W - M - 330}px;top:78px;width:330px;height:44px;text-align:center;font-size:18px;line-height:40px;color:{color}">{tema}</div>'
            + f'<div class="rule" style="left:{M}px;top:156px;width:{IW}px"></div>')


def check(x, y, txt, col=GRN, size=28, w=IW):
    return (f'<div class="abs" style="left:{x}px;top:{y + 4}px;width:36px;height:36px;border-radius:18px;background:{col};color:#04101f;'
            f'font-family:Archivo;font-weight:800;font-size:24px;line-height:36px;text-align:center">✓</div>'
            f'<div class="abs p" style="left:{x + 56}px;top:{y}px;width:{w - 56}px;font-size:{size}px;line-height:44px;color:#e8eef6">{txt}</div>')


def cross(x, y, txt, size=28, w=IW):
    return (f'<div class="abs" style="left:{x}px;top:{y + 4}px;width:36px;height:36px;border-radius:18px;border:2px solid {RED};color:{RED};'
            f'font-family:Archivo;font-weight:800;font-size:22px;line-height:32px;text-align:center">✕</div>'
            f'<div class="abs p" style="left:{x + 56}px;top:{y}px;width:{w - 56}px;font-size:{size}px;line-height:44px;color:#c6d4e4">{txt}</div>')


def box(x, y, w, h, txt, col='#23415f', tc='#e8eef6', fs=24, bg='#071a2f'):
    return (f'<div class="abs" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;background:{bg};border:2px solid {col};border-radius:12px"></div>'
            f'<div class="abs k" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;text-align:center;font-size:{fs}px;line-height:{h}px;color:{tc}">{txt}</div>')


def line(x1, y1, x2, y2, col='#23415f', wd=3, dash=''):
    d = f' stroke-dasharray="{dash}"' if dash else ''
    return (f'<svg class="abs" style="left:0;top:0" width="{W}" height="{H}" viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg">'
            f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{col}" stroke-width="{wd}"{d}/></svg>')


def callout(top, h, label, txt, col=CY, size=27):
    return (f'<div class="panel" style="left:{M}px;top:{top}px;width:{IW}px;height:{h}px"></div>'
            f'<div class="abs" style="left:{M}px;top:{top}px;width:6px;height:{h}px;background:{col};border-radius:3px"></div>'
            f'<div class="abs mono" style="left:{M + 40}px;top:{top + 26}px;width:600px;font-size:17px;line-height:24px;color:{col}">{label}</div>'
            + para(txt, top + 62, size=size, lh=round(size * 1.38), color='#e8eef6', width=IW - 80, left=M + 40))


# =====================================================================
# 6. VISUALES DIBUJADOS (sin capturas): un dibujo por proyecto del sitio, en un lienzo de 912×460
# =====================================================================
VW, VH = 912, 460


def vis(inner, x, y, scale=1.0):
    return (f'<div class="abs" style="left:{x}px;top:{y}px;width:{VW}px;height:{VH}px;transform:scale({scale});transform-origin:0 0">'
            f'{inner}</div>')


def vpanel():
    return f'<div class="abs" style="left:0;top:0;width:{VW}px;height:{VH}px;background:#071a2f;border:2px solid #15304d;border-radius:20px"></div>'


def svg(body):
    return f'<svg class="abs" style="left:0;top:0;overflow:visible" width="{VW}" height="{VH}" viewBox="0 0 {VW} {VH}" xmlns="http://www.w3.org/2000/svg">{body}</svg>'


def tx(x, y, w, t, size=20, col='#e8eef6', cls='p', align='left', lh=None, extra=''):
    lh = lh or round(size * 1.3)
    return f'<div class="abs {cls}" style="left:{x}px;top:{y}px;width:{w}px;font-size:{size}px;line-height:{lh}px;color:{col};text-align:{align}{extra}">{t}</div>'


def v_mejora():
    """Caso de mejora continua: antes y después (índice, antes = 100)."""
    out = vpanel() + tx(34, 26, 600, 'Índice · antes = 100', 15, '#8fa8c4', 'mono')
    base = 400
    for g, (lab, after, delta) in enumerate([('Tiempo de preparación', 85, '−15 %'), ('Reprocesos', 80, '−20 %')]):
        gx = 70 + g * 430
        for b, (val, col, nm) in enumerate([(100, OR, 'Antes'), (after, CY, 'Con BOUW')]):
            bx = gx + b * 150
            h = val * 2.6
            out += (f'<div class="abs" style="left:{bx}px;top:{base - h}px;width:110px;height:{h}px;border-radius:10px 10px 0 0;'
                    f'background:linear-gradient(180deg,{col},{col}55)"></div>'
                    + tx(bx - 20, base - h - 34, 150, str(val), 22, col, 'k', 'center')
                    + tx(bx - 20, base + 8, 150, nm, 15, '#8fa8c4', 'mono', 'center'))
        out += tx(gx + 270, 120, 140, delta, 44, CY, 'h')
        out += tx(gx, 64, 400, lab, 22, '#e8eef6', 't')
    out += f'<div class="abs" style="left:40px;top:{base}px;width:832px;height:2px;background:#23415f"></div>'
    return out


def v_dmaic():
    steps = [('D', 'Definir', 'Qué medir, con el mismo criterio en los 2 turnos'),
             ('M', 'Medir', 'VSM del estado actual y toma de tiempos en la línea'),
             ('A', 'Analizar', 'La causa se busca en el proceso, no en la persona'),
             ('I', 'Mejorar', 'Trabajo estándar y estaciones con 5S'),
             ('C', 'Controlar', 'KPI por turno y 4 operadores capacitados')]
    body = '<line x1="96" y1="130" x2="816" y2="130" stroke="#22b5cf" stroke-width="3" stroke-dasharray="2 10" stroke-linecap="round"/>'
    out = vpanel()
    for i, (l, n, d) in enumerate(steps):
        cx = 96 + i * 180
        col = CY if i < 4 else GRN
        body += f'<circle cx="{cx}" cy="130" r="58" fill="#04101f" stroke="{col}" stroke-width="4"/>'
        out += tx(cx - 58, 92, 116, l, 58, col, 'h', 'center', 76)
        out += tx(cx - 86, 208, 172, n, 24, '#e8eef6', 't', 'center')
        out += tx(cx - 84, 250, 168, d, 18, '#c6d4e4', 'p', 'center', 25)
    return vpanel() + svg(body) + out[len(vpanel()):]


def v_vsm():
    out = vpanel() + tx(30, 22, 600, 'Mapa de flujo de valor · 4 estaciones', 15, '#8fa8c4', 'mono')
    body = ''
    est = [('E1', '57 s', '6,4'), ('E2', '60 s', '6,8'), ('E3', '54 s', '0,7'), ('Insp.', '48 s', '0,5')]
    for i, (n, ct, inv) in enumerate(est):
        x = 110 + i * 200
        body += f'<path d="M{x - 52} 82 L{x - 30} 118 H{x - 74} Z" fill="none" stroke="{OR}" stroke-width="3" stroke-linejoin="round"/>'
        out += tx(x - 82, 124, 60, inv, 17, OR, 'k', 'center')
        out += (f'<div class="abs" style="left:{x}px;top:62px;width:140px;height:96px;border:2px solid #23415f;border-radius:10px;background:#04101f"></div>'
                + tx(x, 72, 140, n, 28, '#e8eef6', 't', 'center') + tx(x, 112, 140, 'C/T ' + ct, 17, '#8fa8c4', 'k', 'center'))
    pts, x = [], 40
    for i in range(4):
        pts += [f'{x},214', f'{x + 110},214', f'{x + 110},190', f'{x + 160},190', f'{x + 160},214']
        x += 200
    body += f'<polyline points="{" ".join(pts)} 872,214" fill="none" stroke="{CY}" stroke-width="3"/>'
    # dona 13 %
    import math
    c = 2 * math.pi * 66
    body += (f'<circle cx="760" cy="340" r="66" fill="none" stroke="#15304d" stroke-width="20"/>'
             f'<circle cx="760" cy="340" r="66" fill="none" stroke="{CY}" stroke-width="20" stroke-dasharray="{c * 0.13:.1f} {c:.1f}" transform="rotate(-90 760 340)"/>')
    out += tx(700, 318, 120, '13 %', 30, CY, 'h', 'center')
    out += (tx(40, 262, 300, 'Entrega', 16, '#8fa8c4', 'mono') + tx(40, 292, 300, '29 min', 60, '#e8eef6', 'h')
            + tx(340, 262, 320, 'Valor agregado', 16, '#8fa8c4', 'mono') + tx(340, 292, 320, '3,7 min', 60, CY, 'h')
            + tx(40, 380, 600, 'El resto es espera e inventario entre estaciones.', 20, '#c6d4e4'))
    return vpanel() + svg(body) + out[len(vpanel()):]


def v_contable():
    import math
    hub = (456, 236)
    nodes = ['Clientes', 'Productos', 'Componentes', 'Kits y despiece', 'Ventas', 'Compras y gastos', 'Anticipos']
    body, out = '', ''
    pos = []
    for i, n in enumerate(nodes):
        a = -math.pi / 2 + (i + 0.5) * 2 * math.pi / len(nodes)
        x, y = hub[0] + 340 * math.cos(a), hub[1] + 168 * math.sin(a)
        pos.append((x, y, n))
        body += f'<line x1="{hub[0]}" y1="{hub[1]}" x2="{x:.0f}" y2="{y:.0f}" stroke="#22b5cf" stroke-opacity=".55" stroke-width="2.5"/>'
    body += f'<circle cx="{hub[0]}" cy="{hub[1]}" r="92" fill="#08243a" stroke="{CY}" stroke-width="4"/>'
    for x, y, n in pos:
        out += (f'<div class="abs" style="left:{x - 98:.0f}px;top:{y - 25:.0f}px;width:196px;height:50px;border-radius:25px;background:#0d3350;border:2px solid #23415f"></div>'
                + tx(round(x - 98), round(y - 25), 196, n, 19, '#e8eef6', 'p', 'center', 50))
    out += tx(hub[0] - 90, hub[1] - 34, 180, 'Tablero', 30, CY, 'h', 'center')
    out += tx(hub[0] - 90, hub[1] + 6, 180, 'se recalcula solo', 16, '#c6d4e4', 'p', 'center')
    out += tx(24, 20, 400, '1 archivo · 11 hojas · macros', 15, '#8fa8c4', 'mono')
    return vpanel() + svg(body) + out


def v_charms():
    out = vpanel()
    steps = ['Catálogo con fotos reales', 'Cotizador en 4 pasos', 'El precio se calcula al elegir', 'El pedido sale a WhatsApp']
    body = ''
    for i, st in enumerate(steps):
        y = 44 + i * 100
        body += (f'<circle cx="64" cy="{y + 32}" r="26" fill="#04101f" stroke="{CY if i < 3 else GRN}" stroke-width="3"/>'
                 + (f'<line x1="64" y1="{y + 58}" x2="64" y2="{y + 106}" stroke="#23415f" stroke-width="3"/>' if i < 3 else ''))
        out += tx(38, y + 14, 52, str(i + 1), 24, CY if i < 3 else GRN, 'h', 'center', 36)
        out += tx(112, y + 16, 380, st, 25, '#e8eef6', 't')
    # teléfono
    px, py = 590, 22
    out += (f'<div class="abs" style="left:{px}px;top:{py}px;width:260px;height:416px;border-radius:34px;border:3px solid #3a5878;background:#0b141a"></div>'
            f'<div class="abs" style="left:{px + 3}px;top:{py + 3}px;width:254px;height:62px;border-radius:31px 31px 0 0;background:#1f2c34"></div>'
            f'<div class="abs" style="left:{px + 20}px;top:{py + 16}px;width:34px;height:34px;border-radius:17px;background:#e8a6b8"></div>'
            + tx(px + 66, py + 14, 180, 'Charms Ecuador', 17, '#e9edef', 't') + tx(px + 66, py + 36, 180, 'WhatsApp', 13, '#8696a0', 'p')
            + f'<div class="abs" style="left:{px + 40}px;top:{py + 110}px;width:200px;height:200px;border-radius:14px 2px 14px 14px;background:#005c4b"></div>'
            + tx(px + 56, py + 124, 176, 'Hola, quiero hacer este pedido:', 16, '#e9edef', 'p', 'left', 22)
            + ''.join(tx(px + 56, py + 178 + j * 30, 176, '✓ ' + t, 17, '#e9edef', 'p') for j, t in enumerate(['Pieza', 'Detalles', 'Precio estimado']))
            + tx(px + 150, py + 284, 80, '✓✓', 13, '#53bdeb', 'p', 'right')
            + f'<div class="abs" style="left:{px + 16}px;top:{py + 352}px;width:228px;height:44px;border-radius:22px;background:#1f2c34"></div>'
            + tx(px + 16, py + 352, 228, 'Mensaje ya escrito', 13, GRN, 'mono', 'center', 44))
    return vpanel() + svg(body) + out[len(vpanel()):]


def v_anatris():
    import math
    cx, cy, r = 250, 330, 200
    body = f'<path d="M{cx - r} {cy} A{r} {r} 0 0 1 {cx + r} {cy}" fill="none" stroke="#23415f" stroke-width="3"/>'
    ang = 120
    a = math.radians(180 - ang)
    ex, ey = cx + r * math.cos(a), cy - r * math.sin(a)
    body += f'<path d="M{cx} {cy} L{cx - r} {cy} A{r} {r} 0 0 1 {ex:.1f} {ey:.1f} Z" fill="{CY}" fill-opacity=".14" stroke="none"/>'
    for d in range(0, 181, 15):
        t = math.radians(180 - d)
        l = 18 if d % 45 == 0 else 9
        body += f'<line x1="{cx + r * math.cos(t):.1f}" y1="{cy - r * math.sin(t):.1f}" x2="{cx + (r - l) * math.cos(t):.1f}" y2="{cy - (r - l) * math.sin(t):.1f}" stroke="#8fa8c4" stroke-width="2"/>'
    body += (f'<line x1="{cx}" y1="{cy}" x2="{cx - r}" y2="{cy}" stroke="#3d5a7a" stroke-width="5" stroke-linecap="round"/>'
             f'<line x1="{cx}" y1="{cy}" x2="{ex:.1f}" y2="{ey:.1f}" stroke="{CY}" stroke-width="7" stroke-linecap="round"/>'
             f'<circle cx="{cx}" cy="{cy}" r="14" fill="#04101f" stroke="{CY}" stroke-width="4"/>')
    out = (tx(30, 22, 400, 'Rango de movimiento · ejemplo', 15, '#8fa8c4', 'mono')
           + tx(cx - 150, cy - 110, 120, f'{ang}°', 40, CY, 'h', 'center')
           + tx(cx - r - 30, cy + 14, 60, '0°', 15, '#8fa8c4', 'k', 'center') + tx(cx + r - 30, cy + 14, 60, '180°', 15, '#8fa8c4', 'k', 'center')
           + tx(30, 392, 440, 'Abducción del hombro', 22, '#e8eef6', 't'))
    lvl = ['Cuerpo completo en 3D', 'Región clínica', 'Músculo por músculo', 'Ficha con su fuente citada']
    for i, l in enumerate(lvl):
        y = 52 + i * 96
        body += f'<line x1="560" y1="{y + 58}" x2="560" y2="{y + 96}" stroke="#23415f" stroke-width="3"/>' if i < 3 else ''
        out += (f'<div class="abs" style="left:{520 + i * 16}px;top:{y}px;width:{340 - i * 16}px;height:58px;border-radius:12px;'
                f'border:2px solid {CY if i == 3 else "#23415f"};background:{"#08243a" if i == 3 else "#04101f"}"></div>'
                + tx(540 + i * 16, y, 310 - i * 16, l, 20, CY if i == 3 else '#e8eef6', 'p', 'left', 58))
    return vpanel() + svg(body) + out


def v_audit():
    import math
    cx, cy, r = 220, 300, 160
    c = math.pi * r
    body = (f'<path d="M{cx - r} {cy} A{r} {r} 0 0 1 {cx + r} {cy}" fill="none" stroke="#15304d" stroke-width="30" stroke-linecap="round"/>'
            f'<path d="M{cx - r} {cy} A{r} {r} 0 0 1 {cx + r} {cy}" fill="none" stroke="{OR}" stroke-width="30" stroke-linecap="round" stroke-dasharray="{c * 0.33:.1f} {c:.1f}"/>')
    out = (tx(30, 22, 400, 'Informe BPM · planta de ejemplo', 15, '#8fa8c4', 'mono')
           + tx(cx - 120, cy - 82, 240, '33 %', 64, OR, 'h', 'center') + tx(cx - 120, cy - 10, 240, 'Preparación · no lista', 18, '#c6d4e4', 'p', 'center')
           + tx(60, 360, 340, 'Hoy', 18, OR, 'mono', 'center') )
    for i, (n, l, col) in enumerate([('1', 'Crítico', RED), ('1', 'Mayor', OR), ('2', 'Menor', YEL)]):
        x = 480 + i * 140
        out += (f'<div class="abs" style="left:{x}px;top:60px;width:120px;height:120px;border-radius:16px;border:2px solid {col};background:{col}18"></div>'
                + tx(x, 70, 120, n, 56, col, 'h', 'center', 64) + tx(x, 140, 120, l, 16, col, 'mono', 'center'))
    out += tx(480, 214, 400, 'CAPA', 16, '#8fa8c4', 'mono')
    out += (f'<div class="abs" style="left:480px;top:244px;width:{9 * 40}px;height:30px;border-radius:6px;background:{OR}"></div>'
            + tx(480, 244, 360, '9 abiertas', 17, '#04101f', 'k', 'left', 30, ';padding-left:12px')
            + f'<div class="abs" style="left:480px;top:284px;width:{4 * 40}px;height:30px;border-radius:6px;background:{GRN}"></div>'
            + tx(480, 284, 160, '4 cerradas', 17, '#04101f', 'k', 'left', 30, ';padding-left:12px')
            + tx(480, 340, 400, 'Con BOUW', 16, CY, 'mono')
            + tx(480, 368, 400, 'La lista en verde y el lote liberado.', 22, '#e8eef6', 't', 'left', 28))
    return vpanel() + svg(body) + out


def v_planta():
    """Plano de planta con 6 puntos de desperdicio (el juego del sitio, dibujado)."""
    out = vpanel()
    body = '<rect x="30" y="30" width="852" height="400" rx="10" fill="none" stroke="#23415f" stroke-width="3"/>'
    body += '<path d="M30 230 H882" stroke="#15304d" stroke-width="40"/>'
    for (x, y, w, h, n) in [(70, 60, 170, 120, 'Corte'), (290, 60, 170, 120, 'Ensamble'), (510, 60, 150, 120, 'Pintura'), (710, 60, 140, 120, 'Empaque'),
                            (70, 290, 220, 110, 'Almacén MP'), (350, 290, 180, 110, 'Inspección'), (600, 290, 250, 110, 'Producto terminado')]:
        body += f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="#0b2036" stroke="#3a5878" stroke-width="2"/>'
        out += tx(x, y + h / 2 - 12, w, n, 17, '#8fa8c4', 'mono', 'center')
    body += '<path d="M150 180 C 200 260, 600 200, 680 290 M380 180 C 420 250, 140 230, 170 290" fill="none" stroke="#f79b4a" stroke-width="2.5" stroke-dasharray="6 6"/>'
    for i, (x, y) in enumerate([(200, 150), (460, 230), (585, 200), (300, 330), (520, 360), (820, 240)]):
        body += (f'<circle cx="{x}" cy="{y}" r="26" fill="{OR}" fill-opacity=".22"/>'
                 f'<circle cx="{x}" cy="{y}" r="15" fill="{OR}"/>')
        out += tx(x - 15, y - 15, 30, str(i + 1), 17, '#04101f', 'h', 'center', 30)
    return vpanel() + svg(body) + out[len(vpanel()):]


def v_firmas():
    out = vpanel() + tx(30, 26, 400, 'Hoy · en serie', 16, OR, 'mono')
    body = ''
    for i in range(4):
        x = 40 + i * 190
        out += box(x, 66, 150, 64, f'Firma {i + 1}', OR, '#e8eef6', 20)
        if i < 3:
            body += f'<line x1="{x + 150}" y1="98" x2="{x + 190}" y2="98" stroke="{OR}" stroke-width="3"/>'
    out += box(800, 66, 80, 64, '⏳', RED, RED, 26)
    out += tx(40, 146, 820, 'El lote espera a que aparezca cada papel, uno tras otro.', 20, '#c6d4e4')
    out += tx(30, 214, 400, 'Con BOUW · en paralelo', 16, CY, 'mono')
    for i in range(3):
        y = 250 + i * 64
        out += box(40, y, 300, 50, f'Revisión {i + 1} · 1 firma', CY, '#e8eef6', 18)
        body += f'<path d="M340 {y + 25} C 420 {y + 25}, 420 316, 500 316" fill="none" stroke="{CY}" stroke-width="3"/>'
    out += box(500, 284, 360, 64, '✓ Lote liberado', GRN, GRN, 24)
    return vpanel() + svg(body) + out[len(vpanel()):]


# =====================================================================
# 1. PERFIL Y PORTADAS
# =====================================================================

# 01 · Logo de la página de empresa 400×400: el dragón 3D del sitio (LinkedIn lo muestra cuadrado; en el celular, a 48 px)
add('01-perfil-dragon-400x400', 400, 400,
    '<div class="abs" style="left:0;top:0;width:400px;height:400px;background:radial-gradient(circle at 50% 46%,#0d2a44 0%,#04101f 70%)"></div>'
    + hero(20, 70, 360, 0.45), step=40)

# 02 · Variante: el dragón sobre las letras BOUW en 3D (como en la portada del sitio)
add('02-perfil-logo-completo-400x400', 400, 400,
    '<div class="abs" style="left:0;top:0;width:400px;height:400px;background:radial-gradient(circle at 50% 46%,#0d2a44 0%,#04101f 70%)"></div>'
    + glow(200, 190, 190, 0.35) + logo(28, 96, 344)
    + '<div class="abs mono" style="left:0;top:296px;width:400px;text-align:center;font-size:12px;line-height:18px;letter-spacing:0.28em">Automation &amp; Digital</div>',
    step=40)

# 05 · Foto de perfil 720×720 (Facebook, Instagram, WhatsApp; se ve en círculo)
add('05-perfil-dragon-720x720', 720, 720,
    '<div class="abs" style="left:0;top:0;width:720px;height:720px;background:radial-gradient(circle at 50% 46%,#0d2a44 0%,#04101f 70%)"></div>'
    + hero(70, 130, 580, 0.45))
add('06-perfil-logo-completo-720x720', 720, 720,
    '<div class="abs" style="left:0;top:0;width:720px;height:720px;background:radial-gradient(circle at 50% 46%,#0d2a44 0%,#04101f 70%)"></div>'
    + glow(360, 330, 330, 0.35) + logo(70, 186, 580)
    + '<div class="abs mono" style="left:0;top:520px;width:720px;text-align:center;font-size:20px;line-height:28px;letter-spacing:0.3em">Automation &amp; Digital</div>')

# 03 · Portada de la página de empresa 1128×191 (el logo de la página tapa abajo a la izquierda: el texto empieza en x=300)
add('03-portada-empresa-1128x191', 1128, 191,
    '<div class="abs mono" style="left:300px;top:34px;width:520px;font-size:12px;line-height:18px;color:#4fd6e8">Quito · Monterrey &#8212; Est. 7+</div>'
    + f'<div class="abs serif" style="left:300px;top:60px;width:560px;font-size:50px;line-height:58px">{LEMA}</div>'
    + '<div class="abs mono" style="left:300px;top:136px;width:560px;font-size:11px;line-height:18px">Ingeniería de procesos, calidad y automatización</div>'
    + glow(970, 96, 160, 0.45) + logo(836, 24, 268),
    step=30)

# 04 · Banner del perfil personal 1584×396 (la foto tapa la parte izquierda: el contenido empieza en x=560)
SERV = ['Lean &amp; planta', 'Calidad &amp; BPM', 'Automatización', 'Simulación', 'Web &amp; producto']
chips = ''
x = 560
for s_ in SERV:
    w = int(len(html.unescape(s_)) * 10.6 + 44)
    chips += f'<div class="chip" style="left:{x}px;top:316px;width:{w}px;height:40px;font-size:15px;line-height:36px">{s_}</div>'
    x += w + 12
add('04-banner-perfil-personal-1584x396', 1584, 396,
    '<div class="abs mono" style="left:560px;top:52px;width:500px;font-size:14px;line-height:20px;color:#4fd6e8">Quito · Monterrey &#8212; Est. 7+</div>'
    + '<div class="abs h" style="left:560px;top:96px;width:640px;font-size:62px;line-height:66px">'
      '<span class="dim">Del dis</span>eño <span class="dim">a la rea</span><span class="c">lidad</span></div>'
    + f'<div class="abs serif" style="left:560px;top:198px;width:700px;font-size:58px;line-height:64px">{LEMA}</div>'
    + chips
    + glow(1400, 160, 220, 0.4) + logo(1236, 44, 320)
    + '<div class="abs mono" style="left:1236px;top:226px;width:320px;text-align:center;font-size:12px;line-height:20px;letter-spacing:0.24em">Automation &amp; Digital Solutions</div>')

# =====================================================================
# 2. PUBLICACIONES 1080×1350
# =====================================================================
W, H, M = 1080, 1350, 84
IW = W - 2 * M


def header(n, tema, raw=False):
    return (logo(M, 50, 190)
            + f'<div class="abs mono" style="left:{W - M - 640}px;top:84px;width:640px;text-align:right;font-size:21px;line-height:28px">'
              f'{e(tema)}</div>'
            + f'<div class="rule" style="left:{M}px;top:156px;width:{IW}px"></div>')


def footer(phrase, cta, serif=False):
    cw = int(len(cta) * 15.5 + 60)
    cls = 'serif' if serif else 'p'
    fs = 'font-size:36px;line-height:40px;color:#e8eef6' if serif else 'font-size:24px;line-height:32px;color:#93a7bf'
    return (f'<div class="rule" style="left:{M}px;top:1170px;width:{IW}px"></div>'
            + f'<div class="abs {cls}" style="left:{M}px;top:1206px;width:{IW - cw - 36}px;{fs}">{phrase}</div>'
            + f'<div class="abs t" style="left:{W - M - cw}px;top:1204px;width:{cw}px;text-align:right;font-size:28px;line-height:36px;font-weight:700;color:#4fd6e8">{e(cta)}&nbsp;→</div>'
            + f'<div class="abs mono" style="left:{M}px;top:1290px;width:{IW}px;font-size:18px;line-height:26px;color:#6f88a3;letter-spacing:.14em">bouw-eight.vercel.app · WhatsApp +593 96 368 4012</div>')


def kicker(t, top=206, color='#4fd6e8'):
    return (f'<div class="abs" style="left:{M}px;top:{top + 10}px;width:12px;height:12px;border-radius:6px;background:{color}"></div>'
            f'<div class="abs mono" style="left:{M + 26}px;top:{top}px;width:{IW - 26}px;font-size:21px;line-height:32px;color:{color}">{t}</div>')


def title(t, size, top=256, width=IW):
    return f'<div class="abs h" style="left:{M}px;top:{top}px;width:{width}px;font-size:{size}px">{t}</div>'


def para(t, top, size=30, lh=42, color='#c6d4e4', width=IW, left=M):
    return f'<div class="abs p" style="left:{left}px;top:{top}px;width:{width}px;font-size:{size}px;line-height:{lh}px;color:{color}">{t}</div>'


def stats(rows, top, num=84, color='#4fd6e8'):
    out = f'<div class="rule" style="left:{M}px;top:{top}px;width:{IW}px"></div>'
    cw = IW // len(rows)
    for i, (n, l) in enumerate(rows):
        x = M + i * cw
        out += (f'<div class="abs h" style="left:{x}px;top:{top + 30}px;width:{cw - 20}px;font-size:{num}px;line-height:{num}px;color:{color}">{n}</div>'
                f'<div class="abs p" style="left:{x}px;top:{top + 40 + num}px;width:{cw - 30}px;font-size:23px;line-height:31px;color:#93a7bf">{l}</div>')
    return out


def hoy_bouw(hoy, con, top, h=230):
    half = (IW - 24) // 2
    out = ''
    for i, (lab, txt, col) in enumerate([('Hoy', hoy, '#f79b4a'), ('Con BOUW', con, '#4fd6e8')]):
        x = M + i * (half + 24)
        out += (f'<div class="panel" style="left:{x}px;top:{top}px;width:{half}px;height:{h}px"></div>'
                f'<div class="abs" style="left:{x + 30}px;top:{top + 38}px;width:12px;height:12px;border-radius:6px;background:{col}"></div>'
                f'<div class="abs mono" style="left:{x + 52}px;top:{top + 28}px;width:{half - 80}px;font-size:18px;line-height:30px;color:{col}">{lab}</div>'
                f'<div class="abs p" style="left:{x + 30}px;top:{top + 78}px;width:{half - 60}px;font-size:24px;line-height:33px;color:#e8eef6">{e(txt)}</div>')
    return out


def chip_row(items, top, size=20, gap=12, h=48):
    out, x, y = '', M, top
    for it in items:
        w = int(len(it) * size * 0.62 + 44)
        if x + w > W - M:
            x, y = M, y + h + gap
        out += f'<div class="chip" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;font-size:{size}px;line-height:{h - 4}px">{e(it)}</div>'
        x += w + gap
    return out


def post(name, body):
    add(name, W, H, body)


# L01 · Presentación (la portada del sitio)
post('L01-presentacion',
     f'<div class="abs mono" style="left:{M}px;top:84px;width:300px;font-size:19px;line-height:28px;color:#4fd6e8">Quito · Monterrey</div>'
     + dash(M, 124, 150)
     + f'<div class="abs mono" style="left:{M}px;top:140px;width:300px;font-size:19px;line-height:28px">Est. 7+</div>'
     + f'<div class="abs mono" style="left:{W - M - 400}px;top:84px;width:400px;text-align:right;font-size:21px;line-height:30px">Quiénes somos</div>'
     + hero(150, 150, 840, 0.5)
     + title('<span class="dim">Del dis</span>eño<br><span class="dim">a la rea</span><span class="c">lidad</span>', 112, top=760)
     + f'<div class="abs serif" style="left:{M}px;top:990px;width:{IW}px;font-size:64px;line-height:70px">{LEMA}</div>'
     + para('Automatizamos procesos y convertimos ideas de ingeniería en productos que funcionan. 7+ años entre Ecuador y México.', 1076, size=26, lh=36)
     + footer('Nueve horas al día en común: siempre hay alguien para responderte.', 'Hablemos'))


# L02 · Servicio: Lean manufacturing & ingeniería de planta
post('L02-lean-ingenieria-de-planta',
     header(2, 'Servicios')
     + kicker('Lean manufacturing &amp; ingeniería de planta')
     + title('Elimina cuellos de botella y maximiza cada metro cuadrado de tu planta.', 66)
     + para('Convertimos operaciones lentas y congestionadas en flujos de producción esbeltos, ágiles y altamente rentables.', 498, size=29, lh=40)
     + stats([('−15 %', 'Tiempo de preparación'), ('−20 %', 'Reprocesos'), ('4', 'Operadores capacitados, con estándar y control en piso')], 620)
     + f'<div class="abs mono" style="left:{M}px;top:866px;width:{IW}px;font-size:16px;line-height:24px;color:#5d7690">Medido en el caso de mejora continua</div>'
     + hoy_bouw('Recorridos que se cruzan, piezas apiladas en los pasillos y una máquina que frena a todas.',
                'Un solo flujo, cada cosa en su sitio y el mapa de valor con su tablero vigilando la línea.', 918, 222)
     + footer('Agenda una evaluación técnica de tus procesos.', 'Optimiza tu línea'))

# L03 · Servicio: Cumplimiento normativo & BPM
post('L03-cumplimiento-normativo-bpm',
     header(3, 'Servicios')
     + kicker('Cumplimiento normativo &amp; BPM')
     + title('Pasa cualquier auditoría a la primera y elimina el riesgo operativo en tu planta.', 66)
     + para('Transformamos la documentación dispersa en un sistema de calidad sólido, trazable y 100 % preparado '
            'para inspecciones de autoridades o clientes.', 498, size=29, lh=40)
     + f'<div class="abs mono" style="left:{M}px;top:640px;width:{IW}px;font-size:17px;line-height:24px">Lo hacemos</div>'
     + chip_row(['BPM', 'ISO', 'CAPA', 'Trazabilidad', 'Batch records', '8D', 'Causa raíz', 'Auditorías internas',
                 'Gap analysis', 'Integridad de datos', 'Liberación de lotes'], 680, size=19)
     + hoy_bouw('Papeles sueltos, archivadores desbordados, la alarma encendida y un lote retenido.',
                'Expedientes en orden, la trazabilidad en pantalla, la lista en verde y el lote liberado.', 900, 236)
     + footer('Prepara tu planta antes de tu próxima inspección.', 'Diagnóstico gratis'))

# L04 · Proyecto: Programa contable (ERP sobre Excel)
post('L04-programa-contable-excel',
     header(4, 'Proyectos')
     + kicker('Proyecto real · Automatización · Gestión')
     + title('Un ERP pequeño montado sobre Excel: inventario, kits, ventas y caja en un solo archivo.', 62)
     + para('Once hojas conectadas por macros: clientes, productos, componentes, kits con su despiece, ventas, compras y gastos, '
            'anticipos y un tablero que se recalcula solo. El equipo siguió trabajando en la herramienta que ya sabía usar.', 520, size=27, lh=38)
     + stats([('11', 'Hojas conectadas'), ('1', 'Archivo, cero licencias'), ('0', 'Migraciones de sistema')], 718, num=96)
     + f'<div class="panel" style="left:{M}px;top:918px;width:{IW}px;height:200px"></div>'
     + f'<div class="abs" style="left:{M}px;top:918px;width:6px;height:200px;background:#22b5cf;border-radius:3px"></div>'
     + f'<div class="abs mono" style="left:{M + 40}px;top:948px;width:300px;font-size:17px;line-height:24px;color:#4fd6e8">Resultado</div>'
     + para('El cierre mensual dejó de ser un armado manual: se genera desde los movimientos ya capturados.',
            988, size=30, lh=42, color='#e8eef6', width=IW - 80, left=M + 40)
     + footer('Excel · VBA · Inventario · Kits / BOM · Dashboard', 'Hablemos'))

# L05 · Proyecto: Simulación de flujos (el mapa de flujo de valor del sitio, redibujado)
vsm = ''
est = [('E1', '57 s'), ('E2', '60 s'), ('E3', '54 s'), ('Insp.', '48 s')]
inv = ['6,4', '6,8', '0,7', '0,5']
bx, bw, gap = M, 170, 78
for i, (n, ct) in enumerate(est):
    x = M + 58 + i * 228
    ix = x - 52
    vsm += (f'<svg class="abs" style="left:{ix}px;top:796px" width="44" height="40" viewBox="0 0 44 40" xmlns="http://www.w3.org/2000/svg">'
            f'<path d="M22 3 L41 37 H3 Z" fill="none" stroke="#f79b4a" stroke-width="3" stroke-linejoin="round"/></svg>'
            f'<div class="abs k" style="left:{ix - 10}px;top:842px;width:64px;text-align:center;font-size:19px;line-height:26px;color:#f79b4a">{inv[i]}</div>'
            f'<div class="panel" style="left:{x}px;top:770px;width:{bw}px;height:116px;border-radius:10px"></div>'
            f'<div class="abs t" style="left:{x}px;top:790px;width:{bw}px;text-align:center;font-size:30px;line-height:36px">{n}</div>'
            f'<div class="abs k" style="left:{x}px;top:836px;width:{bw}px;text-align:center;font-size:19px;line-height:26px;color:#8fa8c4">C/T {ct}</div>')
# línea de tiempo (escalones del VSM)
pts, x = [], M
for i in range(4):
    pts += [f'{x},40', f'{x + 120},40', f'{x + 120},8', f'{x + 160},8', f'{x + 160},40']
    x += 230
vsm += (f'<svg class="abs" style="left:0;top:918px" width="{W}" height="50" viewBox="0 0 {W} 50" xmlns="http://www.w3.org/2000/svg">'
        f'<polyline points="{" ".join(pts)} {W - M},40" fill="none" stroke="#4fd6e8" stroke-width="3"/></svg>')
vsm += (f'<div class="abs mono" style="left:{M}px;top:992px;width:200px;font-size:17px;line-height:26px">Entrega</div>'
        f'<div class="abs h" style="left:{M}px;top:1024px;width:300px;font-size:64px;line-height:68px">29 min</div>'
        f'<div class="abs mono" style="left:{M + 380}px;top:992px;width:500px;font-size:17px;line-height:26px">Valor agregado</div>'
        f'<div class="abs h" style="left:{M + 380}px;top:1024px;width:560px;font-size:64px;line-height:68px;color:#4fd6e8">3,7 min '
        f'<span style="font-size:34px;color:#8fa8c4">(13 %)</span></div>')
post('L05-simulacion-de-flujos',
     header(5, 'Proyectos')
     + kicker('Proyecto · Simulación de la línea')
     + title('Simulación de flujos &amp; visión analítica.', 70)
     + para('Con los datos de tu operación armamos un modelo de la línea y probamos ahí cada cambio de layout o de proceso. '
            'Sabes cuánto mejora el flujo antes de mover un solo equipo, sin parar la producción para hacer pruebas.', 430, size=28, lh=39)
     + f'<div class="abs mono" style="left:{M}px;top:700px;width:{IW}px;font-size:16px;line-height:24px">Mapa de flujo de valor · línea de 4 estaciones · hoy</div>'
     + vsm
     + footer('Sabes cuánto mejora antes de mover un solo equipo.', 'Probar la simulación'))

# L06 · ¿Cuál te suena? (las 9 frases del sitio)
FRASES = ['El cierre de mes lo arma alguien a mano, juntando archivos.',
          'No sé cuánto tarda de verdad una pieza en salir.',
          'Repetimos trabajo por errores que se detectan tarde.',
          'La misma información vive en tres archivos y ninguno cuadra.',
          'Tenemos una auditoría o una certificación encima.',
          'Hay un diseño que funciona en pantalla y no sabemos fabricarlo.',
          'Cada persona hace la misma tarea a su manera.',
          'Alguien pasa horas cada semana copiando datos de un sitio a otro.',
          'Queremos enseñar el producto antes de tenerlo fabricado.']
fr = ''
for i, f in enumerate(FRASES):
    y = 452 + i * 76
    fr += (f'<div class="abs" style="left:{M}px;top:{y + 14}px;width:34px;height:34px;border:2px solid #4fd6e8;border-radius:6px"></div>'
           f'<div class="abs p" style="left:{M + 58}px;top:{y + 10}px;width:{IW - 58}px;font-size:26px;line-height:40px;color:#e8eef6">{e(f)}</div>'
           + (f'<div class="rule" style="left:{M + 58}px;top:{y + 70}px;width:{IW - 58}px"></div>' if i < 8 else ''))
post('L06-cual-te-suena',
     header(6, 'Qué te pasa')
     + title('¿Cuál te suena?', 92, top=214)
     + para('Son frases que nos dicen los clientes cuando nos llaman. ¿Cuál dices tú? Cuéntanos en los comentarios.', 322, size=28, lh=40)
     + fr
     + footer('¿Ninguna? Puede que todavía no nos necesites, y preferimos decírtelo.', 'Cuéntanos'))

# L07 · En qué condiciones
COND = [('Diagnóstico primero', '1 a 2 semanas', 'Medimos tu proceso real antes de proponer nada. Si al final no hay proyecto, la medición se queda contigo igual.'),
        ('Precio cerrado', '3 a 5 días', 'Alcance, entregables, plazo y precio por escrito antes de construir.'),
        ('Entrega cada semana', '4 a 10 semanas', 'Cada semana te enseñamos algo que ya funciona, para corregir el rumbo cuando todavía cuesta poco.'),
        ('Acompañamiento', '30 días', 'Después de entregar seguimos disponibles mientras el proceso se estabiliza, sin contrato nuevo.')]
cond = ''
for i, (n, pl, d) in enumerate(COND):
    y = 432 + i * 180
    cond += (f'<div class="rule" style="left:{M}px;top:{y}px;width:{IW}px"></div>'
             f'<div class="abs k" style="left:{M}px;top:{y + 30}px;width:60px;font-size:22px;line-height:34px">0{i + 1}</div>'
             f'<div class="abs t" style="left:{M + 70}px;top:{y + 26}px;width:520px;font-size:36px;line-height:42px">{e(n)}</div>'
             f'<div class="abs k" style="left:{W - M - 300}px;top:{y + 32}px;width:300px;text-align:right;font-size:22px;line-height:34px;color:#f79b4a">{e(pl)}</div>'
             f'<div class="abs p" style="left:{M + 70}px;top:{y + 82}px;width:{IW - 70}px;font-size:24px;line-height:33px">{e(d)}</div>')
post('L07-en-que-condiciones',
     header(7, 'Cómo trabajamos')
     + title('En qué condiciones.', 92, top=214)
     + para('Dos sedes, un mismo estándar.', 330, size=30, lh=40, color='#4fd6e8')
     + cond
     + footer('Si algo no se puede prometer, lo decimos desde el principio.', 'Hablemos'))

# L08 · La cuenta (la calculadora del sitio, con su ejemplo y su veredicto)
calc = f'<div class="panel" style="left:{M}px;top:496px;width:{IW}px;height:384px"></div>'
rows = [('Veces por semana', '3'), ('Minutos cada vez', '× 20'), ('Personas que intervienen', '× 1'), ('Semanas trabajadas al año', '× 48')]
for i, (l, v) in enumerate(rows):
    y = 496 + i * 76
    calc += (f'<div class="abs p" style="left:{M + 34}px;top:{y + 20}px;width:600px;font-size:27px;line-height:38px">{e(l)}</div>'
             f'<div class="abs k" style="left:{W - M - 334}px;top:{y + 20}px;width:300px;text-align:right;font-size:30px;line-height:38px">{e(v)}</div>'
             f'<div class="rule" style="left:{M + 2}px;top:{y + 75}px;width:{IW - 4}px"></div>')
calc += (f'<div class="abs" style="left:{M + 2}px;top:802px;width:{IW - 4}px;height:76px;background:#0d2b48;border-radius:0 0 16px 16px"></div>'
         f'<div class="abs mono" style="left:{M + 34}px;top:828px;width:300px;font-size:19px;line-height:26px;color:#c6d4e4">Al año</div>'
         f'<div class="abs h" style="left:{W - M - 434}px;top:808px;width:400px;text-align:right;font-size:58px;line-height:62px;color:#4fd6e8">48 horas</div>'
         f'<div class="abs mono" style="left:{M}px;top:918px;width:200px;font-size:17px;line-height:24px;color:#f79b4a">Veredicto</div>'
         f'<div class="abs t" style="left:{M}px;top:950px;width:{IW}px;font-size:42px;line-height:48px">Está en la frontera.</div>'
         + para('Entre 40 y 150 horas al año. Sale a cuenta si además te está costando errores, o si quien lo hace es justo '
                'la persona que menos debería estar haciéndolo. Si solo son las horas, espera.', 1010, size=24, lh=33))
post('L08-la-cuenta',
     header(8, 'La cuenta')
     + title('Cuánto cuesta hacerlo a mano.', 80, top=214)
     + para('Un ejemplo de la calculadora del sitio. Si no compensa automatizarla, también te lo dice.', 390, size=27, lh=37)
     + calc
     + footer('Haz tu cuenta en la calculadora del sitio.', 'Hacer la cuenta'))

# L09 · ¿Dónde pierde horas esta planta? (el juego del sitio)
post('L09-donde-pierde-horas',
     header(9, 'Reto · 30 segundos')
     + title('¿Dónde pierde horas esta planta?', 76, top=214)
     + para('Hay seis desperdicios escondidos. ¿Cuántos ves? En el sitio te decimos cuáles son, qué cuestan y cómo se ven arreglados.', 400, size=27, lh=37)
     + vis(v_planta(), M, 540, 1.0)
     + f'<div class="abs h" style="left:{W - M - 230}px;top:1090px;width:200px;text-align:right;font-size:56px;line-height:60px">¿?<span class="dim">/6</span></div>'
     + f'<div class="abs mono" style="left:{M}px;top:1110px;width:600px;font-size:19px;line-height:24px">Tu puntaje</div>'
     + footer('Comenta cuántos encontraste.', 'Juega en el sitio'))

# L10 · Contacto
post('L10-contacto',
     header(10, 'Último paso')
     + title('Cuéntanos qué proceso te está costando horas.', 84, top=214)
     + para('Y te respondemos con un plan concreto.', 482, size=34, lh=44, color='#4fd6e8')
     + ''.join(f'<div class="rule" style="left:{M}px;top:{y}px;width:{IW}px"></div>'
               f'<div class="abs mono" style="left:{M}px;top:{y + 34}px;width:300px;font-size:18px;line-height:26px">{a}</div>'
               f'<div class="abs t" style="left:{M + 300}px;top:{y + 26}px;width:{IW - 300}px;font-size:34px;line-height:42px">{b}</div>'
               for y, a, b in [(590, 'WhatsApp', '+593 96 368 4012'), (690, 'Correo', 'bouw.contacto@gmail.com'),
                               (790, 'Sedes', 'Quito, Ecuador · Monterrey, México'), (890, 'Respuesta', 'Menos de 24 horas hábiles')])
     + f'<div class="abs serif" style="left:{M}px;top:1010px;width:560px;font-size:60px;line-height:66px">{LEMA}</div>'
     + hero(650, 976, 280, 0.45)
     + footer('Escríbenos por correo o directo a WhatsApp.', 'Escríbenos por WhatsApp'))

# =====================================================================
# 3. CARRUSEL (documento PDF de LinkedIn) 1080×1350 · "Lo que hemos construido"
# =====================================================================
PROY = [
    ('01', 'Salud · Atlas 3D', 'Anatris', 'Atlas 3D de anatomía y biomecánica para fisioterapia, en el navegador.',
     'anatris-movimiento', [('6', 'Regiones clínicas'), ('113', 'Músculos con ficha'), ('79', 'Tests con sens/spec')],
     'En línea y en producción en anatris.vercel.app, con recorrido guiado y aviso legal antes de usarse.',
     'React · Three.js · WebGL · Supabase · PWA'),
    ('02', 'Hoy → BOUW', 'Simulación de flujos', 'Un modelo de tu línea para probar cada cambio de layout o de proceso antes de mover un solo equipo.',
     'lean-es-poster', [('29 min', 'Tiempo de entrega'), ('3,7 min', 'Valor agregado'), ('13 %', 'Del tiempo agrega valor')],
     'Sabes cuánto mejora el flujo sin parar la producción para hacer pruebas.',
     'Mapa de flujo de valor · línea de 4 estaciones'),
    ('03', 'Automatización · Gestión', 'Programa contable', 'Un ERP pequeño montado sobre Excel: inventario, kits, ventas y caja en un solo archivo.',
     'contable-excel-es-poster', [('11', 'Hojas conectadas'), ('1', 'Archivo, cero licencias'), ('0', 'Migraciones de sistema')],
     'El cierre mensual dejó de ser un armado manual: se genera desde los movimientos ya capturados.',
     'Excel · VBA · Inventario · Kits / BOM · Dashboard'),
    ('04', 'Web · Pedidos por WhatsApp', 'Charms Ecuador', 'Una web que recibe el pedido completo y lo lleva a WhatsApp ya escrito.',
     'charms', [('15', 'Modelos con foto real'), ('4', 'Pasos del cotizador'), ('$0', 'Costo de hosting')],
     'El cliente llega a WhatsApp con la pieza, los detalles y el precio estimado ya escritos.',
     'React · Three.js · Tailwind · WhatsApp · Vercel'),
    ('05', 'Hoy → BOUW', 'Informe de auditoría', 'La misma planta hoy y con BOUW: hallazgos del inspector, CAPA, lotes retenidos y el rastro de un lote hasta su materia prima.',
     'cumplimiento-es-poster', [('9', 'CAPA abiertas'), ('3', 'Lotes retenidos'), ('33 %', 'Preparación hoy')],
     'Expedientes en orden, la trazabilidad en pantalla, la lista en verde y el lote liberado.',
     'BPM · ISO · CAPA · Trazabilidad · Batch records'),
]
N = len(PROY) + 2
car = []
car.append(header(1, f'Carrusel · 1 / {N}', True)
           + kicker('Proyectos')
           + title('Lo que hemos<br>construido.', 116, top=262)
           + para('Lo que tienen en común: procesos que antes costaban horas.', 520, size=34, lh=46, color='#4fd6e8')
           + ''.join(f'<div class="rule" style="left:{M}px;top:{650 + i * 92}px;width:{IW}px"></div>'
                     f'<div class="abs k" style="left:{M}px;top:{650 + i * 92 + 30}px;width:80px;font-size:22px;line-height:34px">{p[0]}</div>'
                     f'<div class="abs t" style="left:{M + 90}px;top:{650 + i * 92 + 24}px;width:520px;font-size:34px;line-height:42px">{e(p[2])}</div>'
                     f'<div class="abs mono" style="left:{W - M - 400}px;top:{650 + i * 92 + 34}px;width:400px;text-align:right;font-size:15px;line-height:26px">{e(p[1])}</div>'
                     for i, p in enumerate(PROY))
           + f'<div class="abs mono" style="left:{M}px;top:1214px;width:400px;font-size:20px;line-height:30px;color:#4fd6e8">Desliza →</div>'
           + f'<div class="abs serif" style="left:{M + 360}px;top:1200px;width:{IW - 360}px;text-align:right;font-size:46px;line-height:52px">{LEMA}</div>')
VISUAL = {'anatris-movimiento': v_anatris, 'lean-es-poster': v_vsm, 'contable-excel-es-poster': v_contable, 'charms': v_charms, 'cumplimiento-es-poster': v_audit}
for i, (n, tag, name, desc, img, st, res, tech) in enumerate(PROY):
    car.append(header(i + 2, f'Carrusel · {i + 2} / {N}', True)
               + f'<div class="abs h" style="left:{M}px;top:196px;width:300px;font-size:120px;line-height:120px;color:#15304d">{n}</div>'
               + f'<div class="abs mono" style="left:{M + 230}px;top:214px;width:{IW - 230}px;font-size:18px;line-height:28px;color:#4fd6e8">{e(tag)}</div>'
               + f'<div class="abs h" style="left:{M + 230}px;top:250px;width:{IW - 230}px;font-size:62px;line-height:66px">{e(name)}</div>'
               + vis(VISUAL[img](), M + 40, 352, 420 / 460)
               + para(e(desc), 800, size=29, lh=40, color='#e8eef6')
               + stats(st, 914, num=60)
               + para('<span class="k" style="font-size:17px;letter-spacing:0.2em">RESULTADO&nbsp;&nbsp;</span>' + e(res), 1076, size=23, lh=32)
               + f'<div class="rule" style="left:{M}px;top:1190px;width:{IW}px"></div>'
               + f'<div class="abs mono" style="left:{M}px;top:1222px;width:640px;font-size:15px;line-height:24px">{e(tech)}</div>'
               + f'<div class="abs mono" style="left:{W - M - 260}px;top:1220px;width:260px;text-align:right;font-size:20px;line-height:28px;color:#4fd6e8">Desliza →</div>')
car.append(header(N, f'Carrusel · {N} / {N}', True)
           + title('¿Cuál sigue?<br><span class="c">El tuyo.</span>', 116, top=230)
           + para('Cuéntanos qué proceso te está costando horas y te respondemos con un plan concreto.', 500, size=34, lh=46)
           + ''.join(f'<div class="rule" style="left:{M}px;top:{y}px;width:{IW}px"></div>'
                     f'<div class="abs k" style="left:{M}px;top:{y + 30}px;width:60px;font-size:22px;line-height:34px">0{j + 1}</div>'
                     f'<div class="abs t" style="left:{M + 70}px;top:{y + 24}px;width:500px;font-size:34px;line-height:42px">{a}</div>'
                     f'<div class="abs k" style="left:{W - M - 330}px;top:{y + 30}px;width:330px;text-align:right;font-size:22px;line-height:34px;color:#f79b4a">{b}</div>'
                     for j, (y, a, b) in enumerate([(680, 'Diagnóstico primero', '1 a 2 semanas'), (780, 'Precio cerrado', '3 a 5 días'),
                                                    (880, 'Entrega cada semana', '4 a 10 semanas'), (980, 'Acompañamiento', '30 días')]))
           + footer(LEMA, 'Hablemos', serif=True))
for i, b in enumerate(car, 1):
    add(f'C{i:02d}-carrusel-proyectos', W, H, b)

# =====================================================================
# 4. ANUNCIO / ENLACE 1200×627 · la calculadora
# =====================================================================
add('A01-anuncio-la-cuenta-1200x627', 1200, 627,
    logo(72, 58, 170)
    + '<div class="abs mono" style="left:628px;width:500px;top:84px;text-align:right;font-size:17px;line-height:24px">La cuenta</div>'
    + '<div class="rule" style="left:72px;top:150px;width:1056px"></div>'
    + '<div class="abs h" style="left:72px;top:190px;width:640px;font-size:68px;line-height:68px">Cuánto cuesta hacerlo a mano.</div>'
    + '<div class="abs p" style="left:72px;top:352px;width:620px;font-size:24px;line-height:34px">Pon tu tarea en la calculadora y mira la cuenta del año. Si no compensa automatizarla, también te lo dice.</div>'
    + '<div class="btn" style="left:72px;top:480px;width:290px;height:66px;font-size:24px;line-height:66px;border-radius:4px">Hacer la cuenta</div>'
    + '<div class="abs mono" style="left:392px;top:500px;width:400px;font-size:15px;line-height:24px;color:#4fd6e8">bouw-eight.vercel.app</div>'
    + '<div class="panel" style="left:780px;top:190px;width:348px;height:356px"></div>'
    + ''.join(f'<div class="abs p" style="left:808px;top:{214 + i * 56}px;width:200px;font-size:20px;line-height:30px">{a}</div>'
              f'<div class="abs k" style="left:1000px;top:{214 + i * 56}px;width:100px;text-align:right;font-size:22px;line-height:30px">{b}</div>'
              for i, (a, b) in enumerate([('Veces / semana', '3'), ('Minutos', '× 20'), ('Personas', '× 1'), ('Semanas', '× 48')]))
    + '<div class="abs" style="left:782px;top:440px;width:344px;height:104px;background:#0d2b48;border-radius:0 0 16px 16px"></div>'
    + '<div class="abs mono" style="left:808px;top:456px;width:200px;font-size:14px;line-height:22px">Al año</div>'
    + '<div class="abs h" style="left:808px;top:480px;width:300px;font-size:50px;line-height:54px;color:#4fd6e8">48 horas</div>')

# =====================================================================
# 5. SERIES 1080×1350 · CALIDAD (Q01–Q05) y AUTOMATIZACIÓN (Z01–Z05)
#    Todo sale del sitio: servicio Cumplimiento & BPM, informe de auditoría, Programa contable,
#    "¿Cuál te suena?" y la calculadora con sus tres veredictos.
# =====================================================================
# ---------- CALIDAD ----------
post('Q01-calidad-el-inspector',
     serie('Q', 1, 'Calidad', OR)
     + kicker('Cumplimiento normativo &amp; BPM', color=OR)
     + title('¿Y si el inspector llega <span class="o">mañana</span>, sin avisar?', 92, top=256)
     + para('Si hoy tendrías que pasar la noche buscando papeles, el problema no es la auditoría: es el sistema.', 560, size=30, lh=42)
     + f'<div class="panel" style="left:{M}px;top:700px;width:{IW}px;height:430px"></div>'
     + f'<div class="abs mono" style="left:{M + 40}px;top:730px;width:600px;font-size:17px;line-height:24px;color:{CY}">Con BOUW, la carpeta ya está armada</div>'
     + check(M + 40, 780, 'Expedientes estandarizados', w=IW - 80)
     + check(M + 40, 862, 'Cada registro con su sitio y su responsable', w=IW - 80)
     + check(M + 40, 944, 'La trazabilidad en pantalla', w=IW - 80)
     + check(M + 40, 1026, 'Carpetas de inspección listas 24/7', w=IW - 80)
     + footer('Prepara tu planta antes de tu próxima inspección.', 'Diagnóstico gratis'))

# Q02 · Trazabilidad: el lote 2410 del informe de auditoría del sitio
tr = (box(M, 640, 250, 76, 'PT 2410', CY, CY, 26) + box(M + 331, 640, 250, 76, 'Mezcla 118') + box(M + 662, 640, 250, 76, 'Envase 77')
      + line(M + 250, 678, M + 331, 678, CY) + line(M + 581, 678, M + 662, 678, CY))
for i, (mp, bad) in enumerate([('MP-03', 0), ('MP-07', 0), ('✕ MP-12', 1), ('MP-21', 0)]):
    x = M + i * 234
    tr += line(M + 456, 716, x + 102, 800, RED if bad else '#23415f', 3, '8 6' if bad else '')
    tr += box(x, 800, 204, 72, mp, RED if bad else '#23415f', RED if bad else '#c6d4e4', 24, '#2a1416' if bad else '#071a2f')
tr += f'<div class="abs mono" style="left:{M}px;top:890px;width:{IW}px;text-align:right;font-size:16px;line-height:24px;color:{RED}">MP-12 sin registro: el rastro se corta</div>'
post('Q02-calidad-trazabilidad',
     serie('Q', 2, 'Calidad', OR)
     + kicker('Trazabilidad · lote 2410', color=OR)
     + title('El rastro se corta en <span style="color:#ff6b5e">MP-12</span>.', 88, top=256)
     + para('Un solo registro que falta y ya no puedes demostrar de qué materia prima salió tu producto terminado.', 456, size=29, lh=40)
     + f'<div class="abs mono" style="left:{M}px;top:592px;width:{IW}px;font-size:16px;line-height:24px">Genealogía del lote · planta de ejemplo</div>'
     + tr
     + callout(948, 196, 'Con BOUW', 'Control de lotes y genealogía rastreable en minutos: del producto terminado a sus materias primas, sus equipos y quién lo hizo.', size=25)
     + footer('Sin revolver archivos.', 'Diagnóstico gratis'))

# Q03 · Informe de auditoría BPM (planta de ejemplo del sitio)
hall = [('Trazabilidad', 'Crítico', RED), ('CAPA', 'Mayor', OR), ('Expedientes digitales', 'Menor', YEL),
        ('Liberación', 'Menor', YEL), ('Registros de lote', 'Cumple', GRN), ('Integridad de datos', 'Cumple', GRN)]
tab = f'<div class="panel" style="left:{M}px;top:700px;width:{IW}px;height:420px"></div>'
tab += f'<div class="abs mono" style="left:{M + 34}px;top:722px;width:500px;font-size:15px;line-height:22px">Hallazgos del inspector</div>'
tab += f'<div class="abs mono" style="left:{W - M - 234}px;top:722px;width:200px;text-align:right;font-size:15px;line-height:22px">Gravedad</div>'
for i, (h_, g, c) in enumerate(hall):
    y = 760 + i * 58
    tab += (f'<div class="rule" style="left:{M + 2}px;top:{y}px;width:{IW - 4}px"></div>'
            f'<div class="abs p" style="left:{M + 34}px;top:{y + 10}px;width:520px;font-size:25px;line-height:38px;color:#e8eef6">{h_}</div>'
            f'<div class="abs" style="left:{W - M - 194}px;top:{y + 11}px;width:160px;height:36px;border-radius:18px;background:{c}22;border:2px solid {c}"></div>'
            f'<div class="abs k" style="left:{W - M - 194}px;top:{y + 11}px;width:160px;text-align:center;font-size:18px;line-height:36px;color:{c}">{g.upper()}</div>')
post('Q03-calidad-informe-auditoria',
     serie('Q', 3, 'Calidad', OR)
     + kicker('Informe de auditoría BPM · planta de ejemplo', color=OR)
     + title('Preparación: <span class="o">33 %</span>.<br>No lista.', 96, top=256)
     + stats([('1', 'Crítico'), ('1', 'Mayor'), ('2', 'Menor'), ('3', 'Lotes retenidos')], 470, num=88, color=OR)
     + tab
     + footer('Con BOUW: la lista en verde y el lote liberado.', 'Agendar diagnóstico'))

# Q04 · Reincidencia de desviaciones → CAPA con 8D
loop = ''
for i, t_ in enumerate(['Desviación', 'Parche rápido', 'Vuelve a pasar']):
    x = M + 40 + i * 284
    loop += box(x, 690, 250, 70, t_, OR, '#e8eef6', 21)
    if i < 2:
        loop += line(x + 250, 725, x + 284, 725, OR)
ok = ''
for i, t_ in enumerate(['Causa raíz', 'Acción', 'Prueba ✓']):
    x = M + 40 + i * 284
    ok += box(x, 930, 250, 70, t_, CY, CY, 21)
    if i < 2:
        ok += line(x + 250, 965, x + 284, 965, CY)
post('Q04-calidad-capa-8d',
     serie('Q', 4, 'Calidad', OR)
     + kicker('Reincidencia de desviaciones', color=OR)
     + title('Si la desviación vuelve cada mes, no está cerrada.', 80, top=256)
     + f'<div class="panel" style="left:{M}px;top:600px;width:{IW}px;height:190px"></div>'
     + f'<div class="abs mono" style="left:{M + 40}px;top:626px;width:500px;font-size:17px;line-height:24px;color:{OR}">● Hoy</div>' + loop
     + f'<div class="panel" style="left:{M}px;top:840px;width:{IW}px;height:190px"></div>'
     + f'<div class="abs mono" style="left:{M + 40}px;top:866px;width:700px;font-size:17px;line-height:24px;color:{CY}">● Con BOUW · Sistema CAPA con causa raíz (8D)</div>' + ok
     + para('Cada desviación se cierra con su causa, su acción y la prueba de que funcionó, para que no vuelva el mes siguiente.', 1056, size=25, lh=34)
     + footer('CAPA · 8D · Causa raíz · Auditorías internas', 'Hablemos'))

# Q05 · Burocracia y lotes retenidos
post('Q05-calidad-lotes-retenidos',
     serie('Q', 5, 'Calidad', OR)
     + kicker('Burocracia y lotes retenidos', color=OR)
     + title('Ningún lote debería esperar a que aparezca un papel.', 80, top=256)
     + vis(v_firmas(), M, 520, 380 / 460)
     + hoy_bouw('Papeles sueltos, archivadores desbordados, la alarma encendida y un lote retenido.',
                'Revisiones en paralelo y una sola firma por paso. Expedientes en orden y el lote liberado.', 930, 216)
     + footer('Agenda un diagnóstico de calidad gratis.', 'Diagnóstico gratis'))

# ---------- AUTOMATIZACIÓN ----------
post('Z01-automatizacion-si-se-repite',
     serie('Z', 1, 'Automatización', CY)
     + hero(250, 170, 720, 0.5)
     + f'<div class="abs serif" style="left:{M}px;top:640px;width:{IW}px;font-size:118px;line-height:118px">Si se repite,<br>{grad("se automatiza.")}</div>'
     + f'<div class="abs mono" style="left:{M}px;top:910px;width:{IW}px;font-size:17px;line-height:24px">¿Cuál de estas pasa en tu empresa?</div>'
     + check(M, 950, 'El cierre de mes lo arma alguien a mano.', CY, 27)
     + check(M, 1010, 'La misma información vive en tres archivos.', CY, 27)
     + check(M, 1070, 'Alguien copia datos de un sitio a otro.', CY, 27)
     + footer('Cuéntanos cuál y te decimos qué haríamos primero.', 'Hablemos'))

calc2 = f'<div class="panel" style="left:{M}px;top:560px;width:{IW}px;height:330px"></div>'
for i, (l_, v_) in enumerate([('Veces por semana', '5'), ('Minutos cada vez', '× 30'), ('Personas que intervienen', '× 2'), ('Semanas al año', '× 48')]):
    y = 560 + i * 64
    calc2 += (f'<div class="abs p" style="left:{M + 34}px;top:{y + 14}px;width:600px;font-size:26px;line-height:36px">{l_}</div>'
              f'<div class="abs k" style="left:{W - M - 334}px;top:{y + 14}px;width:300px;text-align:right;font-size:28px;line-height:36px">{v_}</div>'
              f'<div class="rule" style="left:{M + 2}px;top:{y + 63}px;width:{IW - 4}px"></div>')
calc2 += (f'<div class="abs" style="left:{M + 2}px;top:818px;width:{IW - 4}px;height:70px;background:#0d2b48;border-radius:0 0 16px 16px"></div>'
          f'<div class="abs mono" style="left:{M + 34}px;top:842px;width:300px;font-size:18px;line-height:24px;color:#c6d4e4">Al año</div>'
          f'<div class="abs h" style="left:{W - M - 434}px;top:824px;width:400px;text-align:right;font-size:54px;line-height:58px;color:{CY}">240 horas</div>')
post('Z02-automatizacion-copiar-datos',
     serie('Z', 2, 'Automatización', CY)
     + kicker('La cuenta')
     + title('Alguien pasa horas cada semana copiando datos de un sitio a otro.', 66, top=256)
     + para('Media hora, 5 veces por semana, entre 2 personas. Haz la cuenta:', 478, size=27, lh=37)
     + calc2
     + f'<div class="abs mono" style="left:{M}px;top:920px;width:300px;font-size:17px;line-height:24px;color:{GRN}">Veredicto</div>'
     + f'<div class="abs t" style="left:{M}px;top:952px;width:{IW}px;font-size:44px;line-height:50px">Aquí sí.</div>'
     + para('Más de 150 horas al año: casi un mes de trabajo de una persona, todos los años. Se cierra alcance y precio en 3 a 5 días.', 1012, size=24, lh=33)
     + footer('Haz la cuenta con tu tarea en la calculadora.', 'Hacer la cuenta'))

post('Z03-automatizacion-cierre-de-mes',
     serie('Z', 3, 'Automatización', CY)
     + kicker('Proyecto real · Programa contable')
     + title('El cierre de mes ya no se arma a mano.', 84, top=256)
     + vis(v_contable(), M + 60, 460, 400 / 460)
     + stats([('11', 'Hojas conectadas'), ('1', 'Archivo, cero licencias'), ('0', 'Migraciones de sistema')], 890, num=80)
     + para('<span class="k" style="font-size:17px;letter-spacing:0.2em">RESULTADO&nbsp;&nbsp;</span>Se genera solo desde los movimientos ya capturados. El equipo siguió en el Excel que ya sabía usar.', 1078, size=24, lh=33)
     + footer('Excel · VBA · Inventario · Kits / BOM · Dashboard', 'Hablemos'))

files = ''
for i, (n_, t_) in enumerate([('ventas_final.xlsx', '$12 430'), ('ventas_final_v2.xlsx', '$12 910'), ('ventas_REAL.xlsx', '$11 870')]):
    y = 560 + i * 110
    files += (f'<div class="panel" style="left:{M}px;top:{y}px;width:400px;height:90px;border-color:#5a2a2a"></div>'
              f'<div class="abs k" style="left:{M + 24}px;top:{y + 12}px;width:360px;font-size:20px;line-height:30px;color:#c6d4e4">{n_}</div>'
              f'<div class="abs h" style="left:{M + 24}px;top:{y + 46}px;width:250px;font-size:30px;line-height:34px;color:{RED}">{t_}</div>')
one = (f'<div class="abs" style="left:{M + 470}px;top:560px;width:442px;height:310px;background:#08243a;border:2px solid {CY};border-radius:18px"></div>'
       f'<div class="abs mono" style="left:{M + 500}px;top:584px;width:400px;font-size:16px;line-height:24px;color:{CY}">1 archivo · 11 hojas conectadas</div>')
for i, h_ in enumerate(['Clientes', 'Productos', 'Componentes', 'Kits', 'Ventas', 'Compras y gastos', 'Anticipos', 'Tablero']):
    x = M + 500 + (i % 2) * 196
    y = 628 + (i // 2) * 56
    one += (f'<div class="abs" style="left:{x}px;top:{y}px;width:184px;height:44px;border-radius:8px;background:#0d3350"></div>'
            f'<div class="abs p" style="left:{x}px;top:{y}px;width:184px;text-align:center;font-size:19px;line-height:44px;color:#e8eef6">{h_}</div>')
post('Z04-automatizacion-tres-archivos',
     serie('Z', 4, 'Automatización', CY)
     + kicker('¿Te suena?')
     + title('La misma información en tres archivos. <span class="dim">Ninguno cuadra.</span>', 70, top=256)
     + f'<div class="abs mono" style="left:{M}px;top:520px;width:400px;font-size:16px;line-height:24px;color:{RED}">Hoy · ejemplo</div>'
     + f'<div class="abs mono" style="left:{M + 470}px;top:520px;width:400px;font-size:16px;line-height:24px;color:{CY}">Con BOUW</div>'
     + files
     + line(M + 410, 715, M + 462, 715, CY, 4)
     + one
     + callout(920, 200, 'Resultado', 'Una sola fuente de verdad, sin migrar a otro sistema ni pagar licencias nuevas. El tablero se recalcula solo.', size=26)
     + footer('Si se repite, se automatiza.', 'Hablemos'))

ver = ''
for i, (rng, ttl, body, c) in enumerate([
        ('Menos de 40 h/año', 'No lo automatices', 'Un proyecto para esto cuesta más de lo que ahorra. Si la tarea crece, vuelve a hacer la cuenta.', RED),
        ('40 a 150 h/año', 'Está en la frontera', 'Sale a cuenta si además te está costando errores. Si solo son las horas, espera.', YEL),
        ('Más de 150 h/año', 'Aquí sí', 'Casi un mes de trabajo de una persona, todos los años. Se construye en 4 a 10 semanas.', GRN)]):
    y = 560 + i * 196
    ver += (f'<div class="panel" style="left:{M}px;top:{y}px;width:{IW}px;height:176px"></div>'
            f'<div class="abs" style="left:{M}px;top:{y}px;width:8px;height:176px;background:{c};border-radius:4px"></div>'
            f'<div class="abs k" style="left:{M + 40}px;top:{y + 26}px;width:360px;font-size:20px;line-height:30px;color:{c}">{rng}</div>'
            f'<div class="abs t" style="left:{M + 400}px;top:{y + 20}px;width:480px;font-size:36px;line-height:42px">{ttl}</div>'
            + para(body, y + 78, size=24, lh=33, width=IW - 80, left=M + 40))
post('Z05-automatizacion-no-todo',
     serie('Z', 5, 'Automatización', CY)
     + kicker('Lo que nadie te dice')
     + title('No todo hay que automatizarlo.', 92, top=256)
     + para('Nuestra calculadora te lo dice antes que nosotros. Así decidimos qué vale la pena:', 470, size=28, lh=38)
     + ver
     + footer('Haz la cuenta con tu tarea en 30 segundos.', 'Hacer la cuenta'))

# =====================================================================
# 7. SERIE PROYECTOS (P01–P07): un proyecto del sitio por publicación, todo dibujado
# =====================================================================
PR = [
    ('P01-proyecto-mejora-continua', 'Caso · Mejora continua · Lean Six Sigma', 'Menos espera, menos reproceso, mejor producto.',
     'Una línea de dos turnos. Trabajamos en piso con producción y calidad para que el producto saliera bien a la primera.',
     v_mejora, [('−15 %', 'Tiempo de preparación'), ('−20 %', 'Reprocesos'), ('4', 'Operadores capacitados')],
     'Agenda una evaluación técnica de tu línea.', 'Optimiza tu línea'),
    ('P02-proyecto-mejora-continua-metodo', 'Caso · Mejora continua · Método', 'Así lo hicimos, paso a paso.',
     'Cada minuto de preparación es un minuto sin producir, y una pieza fuera de especificación se paga dos veces.',
     v_dmaic, [('2', 'Turnos, mismo criterio'), ('VSM', 'Estado actual mapeado'), ('5S', 'Estaciones reorganizadas')],
     'La causa se busca en el proceso, no en la persona.', 'Hablemos'),
    ('P03-proyecto-simulacion-de-flujos', 'Simulación de flujos &amp; visión analítica', '29 minutos de entrega. Solo 3,7 agregan valor.',
     'Con los datos de tu operación armamos un modelo de la línea y probamos ahí cada cambio, antes de mover un solo equipo.',
     v_vsm, [('29 min', 'Tiempo de entrega'), ('3,7 min', 'Valor agregado'), ('13 %', 'Del tiempo agrega valor')],
     'Sin parar la producción para hacer pruebas.', 'Probar la simulación'),
    ('P04-proyecto-programa-contable', 'Automatización · Gestión · Taller de manufactura', 'El cierre de mes, mapeado como una línea.',
     'Un taller que fabrica kits y tótems armaba el cierre a mano. Vimos dónde nace cada dato y cuántas veces se vuelve a escribir.',
     v_contable, [('11', 'Hojas conectadas'), ('1', 'Archivo, cero licencias'), ('0', 'Migraciones de sistema')],
     'El cierre sale de los movimientos ya capturados.', 'Hablemos'),
    ('P05-proyecto-charms-ecuador', 'Web · Pedidos por WhatsApp · Charms Ecuador', 'El pedido llega a WhatsApp ya escrito.',
     'Web para un taller de regalos en porcelana fría que cierra sus ventas por WhatsApp. Sin servidor ni base de datos.',
     v_charms, [('15', 'Modelos con foto real'), ('4', 'Pasos del cotizador'), ('$0', 'Costo de hosting')],
     'El cliente llega con pieza, detalles y precio.', 'Quiero algo así'),
    ('P06-proyecto-anatris', 'Salud · Atlas 3D · Producto propio', 'La anatomía en 3D, en el navegador.',
     'Atlas de anatomía y biomecánica para fisioterapia: rangos de movimiento reales y cada dato clínico con su fuente.',
     v_anatris, [('6', 'Regiones clínicas'), ('113', 'Músculos con ficha'), ('79', 'Tests con sens/spec')],
     'En línea y en producción: anatris.vercel.app', 'Verlo en vivo'),
    ('P07-proyecto-informe-de-auditoria', 'Hoy → BOUW · Informe de auditoría', 'La misma planta, hoy y con BOUW.',
     'Los hallazgos del inspector, las CAPA, los lotes retenidos y el rastro de un lote hasta su materia prima.',
     v_audit, [('9', 'CAPA abiertas hoy'), ('3', 'Lotes retenidos'), ('1', 'Hallazgo crítico')],
     'Prepara tu planta antes de la inspección.', 'Agendar diagnóstico'),
]
for i, (name, kick, ttl, sub, fn, st, ph, cta) in enumerate(PR, 1):
    post(name,
         serie('P', i, 'Proyectos', CY).replace(f'· {i} / 5', f'· {i} / {len(PR)}')
         + kicker(kick)
         + title(ttl, 66, top=246)
         + para(sub, 400, size=25, lh=35)
         + vis(fn(), M, 494)
         + stats(st, 978, num=62)
         + footer(ph, cta))

# =====================================================================
# 6. SERIE CASOS 1080×1350 (K01–K05): un proyecto real del sitio por publicación,
#    con sus fotos y capturas (sitio/imagenes/) y sus cifras tal cual aparecen en la página.
# =====================================================================
def caso(n):
    return serie('K', n, 'Caso real', OR)


def tag(x, y, txt, col=CY, w=None, fs=17):
    w = w or int(len(txt) * fs * 0.72 + 40)
    return (f'<div class="abs" style="left:{x}px;top:{y}px;width:{w}px;height:40px;background:rgba(4,16,31,.86);border:2px solid {col};border-radius:20px"></div>'
            f'<div class="abs mono" style="left:{x}px;top:{y}px;width:{w}px;height:40px;text-align:center;font-size:{fs}px;line-height:36px;color:{col};letter-spacing:.14em">{e(txt)}</div>')


# P01 · Anatris: producto propio, en vivo
post('K01-caso-anatris',
     caso(1)
     + kicker('Producto propio · Salud · Atlas 3D &#8212; En vivo')
     + title('Un atlas 3D de anatomía que corre en el navegador.', 76, top=256)
     + para('El cuerpo completo como modelo navegable: por región clínica, músculo por músculo y con rangos de movimiento reales. '
            'Cada dato clínico va con su fuente citada.', 446, size=27, lh=38)
     + photo('anatris-cuerpo', M, 590, IW, 452, pos='center')
     + tag(M + 24, 614, 'anatris.vercel.app')
     + stats([('6', 'Regiones clínicas'), ('113', 'Músculos con ficha'), ('79', 'Tests con sens/spec')], 1046, num=56)
     + footer('React · Three.js · WebGL · Supabase · PWA', 'Verlo en vivo'))

# P02 · Charms Ecuador: la web que entrega el pedido ya escrito en WhatsApp
ph = ''
for i, nm in enumerate(['charms-movil-inicio', 'charms-movil-cotizar', 'charms-movil-pedidos']):
    x = M + i * 312
    ph += (f'<div class="abs" style="left:{x - 6}px;top:564px;width:{288 + 12}px;height:{570 + 12}px;border-radius:30px;background:#0b2036;border:2px solid #23415f"></div>'
           + photo(nm, x, 570, 288, 570, pos='top').replace('border-radius:18px', 'border-radius:24px'))
post('K02-caso-charms-ecuador',
     caso(2)
     + kicker('Web · Pedidos por WhatsApp &#8212; En vivo')
     + title('El cliente llega a WhatsApp con el pedido <span class="c">ya escrito.</span>', 70, top=256)
     + para('Para un taller de regalos en porcelana fría: catálogo con fotos reales, cotizador en 4 pasos y un muñeco 3D que se gira con el dedo.', 446, size=26, lh=36)
     + ph
     + footer('<span class="c">15</span> modelos · <span class="c">4</span> pasos · <span class="c">$0</span> de hosting', 'Quiero algo así'))

# P03 · Mejora continua en una línea de extrusión: fotos reales de planta
post('K03-caso-mejora-continua-planta',
     caso(3)
     + kicker('Mejora continua · Línea de extrusión', color=OR)
     + title('Esto no es un render. <span class="o">Es una planta real.</span>', 76, top=256)
     + photo('mejora-linea-extrusion', M, 470, 440, 560, pos='center 40%')
     + photo('mejora-termometro', M + 464, 470, IW - 464, 268, pos='center 30%')
     + photo('mejora-producto-paletizado', M + 464, 762, IW - 464, 268, pos='center 45%')
     + tag(M + 20, 490, 'En planta', OR)
     + stats([('−15 %', 'Tiempo de preparación'), ('−20 %', 'Reprocesos'), ('4', 'Operadores con estándar')], 1050, num=60)
     + footer('Medimos en piso antes de proponer nada.', 'Diagnóstico'))

# P04 · Lean: la misma planta, hoy y con BOUW (ilustraciones del sitio)
post('K04-caso-hoy-vs-bouw',
     caso(4)
     + kicker('Lean manufacturing &amp; ingeniería de planta')
     + title('La misma planta. <span class="dim">Otro flujo.</span>', 68, top=262)
     + photo('lean-antes', M, 400, IW, 392, pos='center')
     + tag(M + 20, 420, 'Hoy', OR)
     + photo('lean-despues', M, 810, IW, 336, pos='center 55%')
     + tag(M + 20, 830, 'Con BOUW', CY)
     + footer('De recorridos cruzados a un solo flujo.', 'Evaluación técnica'))

# P05 · Cierre de año: la cuenta de 2026
calc5 = f'<div class="panel" style="left:{M}px;top:600px;width:{IW}px;height:330px"></div>'
for i, (l_, v_) in enumerate([('La tarea', 'Armar el cierre de mes'), ('Veces al año', '12'), ('Horas cada vez', '× 16'), ('Personas', '× 2')]):
    y = 600 + i * 64
    calc5 += (f'<div class="abs p" style="left:{M + 34}px;top:{y + 14}px;width:400px;font-size:26px;line-height:36px">{l_}</div>'
              f'<div class="abs k" style="left:{W - M - 534}px;top:{y + 14}px;width:500px;text-align:right;font-size:26px;line-height:36px">{v_}</div>'
              f'<div class="rule" style="left:{M + 2}px;top:{y + 63}px;width:{IW - 4}px"></div>')
calc5 += (f'<div class="abs" style="left:{M + 2}px;top:858px;width:{IW - 4}px;height:70px;background:#0d2b48;border-radius:0 0 16px 16px"></div>'
          f'<div class="abs mono" style="left:{M + 34}px;top:882px;width:300px;font-size:18px;line-height:24px;color:#c6d4e4">En 2026</div>'
          f'<div class="abs h" style="left:{W - M - 434}px;top:864px;width:400px;text-align:right;font-size:54px;line-height:58px;color:{OR}">384 horas</div>')
post('K05-cierre-de-ano-la-cuenta',
     caso(5).replace('>Caso real<', '>Cierre de año<')
     + hero(680, 180, 330, 0.4)
     + kicker('La cuenta de 2026', top=206, color=OR)
     + title('¿Cuántas horas<br>se fueron a mano<br><span class="o">en 2026?</span>', 66, top=258, width=600)
     + para('Un ejemplo que vemos seguido:', 540, size=26, lh=36)
     + calc5
     + f'<div class="abs mono" style="left:{M}px;top:962px;width:300px;font-size:17px;line-height:24px;color:{GRN}">Veredicto</div>'
     + f'<div class="abs t" style="left:{M}px;top:994px;width:{IW}px;font-size:44px;line-height:50px">Aquí sí. Y en 2027 no se repite.</div>'
     + para('Haz tu cuenta antes de planificar el año: 30 segundos en la calculadora del sitio.', 1060, size=24, lh=33)
     + footer('Si no compensa automatizarla, también te lo dice.', 'Hacer la cuenta'))

# =====================================================================
# 8. SERIE "QUÉ ES BOUW" (M01–M10): frases de posicionamiento, el problema primero.
#    Estilo: una frase grande que contrasta (lo tachado = lo que NO hacemos) + 2-3 líneas del sitio.
# =====================================================================
def tach(t):
    return (f'<span style="color:#8fa8c4;text-decoration:line-through;text-decoration-color:{OR};'
            f'text-decoration-thickness:9px">{t}</span>')


def manif(name, n, kick, frase, body, ph, cta, size=92, body_top=780, drag=True):
    bw = IW - 440 if drag else IW
    post(name,
         serie('M', n, 'Qué es BOUW', CY).replace(f'· {n} / 5', f'· {n} / 10')
         + kicker(kick)
         + f'<div class="abs h" style="left:{M}px;top:252px;width:{IW}px;font-size:{size}px;line-height:{round(size * 1.02)}px">{frase}</div>'
         + f'<div class="abs" style="left:{M}px;top:{body_top - 34}px;width:90px;height:4px;background:{CY}"></div>'
         + para(body, body_top, size=31, lh=44, width=bw)
         + (hero(W - M - 430, body_top - 40, 430, 0.5) if drag else '')
         + footer(ph, cta))


manif('M01-no-vendemos-software', 1, 'Lo que vendemos',
      f'No vendemos {tach("software")}.<br>Te devolvemos <span class="c">horas.</span>',
      'El software es solo la herramienta. Lo que importa es que la tarea que hoy le quita horas a tu equipo deje de hacerse a mano.',
      'Si se repite, se automatiza.', 'Hablemos', size=104)
manif('M02-somos-ingenieros', 2, 'Quiénes somos',
      f'Somos ingenieros de procesos. <span class="c">No vendedores de herramientas.</span>',
      'Ordenamos la planta, blindamos la calidad y automatizamos lo que se repite. Más de 7 años en piso, entre Ecuador y México.',
      'Del diseño a la realidad.', 'Conócenos', size=88)
manif('M03-primero-medimos', 3, 'Cómo empezamos',
      'Primero medimos.<br><span class="c">Después opinamos.</span>',
      'Diagnóstico de 1 a 2 semanas en tu proceso real, antes de proponer nada. Si al final no hay proyecto, la medición se queda contigo.',
      'Sin propuestas de escritorio.', 'Pedir diagnóstico', size=104)
manif('M04-te-lo-decimos', 4, 'Honestidad',
      f'Si no compensa automatizarlo, <span class="o">te lo decimos.</span>',
      'Menos de 40 horas al año no justifica un proyecto. Preferimos perder una venta a venderte algo que no necesitas.',
      'Haz la cuenta en 30 segundos.', 'Hacer la cuenta', size=96)
manif('M05-no-es-excel', 5, 'El problema real',
      f'Tu problema no es {tach("Excel")}.<br>Es que <span class="c">nada está conectado.</span>',
      'La misma información en tres archivos y ninguno cuadra. Lo resolvimos con un solo archivo y 11 hojas conectadas, sin cambiar de sistema.',
      'Usa lo que tu equipo ya sabe usar.', 'Hablemos', size=92)
manif('M06-es-el-proceso', 6, 'El problema real',
      f'El problema casi nunca es la {tach("persona")}. <span class="c">Es el proceso.</span>',
      'Cuando algo falla buscamos el paso que lo deja pasar, no al culpable. Así la desviación se cierra y no vuelve el mes siguiente.',
      'La causa está en el proceso.', 'Hablemos', size=92)
manif('M07-auditoria-sistema', 7, 'Calidad',
      f'Una auditoría no se prepara {tach("la semana antes")}. <span class="c">Se prepara con un sistema.</span>',
      'Expedientes estandarizados, cada registro con su responsable y la carpeta lista 24/7. Si llega un inspector sin aviso, ya está armada.',
      'Diagnóstico de calidad gratis.', 'Agendar', size=84)
manif('M08-precio-cerrado', 8, 'Sin sorpresas',
      'Precio cerrado.<br>Por escrito.<br><span class="c">Antes de empezar.</span>',
      'Alcance, entregables, plazo y precio en 3 a 5 días. Si algo no se puede prometer, lo decimos desde el principio.',
      'Y entregamos algo que funciona cada semana.', 'Hablemos', size=104)

# M09 · Qué vamos a hacer contigo (las condiciones del sitio, como camino)
pasos = ''
for i, (n_, pl, d) in enumerate([('Medimos', '1–2 semanas', 'Diagnóstico en tu proceso real.'),
                                  ('Te damos precio cerrado', '3–5 días', 'Alcance, plazo y precio por escrito.'),
                                  ('Construimos contigo', '4–10 semanas', 'Cada semana ves algo que ya funciona.'),
                                  ('Nos quedamos', '30 días', 'Acompañamiento sin contrato nuevo.')]):
    y = 520 + i * 152
    pasos += (f'<div class="abs" style="left:{M}px;top:{y}px;width:84px;height:84px;border-radius:42px;border:3px solid {CY};background:#04101f"></div>'
              + tx(M, y, 84, f'{i + 1}', 40, CY, 'h', 'center', 84)
              + (f'<div class="abs" style="left:{M + 41}px;top:{y + 86}px;width:3px;height:64px;background:#23415f"></div>' if i < 3 else '')
              + tx(M + 120, y + 4, 520, n_, 38, '#e8eef6', 't', 'left', 44)
              + tx(M + 120, y + 52, 560, d, 25, '#c6d4e4', 'p')
              + tx(W - M - 260, y + 12, 260, pl, 24, OR, 'k', 'right'))
post('M09-que-vamos-a-hacer',
     serie('M', 9, 'Qué es BOUW', CY).replace('· 9 / 5', '· 9 / 10')
     + kicker('Qué vamos a hacer contigo')
     + f'<div class="abs h" style="left:{M}px;top:252px;width:{IW}px;font-size:96px;line-height:98px">Así trabajamos. <span class="c">Sin sorpresas.</span></div>'
     + pasos
     + footer('Si algo no se puede prometer, lo decimos.', 'Empezar'))

manif('M10-dos-sedes', 10, 'Dónde estamos',
      'Quito y Monterrey.<br><span class="c">Un mismo estándar.</span>',
      'Quito desde 2019, Monterrey desde 2023. Nueve horas al día en común: siempre hay alguien para responderte.',
      'Respondemos en menos de 24 h hábiles.', 'Escríbenos', size=100)

# =====================================================================
# 9. NUEVA LÍNEA v2 (N01–N14) · sistema profesional pensado para el celular:
#    etiqueta de categoría arriba, titular grande, poco texto (mínimo 32 px), retícula de plano,
#    barra de marca abajo con el logo. Sin botones falsos. El dragón solo en el logo.
# =====================================================================
LBG, INK, SUB, CYD, LLN = '#f3f0ea', '#0b1b2e', '#4a5d73', '#0e8fa8', '#d9d3c7'
LOGO_CL = 'file://' + os.path.join(ROOT, 'sitio', 'dragon', 'capturas', 'dragon-claro-realidad-transparente.png')
NAVY = '#04101f'


def bp_grid(dark):
    col, op = ('#4fd6e8', .05) if dark else ('#0b1b2e', .055)
    d = ''.join(f'M{x} 0V{H}' for x in range(54, W, 54)) + ''.join(f'M0 {y}H{W}' for y in range(54, H, 54))
    return (f'<svg class="abs" style="left:0;top:0" width="{W}" height="{H}" viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg">'
            f'<path d="{d}" fill="none" stroke="{col}" stroke-opacity="{op}" stroke-width="1.5"/></svg>')


def pill(txt, col, dark, x=M, y=72):
    w = int(len(html.unescape(txt)) * 17.4 + 70)
    bg = 'rgba(4,16,31,.55)' if dark else 'rgba(255,255,255,.6)'
    return (f'<div class="abs" style="left:{x}px;top:{y}px;width:{w}px;height:50px;border-radius:25px;border:2px solid {col};background:{bg}"></div>'
            f'<div class="abs" style="left:{x + 24}px;top:{y + 19}px;width:12px;height:12px;border-radius:6px;background:{col}"></div>'
            f'<div class="abs mono" style="left:{x + 46}px;top:{y}px;width:{w - 50}px;font-size:21px;line-height:50px;color:{col};letter-spacing:.16em">{txt}</div>')


def brandbar(dark):
    src = LOGO if dark else LOGO_CL
    ln, tc = ('rgba(79,214,232,.25)', '#9fb3c8') if dark else ('#d3ccbf', SUB)
    return (f'<div class="abs" style="left:{M}px;top:1214px;width:{IW}px;height:2px;background:{ln}"></div>'
            f'<img class="abs" alt="BOUW" src="{src}" style="left:{M}px;top:1236px;width:160px;height:{round(160 / LOGO_R)}px">'
            f'<div class="abs mono" style="left:{W - M - 560}px;top:1262px;width:560px;text-align:right;font-size:21px;line-height:30px;color:{tc};letter-spacing:.14em">Quito · Monterrey</div>')


def frame(name, dark, tag, tagcol, body, foto=None, pos='center', shade=None):
    bg = ''
    if foto:
        bg = photo(foto, 0, 0, W, H, pos=pos).replace('border-radius:18px', 'border-radius:0')
        bg += (f'<div class="abs" style="left:0;top:0;width:{W}px;height:{H}px;background:'
               f'{shade or "linear-gradient(180deg,rgba(4,16,31,.85) 0%,rgba(4,16,31,.1) 20%,rgba(4,16,31,.2) 40%,rgba(4,16,31,.94) 64%,#04101f 100%)"}"></div>')
    else:
        bg = f'<div class="abs" style="left:0;top:0;width:{W}px;height:{H}px;background:{NAVY if dark else LBG}"></div>' + bp_grid(dark)
    pieces.append((name, W, H, bg + pill(tag, tagcol, dark) + body + brandbar(dark)))


def T(t, size, top, col=None, dark=False, width=IW, left=M, lh=1.0, cls='h'):
    col = col or ('#ffffff' if dark else INK)
    return f'<div class="abs {cls}" style="left:{left}px;top:{top}px;width:{width}px;font-size:{size}px;line-height:{round(size * lh)}px;color:{col}">{t}</div>'


def Pp(t, top, size=34, col=None, dark=False, width=IW, left=M, lh=1.38):
    col = col or ('#c9d6e3' if dark else SUB)
    return f'<div class="abs p" style="left:{left}px;top:{top}px;width:{width}px;font-size:{size}px;line-height:{round(size * lh)}px;color:{col}">{t}</div>'


C_ = lambda t: f'<span style="color:{CY}">{t}</span>'      # cian sobre oscuro
CL_ = lambda t: f'<span style="color:{CYD}">{t}</span>'    # cian sobre claro
O_ = lambda t: f'<span style="color:{OR}">{t}</span>'

# ---------- N01 · 5 señales (claro) ----------
rows = ''
for i, t_ in enumerate(['El cierre de mes se arma a mano', 'Nadie sabe cuánto tarda una pieza', 'Los errores se detectan tarde',
                        'Cada quien hace la tarea a su manera', 'Tres archivos y ninguno cuadra']):
    y = 548 + i * 128
    rows += (f'<div class="abs" style="left:{M}px;top:{y - 22}px;width:{IW}px;height:2px;background:{LLN}"></div>'
             + T(f'0{i + 1}', 54, y, OR, lh=1.1) + T(e(t_), 38, y + 6, INK, width=IW - 120, left=M + 120, lh=1.2, cls='t'))
frame('N01-senales-planta-pierde-horas', False, 'Diagnóstico rápido', CYD,
      T(f'5 señales de que tu empresa {CL_("pierde horas")} sin darse cuenta', 84, 176, lh=1.02) + rows)

# ---------- N02 · Mito vs. realidad (claro arriba, oscuro abajo) ----------
pieces.append(('N02-mito-realidad-automatizar', W, H,
    f'<div class="abs" style="left:0;top:0;width:{W}px;height:{H}px;background:{LBG}"></div>' + bp_grid(False)
    + f'<div class="abs" style="left:0;top:600px;width:{W}px;height:750px;background:{NAVY}"></div>'
    + pill('✕ Mito', OR, False)
    + T('“Automatizar es caro y obliga a cambiar todo el sistema.”', 76, 176, INK, lh=1.05)
    + pill('✓ Realidad', CY, True, y=652)
    + T(f'Un taller automatizó su cierre de mes {C_("sin cambiar de sistema.")}', 60, 740, '#ffffff', lh=1.08)
    + ''.join(T(n_, 88, 950, CY, lh=1) + Pp(l_, 1052, 26, '#c9d6e3', True, 280, M + i * 312) .replace(f'left:{M + i * 312}px', f'left:{M + i * 312}px')
              if False else T(n_, 88, 950, CY, left=M + i * 312, width=280, lh=1) + Pp(l_, 1050, 27, None, True, 280, M + i * 312, 1.3)
              for i, (n_, l_) in enumerate([('11', 'hojas conectadas'), ('0', 'licencias nuevas'), ('0', 'migraciones')]))
    + brandbar(True)))

# ---------- N03 · Caso real con foto ----------
frame('N03-caso-dos-turnos-foto', True, 'Caso real · Mejora continua', OR,
      T('−20 %', 220, 600, CY, lh=1)
      + T('de reprocesos en una línea de dos turnos.', 58, 836, '#ffffff', lh=1.08)
      + Pp(f'Y {C_("−15 %")} en tiempo de preparación, con 4 operadores capacitados.', 1000, 34, '#d6e0ea', True),
      foto='mejora-linea-extrusion', pos='center 35%')

# ---------- N04 · Encuesta (claro) ----------
op = ''
for i, (l_, t_) in enumerate([('A', 'Papeleo de calidad y auditorías'), ('B', 'El cierre de mes'), ('C', 'Esperas en la línea'), ('D', 'Copiar datos de un sistema a otro')]):
    y = 500 + i * 160
    op += (f'<div class="abs" style="left:{M}px;top:{y}px;width:{IW}px;height:134px;border-radius:20px;background:#ffffff;border:2px solid {LLN};box-shadow:0 10px 30px -18px rgba(11,27,46,.35)"></div>'
           f'<div class="abs" style="left:{M + 30}px;top:{y + 27}px;width:80px;height:80px;border-radius:40px;background:{CYD}"></div>'
           + T(l_, 42, y + 27, '#ffffff', width=80, left=M + 30, lh=1.9).replace('text-align:left', '') .replace(f'width:80px;font-size:42px', 'width:80px;text-align:center;font-size:42px')
           + T(e(t_), 38, y + 44, INK, width=IW - 170, left=M + 140, lh=1.2, cls='t'))
frame('N04-encuesta-que-te-quita-horas', False, 'Pregunta de la semana', CYD,
      T(f'¿Qué le quita más horas a {CL_("tu equipo")}?', 92, 176, lh=1.02)
      + op
      + Pp('Responde con la letra en los comentarios.', 1146, 30, SUB))

# ---------- N05 · Frase (oscuro) ----------
frame('N05-cita-ordena-antes-de-automatizar', True, 'Desde la planta', CY,
      f'<div class="abs serif" style="left:{M - 12}px;top:150px;width:300px;font-size:320px;line-height:320px;color:{CY}">“</div>'
      + T(f'Antes de automatizar un proceso, ordénalo. Automatizar el desorden solo te da {O_("desorden más rápido.")}', 84, 400, '#ffffff', lh=1.06, cls='serif')
      + f'<div class="abs" style="left:{M}px;top:1010px;width:70px;height:4px;background:{CY}"></div>'
      + T('Equipo de ingeniería BOUW', 36, 1040, '#ffffff', lh=1.2, cls='t'))

# ---------- N06 · Checklist (claro) ----------
ck = ''
for i, q in enumerate(['¿Mide antes de proponer?', '¿Precio cerrado y por escrito?', '¿Avances cada semana?', '¿Qué pasa después de entregar?', '¿Te diría si no te conviene?']):
    y = 470 + i * 112
    ck += (f'<div class="abs" style="left:{M}px;top:{y}px;width:56px;height:56px;border-radius:10px;border:3px solid {CYD};background:#fff"></div>'
           + T('✓', 40, y + 2, CYD, width=56, left=M, lh=1.35).replace('width:56px;font-size', 'width:56px;text-align:center;font-size')
           + T(e(q), 40, y + 4, INK, width=IW - 90, left=M + 90, lh=1.2, cls='t'))
frame('N06-checklist-antes-de-contratar', False, 'Guía rápida', CYD,
      T(f'Antes de contratar una consultora, {CL_("pregúntale esto:")}', 80, 176, lh=1.04)
      + ck
      + f'<div class="abs" style="left:{M}px;top:1052px;width:{IW}px;height:124px;border-radius:20px;background:{NAVY}"></div>'
      + T(f'En BOUW, las cinco son {C_("sí.")}', 46, 1052, '#ffffff', width=IW - 80, left=M + 40, lh=2.7, cls='t'))

# ---------- N07 · Foto: medimos en la línea ----------
frame('N07-medimos-en-la-linea-foto', True, 'Así trabajamos', CY,
      T(f'Medimos en la línea.<br>{C_("No en la oficina.")}', 100, 700, '#ffffff', lh=1.02)
      + Pp('Tiempos, esperas, inventarios y hasta la temperatura del agua de enfriamiento.', 960, 34, '#d6e0ea', True),
      foto='mejora-termometro', pos='center 75%')

# ---------- N08 · 3 errores (oscuro) ----------
er = ''
for i, (a_, b_) in enumerate([('Automatizar sin hacer la cuenta', 'Menos de 40 h al año no vale un proyecto.'),
                              ('Cambiar de sistema porque sí', 'Construye sobre lo que tu equipo ya usa.'),
                              ('Entregarlo todo al final', 'Entrega algo que funcione cada semana.')]):
    y = 470 + i * 236
    er += (f'<div class="abs" style="left:{M}px;top:{y}px;width:{IW}px;height:206px;border-radius:20px;background:#071a2f;border:2px solid #15304d"></div>'
           + T(f'<span style="color:{RED}">✕</span> {e(a_)}', 42, y + 34, '#ffffff', width=IW - 70, left=M + 36, lh=1.15, cls='t')
           + Pp(f'{C_("✓")} {e(b_)}', y + 112, 33, '#c9d6e3', True, IW - 70, M + 36, 1.3))
frame('N08-errores-al-automatizar', True, 'Aprendido en planta', CY,
      T(f'3 errores al automatizar {C_("y cómo evitarlos")}', 80, 176, '#ffffff', lh=1.04) + er)

# ---------- N09 · Antes / después (claro) ----------
ad = ''
for c_, (lab, col, items) in enumerate([('Antes', OR, ['Archivos juntados a mano', 'La misma cifra, varias veces', 'Nadie confía en el total']),
                                         ('Después', CYD, ['Cada dato se captura una vez', 'Las hojas se hablan solas', 'El cierre sale solo'])]):
    x = M + c_ * 468
    ad += (f'<div class="abs" style="left:{x}px;top:470px;width:444px;height:640px;border-radius:22px;background:{"#ffffff" if c_ else "#ebe4d8"};border:2px solid {LLN}"></div>'
           + pill(lab, col, False, x + 30, 500))
    for i, it in enumerate(items):
        y = 600 + i * 166
        ad += (T('✓' if c_ else '✕', 44, y, col, width=50, left=x + 32, lh=1.1)
               + T(e(it), 36, y + 2, INK, width=340, left=x + 86, lh=1.2, cls='t'))
frame('N09-antes-despues-cierre-de-mes', False, 'Automatización · caso real', CYD,
      T(f'El cierre de mes, {CL_("sin armarlo a mano.")}', 84, 176, lh=1.02) + ad
      + Pp('Taller de manufactura · sobre el mismo Excel, sin cambiar de sistema.', 1136, 26, SUB))

# ---------- N10 · Qué se puede automatizar (oscuro) ----------
g6 = ''
for i, a_ in enumerate(['Cotizaciones', 'Cierre de mes', 'Inventario y kits', 'Reportes de producción', 'Registros de calidad', 'Pedidos por WhatsApp']):
    x = M + (i % 2) * 468
    y = 470 + (i // 2) * 206
    g6 += (f'<div class="abs" style="left:{x}px;top:{y}px;width:444px;height:184px;border-radius:20px;background:#071a2f;border:2px solid #15304d"></div>'
           + T(f'0{i + 1}', 26, y + 28, OR, width=100, left=x + 32, lh=1.2, cls='k')
           + T(a_, 42, y + 74, '#ffffff', width=390, left=x + 32, lh=1.12, cls='t'))
frame('N10-que-se-puede-automatizar', True, 'Automatización', CY,
      T(f'¿Qué se puede automatizar en tu empresa?', 80, 176, '#ffffff', lh=1.04) + g6
      + Pp(f'Si se repite cada semana, {C_("probablemente se puede.")}', 1112, 34, '#c9d6e3', True))

# ---------- N11 · La regla de las 150 horas (claro) ----------
frame('N11-regla-150-horas', False, 'La cuenta', CYD,
      T('150 h', 330, 150, CYD, lh=1).replace('letter-spacing', 'x') .replace('class="abs h"', 'class="abs h" ')
      + T('al año: ahí automatizar ya sale a cuenta.', 64, 500, INK, lh=1.08)
      + Pp('Es casi un mes de trabajo de una persona, cada año.', 660, 36, SUB)
      + f'<div class="abs" style="left:{M}px;top:820px;width:{IW}px;height:300px;border-radius:22px;background:{NAVY}"></div>'
      + T('Tu cuenta', 24, 856, CY, width=400, left=M + 44, lh=1.2, cls='mono')
      + T('veces por semana × minutos × personas × 48 ÷ 60', 44, 906, '#ffffff', width=IW - 88, left=M + 44, lh=1.2, cls='t')
      + Pp(f'{O_("< 40 h")} no vale · {O_("40–150 h")} depende · {C_("> 150 h")} sí', 1040, 30, '#c9d6e3', True, IW - 88, M + 44))

# ---------- N12 · WhatsApp (oscuro, teléfono grande) ----------
px, py = 300, 470
wa = (f'<div class="abs" style="left:{px}px;top:{py}px;width:480px;height:700px;border-radius:52px;border:5px solid #3a5878;background:#0b141a;box-shadow:0 30px 80px -30px rgba(79,214,232,.4)"></div>'
      f'<div class="abs" style="left:{px + 5}px;top:{py + 5}px;width:470px;height:104px;border-radius:47px 47px 0 0;background:#1f2c34"></div>'
      f'<div class="abs" style="left:{px + 36}px;top:{py + 30}px;width:56px;height:56px;border-radius:28px;background:#e8a6b8"></div>'
      + T('Cliente', 32, py + 26, '#e9edef', width=300, left=px + 110, lh=1.2, cls='t') + T('en línea', 22, py + 66, '#8696a0', width=300, left=px + 110, lh=1.2, cls='p')
      + f'<div class="abs" style="left:{px + 70}px;top:{py + 150}px;width:370px;height:360px;border-radius:24px 4px 24px 24px;background:#005c4b"></div>'
      + T('Hola, quiero hacer este pedido:', 30, py + 176, '#e9edef', width=320, left=px + 100, lh=1.3, cls='p')
      + ''.join(T(f'✓ {t_}', 34, py + 280 + j * 56, '#e9edef', width=320, left=px + 100, lh=1.3, cls='t') for j, t_ in enumerate(['Pieza', 'Detalles', 'Precio estimado']))
      + f'<div class="abs" style="left:{px + 30}px;top:{py + 590}px;width:420px;height:70px;border-radius:35px;background:#1f2c34"></div>'
      + T('Mensaje ya escrito ✓✓', 22, py + 590, GRN, width=420, left=px + 30, lh=3.2, cls='mono').replace('width:420px;font-size', 'width:420px;text-align:center;font-size'))
frame('N12-cotizar-por-whatsapp', True, 'Automatización · ventas', CY,
      T(f'Tus clientes ya están en WhatsApp. {C_("¿Tus cotizaciones?")}', 76, 176, '#ffffff', lh=1.04) + wa)

# ---------- N13 · Tip en 3 pasos (claro) ----------
p3 = ''
for i, (a_, b_) in enumerate([('Cuántas veces por semana', 'ej. 5'), ('Cuánto tarda y cuántas personas', 'ej. 30 min · 2 personas'), ('Multiplica por 48 semanas', '5 × 30 × 2 × 48 = 240 h')]):
    y = 470 + i * 186
    p3 += (f'<div class="abs" style="left:{M}px;top:{y}px;width:96px;height:96px;border-radius:48px;background:{CYD}"></div>'
           + T(str(i + 1), 50, y, '#ffffff', width=96, left=M, lh=1.92).replace('width:96px;font-size', 'width:96px;text-align:center;font-size')
           + T(e(a_), 42, y + 2, INK, width=IW - 140, left=M + 136, lh=1.15, cls='t')
           + Pp(e(b_), y + 64, 32, SUB, False, IW - 140, M + 136, 1.3))
frame('N13-tip-haz-esta-cuenta', False, 'Tip de la semana', CYD,
      T(f'¿Vale la pena automatizar esa tarea? {CL_("3 pasos.")}', 80, 176, lh=1.04) + p3
      + f'<div class="abs" style="left:{M}px;top:1040px;width:{IW}px;height:130px;border-radius:20px;background:{NAVY}"></div>'
      + T(f'Más de 150 h al año: {C_("automatízala.")}', 44, 1040, '#ffffff', width=IW - 80, left=M + 40, lh=2.95, cls='t'))

# ---------- N14 · No es reemplazar personas (oscuro) ----------
frame('N14-no-es-reemplazar-personas', True, 'Lo que creemos', CY,
      T('Automatizar no es reemplazar personas.', 104, 220, '#ffffff', lh=1.0)
      + f'<div class="abs" style="left:{M}px;top:600px;width:90px;height:5px;background:{CY}"></div>'
      + T(f'Es quitarles lo que {C_("nunca debió ser su trabajo.")}', 88, 650, '#ffffff', lh=1.05, cls='serif')
      + Pp('Copiar datos. Cuadrar archivos. Armar reportes a mano.', 1010, 36, '#c9d6e3', True))

# ---------- escribir ----------
for f in os.listdir(OUT):
    if f.endswith('.html'):
        os.remove(os.path.join(OUT, f))
names = []
for name, w, h, body in pieces:
    doc = (f'<!doctype html><html lang="es"><head><meta charset="utf-8"><title>{e(name)}</title><style>{CSS}</style></head>'
           f'<body><section class="slide" style="width:{w}px;height:{h}px">{body}</section></body></html>')
    with open(os.path.join(OUT, name + '.html'), 'w') as f:
        f.write(doc)
    names.append(f'{name}:{w}x{h}')
with open(os.path.join(OUT, 'list.txt'), 'w') as f:
    f.write('\n'.join(names))
print(len(pieces), 'piezas')
