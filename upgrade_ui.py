import re

with open('/Users/sumitsaraswat/Portfolio/SumitSaraswat_Portfolio_Academy.html', 'r') as f:
    html = f.read()

# 1. New ultra-premium CSS
new_css = """
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');
    
    :root {
      --bg: #07090f;
      --surface: rgba(20, 25, 35, 0.45);
      --surface-light: rgba(255, 255, 255, 0.05);
      --text-main: #f5f5f7;
      --text-muted: #a1a1a6;
      --accent: #00ffae;
      --border: rgba(255, 255, 255, 0.08);
      --clay-shadow: 10px 20px 40px rgba(0, 0, 0, 0.6), inset 2px 2px 5px rgba(255, 255, 255, 0.1), inset -2px -2px 5px rgba(0, 0, 0, 0.5);
    }

    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      font-family: 'Inter', -apple-system, sans-serif;
      background: var(--bg);
      color: var(--text-main);
      line-height: 1.5;
      -webkit-font-smoothing: antialiased;
    }

    /* A4 Landscape Page Setup */
    .page {
      width: 297mm;
      height: 210mm;
      background: radial-gradient(circle at top right, #11261d 0%, #07090f 50%, #030408 100%);
      margin: 20px auto;
      box-shadow: 0 20px 50px rgba(0,0,0,0.8);
      position: relative;
      overflow: hidden;
      page-break-after: always;
      display: flex;
    }

    @media print {
      body { background: var(--bg); margin: 0; -webkit-print-color-adjust: exact; print-color-adjust: exact; }
      .page { margin: 0; box-shadow: none; page-break-after: always; }
      @page { size: A4 landscape; margin: 0; }
    }

    /* --- Layout Columns --- */
    .image-col {
      width: 55%;
      padding: 15mm 10mm 15mm 20mm;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      perspective: 1000px;
    }
    .content-col {
      width: 45%;
      padding: 15mm 20mm 15mm 10mm;
      display: flex;
      flex-direction: column;
      justify-content: center;
    }

    /* --- macOS Window Wrapper --- */
    .macos-window {
      width: 100%;
      border-radius: 16px;
      background: rgba(30, 30, 35, 0.7);
      backdrop-filter: blur(20px);
      -webkit-backdrop-filter: blur(20px);
      border: 1px solid rgba(255, 255, 255, 0.15);
      box-shadow: var(--clay-shadow);
      overflow: hidden;
      display: flex;
      flex-direction: column;
      transform: rotateX(2deg) rotateY(-2deg); /* Subtle 3D tilt */
      transition: transform 0.3s ease;
    }
    .macos-window:hover {
      transform: rotateX(0deg) rotateY(0deg);
    }
    
    .titlebar {
      height: 28px;
      background: linear-gradient(180deg, rgba(255,255,255,0.1) 0%, rgba(255,255,255,0.02) 100%);
      border-bottom: 1px solid rgba(0,0,0,0.5);
      display: flex;
      align-items: center;
      padding: 0 12px;
      gap: 6px;
    }
    .buttons div {
      width: 10px;
      height: 10px;
      border-radius: 50%;
      display: inline-block;
    }
    .close { background: #ff5f56; border: 1px solid #e0443e; }
    .minimize { background: #ffbd2e; border: 1px solid #dea123; }
    .zoom { background: #27c93f; border: 1px solid #1aab29; }
    
    .window-content {
      background: #000;
      display: flex;
      justify-content: center;
      align-items: center;
      padding: 0;
    }

    .img-contain-landscape, .img-cert {
      width: 100%;
      height: auto;
      display: block;
      object-fit: cover;
    }

    /* --- Cover Page --- */
    .cover {
      flex-direction: row;
      align-items: center;
      justify-content: space-between;
      padding: 0 30mm;
    }
    .cover-left { width: 60%; }
    .cover-right { width: 35%; display: flex; justify-content: flex-end; }
    
    .cover-title { 
      font-size: 68px; 
      font-weight: 900; 
      letter-spacing: -0.04em; 
      margin-bottom: 5px; 
      line-height: 1.1; 
      background: linear-gradient(135deg, #ffffff 0%, #a1a1a6 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }
    .cover-subtitle { font-size: 20px; font-weight: 600; color: var(--accent); margin-bottom: 25px; }
    .cover-academy { font-size: 14px; font-weight: 800; color: white; text-transform: uppercase; letter-spacing: 3px; margin-bottom: 10px; opacity: 0.9; }
    
    .social-links { display: flex; gap: 20px; margin-top: 30px; }
    .social-links a { display: flex; align-items: center; gap: 8px; color: var(--text-main); text-decoration: none; font-size: 14px; font-weight: 600; transition: color 0.2s; }
    .social-links svg { width: 24px; height: 24px; fill: currentColor; }
    
    .photo-wrapper {
      width: 190px;
      height: 190px;
      border-radius: 50%;
      padding: 5px;
      background: linear-gradient(135deg, var(--accent), #0080ff);
      box-shadow: 0 0 60px rgba(0,255,174,0.3), inset 2px 2px 10px rgba(255,255,255,0.5);
    }
    .photo-wrapper img {
      width: 100%;
      height: 100%;
      border-radius: 50%;
      object-fit: cover;
      border: 5px solid #050505;
    }

    /* --- Project Pages Text --- */
    .project-header { margin-bottom: 12px; }
    .project-title { 
      font-size: 30px; 
      font-weight: 800; 
      letter-spacing: -0.03em; 
      color: white; 
      line-height: 1.15;
      text-shadow: 0 2px 10px rgba(0,0,0,0.5);
    }
    .project-summary { font-size: 14px; font-weight: 500; color: var(--text-muted); margin-top: 6px; line-height: 1.4; }
    
    .meta-grid {
      display: flex;
      gap: 15px;
      margin-bottom: 15px;
      padding: 10px 14px;
      background: var(--surface);
      border-radius: 12px;
      border: 1px solid var(--border);
      backdrop-filter: blur(20px);
      -webkit-backdrop-filter: blur(20px);
      box-shadow: inset 1px 1px 2px rgba(255,255,255,0.05), 0 4px 15px rgba(0,0,0,0.3);
    }
    .meta-item { display: flex; flex-direction: column; }
    .meta-label { font-size: 10px; font-weight: 800; color: var(--accent); text-transform: uppercase; letter-spacing: 1.5px; margin-bottom: 2px; }
    .meta-value { font-size: 12px; font-weight: 600; color: var(--text-main); }

    .section-title { font-size: 11px; font-weight: 800; color: var(--text-main); margin-bottom: 6px; margin-top: 14px; text-transform: uppercase; letter-spacing: 1.5px; opacity: 0.8;}
    .content-text { 
      font-size: 12px; 
      color: var(--text-muted); 
      text-align: left; 
      line-height: 1.6; 
      background: rgba(255,255,255,0.02);
      padding: 10px 12px;
      border-radius: 8px;
      border: 1px solid rgba(255,255,255,0.05);
    }
    .content-text strong { color: white; font-weight: 700; }

    .links { margin-top: 18px; display: flex; flex-wrap: wrap; gap: 12px; }
    .link-item { 
      display: inline-flex; align-items: center; gap: 6px;
      font-size: 11px; font-weight: 800; color: var(--bg); 
      background: linear-gradient(180deg, #ffffff 0%, #e0e0e0 100%);
      padding: 8px 16px; border-radius: 100px; 
      text-decoration: none;
      box-shadow: 0 4px 10px rgba(255,255,255,0.2), inset 0 1px 0 rgba(255,255,255,0.8);
    }
    .link-item.secondary {
      background: var(--surface);
      color: var(--text-main);
      border: 1px solid var(--border);
      box-shadow: 0 4px 10px rgba(0,0,0,0.5), inset 0 1px 0 rgba(255,255,255,0.1);
    }

    .page-number { position: absolute; bottom: 12mm; left: 20mm; font-size: 10px; color: rgba(255,255,255,0.4); font-weight: 800; letter-spacing: 2px; text-transform: uppercase; }
    .decor-line { position: absolute; top: 0; left: 0; width: 100%; height: 5px; background: linear-gradient(90deg, var(--accent), #0080ff, #ff007a); }
  </style>
"""

# Replace the existing style block
html = re.sub(r'<style>.*?</style>', new_css, html, flags=re.DOTALL)

# 2. Wrap all project images in the macOS window
window_html = """
<div class="macos-window">
  <div class="titlebar">
    <div class="buttons">
      <div class="close"></div>
      <div class="minimize"></div>
      <div class="zoom"></div>
    </div>
  </div>
  <div class="window-content">
    \g<0>
  </div>
</div>
"""

# Find the images for Meta, EcoNudge, Annapurna, CrisisGuard, MedSafe and replace them with wrapped version
# We specifically target img tags that have class="img-contain-landscape" or class="img-cert"
html = re.sub(r'<img[^>]+class="(img-contain-landscape|img-cert)"[^>]*>', window_html, html)

with open('/Users/sumitsaraswat/Portfolio/SumitSaraswat_Portfolio_Academy.html', 'w') as f:
    f.write(html)

print("UI upgraded successfully.")
