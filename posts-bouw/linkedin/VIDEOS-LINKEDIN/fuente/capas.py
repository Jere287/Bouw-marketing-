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
    # barra de progreso
    files['bar'] = (f'<!doctype html><html><head><style>*{{margin:0}}body{{background:transparent}}</style></head><body>'
                    f'<div style="width:{W - 2 * M}px;height:6px;border-radius:3px;background:linear-gradient(90deg,{CY},{GRN})"></div></body></html>')
    os.makedirs(f'{OUT}/{k}', exist_ok=True)
    for n, doc in files.items():
        open(f'{OUT}/{k}/{n}.html', 'w').write(doc)
    json.dump(cfg, open(f'{OUT}/{k}/cfg.json', 'w'), ensure_ascii=False)


C = lambda t: f'<span style="color:{CY}">{t}</span>'
CFGS = [
 dict(key='cumplimiento-es', src='v1', trim=13.0, crop=None, box=(M, 400, W - 2 * M, round((W - 2 * M) * 9 / 16)),
      tag='Mejora de procesos', hook=f'Tu pedido ya está listo. {C("¿Por qué no sale?")}',
      caps=[(0, 6.0, 'HOY', OR, 'Ella busca el registro del lote entre papeles. Él espera de brazos cruzados: el pallet no puede salir sin ese papel.'),
            (6.0, 13.0, 'CON BOUW', GRN, f'El registro aparece en pantalla en minutos, el lote se libera y {C("el pedido sale.")}')],
      cs=36, end=dict(lema='Del diseño a la realidad.', cta='El producto estaba listo. Faltaba el proceso.', sub='Mejora de procesos · Trazabilidad · Liberación de lotes')),
 dict(key='excel-es', src='v3', trim=34.0, crop=(1440, 962, 0, 0), box=(M, 360, W - 2 * M, round((W - 2 * M) * 962 / 1440)),
      tag='Automatización · Excel + VBA', hook=f'¿Tu cierre de mes todavía se arma {C("a mano?")}', hs=70,
      caps=[(0, 3, 'UN SOLO ARCHIVO', CY, f'11 hojas de Excel {C("conectadas por macros.")}'),
            (3, 11, '01 · FACTURAS', CY, f'Las facturas electrónicas del SRI {C("entran solas,")} sin volver a teclear.'),
            (11, 19, '02 · INVENTARIO', CY, f'Cada kit se costea desde su despiece y el stock {C("avisa antes de faltar.")}'),
            (19, 28, '03 · TABLERO', CY, f'Ingresos, gastos, cartera y margen: {C("se recalcula solo.")}'),
            (28, 34, '04 · CIERRE DE MES', GRN, f'El cierre ya no se arma a mano: {C("sale de lo ya capturado.")}')],
      cs=36, end=dict(lema='Si se repite, se automatiza.', cta='¿Qué proceso tuyo sigue a mano?', sub='Automatización de procesos · Excel · VBA · Dashboards')),
 dict(key='compliance-en', src='v0', trim=13.0, crop=None, box=(M, 400, W - 2 * M, round((W - 2 * M) * 9 / 16)),
      tag='Process improvement', hook=f'Your order is ready. {C("Why isn’t it shipping?")}',
      caps=[(0, 6.0, 'TODAY', OR, 'She digs through paper for the lot record. He waits, arms crossed: the pallet can’t ship without it.'),
            (6.0, 13.0, 'WITH BOUW', GRN, f'The record is on screen in minutes, the lot is released and {C("the order ships.")}')],
      cs=36, end=dict(lema='From design to reality.', cta='The product was ready. The process wasn’t.', sub='Process improvement · Traceability · Lot release')),
 dict(key='excel-en', src='v2', trim=34.0, crop=(1440, 962, 0, 0), box=(M, 360, W - 2 * M, round((W - 2 * M) * 962 / 1440)),
      tag='Automation · Excel + VBA', hook=f'Is your month-end close still {C("done by hand?")}', hs=70,
      caps=[(0, 3, 'ONE FILE', CY, f'11 Excel sheets {C("wired together with macros.")}'),
            (3, 11, '01 · INVOICES', CY, f'E-invoices {C("load themselves,")} no retyping.'),
            (11, 19, '02 · INVENTORY', CY, f'Each kit is costed from its bill of materials and stock {C("warns before it runs out.")}'),
            (19, 28, '03 · DASHBOARD', CY, f'Income, expenses, receivables and margin: {C("it recalculates itself.")}'),
            (28, 34, '04 · MONTH-END', GRN, f'The close is no longer assembled by hand: {C("it comes from what is already captured.")}')],
      cs=36, end=dict(lema='If it repeats, automate it.', cta='Which of your processes is still manual?', sub='Process automation · Excel · VBA · Dashboards')),
]
for c in CFGS:
    build(c)
print('ok', len(CFGS))
