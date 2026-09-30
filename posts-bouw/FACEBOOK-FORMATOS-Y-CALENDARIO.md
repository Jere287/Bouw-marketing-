# Facebook BOUW: formatos, sello y calendario día por día

> Todo sigue el [`MANUAL-DE-MARCA.md`](../MANUAL-DE-MARCA.md): navy, cian técnico, **un solo naranja por pieza (el botón)**, Archivo Expanded + IBM Plex.
> **El sello de BOUW es el dragón del sitio**, redibujado como silueta heráldica plana (un solo color, vector). Se ve igual de nítido en una foto de perfil de 176 px que en una lona.

---

## 1. El sello: sistema de logo "responsivo"

Como hacen las marcas grandes (Starbucks, Mastercard, Firefox), el logo tiene **versiones según el tamaño**: con texto cuando hay espacio y solo el símbolo cuando es pequeño. Así "QUITO · MONTERREY" nunca se pone ilegible.

| Archivo (`sello/`) | Qué es | Dónde se usa |
|---|---|---|
| `sello-bouw.png` / `.svg` (1200×1200, fondo transparente) | Sello completo: dragón + **BOUW** grande arriba + **QUITO · MONTERREY** abajo | Tamaños **de 300 px en adelante**: propuestas, portada de documentos, firma de correo grande, stickers, lona |
| `marca-dragon.png` / `.svg` | Solo el dragón dentro de un anillo, **sin texto** | Tamaños chicos: pie de las publicaciones (108 px), avatar, favicon |
| `fb-perfil-720.png` (720×720) | La marca sobre navy | **Foto de perfil** de Facebook, Instagram y WhatsApp Business |
| `emblema-dragon.svg` (cian) · `-blanco.svg` · `-navy.svg` | El dragón solo, detallado | Piezas "héroe" (F02, H01, portada), marca de agua (F11 en contorno) |
| `emblema-dragon-simple.svg` | Dragón con menos detalle | Cuando el dragón mide **menos de 120 px** |

**Reglas del sello:** va sobre navy `#04101F` (o en navy sobre fondo claro con `emblema-dragon-navy.svg`); no se deforma, no se le ponen sombras ni efectos 3D; una sola aparición grande por pieza (la marca chica del pie no cuenta). Debajo de 300 px **no** se usa el sello con texto: se usa `marca-dragon`.

---

## 2. Formatos para subir a Facebook (2026)

| Pieza | Tamaño que subes | Cómo se ve | Zona segura | Archivo listo |
|---|---|---|---|---|
| **Foto de perfil** | 720×720 (mínimo 196) | Círculo de 176 px en computadora y 196 px en celular | Lo importante dentro del círculo central | `sello/fb-perfil-720.png` |
| **Portada** | **1640×624** | 820×312 en computadora; en celular se recorta a los lados | Texto y dragón entre x = 280 y x = 1370 (el centro). Nada importante en la esquina inferior izquierda (la tapa la foto de perfil) | Express: *Portada* · `adobe/png/bouw-fb-portada-01.png` |
| **Publicación del feed** | **1080×1350 (4:5)** | Ocupa más pantalla en el celular que el cuadrado | 60 px de margen; el pie con el sello queda dentro | Express: *Semana 1–4* · `adobe/png/bouw-fb-semana*.png` |
| Publicación cuadrada | 1080×1080 | Para carruseles | — | Se genera desde `posts.html` si hace falta |
| **Historia** | **1080×1920 (9:16)** | Pantalla completa | Deja libres **250 px arriba y abajo** (ahí van el nombre de la página y la caja de respuesta) | Express: *Historias* · `adobe/png/bouw-fb-historias-*.png` |
| Enlace / horizontal | 1200×630 | Vista previa de un enlace | — | — |

**Al subir:**
1. Sube en **PNG** las piezas que tienen texto (Facebook comprime menos el texto nítido). Las fotos van en JPG.
2. Súbelas desde la computadora o desde Meta Business Suite, no reenviadas por WhatsApp: WhatsApp las comprime.
3. En Adobe Express: **Descargar → PNG → elige la página**. No cambies el tamaño al descargar.
4. Pon el texto de la publicación en el cuadro de texto, no dentro de la imagen (la imagen ya tiene el titular).

---

## 3. Diseños en Adobe Express (editables)

Cada documento se abre en Adobe Express con los textos editables, las tipografías de la marca (Adobe Fonts), la retícula, el logo y el dragón como **vectores editables** (puedes cambiarles color o tamaño sin perder calidad).

| Documento | Páginas | Enlace |
|---|---|---|
| Portada Facebook 1640×624 | 1 | [Abrir en Express](https://new.express.adobe.com/id/urn:aaid:sc:US:a10ed361-20f4-4b84-a611-26823ca1e720) |
| Semana 1 (5–8 oct) | F01 · F02 · F03 | [Abrir en Express](https://new.express.adobe.com/id/urn:aaid:sc:US:1a28cf60-e38d-41e1-9907-a49f4497a168) |
| Semana 2 (12–16 oct) | F04 · F05 · F06 | [Abrir en Express](https://new.express.adobe.com/id/urn:aaid:sc:US:b72cfcc0-0dda-4d78-bf43-aa817c380793) |
| Semana 3 (19–23 oct) | F07 · F08 · F09 | [Abrir en Express](https://new.express.adobe.com/id/urn:aaid:sc:US:e172aff3-605e-4a8f-b8c1-61b2193abdd5) |
| Semana 4 (26–28 oct) | F11 · F10 | [Abrir en Express](https://new.express.adobe.com/id/urn:aaid:sc:US:e819cbf4-7a97-4829-bee9-540f432a81c5) |
| Historias 1080×1920 | H01 · H02 · H03 | [Abrir en Express](https://new.express.adobe.com/id/urn:aaid:sc:US:98209196-2e07-43eb-8065-aef8992924dc) |

> **F03 (Dos ingenieros):** antes de publicarla, reemplaza los recuadros "[ Foto socio 1/2 ]" por fotos reales (en Express: arrastra la foto sobre el recuadro) y pon los nombres.
> En la cuenta de Adobe quedaron las versiones anteriores (con el dragón 3D, sin "(v2)" en el nombre) y cuatro documentos de prueba ("prueba imagen", "prueba css", "prueba svg" y una primera "Portada"). Se pueden borrar: los buenos son los que dicen **(v2)**.

---

## 4. Calendario día por día (octubre 2026)

**Horarios:** 07:30 (el dueño revisa el celular antes de entrar), 12:30 (almuerzo) y 19:30. Después de dos semanas revisa en Meta Business Suite → *Estadísticas* a qué hora responde tu público y ajusta.
**Ritmo:** 3 publicaciones por semana + 2 historias. Todos los días: responder comentarios y mensajes en menos de 1 hora (en Facebook eso pesa más que publicar mucho).

### Antes de empezar: sábado 3 y domingo 4 de octubre
- [ ] Foto de perfil: `sello/fb-perfil-720.png`
- [ ] Portada: descargar de Express (1640×624)
- [ ] Botón de la página: **Enviar mensaje de WhatsApp** → +593 96 368 4012
- [ ] Categoría: *Consultor empresarial*. Ciudad: Quito. Sitio: bouw-eight.vercel.app
- [ ] Descripción (máx. 255): *Orden, tiempo y control para pymes de Quito. Procesos, automatización y seguridad de la información. Radiografía gratis: 1 hora en tu empresa. Del diseño a la realidad.*
- [ ] Invitar a contactos de ambos socios (solo dueños y gerentes; calidad antes que cantidad)

### Semana 1: presentarse
| Día | Hora | Qué | Pieza | Texto |
|---|---|---|---|---|
| **Lun 5** | 07:30 | Publicación · **fijarla arriba** | F01 ¿Qué te quita más el sueño? | ver §5 · F01 |
| Lun 5 | 12:30 | Historia | H02 ¿1, 2 o 3? | "Respóndenos con el número" |
| **Mié 7** | 12:30 | Publicación | F02 Del diseño a la realidad (dragón) | §5 · F02 |
| Mié 7 | 19:30 | Historia | H01 ¿Excel y WhatsApp? | — |
| **Jue 8** | 19:30 | Publicación | F03 Dos ingenieros (con fotos) | §5 · F03 |
| Vie 9 | — | **Feriado (Independencia de Guayaquil)**: no publicar | — | Solo responder mensajes |

### Semana 2: mostrar que entendemos el problema
| Día | Hora | Qué | Pieza | Texto |
|---|---|---|---|---|
| **Lun 12** | 07:30 | Publicación | F04 Marca lo que reconozcas | §5 · F04 |
| Mar 13 | 12:30 | Historia | H02 ¿1, 2 o 3? (repetir) | — |
| **Mié 14** | 12:30 | Publicación | F05 Caso real: programa contable | §5 · F05 |
| Jue 15 | 19:30 | Historia | H03 Caso real | — |
| **Vie 16** | 12:30 | Publicación | F06 La cuenta | §5 · F06 |

### Semana 3: cómo trabajamos y control
| Día | Hora | Qué | Pieza | Texto |
|---|---|---|---|---|
| **Lun 19** | 07:30 | Publicación | F07 Plazos que se pueden escribir | §5 · F07 |
| Mar 20 | 12:30 | Historia | H01 ¿Excel y WhatsApp? | — |
| **Mié 21** | 12:30 | Publicación | F08 Respaldo | §5 · F08 |
| Jue 22 | 19:30 | Historia | H03 Caso real | — |
| **Vie 23** | 12:30 | Publicación | F09 Se va la luz 8 horas | §5 · F09 |

### Semana 4: pedir la Radiografía
| Día | Hora | Qué | Pieza | Texto |
|---|---|---|---|---|
| **Lun 26** | 07:30 | Publicación | F11 Radiografía (dragón en contorno) | §5 · F11 |
| Lun 26 | — | **Promoción pagada** (opcional) de F11: USD 3/día × 7 días. Público: Quito + 25 km, 28–60 años, intereses *pequeñas empresas, emprendimiento, administración de empresas*. Botón: *Enviar mensaje de WhatsApp* | F11 | — |
| Mar 27 | 12:30 | Historia | H02 ¿1, 2 o 3? | — |
| **Mié 28** | 12:30 | Publicación | F10 Antes de comprar un ERP | §5 · F10 |
| Vie 30 | 12:30 | Compartir de nuevo F05 (caso real) con un texto nuevo: "Lo más preguntado del mes." | F05 | — |
| Sáb 31 | — | **Revisión del mes** (ver §6) | — | — |

> Lun 2 y mar 3 de noviembre son feriados (Difuntos e Independencia de Cuenca): no publicar. Noviembre arranca el miércoles 4 con el mismo ritmo, rotando las piezas que mejor funcionaron y la serie de LinkedIn (`png/li-*`).

---

## 5. Textos para pegar (voz BOUW: frase del cliente → qué haríamos → número → una acción)

**Firma de todas las publicaciones:**
`BOUW · Del diseño a la realidad · Quito · Monterrey · WhatsApp +593 96 368 4012`

**F01 · ¿Qué te quita más el sueño?** (fijada)
> ¿Qué te quita más el sueño?
> 1 · Orden: "Todo pasa por mí." Te dejamos una empresa que funciona aunque no estés encima.
> 2 · Tiempo: "No nos alcanza el día." Tu equipo recupera horas cada semana.
> 3 · Control: "Me entero a fin de mes." Tus números cada lunes y tu información protegida.
> Responde con 1, 2 o 3 y te decimos qué haríamos primero.

**F02 · Del diseño a la realidad**
> Somos BOUW, un equipo de ingeniería con más de 7 años de experiencia combinada entre Quito y Monterrey.
> Trabajamos en tres cosas: orden, para que tu empresa funcione aunque no estés encima; tiempo, para que tu equipo haga más sin contratar más; y control, para que veas tus números a tiempo y tu información esté segura.
> Antes de proponerte nada, hacemos la cuenta. Si el número no da, te lo decimos.
> Pide tu Radiografía: 1 hora en tu empresa, gratis.

**F03 · Dos ingenieros**
> [Nombre], ingeniero industrial: procesos y calidad.
> [Nombre], informática y ciberseguridad: sistemas y seguridad.
> Entramos a tu empresa, hacemos la cuenta y dejamos las cosas funcionando. Escríbenos y conversemos.

**F04 · Marca lo que reconozcas**
> Esta no es la lista de lo que vendemos. Es la lista de frases con las que nos escriben. ¿Cuántas marcas?
> ¿Dos o más? Escríbenos. ¿Ninguna? Todavía no nos necesitas, y preferimos decírtelo aquí.

**F05 · Caso real**
> Un taller de manufactura cerraba el mes armando todo a mano.
> Construimos un ERP pequeño sobre el Excel que el equipo ya sabía usar: 11 hojas conectadas, 1 archivo, cero licencias, cero migraciones.
> Ahora el cierre mensual sale solo de los movimientos ya capturados. ¿Tu cierre todavía se arma a mano?

**F06 · La cuenta**
> Cuánto cuesta hacerlo a mano (ejemplo): 5 veces por semana × 30 minutos × 2 personas × 48 semanas = 240 horas al año.
> Con más de 150 horas al año, vale automatizar. Con menos de 40, no lo automatices: te lo decimos.
> Haz la cuenta con tu tarea y mándanosla.

**F07 · Plazos que se pueden escribir**
> 01 · Radiografía: 1 hora en tu empresa, gratis.
> 02 · Alcance y precio cerrados en 3 a 5 días.
> 03 · Construcción: de 4 a 10 semanas.
> 04 · Entrega funcionando, con la documentación para mantenerlo sin nosotros.

**F08 · Respaldo**
> Un respaldo que nunca se restauró no es un respaldo.
> Tres controles que revisamos en cada Radiografía: respaldo probado, doble factor en correo y sistemas, y accesos por rol. Son los más baratos de cerrar.

**F09 · Se va la luz 8 horas**
> ¿Qué pasa en tu operación si se va la luz 8 horas?
> 0 min: ¿quién decide? 30 min: ¿qué va al generador? 2 h: ¿cómo sigues vendiendo, despachando y facturando?
> Si no está escrito, no es un plan. Lo armamos contigo.

**F10 · Antes de comprar un ERP**
> Antes de invertir en un ERP: ¿tengo el proceso dibujado? ¿Qué problema exacto resuelve? ¿Quién lo usará todos los días? ¿Cómo migro los datos? ¿Quién cuida accesos y respaldos?
> A veces la respuesta es el Excel que ya tienes, bien armado.

**F11 · Radiografía**
> Una hora en tu empresa, gratis:
> · Revisamos un proceso clave (ventas, inventario, despacho o cierre de mes).
> · Hacemos la cuenta de horas con tus números.
> · Revisamos cinco puntos de seguridad.
> Al día siguiente te enviamos qué haríamos primero. Escríbenos: RADIOGRAFÍA.

**Respuesta tipo por WhatsApp** (cuando alguien escribe "1", "2", "3" o "RADIOGRAFÍA"):
> ¡Hola! Gracias por escribir. Para prepararnos: ¿a qué se dedica tu empresa, cuántas personas son y qué es lo que más te frena hoy? Con eso te proponemos día y hora para la Radiografía (1 hora, sin costo).

---

## 6. Qué medir cada semana (Meta Business Suite → Estadísticas)

| Métrica | Por qué importa | Meta del primer mes |
|---|---|---|
| **Conversaciones iniciadas** (WhatsApp y Messenger) | Es lo único que se convierte en Radiografías | 10 |
| **Radiografías agendadas** | Tu embudo real | 3 |
| Comentarios con "1", "2" o "3" en F01 | Te dice qué necesidad vende más | Anótalos |
| Alcance por publicación | Qué temas mueve el algoritmo | Comparar entre piezas |
| Guardados y compartidos | Señal de contenido útil (F06 y F10 deberían ganar) | — |

**Revisión del sábado 31:** las 2 piezas con más conversaciones se repiten en noviembre con otro titular. La que tenga menos alcance y cero mensajes se reemplaza.
