# El nicho de Bouw: preparar a los proveedores pymes para pasar las evaluaciones de sus clientes regulados

> 🧭 **Modelo principal de Bouw:** [`HANOVA-QUITO.md`](HANOVA-QUITO.md) (la Hanova de Quito). Este documento queda como pieza de apoyo.

> **En una frase:** los bancos y las cooperativas **están obligados por norma** a evaluar la continuidad, la seguridad y el manejo de datos de sus proveedores. Los proveedores pymes (software, call center, cobranza, soporte de TI, custodia de documentos…) **reciben esas evaluaciones y no tienen cómo pasarlas.** Bouw los deja listos.
>
> Reemplaza como foco a [`ESTRATEGIA-3-AREAS.md`](ESTRATEGIA-3-AREAS.md) y [`VENTA-ATERRIZADA.md`](VENTA-ATERRIZADA.md). No es una idea nueva: es el punto exacto donde se cruzan las tres áreas y donde nadie está parado.

---

## 1. Por qué existe el problema (la cadena de obligación)

```
  NORMA                          OBLIGADO                         QUIEN SUFRE
  ─────                          ────────                         ───────────
  Superintendencia de Bancos  ─► Bancos           ─┐
  (Res. SB-2021-2126,             (y aseguradoras)  │  "Demuéstrame tu plan de
   riesgo operativo)                                ├─► continuidad, tus controles  ─►  PROVEEDOR PYME
  SEPS (norma de riesgo       ─► Cooperativas     ─┤   de seguridad y cómo cuidas     (no tiene cómo
   operativo, art. 18)            (~394)            │   los datos de mis socios"        demostrarlo)
  LOPDP (encargados)          ─► Cualquiera que   ─┘                                        │
                                  entregue datos                                            ▼
                                  a un proveedor                                          BOUW
```

| Norma | Qué le exige a la entidad sobre sus proveedores |
|---|---|
| **Superintendencia de Bancos, norma de riesgo operativo** (Res. SB-2021-2126) | Un **proceso integral de administración de proveedores**: homologación, **evaluación periódica**, cláusulas de SLA, confidencialidad y auditoría, control del riesgo de terceros. A los proveedores de nube les exige **ISO 27001** |
| **SEPS, norma de riesgo operativo** (cooperativas) | **Calificación y selección de proveedores** (art. 18). Deben **monitorear y verificar que los planes de continuidad de los proveedores de servicios críticos estén actualizados**, con revisión al menos **una vez al año** |
| **LOPDP** | Todo proveedor que trata datos por cuenta de otro (el "encargado") necesita un **contrato con medidas técnicas y organizativas de seguridad**, y responde por sus incumplimientos |
| **Ley de Ciberseguridad** (vigente desde el 22/5/2026) | El sistema financiero es servicio esencial. La presión sobre la cadena de proveedores solo aumenta |

**Traducción:** el banco o la cooperativa **tiene que** pedirle al proveedor pruebas de continuidad, seguridad y protección de datos, y tiene que volver a pedirlas **cada año**. Si el proveedor no las tiene, la entidad queda mal ante su supervisor. Así que presiona al proveedor o lo cambia.

---

## 2. Por qué es exactamente su nicho

Lo que el proveedor tiene que demostrar se reparte **justo** entre ustedes dos:

| Lo que le piden al proveedor | Quién de Bouw lo resuelve |
|---|---|
| Plan de continuidad del negocio (procesos críticos, tiempos de recuperación, contingencia, pruebas) | **Tú**, ing. industrial |
| Procesos documentados, SLAs e indicadores de servicio | **Tú** |
| Controles de seguridad de la información y evidencias (accesos, respaldos, antimalware, incidentes) | **Tu socio**, ciberseguridad |
| Medidas de protección de datos y contrato de encargado (LOPDP) | **Tu socio** + abogado aliado para el contrato |
| Responder el cuestionario del cliente y armar la carpeta de evidencias | **Ambos, con Claude** para redactar rápido |

Un consultor de procesos solo no puede hacer la parte de seguridad. Un técnico de ciberseguridad solo no hace el plan de continuidad ni los procesos. **Ustedes dos juntos cubren el 100% de lo que piden.**

**El papel de la IA:** Claude **no es lo que vendes**. Es por qué pueden cobrar precio de pyme con margen: una política, un plan o una respuesta de cuestionario en horas en lugar de días. (Los talleres de IA quedan descartados, como bien dijiste: ya existen y hay mucha competencia.)

---

## 3. El cliente exacto

**Pymes de 10–200 personas que le prestan servicios a bancos, cooperativas, mutualistas o aseguradoras**, sobre todo si tocan sistemas, datos de clientes o procesos críticos:

| Tipo de proveedor | Por qué lo evalúan fuerte |
|---|---|
| Empresas de software (core, canales digitales, apps, crédito) | Acceso a sistemas y datos. Servicio crítico |
| Soporte de TI, redes, nube o datacenter local | Acceso privilegiado. La norma pide ISO 27001 a la nube |
| Call center, contact center y cobranza | Manejan datos personales de socios y clientes |
| Impresión, digitalización y custodia de documentos | Datos personales y continuidad |
| Mensajería y courier de tarjetas y documentos | Datos y continuidad |
| Agencias de marketing con bases de socios | Datos personales (LOPDP) |
| Seguridad física y monitoreo | Continuidad y acceso a instalaciones |

**Dónde están:** Quito concentra la sede de la mayoría de cooperativas grandes y medianas y de sus proveedores. Cuenca también tiene muchas. Empieza en Quito.

---

## 4. Competencia: qué existe y por qué no les quita este espacio

| Quién | Qué hace | Por qué no es competencia directa |
|---|---|---|
| **Certificadoras y auditoras** (p. ej. AENOR, que ofrece homologación de proveedores en Ecuador) | **Evalúan** al proveedor por encargo del banco o la empresa grande | Están del lado del que evalúa. Por independencia, no asesoran al que auditan |
| **Software de riesgo** (GlobalSuite, Pirani) | Herramientas para que **la entidad** gestione sus riesgos y proveedores | Le venden a la entidad, no al proveedor |
| **Big Four y estudios jurídicos** | Asesoran a bancos y cooperativas grandes | No bajan al proveedor pyme ni a precios de pyme |
| **Consultores de ISO 27001** | Proyectos de certificación completos ($8.000–$25.000+ y varios meses) | Es más de lo que un proveedor pyme necesita para **pasar la evaluación**. Bouw ofrece lo proporcional y, si el contrato exige certificación, acompaña después |
| **El técnico de sistemas del proveedor** | Configura equipos | No sabe hacer un plan de continuidad ni responder un cuestionario normativo |

**Hueco:** *preparación rápida, proporcional y a precio de pyme del lado del proveedor.* No encontré a nadie en Ecuador posicionado ahí. **Es una hipótesis hasta la validación de la sección 7.**

---

## 5. Por qué pagarían (no es "me gustaría", es "o lo hago o pierdo el contrato")

- **Disparador concreto:** llega un cuestionario de evaluación con plazo, una renovación de contrato o una licitación que exige evidencias.
- **Costo de no hacerlo:** perder o no ganar un contrato que suele valer mucho más que el servicio de Bouw.
- **Recurrencia forzada:** la entidad debe **reevaluar cada año**, así que el proveedor necesita mantener y actualizar sus evidencias.
- **Ancla de precio en la venta:** *"¿Cuánto vale al año tu contrato con la cooperativa? Esto cuesta una fracción y lo necesitas cada año."*

---

## 6. La oferta: un solo producto, "Proveedor Listo"

| Fase | Qué incluye | Plazo | Precio de referencia |
|---|---|---|---|
| **1. Diagnóstico frente al cuestionario real** | Tomas el cuestionario (o la norma) de su cliente, lo contrastas con su situación y entregas un semáforo de brechas y un plan | 1–2 semanas | $500–$900 (se descuenta si contratan la fase 2) |
| **2. Preparación** | Plan de continuidad + prueba, procesos y SLAs documentados, políticas y controles mínimos de seguridad implementados con evidencia, medidas LOPDP + contrato de encargado (con abogado), **respuestas al cuestionario + carpeta de evidencias** | 4–6 semanas | $2.500–$5.000 (10–50 personas) · $5.000–$9.000 (50–200) |
| **3. Mantenimiento anual** | Actualización de evidencias, prueba anual del plan, acompañamiento en la reevaluación del cliente | Todo el año | $150–$400/mes |
| *Después, si el contrato lo exige* | Camino a ISO 27001 o 22301 con tu socio | — | Proyecto aparte |

Nada más. No talleres, no WhatsApp y no "chequeo 360" genérico: **un producto, un cliente, un resultado ("pasas la evaluación")**. Los cuestionarios de [`chequeo-360/`](chequeo-360/) (1 y 2) se reutilizan como base de la fase 1.

---

## 7. Validación en 2 semanas (antes de invertir más)

No es para buscar ideas nuevas: es para confirmar que este nicho paga.

**Conversaciones (10 en total):**
- **5 proveedores** de bancos o cooperativas:
  1. "¿Alguna vez un cliente financiero les envió un cuestionario o evaluación de proveedor? ¿Qué pedía?"
  2. "¿Cuánto tiempo les tomó responderlo? ¿Qué no pudieron responder?"
  3. "¿Han perdido o casi perdido un contrato por eso? ¿Les pusieron observaciones?"
  4. "¿Quién lo resolvió? ¿Cuánto les costó?"
- **3 jefes de riesgos o seguridad** de cooperativas o bancos:
  1. "¿Qué es lo que más les falla a sus proveedores en la evaluación?"
  2. "¿Tienen proveedores críticos que no pasan y no pueden cambiar?"
- **2 dueños de empresas de software para cooperativas:** son el segmento más probable.

**Consigue 2–3 cuestionarios reales** (sin datos del cliente). Con eso armas la plantilla de la fase 1 y tu oferta se vuelve concreta de verdad.

| Resultado | Decisión |
|---|---|
| 3 de 5 proveedores recibieron evaluaciones y les costó responderlas | ✅ **El nicho existe.** Ofrece el diagnóstico pagado |
| 1 diagnóstico pagado en los primeros 30 días | ✅ Confirma que pagan. Sigue a la fase 2 |
| Los proveedores dicen "nadie nos pide nada" | ❌ La norma no se aplica en la práctica. Cambia al lado de la entidad (cooperativas directamente) |

---

## 8. Dónde encontrar a los primeros clientes

1. **Las mismas cooperativas y bancos:** el jefe de riesgos **quiere** que sus proveedores pasen, y puede referirte a los que están atrasados. ⚠️ Regla ética: nunca evalúes para la cooperativa y prepares al proveedor en el mismo caso (conflicto de interés).
2. **LinkedIn:** busca "software para cooperativas Ecuador", "call center cobranza Quito", "custodia documental Quito" y contacta a gerentes generales.
3. **Ferias, redes y eventos del sector cooperativo y bancario:** ahí exponen los proveedores.
4. **Mensaje de contacto:**
> "Hola [Nombre], vi que [empresa] trabaja con cooperativas. Por norma (SEPS y Superintendencia de Bancos), sus clientes deben evaluar cada año el plan de continuidad, la seguridad y el manejo de datos de sus proveedores. Somos Bouw (ingeniería industrial + ciberseguridad) y preparamos a proveedores para pasar esas evaluaciones. ¿Les ha llegado algún cuestionario de ese tipo este año?"

---

## 9. Qué se deja en pausa
Chatbots y WhatsApp, talleres de IA, gimnasios, Guayaquil y "Clínica en Regla". Quedan documentados en el repositorio por si el nicho no se valida, pero **no se trabajan** mientras se prueba este.

---

## Fuentes
- Superintendencia de Bancos: [Asobanca, cronograma de la norma de riesgo operativo (SB-2021-2126)](https://asobanca.org.ec/wp-content/uploads/2022/05/Cronograma-plazos-cumplimiento-Norma-Riesgo-Operativo-Res.-Nro.-SB-2021-2126.pdf) · [GlobalSuite, requisitos de la norma](https://www.globalsuitesolutions.com/es/norma-control-gestion-riesgo-operativo-ecuador/) · [Pirani, norma de control](https://www.piranirisk.com/es/blog/norma-control-riesgos-operativos-ecuador-superbancos) · [Codificación de normas de la SB](https://www.superbancos.gob.ec/bancos/codificacion-de-normas-de-la-sb-libro-uno-sistema-financiero/)
- SEPS: [Norma de riesgo operativo](https://www.seps.gob.ec/wp-content/uploads/NORMA-DE-RIESGO-OPERATIVO.pdf) · [Resolución SEPS 0116 riesgo operativo](https://www.seps.gob.ec/wp-content/uploads/RESOLUCIO%CC%81N-Nro.-SEPS-IGT-IGS-INSESF-INR-INGINT-INSEPS-IGJ-0116-RIESGO-OPERATIVO_firmado.pdf) · [Resolución de seguridad de la información (2022)](https://rfd.org.ec/docs/normativa/2022/Boletin-32/Seguridad%20Informacion.pdf)
- LOPDP (encargados): [Cumple.ec, contrato de encargo](https://cumple.ec/blog/contrato-encargo-tratamiento-lopdp-ecuador) · [Cumple.ec, subencargados](https://cumple.ec/blog/obligaciones-encargado-subencargado-lopdp-ecuador)
- Competencia: [AENOR Ecuador, homologación de proveedores](https://www.aenor.com/web/ecu/inspeccion/homologacion-proveedores)
- Contexto: [Kaspersky, cadenas de suministro](https://latam.kaspersky.com/about/press-releases/ciberataques-a-cadenas-de-suministro-se-disparan-mas-de-un-tercio-de-las-grandes-empresas-ya-ha-sido-blanco) · [Primicias, cooperativas](https://www.primicias.ec/economia/cooperativas-pequenas-numerosas-liquidacion-superintendencia-economia-popular-solidaria-121041/)
