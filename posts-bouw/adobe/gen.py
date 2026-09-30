"""Genera los HTML listos para Adobe Express (y su vista previa local).

Cada documento es una serie de .slide con posición absoluta. Las imágenes van en base64.
Salida: out/<doc>.html (exportar) y out/<doc>.preview.html (fuentes locales, para revisar).
"""
import base64, os, html

HERE = os.path.dirname(os.path.abspath(__file__))
A = os.path.join(HERE, 'assets')
OUT = os.path.join(HERE, 'html')
os.makedirs(OUT, exist_ok=True)
FONTS = '/home/user/Bouw-marketing-/posts-bouw/fonts'
KIT = '<link rel="stylesheet" href="https://use.typekit.net/dnh2wmm.css">'


def uri(name):
    with open(os.path.join(A, name), 'rb') as f:
        return 'data:image/png;base64,' + base64.b64encode(f.read()).decode()


# Express no descarga imágenes por URL ni lee background-image: van en base64, livianas (paleta de 32 colores)
IMG = {k: uri('x-' + k + '.png') for k in ['front', 'd34', 'plano', 'seal']}

# Logo como vector plano (Express lo convierte en formas editables). Sin degradados, según el manual.
LOGO_SVG = ('<svg class="abs" style="left:{x}px;top:{y}px" width="{w}" height="{h}" viewBox="-2 -3.15 3.95 6.3" xmlns="http://www.w3.org/2000/svg">'
            '<path d="M -1.8 -2.5 H 0.5 V -2.86 L 1.22 -2.125 L 0.5 -1.39 V -1.75 H -0.9 V -0.25 H -1.8 Z" fill="#1f5488"/>'
            '<path d="M -1.8 0.25 H -0.9 V 1.75 H 0.2 V 2.5 H -1.8 Z" fill="#1f5488"/>'
            '<path d="M 0.2 -2.65 A 1.5 1.5 0 0 1 0.2 0.35 L 0.2 -0.2 A 0.95 0.95 0 0 0 0.2 -2.1 Z" fill="#22b5cf"/>'
            '<path d="M 0.2 -0.35 A 1.5 1.5 0 0 1 0.2 2.65 L -0.5 2.65 L -0.5 2.97 L -1.28 2.375 L -0.5 1.78 L -0.5 2.1 L 0.2 2.1 A 0.95 0.95 0 0 0 0.2 0.2 Z" fill="#e87722"/>'
            '<circle cx="1.31" cy="-1.668" r="0.44" fill="#22b5cf"/><circle cx="1.31" cy="0.632" r="0.44" fill="#f79b4a"/></svg>')


def logo(x, y, h):
    return LOGO_SVG.format(x=x, y=y, w=round(h * 3.95 / 6.3), h=h)

CSS = """
*{margin:0;padding:0;box-sizing:border-box}
body{background:#04101f}
.slide{position:relative;overflow:hidden;background:#04101f;color:#e8eef6;font-family:"ibm-plex-sans",sans-serif}
.abs{position:absolute}
.grid{position:absolute;left:0;top:0}
.h{font-family:"archivo-expanded",sans-serif;font-weight:800;letter-spacing:-0.02em;line-height:1.04;color:#e8eef6}
.o{color:#e87722}
.mono{font-family:"ibm-plex-mono",monospace;font-weight:500;text-transform:uppercase;letter-spacing:0.14em;color:#8fa8c4}
.k{font-family:"ibm-plex-mono",monospace;font-weight:500;color:#4fd6e8}
.t{font-family:"archivo-expanded",sans-serif;font-weight:800;color:#e8eef6;letter-spacing:-0.01em}
.p{font-family:"ibm-plex-sans",sans-serif;font-weight:400;color:#c6d4e4;line-height:1.35}
.rule{position:absolute;height:2px;background:#17406b}
.panel{position:absolute;background:#071a2f;border:2px solid #17406b}
.cta{position:absolute;background:#e87722;color:#04101f;font-family:"archivo-expanded",sans-serif;font-weight:800;text-align:center}
.brandtxt{font-family:"archivo-expanded",sans-serif;font-weight:800;color:#e8eef6;letter-spacing:0.02em}
"""

PREVIEW_FONTS = f"""
<style>
@font-face{{font-family:"archivo-expanded";src:url(file://{FONTS}/Archivo-100_900.woff2);font-weight:100 900;font-stretch:62% 125%}}
@font-face{{font-family:"ibm-plex-sans";src:url(file://{FONTS}/IBMPlexSans-400.woff2);font-weight:100 700}}
@font-face{{font-family:"ibm-plex-mono";src:url(file://{FONTS}/IBMPlexMono-500.woff2);font-weight:500}}
.h,.t,.cta,.brandtxt{{font-stretch:125%}}
</style>"""


def grid_svg_inline(w, h, step=60, marks=True):
    """Retícula cian + marcas de corte como SVG en base64 (una sola capa de imagen)."""
    lines = []
    for x in range(step, w, step):
        lines.append(f'<line x1="{x}" y1="0" x2="{x}" y2="{h}"/>')
    for y in range(step, h, step):
        lines.append(f'<line x1="0" y1="{y}" x2="{w}" y2="{y}"/>')
    m = ''
    if marks:
        d, L = 36, 34
        pts = [(d, d, 1, 1), (w - d, d, -1, 1), (d, h - d, 1, -1), (w - d, h - d, -1, -1)]
        for x, y, sx, sy in pts:
            m += f'<path d="M{x} {y + sy * L} V{y} H{x + sx * L}" fill="none" stroke="#4fd6e8" stroke-width="3"/>'
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">'
           f'<g stroke="#4fd6e8" stroke-opacity="0.07" stroke-width="2">{"".join(lines)}</g>{m}</svg>')
    return 'data:image/svg+xml;base64,' + base64.b64encode(svg.encode()).decode()


def e(s):
    return html.escape(s, quote=False)


def slide(w, h, body, name):
    return (f'<section class="slide" data-canvas-width="{w}" data-canvas-height="{h}" data-name="{e(name)}" '
            f'style="width:{w}px;height:{h}px">'
            f'{grid(w, h)}{body}</section>')


def grid(w, h, step=60):
    """Retícula y marcas de corte como SVG en línea: Express la convierte en 2 trazos vectoriales."""
    d = ''.join(f'M{x} 0V{h}' for x in range(step, w, step)) + ''.join(f'M0 {y}H{w}' for y in range(step, h, step))
    D, L = 36, 34
    m = ''.join(f'M{x} {y + sy * L}V{y}H{x + sx * L}' for x, y, sx, sy in
                [(D, D, 1, 1), (w - D, D, -1, 1), (D, h - D, 1, -1), (w - D, h - D, -1, -1)])
    return (f'<svg class="grid" width="{w}" height="{h}" viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg">'
            f'<path d="{d}" fill="none" stroke="#4fd6e8" stroke-opacity="0.07" stroke-width="2"/>'
            f'<path d="{m}" fill="none" stroke="#4fd6e8" stroke-width="3"/></svg>')


# ---------- piezas del feed 1080×1350 ----------
W, H = 1080, 1350
M = 84


def header(hoja):
    return (logo(M, 74, 58) +
            f'<div class="abs brandtxt" style="left:{M + 50}px;top:80px;font-size:34px;line-height:46px">BOUW</div>'
            f'<div class="abs mono" style="right:{M}px;top:88px;font-size:21px;line-height:30px;text-align:right;width:560px">{e(hoja)}</div>'
            f'<div class="rule" style="left:{M}px;top:160px;width:{W - 2 * M}px"></div>')


def footer(phrase, cta, cta_w=None):
    cw = cta_w or (len(cta) * 17 + 70)
    return (f'<div class="rule" style="left:{M}px;top:1160px;width:{W - 2 * M}px"></div>'
            f'<img class="abs" src="{IMG["seal"]}" style="left:{M - 6}px;top:1182px;width:112px;height:112px" alt="">'
            f'<div class="abs p" style="left:{M + 126}px;top:1206px;width:{W - 2 * M - 126 - cw - 24}px;font-size:25px;line-height:32px;color:#93a7bf">{phrase}</div>'
            f'<div class="cta" style="left:{W - M - cw}px;top:1208px;width:{cw}px;height:62px;font-size:22px;line-height:62px">{e(cta)}</div>')


def title(t, size, top=214, width=W - 2 * M):
    return f'<div class="abs h" style="left:{M}px;top:{top}px;width:{width}px;font-size:{size}px">{t}</div>'


def spec(rows, top, gap=150, kw=150):
    out = ''
    for i, (k, b, s) in enumerate(rows):
        y = top + i * gap
        out += (f'<div class="rule" style="left:{M}px;top:{y}px;width:{W - 2 * M}px"></div>'
                f'<div class="abs k" style="left:{M}px;top:{y + 30}px;width:{kw}px;font-size:24px;line-height:34px">{e(k)}</div>'
                f'<div class="abs t" style="left:{M + kw}px;top:{y + 26}px;width:{W - 2 * M - kw}px;font-size:34px;line-height:42px">{e(b)}</div>')
        if s:
            out += f'<div class="abs p" style="left:{M + kw}px;top:{y + 74}px;width:{W - 2 * M - kw}px;font-size:26px;line-height:34px">{e(s)}</div>'
    return out


def dragon_band(top, img='front', w=800):
    return f'<img class="abs" src="{IMG[img]}" style="left:{(W - w) // 2}px;top:{top}px;width:{w}px" alt="">'


feed = []

# F01 · ¿Qué te quita más el sueño? (fijar)
feed.append(('F01 · ¿Qué te quita más el sueño?', header('Hoja 01 · ¿Qué necesitas?')
             + title('¿Qué te quita más <span class="o">el sueño?</span>', 92)
             + spec([('1 · ORDEN', '“Todo pasa por mí.”', 'Te dejamos una empresa que funciona aunque no estés encima.'),
                     ('2 · TIEMPO', '“No nos alcanza el día.”', 'Tu equipo recupera horas cada semana, sin contratar más.'),
                     ('3 · CONTROL', '“Me entero a fin de mes.”', 'Tus números cada lunes y tu información protegida.')],
                    top=480, gap=190, kw=230)
             + footer('Responde con 1, 2 o 3 y te decimos qué haríamos primero.', 'Responde aquí')))

# F02 · Manifiesto con el dragón
feed.append(('F02 · Del diseño a la realidad', header('Hoja 02 · Qué hacemos')
             + title('Del diseño<br>a la realidad.', 104)
             + dragon_band(470)
             + spec([('A—01', 'Orden', 'Que la empresa funcione aunque no estés encima.'),
                     ('A—02', 'Tiempo', 'Que tu equipo haga más sin contratar más.'),
                     ('A—03', 'Control', 'Tus números a tiempo y tu información segura.')],
                    top=740, gap=138)
             + footer('Si el número no da, te lo decimos.', 'Radiografía gratis · 1 h')))

# F03 · Socios
ph = ''
for i, (cap, sub) in enumerate([('Procesos y calidad', '[Nombre] · Ing. Industrial'),
                                ('Sistemas y seguridad', '[Nombre] · Informática y ciberseguridad')]):
    x = M + i * 468
    ph += (f'<div class="panel" style="left:{x}px;top:400px;width:444px;height:500px"></div>'
           f'<div class="abs mono" style="left:{x}px;top:640px;width:444px;text-align:center;font-size:20px">[ Foto socio {i + 1} ]</div>'
           f'<div class="abs t" style="left:{x}px;top:926px;width:444px;font-size:30px;line-height:38px">{e(cap)}</div>'
           f'<div class="abs p" style="left:{x}px;top:970px;width:444px;font-size:24px;line-height:32px">{e(sub)}</div>')
feed.append(('F03 · Dos ingenieros', header('Hoja 03 · Quiénes somos')
             + title('Dos ingenieros.<br><span class="o">Un mismo estándar.</span>', 66) + ph
             + f'<div class="abs mono" style="left:{M}px;top:1060px;width:900px;font-size:20px;color:#4fd6e8">Quito · Monterrey · +7 años combinados</div>'
             + footer('Entramos, hacemos la cuenta y lo dejamos funcionando.', 'Conversemos')))

# F04 · Marca lo que reconozcas
chk = ''
items = ['Cada persona hace la misma tarea a su manera.',
         'Alguien pasa horas cada semana copiando datos de un sitio a otro.',
         'Todo pasa por el dueño.',
         'Los números llegan a fin de mes.',
         'Nadie ha probado si el respaldo funciona.']
for i, it in enumerate(items):
    y = 470 + i * 132
    chk += (f'<div class="abs" style="left:{M}px;top:{y + 6}px;width:48px;height:48px;border:3px solid #4fd6e8"></div>'
            f'<div class="abs p" style="left:{M + 80}px;top:{y}px;width:830px;font-size:32px;line-height:42px;color:#e8eef6">{e(it)}</div>'
            + (f'<div class="rule" style="left:{M}px;top:{y + 108}px;width:{W - 2 * M}px"></div>' if i < 4 else ''))
feed.append(('F04 · Marca lo que reconozcas', header('Hoja 04 · Qué te pasa')
             + title('Marca lo que <span class="o">reconozcas.</span>', 88) + chk
             + footer('¿Ninguna? Todavía no nos necesitas.', '¿Dos o más? Escríbenos')))

# F05 · Caso real
met = ''
for i, (n, lab) in enumerate([('11', 'Hojas conectadas'), ('1', 'Archivo, cero licencias'), ('0', 'Migraciones de sistema')]):
    x = M + i * 312
    met += (f'<div class="panel" style="left:{x}px;top:560px;width:288px;height:250px"></div>'
            f'<div class="abs h" style="left:{x + 28}px;top:580px;width:240px;font-size:120px;line-height:140px;color:#4fd6e8">{n}</div>'
            f'<div class="abs mono" style="left:{x + 28}px;top:730px;width:240px;font-size:18px;line-height:26px;color:#c6d4e4">{e(lab)}</div>')
feed.append(('F05 · Caso real: programa contable', header('Proyecto real · Manufactura')
             + f'<div class="abs mono" style="left:{M}px;top:214px;width:900px;font-size:22px;color:#4fd6e8">Automatización · Gestión · 2025</div>'
             + title('Un ERP pequeño, sobre el Excel que el equipo ya usaba.', 70, top=262) + met
             + f'<div class="abs p" style="left:{M}px;top:870px;width:{W - 2 * M}px;font-size:30px;line-height:42px">El cierre mensual dejó de armarse a mano: ahora sale solo de los movimientos ya capturados.</div>'
             + footer('¿Tu cierre de mes todavía se arma a mano?', 'Hablemos')))

# F06 · La cuenta
calc = ''
rows = [('Tarea: pasar pedidos del correo a la hoja', 'Ejemplo'), ('Veces por semana', '5'), ('Minutos cada vez', '× 30'),
        ('Personas que intervienen', '× 2'), ('Semanas al año', '× 48')]
for i, (l, v) in enumerate(rows):
    y = 440 + i * 74
    calc += (f'<div class="abs p" style="left:{M + 30}px;top:{y + 16}px;width:640px;font-size:27px;line-height:40px">{e(l)}</div>'
             f'<div class="abs k" style="left:{W - M - 330}px;top:{y + 16}px;width:300px;text-align:right;font-size:30px;line-height:40px">{e(v)}</div>'
             f'<div class="rule" style="left:{M}px;top:{y + 72}px;width:{W - 2 * M}px"></div>')
calc = f'<div class="panel" style="left:{M}px;top:440px;width:{W - 2 * M}px;height:480px"></div>' + calc
calc += (f'<div class="abs" style="left:{M}px;top:810px;width:{W - 2 * M}px;height:110px;background:#0f2c4c"></div>'
         f'<div class="abs t" style="left:{M + 30}px;top:840px;width:400px;font-size:34px;line-height:50px">Al año</div>'
         f'<div class="abs h" style="left:{W - M - 430}px;top:826px;width:400px;text-align:right;font-size:72px;line-height:80px;color:#4fd6e8">240 h</div>'
         f'<div class="abs h" style="left:{M}px;top:966px;width:300px;font-size:52px;line-height:60px;color:#4fd6e8">Aquí sí.</div>'
         f'<div class="abs p" style="left:{M + 290}px;top:960px;width:620px;font-size:25px;line-height:34px">Más de 150 horas al año. Con menos de 40, no lo automatices: te lo decimos.</div>')
feed.append(('F06 · La cuenta', header('Hoja 05 · La cuenta') + title('Cuánto cuesta hacerlo a mano.', 78) + calc
             + footer('Haz la cuenta con tu tarea y mándanosla.', 'Haz la cuenta')))

# F07 · Método
feed.append(('F07 · Plazos que se pueden escribir', header('Hoja 06 · Cómo trabajamos')
             + title('Plazos que se pueden <span class="o">escribir.</span>', 84)
             + spec([('01', 'Radiografía', '1 hora en tu empresa. Gratis.'),
                     ('02', 'Alcance y precio cerrados', 'En 3 a 5 días.'),
                     ('03', 'Construcción', 'De 4 a 10 semanas, según el tamaño.'),
                     ('04', 'Entrega', 'Funcionando, con la documentación para mantenerlo sin nosotros.')],
                    top=470, gap=164, kw=120)
             + footer('Sin reuniones que no terminan en nada.', 'Agenda la tuya')))

# F08 · Respaldo
feed.append(('F08 · Respaldo', header('Hoja 07 · Control')
             + title('¿Cuándo <span class="o">restauraste</span> un respaldo por última vez?', 74)
             + spec([('C—01', 'Respaldo probado', 'Un respaldo que nunca se restauró no es un respaldo.'),
                     ('C—02', 'Doble factor', 'En correo, banca y sistemas. Lo más barato de cerrar.'),
                     ('C—03', 'Accesos por rol', 'Cada persona ve solo lo que necesita.')],
                    top=590, gap=170)
             + footer('Lo revisamos en la Radiografía.', 'Escríbenos')))

# F09 · Apagón
feed.append(('F09 · Se va la luz 8 horas', header('Hoja 08 · Temporada seca')
             + title('Se va la luz 8 horas. ¿Qué pasa en tu <span class="o">operación?</span>', 74)
             + spec([('0 MIN', '¿Quién decide?', 'Y a quién se avisa primero.'),
                     ('30 MIN', '¿Qué va al generador?', 'Las cargas críticas, en orden.'),
                     ('2 H', '¿Cómo sigues vendiendo?', 'Despachar, facturar, atender.')],
                    top=560, gap=180)
             + footer('Si no está escrito, no es un plan.', 'Armémoslo')))

# F10 · ERP
feed.append(('F10 · Antes de comprar un ERP', header('Hoja 09 · Antes de comprar')
             + title('5 preguntas antes de comprar un <span class="o">ERP.</span>', 80)
             + spec([('?—01', '¿Tengo el proceso dibujado?', ''), ('?—02', '¿Qué problema exacto resuelve?', ''),
                     ('?—03', '¿Quién lo usará todos los días?', ''), ('?—04', '¿Cómo migro los datos?', ''),
                     ('?—05', '¿Quién cuida accesos y respaldos?', '')], top=500, gap=120, kw=130)
             + footer('A veces la respuesta es el Excel que ya tienes, bien armado.', 'Hablemos')))

# F11 · Radiografía con el dragón
feed.append(('F11 · Radiografía', header('Hoja 10 · Radiografía')
             + title('Una hora en tu empresa. <span class="o">Gratis.</span>', 88)
             + dragon_band(452, 'plano')
             + spec([('R—01', 'Un proceso clave', 'Ventas, inventario, despacho o cierre de mes.'),
                     ('R—02', 'La cuenta de horas', 'Con tus números. Si no da, te lo decimos.'),
                     ('R—03', 'Cinco puntos de seguridad', 'Respaldos, accesos y correo.')],
                    top=700, gap=146)
             + footer('Al día siguiente: qué haríamos primero.', 'Pide la tuya')))

# ---------- historias 1080×1920 (zona libre 250 px arriba y abajo) ----------
SW, SH = 1080, 1920
stories = []


def st_head(label):
    return (logo(M, 270, 62) +
            f'<div class="abs brandtxt" style="left:{M + 54}px;top:278px;font-size:36px;line-height:48px">BOUW</div>'
            f'<div class="abs mono" style="right:{M}px;top:288px;width:500px;text-align:right;font-size:22px">{e(label)}</div>'
            f'<div class="rule" style="left:{M}px;top:366px;width:{SW - 2 * M}px"></div>')


def st_cta(txt, top=1500):
    w = len(txt) * 24 + 90
    return (f'<div class="cta" style="left:{M}px;top:{top}px;width:{w}px;height:92px;font-size:32px;line-height:92px">{e(txt)}</div>'
            f'<div class="abs mono" style="left:{M}px;top:{top + 124}px;width:900px;font-size:22px">WhatsApp +593 96 368 4012</div>')


stories.append(('H01 · ¿Excel y WhatsApp?', st_head('Radiografía')
                + f'<div class="abs h" style="left:{M}px;top:430px;width:{SW - 2 * M}px;font-size:104px">¿Tu empresa vive en Excel y <span class="o">WhatsApp?</span></div>'
                + f'<img class="abs" src="{IMG["front"]}" style="left:140px;top:910px;width:800px" alt="">'
                + f'<div class="abs p" style="left:{M}px;top:1190px;width:{SW - 2 * M}px;font-size:40px;line-height:54px">Una hora en tu empresa, gratis. Al día siguiente te decimos qué haríamos primero.</div>'
                + st_cta('Escríbenos: RADIOGRAFÍA')))

opts = ''
for i, (n, w_, q) in enumerate([('1', 'Orden', '“Todo pasa por mí.”'), ('2', 'Tiempo', '“No nos alcanza el día.”'),
                                 ('3', 'Control', '“Me entero a fin de mes.”')]):
    y = 760 + i * 220
    opts += (f'<div class="panel" style="left:{M}px;top:{y}px;width:{SW - 2 * M}px;height:190px"></div>'
             f'<div class="abs h" style="left:{M + 40}px;top:{y + 30}px;width:120px;font-size:110px;line-height:130px;color:#4fd6e8">{n}</div>'
             f'<div class="abs t" style="left:{M + 190}px;top:{y + 40}px;width:680px;font-size:48px;line-height:58px">{w_}</div>'
             f'<div class="abs p" style="left:{M + 190}px;top:{y + 106}px;width:680px;font-size:32px;line-height:42px">{e(q)}</div>')
stories.append(('H02 · ¿1, 2 o 3?', st_head('Pregunta de la semana')
                + f'<div class="abs h" style="left:{M}px;top:430px;width:{SW - 2 * M}px;font-size:96px">¿Qué te quita más <span class="o">el sueño?</span></div>'
                + opts + f'<div class="abs p" style="left:{M}px;top:1440px;width:{SW - 2 * M}px;font-size:36px;color:#e8eef6">Respóndenos con el número.</div>'
                + st_cta('Responder 1, 2 o 3', top=1520)))

met2 = ''
for i, (n, lab) in enumerate([('11', 'Hojas conectadas'), ('1', 'Archivo, cero licencias'), ('0', 'Migraciones')]):
    y = 820 + i * 190
    met2 += (f'<div class="rule" style="left:{M}px;top:{y}px;width:{SW - 2 * M}px"></div>'
             f'<div class="abs h" style="left:{M}px;top:{y + 20}px;width:260px;font-size:120px;line-height:150px;color:#4fd6e8">{n}</div>'
             f'<div class="abs t" style="left:{M + 280}px;top:{y + 62}px;width:620px;font-size:40px;line-height:50px">{e(lab)}</div>')
stories.append(('H03 · Caso real', st_head('Proyecto real')
                + f'<div class="abs h" style="left:{M}px;top:430px;width:{SW - 2 * M}px;font-size:88px">El cierre de mes ahora <span class="o">sale solo.</span></div>'
                + met2 + f'<div class="abs p" style="left:{M}px;top:1400px;width:{SW - 2 * M}px;font-size:34px;line-height:46px">Taller de manufactura. Un ERP pequeño sobre su propio Excel.</div>'
                + st_cta('¿Y el tuyo? Escríbenos', top=1520)))

# ---------- portada 1640×624 y perfil 720×720 ----------
CW, CH = 1640, 624
cover = [('Portada Facebook', ''
          + f'<img class="abs" src="{IMG["d34"]}" style="left:830px;top:190px;width:540px" alt="">'
          + logo(280, 130, 52)
          + f'<div class="abs brandtxt" style="left:326px;top:136px;font-size:30px;line-height:42px">BOUW</div>'
          + f'<div class="abs h" style="left:280px;top:208px;width:560px;font-size:64px;line-height:72px">Del diseño<br><span class="o">a la realidad.</span></div>'
          + f'<div class="abs mono" style="left:280px;top:376px;width:560px;font-size:20px;line-height:30px;color:#4fd6e8">Orden · Tiempo · Control</div>'
          + f'<div class="abs mono" style="left:280px;top:414px;width:560px;font-size:18px;line-height:28px">Consultoría técnica · Quito · Monterrey</div>')]


def build(name, title_, w, h, slides):
    body = ''.join(slide(w, h, b, n) for n, b in slides)
    if name != 'bouw-fb-portada':
        # regla de marca: un solo naranja por pieza (el botón)
        body = body.replace('<span class="o">', '<span>')
    head = (f'<!doctype html><html lang="es"><head><meta charset="utf-8"><title>{e(title_)}</title>'
            f'<meta name="hz:slide-selector" content=".slide">'
            f'<meta name="hz:canvas-width" content="{w}"><meta name="hz:canvas-height" content="{h}">'
            f'{KIT}<style>{CSS}</style>')
    doc = head + '</head><body>' + body + '</body></html>'
    with open(os.path.join(OUT, name + '.html'), 'w') as f:
        f.write(doc)
    with open(os.path.join(OUT, name + '.preview.html'), 'w') as f:
        f.write(doc.replace('</head>', PREVIEW_FONTS + '</head>').replace(KIT, ''))
    print(name, len(doc) // 1024, 'KB', len(slides), 'slides')


F = dict(feed)
S1 = ['F01 · ¿Qué te quita más el sueño?', 'F02 · Del diseño a la realidad', 'F03 · Dos ingenieros']
S2 = ['F04 · Marca lo que reconozcas', 'F05 · Caso real: programa contable', 'F06 · La cuenta']
S3 = ['F07 · Plazos que se pueden escribir', 'F08 · Respaldo', 'F09 · Se va la luz 8 horas']
S4 = ['F11 · Radiografía', 'F10 · Antes de comprar un ERP']
for i, grp in enumerate([S1, S2, S3, S4], 1):
    build(f'bouw-fb-semana{i}', f'BOUW · Facebook semana {i}', W, H, [(n, F[n]) for n in grp])
build('bouw-fb-historias', 'BOUW · Historias', SW, SH, stories)
build('bouw-fb-portada', 'BOUW · Portada Facebook', CW, CH, cover)
