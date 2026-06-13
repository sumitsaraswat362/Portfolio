import re

with open('/Users/sumitsaraswat/Portfolio/SumitSaraswat_CV_Academy.html', 'r') as f:
    html = f.read()

# 1. Update CSS Font Sizes
css_replacements = {
    r'\.summary \{\s*font-size: 10\.5px;': '.summary {\n      font-size: 11px;',
    r'\.header-right \{\s*text-align: right;\s*font-size: 10\.5px;': '.header-right {\n      text-align: right;\n      font-size: 11px;',
    r'\.item-title \{\s*font-size: 11\.5px;': '.item-title {\n      font-size: 12px;',
    r'\.edu-title \{\s*font-size: 11\.5px;': '.edu-title {\n      font-size: 12px;',
    r'\.item-desc \{\s*font-size: 10px;': '.item-desc {\n      font-size: 10.5px;',
    r'\.item-sub \{\s*font-size: 10px;': '.item-sub {\n      font-size: 10.5px;',
    r'\.edu-date \{\s*font-size: 10px;': '.edu-date {\n      font-size: 10.5px;',
    r'\.edu-sub \{\s*font-size: 10px;': '.edu-sub {\n      font-size: 10.5px;',
    r'\.section-title \{\s*font-size: 10px;': '.section-title {\n      font-size: 10.5px;',
    r'\.award-item \{\s*display: flex;\s*gap: 6px;\s*align-items: baseline;\s*margin-bottom: 3px;\s*font-size: 10px;': '.award-item {\n      display: flex;\n      gap: 6px;\n      align-items: baseline;\n      margin-bottom: 3px;\n      font-size: 10.5px;',
    r'\.item-badge \{\s*font-size: 9px;': '.item-badge {\n      font-size: 9.5px;',
    r'\.footer \{\s*position: absolute;\s*bottom: 10mm;\s*left: 16mm;\s*right: 16mm;\s*display: flex;\s*justify-content: space-between;\s*align-items: center;\s*font-size: 9px;': '.footer {\n      position: absolute;\n      bottom: 10mm;\n      left: 16mm;\n      right: 16mm;\n      display: flex;\n      justify-content: space-between;\n      align-items: center;\n      font-size: 9.5px;',
    r'\.project-links \{\s*margin-top: 2px;\s*font-size: 9\.5px;': '.project-links {\n      margin-top: 2px;\n      font-size: 10px;',
    r'\.skill-pill \{\s*font-size: 9\.5px;': '.skill-pill {\n      font-size: 10px;'
}

for pattern, replacement in css_replacements.items():
    html = re.sub(pattern, replacement, html)


# 2. Extract and Replace Projects
# Split at Selected Projects
parts = html.split('<h2 class="section-title">Selected Projects</h2>')
if len(parts) == 2:
    header = parts[0] + '<h2 class="section-title">Selected Projects</h2>\n'
    rest = parts[1]
    
    # Isolate the CrisisGuard and EcoNudge
    eco_split = rest.split('<!-- Clinical Trial Auditor -->')
    first_two_projects = eco_split[0]
    remainder = eco_split[1]
    
    # Isolate MedSafe AI
    medsafe_split = remainder.split('<!-- MedSafe AI -->')
    meta_projects_html = medsafe_split[0]
    medsafe_and_rest = '<!-- MedSafe AI -->' + medsafe_split[1]
    
    annapurna_html = """
      <!-- Annapurna -->
      <div class="item">
        <div class="item-row">
          <span class="item-title">Annapurna — Autonomous Cold-Chain Logistics AI</span>
          <span class="item-badge team">TEAM PROJECT</span>
        </div>
        <div class="item-sub">AI Architect & Full-Stack Lead</div>
        <div class="item-desc">
          <ul>
            <li>Engineered an Edge-AI powered platform that actively detects refrigeration failures in transit and autonomously reroutes perishable cargo via an intelligent distress marketplace to prevent food waste.</li>
            <li>Built the frontend using Next.js, integrated with a Supabase backend and LoRaWAN IoT fallbacks, ensuring continuous temperature tracking even in zero-connectivity dead zones.</li>
          </ul>
        </div>
        <div class="project-links"><a href="https://annapurna-alpha.vercel.app">↗ Visit Site</a><a href="https://github.com/sumitsaraswat362/Annapurna">⌘ GitHub</a></div>
      </div>
"""

    merged_meta_html = """
      <!-- SynthAudit & Clinical Trial Auditor -->
      <div class="item">
        <div class="item-row">
          <span class="item-title">SynthAudit & Clinical Trial Auditor — AI Agent for Protocol Triage</span>
          <span class="item-badge">META HACKATHON FINALIST</span>
        </div>
        <div class="item-desc">
          <ul>
            <li>Built an autonomous RL environment where AI agents learn to triage clinical protocol deviations. Engineered a benchmark so rigorous that <strong>Meta's Llama 3.1 405B scored only 0.34/1</strong>.</li>
            <li>Cleared Round 1 against <strong>32,000+ teams</strong> and trained a custom model that <strong>increased performance by 283%</strong>, securing a spot in the Top 100 National Finals as the <strong>only solo freshman</strong>.</li>
          </ul>
        </div>
        <div class="project-links"><a href="https://github.com/sumitsaraswat362/clinical-trial-auditor">⌘ GitHub</a> <a href="https://drive.google.com/file/d/1Xh1TJI66z11OKxwj2l7xOEci9D-SREj6/view?usp=share_link">[National Finalist Certificate]</a></div>
      </div>
"""

    new_html = header + annapurna_html + first_two_projects + merged_meta_html + medsafe_and_rest
    
    with open('/Users/sumitsaraswat/Portfolio/SumitSaraswat_CV_Academy.html', 'w') as f:
        f.write(new_html)
    print("CV Updated Successfully.")
else:
    print("Failed to find Selected Projects section")
