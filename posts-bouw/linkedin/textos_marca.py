"""Textos de la serie D (los usa calendario.py para armar la carpeta PUBLICAR).

Formato copiado de lo que publica Hanova Consulting en LinkedIn (pregunta o idea de entrada, explicación corta,
lista de 3 puntos con viñeta, frase de cierre, hashtags con el nombre de la firma), con una diferencia:
cada texto termina con una invitación concreta para que el posible cliente escriba.
"""
import os, shutil

POSTS = [
    ('Jueves 19 nov', 'D01-tip-haz-la-cuenta.png', """¿Cuánto le cuesta a tu empresa una tarea que se hace a mano?

Muchas veces se decide comprar un sistema sin saber cuánto cuesta el problema que se quiere resolver.

Un ejemplo que vemos seguido: media hora, cinco veces por semana, entre dos personas. Parece poco, pero al año son 240 horas. Casi un mes y medio de trabajo de una persona.

Antes de invertir en cualquier herramienta, conviene responder tres preguntas:
• ¿Cuántas veces se repite la tarea?
• ¿Cuánto tiempo toma cada vez y cuántas personas intervienen?
• ¿Qué errores o retrasos provoca?

Con esa cuenta en la mano, la decisión deja de ser una apuesta.

Si quieres hacer la cuenta de una tarea de tu empresa, escríbenos por mensaje y la calculamos contigo sin costo.

#BOUW #Automatización #Productividad #Pymes""",
     'Calcula la tuya en 30 segundos: www.bouwlatam.com',
     'Tip del día de BOUW: 30 minutos, 5 veces por semana, 2 personas equivalen a 240 horas al año.'),

    ('Martes 24 nov', 'D02-caso-reprocesos.png', """En una línea de extrusión bajamos los reprocesos un 20 %.

No compramos maquinaria nueva ni cambiamos de proveedor. El trabajo fue otro:
• Medimos en piso los tiempos, los recorridos y los rechazos.
• Ordenamos el flujo y estandarizamos el cambio de formato.
• Capacitamos a cuatro operadores para sostener el estándar.

El tiempo de preparación también bajó un 15 %.

En la mayoría de las plantas la capacidad ya existe. Lo que falta es que el flujo tenga sentido.

Si tu línea tiene reprocesos o cambios de formato lentos, escríbenos y agendamos una evaluación técnica.

#BOUW #MejoraContinua #Lean #Manufactura""",
     'El caso completo: www.bouwlatam.com',
     'Caso real de BOUW sobre la foto de una línea de extrusión: −20 % de reprocesos y −15 % en tiempo de preparación.'),

    ('Miércoles 25 nov', 'BOUW-carrusel-3-errores.pdf', """3 errores que vemos al automatizar una empresa (y cómo evitarlos).

Automatizar puede ahorrar cientos de horas al año. Pero hecho sin método, termina costando más de lo que ahorra.

En el carrusel te contamos los tres errores más comunes que encontramos en las empresas que nos llaman.

¿Te pasa alguno? Escríbenos por mensaje y en una llamada de 20 minutos te decimos qué haríamos primero.

#BOUW #Automatización #TransformaciónDigital #Pymes""",
     'Más sobre cómo trabajamos: www.bouwlatam.com',
     'Carrusel de BOUW: 3 errores al automatizar tu empresa.'),

    ('Jueves 26 nov', 'D04-frase-si-se-repite.png', """Si se repite, se automatiza.

Es la regla con la que trabajamos en BOUW, y tiene dos partes que importan igual:
• Si una tarea no se repite, no se automatiza: se ordena.
• Si un proceso no se mide, todavía no se toca.

Automatizar sin estas dos reglas es invertir a ciegas.

¿Qué tarea se repite todas las semanas en tu empresa? Cuéntanos y te decimos si vale la pena automatizarla.

#BOUW #FraseDeLaSemana #Automatización #MejoraContinua""",
     'www.bouwlatam.com',
     'Frase de la semana de BOUW: "Si se repite, se automatiza", sobre la foto de una pieza extruida.'),

    ('Martes 1 dic', 'D05-caso-cierre-de-mes.png', """El cierre de mes que se armaba a mano, ahora sale solo.

Un taller de manufactura llevaba inventario, kits, ventas y caja en archivos separados. Cada fin de mes, alguien pasaba días juntándolos.

Lo que hicimos:
• Un ERP pequeño dentro de un solo Excel, con 11 hojas conectadas.
• Un tablero que se recalcula con cada movimiento.
• Cero licencias nuevas y cero migración: el equipo siguió en la herramienta que ya conocía.

No siempre hace falta un sistema nuevo. A veces hace falta que el que ya tienes trabaje solo.

Si tu cierre de mes todavía se arma a mano, escríbenos.

#BOUW #Automatización #Excel #Pymes""",
     'Mira el proyecto: www.bouwlatam.com',
     'Caso real de BOUW: tablero del Programa contable en Excel, con 11 hojas conectadas y 0 licencias.'),

    ('Miércoles 2 dic', 'D06-pregunta-auditoria.png', """¿Tu planta pasaría una auditoría mañana, sin aviso?

Para responder con seguridad, deberías poder decir que sí a estas tres:
• Cada registro tiene su sitio y su responsable.
• Puedes rastrear un lote hasta su materia prima en minutos.
• Las desviaciones se cierran con causa raíz y no vuelven el mes siguiente.

Si alguna te hizo dudar, el problema no es la auditoría. Es el sistema de calidad.

Hacemos un diagnóstico de calidad sin costo antes de tu próxima inspección. Escríbenos por mensaje.

#BOUW #Calidad #BPM #ISO9001""",
     'Diagnóstico de calidad: www.bouwlatam.com',
     'Pregunta de BOUW: ¿Tu planta pasaría una auditoría mañana?, con tres puntos de control.'),

    ('Jueves 3 dic', 'D07-caso-whatsapp.png', """¿Tu negocio vende por WhatsApp?

Entonces conoces la conversación: "Hola, ¿cuánto cuesta?", y después veinte mensajes para saber qué quiere el cliente.

Para un taller de regalos en porcelana fría hicimos una web que resuelve eso:
• Catálogo con fotos reales de 15 modelos.
• Cotizador de cuatro pasos que calcula el precio mientras el cliente elige.
• El pedido llega a WhatsApp ya escrito, con la pieza, los detalles y el precio.

Además, no necesita servidor: mantenerla en línea cuesta $0 al mes.

Si vendes por WhatsApp y quieres algo así, escríbenos.

#BOUW #WhatsAppBusiness #ComercioElectrónico #Ecuador""",
     'Pruébala: charms-ecuador.vercel.app',
     'Caso real de BOUW: tres pantallas de celular de la web de Charms Ecuador con su catálogo y cotizador.'),

    ('Martes 8 dic', 'D08-tip-tres-archivos.png', """ventas_final.xlsx, ventas_final_v2.xlsx, ventas_REAL.xlsx.

Si en tu empresa existen archivos así, la información ya no cuadra. Y en cada reunión alguien llega con un número distinto.

Las señales más comunes:
• Los mismos datos se capturan en más de un lugar.
• Nadie sabe cuál es la versión correcta.
• Los reportes se arman copiando y pegando.

La solución no siempre es un sistema nuevo. Muchas veces basta con una sola fuente de datos bien conectada.

¿Te suena? Escríbenos y revisamos tu caso.

#BOUW #Datos #Excel #Pymes""",
     'www.bouwlatam.com',
     'Tip del día de BOUW: si tienes ventas_final_v2.xlsx, tienes un problema.'),

    ('Miércoles 9 dic', 'D09-como-trabajamos.png', """La pregunta que más nos hacen antes de empezar: ¿cuánto va a costar y cuándo termina?

Por eso lo dejamos por escrito desde el inicio:
• Diagnóstico: de 1 a 2 semanas. Medimos el proceso real antes de proponer nada.
• Precio cerrado: en 3 a 5 días, con alcance, entregables y plazo.
• Entrega semanal: de 4 a 10 semanas, viendo avances cada semana.
• Acompañamiento: 30 días después de entregar, sin contrato nuevo.

Si algo no se puede prometer, lo decimos antes de empezar.

¿Tienes un proyecto en mente? Escríbenos y agendamos el diagnóstico.

#BOUW #Consultoría #GestiónDeProyectos #Pymes""",
     'www.bouwlatam.com',
     'Cómo trabajamos en BOUW: diagnóstico, precio cerrado, entrega semanal y acompañamiento, con sus plazos.'),

    ('Jueves 10 dic', 'D10-cuentanos.png', """¿Qué proceso te está costando horas?

Cuéntanos en dos líneas:
• Qué se hace.
• Cada cuánto se repite.
• Quién lo hace.

Te respondemos en menos de 24 horas hábiles con lo que haríamos primero, cuánto tiempo tomaría y cómo lo mediríamos. Sin compromiso.

WhatsApp: +593 96 368 4012
Correo: bouw.contacto@gmail.com

#BOUW #Automatización #MejoraContinua #Quito #Monterrey""",
     'Escríbenos directo: wa.me/593963684012',
     'BOUW invita a contar qué proceso cuesta horas, con su WhatsApp +593 96 368 4012.'),
]

# La carpeta PUBLICAR la arma calendario.py, que mezcla esta serie con la serie A.
