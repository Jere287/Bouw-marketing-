"""Serie S "¿Sabías que…?": datos reales con fuente citada en la imagen, cada pieza de otro color.
Reutiliza el lenguaje visual de la serie A (gen_auto.py).

Fuentes (verificadas al armar la serie, noviembre 2026):
S01 Panko (Univ. de Hawái), auditoría de 54 hojas de cálculo: 49 con errores (91 %).
S02 McKinsey Global Institute (2016): 45 % de las actividades laborales automatizables con tecnología ya demostrada.
S03 IISE, "Measuring the cost of quality": costo de la mala calidad ≈ 15 % de las ventas (rango 5–35 %).
S04 McKinsey Global Institute, "The Social Economy" (2012): 19 % de la semana laboral en buscar y reunir información.
S05 Asana, Anatomy of Work Index 2021 (+13 000 trabajadores): ~60 % del tiempo en "trabajo sobre el trabajo".
S06 Siemens, True Cost of Downtime 2024: los paros no planificados cuestan 11 % de los ingresos de las 500 mayores empresas.
S07 Shigeo Shingo (SMED, Toyota): un cambio de prensa pasó de 4 horas a 3 minutos.
S08 Kantar, citado por Expansión (2025): 71 % de los adultos en línea en México ve la mensajería como lo más rápido para tratar con empresas.
S09 CEPAL (2019): las mipymes son el 99 % de las empresas, 61 % del empleo formal y 25 % de la producción de América Latina.

Uso: python3 gen_datos.py && node shot_datos.js  →  png/S*.png
"""
import os
import gen_auto as g

OUT = os.path.join(g.HERE, 'html_datos')
os.makedirs(OUT, exist_ok=True)
W, H = g.W, g.H
NAVY, ORANGE, ORANGE_D, CYAN, CREAM, YELLOW = g.NAVY, g.ORANGE, g.ORANGE_D, g.CYAN, g.CREAM, g.YELLOW


def sabias(top, color, bg='transparent'):
    return g.tag('¿Sabías que…?', top, color, bg)


def fuente(t, color, top=1090):
    return g.text('Fuente: ' + t, top, 22, color=color, width=880)


def stat(x, y, w, h, n, t, bg, fg, nsize=100):
    return (f'<div class="abs" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;border-radius:26px;background:{bg};'
            f'display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;color:{fg}">'
            f'<div class="hd" style="font-size:{nsize}px;line-height:1;white-space:nowrap">{n}</div>'
            f'<div class="tx" style="font-size:26px;margin-top:10px">{t}</div></div>')


def bouw(t, top, bg, fg, h=110):
    return g.pill(110, top, 860, h, t, bg, fg, 28, 20)


pieces = []


def add(name, body):
    pieces.append((name, body))


# S01 · cian: 9 de cada 10 hojas de cálculo con errores
add('S01-hojas-de-calculo',
    g.fill(CYAN) + g.dots(40, 60, NAVY, .18)
    + g.logo(solid=NAVY) + sabias(290, NAVY)
    + g.head('9 <span style="font-size:110px">de cada</span> 10', 360, 230, color=NAVY)
    + g.head('hojas de cálculo auditadas tenían errores.', 640, 66, color=NAVY, width=880)
    + g.text('En una auditoría de 54 hojas usadas en empresas reales, 49 tenían al menos un error.', 820, 30, color=NAVY, width=840)
    + bouw('Si tus decisiones salen de un Excel, vale la pena revisarlo.', 940, NAVY, '#fff')
    + fuente('Raymond Panko, Universidad de Hawái.', NAVY)
    + g.footer(NAVY, 1160).replace('top:1240px', 'top:1242px'))

# S02 · azul: 45 % de las actividades
add('S02-45-por-ciento',
    g.blue() + g.dots(780, 70, CYAN, .25)
    + g.logo() + sabias(290, ORANGE)
    + g.head('<span style="color:' + ORANGE + '">45 %</span>', 360, 260)
    + g.head('de las actividades del trabajo se pueden automatizar con tecnología que ya existe.', 640, 58, width=900)
    + g.text('Pocos puestos se automatizan completos. Lo que se automatiza son tareas: copiar, buscar, calcular, reportar.', 840, 30, color='rgba(255,255,255,.85)', width=860)
    + fuente('McKinsey Global Institute.', 'rgba(255,255,255,.65)', 1060)
    + g.footer('#fff', 1160).replace('top:1240px', 'top:1242px'))

# S03 · naranja: 15 % de las ventas
add('S03-costo-mala-calidad',
    g.fill(ORANGE) + g.dots(40, 1060, '#fff', .3, 6, 3)
    + g.logo(solid='#ffffff') + sabias(290, NAVY)
    + g.head('15 %', 360, 280, color='#fff')
    + g.head('de las ventas se va, en promedio, en <span style="color:' + NAVY + '">reprocesos, desperdicio y devoluciones</span>.', 660, 56, color='#fff', width=900)
    + g.text('Es el costo de la mala calidad en manufactura. En algunas plantas llega al 35 %.', 860, 30, color=NAVY, width=840)
    + fuente('IISE, Institute of Industrial and Systems Engineers.', NAVY, 1060)
    + g.footer(NAVY, 1160).replace('top:1240px', 'top:1242px'))

# S04 · crema partido: 19 % buscando información
bar = (f'<div class="abs" style="left:110px;top:780px;width:860px;height:70px;border-radius:35px;background:rgba(13,41,71,.10)"></div>'
       f'<div class="abs" style="left:110px;top:780px;width:{round(860 * .19)}px;height:70px;border-radius:35px;background:{ORANGE}"></div>'
       + ''.join(f'<div class="abs tg" style="left:{110 + i * 172}px;top:870px;width:172px;text-align:center;font-size:22px;color:{NAVY}">{d}</div>'
                 for i, d in enumerate(['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes'])))
add('S04-buscando-informacion',
    g.fill(CREAM) + g.dots(800, 70, NAVY, .12)
    + g.logo(solid=NAVY) + sabias(290, ORANGE_D)
    + g.head('Casi <span style="color:' + ORANGE_D + '">un día</span> a la semana', 380, 74, color=NAVY, width=940)
    + g.head('se va en buscar y reunir información.', 500, 52, color=NAVY, width=880)
    + g.text('Es el 19 % de la semana laboral.', 680, 32, color=NAVY)
    + bar
    + bouw('Una sola fuente de datos ordenada devuelve ese día.', 950, NAVY, '#fff')
    + fuente('McKinsey Global Institute.', NAVY, 1090)
    + g.footer(NAVY, 1160).replace('top:1240px', 'top:1242px'))

# S05 · amarillo: 60 % trabajo sobre el trabajo
add('S05-trabajo-sobre-el-trabajo',
    g.fill(YELLOW) + g.dots(40, 60, NAVY, .15)
    + g.logo(solid=NAVY) + sabias(290, NAVY)
    + g.head('60 %', 360, 280, color=ORANGE_D)
    + g.head('del día se va en "trabajo sobre el trabajo"', 660, 64, color=NAVY, width=900)
    + g.text('Correos de seguimiento, buscar archivos, actualizar estados, pedir datos. Todo lo que no es el trabajo para el que te contrataron.', 850, 30, color=NAVY, width=860)
    + fuente('Asana, Anatomy of Work Index, encuesta a más de 13 000 trabajadores.', NAVY, 1060)
    + g.footer(NAVY, 1160).replace('top:1240px', 'top:1242px'))

# S06 · foto real de planta: paros no planificados
add('S06-paros-no-planificados',
    f'<img class="abs" src="{g.data(g.site("mejora-linea-extrusion"), W)}" style="left:0;top:0;width:{W}px;height:{H}px;object-fit:cover;object-position:center 30%">'
    + f'<div class="abs" style="left:0;top:0;width:{W}px;height:{H}px;background:linear-gradient(180deg,rgba(13,41,71,.88) 0%,rgba(13,41,71,.72) 45%,rgba(6,20,43,.96) 100%)"></div>'
    + g.logo() + sabias(290, ORANGE)
    + g.head('<span style="color:' + ORANGE + '">11 %</span>', 360, 260)
    + g.head('de sus ingresos pierden las 500 empresas más grandes del mundo por paros no planificados.', 640, 54, width=900)
    + g.text('Si a ellas les pasa con todos sus recursos, en una planta mediana un paro pesa todavía más.', 860, 30, color='rgba(255,255,255,.88)', width=840)
    + fuente('Siemens, The True Cost of Downtime 2024.', 'rgba(255,255,255,.7)', 1060)
    + g.footer('#fff', 1160).replace('top:1240px', 'top:1242px'))

# S07 · azul con dos bloques: de 4 horas a 3 minutos
add('S07-de-4-horas-a-3-minutos',
    g.blue() + g.dots(780, 70, CYAN, .25)
    + g.logo() + sabias(290, CYAN)
    + stat(110, 380, 400, 260, '4 h', 'antes', 'rgba(255,255,255,.08)', '#fff', 110)
    + f'<div class="abs hd" style="left:520px;top:450px;width:40px;text-align:center;font-size:70px;color:{ORANGE}">→</div>'
    + stat(570, 380, 400, 260, '3 min', 'después', ORANGE, NAVY, 110)
    + g.head('Así bajó Toyota un cambio de formato en una prensa.', 700, 60, width=900)
    + g.text('El método se llama SMED. No compraron otra máquina: separaron lo que se puede preparar con la máquina andando.', 880, 30, color='rgba(255,255,255,.85)', width=860)
    + fuente('Shigeo Shingo, creador del método SMED.', 'rgba(255,255,255,.65)', 1070)
    + g.footer('#fff', 1160).replace('top:1240px', 'top:1242px'))

# S08 · cian partido con naranja: mensajería en México
add('S08-mensajeria-mexico',
    g.fill(CYAN)
    + f'<div class="abs" style="left:0;top:820px;width:{W}px;height:{H - 820}px;background:{NAVY}"></div>'
    + g.logo(solid=NAVY) + sabias(290, NAVY)
    + g.head('71 %', 350, 260, color=NAVY)
    + g.head('de los adultos en línea en México dice que escribir por mensaje es lo más rápido para tratar con empresas.', 610, 50, color=NAVY, width=900)
    + g.text('Si tu cliente ya está en WhatsApp, el pedido debería poder llegar ahí completo y sin veinte mensajes.', 870, 30, color='#fff', width=860)
    + fuente('Kantar, citado por Expansión.', 'rgba(255,255,255,.65)', 1050)
    + g.footer('#fff', 1160).replace('top:1240px', 'top:1242px'))

# S09 · naranja con tres cifras: las mipymes en América Latina
cif = [('99 %', 'de las empresas'), ('61 %', 'del empleo formal'), ('25 %', 'de la producción')]
c3 = ''.join(stat(110 + i * 292, 560, 276, 230, n, t, '#fff' if i < 2 else NAVY, NAVY if i < 2 else '#fff', 76) for i, (n, t) in enumerate(cif))
add('S09-mipymes-latam',
    g.fill(ORANGE) + g.dots(780, 60, '#fff', .35)
    + g.logo(solid='#ffffff') + sabias(290, NAVY)
    + g.head('Las pequeñas y medianas empresas en América Latina son…', 360, 54, color='#fff', width=920)
    + c3
    + g.head('…pero producen solo un cuarto.', 830, 56, color=NAVY, width=900)
    + g.text('La diferencia no es el esfuerzo. Es la productividad: procesos, datos y herramientas.', 920, 30, color=NAVY, width=840)
    + fuente('CEPAL, Comisión Económica para América Latina y el Caribe.', NAVY, 1060)
    + g.footer(NAVY, 1160).replace('top:1240px', 'top:1242px'))

for name, body in pieces:
    open(os.path.join(OUT, name + '.html'), 'w').write(
        f'<!doctype html><html lang="es"><head><meta charset="utf-8"><style>{g.CSS}</style></head><body><section class="slide">{body}</section></body></html>')
open(os.path.join(OUT, 'list.txt'), 'w').write('\n'.join(f'{n}:{W}x{H}' for n, _ in pieces))
print(len(pieces), 'piezas')
