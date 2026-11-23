# Antes y después del sitio BOUW

Capturado de https://bouw-eight.vercel.app/ en español (`locale es-ES`), capturas a `deviceScaleFactor 2`.
(`www.bouwlatam.com` está bloqueado por la red de este entorno; es el mismo sitio.)

No se descargaron fotos nuevas: todas las imágenes del inicio y de `/proyectos/mejora-continua` (incluida la sección `#oficina`)
ya estaban en `../imagenes/`. El sitemap solo tiene `/`, `/proyectos/mejora-continua` y `/privacidad`.
El juego no usa recortes aparte: recorta por CSS (`background-size: 340%`) las dos imágenes completas
`/servicios/lean-antes.webp` y `/servicios/lean-despues.webp` (= `../imagenes/juego-planta*.png` / `lean-antes|despues.png`).

## Carpetas

| Carpeta | Contenido |
|---|---|
| `pares/` | Fotograma más claro del estado "Hoy" y del estado "Con BOUW" de los videos de servicios (1440×810). |
| `juego/` | Juego "¿Dónde pierde horas esta planta?": recortes antes/después de cada desperdicio, capturas del juego y del panel. |
| `servicios/` | Interruptor "Hoy / Con Bouw" de los bloques Lean y Cumplimiento (inicio, sección `#proyectos`). |
| `hero/` | Deslizador "Plano / Realidad" del dragón en la portada. |
| `proyecto/` | `/proyectos/mejora-continua`: simulación Antes/Después, gráfico "Medido antes y después", sección `#oficina`. |
| `videos/` | Los 5 `.mp4` que usa el sitio en español. |
| `frames/<video>/` | Fotogramas (JPG): 1 por s en lean/cumplimiento, 1 cada 2 s en los de Excel, 2 por s en planta. |

## Pares ANTES / DESPUÉS

| Antes | Después | Qué muestra | Texto del sitio · ANTES | Texto del sitio · DESPUÉS |
|---|---|---|---|---|
| `pares/lean-antes.png` | `pares/lean-despues.png` | Video Lean (`lean-es.mp4`, s 4,6 y s 12,5): planta isométrica desordenada → planta en un solo flujo. | Etiqueta "HOY". Rótulos: "Cola frente a la estación", "Buscando herramientas", "Recorridos que se cruzan" | Etiqueta "CON BOUW". Rótulos: "Mapa de flujo de valor", "Preparación −15 %", "Reprocesos −20 %", "5S: cada cosa en su sitio", "Un solo flujo, sin cruces" |
| `pares/cumplimiento-antes.png` | `pares/cumplimiento-despues.png` | Video Cumplimiento (`cumplimiento-es.mp4`, s 4,6 y s 12,5): oficina/almacén con papeles y lote retenido → todo ordenado y lote liberado. | "HOY". Rótulos: "Desviaciones que vuelven", "Lote retenido", "Buscando un registro" | "CON BOUW". Rótulos: "Carpeta de inspección lista", "Cada registro en su sitio", "Lote liberado", "Trazabilidad en minutos" |
| `servicios/lean-hoy.png` | `servicios/lean-con-bouw.png` | Interruptor "Hoy / Con Bouw", ventana "mapa-de-flujo · línea de 4 estaciones". | "Planta · hoy". Tiempo de preparación 100, Reprocesos 100, Tiempo de entrega 29 min. Inventario E1 6,4 · E2 6,8 · E3 0,7 · Insp. 0,5. "Entrega 29 min \| Valor agregado 3,7 min (13 %)". Alt: "Planta en isométrico: recorridos cruzados, piezas apiladas y una estación que frena a las demás" | "Planta · con Bouw". Tiempo de preparación −15 %, Reprocesos −20 %, Tiempo de entrega −72 %. Inventario E1 0,3 · E2 1,1 · E3 0,4 · Insp. 0,3. "Entrega 8 min \| Valor agregado 3,7 min (45 %)". Alt: "La misma planta ordenada: un solo flujo, cada cosa en su sitio" |
| `servicios/cumplimiento-hoy.png` | `servicios/cumplimiento-con-bouw.png` | Interruptor "Hoy / Con Bouw", ventana "informe-de-auditoria · planta de ejemplo" (Informe de auditoría BPM). | "No lista". Preparación 33 %. 1 Crítico, 1 Mayor, 2 Menor. CAPA abiertas 9, CAPA cerradas 4, Lotes retenidos 3. Hallazgos: Trazabilidad Crítico, CAPA Mayor, Registros de lote Cumple, Expedientes digitales Menor, Integridad de datos Cumple, Liberación Menor. "MP-12 sin registro: el rastro se corta" | "Lista para inspección". Preparación 100 %. 0 Crítico, 0 Mayor, 0 Menor. CAPA abiertas 0, CAPA cerradas 13, Lotes retenidos 0. Todos los hallazgos "Cumple". "Rastreado completo en minutos" |
| `hero/hero-plano.png` | `hero/hero-realidad.png` | Portada: deslizador "Del plano a la realidad: arrastra para partir el dragón" al extremo derecho (94, todo plano) y al izquierdo (16, todo realidad). | "Plano" (letras BOUW en modo plano/contorno) | "Realidad" (BOUW en 3D con el dragón) |
| `proyecto/toggle-antes.png` | `proyecto/toggle-despues.png` | Mejora continua, `#linea`: simulación "Cómo se optimiza una línea — La línea, en marcha". | "Estado actual: la estación 2 trabaja al límite. Recibe las piezas nuevas y también las que vuelven de reproceso, así que su cola crece y la línea se llena de inventario esperando." Ritmo de salida 100 · Inventario 100 · Tiempo de una pieza 100 (índice, antes = 100) | "Con las dos mejoras la estación 2 queda con holgura y su cola se vacía: menos inventario y cada pieza pasa mucho menos tiempo en la línea. Quitar un poco de carga al cuello de botella cambia toda la línea. Los KPI por turno y los cuatro operadores capacitados hacen que el estándar se mantenga cuando ya no estamos." Ritmo de salida 111 (+11) · Inventario 31 (−69) · Tiempo de una pieza 28 (−72) |
| `proyecto/medido-antes-despues.png` (una sola imagen con ambos) | — | Mejora continua: "Resultados — Medido antes y después". | "Mismos indicadores, mismo criterio, en los dos turnos. Si no se midió igual antes y después, no se cuenta como mejora." Tiempo de preparación: ANTES 100 | DESPUÉS 85 (−15%). Reprocesos: ANTES 100 | DESPUÉS 80 (−20%). "Índice · antes = 100" |

## Juego "¿Dónde pierde horas esta planta?"

Texto del sitio: "Pruébalo · 30 segundos — ¿Dónde pierde horas esta planta? Hay seis desperdicios escondidos. Toca la planta donde veas uno y te decimos qué es, qué cuesta y cómo se ve arreglado."
Al terminar: "6/6 encontrados. Los encontraste todos. Así se ve la misma planta con un solo flujo." (`juego/estado-final.png`; `juego/estado-0-inicio.png` es el estado inicial).

`desperdicio-N-antes.png` / `-despues.png` son los recortes a resolución nativa (412×309) de las imágenes originales, con las mismas posiciones que usa el sitio para "HOY" y "CON BOUW". `estado-N.png` = juego completo tras tocar el punto; `panel-N.png` = solo el panel.

| N | Punto (left/top) | Desperdicio · etiqueta | Lo que cuesta (HOY) | Cómo se arregla (CON BOUW) |
|---|---|---|---|---|
| 1 | 32,8 % / 48 % | Espera · VSM | Un operador parado, esperando a que la estación de antes le pase piezas. | Balanceo de línea: cada estación al ritmo de la línea, con el mapa de flujo de valor. |
| 2 | 24,2 % / 58,9 % | Inventario en proceso · WIP | Piezas apiladas frente a la máquina más lenta. Ahí está el cuello de botella. | Nivelación de flujo: las piezas pasan una a una por la banda, sin montones. |
| 3 | 70,3 % / 44,3 % | Movimiento · 5S | Buscar herramientas y piezas entre el desorden, varias veces por turno. | 5S y trabajo estándar: cada cosa en su sitio. En el caso de mejora continua, la preparación bajó 15 %. |
| 4 | 58,6 % / 80,9 % | Transporte · Layout | Recorridos largos que se cruzan para llevar una caja de un lado a otro. | Rediseño de layout: lo que se usa junto va junto, y el flujo va en un solo sentido. |
| 5 | 50 % / 43,1 % | Sobreproducción · VSM | Cajas hechas antes de que alguien las pida, bloqueando el pasillo y el montacargas. | Producir al ritmo de lo que se vende, con el mapa de valor a la vista de todos. |
| 6 | 62,9 % / 25,1 % | Defectos · Causa raíz | Máquina en rojo: piezas que vuelven a pasar por reproceso. | Acciones correctivas con su causa raíz. En el caso, los reprocesos bajaron 20 %. |

## Otras capturas y videos (sin par)

| Archivo | Qué es / texto del sitio |
|---|---|
| `proyecto/seccion-oficina.png` | `#oficina`: "Del piso a la oficina — El mismo método, aplicado al cierre de mes". ✓ Las facturas electrónicas del SRI entran solas ✓ Cada kit se costea desde su despiece ✓ El stock avisa antes de que falte ✓ Tablero y estado de resultados automáticos. "El video usa datos de demostración. Los números del cliente se quedan con el cliente." |
| `videos/lean-es.mp4` | Video del servicio Lean, 14 s, 1440×810 (Hoy → Con BOUW). |
| `videos/cumplimiento-es.mp4` | Video del servicio de cumplimiento, 14 s, 1440×810 (Hoy → Con BOUW). |
| `videos/mejora-planta.mp4` | `/proyectos/mejora/planta.mp4`, 4,7 s, 720×1296, video vertical de la planta (mejora continua). |
| `videos/contable-excel-es.mp4` | `/proyectos/contable/excel-es.mp4`, 34 s, 1440×1080, "Programa_contable.xlsm · Excel · VBA" (sección `#oficina`). |
| `videos/contable-excel-pantalla.mp4` | `/proyectos/contable/excel-pantalla.mp4`, 34 s, 1200×780, tablero del programa contable (inicio). |

Fotos nuevas: ninguna; todas ya están en `../imagenes/` (ver `../imagenes/LISTA.md`). Textos alt de las fotos del proyecto según el sitio:
- `mejora-linea-extrusion`: "Línea de producción con tolvas azules y tableros de control en planta" (pie: "La línea, en operación")
- `mejora-termometro`: "Pirómetro Fluke apuntando al agua de la tina de enfriamiento" (pie: "Temperatura del agua de enfriamiento, tomada en la línea")
- `mejora-perfil-seccion`: "Perfil sostenido en la mano, con la sección visible en el extremo" (pie: "Revisión de la geometría del perfil")
- `mejora-perfil-estudio`: "Perfil negro sobre fondo azul marino con retícula técnica"
- `mejora-producto-paletizado`: pie "El producto que sale de la línea"
