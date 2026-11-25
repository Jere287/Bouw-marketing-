"""Capas gráficas (PNG) para editar los videos del sitio en formato LinkedIn 4:5."""
import os, json, html
ROOT = '/home/user/Bouw-marketing-/posts-bouw'
F = ROOT + '/fonts'
OUT = '/tmp/claude-0/-home-user-Bouw-marketing-/ae718e48-3374-5ea4-b0dc-c539d41ea878/scratchpad/vid/build'
LOGO = 'file://' + ROOT + '/sitio/dragon/capturas/dragon-oscuro-realidad-transparente.png'
LR = 2135 / 1121
W, H, M = 1080, 1350, 72
CY, OR, GRN = '#4fd6e8', '#f79b4a', '#5ad19a'
CSS = f"""
@font-face{{font-family:Archivo;src:url(file://{F}/Archivo-100_900.woff2);font-weight:100 900}}
@font-face{{font-family:Plex;src:url(file://{F}/IBMPlexSans-400.woff2)}}
@font-face{{font-family:PlexMono;src:url(file://{F}/IBMPlexMono-500.woff2)}}
@font-face{{font-family:Instrument;src:url(file://{F}/InstrumentSerif-Italic.ttf);font-style:italic}}
*{{margin:0;padding:0;box-sizing:border-box}} html,body{{background:transparent}}
.s{{position:relative;width:{W}px;height:{H}px;overflow:hidden}} .a{{position:absolute}}
.h{{font-family:Archivo;font-weight:700;letter-spacing:-0.028em;color:#fff}}
.m{{font-family:PlexMono;font-weight:500;text-transform:uppercase;letter-spacing:.16em}}
.p{{font-family:Plex;color:#d6e0ea}}
"""


def grid():
    d = ''.join(f'M{x} 0V{H}' for x in range(54, W, 54)) + ''.join(f'M0 {y}H{W}' for y in range(54, H, 54))
    return (f'<svg class="a" style="left:0;top:0" width="{W}" height="{H}"><path d="{d}" fill="none" stroke="#4fd6e8" stroke-opacity=".05" stroke-width="1.5"/></svg>')


def pill(t, col, x, y, fs=21, solid=False):
    w = int(len(html.unescape(t)) * fs * 0.83 + 70)
    bg = col if solid else 'rgba(4,16,31,.6)'
    tc = '#04101f' if solid else col
    dot = '' if solid else f'<div class="a" style="left:{x + 22}px;top:{y + 19}px;width:12px;height:12px;border-radius:6px;background:{col}"></div>'
    return (f'<div class="a" style="left:{x}px;top:{y}px;width:{w}px;height:50px;border-radius:25px;border:2px solid {col};background:{bg}"></div>{dot}'
            f'<div class="a m" style="left:{x + (12 if solid else 44)}px;top:{y}px;width:{w - (24 if solid else 48)}px;height:50px;font-size:{fs}px;line-height:50px;color:{tc};{"text-align:center" if solid else ""}">{t}</div>')


def brandbar():
    return (f'<div class="a" style="left:{M}px;top:1222px;width:{W - 2 * M}px;height:2px;background:rgba(79,214,232,.25)"></div>'
            f'<img class="a" src="{LOGO}" style="left:{M}px;top:1240px;width:150px;height:{round(150 / LR)}px">'
            f'<div class="a m" style="left:{M + 172}px;top:1272px;width:300px;font-size:16px;line-height:24px;color:#9fb3c8">Quito · Monterrey</div>'
            f'<div class="a h" style="left:{W - M - 560}px;top:1262px;width:560px;text-align:right;font-size:31px;line-height:40px;color:{CY};letter-spacing:-0.01em">www.bouwlatam.com</div>')


def page(body, bg=True):
    base = ('<div class="a" style="left:0;top:0;width:1080px;height:1350px;background:#04101f"></div>'
            '<div class="a" style="left:420px;top:-300px;width:1000px;height:1000px;border-radius:50%;background:radial-gradient(circle,rgba(79,214,232,.18),rgba(79,214,232,0) 65%)"></div>'
            '<div class="a" style="left:-420px;top:800px;width:900px;height:900px;border-radius:50%;background:radial-gradient(circle,rgba(247,155,74,.09),rgba(247,155,74,0) 65%)"></div>'
            + grid()) if bg else ''
    return f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body><div class="s">{base}{body}</div></body></html>'


def build(cfg):
    k = cfg['key']
    vx, vy, vw, vh = cfg['box']
    files = {}
    # fondo: etiqueta, gancho, halo detrás del video, barra de marca
    bgb = (pill(cfg['tag'], CY, M, 64)
           + f'<div class="a h" style="left:{M}px;top:146px;width:{W - 2 * M}px;font-size:{cfg.get("hs", 74)}px;line-height:{round(cfg.get("hs", 74) * 1.03)}px">{cfg["hook"]}</div>'
           + f'<div class="a" style="left:{vx - 6}px;top:{vy - 6}px;width:{vw + 12}px;height:{vh + 12}px;border-radius:30px;background:rgba(79,214,232,.25);'
             f'box-shadow:0 40px 90px -30px rgba(0,0,0,.85),0 0 60px -10px rgba(79,214,232,.35)"></div>'
           + brandbar())
    files['bg'] = page(bgb)
    # máscara de esquinas redondeadas para el video
    files['mask'] = (f'<!doctype html><html><head><style>*{{margin:0}}body{{background:#000}}</style></head><body>'
                     f'<div style="width:{vw}px;height:{vh}px;background:#fff;border-radius:24px"></div></body></html>')
    # subtítulos por escena (transparentes)
    cy0 = vy + vh + 26
    for i, (a, b, lab, col, txt) in enumerate(cfg['caps']):
        if lab.startswith('LEAN'):
            tools = cfg['lean_tools']
            cx, cyc = vx + vw // 2, vy + vh // 2
            chips = ''
            cw_, gap = 196, 14
            x0 = cx - (len(tools) * cw_ + (len(tools) - 1) * gap) // 2
            for j, t_ in enumerate(tools):
                chips += (f'<div class="a" style="left:{x0 + j * (cw_ + gap)}px;top:{cyc + 40}px;width:{cw_}px;height:52px;border-radius:26px;background:rgba(4,16,31,.85);border:2px solid {CY}"></div>'
                          f'<div class="a m" style="left:{x0 + j * (cw_ + gap)}px;top:{cyc + 40}px;width:{cw_}px;height:52px;text-align:center;font-size:17px;line-height:52px;color:#fff;letter-spacing:.08em">{t_}</div>')
            body = (f'<div class="a" style="left:{vx}px;top:{vy}px;width:{vw}px;height:{vh}px;border-radius:24px;background:radial-gradient(ellipse at center,rgba(4,16,31,.78),rgba(4,16,31,.45) 75%)"></div>'
                    f'<div class="a m" style="left:{vx}px;top:{cyc - 96}px;width:{vw}px;text-align:center;font-size:22px;line-height:30px;color:{CY};letter-spacing:.3em">{cfg["lean_kicker"]}</div>'
                    f'<div class="a h" style="left:{vx}px;top:{cyc - 58}px;width:{vw}px;text-align:center;font-size:72px;line-height:80px">Lean <span style="color:{CY}">Manufacturing</span></div>'
                    + chips
                    + pill(cfg['lean_kicker'], CY, M, cy0, 20, solid=True)
                    + f'<div class="a h" style="left:{M}px;top:{cy0 + 64}px;width:{W - 2 * M}px;font-size:{cfg.get("cs", 38)}px;line-height:{round(cfg.get("cs", 38) * 1.22)}px;font-weight:600">{txt}</div>')
            files[f'cap{i}'] = page(body, bg=False)
            continue
        body = ((pill(lab, col, M, cy0, 20, solid=True) if lab else '')
                + f'<div class="a h" style="left:{M}px;top:{cy0 + (64 if lab else 0)}px;width:{W - 2 * M}px;font-size:{cfg.get("cs", 38)}px;line-height:{round(cfg.get("cs", 38) * 1.22)}px;'
                  f'font-weight:600;letter-spacing:-0.01em">{txt}</div>')
        files[f'cap{i}'] = page(body, bg=False)
    # tarjeta final
    e = cfg['end']
    endb = (f'<img class="a" src="{LOGO}" style="left:{(W - 640) // 2}px;top:250px;width:640px;height:{round(640 / LR)}px">'
            f'<div class="a" style="left:{(W - 640) // 2}px;top:250px;width:640px;height:{round(640 / LR)}px;background:radial-gradient(ellipse,rgba(79,214,232,.18),rgba(79,214,232,0) 70%);z-index:-1"></div>'
            f'<div class="a" style="left:0;top:640px;width:{W}px;text-align:center;font-family:Instrument;font-style:italic;font-size:76px;line-height:84px;color:#fff">{e["lema"]}</div>'
            f'<div class="a h" style="left:{M}px;top:790px;width:{W - 2 * M}px;text-align:center;font-size:46px;line-height:56px">{e["cta"]}</div>'
            f'<div class="a" style="left:{(W - 640) // 2}px;top:930px;width:640px;height:96px;border-radius:48px;background:{CY}"></div>'
            f'<div class="a h" style="left:{(W - 640) // 2}px;top:930px;width:640px;text-align:center;font-size:44px;line-height:96px;color:#04101f;letter-spacing:-0.01em">www.bouwlatam.com</div>'
            f'<div class="a m" style="left:0;top:1070px;width:{W}px;text-align:center;font-size:22px;line-height:32px;color:#9fb3c8">{e["sub"]}</div>')
    files['end'] = page(endb)
    if cfg.get('stats'):
        st_ = cfg['stats']
        sb = (f'<div class="a m" style="left:0;top:330px;width:{W}px;text-align:center;font-size:24px;line-height:32px;color:{CY};letter-spacing:.3em">{st_["kicker"]}</div>'
              f'<div class="a h" style="left:{M}px;top:380px;width:{W - 2 * M}px;text-align:center;font-size:60px;line-height:66px">{st_["title"]}</div>')
        for j, (num, lab) in enumerate(st_['items']):
            x = M + j * ((W - 2 * M) // 2)
            sb += (f'<div class="a" style="left:{x + 12}px;top:540px;width:{(W - 2 * M) // 2 - 24}px;height:330px;border-radius:26px;background:#071a2f;border:2px solid rgba(79,214,232,.4)"></div>'
                   f'<div class="a h" style="left:{x}px;top:590px;width:{(W - 2 * M) // 2}px;text-align:center;font-size:112px;line-height:160px;color:{GRN}">{num}</div>'
                   f'<div class="a h" style="left:{x}px;top:770px;width:{(W - 2 * M) // 2}px;text-align:center;font-size:36px;line-height:44px;font-weight:600">{lab}</div>')
        sb += f'<div class="a p" style="left:0;top:930px;width:{W}px;text-align:center;font-size:26px;line-height:36px;color:#9fb3c8">{st_["foot"]}</div>'
        files['stats'] = page(sb)
    # barra de progreso
    files['bar'] = (f'<!doctype html><html><head><style>*{{margin:0}}body{{background:transparent}}</style></head><body>'
                    f'<div style="width:{W - 2 * M}px;height:6px;border-radius:3px;background:linear-gradient(90deg,{CY},{GRN})"></div></body></html>')
    os.makedirs(f'{OUT}/{k}', exist_ok=True)
    for n, doc in files.items():
        open(f'{OUT}/{k}/{n}.html', 'w').write(doc)
    json.dump(cfg, open(f'{OUT}/{k}/cfg.json', 'w'), ensure_ascii=False)


C = lambda t: f'<span style="color:{CY}">{t}</span>'
O = lambda t: f'<span style="color:{OR}">{t}</span>'
CFGS = [
 dict(key='cumplimiento-es', src='v1', trim=13.0, crop=None, box=(M, 400, W - 2 * M, round((W - 2 * M) * 9 / 16)),
      tag='Mejora de procesos', hook=f'Mismo equipo. Misma planta. {C("Otro resultado.")}', hs=76,
      lean_kicker='Aplicando', lean_tools=['5S', 'Flujo continuo', 'Trabajo estándar', 'Kaizen'],
      caps=[(0, 5.2, 'HOY', OR, f'Buscando. Esperando.<br>{O("Detenido.")}'),
            (5.2, 7.6, 'LEAN', CY, f'Ordenamos el proceso,<br>{C("paso a paso.")}'),
            (7.6, 13.0, 'CON BOUW', GRN, f'Ordenado. Liberado.<br>{C("En camino.")}')],
      stats=dict(kicker='Resultado medido', title='Caso real de mejora continua', items=[('−15 %', 'tiempo de<br>preparación'), ('−20 %', 'reprocesos')], foot='Línea de producción de dos turnos · 4 operadores capacitados'),
      cs=58, end=dict(lema='Del diseño a la realidad.', cta='No cambiamos a tu gente.<br>Mejoramos tu proceso.', sub='Mejora de procesos · Mejora continua · Producción')),
 dict(key='excel-es', src='v3', trim=34.0, crop=(1440, 962, 0, 0), box=(M, 360, W - 2 * M, 624),
      tag='Automatización de procesos', hook=f'¿Cuántas horas al mes {C("pierde tu equipo haciendo lo mismo?")}', hs=66,
      caps=[(0, 3, 'UN SOLO ARCHIVO', CY, f'Todo en<br>{C("un solo lugar.")}'),
            (3, 11, 'FACTURAS', CY, f'Las facturas:<br>{C("ya no se teclean.")}'),
            (11, 19, 'INVENTARIO', CY, f'El inventario:<br>{C("ya no se cuenta.")}'),
            (19, 28, 'REPORTES', CY, f'Los reportes:<br>{C("ya no se arman.")}'),
            (28, 34, 'CIERRE DE MES', GRN, f'El cierre de mes:<br>{C("ya no se espera.")}')],
      stats=dict(kicker='Caso real · taller de manufactura', title='No es más trabajo. Es menos.', items=[('11', 'hojas<br>conectadas'), ('0', 'licencias<br>nuevas')], foot='Sobre el mismo Excel · Excel + VBA · facturas del SRI automáticas'),
      cs=52, end=dict(lema='Si se repite, se automatiza.', cta='¿Qué tarea quitarías primero?', sub='Automatización de procesos · Excel · VBA · Dashboards')),
 dict(key='compliance-en', src='v0', trim=13.0, crop=None, box=(M, 400, W - 2 * M, round((W - 2 * M) * 9 / 16)),
      tag='Process improvement', hook=f'Same team. Same plant. {C("A different result.")}', hs=76,
      lean_kicker='Applying', lean_tools=['5S', 'Flow', 'Standard work', 'Kaizen'],
      caps=[(0, 5.2, 'TODAY', OR, f'Searching. Waiting.<br>{O("Stuck.")}'),
            (5.2, 7.6, 'LEAN', CY, f'We fix the process,<br>{C("step by step.")}'),
            (7.6, 13.0, 'WITH BOUW', GRN, f'Organized. Released.<br>{C("On its way.")}')],
      stats=dict(kicker='Measured result', title='Real continuous improvement case', items=[('−15 %', 'setup<br>time'), ('−20 %', 'rework')], foot='Two-shift production line · 4 operators trained'),
      cs=58, end=dict(lema='From design to reality.', cta='We don’t change your people.<br>We improve your process.', sub='Process improvement · Continuous improvement · Production')),
 dict(key='excel-en', src='v2', trim=34.0, crop=(1440, 962, 0, 0), box=(M, 360, W - 2 * M, 624),
      tag='Process automation', hook=f'How many hours a month {C("does your team spend doing the same thing?")}', hs=64,
      caps=[(0, 3, 'ONE FILE', CY, f'Everything in<br>{C("one place.")}'),
            (3, 11, 'INVOICES', CY, f'Invoices:<br>{C("no more retyping.")}'),
            (11, 19, 'INVENTORY', CY, f'Inventory:<br>{C("no more counting.")}'),
            (19, 28, 'REPORTS', CY, f'Reports:<br>{C("no more building.")}'),
            (28, 34, 'MONTH-END CLOSE', GRN, f'Month-end close:<br>{C("no more waiting.")}')],
      stats=dict(kicker='Real case · manufacturing shop', title='It’s not more work. It’s less.', items=[('11', 'connected<br>sheets'), ('0', 'new<br>licenses')], foot='On the same Excel · Excel + VBA · automatic e-invoices'),
      cs=52, end=dict(lema='If it repeats, automate it.', cta='Which task would you remove first?', sub='Process automation · Excel · VBA · Dashboards')),
]
for c in CFGS:
    build(c)
print('ok', len(CFGS))
