# ideas-posts/: contenido de Bouw para Facebook e Instagram

| Archivo | Qué hay |
|---|---|
| [`BANCO-DE-IDEAS.md`](BANCO-DE-IDEAS.md) | 46 ideas de posts organizadas por dolor, ciudad (Quito/Guayaquil) y formato |
| [`REFERENTES.md`](REFERENTES.md) | Marcas con buen diseño (HubSpot, Notion, Linear, Nubank, Kommo, Alegra, DeUna…) y qué copiarle a cada una |
| `mockups/png/` | 7 maquetas listas (1080×1350, formato vertical de IG/FB) |
| `mockups/posts.html` | Fuente editable de las maquetas |
| `mockups/render.js` | Script que convierte el HTML en PNG |

## Maquetas incluidas

| Archivo | Idea | Estilo (referente) |
|---|---|---|
| `p1-tiempos.png` | El mismo paciente. Dos respuestas. | Dato gigante (HubSpot) |
| `p2-chat.png` | Son las 11:08 p. m. Tu negocio está cerrado. | Chat (Kommo) |
| `p3-recepcion.png` | Tu recepcionista no es lenta… | Frase gigante (Nubank) |
| `p4-gye-noche.png` | Tu local cierra a las 7 (Guayaquil) | Noche premium (Linear) |
| `p5-checklist.png` | WhatsApp Business bien configurado | Checklist (Notion) |
| `p6-sri.png` | SRI 2026: la factura ya no espera | Alerta regulatoria (Alegra) |
| `p7-calculo.png` | ¿Cuánto te cuesta no contestar a tiempo? | Calculadora (HubSpot) |

> `p1` usa un tiempo de ejemplo (3 h 38 m). Antes de publicarlo, cámbialo por un resultado real de tus auditorías de cliente fantasma.

## Sistema visual de Bouw (propuesta)

| Token | Color | Uso |
|---|---|---|
| Tinta | `#14161A` | Textos, fondos oscuros |
| Papel | `#F3EFE7` | Fondo claro principal |
| **Naranja Bouw** | `#FF5B1F` | Acento, el color que se reconoce. "Naranja de obra", por *bouw* = construir |
| Arena | `#E4DCCB` | Fondo secundario |
| Noche | `#0E1116` | Serie Guayaquil/premium |

- **Títulos:** Space Grotesk Bold (Google Fonts, gratis; también está en Canva).
- **Texto:** Inter.
- **Logo provisional:** `■ bouw` (cuadrado naranja + palabra en minúsculas).
- **Reglas:** un solo acento por post. Máximo 12 palabras en portada. Alterna fondo claro, naranja y oscuro en el feed.

## Regenerar las imágenes
```bash
cd ideas-posts/mockups
NODE_PATH=$(npm root -g) node render.js   # requiere playwright
```
