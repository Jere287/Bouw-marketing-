"""Arma PLAN-SEMANAL: junta PUBLICAR (martes a jueves) y PUBLICAR-SABIAS-QUE (viernes) en carpetas por semana,
escribe PLAN-SEMANAL.md y dibuja el calendario en PLAN-SEMANAL.png.
Uso: python3 calendario.py && python3 calendario_datos.py && python3 plan_semanal.py && node shot_plan.js
"""
import datetime as dt, os, re, shutil

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'PLAN-SEMANAL')
MES = {'nov': 11, 'dic': 12, 'ene': 1}
DIAS = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
MESES = {11: 'nov', 12: 'dic', 1: 'ene'}
TEMA = {'D02': 'Caso real: −20 % de reprocesos', 'A11': '5 cosas que tu equipo hace a mano cada lunes', 'A13': '240 horas al año',
        'D06': '¿Tu planta pasaría una auditoría mañana?', 'A18': 'Carrusel: 5 tareas que puedes automatizar este mes',
        'D05': 'Caso real: el cierre de mes que ahora sale solo', 'A14': 'Mito y realidad: automatizar no es caro',
        'A12': 'Antes y después: cotizar a mano', 'D07': 'Caso real: el pedido llega a WhatsApp escrito',
        'A15': 'Semáforo: no todo hay que automatizarlo', 'D03': 'Carrusel: 3 errores al automatizar',
        'A16': 'Así llega un pedido por WhatsApp', 'D09': 'Cómo trabajamos: plazo y precio por escrito',
        'A17': 'El reporte del lunes puede llegar solo', 'D04': 'Frase: Si se repite, se automatiza',
        'D08': 'Tip: si tienes ventas_final_v2.xlsx…', 'D10': '¿Qué proceso te está costando horas?',
        'S01': '¿Sabías que…? 9 de cada 10 hojas de cálculo tienen errores', 'S02': '¿Sabías que…? 45 % del trabajo es automatizable',
        'S03': '¿Sabías que…? 15 % de las ventas se va en mala calidad', 'S04': '¿Sabías que…? Un día a la semana buscando información',
        'S05': '¿Sabías que…? 60 % del día es trabajo sobre el trabajo', 'S06': '¿Sabías que…? 11 % de ingresos perdidos por paros',
        'S07': '¿Sabías que…? De 4 horas a 3 minutos (SMED)', 'S08': '¿Sabías que…? 71 % prefiere el chat en México',
        'S09': '¿Sabías que…? Pymes: 99 % de las empresas, 25 % de la producción'}

items = []
for src in ['PUBLICAR', 'PUBLICAR-SABIAS-QUE']:
    for d in sorted(os.listdir(os.path.join(HERE, src))):
        m = re.match(r'\d+_(\d+)-(\w+)_(\w\d\d)', d)
        if not m:
            continue
        day, mon, code = int(m.group(1)), MES[m.group(2)], m.group(3)
        fecha = dt.date(2027 if mon == 1 else 2026, mon, day)
        items.append((fecha, code, os.path.join(HERE, src, d)))
items.sort()

shutil.rmtree(OUT, ignore_errors=True)
os.makedirs(OUT)
semanas = {}
for f, code, path in items:
    lunes = f - dt.timedelta(days=f.weekday())
    semanas.setdefault(lunes, []).append((f, code, path))

md = ['# Plan semanal de LinkedIn · BOUW', '',
      'Empieza **hoy, jueves 19 de noviembre de 2026**. Martes a jueves van las series de marca y automatización; los viernes, "¿Sabías que…?".',
      'Hora: **08:00 Quito / 07:00 Monterrey** (si hoy ya pasó esa hora, publica en cuanto puedas antes de las 13:00).', '',
      'Cada día tiene su carpeta con `imagen.png` (o el PDF del carrusel) y `publicar.txt` (texto, texto alternativo y primer comentario).', '',
      '## Rutina de cada semana', '',
      '| Día | Qué hacer | Tiempo |', '|---|---|---|',
      '| **Lunes** | Programar en LinkedIn las publicaciones de la semana (el reloj junto a "Publicar"). Revisar mensajes del fin de semana. | 20 min |',
      '| **Martes a viernes** | La publicación sale sola. Apenas salga: poner el primer comentario con el enlace y compartirla desde el perfil de cada socio con una frase propia. | 5 min |',
      '| **Durante la primera hora** | Responder todos los comentarios. A quien diga "me pasa", escribirle por mensaje privado y ofrecer una llamada de 20 minutos. | 15 min |',
      '| **Viernes por la tarde** | Anotar impresiones, reacciones, comentarios y mensajes de la semana. Ver qué publicación funcionó mejor. | 10 min |', '']
n = 0
for i, (lunes, lst) in enumerate(sorted(semanas.items()), 1):
    fin = lunes + dt.timedelta(days=4)
    nombre = f'SEMANA-{i:02d}_{lunes.day}-{MESES[lunes.month]}_al_{fin.day}-{MESES[fin.month]}'
    os.makedirs(os.path.join(OUT, nombre))
    md += [f'## Semana {i} · del {lunes.day} {MESES[lunes.month]} al {fin.day} {MESES[fin.month]}' + (' (empieza hoy)' if i == 1 else ''), '',
           '| Día | Publicación | Carpeta |', '|---|---|---|']
    for f, code, path in lst:
        n += 1
        dname = f'{DIAS[f.weekday()].upper()}-{f.day:02d}-{MESES[f.month]}_{code}'
        shutil.copytree(path, os.path.join(OUT, nombre, dname))
        hoy = ' **← HOY**' if f == dt.date(2026, 11, 19) else ''
        md.append(f'| {DIAS[f.weekday()]} {f.day} {MESES[f.month]} | {TEMA[code]}{hoy} | `{nombre}/{dname}` |')
    md.append('')
    for f, code, path in lst:
        t = open(os.path.join(path, 'publicar.txt')).read()
        txt = t.split('1) TEXTO (copiar y pegar):', 1)[1].split('\n2) ', 1)[0].strip()
        resto = '2) ' + t.split('\n2) ', 1)[1].split('\n4) ', 1)[0].strip()
        tags = ' '.join(w for w in txt.split() if w.startswith('#'))
        md += [f'### {DIAS[f.weekday()]} {f.day} {MESES[f.month]} · {TEMA[code]}', '',
               f'**Hashtags:** {tags}', '', '**Texto de la publicación (copiar y pegar):**', '', '```', txt, '```', '',
               resto.replace('2) IMAGEN: imagen.png', '**Imagen:** `imagen.png`').replace('2) DOCUMENTO:', '**Documento:**')
                    .replace('Al subirla toca "Texto alternativo" y pega:', '**Texto alternativo:**')
                    .replace('3) PRIMER COMENTARIO (apenas salga la publicación):', '\n**Primer comentario:**')
                    .replace('3) PRIMER COMENTARIO (con la fuente, apenas salga la publicación):', '\n**Primer comentario (con la fuente):**'), '']
    if lunes == dt.date(2026, 12, 14):
        md += ['> **Pausa del 19 de diciembre al 4 de enero.** Solo responder mensajes. Volvemos el martes 5 de enero.', '']
md += ['## Metas al 29 de enero', '', '| Indicador | Meta |', '|---|---|',
       '| Conversaciones (mensajes o WhatsApp) que llegan por LinkedIn | 20 |', '| Diagnósticos agendados | 6 |',
       '| Seguidores nuevos de la página | +300 |', '| Interacción media por publicación | 3 % o más |', '',
       f'Total: **{n} publicaciones** en {len(semanas)} semanas.', '',
       '**Desde el 12 de enero** quedan martes a jueves libres: conviene preparar una tanda nueva en la primera semana de enero, repitiendo los formatos que más comentarios hayan tenido.']
open(os.path.join(OUT, 'PLAN-SEMANAL.md'), 'w').write('\n'.join(md) + '\n')

# calendario visual (primeras 5 semanas, hasta la pausa)
NAVY, ORANGE, CYAN, CREAM = '#0d2947', '#f79b4a', '#4fd6e8', '#fbf6ea'
cells = ''
for r, (lunes, lst) in enumerate(sorted(semanas.items())[:5]):
    cells += f'<div class="wk">Semana {r + 1}<br><span>{lunes.day} {MESES[lunes.month]}</span></div>'
    by = {f.weekday(): (f, code) for f, code, _ in lst}
    for wd in range(1, 5):
        if wd in by:
            f, code = by[wd]
            img = os.path.join(HERE, 'png', {'A18': 'A18-carrusel-1-portada.png', 'D03': 'D03-carrusel-1-portada.png'}.get(code, ''))
            if code not in ('A18', 'D03'):
                img = [os.path.join(HERE, 'png', x) for x in os.listdir(os.path.join(HERE, 'png')) if x.startswith(code + '-')][0]
            hoy = ' hoy' if f == dt.date(2026, 11, 19) else ''
            cells += (f'<div class="c{hoy}"><img src="file://{img}"><div class="t"><b>{DIAS[wd][:3]} {f.day}</b> {TEMA[code]}</div>'
                      + ('<div class="badge">HOY</div>' if hoy else '') + '</div>')
        else:
            cells += '<div class="c empty"></div>'
FONTS = os.path.join(os.path.dirname(HERE), 'fonts')
html = f"""<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:A;src:url(file://{FONTS}/Archivo-100_900.woff2);font-weight:100 900}}
@font-face{{font-family:P;src:url(file://{FONTS}/IBMPlexSans-400.woff2)}}
*{{margin:0;padding:0;box-sizing:border-box}} body{{background:{CREAM};font-family:P;color:{NAVY};width:1600px;padding:48px}}
h1{{font-family:A;font-weight:800;font-size:46px}} p{{font-size:20px;margin:8px 0 28px}}
.g{{display:grid;grid-template-columns:150px repeat(4,1fr);gap:14px}}
.h{{font-family:A;font-weight:700;font-size:20px;text-transform:uppercase;letter-spacing:.08em;color:{ORANGE}}}
.wk{{font-family:A;font-weight:800;font-size:22px;align-self:center}} .wk span{{font-family:P;font-weight:400;font-size:17px;color:#5b6b7e}}
.c{{position:relative;background:#fff;border-radius:14px;overflow:hidden;box-shadow:0 6px 18px rgba(13,41,71,.10);display:flex;gap:10px;padding:10px;align-items:center;min-height:120px}}
.c img{{width:84px;height:105px;object-fit:cover;border-radius:8px;flex:none}} .t{{font-size:16px;line-height:1.3}} .t b{{display:block;font-family:A;font-size:17px;color:{NAVY}}}
.empty{{background:transparent;box-shadow:none}} .hoy{{outline:4px solid {ORANGE}}}
.badge{{position:absolute;top:8px;right:8px;background:{ORANGE};color:#fff;font-family:A;font-weight:800;font-size:14px;padding:4px 10px;border-radius:12px}}
.note{{margin-top:22px;font-size:18px;color:#5b6b7e}}
</style></head><body><h1>Plan semanal de LinkedIn · BOUW</h1>
<p>Martes a jueves: marca y automatización. Viernes: ¿Sabías que…? · 08:00 Quito / 07:00 Monterrey</p>
<div class="g"><div></div><div class="h">Martes</div><div class="h">Miércoles</div><div class="h">Jueves</div><div class="h">Viernes</div>{cells}</div>
<div class="note">Pausa del 19 de diciembre al 4 de enero. Enero continúa en PLAN-SEMANAL.md.</div></body></html>"""
open(os.path.join(HERE, 'html_plan.html'), 'w').write(html)
print(n, 'publicaciones en', len(semanas), 'semanas')
