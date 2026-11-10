# Copia de referencia del sitio BOUW

Fuente: https://bouw-eight.vercel.app/, descargado el 10/11/2026.

## Contenido de esta carpeta

| Ruta | Qué es |
|---|---|
| `index.html` | HTML completo del sitio (descargado con curl, renderizado del lado del servidor) |
| `assets/` | Logos e imágenes de marca (ver la lista más abajo) |
| `next/` | Archivos JS/CSS de `_next/static` que referencia el HTML (solo para consulta) |
| `capturas/pagina-completa.png` | Página completa a 1440 px de ancho, en español |
| `capturas/encabezado.png` | Barra de navegación con el logo (a 2×) |
| `capturas/logo-recorte.png` | Recorte ajustado del logo del encabezado (a 2×) |
| `TEXTOS-DEL-SITIO.md` | Todo el texto visible en español, en orden de aparición |

## Archivos de logo y marca encontrados

| Archivo | Origen en el sitio | Tamaño | Descripción |
|---|---|---|---|
| `assets/bouw-logo-negativo.png` | `/marca/bouw-logo-negativo.png`: `<img alt="BOUW">` del **encabezado** (h-10) y del **footer** (h-14), servido por `/_next/image` | 720×304, PNG con transparencia | **Logo principal.** Palabra "BOUW" en mayúsculas, sans-serif extendida y muy gruesa, en cian claro (≈ `#7dd3e3`). Un **dragón blanco** de grabado/tinta, con las alas abiertas, está posado sobre la "W" y asoma por encima a la derecha. Versión "negativo", pensada para fondo oscuro: sobre el fondo claro del navbar el dragón blanco casi no se ve. |
| `assets/bouw-dragon-blanco.png` | `/marca/bouw-dragon-blanco.png`, referenciado solo en JS (componente de marca, variante `dragon`, 900×648) | 900×648, PNG con transparencia | Solo el dragón, en blanco sobre transparente (se ve en blanco si se abre sobre fondo blanco). Se usa en el dragón interactivo ("Haz clic · lanza fuego"). |
| `assets/opengraph-image.png` | `meta og:image` y `twitter:image` | 1200×630 | Logo BOUW cian con el dragón blanco sobre fondo azul noche (≈ `#06101f`). Alt: "BOUW: el logotipo con el dragón sobre fondo azul noche". |
| `assets/icon.png` | `<link rel="icon">` 512×512 | 512×512 | Ícono de app: el dragón blanco sobre un cuadrado redondeado azul noche. |
| `assets/apple-icon.png` | `<link rel="apple-touch-icon">` | 180×180 | El mismo ícono del dragón para iOS. |
| `assets/favicon.ico` | `<link rel="icon">` 64×64 | 16–64 px (4 tamaños) | Favicon con el dragón. |

No se encontraron:

- **SVG de logo en línea.** Los únicos `<svg>` del encabezado son íconos de interfaz (la luna del cambio de tema); el footer no tiene ninguno. Por eso **no** hay `logo-navbar-inline.svg` ni `logo-footer-inline.svg`: el logo del navbar y el del footer son el mismo PNG.
- **SVG de logo en los JS.** Los SVG de `next/*.js` son íconos (flechas, cerrar, play, sol), diagramas de los casos (mapa de flujo, trazabilidad, medidores) e ilustraciones isométricas, pero ninguno es el logo.
- **Manifest.** `manifest.webmanifest`, `manifest.json` y `site.webmanifest` dan 404. Tampoco existen otras variantes como `/marca/bouw-logo.png`, `-positivo.png` o `.svg`.

## Logo principal del encabezado

**`assets/bouw-logo-negativo.png`**: la palabra **BOUW** en cian, en una sans extendida muy gruesa, con un **dragón blanco ilustrado** (alas abiertas, cola enroscada) apoyado sobre la W. En el navbar aparece a 40 px de alto, seguido de un separador vertical y del texto "AUTOMATION & DIGITAL" en dos líneas, en gris y espaciado ancho. Paleta: cian claro, blanco y azul noche como fondo de marca.

## ¿Coincide con `posts-bouw/logo-bouw.svg`?

**No.** `posts-bouw/logo-bouw.svg` es otro símbolo, sin texto y sin dragón:

- Es un monograma geométrico, una especie de "B" o "P", con dos bloques en L azul marino (`#1b4c80` → `#0d2947`).
- Tiene un arco cian (`#4fd6e8` → `#1a97b3`) y un arco naranja (`#f79b4a` → `#d5610f`) con puntas de flecha.
- Lleva un trazo de circuito cian y dos esferas, una turquesa y una naranja.

Solo comparten parte de la paleta: el cian y el naranja (`#4fd6e8`, `#f79b4a`) también se usan como colores de acento en el sitio (`r`, `i`, `s`, `n` en `next/3hag0255517ro.js`). La identidad que el sitio publica hoy es la palabra **BOUW en cian con el dragón blanco**, no el monograma de `logo-bouw.svg`.
