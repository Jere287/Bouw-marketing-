# Dragón 3D del hero — bouw-eight.vercel.app

El dragón del hero ("Del diseño a la realidad") **no es una imagen**: es un modelo 3D (WebGL, three.js / React Three Fiber) que se renderiza en vivo en un `<canvas>` fijo a pantalla completa.

- **Dragón:** `/dragon.glb`, un modelo con esqueleto y 7 animaciones. Se carga de forma diferida desde el chunk JS `2wl59rriraxna.js`.
- **Letras "BOUW":** el código las genera en tiempo de ejecución (geometría extruida). No existen como archivo.
- **"Plano / realidad":** son dos materiales sobre la misma escena, separados por el divisor arrastrable. El modo plano es un shader con wireframe y líneas cian. No hay dos imágenes distintas.
- **next/image:** el dragón no pasa por next/image (solo lo usan los logos y las fotos de proyectos). Por eso no hay variantes `w=3840`.
- **Archivos que no se usan:** el chunk menciona `/px.png`, `/nx.png`, `/py.png`, `/ny.png`, `/pz.png` y `/nz.png`. Son valores por defecto del componente `Environment` de drei y el navegador nunca los pidió (comprobado en 1440×900 claro, 1440×900 oscuro y 390×844).

## originales/ (descargados tal cual del sitio)

| Archivo | URL de origen | Tamaño | Nota |
|---|---|---|---|
| `dragon.glb` | https://bouw-eight.vercel.app/dragon.glb | 853 276 B | glTF 2.0 (glTF-Transform 4.5.1, EXT_meshopt_compression + EXT_texture_webp). 1 malla con esqueleto `model.002`. Animaciones: caminar, estirarse, frenado, fuego, planeo, rugido, vuelo |
| `dragon-texture_diffuse.webp` | extraída de `dragon.glb` (imagen 1) | 1024×1024 px | color base |
| `dragon-texture_normal.webp` | extraída de `dragon.glb` (imagen 0) | 1024×1024 px | mapa normal |
| `dragon-texture_metallic-texture_roughness.webp` | extraída de `dragon.glb` (imagen 2) | 1024×1024 px | metal/rugosidad |
| `2wl59rriraxna.js` | https://bouw-eight.vercel.app/_next/static/immutable/chunks/2wl59rriraxna.js | 1 176 856 B | chunk diferido con three.js y la escena del hero (carga `dragon.glb`, construye las letras y los shaders plano/realidad) |

## capturas/ (deviceScaleFactor 3)

Hay dos tipos de captura:

- **Transparentes** (`*-transparente.png`): fondo de html/body/hero en transparent, todo el DOM oculto salvo el canvas, `omitBackground: true` y recorte automático al contorno del modelo. Son PNG RGBA.
- **Con fondo** (`*-con-fondo.png`): la página tal cual, recortada a la zona del dragón (x 560–1440, y 230–700 px CSS).

| Archivo | Píxeles | Contenido |
|---|---|---|
| `dragon-claro-realidad-transparente.png` | 2128×1105 RGBA | dragón + BOUW, modo **realidad**, fondo transparente |
| `dragon-claro-plano-transparente.png` | 2132×1108 RGBA | dragón + BOUW, modo **plano** (blueprint), fondo transparente |
| `dragon-claro-dividido-transparente.png` | 2131×1108 RGBA | estado inicial (divisor en su sitio; solo el borde de la B sale en plano) |
| `dragon-oscuro-realidad-transparente.png` | 2135×1121 RGBA | tema oscuro, realidad, transparente |
| `dragon-oscuro-plano-transparente.png` | 2138×1124 RGBA | tema oscuro, plano, transparente |
| `dragon-oscuro-dividido-transparente.png` | 2131×1108 RGBA | tema oscuro, estado inicial, transparente |
| `dragon-movil-390-transparente.png` | 935×568 RGBA | móvil 390×844, transparente |
| `dragon-claro-realidad-con-fondo.png` | 2640×1410 RGB | tema claro, realidad, con fondo de la página |
| `dragon-claro-plano-con-fondo.png` | 2640×1410 RGB | tema claro, plano |
| `dragon-claro-dividido-con-fondo.png` | 2640×1410 RGB | tema claro, estado inicial |
| `dragon-oscuro-realidad-con-fondo.png` | 2640×1410 RGB | tema oscuro, realidad |
| `dragon-oscuro-plano-con-fondo.png` | 2640×1410 RGB | tema oscuro, plano |
| `dragon-oscuro-dividido-con-fondo.png` | 2640×1410 RGB | tema oscuro, estado inicial |
| `dragon-movil-390-con-fondo.png` | 1170×2532 RGB | pantalla completa en móvil 390×844 |
| `dragon-solo-reposo-frente.png` | 2476×1958 RGBA | **solo el dragón, sin letras**: render propio de `dragon.glb` (three 0.160, pose de reposo, de frente), transparente |
| `dragon-solo-reposo-tres-cuartos.png` | 2400×1952 RGBA | solo el dragón, reposo, vista 3/4, transparente |
| `dragon-solo-rugido.png` | 2384×1586 RGBA | solo el dragón, animación "rugido" (t = 0.8 s), transparente |
| `dragon-solo-vuelo.png` | 2344×824 RGBA | solo el dragón, animación "vuelo" (t = 0.3 s), transparente |

**Aviso de resolución:** el sitio limita la resolución del canvas. Con DPR 3 dibujó un buffer de 1326×829 para un viewport de 1440×900, es decir, unas 0.92× (en este entorno de captura, que no tiene GPU). Las capturas del sitio a DPR 3 están, por tanto, ampliadas: el detalle real equivale a unos 710 px de ancho. Los renders `dragon-solo-*` sí se dibujaron a resolución nativa (canvas de 3200×3200), pero con iluminación propia, más oscura que la del sitio y sin el brillo cian de borde.

## Cuál usar

- **Dragón + BOUW, transparente (igual que en la web):** `capturas/dragon-claro-realidad-transparente.png`.
- **Versión blueprint/plano, transparente:** `capturas/dragon-claro-plano-transparente.png`.
- **Dragón solo, sin letras, transparente:** `capturas/dragon-solo-reposo-tres-cuartos.png`. Es la de más resolución real, aunque la iluminación difiere de la web.
- **Máxima calidad posible:** `originales/dragon.glb`, el modelo original. Se puede volver a renderizar a cualquier tamaño, pose o animación (en Blender, three.js editor o https://gltf-viewer.donmccurdy.com).
- **Con fondo de la página:** `capturas/dragon-claro-realidad-con-fondo.png` (claro) o `capturas/dragon-oscuro-realidad-con-fondo.png` (oscuro).
