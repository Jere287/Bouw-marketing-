"""Arma la carpeta PUBLICAR-SABIAS-QUE: serie S "¿Sabías que…?" con datos reales y su fuente.
Cada carpeta trae imagen.png y publicar.txt (fecha, texto, texto alternativo, primer comentario con la fuente).
Uso: python3 calendario_datos.py
"""
import os, shutil

S = [
    ('S01-hojas-de-calculo.png', """¿Sabías que 9 de cada 10 hojas de cálculo auditadas tenían errores?

En una auditoría de 54 hojas de cálculo usadas en empresas reales, 49 tenían al menos un error. Lo documentó Raymond Panko, investigador de la Universidad de Hawái que lleva años estudiando el tema.

El problema no es Excel. Es que muchas decisiones importantes (precios, inventario, pagos) salen de archivos que nadie revisó desde que se hicieron.

Tres señales de que tu archivo necesita una revisión:
• Varias personas lo editan y nadie sabe qué cambió.
• Hay fórmulas que nadie se atreve a tocar.
• Los totales no cuadran con otros reportes.

Si tus números salen de un Excel, escríbenos y lo revisamos contigo.

#BOUW #Excel #Datos #Pymes""",
     'Fuente: Raymond R. Panko, "What We Know About Spreadsheet Errors", Universidad de Hawái. Más en bouw-eight.vercel.app',
     '¿Sabías que…? 9 de cada 10 hojas de cálculo auditadas tenían errores. Fuente: Raymond Panko, Universidad de Hawái.'),
    ('S02-45-por-ciento.png', """¿Sabías que el 45 % de las actividades del trabajo se pueden automatizar con tecnología que ya existe?

Lo calculó McKinsey analizando unas 2 000 actividades laborales. El dato importante no es que desaparezcan puestos: menos del 5 % se pueden automatizar completos.

Lo que sí se automatiza son tareas dentro de cada puesto:
• Copiar datos de un lugar a otro.
• Buscar información.
• Calcular y armar reportes.

Eso es justo lo que le quita horas a un equipo pequeño.

¿Qué tarea de tu equipo cabe en esa lista? Cuéntanos y te decimos si vale la pena automatizarla.

#BOUW #Automatización #Productividad #FuturoDelTrabajo""",
     'Fuente: McKinsey Global Institute, "Four fundamentals of workplace automation". Más en bouw-eight.vercel.app',
     '¿Sabías que…? El 45 % de las actividades del trabajo se pueden automatizar con tecnología que ya existe. Fuente: McKinsey Global Institute.'),
    ('S03-costo-mala-calidad.png', """¿Sabías que la mala calidad cuesta, en promedio, el 15 % de las ventas de una empresa manufacturera?

Es lo que se pierde en reprocesos, desperdicio, devoluciones, inspecciones extra y reclamos. Según el Institute of Industrial and Systems Engineers, el rango va del 5 % al 35 %, según la complejidad del producto.

Lo difícil es que ese costo casi nunca aparece como una línea en los estados financieros. Está repartido en horas extra, material perdido y clientes que no vuelven.

Medirlo es el primer paso para bajarlo. En una línea de extrusión bajamos los reprocesos un 20 % sin comprar maquinaria.

¿Sabes cuánto te cuesta a ti? Escríbenos y lo medimos.

#BOUW #Calidad #MejoraContinua #Manufactura""",
     'Fuente: IISE, "Measuring the cost of quality". Más en bouw-eight.vercel.app',
     '¿Sabías que…? El 15 % de las ventas se va en reprocesos, desperdicio y devoluciones. Fuente: IISE.'),
    ('S04-buscando-informacion.png', """¿Sabías que casi un día de cada semana laboral se va en buscar y reunir información?

McKinsey lo midió en el 19 % de la semana: buscar archivos, pedir datos a otra área, preguntar cuál es la versión correcta.

En una empresa pequeña eso se nota todavía más, porque la misma persona que busca es la que tiene que vender, producir o cobrar.

La solución suele ser simple:
• Una sola fuente de datos, no tres archivos.
• Cada dato se captura una vez.
• Los reportes se arman solos desde ahí.

¿Cuánto tiempo pierde tu equipo buscando información? Escríbenos y lo revisamos.

#BOUW #Productividad #Datos #Pymes""",
     'Fuente: McKinsey Global Institute, "The Social Economy" (2012). Más en bouw-eight.vercel.app',
     '¿Sabías que…? Casi un día a la semana se va en buscar y reunir información, el 19 % de la semana laboral. Fuente: McKinsey Global Institute.'),
    ('S05-trabajo-sobre-el-trabajo.png', """¿Sabías que el 60 % del día de trabajo se va en "trabajo sobre el trabajo"?

Así lo llama el estudio Anatomy of Work de Asana, que encuestó a más de 13 000 trabajadores: correos de seguimiento, buscar archivos, actualizar estados, pedir datos.

Es todo lo que rodea al trabajo, pero no es el trabajo.

Buena parte de eso son tareas repetitivas que se pueden automatizar o eliminar con un proceso más claro.

Si sientes que tu equipo está ocupado todo el día pero avanza poco, escríbenos. Empezamos midiendo dónde se va el tiempo.

#BOUW #Productividad #Procesos #Automatización""",
     'Fuente: Asana, Anatomy of Work Index 2021. Más en bouw-eight.vercel.app',
     '¿Sabías que…? El 60 % del día se va en trabajo sobre el trabajo. Fuente: Asana, Anatomy of Work Index.'),
    ('S06-paros-no-planificados.png', """¿Sabías que las 500 empresas más grandes del mundo pierden el 11 % de sus ingresos por paros no planificados?

Lo publicó Siemens en su estudio The True Cost of Downtime 2024. Son alrededor de 1,4 billones de dólares al año.

Si eso le pasa a empresas con equipos de mantenimiento completos, en una planta mediana cada paro pesa todavía más.

La mayoría de los paros no son sorpresa: avisan antes con señales que nadie está midiendo.
• Tiempos de ciclo que se alargan.
• Temperaturas fuera de rango.
• Reprocesos que suben poco a poco.

¿Cuántas horas de paro tuvo tu planta este mes? Escríbenos y revisamos tu línea.

#BOUW #Mantenimiento #Manufactura #MejoraContinua""",
     'Fuente: Siemens, "The True Cost of Downtime 2024". Más en bouw-eight.vercel.app',
     '¿Sabías que…? El 11 % de los ingresos se pierde por paros no planificados en las 500 empresas más grandes. Fuente: Siemens 2024. Sobre la foto de una línea de extrusión.'),
    ('S07-de-4-horas-a-3-minutos.png', """¿Sabías que Toyota bajó un cambio de formato de 4 horas a 3 minutos?

Lo logró Shigeo Shingo con un método que hoy se usa en plantas de todo el mundo: SMED.

La idea central es simple: separar lo que solo se puede hacer con la máquina parada de lo que se puede preparar mientras sigue produciendo.

No hace falta llegar a 3 minutos para que valga la pena. En una línea de extrusión bajamos el tiempo de preparación un 15 % con este mismo principio.

¿Cuánto tarda hoy un cambio de formato en tu línea? Escríbenos y lo medimos juntos.

#BOUW #SMED #Lean #Manufactura""",
     'Fuente: Shigeo Shingo, "A Revolution in Manufacturing: The SMED System". Más en bouw-eight.vercel.app',
     '¿Sabías que…? Toyota bajó un cambio de formato de 4 horas a 3 minutos con el método SMED.'),
    ('S08-mensajeria-mexico.png', """¿Sabías que el 71 % de los adultos en línea en México dice que escribir por mensaje es lo más rápido para tratar con una empresa?

Es un dato de Kantar publicado por Expansión. Tus clientes ya están en WhatsApp; la pregunta es si tu negocio está listo para recibirlos ahí.

Lo que suele pasar: el cliente pregunta el precio, se cruzan veinte mensajes y a veces la venta se pierde en el camino.

Una web con catálogo y cotizador puede mandar el pedido a WhatsApp ya escrito, con el producto, los detalles y el precio. Así lo hicimos para un taller en Ecuador.

¿Vendes por WhatsApp? Escríbenos y te mostramos un ejemplo funcionando.

#BOUW #WhatsAppBusiness #Ventas #México""",
     'Fuente: Kantar, citado por Expansión (2025). Ejemplo en vivo: charms-ecuador.vercel.app',
     '¿Sabías que…? El 71 % de los adultos en línea en México dice que la mensajería es lo más rápido para tratar con empresas. Fuente: Kantar.'),
    ('S09-mipymes-latam.png', """¿Sabías que las pymes son el 99 % de las empresas de América Latina, pero producen solo el 25 %?

Según la CEPAL, también generan el 61 % del empleo formal. La diferencia está en la productividad: en promedio, una empresa pequeña produce mucho menos por persona que una grande.

No es por falta de esfuerzo. Casi siempre es por procesos que dependen de la memoria de alguien, datos repartidos en varios archivos y tareas que se repiten a mano.

Esa brecha es justo donde trabajamos: ordenar el proceso, medirlo y automatizar lo que se repite.

Si tienes una pyme y quieres crecer sin contratar el doble, escríbenos.

#BOUW #Pymes #Productividad #AméricaLatina""",
     'Fuente: CEPAL, "Mipymes en América Latina: un frágil desempeño y nuevos desafíos para las políticas de fomento". Más en bouw-eight.vercel.app',
     '¿Sabías que…? Las pymes son el 99 % de las empresas y el 61 % del empleo formal en América Latina, pero el 25 % de la producción. Fuente: CEPAL.'),
]

# Fechas: un "¿Sabías que…?" cada viernes, sin chocar con el calendario aprobado de martes a jueves.
FECHAS = ['Viernes 20 nov 2026', 'Viernes 27 nov 2026', 'Viernes 4 dic 2026', 'Viernes 11 dic 2026', 'Viernes 18 dic 2026',
          'Viernes 8 ene 2027', 'Viernes 15 ene 2027', 'Viernes 22 ene 2027', 'Viernes 29 ene 2027']

HERE = os.path.dirname(os.path.abspath(__file__))
base = os.path.join(HERE, 'PUBLICAR-SABIAS-QUE')
shutil.rmtree(base, ignore_errors=True)
os.makedirs(base)
tabla = []
for i, ((f, txt, com, alt), fecha) in enumerate(zip(S, FECHAS), 1):
    d = os.path.join(base, f'{i:02d}_{fecha.split()[1]}-{fecha.split()[2]}_{f[:3]}')
    os.makedirs(d)
    shutil.copy(os.path.join(HERE, 'png', f), os.path.join(d, 'imagen.png'))
    open(os.path.join(d, 'publicar.txt'), 'w').write(
        f'FECHA: {fecha}, 08:00 Quito / 07:00 Monterrey\n\n1) TEXTO (copiar y pegar):\n\n{txt}\n\n'
        f'2) IMAGEN: imagen.png\n   Al subirla toca "Texto alternativo" y pega:\n   {alt}\n\n'
        f'3) PRIMER COMENTARIO (con la fuente, apenas salga la publicación):\n   {com}\n\n'
        f'4) Responde todos los comentarios en la primera hora. A quien diga que le pasa, escríbele por mensaje privado.\n')
    tabla.append(f'{i:02d}  {fecha}  {f[:-4]}')
open(os.path.join(base, 'CALENDARIO.txt'), 'w').write(
    'BOUW · LinkedIn · serie "¿Sabías que…?" (datos reales con fuente)\n'
    'Va los viernes, para sumarse al calendario aprobado de martes a jueves sin chocar.\n\n' + '\n'.join(tabla) + '\n')
print('\n'.join(tabla))
