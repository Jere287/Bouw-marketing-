"""Serie A (automatización) para LinkedIn de BOUW: mismo lenguaje de consultora que la serie D
(logo arriba, titular grueso, etiqueta de formato, pie con íconos), pero jugando con color y composición
para que el feed no se vea lineal: fondos naranja, cian, crema y azul, bloques partidos, antes/después,
mito/realidad, semáforo, chat y carrusel.

Uso: python3 gen_auto.py && node shot_auto.js  →  png/A1*.png
"""
import base64, io, os
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, '..'))
IMGS = os.path.join(ROOT, 'sitio', 'imagenes')
FONTS = os.path.join(ROOT, 'fonts')
OUT = os.path.join(HERE, 'html_auto')
os.makedirs(OUT, exist_ok=True)
W, H = 1080, 1350
NAVY, ROYAL, DEEP = '#0d2947', '#123a7a', '#06142b'
ORANGE, ORANGE_D, CYAN, CYAN_D, CREAM, YELLOW, GREEN, RED = '#f79b4a', '#e2731f', '#4fd6e8', '#1a97b3', '#fbf6ea', '#ffe9a8', '#3ccf8e', '#ff6b5e'
LOGO = os.path.join(ROOT, 'sitio', 'dragon', 'capturas', 'dragon-oscuro-realidad-transparente.png')
_cache = {}


def data(path, width, quality=86):
    k = (path, width)
    if k in _cache:
        return _cache[k]
    im = Image.open(path)
    if im.width > width * 2:
        im = im.resize((width * 2, round(im.height * width * 2 / im.width)), Image.LANCZOS)
    buf = io.BytesIO()
    if im.mode in ('RGBA', 'LA', 'P') and im.convert('RGBA').getextrema()[3][0] < 250:
        im.convert('RGBA').save(buf, 'PNG', optimize=True)
        r = 'data:image/png;base64,' + base64.b64encode(buf.getvalue()).decode()
    else:
        im.convert('RGB').save(buf, 'JPEG', quality=quality)
        r = 'data:image/jpeg;base64,' + base64.b64encode(buf.getvalue()).decode()
    _cache[k] = r
    return r


def logo_solid(color):
    """El logo del sitio (dragón + BOUW) en un solo color, para fondos naranja, cian o crema."""
    k = ('solid', color)
    if k in _cache:
        return _cache[k]
    im = Image.open(LOGO).convert('RGBA')
    im = im.resize((640, round(im.height * 640 / im.width)), Image.LANCZOS)
    rgb = tuple(int(color[i:i + 2], 16) for i in (1, 3, 5))
    solid = Image.new('RGBA', im.size, rgb + (0,))
    solid.putalpha(im.getchannel('A'))
    buf = io.BytesIO()
    solid.save(buf, 'PNG', optimize=True)
    _cache[k] = 'data:image/png;base64,' + base64.b64encode(buf.getvalue()).decode()
    return _cache[k]


def site(n):
    return os.path.join(IMGS, n + '.png')


CSS = f"""
@font-face{{font-family:"Archivo";src:url(file://{FONTS}/Archivo-100_900.woff2);font-weight:100 900;font-stretch:62% 125%}}
@font-face{{font-family:"Plex";src:url(file://{FONTS}/IBMPlexSans-400.woff2);font-weight:400}}
@font-face{{font-family:"PlexMono";src:url(file://{FONTS}/IBMPlexMono-500.woff2);font-weight:500}}
*{{margin:0;padding:0;box-sizing:border-box}}
.slide{{position:relative;overflow:hidden;width:{W}px;height:{H}px;font-family:"Plex",sans-serif;color:#fff}}
.abs{{position:absolute}}
.hd{{font-family:"Archivo";font-weight:800;letter-spacing:-0.02em;line-height:1.02}}
.tg{{font-family:"Archivo";font-weight:700;letter-spacing:0.08em;text-transform:uppercase}}
.tx{{font-family:"Plex";line-height:1.4}}
.mn{{font-family:"PlexMono";font-weight:500}}
"""

IC = ['<path d="M7 9h3v9H7zM8.5 5.5a1.6 1.6 0 1 1 0 3.2 1.6 1.6 0 0 1 0-3.2zM12 9h2.9v1.3c.4-.8 1.4-1.5 2.9-1.5 3 0 3.6 1.9 3.6 4.5V18h-3v-4.2c0-1-.1-2.3-1.5-2.3s-1.8 1.1-1.8 2.2V18H12z"/>',
      '<path d="M12 3.5a8.5 8.5 0 0 0-7.3 12.8L3.5 20.5l4.3-1.1A8.5 8.5 0 1 0 12 3.5zm0 1.6a6.9 6.9 0 1 1-3.6 12.8l-.3-.2-2.4.6.7-2.3-.2-.3A6.9 6.9 0 0 1 12 5.1zm-2.6 3.3c-.2 0-.5 0-.7.3-.3.3-.9.9-.9 2.1s.9 2.4 1 2.6c.1.2 1.8 2.8 4.4 3.8 2.2.9 2.6.7 3.1.6.5 0 1.5-.6 1.7-1.2.2-.6.2-1.1.2-1.2-.1-.1-.2-.2-.5-.3l-1.7-.8c-.2-.1-.4-.1-.6.1l-.8 1c-.1.2-.3.2-.5.1-.3-.1-1.1-.4-2-1.3-.8-.7-1.3-1.5-1.4-1.8-.2-.3 0-.4.1-.5l.4-.5.3-.4v-.5l-.8-1.9c-.2-.5-.4-.4-.6-.4z"/>',
      '<path d="M12 3.5a8.5 8.5 0 1 0 0 17 8.5 8.5 0 0 0 0-17zm5.9 7.7h-2.7a13 13 0 0 0-1-4.9 7 7 0 0 1 3.7 4.9zM12 5.1c.7 1 1.5 3 1.6 6.1h-3.2c.1-3.1.9-5.1 1.6-6.1zm-2.2.2a13 13 0 0 0-1 4.9H6.1a7 7 0 0 1 3.7-4.9zM6.1 12.8h2.7a13 13 0 0 0 1 4.9 7 7 0 0 1-3.7-4.9zm5.9 6.1c-.7-1-1.5-3-1.6-6.1h3.2c-.1 3.1-.9 5.1-1.6 6.1zm2.2-.2a13 13 0 0 0 1-4.9h2.7a7 7 0 0 1-3.7 4.9z"/>']


def footer(col='#fff', top=1170):
    out = ''
    for i, p in enumerate(IC):
        x = W // 2 - 150 + i * 84
        out += (f'<div class="abs" style="left:{x}px;top:{top}px;width:60px;height:60px;border:3px solid {col};border-radius:30px"></div>'
                f'<svg class="abs" style="left:{x + 12}px;top:{top + 12}px" width="36" height="36" viewBox="0 0 24 24" fill="{col}">{p}</svg>')
    return out + f'<div class="abs tg" style="left:0;top:{top + 80}px;width:{W}px;text-align:center;font-size:20px;letter-spacing:.12em;color:{col}">bouw-eight.vercel.app</div>'


def logo(top=56, w=280, solid=None, left=None):
    src = logo_solid(solid) if solid else data(LOGO, w)
    x = (W - w) // 2 if left is None else left
    return f'<img class="abs" src="{src}" style="left:{x}px;top:{top}px;width:{w}px;height:{round(w / 1.905)}px">'


def tag(t, top, color, bg='transparent', left=None):
    pos = f'left:0;width:{W}px;text-align:center' if left is None else f'left:{left}px'
    return (f'<div class="abs tg" style="{pos};top:{top}px;font-size:24px;color:{color}">'
            f'<span style="display:inline-block;padding:10px 26px;border:3px solid {color};border-radius:40px;background:{bg}">{t}</span></div>')


def head(t, top, size=84, color='#fff', width=900, left=None, align='center'):
    x = (W - width) // 2 if left is None else left
    return f'<div class="abs hd" style="left:{x}px;top:{top}px;width:{width}px;text-align:{align};font-size:{size}px;color:{color}">{t}</div>'


def text(t, top, size=32, color='#fff', width=860, left=None, align='center', weight=400):
    x = (W - width) // 2 if left is None else left
    return f'<div class="abs tx" style="left:{x}px;top:{top}px;width:{width}px;text-align:{align};font-size:{size}px;color:{color};font-weight:{weight}">{t}</div>'


def fill(color):
    return f'<div class="abs" style="left:0;top:0;width:{W}px;height:{H}px;background:{color}"></div>'


def blue():
    return f'<div class="abs" style="left:0;top:0;width:{W}px;height:{H}px;background:radial-gradient(120% 90% at 50% 0%,{ROYAL} 0%,{NAVY} 55%,{DEEP} 100%)"></div>'


def dots(x, y, color, op=.25, cols=9, rows=6):
    d = ''.join(f'<circle cx="{15 + i * 30}" cy="{15 + j * 30}" r="3"/>' for i in range(cols) for j in range(rows))
    return f'<svg class="abs" style="left:{x}px;top:{y}px;opacity:{op}" width="{cols * 30}" height="{rows * 30}" fill="{color}">{d}</svg>'


def shot(img, x, y, w, h, pos='top', r=20, border='#fff'):
    return (f'<img class="abs" src="{data(site(img), w)}" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;object-fit:cover;object-position:{pos};'
            f'border-radius:{r}px;box-shadow:0 30px 70px rgba(0,0,0,.35);border:4px solid {border}">')


def pill(x, y, w, h, t, bg, col, size=28, r=16):
    return (f'<div class="abs" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;border-radius:{r}px;background:{bg}"></div>'
            f'<div class="abs tx" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;display:flex;align-items:center;justify-content:center;text-align:center;font-size:{size}px;line-height:1.2;color:{col};padding:0 16px">{t}</div>')


pieces = []


def add(name, body):
    pieces.append((name, body))


# A11 · Fondo naranja: lo que tu equipo hace a mano cada lunes
tasks = ['Armar el reporte de ventas de la semana', 'Pasar pedidos de WhatsApp a un Excel', 'Actualizar el inventario a mano',
         'Recordar a clientes los pagos pendientes', 'Copiar datos de un sistema a otro']
rows = ''.join(
    f'<div class="abs" style="left:110px;top:{560 + i * 104}px;width:860px;height:84px;border-radius:16px;background:rgba(255,255,255,.96)"></div>'
    f'<div class="abs hd" style="left:140px;top:{576 + i * 104}px;width:60px;font-size:44px;color:{ORANGE_D}">{i + 1}</div>'
    f'<div class="abs tx" style="left:210px;top:{584 + i * 104}px;width:740px;font-size:30px;color:{NAVY}">{t}</div>'
    for i, t in enumerate(tasks))
add('A11-lunes-a-mano',
    fill(ORANGE) + dots(780, 60, '#fff', .35) + dots(40, 1080, '#fff', .3, 6, 3)
    + logo(solid='#ffffff')
    + head('5 cosas que tu equipo hace <span style="color:' + NAVY + '">a mano</span> cada lunes', 300, 74, width=900)
    + rows
    + text('Todas se pueden automatizar. ¿Cuál te quita más horas?', 1100, 30, color=NAVY, weight=400)
    + footer(NAVY, 1180).replace(f'top:{1180 + 80}px', 'top:1262px'))

# A12 · Antes / Después partido en dos colores: cotizar
pasos_antes = ['Leer el mensaje', 'Buscar el precio', 'Calcular', 'Escribir la cotización', 'Enviar', 'Esperar respuesta']
antes = ''.join(pill(80 + (i % 3) * 312, 300 + (i // 3) * 100, 290, 76, t, 'rgba(13,41,71,.08)', NAVY, 25) for i, t in enumerate(pasos_antes))
add('A12-antes-despues-cotizar',
    fill(CREAM)
    + f'<div class="abs" style="left:0;top:640px;width:{W}px;height:{H - 640}px;background:{NAVY}"></div>'
    + logo(36, 200, solid=NAVY, left=80)
    + tag('Antes', 60, ORANGE_D, left=W - 260)
    + head('Cotizar a mano: <span style="color:' + ORANGE_D + '">6 pasos</span> por cliente', 170, 52, color=NAVY, width=920, left=80, align='left')
    + antes
    + text('Y se repite con cada cliente, todos los días.', 530, 28, color=NAVY, width=920, left=80, align='left')
    + tag('Después', 700, CYAN, left=80)
    + head('El cliente elige y el pedido <span style="color:' + CYAN + '">llega escrito</span>.', 800, 66, width=920, left=80, align='left')
    + pill(80, 990, 920, 90, 'Pieza ✓ &nbsp; Detalles ✓ &nbsp; Precio estimado ✓ &nbsp;→ &nbsp;solo confirmas', 'rgba(79,214,232,.14)', '#fff', 30)
    + footer('#fff', 1150).replace('top:1230px', 'top:1232px'))

# A13 · Cian a todo color: 240 horas
add('A13-240-horas',
    fill(CYAN) + dots(40, 60, NAVY, .18) + dots(770, 1000, NAVY, .18, 9, 4)
    + logo(solid=NAVY)
    + tag('La cuenta', 290, NAVY)
    + head('240', 360, 330, color=NAVY)
    + head('horas al año', 690, 84, color=NAVY)
    + text('es lo que suma copiar datos media hora, cinco veces por semana, entre dos personas.', 820, 34, color=NAVY, width=840)
    + text('<b>Casi un mes y medio de trabajo de una persona.</b>', 960, 32, color=NAVY)
    + footer(NAVY))

# A14 · Mito / Realidad partido en diagonal (naranja y azul)
add('A14-mito-realidad',
    blue()
    + f'<div class="abs" style="left:0;top:0;width:{W}px;height:{H}px;background:{ORANGE};clip-path:polygon(0 0,100% 0,100% 44%,0 56%)"></div>'
    + logo(40, 230, solid='#ffffff')
    + tag('Mito', 230, '#fff', left=96)
    + head('“Automatizar es caro y necesito un sistema nuevo.”', 320, 64, color='#fff', width=880, left=96, align='left')
    + tag('Realidad', 800, CYAN, left=96)
    + head('Muchas veces basta con <span style="color:' + CYAN + '">el Excel que ya usas</span>, bien conectado.', 890, 58, width=880, left=96, align='left')
    + text('Así lo hicimos en un taller: 11 hojas conectadas, 0 licencias nuevas.', 1080, 26, color='rgba(255,255,255,.75)', width=880, left=96, align='left')
    + footer('#fff', 1170))

# A15 · Semáforo: ¿vale la pena automatizarlo?
sem = [(RED, 'Menos de 40 h al año', 'No lo automatices. Cuesta más de lo que ahorra.'),
       ('#f2c94c', 'De 40 a 150 h al año', 'Está en la frontera. Vale si además te cuesta errores.'),
       (GREEN, 'Más de 150 h al año', 'Aquí sí. Es casi un mes de trabajo de una persona.')]
semr = ''
for i, (c, t, d) in enumerate(sem):
    y = 560 + i * 180
    semr += (f'<div class="abs" style="left:110px;top:{y}px;width:860px;height:156px;border-radius:24px;background:#fff;box-shadow:0 14px 40px rgba(13,41,71,.10)"></div>'
             f'<div class="abs" style="left:140px;top:{y + 38}px;width:80px;height:80px;border-radius:40px;background:{c}"></div>'
             f'<div class="abs hd" style="left:250px;top:{y + 30}px;width:680px;font-size:38px;color:{NAVY}">{t}</div>'
             f'<div class="abs tx" style="left:250px;top:{y + 86}px;width:690px;font-size:26px;color:#4a5b70">{d}</div>')
add('A15-semaforo',
    fill(CREAM) + dots(800, 70, NAVY, .12)
    + logo(solid=NAVY)
    + tag('¿Vale la pena?', 290, ORANGE_D)
    + head('No todo hay que <span style="color:' + ORANGE_D + '">automatizarlo</span>.', 370, 78, color=NAVY)
    + semr
    + footer(NAVY, 1140).replace('top:1220px', 'top:1222px'))

# A16 · Chat de WhatsApp: el pedido llega escrito
def bubble(y, t, me=False, h=None):
    x = 520 if me else 110
    bg = '#dcf8c6' if me else '#fff'
    return (f'<div class="abs" style="left:{x}px;top:{y}px;width:450px;border-radius:22px;background:{bg};padding:22px 26px;'
            f'box-shadow:0 8px 20px rgba(0,0,0,.18);font-family:Plex;font-size:27px;line-height:1.35;color:#1a1a1a">{t}</div>')
add('A16-chat-whatsapp',
    blue() + dots(780, 70, CYAN, .25)
    + logo()
    + tag('Así llega un pedido', 290, ORANGE)
    + bubble(390, 'Hola, quiero cotizar:<br>• <b>Cuadro columpio</b>, 2 figuras<br>• Frase: "Siempre juntos"<br>• Entrega: 12 dic', me=False)
    + f'<div class="abs tx" style="left:110px;top:640px;width:450px;font-size:22px;color:rgba(255,255,255,.6)">Ejemplo de pedido enviado desde la web</div>'
    + bubble(700, '¡Listo! Lo tenemos para el 12. Te paso los datos de pago 👍', me=True)
    + head('Sin veinte mensajes de ida y vuelta.', 900, 62, width=880)
    + text('Web con cotizador que entrega el pedido escrito a tu WhatsApp. ¿Vendes por chat? Escríbenos.', 1030, 28, color='rgba(255,255,255,.85)', width=860)
    + footer('#fff', 1160).replace('top:1240px', 'top:1242px'))

# A17 · El reporte del lunes llega solo (crema + captura real)
add('A17-reporte-del-lunes',
    fill(CREAM)
    + f'<div class="abs" style="left:0;top:{H - 470}px;width:{W}px;height:470px;background:{ORANGE}"></div>'
    + logo(solid=NAVY)
    + tag('Automatización', 290, NAVY)
    + head('El reporte que alguien arma cada lunes puede <span style="color:' + ORANGE_D + '">llegar solo</span>.', 370, 66, color=NAVY, width=900)
    + shot('contable-excel-es-poster', 160, 620, 760, 470, border='#fff')
    + text('Tablero que se recalcula con cada movimiento.', 1110, 28, color=NAVY, weight=400)
    + footer(NAVY, 1170))

# A18 · Carrusel: 5 tareas que puedes automatizar este mes (7 láminas, cada una de un color)
car = [(ORANGE, NAVY, '#ffffff', 'Reportes semanales', 'Se arman solos con los datos que ya capturas.', '01'),
       (CYAN, NAVY, NAVY, 'Cotizaciones', 'El cliente elige y la cotización sale calculada.', '02'),
       (CREAM, NAVY, NAVY, 'Inventario', 'Cada venta descuenta sola; avisa cuando falta material.', '03'),
       (NAVY, '#ffffff', None, 'Cobranza', 'Recordatorios de pago que salen solos en la fecha.', '04'),
       (YELLOW, NAVY, NAVY, 'Cierre de mes', 'Sale de los movimientos del mes, sin juntar archivos.', '05')]
add('A18-carrusel-1-portada',
    blue() + dots(40, 300, CYAN, .2) + dots(780, 1000, ORANGE, .3, 9, 4)
    + logo()
    + head('<span style="color:' + ORANGE + ';font-size:320px;line-height:1">5</span>', 330, 320)
    + head('tareas que puedes <span style="color:' + CYAN + '">automatizar</span> este mes', 680, 82, width=880)
    + text('sin comprar un sistema nuevo', 920, 36, color='rgba(255,255,255,.85)')
    + text('Desliza →', 1100, 30, color=ORANGE, weight=400)
    + footer('#fff', 1170))
for i, (bg, fg, lg, t, d, n) in enumerate(car):
    add(f'A18-carrusel-{i + 2}-{n}',
        (blue() if bg == NAVY else fill(bg)) + dots(780, 60, fg, .2)
        + (logo() if lg is None else logo(solid=lg))
        + f'<div class="abs hd" style="left:0;top:290px;width:{W}px;text-align:center;font-size:260px;line-height:1;color:{ {NAVY: ORANGE, CREAM: ORANGE, CYAN: '#ffffff', YELLOW: ORANGE_D}.get(bg, NAVY) };opacity:.95">{n}</div>'
        + head(t, 600, 96, color=fg)
        + f'<div class="abs" style="left:490px;top:740px;width:100px;height:6px;background:{fg};opacity:.6"></div>'
        + text(d, 790, 38, color=fg, width=800)
        + text(f'{i + 2} / 7', 1100, 26, color=fg)
        + footer(fg, 1170))
add('A18-carrusel-7-cierre',
    fill(ORANGE) + dots(40, 300, '#fff', .3)
    + logo(solid='#ffffff')
    + head('¿Cuál de las cinco te quita más horas?', 330, 84, color=NAVY, width=880)
    + text('Escríbenos el número por mensaje o WhatsApp. Te decimos en una llamada de 20 minutos cómo lo haríamos y cuánto tardaría.', 620, 34, color=NAVY, width=840)
    + head('+593 96 368 4012', 900, 70, color='#fff')
    + footer(NAVY, 1170))

for name, body in pieces:
    open(os.path.join(OUT, name + '.html'), 'w').write(
        f'<!doctype html><html lang="es"><head><meta charset="utf-8"><style>{CSS}</style></head><body><section class="slide">{body}</section></body></html>')
open(os.path.join(OUT, 'list.txt'), 'w').write('\n'.join(f'{n}:{W}x{H}' for n, _ in pieces))
print(len(pieces), 'piezas')
