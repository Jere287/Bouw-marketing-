"""Piezas de LinkedIn de BOUW con el logo oficial del sitio (public/logo-bouw.svg de bouw-eight.vercel.app).

Genera html/<pieza>.html (una pieza por archivo) y luego shot.js las pasa a png/.
Todo el contenido sale del sitio: lema, descriptor, sedes, los 4 campos con sus plazos,
la Radiografía, la calculadora "la cuenta" y la voz honesta ("si el número no da, te lo decimos").
"""
import html, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'html')
os.makedirs(OUT, exist_ok=True)
FONTS = os.path.normpath(os.path.join(HERE, '..', 'fonts'))

# ---------- logo oficial (mismo archivo que usa el sitio) ----------
_LOGO = open(os.path.join(HERE, '..', 'logo-bouw.svg')).read()
_LOGO = _LOGO[_LOGO.index('<defs>'):_LOGO.rindex('</svg>')]
_LOGO = re.sub(r'>\s+<', '><', _LOGO).strip()
_n = [0]


def logo(x, y, h):
    """Logo oficial con sus degradados. Cada copia lleva ids propios para no chocar en la misma página."""
    _n[0] += 1
    k = f'l{_n[0]}'
    body = re.sub(r'id="(\w+)"', lambda m: f'id="{k}{m.group(1)}"', _LOGO)
    body = re.sub(r'url\(#(\w+)\)', lambda m: f'url(#{k}{m.group(1)})', body)
    w = round(h * 3.95 / 6.3)
    return (f'<svg class="abs" style="left:{x}px;top:{y}px" width="{w}" height="{h}" '
            f'viewBox="-2 -3.15 3.95 6.3" xmlns="http://www.w3.org/2000/svg">{body}</svg>')


def lw(h):
    return round(h * 3.95 / 6.3)


CSS = f"""
@font-face{{font-family:"Archivo";src:url(file://{FONTS}/Archivo-100_900.woff2);font-weight:100 900;font-stretch:62% 125%}}
@font-face{{font-family:"Plex";src:url(file://{FONTS}/IBMPlexSans-400.woff2);font-weight:100 700}}
@font-face{{font-family:"PlexMono";src:url(file://{FONTS}/IBMPlexMono-500.woff2);font-weight:500}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{background:#04101f}}
.slide{{position:relative;overflow:hidden;background:#04101f;color:#e8eef6;font-family:"Plex",sans-serif}}
.abs{{position:absolute}}
.h{{font-family:"Archivo";font-stretch:125%;font-weight:800;letter-spacing:-0.02em;line-height:1.04;color:#e8eef6}}
.o{{color:#e87722}}
.c{{color:#4fd6e8}}
.mono{{font-family:"PlexMono";font-weight:500;text-transform:uppercase;letter-spacing:0.14em;color:#8fa8c4}}
.k{{font-family:"PlexMono";font-weight:500;color:#4fd6e8}}
.t{{font-family:"Archivo";font-stretch:125%;font-weight:800;color:#e8eef6;letter-spacing:-0.01em}}
.p{{font-family:"Plex";font-weight:400;color:#c6d4e4;line-height:1.35}}
.rule{{position:absolute;height:2px;background:#17406b}}
.crule{{position:absolute;height:2px;background:#22b5cf}}
.panel{{position:absolute;background:#071a2f;border:2px solid #17406b}}
.cta{{position:absolute;background:#e87722;color:#04101f;font-family:"Archivo";font-stretch:125%;font-weight:800;text-align:center}}
.brand{{font-family:"Archivo";font-stretch:125%;font-weight:800;color:#e8eef6;letter-spacing:0.02em}}
"""


def e(s):
    return html.escape(s, quote=False)


def grid(w, h, step=60, marks=True, D=36, L=34):
    d = ''.join(f'M{x} 0V{h}' for x in range(step, w, step)) + ''.join(f'M0 {y}H{w}' for y in range(step, h, step))
    m = ''
    if marks:
        m = ''.join(f'M{x} {y + sy * L}V{y}H{x + sx * L}' for x, y, sx, sy in
                    [(D, D, 1, 1), (w - D, D, -1, 1), (D, h - D, 1, -1), (w - D, h - D, -1, -1)])
        m = f'<path d="{m}" fill="none" stroke="#4fd6e8" stroke-width="3"/>'
    return (f'<svg class="abs" style="left:0;top:0" width="{w}" height="{h}" viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg">'
            f'<path d="{d}" fill="none" stroke="#4fd6e8" stroke-opacity="0.07" stroke-width="2"/>{m}</svg>')


pieces = []  # (archivo, w, h, cuerpo)


def add(name, w, h, body, step=60, marks=True, D=36, L=34):
    pieces.append((name, w, h, grid(w, h, step, marks, D, L) + body))


# =====================================================================
# 1. PERFIL Y PORTADAS
# =====================================================================

# Logo de perfil 400×400 (página de empresa y foto de perfil). Solo el símbolo: se lee a 48 px.
add('01-perfil-logo-400x400', 400, 400,
    logo((400 - lw(260)) // 2, 70, 260), step=40, D=22, L=22)

# Variante con el nombre (para la página de empresa, donde el logo se ve cuadrado)
add('02-perfil-logo-nombre-400x400', 400, 400,
    logo(150, 58, 160)
    + '<div class="abs brand" style="left:0;top:248px;width:400px;text-align:center;font-size:52px;line-height:60px">BOUW</div>'
    + '<div class="abs mono" style="left:0;top:318px;width:400px;text-align:center;font-size:14px;line-height:20px;color:#4fd6e8">Del diseño a la realidad</div>',
    step=40, D=22, L=22)

# Foto de perfil de Facebook / Instagram / WhatsApp 720×720 (se ve en círculo: el logo va centrado y con aire)
add('05-perfil-facebook-720x720', 720, 720,
    logo((720 - lw(440)) // 2, 140, 440), step=60, D=40, L=40)

# Portada de la página de empresa 1128×191
CAMPOS = ['Mejora de procesos', 'Sistemas de calidad', 'Automatización', 'Diseño a producto']
add('03-portada-empresa-1128x191', 1128, 191,
    # El logo de la página de empresa tapa la esquina inferior izquierda: el contenido va de x=300 en adelante
    '<div class="abs h" style="left:300px;top:38px;width:780px;font-size:42px;line-height:48px">Del diseño <span class="o">a la realidad.</span></div>'
    + '<div class="crule" style="left:300px;top:104px;width:770px"></div>'
    + '<div class="abs k" style="left:300px;top:116px;width:800px;font-size:15px;line-height:22px;letter-spacing:0.04em">'
    + ' · '.join(CAMPOS) + '</div>'
    + '<div class="abs mono" style="left:300px;top:144px;width:800px;font-size:12px;line-height:20px">Automation &amp; Digital Solutions · Quito · Monterrey</div>'
    + logo(1010, 30, 70),
    step=30, D=16, L=16)

# Banner del perfil personal 1584×396 (la foto tapa la esquina inferior izquierda: el contenido va de x=520 en adelante)
banner_campos = ''
for i, (c, plazo) in enumerate(zip(CAMPOS, ['4–8 sem', '6–10 sem', '4–10 sem', '8–16 sem'])):
    x = 560 + i * 238
    banner_campos += (f'<div class="abs" style="left:{x}px;top:262px;width:222px;height:2px;background:#22b5cf"></div>'
                      f'<div class="abs k" style="left:{x}px;top:274px;font-size:15px;line-height:22px">A—0{i + 1} · {plazo}</div>'
                      f'<div class="abs t" style="left:{x}px;top:300px;width:222px;font-size:19px;line-height:24px">{c}</div>')
add('04-banner-perfil-personal-1584x396', 1584, 396,
    logo(560, 62, 92)
    + '<div class="abs brand" style="left:630px;top:70px;font-size:34px;line-height:40px">BOUW</div>'
    + '<div class="abs mono" style="left:630px;top:116px;font-size:13px;line-height:18px;letter-spacing:0.18em">Automation &amp; Digital Solutions</div>'
    + '<div class="abs h" style="left:560px;top:166px;width:960px;font-size:56px;line-height:62px">Del diseño <span class="o">a la realidad.</span></div>'
    + banner_campos
    + '<div class="abs mono" style="left:1164px;width:360px;top:74px;text-align:right;font-size:14px;line-height:22px;color:#4fd6e8">Quito · desde 2019<br>Monterrey · desde 2023</div>')

# =====================================================================
# 2. CAMPAÑA "DEL DISEÑO A LA REALIDAD" · publicaciones 1080×1350
# =====================================================================
W, H, M = 1080, 1350, 84


def header(hoja):
    return (logo(M, 72, 62)
            + f'<div class="abs brand" style="left:{M + 52}px;top:80px;font-size:34px;line-height:46px">BOUW</div>'
            + f'<div class="abs mono" style="right:{M}px;top:88px;font-size:21px;line-height:30px;text-align:right;width:600px">{e(hoja)}</div>'
            + f'<div class="crule" style="left:{M}px;top:160px;width:{W - 2 * M}px"></div>')


def footer(phrase, cta):
    cw = len(cta) * 17 + 70
    return (f'<div class="rule" style="left:{M}px;top:1160px;width:{W - 2 * M}px"></div>'
            + f'<div class="abs p" style="left:{M}px;top:1200px;width:{W - 2 * M - cw - 30}px;font-size:25px;line-height:33px;color:#93a7bf">{phrase}</div>'
            + f'<div class="cta" style="left:{W - M - cw}px;top:1204px;width:{cw}px;height:64px;font-size:22px;line-height:64px">{e(cta)}</div>')


def title(t, size, top=214):
    return f'<div class="abs h" style="left:{M}px;top:{top}px;width:{W - 2 * M}px;font-size:{size}px">{t}</div>'


def spec(rows, top, gap=150, kw=150, bsize=34):
    out = ''
    for i, (k, b, s) in enumerate(rows):
        y = top + i * gap
        out += (f'<div class="rule" style="left:{M}px;top:{y}px;width:{W - 2 * M}px"></div>'
                f'<div class="abs k" style="left:{M}px;top:{y + 30}px;width:{kw}px;font-size:24px;line-height:34px">{e(k)}</div>'
                f'<div class="abs t" style="left:{M + kw}px;top:{y + 26}px;width:{W - 2 * M - kw}px;font-size:{bsize}px;line-height:42px">{e(b)}</div>')
        if s:
            out += f'<div class="abs p" style="left:{M + kw}px;top:{y + 74}px;width:{W - 2 * M - kw}px;font-size:26px;line-height:34px">{e(s)}</div>'
    return out


def post(name, body):
    add(name, W, H, body)


# L01 · Presentación
post('L01-presentacion',
     header('Hoja 01 · Quiénes somos')
     + logo(M, 230, 250)
     + title('Del diseño<br>a la realidad.', 92, top=520)
     + '<div class="abs p" style="left:84px;top:740px;width:912px;font-size:32px;line-height:44px">Consultoría técnica para empresas que necesitan que lo que se dibuja en papel funcione en la operación.</div>'
     + spec([('QUITO', 'Ecuador', 'Desde 2019.'), ('MONTERREY', 'México', 'Desde 2023.')], top=900, gap=110, kw=240)
     + footer('Más de 7 años combinados.', 'Conócenos'))

# L02–L05 · Los cuatro campos del sitio
campos = [
    ('L02-campo-mejora-de-procesos', 'A—01', 'Mejora de procesos', '4 a 8 semanas',
     'Que la tarea se haga igual sin importar quién la haga.',
     [('01', 'Dibujamos el proceso como es hoy', 'Con las personas que lo hacen.'),
      ('02', 'Quitamos los pasos que sobran', 'Y escribimos el método.'),
      ('03', 'Lo dejamos funcionando', 'Con el procedimiento y los indicadores.')],
     '“Cada uno hace la tarea a su manera.”'),
    ('L03-campo-sistemas-de-calidad', 'A—02', 'Sistemas de calidad', '6 a 10 semanas',
     'Un sistema que se usa todos los días, no una carpeta para la auditoría.',
     [('01', 'Diagnóstico frente a la norma', 'Qué existe, qué falta.'),
      ('02', 'Documentos que la gente entiende', 'Cortos y en el lugar de trabajo.'),
      ('03', 'Indicadores y revisión', 'Para que el sistema se mantenga solo.')],
     '“El papeleo existe, pero nadie lo usa.”'),
    ('L04-campo-automatizacion', 'A—03', 'Automatización', '4 a 10 semanas',
     'Que el equipo deje de copiar datos de un sitio a otro.',
     [('01', 'Hacemos la cuenta', 'Cuánto cuesta hacerlo a mano.'),
      ('02', 'Automatizamos lo que da el número', 'Con las herramientas que ya usas.'),
      ('03', 'Entregamos documentado', 'Para mantenerlo sin nosotros.')],
     '“No nos alcanza el día.”'),
    ('L05-campo-diseno-a-producto', 'A—04', 'Diseño a producto', '8 a 16 semanas',
     'De la idea al plano, y del plano a algo que se puede fabricar.',
     [('01', 'Concepto y requisitos', 'Qué tiene que hacer y para quién.'),
      ('02', 'Diseño y prototipo', 'Planos y pruebas antes de invertir.'),
      ('03', 'Listo para fabricar', 'Documentación para producción.')],
     '“Tenemos la idea, falta llevarla a la realidad.”'),
]
for name, code, nombre, plazo, promesa, pasos, frase in campos:
    post(name,
         header(f'Campo {code} · {nombre}')
         + f'<div class="abs k" style="left:{M}px;top:214px;font-size:26px;line-height:34px">{code} · PLAZO {plazo.upper()}</div>'
         + title(e(nombre) + '.', 84, top=262)
         + f'<div class="abs p" style="left:{M}px;top:460px;width:{W - 2 * M}px;font-size:34px;line-height:46px;color:#e8eef6">{e(promesa)}</div>'
         + spec(pasos, top=640, gap=150, kw=120)
         + footer(e(frase), 'Radiografía gratis · 1 h'))

# L06 · Las frases con las que nos llaman (cita del sitio)
frases = ['“Cada uno hace la tarea a su manera.”', '“Todo pasa por mí.”', '“No nos alcanza el día.”',
          '“Me entero de los números a fin de mes.”', '“Compramos un sistema y nadie lo usa.”']
fr = ''
for i, f in enumerate(frases):
    y = 560 + i * 104
    fr += (f'<div class="rule" style="left:{M}px;top:{y}px;width:{W - 2 * M}px"></div>'
           f'<div class="abs k" style="left:{M}px;top:{y + 30}px;font-size:22px;line-height:34px">0{i + 1}</div>'
           f'<div class="abs t" style="left:{M + 90}px;top:{y + 26}px;width:820px;font-size:32px;line-height:42px">{e(f)}</div>')
post('L06-frases-con-las-que-nos-llaman',
     header('Hoja 06 · Lo que escuchamos')
     + title('Esta no es la lista de lo que vendemos.', 66)
     + '<div class="abs p" style="left:84px;top:430px;width:912px;font-size:34px;line-height:46px;color:#4fd6e8">Es la lista de frases con las que nos llaman.</div>'
     + fr + footer('¿Cuál dices tú?', 'Escríbenos'))

# L07 · Cómo trabajamos
post('L07-como-trabajamos',
     header('Hoja 07 · Cómo trabajamos')
     + title('Plazos que se pueden escribir.', 84)
     + spec([('01', 'Radiografía', '1 hora en tu empresa. Gratis.'),
             ('02', 'Alcance y precio cerrados', 'Por escrito, antes de empezar.'),
             ('03', 'Construcción', 'De 4 a 16 semanas, según el campo.'),
             ('04', 'Entrega', 'Funcionando, con la documentación para mantenerlo sin nosotros.')],
            top=470, gap=164, kw=120)
     + footer('Sin reuniones que no terminan en nada.', 'Pide tu Radiografía'))

# L08 · La cuenta (la calculadora del sitio)
calc = f'<div class="panel" style="left:{M}px;top:440px;width:{W - 2 * M}px;height:480px"></div>'
rows = [('Tarea: pasar pedidos del correo a la hoja', 'Ejemplo'), ('Veces por semana', '5'), ('Minutos cada vez', '× 30'),
        ('Personas que intervienen', '× 2'), ('Semanas al año', '× 48')]
for i, (l, v) in enumerate(rows):
    y = 440 + i * 74
    calc += (f'<div class="abs p" style="left:{M + 30}px;top:{y + 16}px;width:640px;font-size:27px;line-height:40px">{e(l)}</div>'
             f'<div class="abs k" style="left:{W - M - 330}px;top:{y + 16}px;width:300px;text-align:right;font-size:30px;line-height:40px">{e(v)}</div>'
             f'<div class="rule" style="left:{M}px;top:{y + 72}px;width:{W - 2 * M}px"></div>')
calc += (f'<div class="abs" style="left:{M}px;top:810px;width:{W - 2 * M}px;height:110px;background:#0f2c4c"></div>'
         f'<div class="abs t" style="left:{M + 30}px;top:840px;width:400px;font-size:34px;line-height:50px">Al año</div>'
         f'<div class="abs h" style="left:{W - M - 430}px;top:826px;width:400px;text-align:right;font-size:72px;line-height:80px;color:#4fd6e8">240 h</div>'
         f'<div class="abs p" style="left:{M}px;top:970px;width:{W - 2 * M}px;font-size:28px;line-height:38px">Si el número no da, te lo decimos. No automatizamos por automatizar.</div>')
post('L08-la-cuenta', header('Hoja 08 · La cuenta') + title('Cuánto cuesta hacerlo a mano.', 78) + calc
     + footer('Haz la cuenta con tu tarea.', 'Haz la cuenta'))

# L09 · Honestidad
chk = ''
items = ['Cada persona hace la misma tarea a su manera.', 'Alguien pasa horas copiando datos de un sitio a otro.',
         'Todo pasa por el dueño.', 'Los números llegan a fin de mes.', 'La idea está, pero no hay plano para fabricarla.']
for i, it in enumerate(items):
    y = 470 + i * 132
    chk += (f'<div class="abs" style="left:{M}px;top:{y + 6}px;width:48px;height:48px;border:3px solid #4fd6e8"></div>'
            f'<div class="abs p" style="left:{M + 80}px;top:{y}px;width:830px;font-size:32px;line-height:42px;color:#e8eef6">{e(it)}</div>'
            + (f'<div class="rule" style="left:{M}px;top:{y + 108}px;width:{W - 2 * M}px"></div>' if i < 4 else ''))
post('L09-marca-lo-que-reconozcas', header('Hoja 09 · ¿Nos necesitas?')
     + title('Marca lo que reconozcas.', 88) + chk
     + footer('¿Ninguna? Todavía no nos necesitas.', '¿Dos o más? Escríbenos'))

# L10 · Radiografía (cierre de la campaña)
post('L10-radiografia', header('Hoja 10 · Radiografía')
     + title('Una hora en tu empresa. Gratis.', 88)
     + logo(M, 470, 180)
     + '<div class="abs p" style="left:250px;top:500px;width:746px;font-size:32px;line-height:44px;color:#e8eef6">Revisamos un proceso clave contigo y al día siguiente te decimos qué haríamos primero.</div>'
     + spec([('R—01', 'Un proceso clave', 'Ventas, inventario, despacho, calidad o cierre de mes.'),
             ('R—02', 'La cuenta de horas', 'Con tus números. Si no da, te lo decimos.'),
             ('R—03', 'El primer paso', 'Por escrito, con plazo y precio.')],
            top=700, gap=146)
     + footer('WhatsApp +593 96 368 4012', 'Pide tu Radiografía'))

# =====================================================================
# 3. CARRUSEL (documento PDF de LinkedIn) 1080×1350 · "Los 4 campos"
# =====================================================================
car = []
car.append(header('Carrusel · 1 / 6') + logo(M, 260, 220)
           + title('4 campos.<br>Un mismo <span class="o">estándar.</span>', 100, top=520)
           + '<div class="abs p" style="left:84px;top:880px;width:912px;font-size:34px;line-height:46px">Del diseño a la realidad: qué hacemos y cuánto tarda cada cosa.</div>'
           + '<div class="abs mono" style="left:84px;top:1220px;font-size:22px;color:#4fd6e8">Desliza →</div>')
for i, (name, code, nombre, plazo, promesa, pasos, frase) in enumerate(campos):
    two = len(nombre) > 17
    car.append(header(f'Carrusel · {i + 2} / 6')
               + f'<div class="abs h" style="left:{M}px;top:200px;font-size:160px;line-height:170px;color:#17406b">0{i + 1}</div>'
               + f'<div class="abs k" style="left:{M}px;top:392px;font-size:24px;line-height:32px">{code} · PLAZO {plazo.upper()}</div>'
               + title(e(nombre) + '.', 80, top=436)
               + f'<div class="abs p" style="left:{M}px;top:{622 if two else 540}px;width:{W - 2 * M}px;font-size:32px;line-height:44px;color:#e8eef6">{e(promesa)}</div>'
               + spec(pasos, top=800, gap=124, kw=120, bsize=32)
               + f'<div class="abs p" style="left:{M}px;top:1190px;width:700px;font-size:24px;line-height:32px;color:#93a7bf">Lo escuchamos así: {e(frase)}</div>'
               + '<div class="abs mono" style="left:696px;width:300px;text-align:right;top:1196px;font-size:22px;color:#4fd6e8">Desliza →</div>')
car.append(header('Carrusel · 6 / 6') + title('¿Por dónde empezar?', 88)
           + spec([('01', 'Radiografía', '1 hora, gratis.'), ('02', 'La cuenta', 'Si el número no da, te lo decimos.'),
                   ('03', 'Alcance y precio', 'Cerrados, por escrito.')], top=470, gap=170, kw=120)
           + footer('Quito · Monterrey', 'Pide tu Radiografía'))
for i, b in enumerate(car, 1):
    add(f'C{i:02d}-carrusel-4-campos', W, H, b)

# =====================================================================
# 4. ANUNCIO / ENLACE 1200×627
# =====================================================================
add('A01-anuncio-radiografia-1200x627', 1200, 627,
    logo(72, 70, 70)
    + '<div class="abs brand" style="left:130px;top:78px;font-size:30px;line-height:40px">BOUW</div>'
    + '<div class="abs mono" style="left:828px;width:300px;top:84px;text-align:right;font-size:16px;line-height:24px">Radiografía</div>'
    + '<div class="crule" style="left:72px;top:150px;width:1056px"></div>'
    + '<div class="abs h" style="left:72px;top:190px;width:900px;font-size:64px;line-height:70px">Una hora en tu empresa. Gratis.</div>'
    + '<div class="abs p" style="left:72px;top:356px;width:760px;font-size:26px;line-height:36px">Al día siguiente te decimos qué haríamos primero. Si el número no da, te lo decimos.</div>'
    + '<div class="cta" style="left:72px;top:474px;width:330px;height:64px;font-size:22px;line-height:64px">Pide tu Radiografía</div>'
    + '<div class="abs mono" style="left:440px;top:494px;font-size:16px;line-height:24px;color:#4fd6e8">Quito · Monterrey</div>'
    + logo(960, 300, 240))

# ---------- escribir ----------
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

# ---------- documentos para Adobe Express (una .slide por pieza, fuentes de Adobe Fonts) ----------
KIT = '<link rel="stylesheet" href="https://use.typekit.net/dnh2wmm.css">'
XCSS = re.sub(r'@font-face\{[^}]*\}\n', '', CSS)
XCSS = (XCSS.replace('font-family:"Archivo";font-stretch:125%', 'font-family:"archivo-expanded",sans-serif')
        .replace('font-family:"PlexMono"', 'font-family:"ibm-plex-mono",monospace')
        .replace('font-family:"Plex",sans-serif', 'font-family:"ibm-plex-sans",sans-serif')
        .replace('font-family:"Plex"', 'font-family:"ibm-plex-sans",sans-serif'))
GROUPS = {
    'bouw-li-perfil': ['01-', '02-'],
    'bouw-li-portada-empresa': ['03-'],
    'bouw-li-banner-personal': ['04-'],
    'bouw-li-publicaciones-1': ['L01', 'L02', 'L03', 'L04', 'L05'],
    'bouw-li-publicaciones-2': ['L06', 'L07', 'L08', 'L09', 'L10'],
    'bouw-li-carrusel': ['C'],
    'bouw-li-anuncio': ['A'],
}
XOUT = os.path.join(HERE, 'express')
os.makedirs(XOUT, exist_ok=True)
for doc, prefixes in GROUPS.items():
    sel = [p for p in pieces if any(p[0].startswith(x) for x in prefixes)]
    w, h = sel[0][1], sel[0][2]
    slides = ''.join(f'<section class="slide" data-canvas-width="{pw}" data-canvas-height="{ph}" data-name="{e(n)}" '
                     f'style="width:{pw}px;height:{ph}px">{b}</section>' for n, pw, ph, b in sel)
    out = (f'<!doctype html><html lang="es"><head><meta charset="utf-8"><title>BOUW · LinkedIn</title>'
           f'<meta name="hz:slide-selector" content=".slide"><meta name="hz:canvas-width" content="{w}">'
           f'<meta name="hz:canvas-height" content="{h}">{KIT}<style>{XCSS}</style></head><body>{slides}</body></html>')
    with open(os.path.join(XOUT, doc + '.html'), 'w') as f:
        f.write(out)
    print(doc, len(sel), len(out) // 1024, 'KB')
