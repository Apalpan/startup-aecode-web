# startup-aecode-web — CLAUDE.md
> Contexto permanente del proyecto. Leer al inicio de cada sesión.

---

## Qué es este proyecto

**Sitio web público de AECODE** — Next.js static export. Página institucional de AECODE como startup EdTech AEC. Incluye: pitch principal, branding con AECODITO (mascota), métricas de startup, modelo de negocio y narrativa de inversión.

**Título del sitio:** "AECODE — Startup Intelligence Report"

**Estado actual (rebuild jun-2026):** El sitio fue reconstruido como **single-file premium sin build step**. La fuente de verdad ahora es **`build.py`** (generador Python): contiene todos los datos/copys del reporte como estructuras de datos y emite `index.html`. Se reemplazó el viejo export estático de Next.js (`_next/`, chunks, RSC) — ya no existe. Para cambiar el sitio: editar `build.py` y correr `python build.py`.

---

## Estructura del directorio (single-file)

```
startup-aecode-web/
├── build.py            ← FUENTE DE VERDAD. Genera index.html. Editar aquí.
├── index.html          ← Generado (no editar a mano; se sobrescribe)
├── 404.html            ← Página de error branded (AECODITO)
├── aecode-logo.svg     ← Logo oficial AECODE
├── aecodito.png        ← Mascota AECODITO (hero, 404, asistente, OG)
└── .nojekyll           ← GitHub Pages sin Jekyll
```

### Cómo está construido index.html (craft elite-frontend)
- Tokens OKLCH driven by `--hue` (marca AECODE índigo/violeta/verde) + fallbacks hex sRGB.
- Tipografía fluida `clamp()`: Space Grotesk (display) + Plus Jakarta Sans (texto) + JetBrains Mono (datos, tabular-nums).
- Motion: curvas `--ease-out` < 300ms, scale-on-press, reveals IntersectionObserver (solo transform/opacity), count-up, scroll-progress.
- Glass nav, command menu `⌘K`, asistente flotante AECODITO, aurora GPU.
- `prefers-reduced-motion` respetado, focus rings box-shadow, responsive real.

---

## Stack técnico

```
Generador:   build.py (Python 3, sin dependencias) → index.html
Output:      HTML/CSS/JS vanilla single-file, sin build step ni framework
Fuentes:     Google Fonts (Space Grotesk, Plus Jakarta Sans, JetBrains Mono)
Imágenes:    SVG + PNG nativos (aecode-logo.svg, aecodito.png)
QA:          node _qa.js (Playwright headless) — opcional, no commiteado
Deploy:      GitHub Pages (rama main, raíz) — push y listo
```

---

## Contenido del sitio

Basado en el título y meta description:
- **Narrativa de inversión AECODE** completa
- Branding con AECODITO (mascota IA)
- Métricas de startup y modelo de negocio
- Pitch para inversores y aliados

---

## Cómo trabajar con este proyecto

### Cualquier cambio (texto, métricas, colores, secciones)
```bash
# 1. Editar build.py (datos en NAV/HERO_STATS/ENGINES/METRICS/TREE/FUNNEL/... o CSS/JS)
python build.py          # regenera index.html
# 2. (opcional) QA visual
node _qa.js              # screenshots desktop+mobile, chequeo de consola
# 3. Deploy
git add -A && git commit -m "..." && git push   # GitHub Pages (main)
```
**Nunca editar index.html a mano** — `build.py` lo sobrescribe.

### Para cambios de assets (logo, mascota)
- `aecode-logo.svg` → editar directamente (SVG)
- `aecodito.png` → reemplazar el archivo

---

## Branding AECODE que debe mantenerse

```
Colores principales:
  #4A3AC1  (índigo — color principal)
  #7C7EDF  (violeta — secundario)
  #47CF78  (verde — positivo/crecimiento)
  #0E1121  (fondo dark)
  #EEF3F8  (texto principal)

Tipografía:
  Plus Jakarta Sans — cuerpo, UI
  Space Grotesk — headers, énfasis
  JetBrains Mono — código, datos

Mascota: AECODITO (orbe IA, avatar de la plataforma)
Logo: aecode-logo.svg
```

---

## Relación con otros proyectos AECODE

| Proyecto | Relación |
|---------|---------|
| `aecode-startup-cockpit` | Misma narrativa y métricas — fuente de verdad para datos |
| `ia-academy` | El producto principal al que enlaza el sitio |
| `trainermath-ai-core` | Producto relacionado (TrainerMath) |
| `AP_Knowledge_OS/02_EMPRESAS/AECODE/` | Contexto estratégico y docs de negocio |

---

## SEO y metadata del sitio

```
Title:       AECODE Startup Intelligence Report
Description: Reporte maestro AECODE con branding, AECODITO, métricas, pitch,
             modelo híbrido, jurado, producto, finanzas y startup readiness.
OG Title:    AECODE Startup Intelligence Report
OG Desc:     El Skill Operating System para la fuerza laboral AEC en español.
             Métricas, modelo híbrido y proyecciones en vivo.
OG Image:    aecodito.png
```

---

## Deploy

El sitio es un export estático, puede desplegarse en:
- **Vercel** (recomendado para Next.js): conectar el repo fuente
- **Netlify**: drag & drop del directorio o conectar repo
- **GitHub Pages**: push del directorio a rama `gh-pages`

---

## Contexto de negocio

- **Empresa:** AECODE
- **Audiencia:** inversores, aliados estratégicos, posibles co-fundadores, ProInnóvate
- **Objetivo del sitio:** narrativa de inversión + demostración de producto y tesis
- **Owner:** Alejandro Palpan (apalpan@genplusdesign.com)
- **Financiamiento activo:** ProInnóvate Hito 1, Startup Chile

---

## Tareas frecuentes

| Tarea | Cómo hacerlo |
|-------|-------------|
| Actualizar métricas del sitio | Editar los dicts en `build.py` (HERO_STATS, ENGINES, METRICS, TREE…) y `python build.py` |
| Cambiar logo | Reemplazar `aecode-logo.svg` |
| Actualizar AECODITO | Reemplazar `aecodito.png` |
| Agregar nueva sección | Añadir bloque en el `PAGE` de `build.py` (+ entrada en `NAV`) y regenerar |
| Ver cómo se ve | `python build.py` y abrir `index.html`, o `node _qa.js` para screenshots |
