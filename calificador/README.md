# Calificador Bouw de WhatsApp

Herramienta gratuita (inspirada en el *Website Grader* de HubSpot, ver [`EMPRESAS-GEMELAS.md`](../EMPRESAS-GEMELAS.md)) que le pone al WhatsApp de una clínica o gimnasio una **nota de 0 a 100**, estima **cuánto dinero se le escapa al mes** y le da **3 cambios prioritarios**. Al final, el dueño manda su resultado al WhatsApp de Bouw. Así se convierte en lead.

| Archivo | Uso |
|---|---|
| `index.html` | Página lista para subir a internet (un solo archivo, sin servidor) |
| `calificador.html` | Misma página en formato fragmento (versión publicada como Artifact) |

**Vista previa (privada):** https://claude.ai/artifact/E26YKRMZkFnact3swkQYK9

## 1. Configura tu número de WhatsApp (obligatorio)
En `index.html` (y en `calificador.html` si vuelves a publicar), busca:
```js
const WA_NUMBER = "";
```
y pon tu número en formato internacional **sin + ni espacios**, por ejemplo `"593991234567"`.
- Con número: aparece el botón **"Recibir mi informe completo por WhatsApp"**, que abre WhatsApp con el resultado ya escrito.
- Sin número: solo aparece **"Copiar mi resultado"**.

## 2. Súbelo gratis a internet (elige uno)
- **Netlify Drop:** entra a app.netlify.com/drop y arrastra la carpeta `calificador/`. En 1 minuto tienes un link público.
- **GitHub Pages:** en este repositorio, *Settings → Pages → Deploy from branch*, carpeta raíz. La URL será `.../calificador/`.
- **Dominio propio:** cuando tengas `bouw.ec` o similar, apunta `calificador.bouw.ec` a cualquiera de los dos.

## 3. Cómo funciona la nota (Método 3R)
| Bloque | Puntos | Preguntas |
|---|---|---|
| **Responder** | 45 | Tiempo de respuesta (15) · fuera de horario (10) · da precio (8) · catálogo y respuestas rápidas (6) · quién atiende (6) |
| **Recordar** | 35 | Seguimiento a quien no cerró (12) · recordatorios de cita, clase o renovación (12) · etapas y etiquetas (11) |
| **Reportar** | 20 | Sabe cuántos mensajes recibió (7) · sabe su conversión (8) · sabe de qué canal vienen (5) |

**Niveles:** 0–39 Crítico · 40–69 En riesgo · 70–84 Bien, con fugas · 85–100 Excelente.

**Fuga estimada al mes** = mensajes por semana × 4 × % de fuga × valor de un cliente nuevo.
El % de fuga va de 5% (nota 100) a 45% (nota 0). Es una **estimación orientativa** para abrir la conversación, no un diagnóstico. En el diagnóstico real lo reemplazas por los datos del cliente.

**Recomendaciones:** se muestran las 3 preguntas donde el negocio perdió más puntos, con el consejo correspondiente adaptado a clínica o gimnasio.

## 4. Cómo usarlo para conseguir clientes
1. **Bio de IG/FB:** "¿Qué nota saca tu WhatsApp? 👉 [link]".
2. **Anuncio de $5/día** (Quito, dueños de clínicas y gimnasios): *"¿Qué nota saca el WhatsApp de tu clínica? Descúbrelo en 2 minutos."*
3. **Después de la auditoría de cliente fantasma:** "Te dejo el calificador para que veas tu nota. Si quieres, lo revisamos juntos."
4. **Post fijado:** carrusel con los 3 bloques del Método 3R y el link.
5. **Seguimiento:** cuando alguien mande su resultado, respóndele en menos de 5 minutos (predica con el ejemplo) y ofrécele el diagnóstico de 20 minutos.

## 5. Alternativa sin código (Tally o Google Forms)
Si prefieres un formulario que guarde las respuestas, copia las 11 preguntas y sus puntos de la tabla de arriba en **Tally** (permite calcular puntaje y mostrar un resultado) y pide el WhatsApp al final.

## Privacidad
La página no guarda ni envía respuestas por sí sola. Solo se comparten si el usuario decide mandarlas por WhatsApp o copiarlas. Si pasas a Tally/Forms y guardas datos, agrega un aviso de privacidad según la Ley de Protección de Datos (LOPDP).
