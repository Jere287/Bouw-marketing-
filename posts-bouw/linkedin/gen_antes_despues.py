# Genera la serie V (antes y después reales del sitio) -> html_antes_despues/*.html
# Luego: NODE_PATH=$(npm root -g) node shot_antes_despues.js
import os
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'html_antes_despues')
FONTS = '../../fonts/'
IMG = '../../sitio/imagenes/'
CSS = f'''
@font-face{{font-family:"Archivo";src:url({FONTS}Archivo-100_900.woff2);font-weight:100 900;font-stretch:62% 125%}}
@font-face{{font-family:"Plex";src:url({FONTS}IBMPlexSans-400.woff2);font-weight:400}}
@font-face{{font-family:"PlexMono";src:url({FONTS}IBMPlexMono-500.woff2);font-weight:500}}
*{{margin:0;padding:0;box-sizing:border-box}}
.slide{{position:relative;overflow:hidden;width:1080px;height:1350px;font-family:"Plex",sans-serif;color:#0d2947}}
.abs{{position:absolute}}
.hd{{font-family:"Archivo";font-weight:800;letter-spacing:-0.02em;line-height:1.02}}
.tg{{font-family:"Archivo";font-weight:700;letter-spacing:0.08em;text-transform:uppercase}}
.tx{{font-family:"Plex";line-height:1.38}}
.mn{{font-family:"PlexMono";font-weight:500}}
.cream{{background:#fbf6ea}} .navy{{background:#0d2947;color:#fff}}
.or{{color:#e87722}} .cy{{color:#4fd6e8}}
.chip{{position:absolute;font-family:"Archivo";font-weight:700;letter-spacing:.08em;text-transform:uppercase;font-size:22px;padding:9px 20px;border-radius:40px}}
.chip.hoy{{background:#fbf6ea;color:#e87722;border:2.5px solid #e87722}}
.chip.bouw{{background:#0d2947;color:#4fd6e8;border:2.5px solid #4fd6e8}}
.ph{{position:absolute;border-radius:14px;overflow:hidden;background-size:cover}}
.ph img{{width:100%;height:100%;object-fit:cover;display:block}}
'''
def page(body):
    return f'<!doctype html><html lang="es"><head><meta charset="utf-8"><style>{CSS}</style></head><body><section class="slide">{body}</section></body></html>'

def write(name, body):
    open(os.path.join(D, name + '.html'), 'w').write(page(body))

# ---------- V01 / V02: antes y después apilado ----------
def stacked(name, head, imgA, imgB, chipA, chipB, posA, posB, stats, nota):
    st = ''.join(
        f'<div class="abs" style="left:{70+i*320}px;top:1190px;width:300px">'
        f'<div class="hd cy" style="font-size:44px;white-space:nowrap">{n}</div>'
        f'<div class="tx" style="font-size:19px;color:#c6d4e4;margin-top:6px">{l}</div></div>'
        for i,(n,l) in enumerate(stats))
    body = f'''
<div class="abs cream" style="left:0;top:0;width:1080px;height:720px"></div>
<div class="abs navy" style="left:0;top:720px;width:1080px;height:630px"></div>
<img class="abs" src="logo-oscuro.png" style="left:70px;top:30px;width:150px;height:79px">
<div class="abs hd" style="left:70px;top:118px;width:940px;font-size:62px">{head}</div>
<div class="ph" style="left:70px;top:262px;width:940px;height:440px"><img src="{imgA}" style="object-position:{posA}"></div>
<div class="chip hoy" style="left:94px;top:284px">{chipA}</div>
<div class="ph" style="left:70px;top:738px;width:940px;height:420px;border:2px solid #4fd6e8"><img src="{imgB}" style="object-position:{posB}"></div>
<div class="chip bouw" style="left:94px;top:760px">{chipB}</div>
{st}
<div class="abs mn" style="left:70px;top:1292px;width:940px;font-size:19px;color:#8fa8c4">{nota}</div>
'''
    write(name, body)

stacked('V01-planta-antes-despues',
 'Misma planta.<br><span class="or">Un solo flujo.</span>',
 IMG+'lean-antes.png', IMG+'lean-despues.png', 'Hoy', 'Con BOUW', 'center 55%', 'center 55%',
 [('−15 %','tiempo de preparación (caso real)'),('−20 %','reprocesos (caso real)'),('29 → 8 min','tiempo de entrega (modelo)')],
 'Caso: línea de dos turnos. Entrega: simulación de una línea de 4 estaciones.')

stacked('V02-auditoria-antes-despues',
 'La auditoría llega.<br><span class="or">¿Tu carpeta está lista?</span>',
 'cump-antes.png', 'cump-despues.png', 'Hoy', 'Con BOUW', 'center 40%', 'center 40%',
 [('33→100 %','preparación para inspección'),('9 → 0','CAPA abiertas'),('3 → 0','lotes retenidos')],
 'Planta de ejemplo (ilustrativo). Informe de auditoría BPM simulado.')

# ---------- V03: carrusel del juego ----------
PTS = [(32.8,48),(24.2,58.9),(70.3,44.3),(58.6,80.9),(50,43.1),(62.9,25.1)]
W = [
 ('Espera','VSM','Un operador parado, esperando a que la estación de antes le pase piezas.','Balanceo de línea: cada estación al ritmo de la línea, con el mapa de flujo de valor.'),
 ('Inventario en proceso','WIP','Piezas apiladas frente a la máquina más lenta. Ahí está el cuello de botella.','Nivelación de flujo: las piezas pasan una a una por la banda, sin montones.'),
 ('Movimiento','5S','Buscar herramientas y piezas entre el desorden, varias veces por turno.','5S y trabajo estándar: cada cosa en su sitio. En el caso de mejora continua, la preparación bajó 15 %.'),
 ('Transporte','Layout','Recorridos largos que se cruzan para llevar una caja de un lado a otro.','Rediseño de layout: lo que se usa junto va junto, y el flujo va en un solo sentido.'),
 ('Sobreproducción','VSM','Cajas hechas antes de que alguien las pida, bloqueando el pasillo y el montacargas.','Producir al ritmo de lo que se vende, con el mapa de valor a la vista de todos.'),
 ('Defectos','Causa raíz','Máquina en rojo: piezas que vuelven a pasar por reproceso.','Acciones correctivas con su causa raíz. En el caso, los reprocesos bajaron 20 %.'),
]
dots = ''.join(
  f'<div class="abs" style="left:calc({x}% - 26px);top:calc({y}% - 26px);width:52px;height:52px;border-radius:50%;background:#e87722;border:3px solid #fff;color:#fff;font-family:Archivo;font-weight:800;font-size:28px;text-align:center;line-height:46px;box-shadow:0 0 0 8px rgba(232,119,34,.35)">{i+1}</div>'
  for i,(x,y) in enumerate(PTS))
write('V03-1-portada', f'''
<div class="abs navy" style="left:0;top:0;width:1080px;height:1350px"></div>
<img class="abs" src="logo-claro.png" style="left:70px;top:44px;width:170px;height:72px">
<div class="abs tg cy" style="left:70px;top:150px;font-size:22px">Pruébalo · 30 segundos</div>
<div class="abs hd" style="left:70px;top:196px;width:940px;font-size:78px;color:#fff">Seis formas de perder horas en una planta. <span class="or">¿Ves las seis?</span></div>
<div class="abs" style="left:70px;top:590px;width:940px;height:604px"><div class="ph" style="left:0;top:0;width:940px;height:604px"><img src="{IMG}lean-antes.png"></div>{dots}</div>
<div class="abs mn" style="left:70px;top:1240px;font-size:24px;color:#8fa8c4">Desliza → cada una, con su costo y cómo se arregla</div>
''')
for i,(n,tag,costo,fix) in enumerate(W, start=1):
    write(f'V03-{i+1}-desperdicio-{i}', f'''
<div class="abs cream" style="left:0;top:0;width:1080px;height:1350px"></div>
<div class="abs tg" style="left:70px;top:60px;font-size:22px;color:#4a6d8c">Desperdicio {i} de 6</div>
<div class="abs mn" style="right:70px;top:58px;font-size:22px;color:#1a97b3;border:2px solid #1a97b3;border-radius:30px;padding:6px 18px">{tag}</div>
<div class="abs hd" style="left:70px;top:112px;width:940px;font-size:92px">{n}</div>
<div class="ph" style="left:70px;top:262px;width:455px;height:341px"><img src="../../sitio/antes-despues/juego/desperdicio-{i}-antes.png"></div>
<div class="ph" style="left:555px;top:262px;width:455px;height:341px;border:2px solid #1a97b3"><img src="../../sitio/antes-despues/juego/desperdicio-{i}-despues.png"></div>
<div class="chip hoy" style="left:90px;top:282px;font-size:19px;padding:7px 16px">Hoy</div>
<div class="chip bouw" style="left:575px;top:282px;font-size:19px;padding:7px 16px">Con BOUW</div>
<div class="abs tg or" style="left:70px;top:674px;font-size:24px">Lo que cuesta</div>
<div class="abs tx" style="left:70px;top:724px;width:940px;font-size:44px;line-height:1.3">{costo}</div>
<div class="abs tg" style="left:70px;top:930px;font-size:24px;color:#1a97b3">Cómo se arregla</div>
<div class="abs tx" style="left:70px;top:988px;width:940px;font-size:44px;line-height:1.3;font-weight:400">{fix}</div>
<div class="abs mn" style="left:70px;top:1290px;font-size:20px;color:#4a6d8c">{i} / 6 · www.bouwlatam.com</div>
''')
write('V03-8-cierre', '''
<div class="abs navy" style="left:0;top:0;width:1080px;height:1350px"></div>
<img class="abs" src="logo-claro.png" style="left:70px;top:44px;width:170px;height:72px">
<div class="abs hd" style="left:70px;top:210px;width:940px;font-size:88px;color:#fff">Tu planta tiene los suyos. <span class="cy">Vamos a medirlos.</span></div>
<div class="abs tx" style="left:70px;top:600px;width:900px;font-size:40px;color:#c6d4e4">Si no los ves todos, no pasa nada: para eso medimos. Antes de proponerte algo, hacemos la cuenta. Si el número no da, te lo decimos.</div>
<div class="abs" style="left:70px;top:900px;width:940px;height:150px;background:#17406b;border-radius:18px"></div>
<div class="abs hd" style="left:110px;top:930px;font-size:50px;color:#fff">Radiografía gratis · 1 hora</div>
<div class="abs tx" style="left:110px;top:1000px;font-size:28px;color:#c6d4e4">Escríbenos por WhatsApp +593 96 368 4012</div>
<div class="abs mn" style="left:70px;top:1270px;font-size:26px;color:#4fd6e8;letter-spacing:.08em">WWW.BOUWLATAM.COM</div>
''')
print('ok', len(os.listdir(D)))
