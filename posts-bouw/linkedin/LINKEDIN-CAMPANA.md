# LinkedIn BOUW: perfil, portadas y campaña "Del diseño a la realidad"

> Todo sale de **bouw-eight.vercel.app**:
> - **El logo:** el mismo PNG del encabezado y del pie de página, `marca/bouw-logo-negativo.png` (BOUW en cian con el dragón blanco). El dragón solo, `marca/bouw-dragon-blanco.png`, es el ícono del sitio.
> - **Los colores y las letras:** los del sitio: Archivo, IBM Plex Sans, IBM Plex Mono e Instrument Serif.
> - **El contenido:** el lema *Si se repite, se automatiza.*, los servicios, los proyectos, "¿Cuál te suena?", la calculadora, las condiciones y el contacto.
>
> El texto completo del sitio está en [`../sitio/TEXTOS-DEL-SITIO.md`](../sitio/TEXTOS-DEL-SITIO.md) y sus imágenes en `../sitio/imagenes/`.

Todo está listo para subir en `png/`, y el carrusel en `BOUW-carrusel-proyectos.pdf`. Para cambiar un texto, edita `gen_li.py` y ejecuta:
`python3 gen_li.py && node shot.js && node pdf.js`

---

## 1. Primero: perfil y portadas (antes del martes 17)

| Pieza | Tamaño | Dónde se sube | Archivo (`png/`) |
|---|---|---|---|
| Logo de la página de empresa | 400×400 | Página de empresa → Editar → Logo | `01-perfil-dragon-400x400.png` (el dragón, como el ícono del sitio) |
| Logo con nombre (alternativa) | 400×400 | Si prefieres que se lea "BOUW" en el logo | `02-perfil-logo-completo-400x400.png` |
| Portada de la página de empresa | **1128×191** | Página de empresa → Editar → Imagen de portada | `03-portada-empresa-1128x191.png` |
| Banner del perfil personal (cada socio) | **1584×396** | Tu perfil → lápiz sobre la portada | `04-banner-perfil-personal-1584x396.png` |
| Foto de perfil grande (WhatsApp, Facebook) | 720×720 | WhatsApp Business, Facebook, firmas | `05-perfil-logo-720x720.png` |

**Zonas seguras:**
- **Portada de empresa:** el logo de la página tapa la esquina inferior izquierda, así que el texto empieza en x = 300 y el logo BOUW va a la derecha.
- **Banner personal:** tu foto tapa la parte izquierda, así que el contenido empieza en x = 560. En el celular se recortan los lados.

**Datos de la página de empresa (copiar tal cual, son los del sitio):**
- Nombre: **BOUW**
- Eslogan: *Si se repite, se automatiza. Ingeniería de procesos, calidad y automatización para empresas que fabrican.*
- Sector: Servicios y consultoría empresarial · Tamaño: 2–10 empleados · Sedes: Quito (principal) y Monterrey
- Sitio web: bouw-eight.vercel.app · Botón personalizado **"Contactar"** → WhatsApp +593 96 368 4012
- "Acerca de":
  > Del diseño a la realidad. Automatizamos procesos y convertimos ideas de ingeniería en productos que funcionan. Llevamos más de 7 años haciéndolo entre Ecuador y México.
  > Lean manufacturing e ingeniería de planta · Cumplimiento normativo y BPM · Automatización · Simulación de flujos · Web y producto.
  > Diagnóstico primero (1 a 2 semanas), precio cerrado por escrito (3 a 5 días), entrega cada semana (4 a 10 semanas) y 30 días de acompañamiento.
  > Quito, Ecuador (desde 2019) · Monterrey, México (desde 2023). Nueve horas al día en común: siempre hay alguien para responderte.
  > bouw.contacto@gmail.com · +593 96 368 4012

**Titular del perfil personal (cada socio):** *Socio en BOUW · Automation & Digital Solutions · Si se repite, se automatiza · Quito*

---

## 2. Las piezas

| Archivo | Tamaño | Qué es |
|---|---|---|
| `L01-presentacion.png` | 1080×1350 | Del diseño a la realidad · lema · sedes · 7+ años |
| `L02-lean-ingenieria-de-planta.png` | 1080×1350 | Servicio Lean: −15 % preparación, −20 % reprocesos; hoy / con BOUW |
| `L03-cumplimiento-normativo-bpm.png` | 1080×1350 | Servicio BPM: lo que hacemos; hoy / con BOUW |
| `L04-programa-contable-excel.png` | 1080×1350 | Proyecto: ERP sobre Excel (11 hojas, 1 archivo, 0 migraciones) |
| `L05-simulacion-de-flujos.png` | 1080×1350 | Proyecto: mapa de flujo de valor (29 min de entrega, 3,7 min de valor agregado) |
| `L06-cual-te-suena.png` | 1080×1350 | Las 9 frases de "¿Cuál te suena?" |
| `L07-en-que-condiciones.png` | 1080×1350 | Diagnóstico → precio cerrado → entrega semanal → acompañamiento |
| `L08-la-cuenta.png` | 1080×1350 | La calculadora: 3 × 20 min × 1 × 48 = 48 h, "Está en la frontera" |
| `L09-donde-pierde-horas.png` | 1080×1350 | El juego del sitio, con la planta original |
| `L10-contacto.png` | 1080×1350 | WhatsApp, correo, sedes, respuesta en menos de 24 h hábiles |
| `C01`–`C07` + `BOUW-carrusel-proyectos.pdf` | 1080×1350 | Carrusel "Lo que hemos construido": Anatris, Simulación, Programa contable, Charms Ecuador, Informe de auditoría |
| `A01-anuncio-la-cuenta-1200x627.png` | 1200×627 | Anuncio o enlace hacia la calculadora |

**Formatos de LinkedIn:**
- Las publicaciones son verticales, de **1080×1350**: es la que más pantalla ocupa en el celular.
- El carrusel se sube como **documento PDF** (Publicar → Añadir documento), y LinkedIn lo muestra como láminas que se deslizan.
- **1200×627** es para enlaces y anuncios.

---

## 3. Calendario (martes a jueves, 08:00)

| Fecha | Pieza | Objetivo |
|---|---|---|
| **Mar 17 nov** | L01 Presentación | Quiénes somos (fijarla en la página) |
| Mié 18 nov | L02 Lean & planta | Servicio |
| Jue 19 nov | L06 ¿Cuál te suena? | Conversación en comentarios |
| **Mar 24 nov** | L03 Cumplimiento & BPM | Servicio |
| Mié 25 nov | **Carrusel "Lo que hemos construido" (PDF)** | Alcance: los carruseles se guardan y comparten más |
| Jue 26 nov | L07 En qué condiciones | Confianza: plazos y precio por escrito |
| **Mar 1 dic** | L04 Programa contable | Prueba: proyecto real |
| Mié 2 dic | L08 La cuenta | Llevar gente a la calculadora |
| Jue 3 dic | L09 ¿Dónde pierde horas esta planta? | Llevar gente al juego del sitio |
| **Mar 8 dic** | L05 Simulación de flujos | Prueba: proyecto real |
| Mié 9 dic | L10 Contacto | Cierre: llamada a la acción |
| 8–22 dic | A01 Anuncio (opcional, pagado) | USD 5–10 al día, Quito y Monterrey; cargos: gerente, dueño, jefe de planta, operaciones o calidad |

**Cada semana, además:** cada socio comparte la publicación desde su perfil con una línea propia. El perfil personal llega a 5–10 veces más gente que la página. Responde todos los comentarios durante la primera hora.

---

## 4. Textos para pegar (salen del sitio)

**L01 · Presentación**
> Del diseño a la realidad.
> Automatizamos procesos y convertimos ideas de ingeniería en productos que funcionan. Llevamos más de 7 años haciéndolo entre Ecuador y México.
> Quito desde 2019 · Monterrey desde 2023. Nueve horas al día en común: siempre hay alguien para responderte.
> Si se repite, se automatiza.
> bouw-eight.vercel.app
> #Quito #Monterrey #Manufactura #Automatización

**L02 · Lean manufacturing & ingeniería de planta**
> Elimina cuellos de botella y maximiza cada metro cuadrado de tu planta.
> Hoy: recorridos que se cruzan, piezas apiladas en los pasillos y una máquina que frena a todas.
> Con BOUW: un solo flujo, cada cosa en su sitio y el mapa de valor con su tablero vigilando la línea.
> En el caso de mejora continua: −15 % en tiempo de preparación, −20 % en reprocesos y 4 operadores capacitados.
> Agenda una evaluación técnica de tus procesos: bouw-eight.vercel.app
> #Lean #SMED #VSM #5S

**L03 · Cumplimiento normativo & BPM**
> Pasa cualquier auditoría a la primera.
> Si llega un inspector sin aviso, la carpeta ya está armada: expedientes estandarizados, cada registro en su sitio y con su responsable, y la trazabilidad en pantalla.
> BPM · ISO · CAPA · Trazabilidad · Batch records · 8D · Causa raíz · Auditorías internas.
> Agenda un diagnóstico de calidad gratis antes de tu próxima inspección.
> #BPM #ISO #Calidad

**Carrusel · Lo que hemos construido**
> Lo que tienen en común: procesos que antes costaban horas.
> Anatris, una simulación de flujos, un ERP sobre Excel, la web de Charms Ecuador y un informe de auditoría. Cinco proyectos en 7 láminas.

**L04 · Programa contable**
> Un ERP pequeño montado sobre Excel: inventario, kits, ventas y caja en un solo archivo.
> Once hojas conectadas por macros. El equipo siguió trabajando en la herramienta que ya sabía usar, sin migrar a otro sistema ni pagar licencias nuevas.
> Resultado: el cierre mensual dejó de ser un armado manual.

**L05 · Simulación de flujos**
> Con los datos de tu operación armamos un modelo de la línea y probamos ahí cada cambio de layout o de proceso.
> Sabes cuánto mejora el flujo antes de mover un solo equipo, sin parar la producción para hacer pruebas.
> Pruébala en bouw-eight.vercel.app

**L06 · ¿Cuál te suena?**
> Son frases que nos dicen los clientes cuando nos llaman. ¿Cuál dices tú? Te leemos en los comentarios.
> Si ninguna se parece a tu semana, puede que todavía no nos necesites, y preferimos decírtelo.

**L07 · En qué condiciones**
> Diagnóstico primero (1 a 2 semanas): medimos tu proceso real antes de proponer nada.
> Precio cerrado (3 a 5 días): alcance, entregables, plazo y precio por escrito.
> Entrega cada semana (4 a 10 semanas). Acompañamiento de 30 días, sin contrato nuevo.
> Si algo no se puede prometer, lo decimos desde el principio.

**L08 · La cuenta**
> 3 veces por semana × 20 minutos × 1 persona × 48 semanas = 48 horas al año.
> Veredicto: está en la frontera. Sale a cuenta si además te está costando errores. Si solo son las horas, espera.
> Haz la cuenta con tu tarea en la calculadora: bouw-eight.vercel.app

**L09 · ¿Dónde pierde horas esta planta?**
> Hay seis desperdicios escondidos. ¿Cuántos ves?
> Pruébalo en 30 segundos en bouw-eight.vercel.app: toca la planta y te decimos qué es, qué cuesta y cómo se ve arreglado.

**L10 · Contacto**
> Cuéntanos qué proceso te está costando horas y te respondemos con un plan concreto.
> WhatsApp +593 96 368 4012 · bouw.contacto@gmail.com
> Respondemos en menos de 24 horas hábiles.

**A01 · Anuncio** (enlace a bouw-eight.vercel.app)
> Titular: Cuánto cuesta hacerlo a mano · Texto: Rellena la fila con una tarea que hoy se haga a mano. Si no compensa automatizarla, también te lo dice.

---

## 5. Cómo medir (cada viernes, 10 minutos)

| Indicador | Meta de las 4 semanas |
|---|---|
| Seguidores de la página | +150 |
| Interacción por publicación (reacciones + comentarios ÷ impresiones) | ≥ 3 % |
| Mensajes o WhatsApp que llegan por LinkedIn | ≥ 8 |
| Diagnósticos agendados | ≥ 3 |

Lo que más funcione (normalmente el carrusel y "La cuenta") se repite en enero con otro proyecto.
