# Bouw: consultora de 3 áreas (Ing. Industrial × Ciberseguridad × IA)

> 🎯 **Foco actual:** [`NICHO-BOUW.md`](NICHO-BOUW.md): preparar a proveedores pymes de bancos y cooperativas para pasar sus evaluaciones. Este documento queda como referencia.

> Equipo: **tú** (Ingeniería Industrial) + **tu socio** (Ingeniería en Ciberseguridad) + **Claude** (IA para investigar, analizar, documentar y automatizar).
> Objetivo: una consultora que pueda abarcar varias soluciones, **centrada en 3 áreas con poca competencia**.
> ➡️ **Versión aterrizada para vender (qué área abrir primero, ofertas con precio y guiones):** [`VENTA-ATERRIZADA.md`](VENTA-ATERRIZADA.md) · Cuestionarios: [`chequeo-360/`](chequeo-360/)
> Fecha: sept. 2026. Reemplaza el foco de [`PLAN-BOUW.md`](PLAN-BOUW.md). Lo anterior (WhatsApp, clínicas) no se pierde: pasa a ser un producto de entrada (sección 6).

---

## 0. Resumen

**Posicionamiento:** *Bouw, operaciones seguras.* **"Construimos empresas que siguen funcionando aunque falle la luz, el sistema o el proveedor."** (*bouw* = construir)

La ventaja no está en ninguna disciplina sola (las tres tienen competencia). Está en **el cruce**:

```
   Ing. Industrial              Ciberseguridad
  (procesos, costos,          (riesgo digital, normas,
   calidad, continuidad)       protección de datos)
            \                        /
             \   ÁREA 2             /
              \  Continuidad       /
    ÁREA 3     \  y resiliencia   /     ÁREA 1
    IA segura   \                /      Cumplimiento
    y productiva \______________/       de ciberseguridad
                   \    IA    /         (sectores esenciales)
                    \(Claude)/
```

| # | Área | Cruce | Por qué hay poca competencia |
|---|---|---|---|
| **1** | **Cumplimiento de ciberseguridad y datos** para organizaciones medianas de sectores esenciales (cooperativas, salud, educación) | Ciberseguridad + sistemas de gestión (Ind.) | Ley de Ciberseguridad vigente desde el 22/5/2026 y con reglamentos en camino. Las firmas grandes atienden a bancos y cooperativas del segmento 1; **las medianas y pequeñas quedan solas** |
| **2** | **Continuidad del negocio y resiliencia**: apagones + ransomware + fallas de proveedores | Ind. (procesos críticos, contingencia) + Ciber (respaldo, recuperación) | Los instaladores solares venden equipos y los técnicos de TI venden respaldos, pero **nadie hace el plan integral** para pymes. Estiaje de sept. 2026 a mar. 2027 |
| **3** | **IA segura y productiva** para pymes medianas | Ind. (mejora de procesos, retorno) + Ciber (uso seguro, datos) + Claude | Las agencias venden chatbots (saturado). **Nadie combina procesos + retorno medible + seguridad de datos** |

**Cómo crecen juntas:** un solo diagnóstico de entrada ("Chequeo Bouw 360") detecta necesidades en las tres áreas, y cada cliente puede comprar más de una.

---

## 1. Por qué este equipo puede hacerlo (y dónde está el límite)

| Quién | Aporta | Ejemplos de entregables |
|---|---|---|
| **Tú (Ing. Industrial)** | Procesos, mapeo de flujos, costos, indicadores, mejora continua (lean), gestión de calidad (ISO 9001), análisis de impacto en el negocio, gestión de proyectos | Mapa de procesos críticos, análisis de impacto, planes de contingencia operativa, tablero de indicadores, cálculo de retorno de la IA |
| **Tu socio (Ciberseguridad)** | Riesgo digital, controles, ISO 27001, respuesta a incidentes, pruebas de vulnerabilidad, respaldos | Brechas frente a la ley o a la SEPS, políticas técnicas, procedimiento de incidentes en 72 h, pruebas de phishing, plan de respaldo 3-2-1 |
| **Claude** | Investigación normativa, primeros borradores, análisis de datos, plantillas, automatizaciones, materiales de capacitación | Un manual o política en horas y no en días, matrices de riesgo, resúmenes de normas, prototipos de automatización, informes para clientes |

**Ventaja económica:** con Claude, un equipo de 2 entrega documentación y análisis a **velocidad de firma mediana** y con **precio de pyme**. Ese es el margen que la competencia tradicional no tiene.

**Límites (no negociables):**
- Claude **no reemplaza** la firma de un profesional, una certificación ni la revisión legal. Todo entregable lo revisa y firma uno de ustedes, o el abogado aliado cuando es jurídico.
- **Confidencialidad:** no subas datos personales ni información sensible de clientes a ninguna IA sin su autorización. Usa datos anonimizados o de muestra, cuentas con privacidad empresarial y un **acuerdo de confidencialidad** firmado con cada cliente. Una consultora de ciberseguridad que filtra datos no tiene segunda oportunidad.

---

## 2. Panorama: qué descartamos y por qué

| Servicio posible | Saturación en Ecuador | Veredicto |
|---|---|---|
| Chatbots / CRM de WhatsApp | 🔴 Alta (Blue Nova, agencias IA, SaaS de $15–$50) | Solo como producto de entrada dentro del Área 3 |
| Marketing digital / redes | 🔴 Alta | Descartado |
| Seguridad y Salud en el Trabajo (SST) | 🔴 Alta (muchos técnicos acreditados) | Descartado |
| Implementación de ERP (Odoo y otros) | 🟠 Media-alta (partners establecidos) | Descartado |
| Consultoría ISO 9001 aislada | 🟠 Media-alta | Solo como parte de las Áreas 1 y 2 |
| Pentesting a bancos grandes | 🟠 Media (firmas grandes y regionales) | No es tu segmento |
| Lean / productividad aislada | 🟡 Media | Se integra en el Área 3 (IA + procesos) |
| UAFE, EUDR, autogeneración | Ver [`OPORTUNIDADES-NICHOS.md`](OPORTUNIDADES-NICHOS.md) | No encajan como foco |
| **Ciberseguridad para medianas de sectores esenciales** | 🟢 **Baja** | ✅ **Área 1** |
| **Continuidad del negocio para pymes** | 🟢 **Baja** | ✅ **Área 2** |
| **IA con procesos + seguridad** | 🟢 **Baja (por ahora)** | ✅ **Área 3** |

---

## 3. Área 1: Cumplimiento de ciberseguridad y datos

### Cliente objetivo
| Segmento | Cuántos | Por qué ahora |
|---|---|---|
| **Cooperativas de ahorro y crédito, segmentos 3, 4 y 5** | ~394 cooperativas activas en total; **136 en el segmento 4** y **50 en el 5** (feb. 2026) | El sistema financiero ya era regulado, así que **la Ley de Ciberseguridad les aplica de inmediato**. La SEPS ya exige controles (seguridad de la información, Res. 2022-002; ciberseguridad en canales digitales, Res. 009 de feb. 2024; riesgo operativo). Tienen menos presupuesto que el segmento 1 |
| **Clínicas y centros médicos medianos** | Cientos en Quito | Salud está en el catálogo mínimo de servicios esenciales; manejan datos sensibles (LOPDP); el ransomware golpea más a salud (ESET, T1 2026) |
| **Colegios y universidades privadas** | Decenas en Quito | Educación está en el catálogo de servicios esenciales, y manejan datos de menores |
| **Empresas de software y servicios digitales locales** | Decenas | Reglamento de Prestadores de Servicios Digitales a 12 meses (mayo 2027) |

### Evidencia
- Ley Orgánica para el Fortalecimiento de la Ciberseguridad: vigente desde el **22/5/2026**; notificación de incidentes en **72 h**; multas del **0,1% al 1,5%** del volumen de negocio. Reglamentos a 6 meses (**nov. 2026**) y 12 meses (**mayo 2027**). **24 meses** de adecuación para sectores sin regulación previa.
- Ecuador aparece entre los países de América Latina con más intentos de ransomware (Kaspersky, ESET).

### Oferta
| Producto | Precio sugerido | Quién lo hace |
|---|---|---|
| **Diagnóstico de brechas** (ley + SEPS o LOPDP): semáforo por control | $800–$1.500 | Socio (técnico) + tú (proceso y gestión) + Claude (matriz, informe) |
| **Puesta en cumplimiento**: políticas, procedimiento de incidentes (72 h), inventario de activos, matriz de riesgos, capacitación | $3.000–$8.000 | Ambos |
| **Responsable de seguridad externo** (virtual CISO) mensual | $400–$900/mes | Socio |
| Pruebas de phishing y capacitación trimestral | $250–$600 por campaña | Socio + Claude (materiales) |

### Competencia
Firmas grandes (Big Four, Andersen, estudios jurídicos) y fabricantes de software (GlobalSuite y otros) apuntan a bancos y cooperativas del segmento 1. **Las cooperativas de los segmentos 3–5 y las clínicas medianas no tienen un proveedor especializado y asequible.** Es una hipótesis: valídala en la sección 9.

---

## 4. Área 2: Continuidad del negocio y resiliencia

### El dolor
- **Apagones:** el estiaje va de **sept. 2026 a mar. 2027**, con **noviembre como el mes más crítico** (déficit de hasta 450 MW). CENACE estima un **18% de probabilidad de apagones** sin importaciones de Colombia y un impacto esperado de $41 M por energía no suministrada. Los apagones de 2024 siguen frescos.
- **Ciberataques:** manufactura, tecnología y salud fueron los sectores más atacados por ransomware en el T1 2026 (ESET). Los atacantes usan a **pymes proveedoras** para entrar a empresas grandes.
- **Proveedores:** la cadena de suministro es el punto débil (ver Área 1).

### Cliente objetivo
Manufactura y distribución medianas (Quito y valles), clínicas, cooperativas (la norma de riesgo operativo de la SEPS pide continuidad), cadenas de retail regionales y **proveedores de empresas grandes**: el 65% de las grandes empresas ve las vulnerabilidades de sus proveedores como el principal obstáculo de resiliencia (Kaspersky).

### Oferta: "Plan Bouw de Continuidad"
| Paso | Quién |
|---|---|
| 1. **Análisis de impacto en el negocio**: qué procesos no pueden parar, cuánto cuesta cada hora caída | Tú (Ind.) + Claude (cálculos, plantillas) |
| 2. **Escenarios**: apagón de 4, 8 y 24 h; ransomware; caída de un proveedor crítico; ausencia de personal clave | Ambos |
| 3. **Plan operativo**: turnos, inventario de seguridad, procesos manuales de respaldo, energía de respaldo priorizada (dimensionar, no vender equipos) | Tú |
| 4. **Plan digital**: respaldos 3-2-1, recuperación, contactos de incidente, prioridades de restauración | Socio |
| 5. **Simulacro** y mejora | Ambos |

| Producto | Precio sugerido |
|---|---|
| Chequeo de continuidad (medio día) | $300–$500 |
| Plan completo | $1.500–$4.000 |
| Simulacro anual + actualización | $500–$1.200/año |
| Sello "Proveedor Confiable Bouw" (continuidad + seguridad básica para cuestionarios de clientes grandes) | $1.200–$3.000 |

### Competencia
Hay consultores de ISO 22301 (continuidad) para corporaciones; los instaladores solares y de generadores venden equipos; los técnicos de TI venden respaldos. **Nadie vende a la pyme el plan que une operación y tecnología.** Timing perfecto: estiaje en curso.

---

## 5. Área 3: IA segura y productiva

### El dolor
- **El 90%** de las organizaciones ecuatorianas que planean adoptar IA **no tiene una hoja de ruta**; **el 68%** no encuentra talento en IA (CITEC); madurez de IA de Ecuador: 20/100 (BCG).
- Los empleados ya usan IA **sin reglas**: pegan datos de clientes en herramientas gratuitas, lo que choca con la LOPDP.

### Cliente objetivo
Pymes medianas (20–200 empleados): distribuidoras, manufactura, servicios profesionales, clínicas, colegios.

### Oferta: "Método Bouw: Procesos → IA → Seguro"
| Paso | Quién |
|---|---|
| 1. **Mapeo de procesos** y tiempos (dónde se pierden horas) | Tú (lean, estudio de tiempos) |
| 2. **3 casos de uso con retorno calculado** (horas ahorradas, errores evitados) | Tú + Claude |
| 3. **Implementación**: asistentes con Claude, automatizaciones, plantillas; incluye el Sistema de Ventas por WhatsApp para quien lo necesite | Tú + Claude (+ proveedor si hace falta) |
| 4. **Política de uso seguro de IA**: qué datos sí y qué datos no, cuentas corporativas, permisos, cumplimiento LOPDP | Socio |
| 5. **Capacitación** por área + medición a 30/60/90 días | Ambos |

| Producto | Precio sugerido |
|---|---|
| Taller "IA segura para tu equipo" (CCQ, ConQuito, empresas) | $300–$600 por grupo, o gratis como gancho |
| Diagnóstico + hoja de ruta | $900–$1.800 |
| Implementación de 1–3 casos de uso | $2.000–$6.000 |
| Acompañamiento mensual | $300–$800/mes |

### Competencia
Agencias de chatbots (saturado) y formadores de "ChatGPT para empresas". **Pocas combinan ingeniería de procesos (retorno medible) + seguridad de datos.** Riesgo: se saturará en 12–24 meses, así que hay que entrar ya y construir casos.

---

## 6. Cómo encaja todo (y qué pasa con lo anterior)

```
                 CHEQUEO BOUW 360 (gratis o $150–$300)
      Operación (Ind.)  ·  Seguridad (Ciber)  ·  IA y automatización
                               │
        ┌──────────────────────┼──────────────────────┐
     Área 1                 Área 2                 Área 3
  Cumplimiento            Continuidad             IA segura
  ciberseguridad          y resiliencia           y productiva
        └──────────── retainers mensuales ─────────────┘
```

| Lo que ya hicimos | Dónde queda |
|---|---|
| Sistema de Ventas por WhatsApp, Calificador, posts de clínicas y gimnasios | **Producto de entrada del Área 3** para pymes pequeñas: ingreso rápido mientras se cierran los proyectos grandes. No es el foco de marca |
| "Clínica en Regla" | Paquete vertical de salud que combina **Áreas 1 + 2** (+ permisos ACESS con aliado) |
| Índice Bouw, Método 3R | Se reutilizan. Idea nueva: **"Índice Bouw de Resiliencia"** (cuántas pymes de Quito tienen respaldo, plan ante apagón y política de IA) como dato propio para prensa |

### Verticales prioritarios (no atender a todos)
1. **Cooperativas de los segmentos 3–5** (Áreas 1 + 2): regulación que ya aplica y tienen presupuesto.
2. **Salud privada mediana** (Áreas 1 + 2 + 3): datos sensibles, ransomware y continuidad.
3. **Manufactura y distribución mediana, sobre todo proveedores de empresas grandes** (Áreas 2 + 3): apagones, productividad y cuestionarios de seguridad de sus clientes.

---

## 7. Ingresos para vivir de esto (escenario a 12 meses, estimación)

| Fuente | Clientes | Ticket | Ingreso anual aprox. |
|---|---|---|---|
| Diagnósticos (Áreas 1–3) | 20 | $900 | $18.000 |
| Proyectos de implementación | 8 | $3.500 | $28.000 |
| Retainers (vCISO, acompañamiento IA, continuidad) | 6 en promedio × 12 meses | $500/mes | $36.000 |
| Productos de entrada (WhatsApp, talleres) | — | — | $8.000–$12.000 |
| **Total** | | | **~$90.000/año para 2 socios** |

> Es un escenario, no una promesa. Depende de cerrar el primer año con 3–5 casos documentados. Antes de sumar costos fijos, asegura los primeros 3 clientes pagados.

---

## 8. Marketing para este nuevo foco

| Canal | Para qué área o cliente | Qué publicar |
|---|---|---|
| **LinkedIn (principal)** | Cooperativas, manufactura, colegios, gerentes | Alertas normativas (Ley de Ciberseguridad, SEPS), "5 preguntas antes del próximo apagón", casos de IA con horas ahorradas |
| **Charlas y talleres** | CCQ (más de 3.000 afiliados), ConQuito, gremios de cooperativas, Colegio de Ingenieros | "Tu empresa ante el estiaje y el ransomware", "IA segura en 90 minutos" |
| **Prensa (dato propio)** | Todas | Índice Bouw de Resiliencia |
| **Facebook e Instagram** | Clínicas y pymes pequeñas (producto de entrada) | Lo que ya tenemos en `ideas-posts/` |
| **Correo o contacto directo** | Gerentes de riesgos y tecnología de cooperativas | Diagnóstico gratis de 30 minutos frente a la ley |

**Temas de contenido:** 🛡️ Ley y cumplimiento · ⚡ Continuidad (apagón, ransomware) · 🤖 IA segura con retorno · 🏭 Procesos y productividad · 🧾 Casos Bouw.

---

## 9. Plan de 90 días

| Semanas | Acción |
|---|---|
| **1–2** | Formaliza la sociedad (SAS), acuerdo entre socios (reparto, roles, salida), plantilla de acuerdo de confidencialidad y contrato de servicios. Arma los 3 **checklists de diagnóstico** (Ley de Ciberseguridad y SEPS · continuidad · IA) con Claude y valídalos con tu socio |
| **2–4** | **Chequeo Bouw 360 gratis a 10 organizaciones** (3 cooperativas, 3 clínicas, 4 pymes manufactureras o distribuidoras). Pregunta qué les preocupa más del estiaje, la ley y la IA |
| **3–6** | **Taller "Tu empresa ante el estiaje y el ransomware"** en la CCQ o ConQuito (timing: noviembre es el mes crítico). Publica 2 posts por semana en LinkedIn |
| **5–8** | Cierra **3 diagnósticos pagados** y **1 proyecto**. Documenta cada caso (con permiso) |
| **8–12** | Primer **retainer mensual**. Publica el Índice Bouw de Resiliencia #0 con datos de los chequeos (anonimizados). Decide qué área crece más y enfoca ahí |

---

## 10. Riesgos y cómo cubrirlos

| Riesgo | Cómo cubrirlo |
|---|---|
| Falta de credenciales frente a firmas grandes | Tu socio certifica ISO 27001 Lead Implementer o Auditor. Tú, auditor interno ISO 9001 o 22301 y Lean Six Sigma Green Belt. Publica casos y el Índice |
| Responsabilidad si un cliente sufre un ataque | Contratos con alcance claro, sin garantías de "cero incidentes", seguro de responsabilidad profesional en cuanto haya ingresos |
| Filtración de datos por usar IA | Política interna de uso de IA (la misma que venden), solo datos anonimizados y confidencialidad firmada |
| Dispersión (hacer de todo) | Máximo 3 verticales. Todo nuevo pedido debe caer en un área |
| Reglamentos de la ley retrasados | El Área 1 se vende con la SEPS y la LOPDP (ya exigibles). La ley es el acelerador, no la única razón |

---

## Fuentes
- Ley de Ciberseguridad: [NMS Law, entrada en vigencia](https://nmslaw.com.ec/blog/2026/06/01/ecuador-ley-organica-fortalecimiento-ciberseguridad/) · [Santiago Paravano, plazos y catálogo](https://santiagoparavano.substack.com/p/ecuador-ya-tiene-ley-de-ciberseguridad) · [Meythaler & Zambrano, sanciones](https://www.meythalerzambranoabogados.com/post/ley-ciberseguridad-ecuador-lofc) · [Andersen](https://ec.andersen.com/ley-organica-para-el-fortalecimiento-de-la-ciberseguridad/) · [DPL News](https://dplnews.com/entra-en-vigor-ley-de-ciberseguridad-en-ecuador/)
- Cooperativas: [Primicias, cooperativas pequeñas](https://www.primicias.ec/economia/cooperativas-pequenas-numerosas-liquidacion-superintendencia-economia-popular-solidaria-121041/) · [Primicias, liquidaciones 2025](https://www.primicias.ec/economia/cooperativas-liquidacion-quiebra-superintendencia-economia-popular-solvencia-crisis-120964/) · [SEPS, norma de riesgo operativo](https://www.seps.gob.ec/wp-content/uploads/NORMA-DE-RIESGO-OPERATIVO.pdf) · [SEPS, encuesta de servicios digitales y seguridad](https://www.seps.gob.ec/wp-content/uploads/Estudio_SEPS_ITAhora.pdf) · [Canal News, resolución SEPS 2024 de ciberseguridad](https://canalnews.ec/2024/03/05/resolucion-de-la-superintendencia-de-economia-popular-y-solidaria-genera-altas-oportunidades-para-el-canal-de-ciberseguridad/) · [Boletín Contable, cooperativas 2026](https://boletincontable.com/2026/04/21/seguro-depositos-cosede-cooperativas-ecuador-2026/)
- Ransomware y cadena de suministro: [Segurilatam, ESET ransomware 2026](https://www.segurilatam.com/ciberilatam/ransomware-2026-paises-e-industrias-mas-afectadas-segun-eset_20260528.html) · [Kaspersky, Top 3 países](https://latam.kaspersky.com/about/press-releases/empresas-latinoamericanas-reciben-un-promedio-de-dos-ataques-de-ransomware-por-minuto-senala-kaspersky) · [Kaspersky, cadenas de suministro](https://latam.kaspersky.com/about/press-releases/ciberataques-a-cadenas-de-suministro-se-disparan-mas-de-un-tercio-de-las-grandes-empresas-ya-ha-sido-blanco) · [Infosertec, pérdidas en pymes](https://infosertecla.com/2026/09/28/ciberataques-en-pymes-31-sufrio-perdidas-en-latinoamerica/)
- Estiaje: [Primicias, noviembre el mes más fuerte](https://www.primicias.ec/economia/cenace-deficit-energia-electrica-estiaje-fenomeno-elnino-ecuador-apagones-129541/) · [Lexis, CENACE 18% de probabilidad](https://www.lexis.com.ec/noticias/cenace-advierte-un-18-de-probabilidad-de-apagones-en-ecuador-durante-el-estiaje-de-octubre-de-2026-sin-importaciones-de-energia-desde-colombia) · [Primicias, estiaje desde septiembre](https://www.primicias.ec/economia/estiaje-septiembre-sequia-deficit-generacion-contratacion-retrasos-130720/)
- IA: [Sergio.ec, IA en Ecuador](https://sergio.ec/en/ia-en-ecuador-adopcion-desafios-y-oportunidades-reales/) · [La Ecuación Digital](https://www.laecuaciondigital.com/tecnologias/inteligencia-artificial/pymes-ia-experimentacion-estrategia/)
- ISO (referencias de precio, mercado español): [Step Quality, ISO 27001](https://www.stepquality.es/blog/cuanto-cuesta-certificacion-iso-27001.html) · [Tagline, ISO 9001 en Ecuador](https://tagline-soluciones.com/blog/procesos/cuanto-cuesta-certificar-iso-9001-ecuador/)
