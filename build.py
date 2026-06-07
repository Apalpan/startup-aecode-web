# -*- coding: utf-8 -*-
"""
AECODE — Startup Intelligence Report
Generador single-file (sin build step) del sitio publico de AECODE.

Fuente de verdad mantenible: editar los datos/copys aqui y re-ejecutar
    python build.py
para regenerar index.html. Reemplaza el viejo export estatico de Next.js.

Craft aplicado (skills elite-frontend):
  - Tokens OKLCH driven by --hue (marca AECODE indigo/violeta/verde) + fallbacks hex
  - Tipografia fluida clamp(), Space Grotesk + Plus Jakarta Sans + JetBrains Mono (tabular-nums)
  - Motion engine: curvas custom <300ms, scale-on-press, reveals transform/opacity-only
  - Glass-depth en superficies flotantes, interface-quality (focus rings, teclado, aria)
  - Command menu (Ctrl/Cmd K), AECODITO assistant, scroll progress, count-up
  - prefers-reduced-motion respetado, responsive real
"""

# =============================================================================
#  DATA  (contenido real extraido del reporte AECODE — public-safe)
# =============================================================================

NAV = [
    ("norte", "North Star"),
    ("problema", "Problema"),
    ("producto", "Producto"),
    ("modelo", "Modelo"),
    ("mercado", "Mercado"),
    ("metricas", "Metricas"),
    ("economics", "Unit economics"),
    ("gtm", "GTM"),
    ("equipo", "Equipo"),
    ("acciones", "Roadmap"),
]

HERO_STATS = [
    ("0.17", "North Star · skills verificadas / MAU", "meta beta 0.40", 0.17, "", "", 2, False),
    ("$5,150", "MRR total (modelo hibrido)", "meta 12 meses $30k", 5150, "$", "", 0, True),
    ("3.1x", "LTV / CAC", "objetivo > 3x", 3.1, "", "x", 1, False),
    ("420", "Usuarios activos (MAU)", "meta beta 750", 420, "", "", 0, False),
]

PRINCIPIOS = [
    ("Aprendizaje por nivel", "Aprendizaje segun nivel, rol y objetivo profesional — no un catalogo plano."),
    ("Microlearning", "Capsulas cortas para avanzar sin depender de programas largos."),
    ("Practica con caso real", "Practica con casos reales AEC, no solo teoria."),
    ("Certificacion por evidencia", "Certificacion basada en evidencia entregable, no solo asistencia."),
    ("IA como coach", "IA como recomendador, coach y apoyo de evaluacion — no decoracion."),
]

# Modelo hibrido — 4 motores (MRR real / supuesto separado)
ENGINES = [
    {
        "name": "AECODE Live Training",
        "tag": "Motor de caja, confianza y contenido semilla",
        "mrr": "$3,090", "mrr_num": 3090,
        "desc": "Cursos en vivo, cohortes, diplomados, workshops y comunidad guiada para validar demanda, generar casos reales y producir contenido semilla.",
        "kpis": [("Live revenue acumulado", "PEN 140k", "2 anos"), ("Meta MRR", "$7.5k", "escala")],
        "accent": "indigo", "share_now": 60, "share_goal": 25,
    },
    {
        "name": "AECODE Microlearning Skill OS",
        "tag": "Motor de recurrencia, personalizacion y certificacion",
        "mrr": "$1,288", "mrr_num": 1288,
        "desc": "Rutas adaptativas, capsulas cortas, practica aplicada, evidencias, rubricas, creditos, IA y Skill Passport.",
        "kpis": [("Consumo de creditos", "1,120/mes", "supuesto"), ("Meta MRR", "$18k", "escala")],
        "accent": "violet", "share_now": 25, "share_goal": 60,
    },
    {
        "name": "AECODE Enterprise",
        "tag": "Pilotos B2B y dashboards de talento",
        "mrr": "$515", "mrr_num": 515,
        "desc": "Licencias por equipo, diagnosticos de brecha, reportes de talento y upskilling medible.",
        "kpis": [("Senal", "Seats B2B", "pipeline"), ("Foco", "Piloto 30 dias", "por rol")],
        "accent": "green", "share_now": 10, "share_goal": 10,
    },
    {
        "name": "AECODE Credentials",
        "tag": "Certificacion y validacion por partners",
        "mrr": "$257", "mrr_num": 257,
        "desc": "Certificaciones, evaluaciones avanzadas, partners y eventos especializados.",
        "kpis": [("Senal", "Credenciales", "emitidas"), ("Foco", "Attach rate", "credential")],
        "accent": "violet", "share_now": 5, "share_goal": 5,
    },
]

# Metricas con rango saludable + decision (lenguaje ejecutivo)
METRICS = [
    ("Skills certificadas / MAU", "North Star Metric", "Cuantas habilidades reales certifica cada usuario activo en el mes. Conecta aprendizaje, practica, evidencia, certificacion y retencion.", "0.2–0.4 beta · >0.8 escala", "Mejorar ruta, practica y feedback antes de escalar adquisicion.", True),
    ("Inician una ruta", "Activacion", "Personas que pasan de interes general a una ruta concreta por rol o meta.", "50–70% beta", "Diagnostico + primera ruta recomendada en < 5 min.", False),
    ("Practican con caso real", "Aplicacion", "Usuarios que pasan de ver contenido a aplicar lo aprendido. Es el puente entre curso y skill verificable.", "45–65%", "Reducir friccion de la primera practica con casos cercanos al trabajo.", False),
    ("Suben evidencia", "Evidencia", "Entregan archivo, modelo, reporte, script o dashboard evaluable. Diferencia AECODE de un catalogo de cursos.", "35–60% beta · >60% fuerte", "Dividir la evidencia en pasos pequenos y mejorar ejemplos.", False),
    ("Skills aprobadas", "Calidad", "Evidencias que cumplen rubrica y se vuelven progreso certificable. Prueba calidad, no solo actividad.", "55–75% beta", "Ajustar rubricas, feedback y dificultad por nivel.", False),
    ("Retencion mensual", "Lifecycle", "Usuarios que vuelven a aprender, practicar o certificar al mes siguiente. El negocio existe si el progreso es continuo.", "30–45% beta · >50% fuerte", "Recomendaciones, recordatorios y rutas cortas de siguiente skill.", False),
    ("Conversion a pago", "Monetizacion", "Usuarios que pasan de free a pagar por curso, suscripcion, creditos o certificacion.", "3–8% B2C · >10% cohortes", "Vender outcome: certificado, feedback y ruta verificable.", False),
    ("% ingresos escalables", "Escalabilidad", "Reduce dependencia de horas de instructor migrando live a contenido reutilizable.", ">30–50% en MVP", "Convertir cada live en capsulas, skills y creditos.", False),
]

# Arbol de metricas: norte -> producto/growth/revenue (actual -> meta)
TREE = [
    ("Adquisicion", "growth", "Comunidad y contenido producen leads que entran a diagnostico.", [
        ("Qualified leads / mes", "1,200", "target"), ("CAC blended", "<$30", "target"),
    ]),
    ("Activacion", "indigo", "El usuario entiende su punto de partida y arranca una primera skill.", [
        ("Path generated / mes", "403 → 900", "actual → meta"), ("Time to first skill", "<7d → <24h", "objetivo"),
    ]),
    ("Evidencia y calidad", "violet", "La ruta solo vale si produce entregables validables.", [
        ("Rubric pass score", "78 → >82", "/100"), ("Verified skill rate", "sube", "calidad"),
    ]),
    ("Lifecycle", "indigo", "El usuario vuelve porque ve progreso profesional acumulable.", [
        ("Skills / user / month", "0.17 → 0.40", "NSM"), ("Next skill start", "activar", "retencion"),
    ]),
    ("Monetizacion", "green", "La evidencia abre pago por suscripcion, creditos, certificacion y B2B.", [
        ("Total MRR", "$5,150 → $30k", "hibrido"), ("LTV / CAC", "3.1x → >3x", "filtro escala"),
    ]),
    ("Ops / IA", "violet", "El live crea confianza; la plataforma la convierte en activos reutilizables.", [
        ("Support cost / user", "$2.8 → <$1.5", "eficiencia"), ("AI extraction accuracy", ">70–85%", "human-in-loop"),
    ]),
]

# Funnel maestro: visita -> skill verificada -> pago
FUNNEL = [
    ("Visitante", "1000", "100%", "Trafico con intencion, no academia generica."),
    ("Registro", "20–28%", "activacion", "CTA = diagnosticar skill gap, no comprar curso."),
    ("Skill start", "ruta", "primer valor", "Mostrar una skill pequena y accionable hoy."),
    ("Evidencia", "entregable", "calidad", "Ejemplo, rubrica y entregable claro."),
    ("Skill verified", "validada", "progreso", "Feedback rapido = sensacion de progreso."),
    ("Pago", "79 subs", "revenue", "Pago ligado a certificacion o desbloqueo de ruta."),
]

ECONOMICS = [
    ("LTV / CAC", "3.1x", ">3x", "Cada cliente deja mas valor del que cuesta adquirirlo."),
    ("CAC payback", "objetivo", "<6 meses", "Velocidad de recuperacion de la inversion comercial."),
    ("Margen bruto hibrido", "objetivo", ">60%", "Sube margen digital, baja dependencia de horas sincronas."),
    ("Runway", "planificar", "12–18 meses", "Caja para ejecutar hitos antes de levantar."),
]

ACCIONES = [
    "Definir la primera ruta wedge con mayor dolor, evidencia y disposicion de pago.",
    "Separar P&L de live, plataforma e hibrido para no confundir caja con escalabilidad.",
    "Medir semanal: registro, diagnostico, skill start, evidencia, feedback, verificacion y pago.",
    "Convertir cada curso live en capsulas, skills, rubricas y evidencias reutilizables.",
    "Lanzar piloto B2B de 30 dias con brecha por rol, 3 skills y reporte de resultados.",
    "Versionar el Skill Graph AEC como activo central de producto.",
    "Crear data room con metricas reales, supuestos separados y benchmarks citados.",
    "Calcular CAC, LTV, margen bruto, churn, payback, burn y runway antes de levantar.",
]

# AECODITO quick-facts (asistente)
FACTS = [
    ("Que es AECODE", "Plataforma educativa inteligente para profesionales AEC: convierte cada clase en una skill practicada, evidenciada, validada y acumulable."),
    ("North Star", "Skills verificadas con evidencia / usuarios activos mensuales. Actual 0.17 (72/420), meta beta 0.40 (300/750)."),
    ("Modelo", "Hibrido: Live Training (caja) + Microlearning Skill OS (recurrencia) + Enterprise + Credentials. MRR total $5,150."),
    ("Wedge", "Profesional AEC que necesita empleabilidad digital; segundo mercado: empresa AEC con brechas BIM, IA, VDC o productividad."),
    ("Por que ahora", "La IA acelera la obsolescencia tecnica y permite personalizar a escala. BIM, datos y automatizacion ya son requisitos operativos."),
    ("Por que gana", "Tesis clara, mercado con brecha creciente, comunidad vertical y una metrica que no se puede maquillar: skills verificadas con evidencia real."),
]


# =============================================================================
#  CSS  (raw string — sin f-string para no escapar llaves)
# =============================================================================

CSS = r"""
*,*::before,*::after{box-sizing:border-box}
:root{
  color-scheme:dark;
  --hue:268;
  /* curvas de motion (Emil) */
  --ease-out:cubic-bezier(.23,1,.32,1);
  --ease-in-out:cubic-bezier(.77,0,.175,1);
  /* fallback sRGB (marca AECODE) */
  --bg:#0B0D1A; --bg2:#0E1121; --surface:#141733; --line:rgba(255,255,255,.09);
  --fg:#EEF3F8; --fg-muted:#A6ADCB;
  --indigo:#4A3AC1; --violet:#7C7EDF; --green:#47CF78;
  --accent:#7C7EDF; --accent-2:#4A3AC1;
  /* tipografia fluida */
  --step--1:clamp(.80rem,.77rem + .14vw,.88rem);
  --step-0:clamp(1rem,.96rem + .20vw,1.10rem);
  --step-1:clamp(1.20rem,1.12rem + .38vw,1.45rem);
  --step-2:clamp(1.45rem,1.31rem + .68vw,1.95rem);
  --step-3:clamp(1.80rem,1.55rem + 1.20vw,2.75rem);
  --step-4:clamp(2.30rem,1.85rem + 2.20vw,4.10rem);
  --step-5:clamp(2.90rem,2.10rem + 3.80vw,5.60rem);
  --maxw:1180px; --radius:16px;
}
@supports (color: oklch(0 0 0)){
  :root{
    --bg:oklch(.13 .03 var(--hue)); --bg2:oklch(.15 .035 var(--hue));
    --surface:oklch(.20 .05 var(--hue)); --line:oklch(1 0 0 / .10);
    --fg:oklch(.97 .01 250); --fg-muted:oklch(.74 .03 280);
    --indigo:oklch(.50 .19 285); --violet:oklch(.66 .15 288); --green:oklch(.78 .17 152);
    --accent:oklch(.66 .15 288); --accent-2:oklch(.50 .19 285);
  }
}
html{-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale;text-rendering:optimizeLegibility;-webkit-text-size-adjust:100%;scroll-behavior:smooth}
@media (prefers-reduced-motion:reduce){html{scroll-behavior:auto}}
body{
  margin:0;background:var(--bg);color:var(--fg);
  font-family:"Plus Jakarta Sans",system-ui,sans-serif;font-size:var(--step-0);line-height:1.65;
  overflow-x:hidden;
}
h1,h2,h3,h4{font-family:"Space Grotesk",sans-serif;font-weight:600;line-height:1.05;letter-spacing:-.02em;text-wrap:balance;margin:0}
p{text-wrap:pretty;margin:0}
a{color:inherit;text-decoration:none}
.mono{font-family:"JetBrains Mono",monospace;font-variant-numeric:tabular-nums;font-feature-settings:"tnum" 1}
::selection{background:var(--violet);color:#0B0D1A}
:focus-visible{outline:none;box-shadow:0 0 0 2px var(--bg),0 0 0 4px var(--violet);border-radius:8px}

/* layout */
.wrap{width:min(100% - 2.5rem,var(--maxw));margin-inline:auto}
section{padding:clamp(4rem,9vw,8rem) 0;position:relative}
.kicker{display:inline-flex;align-items:center;gap:.5rem;font:600 var(--step--1)/1 "Space Grotesk";letter-spacing:.10em;text-transform:uppercase;color:var(--violet);margin-bottom:1rem}
.kicker::before{content:"";width:22px;height:1px;background:linear-gradient(90deg,var(--violet),transparent)}
.h-sec{font-size:var(--step-3);max-width:18ch}
.lead{color:var(--fg-muted);font-size:var(--step-1);max-width:60ch;margin-top:1rem}
.grid{display:grid;gap:1.1rem}
@media(min-width:720px){.g2{grid-template-columns:repeat(2,1fr)}.g3{grid-template-columns:repeat(3,1fr)}.g4{grid-template-columns:repeat(4,1fr)}}

/* aurora bg (GPU: transform/opacity only) */
.aurora{position:fixed;inset:-30vh -10vw;z-index:-2;filter:blur(90px);opacity:.55;pointer-events:none}
.aurora i{position:absolute;border-radius:50%;mix-blend-mode:screen;will-change:transform}
.aurora i:nth-child(1){width:46vw;height:46vw;left:-6vw;top:-4vh;background:radial-gradient(circle,var(--indigo),transparent 65%);animation:drift1 26s var(--ease-in-out) infinite alternate}
.aurora i:nth-child(2){width:40vw;height:40vw;right:-8vw;top:6vh;background:radial-gradient(circle,var(--violet),transparent 65%);animation:drift2 32s var(--ease-in-out) infinite alternate}
.aurora i:nth-child(3){width:34vw;height:34vw;left:30vw;bottom:-12vh;background:radial-gradient(circle,var(--green),transparent 70%);opacity:.5;animation:drift3 38s var(--ease-in-out) infinite alternate}
@keyframes drift1{to{transform:translate3d(8vw,6vh,0) scale(1.15)}}
@keyframes drift2{to{transform:translate3d(-7vw,9vh,0) scale(1.1)}}
@keyframes drift3{to{transform:translate3d(6vw,-7vh,0) scale(1.2)}}
.grain{position:fixed;inset:0;z-index:-1;pointer-events:none;opacity:.04;background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='120' height='120'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.85' numOctaves='2'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E")}
@media (prefers-reduced-motion:reduce){.aurora i{animation:none}}

/* scroll progress */
.prog{position:fixed;top:0;left:0;height:2px;width:100%;transform:scaleX(0);transform-origin:left;background:linear-gradient(90deg,var(--indigo),var(--violet),var(--green));z-index:60}

/* nav (glass) */
header.nav{position:sticky;top:0;z-index:50;backdrop-filter:blur(14px) saturate(1.4);-webkit-backdrop-filter:blur(14px) saturate(1.4);background:color-mix(in oklch,var(--bg) 72%,transparent);border-bottom:1px solid var(--line)}
@supports not (backdrop-filter:blur(1px)){header.nav{background:var(--bg2)}}
.nav .wrap{display:flex;align-items:center;gap:1.2rem;height:64px}
.brand{display:flex;align-items:center;gap:.6rem;font:700 1.05rem/1 "Space Grotesk";letter-spacing:-.02em}
.brand img{width:26px;height:26px}
.brand b{background:linear-gradient(90deg,var(--violet),var(--green));-webkit-background-clip:text;background-clip:text;color:transparent}
.navlinks{display:none;gap:.2rem;margin-left:auto}
@media(min-width:1000px){.navlinks{display:flex}}
.navlinks a{padding:.45rem .7rem;border-radius:9px;font-size:.84rem;color:var(--fg-muted);transition:color .15s,background .15s}
.navlinks a:hover{color:var(--fg);background:var(--surface)}
.navlinks a.active{color:var(--fg)}
.navlinks a.active::after{content:"";display:block;height:2px;margin-top:5px;border-radius:2px;background:linear-gradient(90deg,var(--violet),var(--green))}
.nav-actions{display:flex;gap:.5rem;margin-left:auto}
@media(min-width:1000px){.nav-actions{margin-left:0}}
.kbd{display:none;align-items:center;gap:.35rem;padding:.45rem .6rem;border:1px solid var(--line);border-radius:9px;color:var(--fg-muted);font:600 .76rem/1 "JetBrains Mono";background:var(--surface)/* */;cursor:pointer;transition:transform .15s var(--ease-out),color .15s}
.kbd:hover{color:var(--fg)} .kbd:active{transform:scale(.96)}
@media(min-width:680px){.kbd{display:inline-flex}}
.kbd kbd{background:rgba(255,255,255,.08);border-radius:5px;padding:.05rem .3rem}

/* buttons */
.btn{display:inline-flex;align-items:center;gap:.5rem;padding:.8rem 1.25rem;border-radius:11px;font:600 .95rem/1 "Plus Jakarta Sans";cursor:pointer;border:1px solid transparent;transition:transform .15s var(--ease-out),box-shadow .2s,background .2s;user-select:none}
.btn:active{transform:scale(.97)}
.btn.primary{color:#0B0D1A;background:linear-gradient(120deg,var(--violet),var(--indigo) 60%,var(--green));box-shadow:0 8px 30px -10px var(--violet)}
.btn.primary:hover{box-shadow:0 12px 40px -8px var(--violet)}
.btn.ghost{color:var(--fg);background:var(--surface);border-color:var(--line)}
.btn.ghost:hover{border-color:var(--violet)}

/* cards / glass */
.card{position:relative;background:linear-gradient(180deg,color-mix(in oklch,var(--surface) 70%,transparent),color-mix(in oklch,var(--bg2) 80%,transparent));border:1px solid var(--line);border-radius:var(--radius);padding:1.5rem;box-shadow:0 1px 0 0 rgba(255,255,255,.05) inset,0 20px 50px -30px #000;transition:transform .3s var(--ease-out),border-color .3s}
.card:hover{transform:translateY(-3px);border-color:color-mix(in oklch,var(--violet) 40%,var(--line))}
.tag{display:inline-block;font:600 .68rem/1.4 "JetBrains Mono";letter-spacing:.04em;text-transform:uppercase;padding:.2rem .5rem;border-radius:6px;background:rgba(124,126,223,.14);color:var(--violet);border:1px solid rgba(124,126,223,.25)}
.tag.assume{background:rgba(255,255,255,.06);color:var(--fg-muted);border-color:var(--line)}
.tag.green{background:rgba(71,207,120,.14);color:var(--green);border-color:rgba(71,207,120,.3)}
.delta{color:var(--green);font:600 .8rem/1 "JetBrains Mono"}

/* hero */
.hero{padding-top:clamp(3rem,7vw,6rem);text-align:center}
.hero .orb{width:clamp(92px,16vw,150px);height:auto;margin:0 auto 1.5rem;filter:drop-shadow(0 16px 40px rgba(124,126,223,.5));animation:float 6s var(--ease-in-out) infinite alternate}
@keyframes float{to{transform:translateY(-12px)}}
@media (prefers-reduced-motion:reduce){.hero .orb{animation:none}}
.hero h1{font-size:var(--step-5);max-width:16ch;margin:0 auto}
.hero h1 .grad{background:linear-gradient(110deg,var(--violet),var(--green));-webkit-background-clip:text;background-clip:text;color:transparent}
.hero .sub{color:var(--fg-muted);font-size:var(--step-1);max-width:50ch;margin:1.4rem auto 0}
.chips{display:flex;flex-wrap:wrap;gap:.5rem;justify-content:center;margin:1.8rem auto 0;max-width:680px}
.chip{display:inline-flex;align-items:center;gap:.45rem;padding:.5rem .85rem;border:1px solid var(--line);border-radius:999px;background:var(--surface);font-size:.82rem;color:var(--fg-muted)}
.chip b{color:var(--fg)}
.cta{display:flex;flex-wrap:wrap;gap:.7rem;justify-content:center;margin-top:2rem}
.lema{margin-top:2.4rem;font-style:italic;color:var(--fg-muted);font-size:var(--step-1)}
.lema b{color:var(--fg);font-style:normal}

/* stat strip */
.stats{display:grid;gap:1px;background:var(--line);border:1px solid var(--line);border-radius:var(--radius);overflow:hidden;margin-top:3rem}
@media(min-width:720px){.stats{grid-template-columns:repeat(4,1fr)}}
.stat{background:var(--bg2);padding:1.4rem 1.3rem;text-align:left}
.stat .big{font:700 clamp(1.9rem,4vw,2.6rem)/1 "Space Grotesk";font-variant-numeric:tabular-nums;background:linear-gradient(120deg,var(--fg),var(--violet));-webkit-background-clip:text;background-clip:text;color:transparent}
.stat .lab{font-size:.82rem;color:var(--fg-muted);margin-top:.45rem}
.stat .meta{font:600 .72rem/1 "JetBrains Mono";color:var(--green);margin-top:.5rem}

/* north star block */
.ns{display:grid;gap:1.4rem}
@media(min-width:860px){.ns{grid-template-columns:1.1fr .9fr}}
.formula{font:600 var(--step-1)/1.4 "JetBrains Mono";background:var(--bg2);border:1px solid var(--line);border-radius:12px;padding:1.2rem;color:var(--fg)}
.formula .num{color:var(--green)}
.nspair{display:flex;gap:1rem;margin-top:1.2rem;flex-wrap:wrap}
.nsbox{flex:1;min-width:130px}
.nsbox .v{font:700 var(--step-3)/1 "Space Grotesk";font-variant-numeric:tabular-nums}
.nsbox .v.muted{color:var(--fg-muted)} .nsbox .v.hot{color:var(--green)}
.nsbox small{color:var(--fg-muted)}
.yn{margin-top:.9rem;padding-left:1.4rem;position:relative}
.yn.y::before{content:"✓";position:absolute;left:0;color:var(--green);font-weight:700}
.yn.n::before{content:"✕";position:absolute;left:0;color:#ff7a7a;font-weight:700}

/* engines */
.engine{display:flex;flex-direction:column;gap:.9rem}
.engine .top{display:flex;align-items:baseline;justify-content:space-between;gap:1rem}
.engine .mrr{font:700 var(--step-2)/1 "Space Grotesk";font-variant-numeric:tabular-nums}
.engine.indigo .mrr{color:var(--violet)} .engine.violet .mrr{color:var(--violet)} .engine.green .mrr{color:var(--green)}
.engine h3{font-size:var(--step-1)}
.engine .kpis{display:flex;gap:.5rem;flex-wrap:wrap;margin-top:.3rem}
.bar{height:7px;border-radius:5px;background:var(--bg2);overflow:hidden;border:1px solid var(--line)}
.bar i{display:block;height:100%;border-radius:5px;background:linear-gradient(90deg,var(--indigo),var(--violet))}
.barrow{display:grid;grid-template-columns:auto 1fr auto;gap:.6rem;align-items:center;font-size:.8rem;color:var(--fg-muted)}
.barrow .v{color:var(--fg);font-family:"JetBrains Mono"}

/* metric rows */
.metric{display:grid;gap:.5rem}
.metric .hd{display:flex;align-items:center;justify-content:space-between;gap:.8rem}
.metric h3{font-size:var(--step-0)}
.metric .range{font:600 .8rem/1 "JetBrains Mono";color:var(--green)}
.metric .why{color:var(--fg-muted);font-size:.88rem}
.metric .dec{font-size:.82rem;border-top:1px dashed var(--line);padding-top:.6rem;margin-top:.2rem}
.metric .dec b{color:var(--violet)}

/* tree */
.treecol{display:flex;flex-direction:column;gap:.7rem}
.treecol .lab{display:flex;align-items:center;gap:.5rem;font:600 .82rem/1 "Space Grotesk";letter-spacing:.04em;text-transform:uppercase;color:var(--fg-muted)}
.dot{width:8px;height:8px;border-radius:50%}
.dot.growth{background:var(--green)} .dot.indigo{background:var(--indigo)} .dot.violet{background:var(--violet)} .dot.green{background:var(--green)}
.treecol p{font-size:.84rem;color:var(--fg-muted)}
.kv{display:flex;justify-content:space-between;gap:.6rem;font-size:.82rem;padding:.5rem 0;border-top:1px solid var(--line)}
.kv b{font-family:"JetBrains Mono";color:var(--fg);white-space:nowrap}
.kv small{color:var(--fg-muted)}

/* funnel */
.funnel{display:flex;flex-direction:column;gap:.6rem}
.fstep{display:grid;grid-template-columns:1fr auto;align-items:center;gap:1rem;padding:1rem 1.2rem;border:1px solid var(--line);border-radius:12px;background:linear-gradient(90deg,color-mix(in oklch,var(--violet) 14%,var(--bg2)),var(--bg2));transition:transform .2s var(--ease-out)}
.fstep:hover{transform:translateX(4px)}
.fstep .n{font:700 1.05rem/1 "Space Grotesk"}
.fstep .v{font:700 var(--step-1)/1 "JetBrains Mono";color:var(--green)}
.fstep small{display:block;color:var(--fg-muted);font-size:.8rem;margin-top:.3rem}

/* list */
.checklist{list-style:none;padding:0;margin:0;display:grid;gap:.8rem}
.checklist li{display:flex;gap:.8rem;align-items:flex-start;padding:1rem 1.2rem;background:var(--bg2);border:1px solid var(--line);border-radius:12px}
.checklist li::before{content:"";flex:none;width:22px;height:22px;border-radius:7px;margin-top:2px;background:linear-gradient(135deg,var(--violet),var(--indigo));position:relative}
.checklist li span{font-size:.92rem}

/* command menu */
.cmdk-back{position:fixed;inset:0;z-index:90;background:rgba(5,6,15,.6);backdrop-filter:blur(4px);display:none;align-items:flex-start;justify-content:center;padding-top:14vh}
.cmdk-back.open{display:flex}
.cmdk{width:min(92vw,560px);background:color-mix(in oklch,var(--surface) 80%,var(--bg));border:1px solid var(--line);border-radius:16px;overflow:hidden;box-shadow:0 30px 80px -20px #000;animation:pop .18s var(--ease-out)}
@keyframes pop{from{opacity:0;transform:scale(.97) translateY(6px)}}
.cmdk input{width:100%;border:0;background:transparent;color:var(--fg);font:500 1.05rem/1 "Plus Jakarta Sans";padding:1.1rem 1.3rem;border-bottom:1px solid var(--line);outline:none}
.cmdk ul{list-style:none;margin:0;padding:.5rem;max-height:46vh;overflow:auto}
.cmdk li{padding:.7rem .9rem;border-radius:10px;font-size:.92rem;color:var(--fg-muted);cursor:pointer;display:flex;justify-content:space-between;gap:1rem}
.cmdk li[aria-selected="true"]{background:rgba(124,126,223,.18);color:var(--fg)}
.cmdk li small{font-family:"JetBrains Mono";opacity:.6}

/* AECODITO assistant */
.fab{position:fixed;right:1.2rem;bottom:1.2rem;z-index:80;display:flex;align-items:center;gap:.6rem;padding:.6rem .7rem .6rem .6rem;border-radius:999px;border:1px solid var(--line);background:color-mix(in oklch,var(--surface) 80%,var(--bg));backdrop-filter:blur(10px);cursor:pointer;box-shadow:0 14px 40px -14px #000;transition:transform .15s var(--ease-out)}
.fab:active{transform:scale(.96)} .fab:hover{border-color:var(--violet)}
.fab img{width:34px;height:34px}
.fab span{font:600 .85rem/1 "Plus Jakarta Sans";padding-right:.4rem}
@media(max-width:620px){.fab span{display:none}}
.panel{position:fixed;right:1.2rem;bottom:5.2rem;z-index:80;width:min(92vw,360px);max-height:70vh;overflow:auto;background:color-mix(in oklch,var(--surface) 85%,var(--bg));border:1px solid var(--line);border-radius:18px;box-shadow:0 30px 80px -24px #000;padding:1.1rem;display:none;animation:pop .2s var(--ease-out)}
.panel.open{display:block}
.panel h4{font-size:1rem;margin-bottom:.2rem}
.panel .q{font:600 .85rem/1.3 "Space Grotesk";color:var(--violet);margin-top:.9rem}
.panel .a{font-size:.86rem;color:var(--fg-muted);margin-top:.2rem}

/* footer */
footer{border-top:1px solid var(--line);padding:3rem 0;color:var(--fg-muted);font-size:.86rem}
footer .wrap{display:flex;flex-wrap:wrap;gap:1.5rem;justify-content:space-between;align-items:center}
.safe{display:inline-flex;align-items:center;gap:.5rem;padding:.4rem .8rem;border-radius:999px;border:1px solid rgba(71,207,120,.3);background:rgba(71,207,120,.1);color:var(--green);font:600 .76rem/1 "JetBrains Mono"}

/* reveal (motion: transform/opacity only) */
.reveal{opacity:0;transform:translateY(18px);transition:opacity .7s var(--ease-out),transform .7s var(--ease-out)}
.reveal.in{opacity:1;transform:none}
@media (prefers-reduced-motion:reduce){.reveal{opacity:1;transform:none;transition:none}}
"""


# =============================================================================
#  JS
# =============================================================================

JS = r"""
// scroll progress
const prog=document.querySelector('.prog');
let ticking=false;
function onScroll(){
  if(ticking)return;ticking=true;
  requestAnimationFrame(()=>{
    const h=document.documentElement;
    const p=h.scrollTop/(h.scrollHeight-h.clientHeight||1);
    prog.style.transform='scaleX('+p+')';ticking=false;
  });
}
addEventListener('scroll',onScroll,{passive:true});onScroll();

// reveal on scroll (one-shot, stagger via index)
const io=new IntersectionObserver((es)=>{
  es.forEach(e=>{ if(e.isIntersecting){ const el=e.target;
    const d=[...el.parentElement.querySelectorAll(':scope > .reveal')].indexOf(el);
    el.style.transitionDelay=Math.max(0,Math.min(d,8))*55+'ms';
    el.classList.add('in');io.unobserve(el);}});
},{rootMargin:'0px 0px -8% 0px',threshold:.12});
document.querySelectorAll('.reveal').forEach(el=>io.observe(el));

// nav active link
const links=[...document.querySelectorAll('.navlinks a')];
const map=new Map(links.map(a=>[a.getAttribute('href').slice(1),a]));
const navio=new IntersectionObserver((es)=>{
  es.forEach(e=>{ if(e.isIntersecting){ links.forEach(l=>l.classList.remove('active'));
    const a=map.get(e.target.id); if(a)a.classList.add('active');}});
},{rootMargin:'-45% 0px -50% 0px'});
document.querySelectorAll('section[id]').forEach(s=>navio.observe(s));

// count-up
const reduce=matchMedia('(prefers-reduced-motion:reduce)').matches;
function countUp(el){
  const t=parseFloat(el.dataset.count),dec=+el.dataset.dec||0,pre=el.dataset.pre||'',suf=el.dataset.suf||'',sep=el.dataset.sep==='1';
  if(reduce){el.textContent=fmt(t,dec,pre,suf,sep);return;}
  const dur=1100,st=performance.now();
  function step(now){const k=Math.min(1,(now-st)/dur);const e=1-Math.pow(1-k,3);
    el.textContent=fmt(t*e,dec,pre,suf,sep);if(k<1)requestAnimationFrame(step);}
  requestAnimationFrame(step);
}
function fmt(v,dec,pre,suf,sep){let n=v.toFixed(dec);if(sep)n=(+n).toLocaleString('en-US',{minimumFractionDigits:dec,maximumFractionDigits:dec});return pre+n+suf;}
const cio=new IntersectionObserver((es)=>{es.forEach(e=>{if(e.isIntersecting){countUp(e.target);cio.unobserve(e.target);}})},{threshold:.6});
document.querySelectorAll('[data-count]').forEach(el=>cio.observe(el));

// command menu
const back=document.querySelector('.cmdk-back'),input=document.querySelector('.cmdk input'),list=document.querySelector('.cmdk ul');
const items=[...list.querySelectorAll('li')];let sel=0;
function openCmd(){back.classList.add('open');input.value='';filter('');input.focus();}
function closeCmd(){back.classList.remove('open');}
function filter(q){q=q.toLowerCase();let first=-1;items.forEach((li,i)=>{const m=li.dataset.k.includes(q);li.style.display=m?'':'none';if(m&&first<0)first=i;});sel=first;paint();}
function paint(){items.forEach((li,i)=>li.setAttribute('aria-selected',i===sel));}
function visible(){return items.filter(li=>li.style.display!=='none');}
input.addEventListener('input',e=>filter(e.target.value));
addEventListener('keydown',e=>{
  if((e.metaKey||e.ctrlKey)&&e.key.toLowerCase()==='k'){e.preventDefault();back.classList.contains('open')?closeCmd():openCmd();}
  if(!back.classList.contains('open'))return;
  if(e.key==='Escape')closeCmd();
  if(e.key==='ArrowDown'||e.key==='ArrowUp'){e.preventDefault();const v=visible();let idx=v.indexOf(items[sel]);idx+= e.key==='ArrowDown'?1:-1;idx=(idx+v.length)%v.length;sel=items.indexOf(v[idx]);paint();v[idx].scrollIntoView({block:'nearest'});}
  if(e.key==='Enter'){const li=items[sel];if(li){go(li.dataset.go);}}
});
list.addEventListener('click',e=>{const li=e.target.closest('li');if(li)go(li.dataset.go);});
function go(id){closeCmd();const el=document.getElementById(id);if(el)el.scrollIntoView({behavior:reduce?'auto':'smooth',block:'start'});}
document.querySelectorAll('[data-cmd]').forEach(b=>b.addEventListener('click',openCmd));
back.addEventListener('click',e=>{if(e.target===back)closeCmd();});

// AECODITO panel
const fab=document.querySelector('.fab'),panel=document.querySelector('.panel');
fab.addEventListener('click',()=>panel.classList.toggle('open'));
document.addEventListener('click',e=>{if(panel.classList.contains('open')&&!panel.contains(e.target)&&!fab.contains(e.target))panel.classList.remove('open');});

document.getElementById('yr').textContent=new Date().getFullYear();
"""


# =============================================================================
#  HTML BUILDERS
# =============================================================================

def esc(s):
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


def stat_html(s):
    big, lab, meta, num, pre, suf, dec, sep = s
    return f"""<div class="stat reveal">
      <div class="big mono" data-count="{num}" data-dec="{dec}" data-pre="{pre}" data-suf="{suf}" data-sep="{1 if sep else 0}">{esc(pre)}0{esc(suf)}</div>
      <div class="lab">{esc(lab)}</div><div class="meta">{esc(meta)}</div></div>"""


def engine_html(e):
    kpis = "".join(f'<div class="kv"><small>{esc(k)}</small><b>{esc(v)} <span class="tag {"assume" if t in ("supuesto","pipeline") else "green"}">{esc(t)}</span></b></div>' for k, v, t in e["kpis"])
    return f"""<article class="card engine {e['accent']} reveal">
      <div class="top"><h3>{esc(e['name'])}</h3><div class="mrr mono">{esc(e['mrr'])}<span style="font-size:.5em;color:var(--fg-muted)"> /mes</span></div></div>
      <span class="tag">{esc(e['tag'])}</span>
      <p style="color:var(--fg-muted);font-size:.9rem">{esc(e['desc'])}</p>
      <div style="margin-top:.3rem">{kpis}</div>
      <div class="barrow"><span>mix actual</span><div class="bar"><i style="width:{e['share_now']}%"></i></div><span class="v">{e['share_now']}%</span></div>
      <div class="barrow"><span>mix objetivo</span><div class="bar"><i style="width:{e['share_goal']}%;background:linear-gradient(90deg,var(--green),var(--violet))"></i></div><span class="v">{e['share_goal']}%</span></div>
    </article>"""


def metric_html(m):
    name, cat, why, rng, dec, nsm = m
    star = ' <span class="tag green">NSM</span>' if nsm else ""
    return f"""<article class="card metric reveal">
      <div class="hd"><h3>{esc(name)}{star}</h3><span class="tag assume">{esc(cat)}</span></div>
      <p class="why">{esc(why)}</p>
      <div class="range">Rango sano: {esc(rng)}</div>
      <div class="dec"><b>Decision &rsaquo;</b> {esc(dec)}</div></article>"""


def tree_html(t):
    name, color, desc, rows = t
    kv = "".join(f'<div class="kv"><small>{esc(k)}</small><b>{esc(v)}</b></div>' for k, v, note in rows)
    return f"""<article class="card treecol reveal">
      <div class="lab"><span class="dot {color}"></span>{esc(name)}</div>
      <p>{esc(desc)}</p>{kv}</article>"""


def funnel_html(f):
    n, v, note, sub = f
    return f"""<div class="fstep reveal"><div><div class="n">{esc(n)}</div><small>{esc(sub)}</small></div>
      <div style="text-align:right"><div class="v mono">{esc(v)}</div><small>{esc(note)}</small></div></div>"""


def econ_html(e):
    name, now, target, why = e
    return f"""<article class="card reveal"><div class="hd" style="display:flex;justify-content:space-between;align-items:baseline">
      <h3 style="font-size:var(--step-0)">{esc(name)}</h3><span class="delta mono">{esc(target)}</span></div>
      <p style="color:var(--fg-muted);font-size:.86rem;margin-top:.5rem">{esc(why)}</p></article>"""


# nav
navlinks = "".join(f'<a href="#{i}">{esc(t)}</a>' for i, t in NAV)
cmd_items = "".join(
    f'<li role="option" data-k="{esc(t.lower())} {i}" data-go="{i}">{esc(t)}<small>↵</small></li>'
    for i, t in NAV
)

principios = "".join(
    f'<article class="card reveal"><span class="tag">{n:02d}</span><h3 style="font-size:var(--step-0);margin-top:.7rem">{esc(p[0])}</h3><p style="color:var(--fg-muted);font-size:.88rem;margin-top:.4rem">{esc(p[1])}</p></article>'
    for n, p in enumerate(PRINCIPIOS, 1)
)
engines = "".join(engine_html(e) for e in ENGINES)
metrics = "".join(metric_html(m) for m in METRICS)
tree = "".join(tree_html(t) for t in TREE)
funnel = "".join(funnel_html(f) for f in FUNNEL)
economics = "".join(econ_html(e) for e in ECONOMICS)
acciones = "".join(f'<li class="reveal"><span>{esc(a)}</span></li>' for a in ACCIONES)
stats = "".join(stat_html(s) for s in HERO_STATS)
facts = "".join(f'<div class="q">{esc(q)}</div><div class="a">{esc(a)}</div>' for q, a in FACTS)


# =============================================================================
#  PAGE
# =============================================================================

DESC = "Reporte de inteligencia AECODE: el Learning Operating System para la fuerza laboral AEC en espanol. Modelo hibrido, North Star, metricas y unit economics — public-safe."

PAGE = f"""<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>AECODE — Startup Intelligence Report</title>
<meta name="description" content="{esc(DESC)}">
<meta name="theme-color" content="#0B0D1A">
<link rel="icon" href="aecode-logo.svg" type="image/svg+xml">
<meta property="og:type" content="website">
<meta property="og:title" content="AECODE — Startup Intelligence Report">
<meta property="og:description" content="{esc(DESC)}">
<meta property="og:image" content="aecodito.png">
<meta name="twitter:card" content="summary_large_image">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&family=Plus+Jakarta+Sans:wght@400;500;600;700&family=JetBrains+Mono:wght@500;600&display=swap" rel="stylesheet">
<style>{CSS}</style>
</head>
<body>
<div class="prog"></div>
<div class="aurora" aria-hidden="true"><i></i><i></i><i></i></div>
<div class="grain" aria-hidden="true"></div>

<header class="nav">
  <div class="wrap">
    <a class="brand" href="#top"><img src="aecode-logo.svg" alt="AECODE"><span>AECODE<b>.</b></span></a>
    <nav class="navlinks" aria-label="Secciones">{navlinks}</nav>
    <div class="nav-actions">
      <button class="kbd" data-cmd aria-label="Abrir buscador de comandos"><kbd>⌘</kbd><kbd>K</kbd> buscar</button>
      <a class="btn primary" href="#acciones">Data room</a>
    </div>
  </div>
</header>

<main id="top">

<!-- HERO -->
<section class="hero" aria-label="Portada">
  <div class="wrap">
    <img class="orb reveal" src="aecodito.png" alt="AECODITO, mascota IA de AECODE" width="150" height="150">
    <div class="kicker reveal" style="justify-content:center">Learning Operating System · Sector AEC</div>
    <h1 class="reveal">El sistema que convierte aprendizaje AEC en <span class="grad">skills verificadas</span>.</h1>
    <p class="sub reveal">Plataforma de aprendizaje AEC inteligente, practica y certificable. Cada curso se vuelve ruta, practica, evidencia, feedback y certificacion — progreso profesional medible, no horas de clase.</p>
    <div class="chips reveal">
      <span class="chip"><b>Modelo</b> Live Training + Microlearning</span>
      <span class="chip"><b>Wedge</b> Profesionales AEC digitales</span>
      <span class="chip"><b>NSM</b> Skills verificadas / MAU</span>
    </div>
    <div class="cta reveal">
      <a class="btn primary" href="#producto">Ver el producto</a>
      <a class="btn ghost" href="#metricas">Explorar metricas</a>
    </div>
    <div class="stats">{stats}</div>
    <p class="lema reveal">La Ingenieria &amp; Construccion Moderna, <b>te la contamos nosotros.</b></p>
  </div>
</section>

<!-- NORTH STAR -->
<section id="norte" aria-label="North Star">
  <div class="wrap">
    <div class="kicker reveal">North Star Metric</div>
    <h2 class="h-sec reveal">Una metrica que no se puede maquillar.</h2>
    <div class="ns" style="margin-top:2rem">
      <div class="reveal">
        <div class="formula">skills_verified_with_evidence <span style="color:var(--violet)">/</span> monthly_active_users</div>
        <div class="nspair">
          <div class="nsbox"><div class="v muted mono">0.17</div><small>Actual · 72 / 420</small></div>
          <div class="nsbox"><div class="v hot mono">0.40</div><small>Meta beta · 300 / 750</small></div>
          <div class="nsbox"><div class="v mono">&gt;0.8</div><small>En escala</small></div>
        </div>
      </div>
      <div class="card reveal">
        <p class="yn y"><b>Cuenta cuando:</b> el usuario inicia una skill, completa una practica, sube un entregable, recibe validacion y la skill queda en su Skill Passport.</p>
        <p class="yn n"><b>No cuenta:</b> solo ver una clase, asistir a un live, descargar material o recibir un certificado sin evidencia.</p>
      </div>
    </div>
  </div>
</section>

<!-- PROBLEMA / SOLUCION -->
<section id="problema" aria-label="Problema y solucion">
  <div class="wrap">
    <div class="kicker reveal">Problema · Solucion</div>
    <h2 class="h-sec reveal">El problema no es que falten cursos. Es que no se vuelven progreso verificable.</h2>
    <div class="grid g2" style="margin-top:2rem">
      <article class="card reveal"><span class="tag assume">Dolor transversal</span>
        <h3 style="font-size:var(--step-1);margin-top:.8rem">Aprendizaje sin evidencia</h3>
        <p style="color:var(--fg-muted);margin-top:.6rem">La pregunta no es si faltan cursos; es quien ordena, valida y mide talento AEC. El aprendizaje no siempre se convierte en progreso verificable.</p></article>
      <article class="card reveal"><span class="tag green">Loop central</span>
        <h3 style="font-size:var(--step-1);margin-top:.8rem">Aprende → practica → evidencia → valida → acumula</h3>
        <p style="color:var(--fg-muted);margin-top:.6rem">Idea madre: cada curso se convierte en ruta, practica, evidencia, feedback y certificacion. Unidad de valor: <b style="color:var(--fg)">skill verificada con evidencia</b>, no hora de clase.</p></article>
    </div>
  </div>
</section>

<!-- PRODUCTO -->
<section id="producto" aria-label="Producto">
  <div class="wrap">
    <div class="kicker reveal">Producto</div>
    <h2 class="h-sec reveal">AECODE diagnostica, recomienda, divide en capsulas, valida evidencias y acumula skills.</h2>
    <p class="lead reveal">El progreso conecta lo nuevo con lo que el usuario ya sabe y recomienda el siguiente skill. IA como recomendador, coach y apoyo de evaluacion.</p>
    <div class="grid g3" style="margin-top:2.2rem">{principios}</div>
  </div>
</section>

<!-- MODELO -->
<section id="modelo" aria-label="Modelo de negocio">
  <div class="wrap">
    <div class="kicker reveal">Modelo hibrido</div>
    <h2 class="h-sec reveal">Cuatro motores. Caja hoy, recurrencia manana.</h2>
    <p class="lead reveal">Actual: 60% Live Training y 25% Microlearning. Objetivo: migrar a 60% Microlearning Skill OS y 25% Live Training — de horas sincronas a activos digitales reutilizables.</p>
    <div class="grid g2" style="margin-top:2.2rem">{engines}</div>
    <div class="card reveal" style="margin-top:1.4rem">
      <h3 style="font-size:var(--step-1)">Logica de migracion</h3>
      <div class="grid g2" style="margin-top:1rem">
        <p style="color:var(--fg-muted);font-size:.9rem">Cada curso live se vuelve capsulas, practicas, rubricas y evidencias reutilizables. Cada usuario live recibe una ruta Microlearning y creditos iniciales para validar su primera skill.</p>
        <p style="color:var(--fg-muted);font-size:.9rem">Cada evidencia validada alimenta el Skill Passport y genera datos para recomendaciones de IA. El objetivo: migrar de 60% Live a 60% Microlearning Skill OS.</p>
      </div>
    </div>
  </div>
</section>

<!-- MERCADO -->
<section id="mercado" aria-label="Mercado y ventaja">
  <div class="wrap">
    <div class="kicker reveal">Mercado · ICP · Moat</div>
    <h2 class="h-sec reveal">AEC LatAm primero, con un moat que no es el contenido.</h2>
    <div class="grid g3" style="margin-top:2rem">
      <article class="card reveal"><span class="tag">ICP</span><h3 style="font-size:var(--step-0);margin-top:.7rem">A quien servimos</h3><p style="color:var(--fg-muted);font-size:.88rem;margin-top:.5rem">B2C: profesionales AEC que buscan empleabilidad digital. B2B: empresas con brechas BIM, IA, VDC, datos o productividad que necesitan upskilling medible.</p></article>
      <article class="card reveal"><span class="tag green">Moat</span><h3 style="font-size:var(--step-0);margin-top:.7rem">Ventaja competitiva</h3><p style="color:var(--fg-muted);font-size:.88rem;margin-top:.5rem">El moat es la red entre skill, evidencia, rol, feedback y demanda de mercado — no el contenido aislado. Verticalidad y data moat.</p></article>
      <article class="card reveal"><span class="tag assume">vs. mercado</span><h3 style="font-size:var(--step-0);margin-top:.7rem">Diferenciacion</h3><p style="color:var(--fg-muted);font-size:.88rem;margin-top:.5rem">Udemy organiza cursos. YouTube distribuye tutoriales. AECODE convierte aprendizaje AEC en skills verificables y datos de talento.</p></article>
    </div>
  </div>
</section>

<!-- METRICAS -->
<section id="metricas" aria-label="Metricas">
  <div class="wrap">
    <div class="kicker reveal">Como medimos el progreso</div>
    <h2 class="h-sec reveal">Metricas en orden de prioridad, en lenguaje ejecutivo.</h2>
    <p class="lead reveal">La prioridad no es medir todo. Es medir si el usuario aprende, practica, sube evidencia, certifica una skill, vuelve y paga por seguir avanzando.</p>
    <div class="grid g2" style="margin-top:2.2rem">{metrics}</div>

    <h3 class="reveal" style="font-size:var(--step-2);margin:3.5rem 0 1.4rem">Arbol de metricas — del norte a producto, growth y revenue</h3>
    <div class="grid g3">{tree}</div>

    <h3 class="reveal" style="font-size:var(--step-2);margin:3.5rem 0 1.4rem">Funnel maestro — de visita a skill verificada y pago</h3>
    <div class="funnel">{funnel}</div>
  </div>
</section>

<!-- ECONOMICS -->
<section id="economics" aria-label="Unit economics">
  <div class="wrap">
    <div class="kicker reveal">Unit economics</div>
    <h2 class="h-sec reveal">Si cada cliente deja mas valor del que cuesta adquirirlo.</h2>
    <p class="lead reveal">CAC, LTV, margen, payback, burn y runway explican si el crecimiento es financiable. Si CAC o burn suben sin retencion, el crecimiento destruye caja.</p>
    <div class="grid g4" style="margin-top:2.2rem">{economics}</div>
  </div>
</section>

<!-- GTM / EQUIPO -->
<section id="gtm" aria-label="Go-to-market y escalabilidad">
  <div class="wrap">
    <div class="kicker reveal">Go-To-Market · Escalabilidad</div>
    <h2 class="h-sec reveal">De comunidad a plataforma; de horas a activos reutilizables.</h2>
    <div class="grid g2" style="margin-top:2rem">
      <article class="card reveal"><span class="tag">GTM</span><p style="color:var(--fg-muted);margin-top:.8rem">Entrar por contenido, webinars, diagnostico gratuito, ruta recomendada, skill express, evidencia, certificado y upsell a creditos, cohortes o plan empresa. <b style="color:var(--fg)">La activacion no es registro; es el primer skill start con evidencia.</b></p></article>
      <article class="card reveal"><span class="tag green">Escala</span><p style="color:var(--fg-muted);margin-top:.8rem">Escala si sube el margen digital y baja la dependencia de horas sincronas. Cada live se convierte en capsulas, skills y creditos — ingresos escalables &gt;30–50% en MVP.</p></article>
    </div>
  </div>
</section>

<section id="equipo" aria-label="Equipo y red">
  <div class="wrap">
    <div class="kicker reveal">Equipo · Red</div>
    <h2 class="h-sec reveal">El jurado compra velocidad de aprendizaje del equipo, no solo la idea.</h2>
    <div class="grid g2" style="margin-top:2rem">
      <article class="card reveal"><span class="tag">Founder-market fit</span><p style="color:var(--fg-muted);margin-top:.8rem">El equipo comunica dominio AEC, criterio de producto, capacidad de comunidad, operacion educativa, IA aplicada, alianzas y ejecucion tecnica.</p></article>
      <article class="card reveal"><span class="tag green">Ecosistema</span><p style="color:var(--fg-muted);margin-top:.8rem">Instructores, empresas, universidades, gremios, comunidades, eventos, sponsors y aliados tecnologicos amplian distribucion, confianza y profundidad. El partner ideal aporta audiencia, casos reales, certificacion, datos o demanda B2B.</p></article>
    </div>
  </div>
</section>

<!-- ACCIONES -->
<section id="acciones" aria-label="Roadmap de acciones">
  <div class="wrap">
    <div class="kicker reveal">Roadmap accionable</div>
    <h2 class="h-sec reveal">Lo que mueve la aguja antes de levantar.</h2>
    <ul class="checklist" style="margin-top:2.2rem">{acciones}</ul>
    <div class="card reveal" style="margin-top:2.5rem;text-align:center;background:linear-gradient(120deg,color-mix(in oklch,var(--indigo) 22%,var(--bg2)),var(--bg2))">
      <h3 style="font-size:var(--step-2)">AECODE: aprender, practicar, evidenciar, certificar y crecer.</h3>
      <p style="color:var(--fg-muted);max-width:48ch;margin:.8rem auto 1.4rem">Talento AEC verificable, en espanol. Solicita el data room con metricas reales, supuestos separados y benchmarks citados.</p>
      <div class="cta"><a class="btn primary" href="mailto:apalpan@genplusdesign.com?subject=AECODE%20Data%20Room">Solicitar data room</a><button class="btn ghost" data-cmd>Buscar seccion ⌘K</button></div>
    </div>
  </div>
</section>

</main>

<footer>
  <div class="wrap">
    <div style="display:flex;align-items:center;gap:.6rem"><img src="aecode-logo.svg" width="22" height="22" alt=""><span>AECODE © <span id="yr">2026</span> · Learning Operating System AEC</span></div>
    <span class="safe">● Reporte public-safe · datos mock, rangos y supuestos separados de metricas reales</span>
  </div>
</footer>

<!-- command menu -->
<div class="cmdk-back" role="dialog" aria-modal="true" aria-label="Buscar seccion">
  <div class="cmdk">
    <input type="text" placeholder="Buscar seccion… (North Star, Modelo, Metricas)" aria-label="Buscar">
    <ul role="listbox">{cmd_items}</ul>
  </div>
</div>

<!-- AECODITO assistant -->
<button class="fab" aria-label="Abrir AECODITO" aria-expanded="false"><img src="aecodito.png" alt=""><span>AECODITO</span></button>
<aside class="panel" aria-label="Resumen AECODITO">
  <h4>Resumen en 30 segundos</h4>
  <p class="a">Lo esencial del reporte AECODE para jurado e inversionista.</p>
  {facts}
</aside>

<script>{JS}</script>
</body>
</html>"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(PAGE)

print("index.html generado:", len(PAGE), "bytes")
