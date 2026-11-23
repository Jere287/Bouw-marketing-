"""Serie D (diseño de marca) para LinkedIn de BOUW, en el formato que usan las consultoras de la región
(investigado en la página de Hanova Consulting, Monterrey):
- fondo azul de marca, logo centrado arriba, titular grueso centrado con palabras clave en naranja;
- etiqueta de formato ("TIP DEL DÍA", "CASO REAL", "FRASE DE LA SEMANA"), carrusel numerado;
- pie con íconos (LinkedIn, WhatsApp, web) y la dirección del sitio.
Diferencias a propósito: fotos reales de los proyectos de BOUW (no robots de banco de imágenes)
y cada pieza termina en una invitación concreta a escribir.

Uso: python3 gen_marca.py && node shot_marca.js  →  png/D*.png
"""
import base64, html, io, os
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, '..'))
IMGS = os.path.join(ROOT, 'sitio', 'imagenes')
FONTS = os.path.join(ROOT, 'fonts')
OUT = os.path.join(HERE, 'html_marca')
os.makedirs(OUT, exist_ok=True)
W, H = 1080, 1350
NAVY, ROYAL, DEEP, ORANGE, CYAN, CREAM = '#0d2947', '#123a7a', '#06142b', '#f79b4a', '#4fd6e8', '#fbf6ea'
LOGO = os.path.join(ROOT, 'sitio', 'dragon', 'capturas', 'dragon-oscuro-realidad-transparente.png')
LOGO_CLARO = os.path.join(ROOT, 'sitio', 'dragon', 'capturas', 'dragon-claro-realidad-transparente.png')


def data(path, width, quality=86):
    im = Image.open(path)
    if im.width > width * 2:
        im = im.resize((width * 2, round(im.height * width * 2 / im.width)), Image.LANCZOS)
    buf = io.BytesIO()
    if im.mode in ('RGBA', 'LA', 'P') and im.convert('RGBA').getextrema()[3][0] < 250:
        im.convert('RGBA').save(buf, 'PNG', optimize=True)
        return 'data:image/png;base64,' + base64.b64encode(buf.getvalue()).decode()
    im.convert('RGB').save(buf, 'JPEG', quality=quality)
    return 'data:image/jpeg;base64,' + base64.b64encode(buf.getvalue()).decode()


def site(n):
    return os.path.join(IMGS, n + '.png')


CSS = f"""
@font-face{{font-family:"Archivo";src:url(file://{FONTS}/Archivo-100_900.woff2);font-weight:100 900;font-stretch:62% 125%}}
@font-face{{font-family:"Plex";src:url(file://{FONTS}/IBMPlexSans-400.woff2);font-weight:400}}
*{{margin:0;padding:0;box-sizing:border-box}}
.slide{{position:relative;overflow:hidden;width:{W}px;height:{H}px;font-family:"Plex",sans-serif;color:#fff}}
.abs{{position:absolute}}
.hd{{font-family:"Archivo";font-weight:800;letter-spacing:-0.02em;line-height:1.02}}
.tg{{font-family:"Archivo";font-weight:700;letter-spacing:0.08em;text-transform:uppercase}}
.tx{{font-family:"Plex";line-height:1.4}}
.o{{color:{ORANGE}}}
.c{{color:{CYAN}}}
"""

# íconos sencillos en blanco (LinkedIn, WhatsApp, web), como el pie de las piezas de consultora
IC_IN = '<path d="M7 9h3v9H7zM8.5 5.5a1.6 1.6 0 1 1 0 3.2 1.6 1.6 0 0 1 0-3.2zM12 9h2.9v1.3c.4-.8 1.4-1.5 2.9-1.5 3 0 3.6 1.9 3.6 4.5V18h-3v-4.2c0-1-.1-2.3-1.5-2.3s-1.8 1.1-1.8 2.2V18H12z"/>'
IC_WA = '<path d="M12 3.5a8.5 8.5 0 0 0-7.3 12.8L3.5 20.5l4.3-1.1A8.5 8.5 0 1 0 12 3.5zm0 1.6a6.9 6.9 0 1 1-3.6 12.8l-.3-.2-2.4.6.7-2.3-.2-.3A6.9 6.9 0 0 1 12 5.1zm-2.6 3.3c-.2 0-.5 0-.7.3-.3.3-.9.9-.9 2.1s.9 2.4 1 2.6c.1.2 1.8 2.8 4.4 3.8 2.2.9 2.6.7 3.1.6.5 0 1.5-.6 1.7-1.2.2-.6.2-1.1.2-1.2-.1-.1-.2-.2-.5-.3l-1.7-.8c-.2-.1-.4-.1-.6.1l-.8 1c-.1.2-.3.2-.5.1-.3-.1-1.1-.4-2-1.3-.8-.7-1.3-1.5-1.4-1.8-.2-.3 0-.4.1-.5l.4-.5.3-.4v-.5l-.8-1.9c-.2-.5-.4-.4-.6-.4z"/>'
IC_WEB = '<path d="M12 3.5a8.5 8.5 0 1 0 0 17 8.5 8.5 0 0 0 0-17zm5.9 7.7h-2.7a13 13 0 0 0-1-4.9 7 7 0 0 1 3.7 4.9zM12 5.1c.7 1 1.5 3 1.6 6.1h-3.2c.1-3.1.9-5.1 1.6-6.1zm-2.2.2a13 13 0 0 0-1 4.9H6.1a7 7 0 0 1 3.7-4.9zM6.1 12.8h2.7a13 13 0 0 0 1 4.9 7 7 0 0 1-3.7-4.9zm5.9 6.1c-.7-1-1.5-3-1.6-6.1h3.2c-.1 3.1-.9 5.1-1.6 6.1zm2.2-.2a13 13 0 0 0 1-4.9h2.7a7 7 0 0 1-3.7 4.9z"/>'


def icons(cx, top, color='#fff', ring='rgba(255,255,255,.9)'):
    out = ''
    for i, p in enumerate([IC_IN, IC_WA, IC_WEB]):
        x = cx - 120 + i * 84
        out += (f'<div class="abs" style="left:{x}px;top:{top}px;width:60px;height:60px;border:3px solid {ring};border-radius:30px"></div>'
                f'<svg class="abs" style="left:{x + 12}px;top:{top + 12}px" width="36" height="36" viewBox="0 0 24 24" fill="{color}">{p}</svg>')
    return out


def footer(dark=True):
    col = '#fff' if dark else NAVY
    ring = 'rgba(255,255,255,.9)' if dark else NAVY
    return (icons(W // 2 - 30, 1170, col, ring)
            + f'<div class="abs tg" style="left:0;top:1250px;width:{W}px;text-align:center;font-size:20px;letter-spacing:.12em;color:{col}">www.bouwlatam.com</div>')


def logo_top(dark=True, w=300, top=56):
    return f'<img class="abs" src="{data(LOGO if dark else LOGO_CLARO, w)}" style="left:{(W - w) // 2}px;top:{top}px;width:{w}px;height:{round(w / 1.905)}px">'


def bg_blue(pattern=True):
    dots = ''
    if pattern:
        dots = ''.join(f'<circle cx="{x}" cy="{y}" r="3"/>' for x in range(30, 300, 30) for y in range(30, 210, 30))
        dots = (f'<svg class="abs" style="left:{W - 330}px;top:{H - 470}px;opacity:.18" width="300" height="210" fill="#fff">{dots}</svg>'
                f'<svg class="abs" style="left:30px;top:250px;opacity:.12" width="300" height="210" fill="#fff">{dots}</svg>')
    return (f'<div class="abs" style="left:0;top:0;width:{W}px;height:{H}px;background:radial-gradient(120% 90% at 50% 0%,{ROYAL} 0%,{NAVY} 55%,{DEEP} 100%)"></div>'
            + dots)


def bg_photo(name, pos='center', strength=.82):
    return (f'<img class="abs" src="{data(site(name), W)}" style="left:0;top:0;width:{W}px;height:{H}px;object-fit:cover;object-position:{pos}">'
            f'<div class="abs" style="left:0;top:0;width:{W}px;height:{H}px;background:linear-gradient(180deg,rgba(13,41,71,{strength}) 0%,rgba(13,41,71,{strength - .25}) 45%,rgba(6,20,43,.95) 100%)"></div>')


def tag(t, top, color=ORANGE, center=True, left=96):
    if center:
        return (f'<div class="abs tg" style="left:0;top:{top}px;width:{W}px;text-align:center;font-size:24px;color:{color}">'
                f'<span style="display:inline-block;padding:10px 26px;border:3px solid {color};border-radius:40px">{t}</span></div>')
    return (f'<div class="abs tg" style="left:{left}px;top:{top}px;font-size:24px;color:{color}">{t}'
            f'<span style="display:inline-block;width:70px;height:3px;background:{color};margin-left:16px;vertical-align:middle"></span></div>')


def head(t, top, size=84, center=True, left=96, width=None, color='#fff'):
    width = width or (W - 2 * left)
    al = 'center' if center else 'left'
    x = (W - width) // 2 if center else left
    return f'<div class="abs hd" style="left:{x}px;top:{top}px;width:{width}px;text-align:{al};font-size:{size}px;color:{color}">{t}</div>'


def text(t, top, size=32, center=True, left=96, width=None, color='rgba(255,255,255,.88)'):
    width = width or (W - 2 * left)
    al = 'center' if center else 'left'
    x = (W - width) // 2 if center else left
    return f'<div class="abs tx" style="left:{x}px;top:{top}px;width:{width}px;text-align:{al};font-size:{size}px;color:{color}">{t}</div>'


def card(x, y, w, h, img, pos='top', radius=20):
    return (f'<img class="abs" src="{data(site(img), w)}" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;object-fit:cover;object-position:{pos};'
            f'border-radius:{radius}px;box-shadow:0 30px 70px rgba(0,0,0,.45);border:4px solid rgba(255,255,255,.9)">')


def check(y, t, x=150, col=ORANGE):
    return (f'<svg class="abs" style="left:{x}px;top:{y + 2}px" width="44" height="44" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10.5" fill="none" stroke="{col}" stroke-width="2"/>'
            f'<path d="M7 12.5l3.2 3.2L17 9" fill="none" stroke="{col}" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></svg>'
            f'<div class="abs tx" style="left:{x + 66}px;top:{y}px;width:{W - x - 66 - 110}px;font-size:32px;line-height:46px;color:#fff">{t}</div>')


pieces = []


def add(name, body):
    pieces.append((name, body))


# D01 · TIP DEL DÍA: haz la cuenta antes de comprar
add('D01-tip-haz-la-cuenta',
    bg_blue() + logo_top()
    + tag('Tip del día', 290)
    + head('Antes de comprar un sistema, <span class="o">haz la cuenta</span> de lo que te cuesta hacerlo a mano.', 380, 74)
    + f'<div class="abs" style="left:190px;top:720px;width:700px;height:250px;border-radius:24px;background:rgba(255,255,255,.07);border:2px solid rgba(255,255,255,.18)"></div>'
    + text('30 min × 5 veces por semana × 2 personas', 755, 30)
    + head('= <span class="o">240 horas</span> al año', 820, 68)
    + text('Casi un mes y medio de trabajo de una persona.', 910, 26, color='rgba(255,255,255,.7)')
    + text('¿Quieres saber la tuya? Escríbenos y la calculamos contigo.', 1040, 30)
    + footer())

# D02 · CASO REAL: −20 % de reprocesos (foto real de la línea)
add('D02-caso-reprocesos',
    bg_photo('mejora-linea-extrusion', 'center 30%', .78) + logo_top()
    + tag('Caso real', 290)
    + head('<span class="o">−20 %</span>', 380, 220)
    + head('de reprocesos en una línea de extrusión', 610, 64, width=860)
    + text('Sin comprar maquinaria nueva. Ordenamos el flujo y estandarizamos el cambio de formato.', 790, 32, width=820)
    + head('−15 % <span style="font-weight:500;font-size:34px">en tiempo de preparación</span>', 960, 54)
    + footer())

# D03 · Carrusel: 3 errores al automatizar (5 láminas)
err = [('Automatizar sin medir primero.', 'Si no sabes cuánto tarda hoy, nunca sabrás cuánto ganaste.'),
       ('Comprar otro sistema cuando el problema es el flujo.', 'Muchas veces el Excel que ya usas basta si está bien hecho.'),
       ('Automatizar lo que no se repite.', 'Menos de 40 horas al año no lo justifica. Te lo decimos aunque no nos convenga.')]
add('D03-carrusel-1-portada',
    f'<div class="abs" style="left:0;top:0;width:{W}px;height:{H}px;background:{CREAM}"></div>'
    + f'<div class="abs" style="left:0;top:0;width:{W}px;height:330px;background:{NAVY}"></div>'
    + logo_top(True, 280, 70)
    + f'<div class="abs hd" style="left:0;top:430px;width:{W}px;text-align:center;font-size:300px;line-height:1;color:{ORANGE}">3</div>'
    + head('errores al automatizar tu empresa', 750, 80, color=NAVY, width=820)
    + text('y cómo evitarlos', 1035, 40, color=NAVY)
    + f'<div class="abs tg" style="left:0;top:1170px;width:{W}px;text-align:center;font-size:26px;color:{NAVY}">Desliza →</div>'
    + f'<div class="abs tg" style="left:0;top:1250px;width:{W}px;text-align:center;font-size:20px;letter-spacing:.12em;color:{NAVY}">www.bouwlatam.com</div>')
for i, (t, d) in enumerate(err, 1):
    add(f'D03-carrusel-{i + 1}-error-{i}',
        f'<div class="abs" style="left:0;top:0;width:{W}px;height:{H}px;background:{CREAM}"></div>'
        + logo_top(False, 230, 60)
        + f'<div class="abs" style="left:110px;top:300px;width:860px;height:720px;border-radius:32px;background:{NAVY}"></div>'
        + f'<div class="abs tg" style="left:0;top:350px;width:{W}px;text-align:center;font-size:30px;color:{ORANGE}">Error {i:02d}</div>'
        + head(t, 440, 70, width=740)
        + f'<div class="abs" style="left:490px;top:740px;width:100px;height:4px;background:{ORANGE}"></div>'
        + text(d, 790, 34, width=700)
        + f'<div class="abs tg" style="left:0;top:1170px;width:{W}px;text-align:center;font-size:26px;color:{NAVY}">{i + 1} / 5</div>'
        + f'<div class="abs tg" style="left:0;top:1250px;width:{W}px;text-align:center;font-size:20px;letter-spacing:.12em;color:{NAVY}">www.bouwlatam.com</div>')
add('D03-carrusel-5-cierre',
    bg_blue() + logo_top()
    + head('¿Te pasa alguno de estos tres?', 380, 80, width=860)
    + text('Escríbenos por mensaje o WhatsApp. En una llamada de 20 minutos te decimos qué haríamos primero y si de verdad vale la pena.', 600, 34, width=820)
    + head('<span class="o">+593 96 368 4012</span>', 860, 64)
    + footer())

# D04 · FRASE DE LA SEMANA
add('D04-frase-si-se-repite',
    bg_photo('mejora-perfil-seccion', 'center', .7) + logo_top()
    + tag('Frase de la semana', 290)
    + head('Si se repite,<br><span class="o">se automatiza.</span>', 470, 120)
    + text('Si no se repite, se ordena. Y si no se mide, todavía no se toca.', 800, 36, width=820)
    + footer())

# D05 · CASO REAL: Programa contable
add('D05-caso-cierre-de-mes',
    bg_blue() + logo_top()
    + tag('Caso real', 290)
    + head('El cierre de mes que se armaba <span class="o">a mano</span>, ahora sale solo.', 370, 66, width=900)
    + card(140, 610, 800, 420, 'contable-excel-es-poster')
    + text('Un ERP dentro de un solo Excel. 11 hojas conectadas, 0 licencias.', 1070, 28, width=900)
    + footer())

# D06 · PREGUNTA: auditoría
add('D06-pregunta-auditoria',
    bg_blue() + logo_top()
    + tag('Pregunta incómoda', 290)
    + head('¿Tu planta pasaría una auditoría <span class="o">mañana</span>?', 380, 84, width=880)
    + check(650, 'Cada registro tiene su sitio y su responsable')
    + check(750, 'Rastreas un lote hasta su materia prima en minutos')
    + check(850, 'Las desviaciones se cierran y no vuelven')
    + text('Si dudaste en alguna, escríbenos. El diagnóstico de calidad es gratis.', 990, 30, width=840)
    + footer())

# D07 · CASO REAL: Charms Ecuador
add('D07-caso-whatsapp',
    bg_blue() + logo_top()
    + tag('Caso real', 290)
    + head('Tus clientes llegan a WhatsApp con el pedido <span class="o">ya escrito</span>.', 370, 64, width=900)
    + ''.join(card(150 + i * 270, 600, 240, 460, n, radius=26) for i, n in enumerate(['charms-movil-inicio', 'charms-movil-cotizar', 'charms-movil-pedidos']))
    + text('Catálogo y cotizador para un taller de regalos. $0 al mes de hosting.', 1095, 26, width=900, color='rgba(255,255,255,.8)')
    + footer())

# D08 · TIP: una sola fuente de datos
add('D08-tip-tres-archivos',
    bg_blue() + logo_top()
    + tag('Tip del día', 290)
    + head('Si tienes <span class="o">ventas_final_v2.xlsx</span>, tienes un problema.', 380, 72, width=900)
    + text('La misma información en tres archivos nunca cuadra. Y en cada reunión alguien trae un número distinto.', 640, 34, width=820)
    + text('La solución no siempre es un sistema nuevo: a veces es <b style="color:#fff">un solo archivo bien conectado</b>.', 820, 34, width=820)
    + text('¿Te pasa? Escríbenos.', 1020, 32, color=ORANGE)
    + footer())

# D09 · CÓMO TRABAJAMOS
st = [('01', 'Diagnóstico', '1 a 2 semanas'), ('02', 'Precio cerrado', '3 a 5 días'), ('03', 'Entrega semanal', '4 a 10 semanas'), ('04', 'Acompañamiento', '30 días')]
rows = ''
for i, (n, t, p) in enumerate(st):
    y = 560 + i * 120
    rows += (f'<div class="abs" style="left:150px;top:{y}px;width:780px;height:96px;border-radius:18px;background:rgba(255,255,255,.08);border:2px solid rgba(255,255,255,.16)"></div>'
             f'<div class="abs hd" style="left:180px;top:{y + 22}px;width:80px;font-size:44px;color:{ORANGE}">{n}</div>'
             f'<div class="abs hd" style="left:280px;top:{y + 26}px;width:400px;font-size:38px;font-weight:700">{t}</div>'
             f'<div class="abs tx" style="left:600px;top:{y + 30}px;width:300px;text-align:right;font-size:28px;color:{CYAN}">{p}</div>')
add('D09-como-trabajamos',
    bg_blue() + logo_top()
    + tag('Cómo trabajamos', 290)
    + head('Plazo y precio <span class="o">por escrito</span>, antes de empezar.', 370, 70, width=880)
    + rows
    + footer())

# D10 · Llamado final
add('D10-cuentanos',
    bg_photo('mejora-termometro', 'center 35%', .9) + logo_top()
    + head('¿Qué proceso te está costando <span class="o">horas</span>?', 380, 80, width=940)
    + text('Cuéntanos en dos líneas qué se hace, cada cuánto y quién lo hace. Te respondemos en menos de 24 horas con lo que haríamos primero.', 700, 34, width=840)
    + head('WhatsApp <span class="o">+593 96 368 4012</span>', 930, 52)
    + footer())

for name, body in pieces:
    open(os.path.join(OUT, name + '.html'), 'w').write(
        f'<!doctype html><html lang="es"><head><meta charset="utf-8"><style>{CSS}</style></head><body><section class="slide">{body}</section></body></html>')
open(os.path.join(OUT, 'list.txt'), 'w').write('\n'.join(f'{n}:{W}x{H}' for n, _ in pieces))
print(len(pieces), 'piezas')
