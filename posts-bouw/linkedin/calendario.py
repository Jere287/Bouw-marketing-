"""Arma la carpeta PUBLICAR: una carpeta por día con la imagen (o el PDF del carrusel) y publicar.txt.

Mezcla la serie D (textos_marca.py) con la serie A de automatización (abajo) y alterna los colores
para que el feed no se vea igual: azul, naranja, cian, crema, foto.
Uso: python3 calendario.py
"""
import os, shutil
from textos_marca import POSTS as D

DD = {p[1]: p for p in D}

A = {
    'A11-lunes-a-mano.png': ("""¿Cuántas horas pierde tu equipo cada lunes haciendo esto a mano?

Estas son las cinco tareas que más encontramos en las empresas que nos llaman:
• Armar el reporte de ventas de la semana.
• Pasar los pedidos de WhatsApp a un Excel.
• Actualizar el inventario a mano.
• Recordar a los clientes los pagos pendientes.
• Copiar datos de un sistema a otro.

Las cinco se pueden automatizar, y casi nunca hace falta comprar un sistema nuevo.

¿Cuál es la que más horas le quita a tu equipo? Dinos el número en los comentarios o por mensaje y te contamos cómo la resolveríamos.

#BOUW #Automatización #Productividad #Pymes""",
        'Haz la cuenta de tu tarea: bouw-eight.vercel.app',
        'Lista de BOUW sobre fondo naranja: 5 cosas que tu equipo hace a mano cada lunes.'),
    'A13-240-horas.png': ("""240 horas al año.

Es lo que suma una tarea que parece pequeña: copiar datos media hora, cinco veces por semana, entre dos personas.

Son casi un mes y medio de trabajo de una persona, todos los años, en algo que no agrega valor.

Lo que más nos sorprende no es el número. Es que casi nadie lo había calculado antes.

¿Quieres saber cuánto suma una tarea de tu empresa? Escríbenos y hacemos la cuenta juntos, sin costo.

#BOUW #Automatización #Productividad #Pymes""",
        'La calculadora, 30 segundos: bouw-eight.vercel.app',
        'Cifra de BOUW sobre fondo cian: 240 horas al año copiando datos.'),
    'A14-mito-realidad.png': ("""Mito: "Automatizar es caro y necesito un sistema nuevo."

Es lo que más escuchamos antes de empezar un proyecto. Y casi nunca es cierto.

Lo que vemos en la práctica:
• La mayoría de las empresas ya tiene la información en Excel.
• El problema es que está repartida en varios archivos que no se hablan.
• Conectarlos bien cuesta mucho menos que un sistema nuevo.

En un taller de manufactura lo hicimos con 11 hojas conectadas en un solo archivo y cero licencias nuevas.

¿Te frenó alguna vez este mito? Escríbenos y revisamos tu caso.

#BOUW #Automatización #Excel #Pymes""",
        'El caso: bouw-eight.vercel.app',
        'Mito y realidad de BOUW: automatizar no siempre requiere un sistema nuevo; basta el Excel que ya usas, bien conectado.'),
    'A12-antes-despues-cotizar.png': ("""Cotizar a mano tiene seis pasos. Y se repiten con cada cliente.

Leer el mensaje, buscar el precio, calcular, escribir la cotización, enviarla y esperar respuesta.

Con un cotizador en la web el cliente elige, el precio se calcula solo y el pedido llega a tu WhatsApp ya escrito. Tú solo confirmas.

Así lo hicimos para un taller de regalos que vende por chat.

Si tu equipo pasa horas cotizando, escríbenos y te mostramos cómo funciona.

#BOUW #Automatización #Ventas #WhatsAppBusiness""",
        'Pruébalo: charms-ecuador.vercel.app',
        'Antes y después de BOUW: cotizar a mano en 6 pasos frente a un pedido que llega escrito.'),
    'A15-semaforo.png': ("""No todo hay que automatizarlo.

Sí, lo dice una empresa que automatiza.

Nuestra regla es simple:
• Menos de 40 horas al año: no lo automatices, cuesta más de lo que ahorra.
• De 40 a 150 horas: está en la frontera, vale si además te cuesta errores.
• Más de 150 horas: aquí sí, es casi un mes de trabajo de una persona.

Preferimos decirte que no vale la pena antes que venderte algo que no necesitas.

¿En qué color cae tu tarea? Escríbenos y la medimos contigo.

#BOUW #Automatización #Procesos #Pymes""",
        'Calcúlalo en 30 segundos: bouw-eight.vercel.app',
        'Semáforo de BOUW: menos de 40 horas al año no automatices, de 40 a 150 está en la frontera, más de 150 sí.'),
    'A16-chat-whatsapp.png': ("""¿Cuántos mensajes necesitas para cerrar un pedido por WhatsApp?

Normalmente son veinte: qué modelo, qué tamaño, para cuándo, cuánto cuesta.

Con una web con cotizador, el cliente llega al chat con todo ya escrito: el producto, los detalles y la fecha. Tu equipo solo confirma y cobra.

Funciona para talleres, tiendas, servicios y cualquier negocio que hoy vende por chat.

¿Vendes por WhatsApp? Escríbenos y te mostramos un ejemplo funcionando.

#BOUW #WhatsAppBusiness #Ventas #Automatización""",
        'Ejemplo en vivo: charms-ecuador.vercel.app',
        'Chat de WhatsApp de ejemplo donde el pedido llega escrito desde la web, con el texto "Sin veinte mensajes de ida y vuelta".'),
    'A17-reporte-del-lunes.png': ("""El reporte que alguien arma cada lunes puede llegar solo.

En muchas empresas hay una persona que dedica la mañana del lunes a juntar ventas, gastos e inventario en un reporte.

Con un tablero conectado a los datos que ya se capturan, ese reporte se recalcula con cada movimiento. El lunes ya está listo.

Empieza el año sin esa tarea. Escríbenos y te decimos cuánto tardaría en tu caso.

#BOUW #Automatización #Reportes #Pymes""",
        'Mira el tablero: bouw-eight.vercel.app',
        'Pieza de BOUW con la captura de un tablero en Excel: el reporte del lunes puede llegar solo.'),
    'BOUW-carrusel-5-tareas.pdf': ("""5 tareas que puedes automatizar este mes, sin comprar un sistema nuevo.

Reportes, cotizaciones, inventario, cobranza y cierre de mes. Las cinco aparecen en casi todas las empresas que visitamos, y las cinco se pueden resolver con las herramientas que ya tienes.

Desliza para ver cómo.

¿Cuál de las cinco te quita más horas? Escríbenos el número y te decimos cómo lo haríamos.

#BOUW #Automatización #Productividad #Pymes""",
        'Más casos: bouw-eight.vercel.app',
        None),
}

# fecha, archivo (serie D o A), en orden alterno de color
CAL = [('Jueves 19 nov', 'D02-caso-reprocesos.png'), ('Martes 24 nov', 'A11-lunes-a-mano.png'),
       ('Miércoles 25 nov', 'A13-240-horas.png'), ('Jueves 26 nov', 'D06-pregunta-auditoria.png'),
       ('Martes 1 dic', 'BOUW-carrusel-5-tareas.pdf'), ('Miércoles 2 dic', 'D05-caso-cierre-de-mes.png'),
       ('Jueves 3 dic', 'A14-mito-realidad.png'), ('Martes 8 dic', 'A12-antes-despues-cotizar.png'),
       ('Miércoles 9 dic', 'D07-caso-whatsapp.png'), ('Jueves 10 dic', 'A15-semaforo.png'),
       ('Martes 15 dic', 'BOUW-carrusel-3-errores.pdf'), ('Miércoles 16 dic', 'A16-chat-whatsapp.png'),
       ('Jueves 17 dic', 'D09-como-trabajamos.png'), ('Martes 5 ene', 'A17-reporte-del-lunes.png'),
       ('Miércoles 6 ene', 'D04-frase-si-se-repite.png'), ('Jueves 7 ene', 'D08-tip-tres-archivos.png'),
       ('Martes 12 ene', 'D10-cuentanos.png')]
TITULO = {'BOUW-carrusel-5-tareas.pdf': '5 tareas que puedes automatizar este mes',
          'BOUW-carrusel-3-errores.pdf': '3 errores al automatizar tu empresa'}

HERE = os.path.dirname(os.path.abspath(__file__))
base = os.path.join(HERE, 'PUBLICAR')
shutil.rmtree(base, ignore_errors=True)
os.makedirs(base)
tabla = []
for i, (fecha, f) in enumerate(CAL, 1):
    if f in A:
        txt, com, alt = A[f]
    else:
        _, _, txt, com, alt = DD[f]
    year = '2027' if 'ene' in fecha else '2026'
    code = f.split('-')[0] if not f.endswith('.pdf') else ('A18-carrusel' if '5-tareas' in f else 'D03-carrusel')
    d = os.path.join(base, f'{i:02d}_{fecha.split()[1]}-{fecha.split()[2]}_{code}')
    os.makedirs(d)
    src = os.path.join(HERE, f) if f.endswith('.pdf') else os.path.join(HERE, 'png', f)
    shutil.copy(src, os.path.join(d, f if f.endswith('.pdf') else 'imagen.png'))
    paso2 = (f'2) DOCUMENTO: sube el PDF con "Añadir documento" (no como imagen). Título del documento:\n   {TITULO[f]}'
             if f.endswith('.pdf') else f'2) IMAGEN: imagen.png\n   Al subirla toca "Texto alternativo" y pega:\n   {alt}')
    open(os.path.join(d, 'publicar.txt'), 'w').write(
        f'FECHA: {fecha} {year}, 08:00 Quito / 07:00 Monterrey\n\n1) TEXTO (copiar y pegar):\n\n{txt}\n\n{paso2}\n\n'
        f'3) PRIMER COMENTARIO (apenas salga la publicación):\n   {com}\n\n'
        f'4) Responde todos los comentarios en la primera hora. A quien diga que le pasa, escríbele por mensaje privado.\n')
    tabla.append(f'{i:02d}  {fecha} {year}  {code}')
open(os.path.join(base, 'CALENDARIO.txt'), 'w').write(
    'BOUW · LinkedIn · calendario (martes, miércoles y jueves, 08:00 Quito / 07:00 Monterrey)\n'
    'Pausa del 18 de diciembre al 4 de enero.\n\n' + '\n'.join(tabla) + '\n')
print('\n'.join(tabla))
