"""Piezas de LinkedIn de BOUW hechas con el logo y los textos de bouw-eight.vercel.app.

Logo: marca/bouw-logo-negativo.png (el mismo PNG del encabezado y del pie del sitio: BOUW en cian con el dragón blanco)
y marca/bouw-dragon-blanco.png (el dragón solo, como el ícono del sitio).
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


LOGO = b64(os.path.join(ROOT, 'marca', 'bouw-logo-negativo.png'))     # 720×304
DRAGON = b64(os.path.join(ROOT, 'marca', 'bouw-dragon-blanco.png'))   # 900×648
LOGO_R = 720 / 304
DRAGON_R = 900 / 648


def logo(x, y, w):
    """Logo del sitio (BOUW + dragón). Se da el ancho; el alto sale de la proporción 720×304."""
    return f'<img class="abs" alt="BOUW" src="{LOGO}" style="left:{x}px;top:{y}px;width:{w}px;height:{round(w / LOGO_R)}px">'


def dragon(x, y, w, op=1):
    o = f';opacity:{op}' if op != 1 else ''
    return f'<img class="abs" alt="" src="{DRAGON}" style="left:{x}px;top:{y}px;width:{w}px;height:{round(w / DRAGON_R)}px{o}">'


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


# =====================================================================
# 1. PERFIL Y PORTADAS
# =====================================================================

# 01 · Logo de la página de empresa 400×400: el dragón, igual que el ícono del sitio (se lee a 48 px).
add('01-perfil-dragon-400x400', 400, 400, dragon(30, 92, 340), step=40)

# 02 · Variante con el logo completo (BOUW + dragón)
add('02-perfil-logo-completo-400x400', 400, 400,
    logo(36, 120, 328)
    + '<div class="abs mono" style="left:0;top:286px;width:400px;text-align:center;font-size:12px;line-height:18px;letter-spacing:0.28em">Automation &amp; Digital</div>',
    step=40)

# 05 · Foto de perfil 720×720 (Facebook, Instagram, WhatsApp; se ve en círculo)
add('05-perfil-logo-720x720', 720, 720,
    logo(100, 222, 520)
    + '<div class="abs mono" style="left:0;top:472px;width:720px;text-align:center;font-size:20px;line-height:28px;letter-spacing:0.3em">Automation &amp; Digital</div>')

# 03 · Portada de la página de empresa 1128×191 (el logo de la página tapa abajo a la izquierda: el texto empieza en x=300)
add('03-portada-empresa-1128x191', 1128, 191,
    '<div class="abs mono" style="left:300px;top:34px;width:520px;font-size:12px;line-height:18px;color:#4fd6e8">Quito · Monterrey &#8212; Est. 7+</div>'
    + f'<div class="abs serif" style="left:300px;top:62px;width:560px;font-size:54px;line-height:60px">{LEMA}</div>'
    + '<div class="abs mono" style="left:300px;top:138px;width:560px;font-size:11px;line-height:18px">Ingeniería de procesos, calidad y automatización</div>'
    + logo(862, 44, 226),
    step=30)

# 04 · Banner del perfil personal 1584×396 (la foto tapa la parte izquierda: el contenido empieza en x=560)
SERV = ['Lean &amp; planta', 'Calidad &amp; BPM', 'Automatización', 'Simulación', 'Web &amp; producto']
chips = ''
x = 560
for s in SERV:
    w = int(len(html.unescape(s)) * 10.6 + 44)
    chips += f'<div class="chip" style="left:{x}px;top:316px;width:{w}px;height:40px;font-size:15px;line-height:36px">{s}</div>'
    x += w + 12
add('04-banner-perfil-personal-1584x396', 1584, 396,
    '<div class="abs mono" style="left:560px;top:52px;width:500px;font-size:14px;line-height:20px;color:#4fd6e8">Quito · Monterrey &#8212; Est. 7+</div>'
    + '<div class="abs h" style="left:560px;top:96px;width:680px;font-size:62px;line-height:66px">'
      '<span class="dim">Del dis</span>eño <span class="dim">a la rea</span><span class="c">lidad</span></div>'
    + f'<div class="abs serif" style="left:560px;top:198px;width:820px;font-size:58px;line-height:64px">{LEMA}</div>'
    + chips
    + logo(1262, 60, 270)
    + '<div class="abs mono" style="left:1262px;top:190px;width:270px;font-size:12px;line-height:20px;letter-spacing:0.24em">Automation &amp; Digital<br>Solutions</div>')

# =====================================================================
# 2. PUBLICACIONES 1080×1350
# =====================================================================
W, H, M = 1080, 1350, 84
IW = W - 2 * M


def header(n, tema, raw=False):
    return (logo(M, 62, 150)
            + f'<div class="abs mono" style="left:{W - M - 640}px;top:84px;width:640px;text-align:right;font-size:19px;line-height:28px">'
              f'{e(tema) if raw else f"Pliego {n:02d} · {e(tema)}"}</div>'
            + f'<div class="rule" style="left:{M}px;top:156px;width:{IW}px"></div>')


def footer(phrase, cta, serif=False):
    cw = int(len(cta) * 14 + 76)
    cls = 'serif' if serif else 'p'
    fs = 'font-size:36px;line-height:40px;color:#e8eef6' if serif else 'font-size:24px;line-height:32px;color:#93a7bf'
    return (f'<div class="rule" style="left:{M}px;top:1170px;width:{IW}px"></div>'
            + f'<div class="abs {cls}" style="left:{M}px;top:1206px;width:{IW - cw - 36}px;{fs}">{phrase}</div>'
            + f'<div class="btn" style="left:{W - M - cw}px;top:1206px;width:{cw}px;height:68px;font-size:24px;line-height:68px;border-radius:4px">{e(cta)}</div>'
            + f'<div class="abs mono" style="left:{M}px;top:1296px;width:{IW}px;font-size:15px;line-height:22px;color:#5d7690">bouw-eight.vercel.app · +593 96 368 4012</div>')


def kicker(t, top=206, color='#4fd6e8'):
    return (f'<div class="abs" style="left:{M}px;top:{top + 10}px;width:12px;height:12px;border-radius:6px;background:{color}"></div>'
            f'<div class="abs mono" style="left:{M + 26}px;top:{top}px;width:{IW - 26}px;font-size:19px;line-height:32px;color:{color}">{t}</div>')


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
     logo(M, 74, 380)
     + f'<div class="abs mono" style="left:{W - M - 400}px;top:96px;width:400px;text-align:right;font-size:19px;line-height:30px">Pliego 01 · Quiénes somos</div>'
     + f'<div class="abs mono" style="left:{M}px;top:296px;width:300px;font-size:19px;line-height:28px;color:#4fd6e8">Quito · Monterrey</div>'
     + dash(M + 330, 310, 150)
     + f'<div class="abs mono" style="left:{M + 510}px;top:296px;width:200px;font-size:19px;line-height:28px">Est. 7+</div>'
     + title('<span class="dim">Del dis</span>eño<br><span class="dim">a la rea</span><span class="c">lidad</span>', 128, top=352)
     + f'<div class="abs serif" style="left:{M}px;top:620px;width:{IW}px;font-size:76px;line-height:84px">{LEMA}</div>'
     + para('Automatizamos procesos y convertimos ideas de ingeniería en productos que funcionan. '
            'Llevamos más de 7 años haciéndolo entre Ecuador y México.', 752, size=31, lh=44)
     + stats([('Quito', 'Ecuador · GMT-5<br>desde 2019'), ('Monterrey', 'México · GMT-6<br>desde 2023'),
              ('7+', 'años de experiencia<br>combinada')], 920, num=56)
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
     + kicker('03 · Automatización · Gestión &#8212; En vivo')
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
     + kicker('02 · Hoy → BOUW')
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
     + para('Son frases que nos dicen los clientes cuando nos llaman. Marca las que se parezcan a tu semana.', 322, size=28, lh=40)
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
     + para('Rellena la fila con una tarea que hoy se haga a mano. Si no compensa automatizarla, también te lo dice.', 390, size=27, lh=37)
     + calc
     + footer('Haz tu cuenta en la calculadora del sitio.', 'Hacer la cuenta'))

# L09 · ¿Dónde pierde horas esta planta? (el juego del sitio)
post('L09-donde-pierde-horas',
     header(9, 'Pruébalo · 30 segundos')
     + title('¿Dónde pierde horas esta planta?', 76, top=214)
     + para('Hay seis desperdicios escondidos. Toca la planta donde veas uno y te decimos qué es, qué cuesta y cómo se ve arreglado.', 400, size=27, lh=37)
     + photo('juego-planta', M, 520, IW, 560)
     + f'<div class="abs h" style="left:{W - M - 230}px;top:1090px;width:200px;text-align:right;font-size:56px;line-height:60px">0<span class="dim">/6</span></div>'
     + f'<div class="abs mono" style="left:{M}px;top:1110px;width:600px;font-size:17px;line-height:24px">Encontrados</div>'
     + footer('Seis desperdicios. ¿Cuántos ves?', 'Pruébalo'))

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
     + f'<div class="abs serif" style="left:{M}px;top:1030px;width:{IW}px;font-size:66px;line-height:72px">{LEMA}</div>'
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
for i, (n, tag, name, desc, img, st, res, tech) in enumerate(PROY):
    car.append(header(i + 2, f'Carrusel · {i + 2} / {N}', True)
               + f'<div class="abs h" style="left:{M}px;top:196px;width:300px;font-size:120px;line-height:120px;color:#15304d">{n}</div>'
               + f'<div class="abs mono" style="left:{M + 230}px;top:214px;width:{IW - 230}px;font-size:18px;line-height:28px;color:#4fd6e8">{e(tag)}</div>'
               + f'<div class="abs h" style="left:{M + 230}px;top:250px;width:{IW - 230}px;font-size:62px;line-height:66px">{e(name)}</div>'
               + photo(img, M, 352, IW, 420)
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
    + '<div class="abs mono" style="left:628px;width:500px;top:84px;text-align:right;font-size:15px;line-height:24px">Pliego 04 · La cuenta</div>'
    + '<div class="rule" style="left:72px;top:150px;width:1056px"></div>'
    + '<div class="abs h" style="left:72px;top:190px;width:640px;font-size:68px;line-height:68px">Cuánto cuesta hacerlo a mano.</div>'
    + '<div class="abs p" style="left:72px;top:352px;width:620px;font-size:24px;line-height:34px">Rellena la fila con una tarea que hoy se haga a mano. Si no compensa automatizarla, también te lo dice.</div>'
    + '<div class="btn" style="left:72px;top:480px;width:290px;height:66px;font-size:24px;line-height:66px;border-radius:4px">Hacer la cuenta</div>'
    + '<div class="abs mono" style="left:392px;top:500px;width:400px;font-size:15px;line-height:24px;color:#4fd6e8">bouw-eight.vercel.app</div>'
    + '<div class="panel" style="left:780px;top:190px;width:348px;height:356px"></div>'
    + ''.join(f'<div class="abs p" style="left:808px;top:{214 + i * 56}px;width:200px;font-size:20px;line-height:30px">{a}</div>'
              f'<div class="abs k" style="left:1000px;top:{214 + i * 56}px;width:100px;text-align:right;font-size:22px;line-height:30px">{b}</div>'
              for i, (a, b) in enumerate([('Veces / semana', '3'), ('Minutos', '× 20'), ('Personas', '× 1'), ('Semanas', '× 48')]))
    + '<div class="abs" style="left:782px;top:440px;width:344px;height:104px;background:#0d2b48;border-radius:0 0 16px 16px"></div>'
    + '<div class="abs mono" style="left:808px;top:456px;width:200px;font-size:14px;line-height:22px">Al año</div>'
    + '<div class="abs h" style="left:808px;top:480px;width:300px;font-size:50px;line-height:54px;color:#4fd6e8">48 horas</div>')

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
