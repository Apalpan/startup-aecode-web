# -*- coding: utf-8 -*-
# Generador del AECODE Startup Intelligence Cockpit (single-file HTML)
P = []
def add(s): P.append(s)

# ============================ HEAD + STYLE OPEN ============================
add(r'''<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>AECODE · Startup Intelligence Cockpit</title>
<meta name="description" content="Cockpit interactivo de inteligencia de negocio para AECODE: North Star, simulador de escenarios, funnel, mix de ingresos, fundabilidad y agenda de readiness. Edita, simula e interpreta tu startup en tiempo real."/>
<meta property="og:title" content="AECODE · Startup Intelligence Cockpit"/>
<meta property="og:description" content="Simula escenarios, edita métricas y entiende qué mover para que AECODE sea financiable."/>
<meta property="og:image" content="aecodito.png"/>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Space+Grotesk:wght@500;600;700&family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet">
<style>
''')

# ============================ CSS ============================
add(r''':root{
  --bg:#0E1121;--bg2:#0D0F1F;--nav:#0C0F29;--card:#222341;--border:#3A4065;
  --txt:#EEF3F8;--muted:#A2B4CB;--lavender:#C5CFFA;
  --indigo:#4A3AC1;--violet:#7C7EDF;--violet2:#8F60EA;
  --blue:#4465EE;--green:#47CF78;--mint:#95E3B1;
  --good:#47CF78;--watch:#F0A030;--risk:#F2617A;
  --good-bg:rgba(71,207,120,.1);--watch-bg:rgba(240,160,48,.1);--risk-bg:rgba(242,97,122,.1);
  --sp:clamp(56px,7vw,92px);
}
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth}
body{font-family:'Plus Jakarta Sans',system-ui,sans-serif;font-size:14px;line-height:1.6;
  color:var(--txt);background:var(--bg);-webkit-font-smoothing:antialiased;overflow-x:hidden}
#bg-canvas{position:fixed;inset:0;z-index:0;pointer-events:none}
.grain{position:fixed;inset:0;z-index:2;pointer-events:none;opacity:.022;
  background-image:url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.65' numOctaves='3' stitchTiles='stitch'/%3E%3CfeColorMatrix type='saturate' values='0'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E");
  background-size:128px 128px}
body::before{content:'';position:fixed;inset:0;z-index:0;pointer-events:none;
  background:radial-gradient(ellipse 900px 520px at 88% -6%,rgba(74,58,193,.24) 0%,transparent 60%),
    radial-gradient(ellipse 620px 380px at 4% 6%,rgba(124,126,223,.09) 0%,transparent 55%),
    radial-gradient(ellipse 520px 300px at 50% 102%,rgba(68,101,238,.07) 0%,transparent 50%)}
#scroll-bar{position:fixed;top:0;left:0;height:2px;z-index:300;width:0;
  background:linear-gradient(90deg,#4A3AC1,#7C7EDF,#47CF78);transition:width .08s linear}
@keyframes gradShift{0%{background-position:0 50%}50%{background-position:100% 50%}100%{background-position:0 50%}}
@keyframes floatY{0%,100%{transform:translateY(0)}50%{transform:translateY(-6px)}}
@keyframes pRing{0%{opacity:.45;transform:scale(1)}100%{opacity:0;transform:scale(1.78)}}
@keyframes shimmer{0%{left:-70%}100%{left:130%}}
@keyframes spin{from{transform:rotate(0)}to{transform:rotate(360deg)}}
@keyframes spinRev{from{transform:rotate(0)}to{transform:rotate(-360deg)}}
@keyframes glowPulse{0%,100%{box-shadow:0 0 0 0 rgba(124,126,223,0)}50%{box-shadow:0 0 22px -2px rgba(124,126,223,.5)}}
@media(prefers-reduced-motion:reduce){*,*::before,*::after{animation-duration:.01ms!important;transition-duration:.01ms!important}}
.grad{background:linear-gradient(90deg,#4A3AC1,#7C7EDF,#8F60EA,#7C7EDF,#4A3AC1);background-size:250% auto;
  -webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;animation:gradShift 5s ease infinite}
.wrap{max-width:1280px;margin:0 auto;padding:0 22px}
.section{padding:var(--sp) 0;position:relative;z-index:5;scroll-margin-top:120px}
.eyebrow{display:inline-flex;align-items:center;gap:9px;font-family:'Space Grotesk',sans-serif;
  font-size:10.5px;font-weight:700;letter-spacing:.28em;text-transform:uppercase;color:var(--violet);margin-bottom:16px}
.eyebrow::before{content:'';width:20px;height:2px;border-radius:2px;background:linear-gradient(90deg,var(--indigo),var(--violet))}
.section-h{font-family:'Space Grotesk',sans-serif;font-size:clamp(24px,3.4vw,38px);font-weight:700;line-height:1.12;letter-spacing:-.02em;margin-bottom:12px}
.section-p{font-size:clamp(13px,1.6vw,16px);color:var(--muted);line-height:1.66;max-width:680px}
.card{background:rgba(34,35,65,.6);backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px);
  border:1px solid var(--border);border-radius:18px;position:relative;overflow:hidden;padding:22px}
.card::before{content:'';position:absolute;inset:0 0 auto 0;height:1px;background:linear-gradient(90deg,transparent,rgba(124,126,223,.26),transparent)}
.card-eyebrow{display:flex;align-items:center;gap:8px;font-family:'Space Grotesk',sans-serif;font-weight:600;
  font-size:9.5px;letter-spacing:.26em;text-transform:uppercase;color:var(--muted);margin-bottom:14px}
.card-eyebrow .tick{width:16px;height:2px;border-radius:2px;background:linear-gradient(90deg,#4A3AC1,#7C7EDF)}
''')

add(r'''/* COMMAND BAR */
#bar{position:fixed;top:0;left:0;right:0;z-index:100;transition:background .35s,box-shadow .35s,border-color .35s;border-bottom:1px solid transparent}
#bar.scrolled{background:rgba(12,15,41,.93);backdrop-filter:blur(22px);-webkit-backdrop-filter:blur(22px);border-bottom:1px solid var(--border);box-shadow:0 4px 40px rgba(0,0,0,.35)}
.bar-in{display:flex;align-items:center;gap:12px;max-width:1280px;margin:0 auto;padding:11px 22px}
.bar-logo{display:flex;align-items:center;gap:10px;text-decoration:none;flex:0 0 auto}
.aecodito{width:38px;height:38px;border-radius:50%;object-fit:cover;border:2px solid var(--violet);animation:floatY 3s ease-in-out infinite}
.bar-name{font-family:'Space Grotesk',sans-serif;font-weight:700;font-size:17px;letter-spacing:.05em;line-height:1}
.bar-sub{font-size:8.5px;letter-spacing:.3em;text-transform:uppercase;color:var(--muted);font-weight:600;margin-top:2px}
.verdict{display:flex;align-items:center;gap:8px;padding:6px 13px;border-radius:999px;border:1px solid var(--border);background:rgba(34,35,65,.72);cursor:pointer}
.verdict .vd{width:8px;height:8px;border-radius:50%;animation:blink 2s infinite}
@keyframes blink{0%,100%{opacity:1}50%{opacity:.35}}
.verdict b{font-family:'Space Grotesk',sans-serif;font-weight:700;font-size:11px;letter-spacing:.05em;text-transform:uppercase;white-space:nowrap}
.verdict span{font-size:10px;color:var(--muted);font-family:'JetBrains Mono',monospace}
.pills{display:flex;gap:3px;margin-left:auto;overflow-x:auto;scrollbar-width:none}
.pills::-webkit-scrollbar{display:none}
.pill{font-family:'Space Grotesk',sans-serif;font-weight:600;font-size:11.5px;color:var(--muted);text-decoration:none;padding:7px 12px;border-radius:9px;transition:.2s;white-space:nowrap;cursor:pointer;border:none;background:transparent}
.pill:hover{color:var(--txt);background:rgba(124,126,223,.1)}
.pill.active{color:#fff;background:linear-gradient(135deg,rgba(74,58,193,.5),rgba(124,126,223,.4))}
.tools{display:flex;gap:5px;flex:0 0 auto}
.tbtn{font-family:'Space Grotesk',sans-serif;font-weight:600;font-size:10.5px;letter-spacing:.04em;color:var(--muted);background:rgba(34,35,65,.6);border:1px solid var(--border);padding:7px 11px;border-radius:999px;cursor:pointer;transition:.2s;white-space:nowrap;display:inline-flex;align-items:center;gap:5px}
.tbtn:hover{color:#fff;background:linear-gradient(135deg,#4A3AC1,#7C7EDF);border-color:transparent}
.tbtn.primary{color:#fff;background:linear-gradient(135deg,#4A3AC1,#7C7EDF);border-color:transparent}
''')

add(r'''/* HERO / NORTH STAR */
#north{padding-top:128px}
.north-grid{display:grid;grid-template-columns:1.15fr .85fr;gap:22px;align-items:stretch}
.north-lead .hbadge{display:inline-flex;align-items:center;gap:9px;background:rgba(74,58,193,.16);border:1px solid rgba(124,126,223,.28);border-radius:999px;padding:6px 15px;font-family:'Space Grotesk',sans-serif;font-size:10px;font-weight:700;letter-spacing:.22em;text-transform:uppercase;color:var(--lavender);margin-bottom:18px}
.pulse-dot{width:7px;height:7px;border-radius:50%;background:var(--green);position:relative}
.pulse-dot::after{content:'';position:absolute;inset:-3px;border-radius:50%;background:var(--green);opacity:.3;animation:pRing 1.8s ease-out infinite}
.north-h1{font-family:'Space Grotesk',sans-serif;font-size:clamp(28px,4.4vw,52px);font-weight:700;line-height:1.05;letter-spacing:-.03em;margin-bottom:16px}
.north-p{font-size:clamp(14px,1.7vw,17px);color:var(--muted);line-height:1.62;margin-bottom:22px;max-width:560px}
.tesis{margin-top:6px;padding:14px 16px;background:rgba(74,58,193,.08);border:1px solid rgba(74,58,193,.2);border-radius:13px;font-size:13px;color:var(--muted);line-height:1.6}
.tesis code{font-family:'JetBrains Mono',monospace;font-size:11.5px;color:var(--lavender);background:rgba(74,58,193,.22);padding:2px 7px;border-radius:5px}
.foco-wrap{margin-top:14px}
.foco-head{display:flex;align-items:center;justify-content:space-between;margin-bottom:8px}
.foco-head .lbl{font-family:'Space Grotesk',sans-serif;font-weight:600;font-size:9.5px;letter-spacing:.22em;text-transform:uppercase;color:var(--muted)}
textarea#foco{width:100%;min-height:64px;resize:vertical;background:rgba(13,15,31,.7);border:1px solid var(--border);border-radius:11px;color:var(--txt);font-family:'Plus Jakarta Sans',sans-serif;font-size:13px;line-height:1.55;padding:11px 12px;outline:none;transition:border-color .2s}
textarea#foco:focus{border-color:var(--violet);box-shadow:0 0 0 3px rgba(124,126,223,.1)}
/* North Star ring panel */
.nsm-panel{display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center}
.ring-outer{position:relative;width:210px;height:210px;display:flex;align-items:center;justify-content:center}
.ring-orbit{position:absolute;inset:-14px;border-radius:50%;border:1px dashed rgba(124,126,223,.16);animation:spin 38s linear infinite}
.ring-orbit::before{content:'';position:absolute;width:8px;height:8px;border-radius:50%;background:var(--violet);top:-4px;left:50%;transform:translateX(-50%)}
.pulse-ring{position:absolute;border-radius:50%;border:1.5px solid var(--violet);width:100%;height:100%;animation:pRing 2.6s ease-out infinite;pointer-events:none}
.pulse-ring.r2{animation-delay:.85s}.pulse-ring.r3{animation-delay:1.7s}
.ring-ctr{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center}
.ring-num{font-family:'JetBrains Mono',monospace;font-weight:700;font-size:46px;line-height:1}
.ring-pct{font-family:'JetBrains Mono',monospace;font-size:11px;color:var(--muted);margin-top:5px}
.nsm-formula{font-family:'JetBrains Mono',monospace;font-size:13px;margin-top:18px}
.nsm-formula .op{color:var(--border)}
.nsm-targets{display:flex;gap:8px;margin-top:14px;flex-wrap:wrap;justify-content:center}
.nsm-tg{font-family:'JetBrains Mono',monospace;font-size:10px;color:var(--muted);border:1px solid var(--border);border-radius:7px;padding:4px 10px}
.nsm-tg b{color:var(--lavender)}
.nsm-insight{margin-top:14px;font-size:12px;color:var(--muted);line-height:1.55;max-width:340px}
''')

add(r'''/* EDITABLE INPUTS */
.edit{font-family:'JetBrains Mono',monospace;background:transparent;border:none;border-bottom:1px dashed transparent;color:inherit;font-size:inherit;font-weight:inherit;padding:0 1px;cursor:text;transition:.15s;-moz-appearance:textfield;text-align:center}
.edit::-webkit-outer-spin-button,.edit::-webkit-inner-spin-button{-webkit-appearance:none}
.edit:hover{border-bottom-color:var(--border)}
.edit:focus{outline:none;border-bottom-color:var(--violet);color:var(--lavender)}
/* INFO BUTTON + POPOVER */
.info{width:15px;height:15px;border-radius:50%;border:1px solid var(--border);background:rgba(124,126,223,.12);color:var(--lavender);font-size:9px;font-weight:700;cursor:pointer;display:inline-flex;align-items:center;justify-content:center;flex:0 0 auto;transition:.2s;font-family:'JetBrains Mono',monospace;line-height:1}
.info:hover{border-color:var(--violet);background:rgba(124,126,223,.28);transform:scale(1.12)}
#popover{position:fixed;z-index:520;max-width:300px;background:rgba(18,20,42,.99);border:1px solid var(--violet);border-radius:13px;padding:14px 15px;font-size:12.5px;line-height:1.6;color:var(--txt);box-shadow:0 14px 50px rgba(0,0,0,.55);opacity:0;pointer-events:none;transform:translateY(7px);transition:opacity .2s,transform .2s}
#popover.show{opacity:1;pointer-events:auto;transform:translateY(0)}
#popover .pop-t{font-family:'Space Grotesk',sans-serif;font-weight:700;font-size:10.5px;letter-spacing:.12em;text-transform:uppercase;color:var(--violet);margin-bottom:6px}
#popover .pop-x{position:absolute;top:8px;right:10px;color:var(--muted);cursor:pointer;font-size:15px;line-height:1}
#popover .pop-x:hover{color:var(--txt)}
''')

add(r'''/* SIMULATOR */
#simulator{background:rgba(13,15,31,.5)}
.sim-grid{display:grid;grid-template-columns:1fr 1.1fr;gap:18px;margin-top:30px}
.sim-controls .presets{display:flex;gap:7px;margin-bottom:18px;flex-wrap:wrap}
.preset{font-family:'Space Grotesk',sans-serif;font-weight:600;font-size:10.5px;letter-spacing:.05em;color:var(--muted);background:rgba(34,35,65,.6);border:1px solid var(--border);padding:7px 13px;border-radius:999px;cursor:pointer;transition:.2s}
.preset:hover{color:#fff;border-color:var(--violet)}
.preset.active{color:#fff;background:linear-gradient(135deg,#4A3AC1,#7C7EDF);border-color:transparent}
.slider-row{margin-bottom:17px}
.slider-top{display:flex;align-items:center;gap:7px;margin-bottom:8px}
.slider-name{font-weight:600;font-size:12.5px;display:flex;align-items:center;gap:6px}
.slider-val{margin-left:auto;font-family:'JetBrains Mono',monospace;font-weight:700;font-size:14px;color:var(--lavender)}
.slider-base{font-family:'JetBrains Mono',monospace;font-size:9.5px;color:var(--border);margin-left:7px}
input[type=range]{-webkit-appearance:none;appearance:none;width:100%;height:5px;border-radius:3px;background:rgba(58,64,101,.5);outline:none;cursor:pointer}
input[type=range]::-webkit-slider-thumb{-webkit-appearance:none;appearance:none;width:18px;height:18px;border-radius:50%;background:linear-gradient(135deg,#7C7EDF,#8F60EA);border:2px solid #EEF3F8;cursor:pointer;box-shadow:0 0 12px rgba(124,126,223,.55)}
input[type=range]::-moz-range-thumb{width:16px;height:16px;border-radius:50%;background:linear-gradient(135deg,#7C7EDF,#8F60EA);border:2px solid #EEF3F8;cursor:pointer}
.slider-help{font-size:11px;color:var(--muted);margin-top:6px;line-height:1.45}
.sim-outputs{display:flex;flex-direction:column;gap:12px}
.sim-verdict{padding:16px 18px;border-radius:15px;border:1px solid var(--border);display:flex;align-items:center;gap:14px;transition:.4s}
.sim-verdict .vbig{font-family:'Space Grotesk',sans-serif;font-weight:700;font-size:17px;line-height:1.15}
.sim-verdict .vsm{font-size:11.5px;color:var(--muted);margin-top:3px;line-height:1.45}
.sim-verdict .vicon{width:46px;height:46px;border-radius:13px;display:flex;align-items:center;justify-content:center;font-size:23px;flex:0 0 auto}
.out-grid{display:grid;grid-template-columns:1fr 1fr;gap:10px}
.out-card{background:rgba(13,15,31,.6);border:1px solid var(--border);border-radius:13px;padding:14px}
.out-lbl{display:flex;align-items:center;gap:6px;font-size:9.5px;letter-spacing:.08em;text-transform:uppercase;color:var(--muted);font-weight:600;margin-bottom:6px}
.out-val{font-family:'JetBrains Mono',monospace;font-weight:700;font-size:25px;line-height:1}
.out-delta{font-family:'JetBrains Mono',monospace;font-size:10.5px;margin-top:3px}
.out-bar{height:3px;border-radius:2px;background:rgba(58,64,101,.35);margin-top:9px;overflow:hidden}
.out-bar i{display:block;height:100%;border-radius:2px;width:0;transition:width .6s ease}
.sim-note{margin-top:4px;padding:11px 14px;background:rgba(74,58,193,.08);border:1px solid rgba(74,58,193,.22);border-radius:11px;font-size:12px;color:var(--muted);line-height:1.5;display:flex;gap:9px}
.sim-note b{color:var(--lavender)}
.sim-note-lbl{font-family:'Space Grotesk',sans-serif;font-weight:700;font-size:8.5px;letter-spacing:.14em;text-transform:uppercase;color:var(--violet);flex:0 0 auto}
''')

add(r'''/* KPI HEALTH GRID */
.kpi-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:11px;margin-top:30px}
.kpi{border-radius:15px;padding:16px;position:relative;overflow:hidden;background:rgba(34,35,65,.58);border:1px solid var(--border);transition:transform .25s,border-color .25s}
.kpi:hover{transform:translateY(-3px);border-color:rgba(124,126,223,.4)}
.kpi.g{border-left:3px solid var(--good)}.kpi.w{border-left:3px solid var(--watch)}.kpi.r{border-left:3px solid var(--risk)}
.kpi-top{display:flex;justify-content:space-between;align-items:center;margin-bottom:7px;gap:6px}
.kpi-name{font-size:9px;letter-spacing:.06em;text-transform:uppercase;color:var(--muted);font-weight:600;display:flex;align-items:center;gap:5px}
.kpi-dot{width:7px;height:7px;border-radius:50%;flex:0 0 auto}
.kpi-val{font-family:'JetBrains Mono',monospace;font-weight:700;font-size:23px;line-height:1;margin-bottom:3px}
.kpi-tgt{font-family:'JetBrains Mono',monospace;font-size:9.5px;color:var(--border)}
.kpi-bar{height:3px;border-radius:2px;background:rgba(58,64,101,.3);margin-top:9px;overflow:hidden;position:relative}
.kpi-bar i{display:block;height:100%;border-radius:2px;width:0;transition:width .7s ease}
.legend{margin-top:16px;display:flex;gap:16px;flex-wrap:wrap;align-items:center;font-size:11px;color:var(--muted)}
.legend .p{display:flex;align-items:center;gap:6px}
.legend .sd{width:8px;height:8px;border-radius:50%}
''')

add(r'''/* FUNNEL */
#funnel-sec{background:rgba(13,15,31,.5)}
.fn-wrap{display:flex;flex-direction:column;gap:8px;margin-top:30px}
.fn-row{display:grid;grid-template-columns:172px 1fr 128px;align-items:center;gap:13px}
.fn-lbl{display:flex;align-items:center;gap:8px;font-weight:600;font-size:12.5px}
.fn-n{font-family:'JetBrains Mono',monospace;font-size:10px;color:var(--border);width:22px}
.fn-track{height:30px;background:rgba(13,15,31,.72);border:1px solid var(--border);border-radius:8px;position:relative;overflow:hidden}
.fn-fill{position:absolute;left:0;top:0;bottom:0;border-radius:7px 0 0 7px;width:0;transition:width .85s ease}
.fn-obj{position:absolute;top:0;bottom:0;width:1.5px;background:rgba(255,255,255,.45);z-index:3}
.fn-obj::after{content:'obj';position:absolute;top:-14px;left:50%;transform:translateX(-50%);font-family:'JetBrains Mono',monospace;font-size:7px;color:var(--muted)}
.fn-v{position:absolute;right:8px;top:50%;transform:translateY(-50%);font-family:'JetBrains Mono',monospace;font-size:11px;color:var(--txt);z-index:2}
.fn-stat{display:flex;align-items:center;gap:5px;justify-content:flex-end;font-family:'JetBrains Mono',monospace;font-size:11px}
.fn-row.neck .fn-track{box-shadow:0 0 0 1.5px var(--risk),0 0 16px -5px var(--risk)}
.neck-flag{font-family:'Space Grotesk',sans-serif;font-weight:700;font-size:7px;letter-spacing:.1em;text-transform:uppercase;color:var(--risk);border:1px solid var(--risk);border-radius:4px;padding:1px 4px;white-space:nowrap}
.fn-note{margin-top:14px;padding:11px 14px;background:rgba(242,97,122,.08);border:1px solid rgba(242,97,122,.22);border-radius:11px;font-size:12px;color:var(--muted);display:flex;gap:9px;line-height:1.5}
.fn-note-lbl{font-family:'Space Grotesk',sans-serif;font-weight:700;font-size:8.5px;letter-spacing:.14em;text-transform:uppercase;color:var(--risk);flex:0 0 auto}
.fn-act{margin-top:10px;padding:11px 14px;background:rgba(74,58,193,.08);border:1px solid rgba(74,58,193,.2);border-radius:11px;font-size:12px;color:var(--muted);line-height:1.55}
.fn-act b{color:var(--lavender)}
''')

add(r'''/* REVENUE MIX */
.mix-card-grid{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-top:30px}
.mix-h{display:flex;justify-content:space-between;align-items:baseline;margin:4px 0 9px}
.mix-h .mt{font-family:'Space Grotesk',sans-serif;font-weight:600;font-size:10px;letter-spacing:.14em;text-transform:uppercase;color:var(--muted)}
.mix-h .mv{font-family:'JetBrains Mono',monospace;font-size:13px;color:var(--txt)}
.mixbar{display:flex;height:26px;border-radius:8px;overflow:hidden;border:1px solid var(--border)}
.seg{height:100%;display:flex;align-items:center;justify-content:center;font-family:'JetBrains Mono',monospace;font-size:9.5px;color:rgba(14,17,33,.85);font-weight:700;min-width:0;overflow:hidden;white-space:nowrap;transition:width .8s ease}
.mixleg{display:flex;flex-wrap:wrap;gap:9px 14px;margin-top:12px}
.mixleg .it{display:flex;align-items:center;gap:6px;font-size:11px;color:var(--muted)}
.mixleg .sw{width:8px;height:8px;border-radius:2px}
.mixleg .it b{color:var(--txt);font-family:'JetBrains Mono',monospace;font-size:11px}
.cash-warn{margin-top:16px;padding:12px 15px;background:var(--watch-bg);border:1px solid rgba(240,160,48,.22);border-radius:11px;font-size:12px;color:var(--muted);line-height:1.55}
.cash-warn b{color:var(--watch)}
.arrow-mid{display:flex;align-items:center;justify-content:center;font-size:22px;color:var(--violet)}
''')

add(r'''/* AGENDA + QUICK WINS */
#readiness{background:rgba(13,15,31,.5)}
.ready-grid{display:grid;grid-template-columns:1.25fr .75fr;gap:18px;margin-top:30px}
.agenda{list-style:none;display:flex;flex-direction:column;gap:3px}
.ag-item{display:flex;gap:11px;align-items:flex-start;padding:9px 10px;border-radius:10px;cursor:pointer;transition:.2s}
.ag-item:hover{background:rgba(124,126,223,.07)}
.ag-check{width:19px;height:19px;border-radius:6px;border:1.5px solid var(--border);flex:0 0 auto;margin-top:1px;display:flex;align-items:center;justify-content:center;transition:.2s;background:transparent}
.ag-check.dn{background:var(--green);border-color:var(--green)}
.ag-n{font-family:'JetBrains Mono',monospace;font-size:11px;color:var(--violet);font-weight:700;flex:0 0 auto;width:20px;margin-top:2px}
.ag-txt{font-size:12.5px;line-height:1.45;transition:.2s}
.ag-txt.dn{text-decoration:line-through;color:var(--muted);opacity:.6}
.ag-prog{height:4px;border-radius:3px;background:rgba(58,64,101,.35);margin-top:16px;overflow:hidden}
.ag-prog i{display:block;height:100%;border-radius:3px;background:linear-gradient(90deg,#4A3AC1,#47CF78);transition:width .5s ease;width:0}
.ag-foot{font-size:10.5px;color:var(--muted);margin-top:6px;font-family:'JetBrains Mono',monospace}
.win-item{display:flex;align-items:flex-start;gap:9px;padding:8px 0;border-bottom:1px dashed rgba(58,64,101,.4)}
.win-item:last-of-type{border-bottom:none}
.win-check{width:17px;height:17px;border-radius:5px;border:1.5px solid var(--border);cursor:pointer;flex:0 0 auto;margin-top:1px;display:flex;align-items:center;justify-content:center;transition:.2s}
.win-check.dn{background:var(--green);border-color:var(--green)}
.win-txt{flex:1;font-size:12.5px;line-height:1.4}
.win-txt.dn{text-decoration:line-through;color:var(--muted);opacity:.6}
.win-del{color:var(--border);cursor:pointer;font-size:16px;line-height:1;padding:0 2px;transition:.15s;align-self:center}
.win-del:hover{color:var(--risk)}
.win-add{display:flex;gap:7px;margin-top:12px}
.win-input{flex:1;background:rgba(13,15,31,.72);border:1px dashed var(--border);border-radius:8px;padding:8px 10px;color:var(--txt);font-family:'Plus Jakarta Sans',sans-serif;font-size:12.5px;outline:none;transition:.2s}
.win-input:focus{border-color:var(--violet);border-style:solid}
.win-addbtn{padding:8px 13px;border-radius:999px;background:linear-gradient(135deg,#4A3AC1,#7C7EDF);border:none;color:#fff;font-family:'Space Grotesk',sans-serif;font-weight:600;font-size:11px;cursor:pointer;white-space:nowrap}
.win-addbtn:hover{opacity:.85}
''')

add(r'''/* INTERPRET GUIDE */
.guide-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin-top:30px}
.guide{padding:22px 20px}
.guide .gn{font-family:'JetBrains Mono',monospace;font-weight:700;font-size:13px;color:var(--violet);width:34px;height:34px;border-radius:10px;background:rgba(74,58,193,.16);border:1px solid rgba(124,126,223,.22);display:flex;align-items:center;justify-content:center;margin-bottom:14px}
.guide h4{font-family:'Space Grotesk',sans-serif;font-weight:700;font-size:15px;margin-bottom:9px}
.guide p{font-size:12.5px;color:var(--muted);line-height:1.6}
.guide p b{color:var(--lavender)}
/* FOOTER */
footer{position:relative;z-index:5;border-top:1px solid var(--border);padding:26px 0;margin-top:40px}
.foot-in{display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:12px;max-width:1280px;margin:0 auto;padding:0 22px}
.foot-brand{font-family:'Space Grotesk',sans-serif;font-weight:700;font-size:14px}
.foot-copy{font-size:10.5px;color:var(--border);font-family:'JetBrains Mono',monospace}
.foot-links{display:flex;gap:16px}
.foot-links a{font-size:11px;color:var(--muted);text-decoration:none}
.foot-links a:hover{color:var(--txt)}
''')

add(r'''/* TOUR */
#tour-box{position:fixed;z-index:560;left:50%;bottom:26px;transform:translateX(-50%) translateY(20px);max-width:430px;width:calc(100% - 40px);background:rgba(18,20,42,.99);border:1px solid var(--violet);border-radius:16px;padding:20px 22px;box-shadow:0 18px 64px rgba(0,0,0,.6);opacity:0;pointer-events:none;transition:opacity .3s,transform .3s}
#tour-box.show{opacity:1;pointer-events:auto;transform:translateX(-50%) translateY(0)}
#tour-box .tt{font-family:'Space Grotesk',sans-serif;font-weight:700;font-size:16px;margin-bottom:8px}
#tour-box .td{font-size:13px;color:var(--muted);line-height:1.6;margin-bottom:16px}
#tour-box .tnav{display:flex;align-items:center;gap:9px}
#tour-box .tstep{font-family:'JetBrains Mono',monospace;font-size:11px;color:var(--muted);margin-right:auto}
.tour-hl{position:relative;z-index:540;border-radius:18px;box-shadow:0 0 0 3px var(--violet),0 0 0 9999px rgba(8,10,22,.8);transition:box-shadow .3s}
.tbtn-s{font-family:'Space Grotesk',sans-serif;font-weight:600;font-size:12px;padding:8px 16px;border-radius:999px;cursor:pointer;border:1px solid var(--border);background:transparent;color:var(--txt);transition:.2s}
.tbtn-s:hover{border-color:var(--violet)}
.tbtn-s.primary{background:linear-gradient(135deg,#4A3AC1,#7C7EDF);border-color:transparent;color:#fff}
/* TOAST */
#toast{position:fixed;bottom:22px;right:22px;z-index:600;background:rgba(18,20,42,.98);border:1px solid var(--violet);border-radius:12px;padding:12px 18px;font-size:12.5px;color:var(--txt);box-shadow:0 10px 40px rgba(0,0,0,.5);opacity:0;transform:translateY(14px);transition:opacity .3s,transform .3s;pointer-events:none}
#toast.show{opacity:1;transform:translateY(0)}
.reveal{opacity:0;transform:translateY(24px);transition:opacity .7s ease,transform .7s ease}
.reveal.in{opacity:1;transform:translateY(0)}
/* RESPONSIVE */
@media(max-width:1024px){
  .north-grid,.sim-grid,.mix-card-grid,.ready-grid{grid-template-columns:1fr}
  .kpi-grid{grid-template-columns:repeat(3,1fr)}
  .guide-grid{grid-template-columns:1fr}
  .arrow-mid{transform:rotate(90deg)}
}
@media(max-width:720px){
  .pills{display:none}
  .kpi-grid{grid-template-columns:repeat(2,1fr)}
  .out-grid{grid-template-columns:1fr 1fr}
  .fn-row{grid-template-columns:108px 1fr;grid-template-rows:auto auto;gap:5px 8px}
  .fn-stat{grid-column:2;justify-content:flex-start}
  .bar-sub{display:none}
  .verdict span{display:none}
}
@media(max-width:480px){.kpi-grid,.out-grid{grid-template-columns:1fr}}
''')

add(r'''</style>
</head>
<body>
<canvas id="bg-canvas"></canvas>
<div class="grain"></div>
<div id="scroll-bar"></div>
<div id="popover"><span class="pop-x" onclick="hidePop()">&times;</span><div class="pop-t" id="pop-t"></div><div id="pop-d"></div></div>
<div id="toast"></div>
<div id="tour-box"><div class="tt" id="tour-t"></div><div class="td" id="tour-d"></div><div class="tnav"><span class="tstep" id="tour-step"></span><button class="tbtn-s" id="tour-prev" onclick="tourPrev()">Atrás</button><button class="tbtn-s primary" id="tour-next" onclick="tourNext()">Siguiente</button></div></div>
''')

# ============================ COMMAND BAR ============================
add(r'''<div id="bar">
  <div class="bar-in">
    <a href="#north" class="bar-logo">
      <img src="aecodito.png" class="aecodito" alt="Aecodito">
      <span><span class="bar-name"><span class="grad">AECODE</span></span><span class="bar-sub">Startup Cockpit</span></span>
    </a>
    <div class="verdict" id="verdict" title="Veredicto de fundabilidad"></div>
    <nav class="pills" id="pills">
      <a class="pill" data-sec="north">Norte</a>
      <a class="pill" data-sec="simulator">Simulador</a>
      <a class="pill" data-sec="kpis">Fundabilidad</a>
      <a class="pill" data-sec="funnel-sec">Funnel</a>
      <a class="pill" data-sec="revenue">Ingresos</a>
      <a class="pill" data-sec="readiness">Agenda</a>
      <a class="pill" data-sec="interpret">Interpretar</a>
    </nav>
    <div class="tools">
      <button class="tbtn primary" onclick="startTour()">&#9737; Tour</button>
      <button class="tbtn" onclick="doExport()">Exportar</button>
      <button class="tbtn" onclick="document.getElementById('imp').click()">Importar</button>
      <button class="tbtn" onclick="doReset()">Reset</button>
      <input type="file" id="imp" accept="application/json" hidden>
    </div>
  </div>
</div>
''')

# ============================ NORTH STAR ============================
add(r'''<section id="north" class="section">
  <div class="wrap">
    <div class="north-grid">
      <div class="north-lead reveal">
        <div class="hbadge"><span class="pulse-dot"></span>Learning OS &middot; AEC &middot; Latam</div>
        <h1 class="north-h1">El cockpit que convierte tu data AEC en <span class="grad">decisiones financiables</span></h1>
        <p class="north-p">Edita cualquier número, simula escenarios y entiende qué mover. Cada métrica trae su explicación &mdash; pasa el cursor por el icono <span class="info" style="cursor:default">i</span> para interpretarla. Todo se guarda en tu navegador.</p>
        <div class="tesis">
          <strong style="color:var(--txt)">Tesis central:</strong> convertir cada curso AEC en ruta, práctica, evidencia y <span class="grad">skill certificable</span>. North Star: <code>skills verificadas con evidencia &divide; usuarios activos mensuales</code> &mdash; la única métrica que no se puede maquillar.
        </div>
        <div class="foco-wrap">
          <div class="foco-head"><span class="lbl">&#9737; El Foco &middot; Una Sola Cosa</span><span class="lbl" id="foco-stamp" style="color:var(--border)"></span></div>
          <textarea id="foco" spellcheck="false" placeholder="Escribe el foco número uno del trimestre..."></textarea>
        </div>
      </div>
      <div class="card nsm-panel reveal" id="nsm-card">
        <div class="card-eyebrow" style="align-self:flex-start"><span class="tick"></span>North Star Metric <span class="info" data-info="nsm">i</span></div>
        <div class="ring-outer">
          <div class="ring-orbit"></div>
          <span class="pulse-ring"></span><span class="pulse-ring r2"></span><span class="pulse-ring r3"></span>
          <svg width="210" height="210" style="position:absolute;inset:0">
            <circle cx="105" cy="105" r="92" fill="none" stroke="rgba(58,64,101,.35)" stroke-width="9"/>
            <circle id="nsm-ring" cx="105" cy="105" r="92" fill="none" stroke="" stroke-width="9" stroke-linecap="round" stroke-dasharray="578" stroke-dashoffset="578" transform="rotate(-90 105 105)" style="transition:stroke-dashoffset 1.1s cubic-bezier(.22,1,.36,1),stroke .4s"/>
          </svg>
          <div class="ring-ctr"><div class="ring-num" id="nsm-num">0.00</div><div class="ring-pct" id="nsm-pct">0% del obj.</div></div>
        </div>
        <div class="nsm-formula"><span class="edit" data-edit="skills" style="width:4ch">72</span> <span class="op">skills &divide;</span> <span class="edit" data-edit="mau" style="width:5ch">420</span> <span class="op">MAU</span></div>
        <div class="nsm-targets">
          <span class="nsm-tg">objetivo beta <b id="tg-beta">0.40</b></span>
          <span class="nsm-tg">escala <b>&gt;0.80</b></span>
        </div>
        <div class="nsm-insight" id="nsm-insight"></div>
      </div>
    </div>
  </div>
</section>
''')

# ============================ SIMULATOR ============================
add(r'''<section id="simulator" class="section">
  <div class="wrap">
    <div class="reveal">
      <div class="eyebrow">El Motor &middot; Simulador de Escenarios</div>
      <h2 class="section-h">Mueve una palanca. Mira el impacto.</h2>
      <p class="section-p">Esto es lo que separa un reporte de una herramienta: arrastra los sliders y observa cómo cambian tu NSM, tu caja recurrente, tu LTV/CAC y tu veredicto de fundabilidad <strong>en vivo</strong>. Aprende la relación causa &rarr; efecto de tu negocio.</p>
    </div>
    <div class="sim-grid">
      <div class="card sim-controls reveal">
        <div class="card-eyebrow"><span class="tick"></span>Palancas &middot; Escenarios predefinidos</div>
        <div class="presets">
          <button class="preset active" data-preset="hoy">Hoy</button>
          <button class="preset" data-preset="beta">Meta Beta</button>
          <button class="preset" data-preset="escala">Escala 12m</button>
        </div>
        <div class="slider-row">
          <div class="slider-top"><span class="slider-name">Evidence Rate <span class="info" data-info="evid">i</span></span><span class="slider-val" id="sv-evid">42%</span></div>
          <input type="range" id="s-evid" min="20" max="80" value="42" step="1">
          <div class="slider-help">% de usuarios que suben evidencia real. Tu cuello de botella actual.</div>
        </div>
        <div class="slider-row">
          <div class="slider-top"><span class="slider-name">Verification Rate <span class="info" data-info="verif">i</span></span><span class="slider-val" id="sv-verif">69%</span></div>
          <input type="range" id="s-verif" min="40" max="95" value="69" step="1">
          <div class="slider-help">% de evidencias que se aprueban como skill verificada.</div>
        </div>
        <div class="slider-row">
          <div class="slider-top"><span class="slider-name">MAU activos <span class="info" data-info="mau2">i</span></span><span class="slider-val" id="sv-mau">420</span></div>
          <input type="range" id="s-mau" min="200" max="6000" value="420" step="20">
          <div class="slider-help">Usuarios activos al mes. Escalar usuarios NO arregla el NSM &mdash; solo la calidad lo hace.</div>
        </div>
        <div class="slider-row">
          <div class="slider-top"><span class="slider-name">Conversión a pago <span class="info" data-info="conv">i</span></span><span class="slider-val" id="sv-conv">7%</span></div>
          <input type="range" id="s-conv" min="2" max="25" value="7" step="1">
          <div class="slider-help">% de MAU que paga la suscripción Pro.</div>
        </div>
        <div class="slider-row">
          <div class="slider-top"><span class="slider-name">Precio Pro / mes <span class="info" data-info="price">i</span></span><span class="slider-val" id="sv-price">$29</span></div>
          <input type="range" id="s-price" min="9" max="99" value="29" step="1">
          <div class="slider-help">Precio mensual del plan Pro. Sube el LTV/CAC sin tocar el CAC.</div>
        </div>
      </div>
      <div class="sim-outputs reveal">
        <div class="sim-verdict" id="sim-verdict">
          <div class="vicon" id="sv-icon">&#9203;</div>
          <div><div class="vbig" id="sv-verdict-t">&mdash;</div><div class="vsm" id="sv-verdict-d"></div></div>
        </div>
        <div class="out-grid">
          <div class="out-card"><div class="out-lbl">NSM proyectado <span class="info" data-info="nsm">i</span></div><div class="out-val" id="o-nsm" style="color:var(--violet)">0.00</div><div class="out-delta" id="od-nsm"></div><div class="out-bar"><i id="ob-nsm" style="background:var(--violet)"></i></div></div>
          <div class="out-card"><div class="out-lbl">MRR plataforma <span class="info" data-info="platmrr">i</span></div><div class="out-val" id="o-plat" style="color:var(--green)">$0</div><div class="out-delta" id="od-plat"></div><div class="out-bar"><i id="ob-plat" style="background:var(--green)"></i></div></div>
          <div class="out-card"><div class="out-lbl">LTV / CAC <span class="info" data-info="ltvcac">i</span></div><div class="out-val" id="o-ltv" style="color:var(--blue)">0.0x</div><div class="out-delta" id="od-ltv"></div><div class="out-bar"><i id="ob-ltv" style="background:var(--blue)"></i></div></div>
          <div class="out-card"><div class="out-lbl">Runway <span class="info" data-info="runway">i</span></div><div class="out-val" id="o-run" style="color:var(--watch)">0 mo</div><div class="out-delta" id="od-run"></div><div class="out-bar"><i id="ob-run" style="background:var(--watch)"></i></div></div>
        </div>
        <div class="sim-note"><span class="sim-note-lbl">Lectura</span><span id="sim-note-txt"></span></div>
      </div>
    </div>
  </div>
</section>
''')

# ============================ KPI / FUNDABILIDAD ============================
add(r'''<section id="kpis" class="section">
  <div class="wrap">
    <div class="reveal">
      <div class="eyebrow">Salud &middot; Fundabilidad</div>
      <h2 class="section-h">Las 8 métricas que mira un inversionista.</h2>
      <p class="section-p">Tu realidad actual (editable &mdash; haz click en cualquier número). El semáforo te dice si estás en objetivo. Toca el icono <span class="info" style="cursor:default">i</span> de cada tarjeta para entender el umbral y por qué importa.</p>
    </div>
    <div class="kpi-grid" id="kpi-grid"></div>
    <div class="legend">
      <div class="p"><span class="sd" style="background:var(--good)"></span>En objetivo</div>
      <div class="p"><span class="sd" style="background:var(--watch)"></span>Vigilar</div>
      <div class="p"><span class="sd" style="background:var(--risk)"></span>En riesgo</div>
      <span style="margin-left:auto;font-size:10.5px;color:var(--border)">Click en cualquier número para editar &middot; se guarda en este navegador</span>
    </div>
  </div>
</section>
''')

# ============================ FUNNEL ============================
add(r'''<section id="funnel-sec" class="section">
  <div class="wrap">
    <div class="reveal">
      <div class="eyebrow">Cadena de Valor</div>
      <h2 class="section-h">De 65k de comunidad a 7 pagos.</h2>
      <p class="section-p">El funnel completo, con el objetivo de conversión marcado en cada paso. El cuello de botella se detecta solo: es el paso con mayor brecha vs su objetivo. Edita los valores y míralo recalcularse.</p>
    </div>
    <div class="fn-wrap" id="fn-wrap"></div>
    <div class="fn-note"><span class="fn-note-lbl">Cuello</span><span id="fn-neck-txt"></span></div>
    <div class="fn-act" id="fn-act"></div>
  </div>
</section>
''')

# ============================ REVENUE MIX ============================
add(r'''<section id="revenue" class="section">
  <div class="wrap">
    <div class="reveal">
      <div class="eyebrow">La Apuesta &middot; Migración del Modelo</div>
      <h2 class="section-h">De caja de cohortes a MRR recurrente.</h2>
      <p class="section-p">Hoy el 60% viene de Live (no recurrente). La apuesta es invertir el mix hacia Microlearning recurrente. Esto es lo que un inversionista quiere ver: un motor que escala sin depender de horas de instructor.</p>
    </div>
    <div class="mix-card-grid">
      <div class="card reveal">
        <div class="card-eyebrow"><span class="tick"></span>Mix actual <span class="info" data-info="mixnow">i</span> &middot; <span id="mix-now-tot" style="color:var(--txt)">$5,150</span>/mes</div>
        <div class="mixbar" id="mix-now"></div>
        <div class="mixleg" id="mix-now-leg"></div>
        <div class="cash-warn">&#9888; Solo <b id="mrr-real">$1,288</b> es <b>MRR real</b> (recurrente). El resto es caja de cohortes Live. Nunca lo llames MRR frente a un inversionista.</div>
      </div>
      <div class="card reveal">
        <div class="card-eyebrow"><span class="tick"></span>Mix objetivo 12m <span class="info" data-info="mixtgt">i</span> &middot; <span id="mix-tgt-tot" style="color:var(--txt)">$30,000</span>/mes</div>
        <div class="mixbar" id="mix-tgt"></div>
        <div class="mixleg" id="mix-tgt-leg"></div>
        <div class="cash-warn" style="background:var(--good-bg);border-color:rgba(71,207,120,.22)">&#9650; Objetivo: <b style="color:var(--green)">60% Microlearning recurrente</b>. El motor Live &rarr; Micro (hoy 18%, meta 45%) es lo que dispara esta migración.</div>
      </div>
    </div>
  </div>
</section>
''')

# ============================ READINESS AGENDA + QUICK WINS ============================
add(r'''<section id="readiness" class="section">
  <div class="wrap">
    <div class="reveal">
      <div class="eyebrow">Startup Readiness</div>
      <h2 class="section-h">La agenda de 10 puntos para ser financiable.</h2>
      <p class="section-p">Marca lo que ya está hecho y mira tu progreso de preparación. A la derecha, los quick wins de esta semana &mdash; agrega los tuyos.</p>
    </div>
    <div class="ready-grid">
      <div class="card reveal">
        <div class="card-eyebrow"><span class="tick"></span>Agenda de Readiness</div>
        <ul class="agenda" id="agenda"></ul>
        <div class="ag-prog"><i id="ag-bar"></i></div>
        <div class="ag-foot" id="ag-foot"></div>
      </div>
      <div class="card reveal">
        <div class="card-eyebrow"><span class="tick"></span>Quick Wins &middot; Esta Semana</div>
        <div id="wins"></div>
        <div class="win-add"><input class="win-input" id="win-new" placeholder="Agregar prioridad..." maxlength="90"><button class="win-addbtn" onclick="addWin()">+ Agregar</button></div>
      </div>
    </div>
  </div>
</section>
''')

# ============================ INTERPRET GUIDE ============================
add(r'''<section id="interpret" class="section">
  <div class="wrap">
    <div class="reveal">
      <div class="eyebrow">Cómo Interpretar este Cockpit</div>
      <h2 class="section-h">Guía rápida para leerlo bien.</h2>
    </div>
    <div class="guide-grid">
      <div class="card guide reveal"><div class="gn">1</div><h4>Empieza por el North Star</h4><p>El <b>NSM</b> mide progresión real (skills verificadas &divide; MAU). Si está en rojo, <b>no escales catálogo ni compres tráfico</b>: tienes uso amplio y tibio, no amor intenso.</p></div>
      <div class="card guide reveal"><div class="gn">2</div><h4>Simula antes de actuar</h4><p>Usa el <b>Simulador</b> para ver qué palanca mueve más tu fundabilidad. Descubrirás que subir Evidence Rate y precio pesa más que duplicar usuarios.</p></div>
      <div class="card guide reveal"><div class="gn">3</div><h4>Ataca el cuello del funnel</h4><p>El paso marcado en rojo tiene la mayor brecha vs su objetivo. <b>Arréglalo primero</b>: optimizar adquisición con el cuello abierto es tirar dinero.</p></div>
      <div class="card guide reveal"><div class="gn">4</div><h4>Separa MRR de caja</h4><p>La caja de cohortes Live <b>no es MRR</b>. Un inversionista valora el recurrente. La migración hacia Microlearning es la tesis de escala.</p></div>
      <div class="card guide reveal"><div class="gn">5</div><h4>Lee el semáforo de fundabilidad</h4><p>Verde = en objetivo, ámbar = vigilar, rojo = bloquea ronda. El <b>veredicto</b> arriba resume si estás listo y qué te falta.</p></div>
      <div class="card guide reveal"><div class="gn">6</div><h4>Cierra la agenda</h4><p>Los 10 puntos son tu checklist de readiness. Cada uno marcado sube tu probabilidad de cerrar una ronda en buenos términos.</p></div>
    </div>
  </div>
</section>
''')

# ============================ FOOTER ============================
add(r'''<footer>
  <div class="foot-in">
    <div class="foot-brand"><span class="grad">AECODE</span> &middot; Startup Intelligence Cockpit</div>
    <div class="foot-links"><a href="#north">Norte</a><a href="#simulator">Simulador</a><a href="#kpis">Fundabilidad</a><a href="#readiness">Agenda</a></div>
    <div class="foot-copy">v2.0 &middot; 2026 &middot; data editable &amp; local</div>
  </div>
</footer>
''')

# ============================ JS ============================
add(r'''<script src="https://cdnjs.cloudflare.com/ajax/libs/animejs/3.2.1/anime.min.js"></script>
<script>
"use strict";
/* ===== SEED ===== */
var SEED={
  meta:{foco:"Subir el Evidence Rate de 42% a 55%. Es el cuello que separa a AECODE de un catálogo de cursos: sin evidencia no hay skill verificable, no hay NSM, no hay pago ligado a outcome.",updated:0},
  star:{skills:72,mau:420,target:0.40},
  health:[
    {k:"LTV / CAC",v:3.1,target:3,unit:"x",dir:"high",pre:"",info:"ltvcac"},
    {k:"CAC Payback",v:5.5,target:6,unit:" mo",dir:"low",pre:"",info:"payback"},
    {k:"Margen plataforma",v:72,target:80,unit:"%",dir:"high",pre:"",info:"margin"},
    {k:"Retención M1",v:38,target:45,unit:"%",dir:"high",pre:"",info:"ret1"},
    {k:"Retención M3",v:21,target:28,unit:"%",dir:"high",pre:"",info:"ret3"},
    {k:"CAC blended",v:35,target:30,unit:"",dir:"low",pre:"$",info:"cac"},
    {k:"Evidence Rate",v:42,target:55,unit:"%",dir:"high",pre:"",info:"evid"},
    {k:"Runway",v:10,target:15,unit:" mo",dir:"high",pre:"",info:"runway"}
  ],
  funnel:[
    {k:"Comunidad",v:65000,base:true},
    {k:"Registro",v:180,target:24,act:"El CTA debe ser 'diagnostica tu skill gap', no 'compra un curso'."},
    {k:"Diagnóstico",v:125,target:70,act:"Ruta recomendada en menos de 5 minutos o cae la activación."},
    {k:"Skill Start",v:74,target:60,act:"Muestra UNA skill pequeña y accionable hoy, no un programa largo."},
    {k:"Evidencia",v:31,target:55,act:"Divide la evidencia en pasos con ejemplo y rúbrica. Te diferencia de Udemy y YouTube.",neck:true},
    {k:"Verificada",v:19,target:65,act:"Acelera el feedback: sin validación rápida el usuario no siente progreso."},
    {k:"Pago",v:7,target:40,act:"Liga el pago a certificación o desbloqueo de ruta, no a 'contenido'. Vende el outcome."}
  ],
  mixNow:[{k:"Live Training",v:3090,c:"#4465EE"},{k:"Microlearning",v:1288,c:"#7C7EDF"},{k:"Enterprise",v:515,c:"#47CF78"},{k:"Credentials",v:257,c:"#95E3B1"}],
  mixTgt:[{k:"Microlearning",v:18000,c:"#7C7EDF"},{k:"Live Training",v:7500,c:"#4465EE"},{k:"Enterprise",v:3000,c:"#47CF78"},{k:"Credentials",v:1500,c:"#95E3B1"}],
  agenda:[
    {t:"Definir la ruta-cuña inicial con mayor pain y disposición a pagar",d:false},
    {t:"Separar P&L de Live, Plataforma e Híbrido",d:false},
    {t:"Tracking semanal de todo el funnel",d:false},
    {t:"Convertir cursos Live en cápsulas y rúbricas reutilizables",d:false},
    {t:"Lanzar piloto B2B de 30 días con 3 skills por rol",d:false},
    {t:"Versionar el AEC Skill Graph como activo central",d:false},
    {t:"Crear data room que separe métricas reales de supuestos",d:false},
    {t:"Calcular unit economics completos antes de levantar",d:false},
    {t:"Desplegar AI para reducir fricción, no como decoración",d:false},
    {t:"Preparar pitch: problema, solución, tracción, equipo, uso de fondos",d:false}
  ],
  wins:[
    {t:"Subir Evidence Rate 42% a 55%",d:false},
    {t:"Separar P&L Live / Plataforma / Híbrido",d:false},
    {t:"Lanzar piloto B2B 30 días",d:false},
    {t:"Calcular CAC/LTV por canal (no blended)",d:false},
    {t:"Convertir último Live en 5 cápsulas",d:false}
  ]
};
/* ===== INFO CONTENT (didáctico) ===== */
var INFO={
  nsm:["North Star Metric","skills verificadas con evidencia &divide; usuarios activos mensuales. Mide progresión profesional real, no vanity metrics como inscripciones o vistas. Es la única métrica que no se puede maquillar: o el usuario demostró una skill, o no."],
  evid:["Evidence Rate","% de usuarios que suben evidencia real de su skill (un entregable evaluado con rúbrica). Es el cuello de botella de AECODE: sin evidencia no hay skill verificable, sin skill no hay NSM, sin NSM no hay pago ligado a outcome."],
  verif:["Verification Rate","% de evidencias subidas que se aprueban como skill verificada (por AI + instructor). Hoy 69%. Si es muy bajo frustra; si es muy alto, no discrimina calidad."],
  mau2:["MAU activos","Usuarios activos mensuales. Ojo: escalar MAU NO mejora el NSM (que es una razón de calidad). Crecer en usuarios con NSM bajo solo amplía un problema."],
  conv:["Conversión a pago","% de MAU que paga la suscripción Pro. Pequeñas mejoras aquí mueven mucho el MRR recurrente."],
  price:["Precio Pro","Precio mensual del plan Pro. Subirlo mejora el LTV/CAC directamente (asumiendo CAC constante) y es la palanca más rápida de unit economics."],
  platmrr:["MRR plataforma","Ingreso recurrente real de la plataforma = MAU &times; conversión &times; precio. Es lo que un inversionista valora; la caja de Live no cuenta como MRR."],
  ltvcac:["LTV / CAC","Valor de vida del cliente &divide; costo de adquisición. &gt;3x indica un negocio sano y escalable. Por debajo de 3x, cada cliente nuevo destruye margen."],
  runway:["Runway","Meses de operación con la caja actual al ritmo de gasto presente. Menos de 12 meses enciende alarma; los inversionistas quieren ver pista para ejecutar la tesis."],
  payback:["CAC Payback","Meses para recuperar el costo de adquirir un cliente. Menos de 6 meses es saludable y permite reinvertir rápido en crecimiento."],
  margin:["Margen de plataforma","% que queda tras costos directos de servir al usuario. Un SaaS sano busca &gt;80%; márgenes bajos limitan la escala."],
  ret1:["Retención M1","% de usuarios activos al mes 1. Mide si el producto engancha en el primer ciclo. Bajo M1 = problema de activación/valor inicial."],
  ret3:["Retención M3","% activos al mes 3. Mide hábito de largo plazo. Es el predictor más fuerte de LTV."],
  cac:["CAC blended","Costo de adquisición promedio de todos los canales mezclados. Útil como referencia, pero calcula CAC por canal antes de levantar."],
  mixnow:["Mix actual","Distribución de ingresos hoy. 60% viene de Live (no recurrente). Riesgo: depende de horas de instructor y no escala solo."],
  mixtgt:["Mix objetivo 12m","Hacia dónde migrar: 60% Microlearning recurrente. Esta inversión del mix es la tesis de escala que vuelve a AECODE financiable."]
};
/* ===== PRESETS ===== */
var PRESETS={
  hoy:{evid:42,verif:69,mau:420,conv:7,price:29},
  beta:{evid:55,verif:78,mau:900,conv:10,price:29},
  escala:{evid:62,verif:85,mau:4200,conv:12,price:39}
};
var COL={good:"var(--good)",watch:"var(--watch)",risk:"var(--risk)"};
var HEX={good:"#47CF78",watch:"#F0A030",risk:"#F2617A"};
''')

add(r'''/* ===== STATE / PERSISTENCE ===== */
var KEY="aecode_cockpit_v2", S, firstPaint=true;
function num(x,f){var n=parseFloat(x);return isNaN(n)?(f===undefined?0:f):n;}
function clone(o){return JSON.parse(JSON.stringify(o));}
function load(){try{var r=localStorage.getItem(KEY);if(r)return merge(JSON.parse(r));}catch(e){}return clone(SEED);}
function merge(sv){
  var b=clone(SEED);
  try{
    if(sv.meta)b.meta.foco=sv.meta.foco||b.meta.foco;
    if(sv.star){b.star.skills=num(sv.star.skills,b.star.skills);b.star.mau=num(sv.star.mau,b.star.mau);b.star.target=num(sv.star.target,b.star.target);}
    if(sv.health)sv.health.forEach(function(h,i){if(b.health[i])b.health[i].v=num(h.v,b.health[i].v);});
    if(sv.funnel)sv.funnel.forEach(function(f,i){if(b.funnel[i])b.funnel[i].v=num(f.v,b.funnel[i].v);});
    if(sv.agenda)sv.agenda.forEach(function(a,i){if(b.agenda[i])b.agenda[i].d=!!a.d;});
    if(sv.wins)b.wins=sv.wins.map(function(w){return{t:w.t||"",d:!!w.d};});
  }catch(e){}
  return b;
}
function save(){try{S.meta.updated=Date.now();localStorage.setItem(KEY,JSON.stringify(S));stamp();}catch(e){}}
function stamp(){var el=document.getElementById("foco-stamp");if(el)el.textContent=S.meta.updated?"guardado "+new Date(S.meta.updated).toLocaleDateString("es-PE",{day:"2-digit",month:"short"}):"";}
function fmt(n){return Math.round(n).toLocaleString("en-US");}
function money(n){return "$"+fmt(n);}
/* ===== COMPUTE ===== */
function nsmStatus(p){return p>=0.9?"good":p>=0.6?"watch":"risk";}
function hStatus(h){return h.dir==="high"?(h.v>=h.target?"good":h.v>=h.target*0.9?"watch":"risk"):(h.v<=h.target?"good":h.v<=h.target*1.1?"watch":"risk");}
function compute(){
  var nsm=S.star.mau>0?S.star.skills/S.star.mau:0;
  var pct=S.star.target>0?nsm/S.star.target:0;
  var hs=S.health.map(function(h){return hStatus(h);});
  var risks=hs.filter(function(x){return x==="risk";}).length;
  var goods=hs.filter(function(x){return x==="good";}).length;
  var watches=hs.filter(function(x){return x==="watch";}).length;
  var v,vc;
  if(risks===0&&goods>=S.health.length*0.7){v="Listo para levantar";vc="good";}
  else if(risks<=2){v="En preparación";vc="watch";}
  else{v="Aún no financiable";vc="risk";}
  return {nsm:nsm,pct:pct,nsmSt:nsmStatus(pct),risks:risks,goods:goods,watches:watches,v:v,vc:vc};
}
''')

add(r'''/* ===== RENDER: VERDICT + NORTH STAR ===== */
function renderVerdict(C){
  var el=document.getElementById("verdict");
  el.innerHTML='<span class="vd" style="background:'+COL[C.vc]+'"></span><b style="color:'+COL[C.vc]+'">'+C.v+'</b><span>'+C.goods+'✓ · '+C.watches+'~ · '+C.risks+'✕</span>';
}
function renderNorth(C){
  var nc=HEX[C.nsmSt];
  document.getElementById("nsm-num").textContent=C.nsm.toFixed(2);
  document.getElementById("nsm-num").style.color=nc;
  document.getElementById("nsm-pct").textContent=Math.round(C.pct*100)+"% del obj.";
  var ring=document.getElementById("nsm-ring");
  ring.setAttribute("stroke",nc);
  var total=578, off=total*(1-Math.max(0,Math.min(1,C.pct)));
  ring.style.strokeDashoffset=firstPaint?total:off;
  if(firstPaint){setTimeout(function(){ring.style.strokeDashoffset=off;},250);}
  document.getElementById("tg-beta").textContent=S.star.target.toFixed(2);
  var ins=document.getElementById("nsm-insight");
  if(C.nsmSt==="risk")ins.innerHTML='<strong style="color:var(--risk)">Solo '+Math.round(C.nsm*100)+'% de tus MAU verifican una skill al mes.</strong> Uso amplio y tibio, no amor intenso. No escales catálogo hasta cerrar este gap.';
  else if(C.nsmSt==="watch")ins.innerHTML='Avanzando. Prioriza subir la tasa de evidencia esta semana para entrar en zona de escala.';
  else ins.innerHTML='NSM en zona de escala. Ahora sí: amplía adquisición con confianza.';
  document.querySelectorAll('[data-edit="skills"]').forEach(function(e){e.value=S.star.skills;});
  document.querySelectorAll('[data-edit="mau"]').forEach(function(e){e.value=S.star.mau;});
}
/* ===== RENDER: KPI ===== */
function renderKPI(){
  var g=document.getElementById("kpi-grid");
  g.innerHTML=S.health.map(function(h,i){
    var st=hStatus(h);
    var ratio=h.dir==="high"?h.v/h.target:(h.v>0?h.target/h.v:1);
    var w=Math.max(6,Math.min(100,ratio*100));
    return '<div class="kpi '+(st==="good"?"g":st==="watch"?"w":"r")+'">'+
      '<div class="kpi-top"><span class="kpi-name">'+h.k+' <span class="info" data-info="'+h.info+'">i</span></span><span class="kpi-dot" style="background:'+COL[st]+'"></span></div>'+
      '<div class="kpi-val" style="color:'+COL[st]+'">'+h.pre+'<span class="edit" data-edit="h'+i+'" style="width:'+(String(h.v).length+1)+'ch">'+h.v+'</span>'+h.unit+'</div>'+
      '<div class="kpi-tgt">obj '+(h.dir==="low"?"≤":"≥")+h.pre+h.target+h.unit+'</div>'+
      '<div class="kpi-bar"><i data-w="'+w+'" style="background:'+COL[st]+'"></i></div></div>';
  }).join("");
}
''')

add(r'''/* ===== RENDER: FUNNEL ===== */
function renderFunnel(){
  var steps=[],neck=null;
  for(var i=1;i<S.funnel.length;i++){
    var p=S.funnel[i-1].v,c=S.funnel[i];
    var conv=p>0?c.v/p*100:0, ratio=c.target>0?conv/c.target:1;
    var st=ratio>=0.97?"good":ratio>=0.85?"watch":"risk";
    var o={k:c.k,v:c.v,conv:conv,target:c.target,st:st,ratio:ratio,act:c.act,idx:i};
    steps.push(o);
  }
  neck=steps.reduce(function(a,b){return b.ratio<a.ratio?b:a;},steps[0]);
  var w=document.getElementById("fn-wrap");
  var html='<div class="fn-row"><div class="fn-lbl"><span class="fn-n">00</span>'+S.funnel[0].k+'</div>'+
    '<div class="fn-track"><div class="fn-fill" data-w="100" style="background:rgba(58,64,101,.55)"></div>'+
    '<span class="fn-v"><span class="edit" data-edit="f0" style="width:7ch">'+S.funnel[0].v+'</span></span></div>'+
    '<div class="fn-stat" style="color:var(--muted)">base 100%</div></div>';
  steps.forEach(function(s){
    var isN=s.k===neck.k;
    html+='<div class="fn-row'+(isN?" neck":"")+'"><div class="fn-lbl"><span class="fn-n">0'+s.idx+'</span>'+s.k+(isN?' <span class="neck-flag">cuello</span>':'')+'</div>'+
      '<div class="fn-track"><div class="fn-fill" data-w="'+Math.max(3,s.conv)+'" style="background:'+COL[s.st]+'"></div>'+
      '<div class="fn-obj" style="left:'+Math.min(99,s.target)+'%"></div>'+
      '<span class="fn-v"><span class="edit" data-edit="f'+s.idx+'" style="width:5ch">'+s.v+'</span></span></div>'+
      '<div class="fn-stat"><span style="color:'+COL[s.st]+';font-weight:700">'+Math.round(s.conv)+'%</span><span style="color:var(--muted)"> / '+s.target+'%</span></div></div>';
  });
  w.innerHTML=html;
  document.getElementById("fn-neck-txt").innerHTML='El paso <b style="color:var(--txt)">'+neck.k+'</b> convierte al '+Math.round(neck.conv)+'% vs '+neck.target+'% objetivo: la mayor brecha del funnel. Arréglalo antes de comprar más tráfico.';
  document.getElementById("fn-act").innerHTML='<b>Qué hacer:</b> '+(neck.act||"");
}
/* ===== RENDER: REVENUE ===== */
function mixBar(arr,id,legId){
  var tot=arr.reduce(function(s,x){return s+x.v;},0);
  document.getElementById(id).innerHTML=arr.map(function(x){var p=tot>0?x.v/tot*100:0;return '<div class="seg" style="width:0;background:'+x.c+'" data-w="'+p+'" title="'+x.k+'">'+(p>=12?Math.round(p)+"%":"")+'</div>';}).join("");
  document.getElementById(legId).innerHTML=arr.map(function(x){var p=tot>0?Math.round(x.v/tot*100):0;return '<div class="it"><span class="sw" style="background:'+x.c+'"></span>'+x.k+' <b>'+money(x.v)+'</b> &middot; '+p+'%</div>';}).join("");
  return tot;
}
function renderRevenue(){
  var t1=mixBar(S.mixNow,"mix-now","mix-now-leg");
  var t2=mixBar(S.mixTgt,"mix-tgt","mix-tgt-leg");
  document.getElementById("mix-now-tot").textContent=money(t1)+"";
  document.getElementById("mix-tgt-tot").textContent=money(t2)+"";
  var micro=S.mixNow.find(function(x){return x.k==="Microlearning";});
  document.getElementById("mrr-real").textContent=money(micro?micro.v:0);
}
''')

add(r'''/* ===== RENDER: AGENDA + WINS ===== */
function renderAgenda(){
  var done=S.agenda.filter(function(a){return a.d;}).length;
  var pct=Math.round(done/S.agenda.length*100);
  document.getElementById("agenda").innerHTML=S.agenda.map(function(a,i){
    return '<li class="ag-item" data-ag="'+i+'"><span class="ag-check'+(a.d?" dn":"")+'">'+(a.d?'<svg width="9" height="9" viewBox="0 0 9 9"><polyline points="1.5,4.5 3.5,6.5 7.5,2.5" stroke="#0E1121" stroke-width="1.8" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>':'')+'</span><span class="ag-n">'+String(i+1).padStart(2,"0")+'</span><span class="ag-txt'+(a.d?" dn":"")+'">'+a.t+'</span></li>';
  }).join("");
  document.getElementById("ag-bar").style.width=pct+"%";
  document.getElementById("ag-foot").textContent=done+"/"+S.agenda.length+" completados · "+pct+"% listo para levantar";
}
function renderWins(){
  var done=S.wins.filter(function(w){return w.d;}).length;
  document.getElementById("wins").innerHTML=S.wins.map(function(w,i){
    return '<div class="win-item"><div class="win-check'+(w.d?" dn":"")+'" data-win="'+i+'">'+(w.d?'<svg width="9" height="9" viewBox="0 0 9 9"><polyline points="1.5,4.5 3.5,6.5 7.5,2.5" stroke="#0E1121" stroke-width="1.8" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>':'')+'</div><div class="win-txt'+(w.d?" dn":"")+'">'+w.t+'</div><span class="win-del" data-del="'+i+'">&times;</span></div>';
  }).join("");
}
function addWin(){var inp=document.getElementById("win-new");var t=inp.value.trim();if(!t)return;S.wins.push({t:t,d:false});inp.value="";save();renderWins();bindWins();}
function bindWins(){
  document.querySelectorAll('[data-win]').forEach(function(el){el.onclick=function(){var i=+el.dataset.win;S.wins[i].d=!S.wins[i].d;save();renderWins();bindWins();};});
  document.querySelectorAll('[data-del]').forEach(function(el){el.onclick=function(){S.wins.splice(+el.dataset.del,1);save();renderWins();bindWins();};});
}
function bindAgenda(){
  document.querySelectorAll('[data-ag]').forEach(function(el){el.onclick=function(){var i=+el.dataset.ag;S.agenda[i].d=!S.agenda[i].d;save();renderAgenda();bindAgenda();};});
}
''')

add(r'''/* ===== EDIT BINDINGS ===== */
function bindEdits(){
  document.querySelectorAll('.edit').forEach(function(inp){
    inp.onchange=function(){
      var key=inp.dataset.edit, val=num(inp.value,undefined);
      if(val===undefined){renderAll();return;}
      if(key==="skills")S.star.skills=val;
      else if(key==="mau")S.star.mau=val;
      else if(key.charAt(0)==="h")S.health[+key.slice(1)].v=val;
      else if(key.charAt(0)==="f")S.funnel[+key.slice(1)].v=val;
      save();renderAll();
    };
    inp.onfocus=function(){inp.select();};
    inp.onkeydown=function(e){if(e.key==="Enter"){e.preventDefault();inp.blur();}};
  });
}
/* ===== MASTER RENDER ===== */
function renderAll(){
  var C=compute();
  renderVerdict(C);renderNorth(C);renderKPI();renderFunnel();renderRevenue();renderAgenda();renderWins();
  bindEdits();bindWins();bindAgenda();bindInfo();
  animateBars();
  firstPaint=false;
}
function animateBars(){
  requestAnimationFrame(function(){
    document.querySelectorAll('.kpi-bar i,.fn-fill,.seg,.out-bar i').forEach(function(b){if(b.dataset.w!==undefined)b.style.width=b.dataset.w+"%";});
  });
}
''')

add(r'''/* ===== SIMULATOR ===== */
var SIM={ids:["evid","verif","mau","conv","price"]};
function simGet(){return {evid:+document.getElementById("s-evid").value,verif:+document.getElementById("s-verif").value,mau:+document.getElementById("s-mau").value,conv:+document.getElementById("s-conv").value,price:+document.getElementById("s-price").value};}
function simCalc(p){
  var k=0.17/(0.42*0.69);
  var nsm=(p.evid/100)*(p.verif/100)*k;
  var plat=p.mau*(p.conv/100)*p.price;
  var total=plat+4297;
  var ltv=p.price*0.1069;
  var run=Math.max(3,Math.min(36,10+(total-5150)/800));
  return {nsm:nsm,plat:plat,total:total,ltv:ltv,run:run};
}
var BASE=simCalc(PRESETS.hoy);
function delta(now,base,suf,inv){
  var d=now-base;var s=d>=0?"+":"";var col=(inv?d<=0:d>=0)?"var(--good)":"var(--risk)";
  if(Math.abs(d)<0.0001)return '<span style="color:var(--muted)">= base</span>';
  return '<span style="color:'+col+'">'+s+(suf==="$"?money(d):suf==="x"?d.toFixed(2)+"x":d.toFixed(2)+(suf||""))+' vs hoy</span>';
}
function runSim(){
  var p=simGet(), r=simCalc(p);
  document.getElementById("sv-evid").textContent=p.evid+"%";
  document.getElementById("sv-verif").textContent=p.verif+"%";
  document.getElementById("sv-mau").textContent=fmt(p.mau);
  document.getElementById("sv-conv").textContent=p.conv+"%";
  document.getElementById("sv-price").textContent="$"+p.price;
  document.getElementById("o-nsm").textContent=r.nsm.toFixed(2);
  document.getElementById("o-plat").textContent=money(r.plat);
  document.getElementById("o-ltv").textContent=r.ltv.toFixed(1)+"x";
  document.getElementById("o-run").textContent=Math.round(r.run)+" mo";
  document.getElementById("od-nsm").innerHTML=delta(r.nsm,BASE.nsm,"");
  document.getElementById("od-plat").innerHTML=delta(r.plat,BASE.plat,"$");
  document.getElementById("od-ltv").innerHTML=delta(r.ltv,BASE.ltv,"x");
  document.getElementById("od-run").innerHTML=delta(r.run,BASE.run," mo");
  setBar("ob-nsm",r.nsm/0.40);setBar("ob-plat",r.plat/8000);setBar("ob-ltv",r.ltv/3);setBar("ob-run",r.run/15);
  /* verdict */
  var v,vc,ic,blocker;
  if(r.nsm<0.25){blocker="Tu NSM aún es bajo. Sube Evidence y Verification Rate: escalar usuarios no lo arregla.";}
  else if(r.ltv<3){blocker="LTV/CAC por debajo de 3x. Sube el precio Pro o reduce el CAC antes de levantar.";}
  else if(r.plat<8000){blocker="MRR plataforma todavía pequeño. Necesitas más MAU y conversión recurrente.";}
  else{blocker="Unit economics y NSM en zona sana: este escenario es defendible ante un inversionista.";}
  if(r.nsm>=0.36&&r.ltv>=3&&r.plat>=8000){v="Listo para levantar";vc="var(--good)";ic="🚀";}
  else if(r.nsm>=0.25&&r.ltv>=2.5){v="En preparación";vc="var(--watch)";ic="🔧";}
  else{v="Aún no financiable";vc="var(--risk)";ic="⚠️";}
  var sv=document.getElementById("sim-verdict");
  sv.style.borderColor=vc;sv.style.background="color-mix(in srgb,"+vc+" 9%,transparent)";
  document.getElementById("sv-icon").textContent=ic;
  document.getElementById("sv-icon").style.background="color-mix(in srgb,"+vc+" 16%,transparent)";
  var vt=document.getElementById("sv-verdict-t");vt.textContent=v;vt.style.color=vc;
  document.getElementById("sv-verdict-d").textContent="Escenario simulado · NSM "+r.nsm.toFixed(2)+" · "+money(r.plat)+" MRR plataforma";
  document.getElementById("sim-note-txt").innerHTML=blocker;
}
function setBar(id,ratio){var el=document.getElementById(id);if(el)el.style.width=Math.max(4,Math.min(100,ratio*100))+"%";}
function applyPreset(name){
  var p=PRESETS[name];if(!p)return;
  document.getElementById("s-evid").value=p.evid;document.getElementById("s-verif").value=p.verif;
  document.getElementById("s-mau").value=p.mau;document.getElementById("s-conv").value=p.conv;document.getElementById("s-price").value=p.price;
  document.querySelectorAll(".preset").forEach(function(b){b.classList.toggle("active",b.dataset.preset===name);});
  runSim();
}
function initSim(){
  SIM.ids.forEach(function(id){document.getElementById("s-"+id).addEventListener("input",function(){document.querySelectorAll(".preset").forEach(function(b){b.classList.remove("active");});runSim();});});
  document.querySelectorAll(".preset").forEach(function(b){b.onclick=function(){applyPreset(b.dataset.preset);};});
  runSim();
}
''')

add(r'''/* ===== INFO POPOVER ===== */
var popEl,popT,popD;
function bindInfo(){
  document.querySelectorAll('.info[data-info]').forEach(function(el){
    el.onclick=function(e){e.stopPropagation();showPop(el,el.dataset.info);};
  });
}
function showPop(el,key){
  var d=INFO[key];if(!d)return;
  popT.innerHTML=d[0];popD.innerHTML=d[1];
  popEl.classList.add("show");
  var r=el.getBoundingClientRect();
  var pw=popEl.offsetWidth,ph=popEl.offsetHeight;
  var left=Math.min(window.innerWidth-pw-12,Math.max(12,r.left-pw/2+r.width/2));
  var top=r.bottom+10; if(top+ph>window.innerHeight-12)top=r.top-ph-10;
  popEl.style.left=left+"px";popEl.style.top=Math.max(12,top)+"px";
}
function hidePop(){popEl.classList.remove("show");}
/* ===== TOUR ===== */
var TOUR=[
  {sel:"#north",t:"El Norte",d:"Todo arranca aquí. El North Star Metric mide progresión real. Si está en rojo, el resto del crecimiento es humo. Puedes editar skills y MAU haciendo click."},
  {sel:"#simulator",t:"El Simulador",d:"Arrastra los sliders y mira el impacto en vivo sobre NSM, MRR, LTV/CAC y el veredicto. Prueba los presets Hoy / Meta Beta / Escala 12m."},
  {sel:"#kpis",t:"Fundabilidad",d:"Las 8 métricas que mira un inversionista. Edita tus valores reales; el semáforo te dice qué bloquea tu ronda. Toca la (i) de cada una para entenderla."},
  {sel:"#funnel-sec",t:"El Funnel",d:"De comunidad a pago. El cuello de botella se detecta solo: es el paso con mayor brecha vs su objetivo. Arréglalo antes de comprar tráfico."},
  {sel:"#revenue",t:"Mix de Ingresos",d:"Hoy dependes de Live (no recurrente). La apuesta es migrar a 60% Microlearning recurrente. Eso es lo que un fondo quiere ver."},
  {sel:"#readiness",t:"Agenda de Readiness",d:"Los 10 puntos para estar listo. Márcalos y mira tu progreso. A la derecha, tus quick wins de la semana."},
  {sel:"#interpret",t:"Cómo interpretarlo",d:"Una guía de 6 pasos para leer el cockpit como un operador. Y recuerda: todo se guarda solo en tu navegador. ¡Listo para volar!"}
];
var tourI=0;
function startTour(){tourI=0;showTourStep();}
function showTourStep(){
  document.querySelectorAll(".tour-hl").forEach(function(e){e.classList.remove("tour-hl");});
  var s=TOUR[tourI], el=document.querySelector(s.sel);
  if(el){el.classList.add("tour-hl");el.scrollIntoView({behavior:"smooth",block:"center"});}
  document.getElementById("tour-t").textContent=s.t;
  document.getElementById("tour-d").textContent=s.d;
  document.getElementById("tour-step").textContent=(tourI+1)+" / "+TOUR.length;
  document.getElementById("tour-prev").style.visibility=tourI===0?"hidden":"visible";
  document.getElementById("tour-next").textContent=tourI===TOUR.length-1?"Terminar":"Siguiente";
  document.getElementById("tour-box").classList.add("show");
}
function tourNext(){if(tourI>=TOUR.length-1){endTour();return;}tourI++;showTourStep();}
function tourPrev(){if(tourI>0){tourI--;showTourStep();}}
function endTour(){document.querySelectorAll(".tour-hl").forEach(function(e){e.classList.remove("tour-hl");});document.getElementById("tour-box").classList.remove("show");}
''')

add(r'''/* ===== TOOLS: EXPORT/IMPORT/RESET ===== */
function doExport(){
  var b=new Blob([JSON.stringify(S,null,2)],{type:"application/json"});
  var u=URL.createObjectURL(b),a=document.createElement("a");
  a.href=u;a.download="aecode-cockpit-"+new Date().toISOString().slice(0,10)+".json";a.click();URL.revokeObjectURL(u);
  toast("Datos exportados");
}
document.addEventListener("DOMContentLoaded",function(){
  var imp=document.getElementById("imp");
  if(imp)imp.addEventListener("change",function(e){
    var f=e.target.files[0];if(!f)return;var r=new FileReader();
    r.onload=function(){try{S=merge(JSON.parse(r.result));save();firstPaint=true;renderAll();toast("Datos importados");}catch(err){toast("Archivo no válido");}};
    r.readAsText(f);
  });
});
function doReset(){if(confirm("¿Volver a los valores semilla? Se perderán tus cambios.")){S=clone(SEED);save();firstPaint=true;renderAll();applyPreset("hoy");toast("Restablecido");}}
/* ===== TOAST ===== */
var toastT;
function toast(m){var el=document.getElementById("toast");el.textContent=m;el.classList.add("show");clearTimeout(toastT);toastT=setTimeout(function(){el.classList.remove("show");},2200);}
/* ===== NAV / SCROLL / REVEAL / PARTICLES ===== */
function initNav(){
  var bar=document.getElementById("bar");
  window.addEventListener("scroll",function(){bar.classList.toggle("scrolled",window.scrollY>40);var sb=document.getElementById("scroll-bar");sb.style.width=(window.scrollY/(document.body.scrollHeight-window.innerHeight)*100)+"%";},{passive:true});
  document.querySelectorAll(".pill").forEach(function(p){p.onclick=function(){var t=document.getElementById(p.dataset.sec);if(t)t.scrollIntoView({behavior:"smooth"});};});
  var secs=["north","simulator","kpis","funnel-sec","revenue","readiness","interpret"];
  var so=new IntersectionObserver(function(en){en.forEach(function(e){if(e.isIntersecting){document.querySelectorAll(".pill").forEach(function(p){p.classList.toggle("active",p.dataset.sec===e.target.id);});}});},{rootMargin:"-45% 0px -50% 0px"});
  secs.forEach(function(id){var el=document.getElementById(id);if(el)so.observe(el);});
}
function initReveal(){
  var o=new IntersectionObserver(function(en){en.forEach(function(e){if(e.isIntersecting){e.target.classList.add("in");o.unobserve(e.target);}});},{threshold:.08,rootMargin:"0px 0px -30px 0px"});
  document.querySelectorAll(".reveal").forEach(function(el,i){el.style.transitionDelay=Math.min(i*0.05,0.35)+"s";o.observe(el);});
}
function initParticles(){
  var c=document.getElementById("bg-canvas");if(!c||window.matchMedia("(prefers-reduced-motion:reduce)").matches)return;
  var ctx=c.getContext("2d"),W,H,pts,N=52,D=135,M={x:-9999,y:-9999};
  function rs(){W=c.width=window.innerWidth;H=c.height=window.innerHeight;}
  function mk(){return{x:Math.random()*W,y:Math.random()*H,vx:(Math.random()-.5)*.3,vy:(Math.random()-.5)*.3,r:Math.random()*1.3+.5};}
  function init(){rs();pts=[];for(var i=0;i<N;i++)pts.push(mk());}
  function loop(){
    ctx.clearRect(0,0,W,H);
    for(var i=0;i<pts.length;i++){var p=pts[i];p.x+=p.vx;p.y+=p.vy;if(p.x<0||p.x>W)p.vx*=-1;if(p.y<0||p.y>H)p.vy*=-1;var dx=p.x-M.x,dy=p.y-M.y,dd=Math.sqrt(dx*dx+dy*dy);if(dd<90){p.vx+=dx/dd*.03;p.vy+=dy/dd*.03;}ctx.beginPath();ctx.arc(p.x,p.y,p.r,0,Math.PI*2);ctx.fillStyle="rgba(124,126,223,.18)";ctx.fill();}
    for(var a=0;a<pts.length;a++)for(var b=a+1;b<pts.length;b++){var ex=pts[a].x-pts[b].x,ey=pts[a].y-pts[b].y,d=Math.sqrt(ex*ex+ey*ey);if(d<D){ctx.beginPath();ctx.moveTo(pts[a].x,pts[a].y);ctx.lineTo(pts[b].x,pts[b].y);ctx.strokeStyle="rgba(74,58,193,"+(.1*(1-d/D))+")";ctx.lineWidth=.65;ctx.stroke();}}
    requestAnimationFrame(loop);
  }
  window.addEventListener("resize",init);window.addEventListener("mousemove",function(e){M.x=e.clientX;M.y=e.clientY;},{passive:true});init();loop();
}
/* ===== BOOT ===== */
function boot(){
  popEl=document.getElementById("popover");popT=document.getElementById("pop-t");popD=document.getElementById("pop-d");
  S=load();
  document.getElementById("foco").value=S.meta.foco||"";
  document.getElementById("foco").addEventListener("input",function(e){S.meta.foco=e.target.value;save();});
  stamp();
  renderAll();initSim();initNav();initReveal();initParticles();
  document.addEventListener("click",function(){hidePop();});
  document.addEventListener("keydown",function(e){if(e.key==="Escape"){hidePop();endTour();}});
  /* hero entrance */
  if(typeof anime!=="undefined"){
    anime({targets:"#bar",translateY:[-20,0],opacity:[0,1],duration:550,easing:"easeOutCubic"});
  }
}
if(document.readyState==="loading")document.addEventListener("DOMContentLoaded",boot);else boot();
</script>
</body>
</html>
''')

# ============================ WRITE FILE ============================
html = "".join(P)
with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
print("OK index.html written:", len(html), "chars (", round(len(html)/1024), "KB )")
